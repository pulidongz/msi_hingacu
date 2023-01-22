import io, os
from django.conf import settings
from django.core.validators import URLValidator
from googleapiclient import discovery
from googleapiclient.http import MediaIoBaseDownload
from httplib2 import Http
from oauth2client import file, client, tools
from etl.models import GoogleDriveFile


class GoogleDrive:

    def __init__(self):
        self.store = file.Storage(settings.GDRIVE_OAUTH_STORAGE)
        self.creds = self.store.get()
        if not self.creds or self.creds.invalid:
            flow = client.flow_from_clientsecrets(settings.GDRIVE_OAUTH_CLIENT, settings.GDRIVE_SCOPES)
            self.creds = tools.run_flow(flow, self.store)
        self.DRIVE = discovery.build('drive', 'v3', http=self.creds.authorize(Http()))

    def print_file_list(self):
        files = self.DRIVE.files().list().execute().get('files', [])
        for f in files:
            print(f['name'], f['mimeType'])

    def download(self, drive_url, folder='drive'):
        # create django file
        gfile, created = GoogleDriveFile.objects.get_or_create(
            drive_url=drive_url
        )

        if gfile.downloaded:
            print("Skipping. File already downloaded.", drive_url)
            return gfile

        # parse drive id
        drive_id = None
        if 'id=' in drive_url:
            drive_id = drive_url.split('id=')[1].split('&')[0]
        elif '/file/d/' in drive_url:
            drive_id = drive_url.split('/file/d/')[1].split('/')[0]
        else:
            # failed to get ID
            return

        # get file metadata
        file = self.DRIVE.files().get(fileId=drive_id).execute()

        # download file
        request = self.DRIVE.files().get_media(fileId=drive_id)
        file_name = file['name']
        folder_path = os.path.join(settings.MEDIA_ROOT, 'files', folder)
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, file_name)
        fh = io.FileIO(file_path, 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(file_path)
            print("Download %d%%." % int(status.progress() * 100))

        # associate file to django model
        gfile.drive_id = drive_id
        gfile.downloaded = True
        gfile.file.name = os.path.relpath(file_path, settings.MEDIA_ROOT)
        gfile.save()

        return gfile
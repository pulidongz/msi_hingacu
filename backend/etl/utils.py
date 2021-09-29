import datetime, io, shutil, os
import unicodedata, re, itertools, sys
from django.conf import settings


all_chars = (chr(i) for i in range(sys.maxunicode))
categories = {'Cc'}
# or equivalently and much more efficiently
control_chars = ''.join(map(chr, itertools.chain(range(0x00,0x20), range(0x7f,0xa0))))
control_char_re = re.compile('[%s]' % re.escape(control_chars))

def remove_control_chars(s):
    return control_char_re.sub('', s)

def get_printable(string):
    #return printable only text
    new_string = string.strip()
    normalized = unicodedata.normalize("NFKD", new_string)
    return normalized


def convert_to_datetime(date_string):
    try:
        return datetime.datetime.strptime(date_string, '%m/%d/%Y')
    except ValueError:
        pass
    try:
        return datetime.datetime.strptime(date_string, '%Y%m%d')
    except ValueError:
        pass
    return None


def get_column_name_index(column_names):
    """
    given the first row of a csv, return a key value mapping for column name and column number
    """
    column_names = list(filter(None, column_names))
    #if settings.DEBUG:
        #print("COLUMNS", column_names)
    #map each column name to their list ordering number AND convert column names to lower case and filter out non-printable characters
    #map each column name to their list ordering number
    mapping = {column_names[i].strip(): i for i in range(0, len(column_names))}
    if settings.DEBUG:
        print("COLUMNS", column_names)
        print("MAPPING", mapping)
    return mapping

def convert_row_to_dict(row, column_names):
    """
    Given a row map each value to it's corresponding column name in lower case.
    """
    data = {}
    for i in range(len(column_names)):
        column_name = column_names[i].strip().lower()
        data[column_name] = row[i]
    return data


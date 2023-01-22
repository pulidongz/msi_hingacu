from django.db import models
from django.contrib.auth.models import User
from etl.models import TimeStampModel, Workbook


class Curator(TimeStampModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


#monkey patch user model to have a is_curator method
def is_curator(self):
    #if self.is_staff:
    #    return True
    return Curator.objects.filter(user=self).exists()
User.add_to_class("is_curator", is_curator)


class Curation(TimeStampModel):
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'
    STATUS_CHOICES = (
        (STATUS_APPROVED, 'Approved'),
        (STATUS_REJECTED, 'Rejected'),
    )

    workbook = models.ForeignKey(Workbook, on_delete=models.CASCADE)
    verdict = models.CharField(max_length=30, choices=STATUS_CHOICES)
    verdict_by =  models.ForeignKey(Curator, null=True, blank=True, on_delete=models.SET_NULL)
    reason = models.TextField()


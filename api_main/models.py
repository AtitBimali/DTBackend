from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TYPE_CHOICES = (
    ('event','Event'),
)

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created"]


class Event(TimeStampedModel):
    type = models.CharField(max_length=50,choices=TYPE_CHOICES,default='event')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='added_by',null=True,blank=True)
    name = models.CharField(max_length=255)
    tagline = models.CharField(max_length=300)
    schedule = models.DateTimeField()
    description = models.TextField()
    image = models.ImageField(null=True,blank=True)
    moderator = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='moderator')
    category = models.CharField(max_length=255)
    sub_category = models.CharField(max_length=255)
    rigor_rank = models.IntegerField()
    attendees = models.ManyToManyField(User,blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.type} -- {self.name}"


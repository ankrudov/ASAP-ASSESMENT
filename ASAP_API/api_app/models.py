from django.db import models
import uuid

class Member(models.Model):
    member_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=60)
from __future__ import unicode_literals

from django.db import models

from ..user_reg.models import User

class Course(models.Model):
	courselinks=models.ManyToManyField(User, related_name="courselinks")
	name = models.CharField(max_length=45)
	description = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add = True)
from django.db import models
import datetime

from django.db import models
from django.utils import timezone

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password=models.CharField(max_length=512)
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=False, editable=False)

class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=30)


class Permissions(models.Model):
    permission_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    description=models.TextField()


class TokenUsers(models.Model):
    user = models.ForeignKey(Users)
    token = models.CharField(max_length=512)
    created = models.DateTimeField(auto_now_add=False, editable=False)
    expired=models.BooleanField

class UserRoles(models.Model):
    user=models.ForeignKey(Users)
    role=models.ForeignKey(Roles)

class PermissionsRoles(models.Model):
    permission=models.ForeignKey(Permissions)
    role=models.ForeignKey(Roles)



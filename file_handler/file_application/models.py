from django.db import models
from django.contrib.auth.models import User

class Folder(models.Model):
    '''This model is used for creating folder table into database'''
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    f_name = models.CharField(max_length = 200, unique=True)
    deleted = models.BooleanField(default = False)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.user.username + self.f_name

def upload_path_fun(inst, filename):
    '''This function is used for providing path for uploading file'''
    if inst.parent_folder != None:
        return f'{inst.user.username.replace(" ","_")}/{inst.parent_folder.f_name.replace(" ","_")}/{filename}'
    return f'{inst.user.username.replace(" ","_")}/{filename}'

class Files(models.Model):
    '''This model is used for creating files table into database'''
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    parent_folder = models.ForeignKey(Folder, on_delete = models.SET_NULL, blank=True, null=True)
    file_name = models.CharField(max_length = 200)
    file = models.FileField(upload_to = upload_path_fun )
    deleted = models.BooleanField(default = False)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.user.username + self.file_name
from django.contrib import admin
from .models import *

#register models so that we can view in django default admin pannel
admin.site.register([Files, Folder])
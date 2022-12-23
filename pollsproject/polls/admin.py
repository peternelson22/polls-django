from django.contrib import admin
from .models import *


admin.site.site_header = 'Nelson Polls'


admin.site.register(Question)
admin.site.register(Choice)
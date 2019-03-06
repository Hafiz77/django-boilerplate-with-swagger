from django.contrib import admin
from app_dir.polls.models import Choice
from django.contrib.auth.models import User
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.

admin.site.site_header = "SWAGGER_TEST"
admin.site.site_title = "SWAGGER_TEST"
admin.site.index_title = "SWAGGER_TEST"

admin.site.register(Choice, SimpleHistoryAdmin)

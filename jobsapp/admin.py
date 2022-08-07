from django.contrib import admin
from .models import Contact
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
# from django.contrib.auth.models import User

# Register your models here.
from jobsapp.models import Job
admin.site.register(Contact)
# admin.site.register(User)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "salary",
        "location",
        "type",
        "category",
        "company_name",
        "last_date",
        "created_at",
        "filled",
        "user",
    ]
    list_filter = ["salary", "last_date", "created_at", "user"]
    date_hierarchy = "created_at"

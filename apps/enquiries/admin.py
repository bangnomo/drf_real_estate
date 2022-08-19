from django.contrib import admin

from .models import Enquiry

# Register your models here.


class EnquiryAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone_number", "message"]
    list_filter = ["name", "email", "phone_number"]


admin.site.register(Enquiry, EnquiryAdmin)

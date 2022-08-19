from django.urls import path

from . import views

urlpatterns = [path("send/", views.send_enquiry_email, name="send-enquiry")]

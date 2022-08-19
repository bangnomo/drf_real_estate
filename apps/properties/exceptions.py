from rest_framework.exceptions import APIException


# https://www.django-rest-framework.org/api-guide/exceptions/#apiexception
class PropertyNotFound(APIException):
    status_code = 404
    default_detail = "The requested property does not exists"

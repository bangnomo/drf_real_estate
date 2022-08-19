from django.urls import include, path

from .views import (ListAgentsPropertyAPIView, ListAllPropertyAPIView,
                    PropertyDetailView, PropertySearchAPIView,
                    PropertyViewsAPIView, create_property_api_view,
                    delete_property_api_view, update_property_api_view,
                    uploadPropertyImage)

urlpatterns = [
    path("all/", ListAgentsPropertyAPIView.as_view(), name="all-properties"),
    path(
        "agent-properties/",
        ListAgentsPropertyAPIView.as_view(),
        name="agent-properties",
    ),
    path("create/", create_property_api_view, name="create-property"),
    path("details/<slug:slug>/", PropertyDetailView.as_view(), name="property-details"),
    path("update/<slug:slug>/", update_property_api_view, name="update-property"),
    path("delete/<slug:slug>/", delete_property_api_view, name="delete-property"),
    path("search/", PropertySearchAPIView.as_view(), name="property-search"),
]

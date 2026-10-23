from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from admin_api import views

# Create a router
router = routers.DefaultRouter()

# Register API endpoints
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

# Define URL patterns
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
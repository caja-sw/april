from django.contrib import admin
from django.urls import path

from main import views
from memo import views as memo_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("memo/", memo_views.memo, name="memo"),
    path("memo/create/", memo_views.memo_create, name="memo_create"),
    path("memo/delete/<int:pk>/", memo_views.memo_delete, name="memo_delete"),
]

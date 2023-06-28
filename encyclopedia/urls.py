from django.urls import path
from . import util
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:pk>/', views.entries, name="entries"),
    path("create-page/", views.createPage, name="create-page"),
    path('edit-page/<str:pk>/', views.editPage, name="edit-page"),
    path('random-page/', views.randomPage, name="random-page")
]
urlpatterns += staticfiles_urlpatterns()

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="HomePage" ),
    path("contact", views.contact, name="ContactPage" ),
    path("ml", views.ml_page, name="MlPage" )
]
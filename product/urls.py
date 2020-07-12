from . import views
from django.urls import path
urlpatterns = [
    path('',views.report, name="report"),

]
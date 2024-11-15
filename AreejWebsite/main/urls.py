from . import views
from django.urls import path

app_name="main"

urlpatterns=[
    path("",views.home_view,name="home_view"),
    path("<str:filter_choice>",views.home_view_filter,name="home_view_filter"),
    path("contact/",views.contact_view,name="contact_view"),
]
from . import views
from django.urls import path

app_name="dashboard"

urlpatterns=[
    path("",views.dashboard_view,name="dashboard_view"),
    path("messages/",views.messages_view,name="messages_view"),
    path("messages/<int:message_id>/read/",views.read_message_view,name="read_message_view"),
    path('messages/<int:message_id>/delete/', views.delete_message_view, name='delete_message_view'),
    path("interests/",views.interests_view,name="interests_view"),
    path("interests/add/",views.add_interest_view,name="add_interest_view"),
    path('interests/<int:interest_id>/delete/', views.delete_interest_view, name='delete_interest_view'),
    path('interests/<int:interest_id>/update/', views.update_interest_view, name='update_interest_view'),
    path("projects/",views.projects_view,name="projects_view"),
    path("projects/add/",views.add_project_view,name="add_project_view"),
    path('projects/<int:project_id>/delete/', views.delete_project_view, name='delete_project_view'),
    path('projects/<int:project_id>/update/', views.update_project_view, name='update_project_view'),
    path("memories/",views.memories_view,name="memories_view"),
    path("memories/add/",views.add_memo_view,name="add_memo_view"),
    path('memories/<int:memo_id>/delete/', views.delete_memo_view, name='delete_memo_view'),
    path('memories/<int:memo_id>/update/', views.update_memo_view, name='update_memo_view'),
    
]
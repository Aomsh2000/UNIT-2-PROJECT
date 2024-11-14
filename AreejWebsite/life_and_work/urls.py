from . import views
from django.urls import path

app_name="life_and_work"

urlpatterns=[
    path('career/',views.career_view,name="career_view"),
    path('freespace/',views.freespace_view,name="freespace_view"),
    path('freespace/<int:interest_id>/interestdetail/',views.interest_detail_view,name="interest_detail_view"),
    path('freespace/<int:memo_id>/memodetail/',views.memo_detail_view,name="memo_detail_view"),
    path('freespace/<int:project_id>/projectdetail/',views.project_detail_view,name="project_detail_view"),

]
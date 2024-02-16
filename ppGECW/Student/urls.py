from django.contrib import admin
from django.urls import path
from Student import views
urlpatterns = [
    
    path('',views.main_page,name="main_page"),
    path('StudentLogin/',views.s_login,name="s_login"),
    path('StudentSignUp/',views.s_signup,name="s_signup"),
    path('StudentHome/',views.s_home,name="s_home"),
    path('StudentOnCampus/',views.s_oncampus,name="s_oncampus"),
    path('StudentPlacementStats/',views.splacement_stats,name="splacement_stats"),
    path('StudentOffcampus/',views.off_campus,name="off_campus"),
    path('StudentResumeBuilder/',views.resume_builder,name="resume_builder"),
    path('StudentInterviewExperience/',views.student_interview_exp,name="student_interview_exp"),
    path('StudentRoadmapAndResources',views.roadmap_resources,name="roadmap_resources")
]
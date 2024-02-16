from django.contrib import admin
from django.urls import path
from PlacementOfficer import views
urlpatterns = [
   
    path('POLogin/',views.po_login,name="po_login"),
    path('POSignUp/',views.po_signup,name="po_signup"),
    path('POHome/',views.po_home,name="po_home"),
    path('POOnCampus/',views.po_oncampus,name="po_oncampus"),
    path('POPlacementStats/',views.po_placement_stats,name="po_placement_stats"),
   
]
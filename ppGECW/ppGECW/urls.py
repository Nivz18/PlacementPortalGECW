
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('PO/',include('PlacementOfficer.urls')),
    path('',include('Student.urls')),
    path('Alumni/',include('Alumni.urls')),

]

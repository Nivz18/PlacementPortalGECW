from django.shortcuts import render

from django.shortcuts import render,HttpResponse

# Create your views here.

def po_login(request):
    return HttpResponse("POlogin")
def po_signup(request):
    return HttpResponse("POSignUp")
def po_home(request):
    return HttpResponse("POhome")
def po_oncampus(request):
    return HttpResponse("POOnCampus")
def po_placement_stats (request):
    return HttpResponse("POPlacementStats")


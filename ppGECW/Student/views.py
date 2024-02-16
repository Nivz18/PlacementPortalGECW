from django.shortcuts import render,HttpResponse,redirect
import requests
from bs4 import BeautifulSoup
from Student.models import *
from django.template import loader
import pdfkit
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from xhtml2pdf import pisa
import logging
# Create your views here.
def main_page(request):
    return HttpResponse("hello")
def s_login(request):
    return HttpResponse("Slogin")
def s_signup(request):
    return HttpResponse("SSignUp")
def s_home(request):
    return HttpResponse("Shome")
def s_oncampus(request):
    return HttpResponse("SOnCampus")
def student_interview_exp(request):
    return HttpResponse("SInterviewExperience")
def roadmap_resources(request):
    return render(request,'Student/roadmap.html')

def resume_builder(request):
    if request.method=="POST":
        name=request.POST.get("name","")
        email=request.POST.get("email","")
        linkedin=request.POST.get("linkedin","")
        skills=request.POST.get("skills","")
        summary=request.POST.get("summary","")
        phone=request.POST.get("phone","")
        university=request.POST.get("university","")
        degree=request.POST.get("degree","")
        cgpa_degree=request.POST.get("cgpa_degree","")
        school_12=request.POST.get("school_12","")
        cgpa_12=request.POST.get("cgpa_12","")
        school_10=request.POST.get("school_10","")
        cgpa_10=request.POST.get("cgpa_10","")
        project1_name=request.POST.get("project1_name","")
        project1_link=request.POST.get("project1_link","")
        project2_name=request.POST.get("project2_name","")
        project2_link=request.POST.get("project2_link","")

        profile={"name":name,"email":email,'linkedin':linkedin,"skills":skills,"summary":summary,"phone":phone,"university":university,"degree":degree,
                 "school_10":school_10,"school_12":school_12,"cgpa_degree":cgpa_degree,"cgpa_12":cgpa_12,"cgpa_10":cgpa_10,
                 "project1_name":project1_name,"project2_name":project2_name,"project1_link":project1_link,"project2_link":project2_link
                 }
        return build_resume(request,profile)
        
        #return render(request,'Student/resume.html',{'profile':profile,'sk_list':sk_list})
    return render(request,'Student/accept.html')

def build_resume(request,profile):
    skill_string=profile['skills']
    sk_list=skill_string.split(",")
    for s in sk_list:
        print(s)
    template=loader.get_template('Student/trial.html')
    html=template.render({'profile':profile,'sk_list':sk_list})
    options={
        'page-size':'Letter',
        'encoding':"UTF-8",
        'enable-local-file-access': "",
    }
    pdf=pdfkit.from_string(html,False,options)
    response=HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachment'
    filename="resume.pdf"
    return response

def splacement_stats (request):
    cse_count=PlacementDetails.objects.filter(department="CSE").count()
    ece_count=PlacementDetails.objects.filter(department="ECE").count()
    me_count=PlacementDetails.objects.filter(department="ME").count()
    count=[cse_count,ece_count,me_count]
    dept=["cse","ece",'me']
    data = zip(dept, count)
    
    return render(request,'Student/placementstats.html',{'dept':dept,'count':count,'data':data})
 


def off_campus(request):
    page=requests.get('https://www.placementindia.com/job-search/search.php?seeker_search_keyword=developer+engineer&seeker_search_city=&seeker_search_experience=0')
    soup=BeautifulSoup(page.text,'html.parser')
    role_list=[]
    company_list=[]
    exp_list=[]
    ctc_list=[]
    l_list=[]
    jd=JobDetails.objects.all()
    if(jd!=None):
       jd.delete()
    for link in soup.find_all('a',class_='job-name'):
        role=link.text
        role_list.append(role)
    for link in soup.find_all('a',class_='job-name'):
        lnk=link.get('href')
        l_list.append(lnk)  
    

    cmpnylst=soup.find_all('p',class_='job-cname')#get the company name in list
    for cl in cmpnylst:
        c_name=cl.text
        company_list.append(c_name)
            
    
    lst=soup.find_all('ul',class_='sjci-need')
    li1=[]
    li2=[]
    li3=[]
    for l in lst:
        li_tag=l.find_all('li')
        if(len(li_tag)==2):
          for i in range(0,2):
              if(i==0):
                li1.append(li_tag[i].text)
              else:
                li3.append(li_tag[i].text)
          li2.append("Not disclosed")      
        else:
          for i in range(0,3):
             if(i==0):
                li1.append(li_tag[i].text)
             elif(i==1):
                li2.append(li_tag[i].text)
             else:
                li3.append(li_tag[i].text)   

    
    for i in range(0,len(company_list)):
        role=role_list[i]
        c_name=company_list[i]
        lnk=l_list[i]
        exp=li1[i]
        ctc=li2[i]
        loc=li3[i]
        JobDetails.objects.create(company_name=c_name,role=role,link=lnk,ctc=ctc,location=loc,experience=exp)
    role=request.GET.get('name')
    if role:
       jd=JobDetails.objects.filter(role__icontains=role)
    else:
       jd=JobDetails.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(jd,4)
    jd=paginator.page(page)
    return render(request,'Student/offcampus.html',{'jd':jd})
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact_Us,Hire_Us,Photography,PhotoOnHomePage,VideoOnHomePage,Cinematography,Blog_video,Blog_Photo


def index(request):
    hire = Hire_Us.objects.all()
    photo=PhotoOnHomePage.objects.all()
    clip=VideoOnHomePage.objects.all()
    context={
        "hire":hire,
        "photo":photo,
        "video":clip
    }
    return render(request,'index.html',context)



def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        msg = request.POST.get('msg', '')
        state = request.POST.get('state', '')
        con=Contact_Us(name=name,email=email,phone=phone,city=city,msg=msg,state=state)
        con.save()
        messages.success(request,'Your message is sent thank you!')
        # return redirect('/')

    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')


def photography(request):
    photos=Photography.objects.all()
    return render(request,'photography.html',{'photos':photos})

def cinematograpgy(request):
    clip = Cinematography.objects.all()
    return render(request,'cinematography.html',{'video':clip})

def blogs(request):
    blog_video=Blog_video.objects.all()
    blog_photo=Blog_Photo.objects.all()
    context={
        "blog_video":blog_video,
        "blog_photo":blog_photo
    }
    return render(request,'blog.html', context)


from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('AboutUs', views.about, name="about"),
    path('ContactUs', views.contact, name="contact"),
    path('photography',views.photography, name='photography'),
    path('cinema1',views.cinematograpgy, name='cinematography'),
    path('blogs',views.blogs, name='blogs'),



]
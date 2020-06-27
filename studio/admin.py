from django.contrib import admin
from .models import Contact_Us,Hire_Us,Photography,PhotoOnHomePage,VideoOnHomePage,Cinematography,Blog_Photo,Blog_video

admin.site.site_header="DeepPhotographyStudio"

class AdminContact(admin.ModelAdmin):
    list_display = ('name','email','phone','city','state','msg')
    search_fields = ('city','email','state','name')
    list_filter = ('name','city','email')
    list_editable = ('email','phone')

class AdminPhotography(admin.ModelAdmin):
    list_display = ('id','image')

class AdminHireUs(admin.ModelAdmin):
    list_display = ('reason1','reason2','reason3','reason4','reason5','reason6','reason7')

class AdminHomePagePhoto(admin.ModelAdmin):
    list_display = ('image',)

class AdminHomePageVideo(admin.ModelAdmin):
    list_display = ('clip',)

class AdminCinematography(admin.ModelAdmin):
    list_display = ('clip',)

class AdminBlogPhoto(admin.ModelAdmin):
    list_display = ('image','Bride_Name','Groom_Name','place','description')
    list_filter = ('place', 'Bride_Name', 'image')
    search_fields = ('place', 'clip', 'Bride_Name')

class AdminBlogVideo(admin.ModelAdmin):
    list_display = ('clip','Bride_Name','Groom_Name','place','description')
    list_filter = ('place','Bride_Name','clip')
    search_fields = ('place','clip','Bride_Name')


admin.site.register(Contact_Us,AdminContact)
admin.site.register(Photography,AdminPhotography)
admin.site.register(Hire_Us,AdminHireUs)
admin.site.register(PhotoOnHomePage,AdminHomePagePhoto)
admin.site.register(VideoOnHomePage,AdminHomePageVideo)
admin.site.register(Cinematography,AdminCinematography)
admin.site.register(Blog_Photo,AdminBlogPhoto)
admin.site.register(Blog_video,AdminBlogVideo)





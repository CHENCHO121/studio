from django.db import models
class Contact_Us(models.Model):
    name=models.CharField(max_length=50,blank=False)
    email=models.EmailField(max_length=50,blank=True)
    phone=models.CharField(max_length=12,blank=False)
    city=models.CharField(max_length=50,blank=True)
    state = models.CharField(max_length=50, blank=True)
    msg=models.CharField(max_length=600,blank=False)

    def __str__(self):
        return(self.name)
    class Meta:
        verbose_name = 'Client Inquiry Table'



class Photography(models.Model):
    image=models.ImageField(upload_to="media/image")
    class Meta:
        verbose_name = 'Photography Table'


class PhotoOnHomePage(models.Model):
    image=models.ImageField(upload_to="media/image")
    class Meta:
        verbose_name = 'Home Page Photo Table'

class VideoOnHomePage(models.Model):
    clip=models.FileField(upload_to='media/video')


class Cinematography(models.Model):
    clip=models.FileField(upload_to='media/video')
    class Meta:
        verbose_name = 'Cinematography Table'


class Hire_Us(models.Model):
    reason1=models.CharField(max_length=100,null=True,blank=True)
    reason2 = models.CharField(max_length=100, null=True, blank=True)
    reason3 = models.CharField(max_length=100, null=True, blank=True)
    reason4 = models.CharField(max_length=100, null=True, blank=True)
    reason5 = models.CharField(max_length=100, null=True, blank=True)
    reason6 = models.CharField(max_length=100, null=True, blank=True)
    reason7 = models.CharField(max_length=100, null=True, blank=True)
    class Meta:
        verbose_name = 'Reason To Hire Us Table'


class Blog_video(models.Model):
    clip = models.FileField(upload_to='media/video')
    Bride_Name=models.CharField(max_length=50,null=True,blank=True)
    Groom_Name = models.CharField(max_length=50, null=True, blank=True)
    place=models.CharField(max_length=50,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.Groom_Name
    class Meta:
        verbose_name = 'Blog Video Table'


class Blog_Photo(models.Model):
    image = models.ImageField(upload_to="media/image")
    Bride_Name = models.CharField(max_length=50, null=True, blank=True)
    Groom_Name = models.CharField(max_length=50, null=True, blank=True)
    place = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.Groom_Name
    class Meta:
        verbose_name = 'Blog Photo Table'






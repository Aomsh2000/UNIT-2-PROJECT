from django.db import models

# Create your models here.
class Interest (models.Model):
    subject=models.CharField(max_length=124)
    about=models.TextField()
    sources=models.TextField()
    image=models.FileField(upload_to="images/",default='images/default (2).jpg')
    created_at=models.DateTimeField(auto_now_add=True)



class Project (models.Model):
    name=models.CharField(max_length=124)
    description=models.TextField()
    link=models.URLField()
    image=models.FileField(upload_to="images/",default='images/default (2).jpg')
    created_at=models.DateTimeField(auto_now_add=True)



class Memory (models.Model):
    title=models.CharField(max_length=124)
    description=models.TextField()
    is_post=models.BooleanField()
    image=models.FileField(upload_to="images/",default='images/default (2).jpg')
    created_at=models.DateTimeField(auto_now_add=True)

    class CategoryChoices(models.TextChoices):
        ACHIEVEMENTS='ACH',"Personal Achievements"
        RELATIONSHIPS='REL',"Family & Loved Ones"
        TRAVEL='TRA',"Travel & Exploration"
        SPECIALEVENTS='SPE',"Celebrations & Special Events"

    category=models.CharField(max_length=64,choices=CategoryChoices.choices,default=CategoryChoices.SPECIALEVENTS)


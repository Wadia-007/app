from django.db import models
from django.contrib import admin
from account.models import MyUser

from django.utils.text import slugify
from tinymce import models as tinymce_models
from bs4 import BeautifulSoup
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    slug = models.CharField(max_length=60, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save()

    def get_absolute_url(self, *args, **kwargs):
        return reverse('category', kwargs={'slug':self.slug})


class Post(models.Model):
    statuses = [
        ('D', 'Draft'),
        ('P', 'Publish')
    ]
    title = models.CharField(max_length=80)
    slug = models.CharField(max_length=60, unique=True, blank=True)
    meta_tag = models.CharField(max_length=300)
    meta_desc = models.CharField(max_length=150)
    content = tinymce_models.HTMLField(blank=True)
    content2 = tinymce_models.HTMLField(blank=True)
    content3 = tinymce_models.HTMLField(blank=True)
    status = models.CharField(max_length=1, choices=statuses)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    image = CloudinaryField(folder='blog/post', default="post-default.jpg", blank=True)
    img_text = models.CharField(max_length=40, blank=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    class Meta:
        ordering = ('-date','-time')



    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save()

    def get_absolute_url(self, *args, **kwargs):
        return reverse('post-detail', kwargs={'slug':self.slug})

    def html_to_text(self, *args, **kwargs):
        soup = BeautifulSoup(self.content, features="html.parser")
        text = soup.get_text()
        return text


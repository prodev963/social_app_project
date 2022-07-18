from atexit import register
from enum import unique
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import misaka
from django.contrib.auth import get_user_model
# Create your models here.
from django import template
register = template.Library()
User = get_user_model()


class Group():
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(blank=True, default='',editable=False)
    members = models.ManyToManyField(User,through='GroupMember',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)                        
    
    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.slug})

    class Meta():
        ordering = ['name']    
    

class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships')
    user = models.ForeignKey(User, related_name='user_groups')

    def __str__(self) -> str:
        return self.user.username

    class Meta():
        unique_together = ('group', 'user')

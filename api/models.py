from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username

class Blog(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(null=True,blank=True,unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='thumbnail',blank=True,null=True)
    published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = self.title.lower().replace(' ','-')
        super().save(*args, **kwargs)

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','content','image','published']
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control','rows':2}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'published':forms.CheckboxInput(attrs={'class':'form-check-input'})
        }
        
    

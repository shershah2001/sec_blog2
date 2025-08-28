from django.shortcuts import render,redirect
from api.models import Author,Blog,BlogForm
# Create your views here.

def home_view(request):
    return render(request,'api/index.html')

def contact_view(request):
    return render(request,'api/contact.html')

def category_view(request):
    return render(request,'api/category.html')
    

def create_view(request):
    if request.method == "POST":
        data = BlogForm(request.POST)
        if data.is_valid():
            if Blog.author == Author.objects.get(user=request.user):
                data.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request,'api/create.html',{'form':form})
            
        
        
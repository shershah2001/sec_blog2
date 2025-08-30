from django.shortcuts import render,redirect
from api.models import Author,Blog,BlogForm
from api.forms import Signup,Login
from django.contrib.auth import login,logout
# Create your views here.

def home_view(request):
    return render(request,'api/index.html')

def contact_view(request):
    return render(request,'api/contact.html')

def category_view(request):
    return render(request,'api/category.html')
    
def create_view(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)  # include files for image upload
        if form.is_valid():
            blog = form.save(commit=False)  # don’t save yet
            blog.author = Author.objects.get(user=request.user)  # assign logged-in user’s author
            blog.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'api/create.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
        
        return render(request, 'api/form.html', {'form': form, 'form_title': 'SignUp'})
        
    else:
        form = Signup()
        return render(request,'api/form.html',{'form':form,'form_title':'SignUp'})
    

def login_view(request):
    if request.method == "POST":
        form = Login(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(user)
            login(request,user)
            return redirect('home')
    else:
        form = Login()
    return render(request,'api/form.html',{'form':form,'form_title':'Login'})
        
            
    

            
        
        
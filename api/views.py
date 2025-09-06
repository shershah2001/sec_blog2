from django.shortcuts import render,redirect,get_object_or_404
from api.models import Author,Blog,BlogForm,Categories
from api.forms import Signup,Login
from django.contrib.auth import login,logout
import datetime
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def profile_view(request):
    author = Author.objects.get(user=request.user)
    posts = Blog.objects.filter(author = author,published=True)
    print("posts==>",posts,"author==>",author)
    data={
        'author':author,
        'posts':posts
    }
    return render(request,'api/profile.html',data)

def home_view(request):
    week_ago = datetime.date.today() - datetime.timedelta(days=7)
    trends = Blog.objects.filter(created_at__gte=week_ago).order_by('-read')
    topAuthor = Author.objects.order_by('-rate')[:4]
    AuthorsPost = [Blog.objects.filter(author = author).first()  for author in topAuthor]
    all_post = Paginator(Blog.objects.filter(published=True),3)
    # post=Blog.objects.filter(published=True)
    # print("post==>", [cat for post in post for cat in post.categories.all()])
    page = request.GET.get('page')
    
    try:
        posts = all_post.page(page)
    except PageNotAnInteger:
        posts = all_post.page(1)
    except EmptyPage:
        posts = all_post.page(all_post.num_pages)
   
    data={
        'posts':posts,   
        'trends':trends[:5],
        'author_post':AuthorsPost,
        'pop_post':Blog.objects.order_by("-read")[:9],
    }
    return render(request,'api/index.html',data)

def contact_view(request):
    return render(request,'api/contact.html')

def category_view(request,slug):
    category  = get_object_or_404(Categories, slug=slug)
    blog = Blog.objects.filter(categories=category,published=True)
    return render(request,'api/category.html',{"category":category,"blog":blog})
    

def detail_view(request,slug):
    blog = Blog.objects.get(slug = slug, published=True)
    return render(request,'api/blog-single.html',{'blog':blog})

def create_view(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)  # include files for image upload
        if form.is_valid():
            blog = form.save(commit=False)  # don’t save yet
            blog.author, created = Author.objects.get_or_create(user=request.user)
            # assign logged-in user’s author
            blog.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'api/create.html', {'form': form,'form_title':'Create Blog'})

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

def logout_view(request):
    if request.method =='POST':
        logout(request)
        return redirect('signup')
    
@login_required
def edit_view(request,slug):
    author = get_object_or_404(Author,user=request.user)
    blog = get_object_or_404(Blog,slug=slug,author=author)
    if request.method == "POST":
        print("form==>",BlogForm(instance=blog))
        form = BlogForm(request.POST,request.FILES,instance=blog)
        print("form==>1",BlogForm(instance=blog))
        if form.is_valid():
            form.save()
            messages.success(request,'Post edit successfully!!')
            return redirect('detail',slug=blog.slug)
    else:
        form=BlogForm(instance=blog)
    return render(request,'api/create.html',{'form':form,'blog':blog,'form_title':'Edit Blog'})
            
@login_required
def delete_view(request,slug):
    author = get_object_or_404(Author,user=request.user)
    blog = get_object_or_404(Blog,slug=slug,author=author)
    if request.method == "POST":
        blog.delete()
        messages.success(request,'Post successfully deleted!!')
        return redirect('profile')
    return render(request,'api/delete.html',{"blog":blog})

            

        
        
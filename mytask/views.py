from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .tests import sumnumber

# Create your views here.
def about(request):
    ans=sumnumber(40,20)
    print(ans)
    return render(request, 'about.html')

def homepage(request):
    title = "My Blog Title"
    cat_data = Category.objects.all()
    blogs = MyBlog.objects.all()
    contex = {
        'abc':title,
        'name':'Mg Myo Kyaw Thu',
        'datas':cat_data,
        'blogs':blogs
        }
    return render(request, 'home.html', contex)



def filter_blog(request):
    cid = request.GET.get('cid')
    cat_obj = Category.objects.get(id=cid)  #Drink
    filter_data = MyBlog.objects.filter(category=cat_obj)
    context = {
        'blogs': filter_data
    }
    return render(request, 'home.html', context)
    
def detail_blog(request, blogid):
    blog = MyBlog.objects.get(id = blogid)
    if request.method == 'POST':
        title = request.POST.get('title')
        pbody = request.POST.get('post_body')
        blogs = MyBlog.objects.filter(id = blogid)
        blogs.update(title=title, post_body=pbody)
        return redirect('/')
     
    context = {
        'blog':blog
    }
    
    return render(request, 'blogdetail.html', context)
    
    
   
def detail_blog(request, blogid):
    blog = MyBlog.objects.get(id = blogid)
    if request.method == 'POST':
        title = request.POST.get('title')
        pbody = request.POST.get('post_body')
        blogs = MyBlog.objects.filter(id = blogid)
        blogs.update(title=title, post_body=pbody)
        return redirect('/')
     
    context = {
        'blog':blog
    }
    
    return render(request, 'blogdetail.html', context)
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from datetime import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Count

from .models import Post,Comment

from .forms import CreateUserForm,MakePost,Comments
from django.contrib import messages


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was successfully created for '+user)

           

            return redirect('login')

    context = {'form':form}
    return render(request,'reg.html',context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password incorrect!!!')


    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    post = Post.objects.all()
    
    
    context = {'post':post}
    return render(request,'home.html',context)



@login_required(login_url='login')
def createPost(request):
    form = MakePost()
    if request.method == 'POST':
        form = MakePost(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form':form
    }
    return render(request,'create.html',context)

class Home(ListView):
    login_required = True
    model = Post
    ordering = ['-id']
    template_name = 'home.html'

   
               

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        context['form'] = Comments()
        return context
    
    def post(self, request, *args, **kwargs):
        form = Comments(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = request.POST.get("post") 
            comment.save()
            return redirect('home')
        else:
            post = get_object_or_404(Post, id=request.POST.get('post.id'))
            liked = False
            if post.likes.filter(id=request.user.id).exists():
                post.likes.remove(request.user)
                liked = False
            else:
                post.likes.add(request.user)
                liked = True
            return HttpResponseRedirect(reverse('home'))



    @classmethod
    def as_view(cls):
        return login_required(super(Home, cls).as_view(),login_url='login')





@login_required(login_url='login')
def view_blog(request, pk_second):
    post = Post.objects.get(pk=pk_second)
    commenty = post.comments.all()
    print(commenty)
    context = {'post': post, 'commenty': commenty}
    return render(request, 'comment.html', context)

@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html')

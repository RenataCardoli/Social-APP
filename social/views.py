from django.shortcuts import render, redirect
from .models import Post
from .forms import PostModelForm, PostUpdateForm, ContactForm, CommentForm 
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('social-index')
    else:
        form = PostModelForm()
    context = {
        'posts': posts,
        'form': form
    }

    return render(request, 'social/index.html', context)

@login_required
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        comentario_form = CommentForm(request.POST)
        if comentario_form.is_valid():
            instance = comentario_form.save(commit=False)
            instance.user = request.user
            instance.post = post #user unique post
            instance.save()
            return redirect('social-post-detail', pk=post.id)
    else:
        comentario_form = CommentForm()
    context = {
        'post':post,
        'comentario_form': comentario_form,
    }    
    
    return render(request, 'social/post_detail.html',context)


@login_required
def post_edit(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('social-post-detail', pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context={
        'post':post,
        'form':form,
    }
    return render (request, 'social/post_edit.html', context)

@login_required
def post_delete(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('social-index')
    context={
        'post':post,
        
    }
    return render(request, 'social/post_delete.html', context)

def about(request):
    data= {
        'form': ContactForm()
    }
    return render (request, 'social/about.html',data)
"""Posts views."""

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post


@login_required
def list_posts(request):
    """List existing posts."""
    posts = Post.objects.all().order_by('-created')
<<<<<<< HEAD
    profile = request.user.profile
    
    return render(request, 'posts/feed.html', {'posts': posts, 'profile': profile})
=======

    return render(request, 'posts/feed.html', {'posts': posts})
>>>>>>> 570e22022dcf8be67007c8385d0d597ba237a910


@login_required
def create_post(request):
    """Create new post view."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')

    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )

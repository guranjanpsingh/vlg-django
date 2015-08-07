from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from vlg_django.models import Post, Comment, PostLikes, PostDisikes, commentLikes, commentDislikes
from django.utils import timezone
# Create your views here.


def index(request):
    posts = Post.objects.order_by('-postedOn')
    template = loader.get_template('posts/index.html')
    context = RequestContext(request, {
        'posts': posts
    })
    return HttpResponse(template.render(context))

def detail(request):
    return HttpResponse('Hello world')
def createPost(request):
    postContent = request.POST['post']
    postedOn = timezone.now()
    postedBy = 'user'
    post = Post(post= postContent, postedOn = postedOn, postedBy = postedBy)
    post.save()
    return index(request)
def likePost(request):
    return HttpResponse('Hello world')
def dislikePost(request):
    return HttpResponse('Hello world')
def createComment(request, post_id):
    commentContent = request.POST['comment']
    postedOn = timezone.now()
    postedBy = 'user'
    post = Post.objects.get(pk=post_id)
    comment = Comment(comment= commentContent, postsID = post, postedOn = postedOn, postedBy = postedBy)
    comment.save()
    return index(request)
def likeComment(request):
    return HttpResponse('Hello world')
def dislikeComment(request):
    return HttpResponse('Hello world')

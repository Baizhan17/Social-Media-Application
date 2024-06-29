from django.http import JsonResponse
from .serializers import PostSerializer, PostDetailSerializer, CommentSerializer, TrendSerializer
from .models import Post, Like, Comment, Trend, PostAttachment
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import viewsets
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.pagination import PageNumberPagination
from .forms import PostForm, AttachmentForm
from account.models import User, FriendRequest
from account.serializers import UserSerializer

class PostPagination(PageNumberPagination):
    page_size = 10  # Number of posts per page

@api_view(['GET'])
def post_list(request):
    usr_id_list = [request.user.id] + [user.id for user in request.user.friends.all()]
    posts = Post.objects.filter(created_by_id__in=usr_id_list)

    paginator = PostPagination()
    paginated_posts = paginator.paginate_queryset(posts, request)
    serializer = PostSerializer(paginated_posts, many=True)
    
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def post_list_profile(request, id):
    user = User.objects.get(pk=id)
    posts = Post.objects.filter(created_by_id=id)
    send_f_request = True
    posts_serializer = PostSerializer(posts, many=True)
    user_serializer = UserSerializer(user)
    h1 = FriendRequest.objects.filter(created_by=request.user, request_for=user).exists()
    h2 = FriendRequest.objects.filter(created_by=user, request_for=request.user).exists()
    if h1 or h2:
        send_f_request = False

    return JsonResponse({'posts': posts_serializer.data, 'user': user_serializer.data, 'send_f_request': send_f_request}, safe=False)

@api_view(['POST'])
def add_post(request):
    post_form = PostForm(request.POST)
    attachment_form = AttachmentForm(request.FILES)

    if post_form.is_valid():
        post = post_form.save(commit=False)
        post.created_by = request.user
        post.save()
        
        if attachment_form.is_valid():
            attachment = attachment_form.save(commit=False)
            attachment.created_by = request.user
            attachment.save()
            post.attachments.add(attachment)

        post.save()
        
        # Update user's post count
        request.user.posts_number += 1
        request.user.save()

        serializer = PostSerializer(post)
        return JsonResponse(serializer.data, safe=False)
    else:
        errors = {**post_form.errors, **attachment_form.errors}
        return JsonResponse({'errors': errors}, status=400)

@api_view(['POST'])
def like_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return JsonResponse({'message': 'Post not found'}, status=404)

    # Check if the user has already liked the post
    if not post.likes.filter(created_by=request.user).exists():
        like = Like.objects.create(created_by=request.user)
        post.likes_counter += 1
        post.likes.add(like)
        post.save()
        return JsonResponse({'message': 'The post has been liked'}, status=200)

    return JsonResponse({'message': 'Post has already been liked'}, status=400)

@api_view(['GET'])
def post_comments(request, pk):
    post = Post.objects.get(pk=pk)
    return JsonResponse({'post': PostDetailSerializer(post).data})

@api_view(['POST'])
def add_comment(request, pk):
    post = Post.objects.get(pk=pk)
    text = request.data.get('body')
    print(f"Received comment text: {text}")  # Add logging for debugging

    if text:
        comment = Comment.objects.create(text=text, created_by=request.user)
        post.comments.add(comment)
        post.comments_counter += 1
        post.save()
        serializer = CommentSerializer(comment)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'message': 'Comment text is required'}, status=400)

@api_view(['GET'])
def get_trends(request):
    serializer = TrendSerializer(Trend.objects.all(), many=True)
    return JsonResponse(serializer.data, safe=False)

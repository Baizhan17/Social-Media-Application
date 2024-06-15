
from django.http import JsonResponse
from .serializers import PostSerializer,PostDetailSerializer,CommentSerializer,TrendSerializer
from .models import Post,Like,Comment,Trend
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .forms import PostForm,AttachmentForm
from account.models import User
from account.serializers import UserSerializer
from django.core.paginator import Paginator

# class PostPagination(PageNumberPagination):
#     page_size=5

# class PostViewSet(viewsets.ModelViewSet):
#     pagination_class = PostPagination
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
@api_view(['GET'])
def post_list(request):
    usr_id_list=[request.user.id]
    for user in request.user.friends.all():
        usr_id_list.append(user.id)
    posts=Post.objects.filter(created_by_id__in=list(usr_id_list))
    #trend=request.GET.get('trend','')
    
    serializer = PostSerializer(posts,many=True)
    return JsonResponse({'data':serializer.data})



@api_view(['GET'])
def post_list_profile(request,id):
    user=User.objects.get(pk=id)
    posts=Post.objects.filter(created_by_id=id)
    posts_serializer = PostSerializer(posts,many=True)
    user_serializer = UserSerializer(user)
    return JsonResponse({'posts':posts_serializer.data,'user':user_serializer.data},safe=False)


@api_view(['POST'])
def add_post(request):
    form=PostForm(request.POST)
    attachment=None
    attachment_form=AttachmentForm(request.FILES)
    if attachment_form.is_valid():
        attachment=attachment_form.save(commit=False)
        attachment.created_by=request.user
        attachment.save()
    if form.is_valid():
        post=form.save(commit=False)
        post.created_by=request.user
        post.save()
        if attachment:
            post.attachments.add(attachment)
        user=request.user
        user.posts_number+=1
        user.save()
        serializer = PostSerializer(posts)
        return JsonResponse(serializer.data,safe=False)
    else:
        return JsonResponse({'error':'gtr'})
    
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
        return JsonResponse({'message': f'The post  has been liked'}, status=200)
    
    return JsonResponse({'message': f'Post with id {post.id} has already been liked'}, status=400)


@api_view(['GET'])
def post_comments(request, pk):
    post = Post.objects.get(pk=pk)
    
    return JsonResponse({'post':PostDetailSerializer(post).data})





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
    
    serializer = TrendSerializer(Trend.objects.all(),many=True)
    return JsonResponse(serializer.data, safe=False)
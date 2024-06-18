from django.http import JsonResponse
from django.contrib.auth.forms import PasswordChangeForm
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from .forms import SignUpForm
from django.core.mail import send_mail
from .models import FriendRequest,User
from .serializers import UserSerializer,FriendRequestSerializer
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
    })


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data=request.data
    message='success'
    form=SignUpForm({
        'email':data.get('email'),
        'password1':data.get('password1'),
        'password2':data.get('password2'),
        'name':data.get('name'),
    })
    if form.is_valid():
        user=form.save()
        user.is_active=False
        user.save()
        # url = f'http://127.0.0.1:8000/activateemail/?email={user.email}&id={user.id}'

        # send_mail(
        #     "Confirm your email",
        #     f"The url for activating your account is: {url}",
        #     "noreply@site.com",
        #     [user.email],
        #     fail_silently=False,
        # )
        #return JsonResponse({'message': 'success'}, status=201)
    else:
        #message='error'
        print(form.errors.as_data())
        message=form.errors.as_json()
    print(message)
    return JsonResponse({'message':message})


@api_view(['POST'])
def send_friend_request(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({'message': 'User not found'}, status=404)

    if FriendRequest.objects.filter(created_by=request.user, request_for=user).exists():
        return JsonResponse({'message': 'Friend request already sent'}, status=400)

    if FriendRequest.objects.filter(created_by=user, request_for=request.user).exists():
        return JsonResponse({'message': 'Friend request already received from this user'}, status=400)
    
    FriendRequest.objects.create(request_for=user, created_by=request.user)
    return JsonResponse({'message': 'Friend request created'}, status=201)



@api_view(['GET'])
def friends(request, pk):
    user = User.objects.get(pk=pk)
    requests = []
   
    if user == request.user:
        requests = FriendRequest.objects.filter(request_for=request.user, status=FriendRequest.SENT)
        requests = FriendRequestSerializer(requests, many=True)
        requests = requests.data

    friends = user.friends.all()

    return JsonResponse({
        'user': UserSerializer(user).data,
        'friends': UserSerializer(friends, many=True).data,
        'requests': requests
    }, safe=False)
    
    
@api_view(['POST'])
def handle_req(request, pk,status):
    user = User.objects.get(pk=pk)
    friend_request = FriendRequest.objects.filter(request_for=request.user).get(created_by=user)
    friend_request.status=status
    friend_request.save()
    user.friends.add(request.user)
    user.friends_number = user.friends_number+1
    user.save()
    request_user = request.user
    request_user.friends_number = request_user.friends_number+1
    request_user.save()
    return JsonResponse({'message': 'Friend request updated'})




@api_view(['POST'])
def reset_account(request):
    user = request.user
    if User.objects.exclude(id=user.id).filter(email=request.data.get('email')).exists():
        return JsonResponse({'message': 'follwing email is already in use'})
    else:
        
        user.email=request.data.get('email')
        user.name=request.data.get('name')
        user.save()
        return JsonResponse({'message': 'new email is setted up'})
    

@api_view(['GET'])
def friends_reccomendations(request):
    serializer=UserSerializer(request.user.friends_suggestion.all(),many=True)
    return JsonResponse(serializer.data,safe=False)








@api_view(['POST'])
def reset_password(request):
    user = request.user
    form=PasswordChangeForm(data=request.POST,user=user)
    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'new password is setted up'})
    return JsonResponse({'message': form.errors.as_json()},safe=False)
    # if User.objects.exclude(id=user.id).filter(email=request.data.get('email')).exists():
    #     return JsonResponse({'message': 'follwing email is already in use'})
    # else:
        
    #     user.email=request.data.get('email')
    #     user.name=request.data.get('name')
    #     user.save()
    #     return JsonResponse({'message': 'new email is setted up'})
        
    

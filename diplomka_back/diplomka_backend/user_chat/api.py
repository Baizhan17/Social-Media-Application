from django.http import JsonResponse
from .serializers import ConversationSerializer,ConvMessageSerializer,ConversationDetailSerializer
from .models import Conversation,ConvMessage
from account.models import User
from rest_framework.decorators import api_view,authentication_classes,permission_classes
#from .forms import PostForm
# from account.models import User
# from account.serializers import UserSerializer



@api_view(['GET'])
def conv_list(request):
    print(f"Request user: {request.user} (ID: {request.user.id}, Email: {request.user.email})")
    
    conversations = Conversation.objects.filter(users__in=list([request.user]))
    serializer = ConversationSerializer(conversations, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def conv_message(request, pk):
    try:
        conversation = Conversation.objects.filter(users=request.user).get(pk=pk)
    except Conversation.DoesNotExist:
        raise NotFound('Conversation not found')
    
    serializer = ConversationDetailSerializer(conversation)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def conv_get_create(request, user_pk):
    user=User.objects.get(pk=user_pk)
    conversations = Conversation.objects.filter(users__in=list([request.user])).filter(users__in=list([user]))
    if conversations.exists:
        conversation = conversations.first()
    else:
        conversation = Conversation.objects.create()
        conversation.users.add(user,request.user)
        conversation.save()
    serializer = ConversationDetailSerializer(conversation)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def send_conv_message(request, pk):
    try:
        conversation = Conversation.objects.filter(users=request.user).get(pk=pk)
    except Conversation.DoesNotExist:
        raise NotFound('Conversation not found')
    
    receiver = None
    for user in conversation.users.all():
        if user != request.user:
            receiver = user
            break

    if not receiver:
        return JsonResponse({'error': 'No receiver found'}, status=400)

    conv_message = ConvMessage.objects.create(
        conversation=conversation,
        text=request.data.get('text'),
        created_by=request.user,
        receiver=receiver,
    )
    serializer = ConvMessageSerializer(conv_message)
    return JsonResponse(serializer.data, safe=False)


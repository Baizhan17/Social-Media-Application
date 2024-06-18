import uuid
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,UserManager
from django.db import models
from django.utils import timezone
# Create your models here.


class CustomUserManager(UserManager):
    def _create_user(self,email,name,password,**extra_fields):
        if not email:
            raise ValueError("Please provide an email address!!!")
        email=self.normalize_email(email)
        user=self.model(email=email,name=name,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    def create_user(self,email=None,name=None,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,name,password,**extra_fields)
    def create_superuser(self,email=None,name=None,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email,name,password,**extra_fields)
    
class User(AbstractBaseUser,PermissionsMixin):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email=models.EmailField(unique=True)
    name=models.CharField(max_length=255,blank=True,default='')
    #photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    friends=models.ManyToManyField('self')
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    friends_number=models.IntegerField(default=0)
    posts_number=models.IntegerField(default=0)
    friends_suggestion=models.ManyToManyField('self')
    date_joined=models.DateTimeField(default=timezone.now)
    last_login=models.DateTimeField(blank=True,null=True)
    
    
    objects=CustomUserManager()
    #authentication fields
    USERNAME_FIELD='email'
    EMAIL_FIELD='email'
    REQUIRED_FIELDS=[]


# class ProfilePhoto(models.Model):
#     photo = models.ImageField(upload_to='photos/', blank=True, null=True)

class FriendRequest(models.Model):
    SENT='sent'
    ACCEPT='accept'
    REJECT='reject'
    STATUS_REQUESTS=(
        (SENT, 'sent'),
        (ACCEPT, 'accept'),
        (REJECT, 'reject'),
    )
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    request_for=models.ForeignKey(User,related_name="received_friendrequests",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20,choices=STATUS_REQUESTS,default=SENT)
    created_by=models.ForeignKey(User,related_name="make_friendrequests",on_delete=models.CASCADE)
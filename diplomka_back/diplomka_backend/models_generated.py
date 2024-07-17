# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountFriendrequest(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    created_at = models.DateTimeField()
    status = models.CharField(max_length=20)
    created_by = models.ForeignKey('AccountUser', models.DO_NOTHING)
    request_for = models.ForeignKey('AccountUser', models.DO_NOTHING, related_name='accountfriendrequest_request_for_set')

    class Meta:
        managed = False
        db_table = 'account_friendrequest'


class AccountUser(models.Model):
    password = models.CharField(max_length=128)
    id = models.CharField(primary_key=True, max_length=32)
    email = models.CharField(unique=True, max_length=254)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()
    date_joined = models.DateTimeField()
    last_login = models.DateTimeField(blank=True, null=True)
    friends_number = models.IntegerField()
    posts_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'account_user'


class AccountUserFriends(models.Model):
    from_user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    to_user = models.ForeignKey(AccountUser, models.DO_NOTHING, related_name='accountuserfriends_to_user_set')

    class Meta:
        managed = False
        db_table = 'account_user_friends'
        unique_together = (('from_user', 'to_user'),)


class AccountUserFriendsSuggestion(models.Model):
    from_user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    to_user = models.ForeignKey(AccountUser, models.DO_NOTHING, related_name='accountuserfriendssuggestion_to_user_set')

    class Meta:
        managed = False
        db_table = 'account_user_friends_suggestion'
        unique_together = (('from_user', 'to_user'),)


class AccountUserGroups(models.Model):
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_user_groups'
        unique_together = (('user', 'group'),)


class AccountUserUserPermissions(models.Model):
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PostComment(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(AccountUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'post_comment'


class PostLike(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    created_by = models.ForeignKey(AccountUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'post_like'


class PostPost(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    body = models.TextField()
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(AccountUser, models.DO_NOTHING)
    likes_counter = models.IntegerField()
    comments_counter = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'post_post'


class PostPostAttachments(models.Model):
    post = models.ForeignKey(PostPost, models.DO_NOTHING)
    postattachment = models.ForeignKey('PostPostattachment', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'post_post_attachments'
        unique_together = (('post', 'postattachment'),)


class PostPostComments(models.Model):
    post = models.ForeignKey(PostPost, models.DO_NOTHING)
    comment = models.ForeignKey(PostComment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'post_post_comments'
        unique_together = (('post', 'comment'),)


class PostPostLikes(models.Model):
    post = models.ForeignKey(PostPost, models.DO_NOTHING)
    like = models.ForeignKey(PostLike, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'post_post_likes'
        unique_together = (('post', 'like'),)


class PostPostattachment(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    created_by = models.ForeignKey(AccountUser, models.DO_NOTHING)
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'post_postattachment'


class PostTrend(models.Model):
    hashtags = models.CharField(max_length=50)
    hashtags_counter = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'post_trend'


class UserChatConversation(models.Model):
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    id = models.CharField(primary_key=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'user_chat_conversation'


class UserChatConversationUsers(models.Model):
    conversation = models.ForeignKey(UserChatConversation, models.DO_NOTHING)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_chat_conversation_users'
        unique_together = (('conversation', 'user'),)


class UserChatConvmessage(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField()
    conversation = models.ForeignKey(UserChatConversation, models.DO_NOTHING)
    created_by = models.ForeignKey(AccountUser, models.DO_NOTHING)
    receiver = models.ForeignKey(AccountUser, models.DO_NOTHING, related_name='userchatconvmessage_receiver_set')
    id = models.CharField(primary_key=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'user_chat_convmessage'

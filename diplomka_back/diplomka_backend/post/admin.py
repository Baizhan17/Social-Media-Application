from django.contrib import admin
from .models import Post,PostAttachment,Trend,Like,Comment,PostReport
# Register your models here.
admin.site.register(Post)
admin.site.register(PostAttachment)
admin.site.register(Trend)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(PostReport)
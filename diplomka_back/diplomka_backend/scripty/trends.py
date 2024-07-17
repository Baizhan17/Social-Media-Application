import django
import sys
import os
from collections import Counter
from datetime import timedelta
from django.utils import timezone
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)),'..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE',"diplomka_backend.settings")
django.setup()

from post.models import Post,Trend
def show_hashtags(text,trends):
    #hastags=[]
    for word in text.split():
        if word[0]=='#':
            trends.append(word[1:])
            
    return trends
for trend in Trend.objects.all():
    trend.delete()           
#posts=Post.objects.all()
trends=[]
this_hour = timezone.now().replace(minute=0, second=0, microsecond=0)
twelve_hours = this_hour - timedelta(hours=12)
#Post.objects.filter(date__range=(this_hour, twelve_hour_later))
print(Post.objects.filter(created_at__range=(twelve_hours,this_hour)))
for post in Post.objects.filter(created_at__gte=twelve_hours):
    #print(show_hashtags(post.body))
    show_hashtags(post.body,trends)
    
#tc=Counter(trends).most_common(3)



for trend in Counter(trends).most_common(3):
    Trend.objects.create(hashtags=trend[0],hashtags_counter=trend[1])
   #print(trend[0],trend[1])
    
#print(Trend.objects.all())
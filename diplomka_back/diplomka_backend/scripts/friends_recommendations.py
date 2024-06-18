import django
import sys
import os
from collections import Counter
from datetime import timedelta
from django.utils import timezone

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)),'..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE',"diplomka_backend.settings")
django.setup()

from account.models import User

users=User.objects.all()

for user in users:
    #myListOfTitles=["Adolf"]
    user.friends_suggestion.clear()
    print("Find friends for: ", user)
    for friend in user.friends.all():
        print("Friend with: ", friend)
        for friendOffriend in friend.friends.all():
            if friendOffriend not in user.friends.all() and friendOffriend!=user:
                user.friends_suggestion.add(friendOffriend)
                print('suggest ',friendOffriend)
        
        #print("friend id: ", friend.id)
    #print(user)

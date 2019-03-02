# -*- coding: utf-8 -*-

__author__ = 'antares'
import sys
import os


pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "StudyAiD2.settings")

import django
from django.contrib.auth import get_user_model

django.setup()

User = get_user_model()

from rest_framework.authtoken.models import Token

for user in User.objects.all():
    print(user.username)
    Token.objects.get_or_create(user=user)

1. 가상환경을 위한 poetry
brew install poetry
poetry init
poetry add django==2.2.5
petry shell #가상환경 진입

2. start project
django-admin startproject config .
#> add gitignore pyhton
python3 manage.py runserver
python3 manage.py migrate : 초기 db 설정

config/settings.py
```
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = "Asia/Seoul"
```

3. 관리자생성
python3 manage.py createsuperuser

4. message app 생성
python3 manage.py startapp messages

5. message model 생성
models.py
```
class Cozmessage(models.Model):

    username = models.CharField(max_length=140)
    text = models.CharField(max_length=140)
    roomname = models.CharField(max_length=140)
    date = models.DateTimeField
    
    def __str__(self):
        return self.name
```

6. cozmessages app 등록
config settings.py 셋팅

CUSTOM_APPS = [
    "cozmessages.apps.CozmessagesConfig"
]

INSTALLED_APPS = CUSTOM_APPS + SYSTEM_APPS

7. admin등록 
cozmessages/admin.py
from .models import Cozmessage
```
from django.contrib import admin
from .models import Cozmessage

@admin.register(Cozmessage)
class CozmessageAdmin(admin.ModelAdmin):

    list_display = [
        "username",
        "text",
        "roomname"
    ]

    list_filter = [
        "username"
    ]

    search_fields = ["username"]
```
python3 manage.py makemigrations
python3 manage.py migrate


8. rest framework 설치
poetry add djangorestframework==3.13.0

INSTALLED_APPS = CUSTOM_APPS + THIRD_PARTY_APPS + SYSTEM_APPS

THIRD_PARTY_APPS=[
    'rest_framework',
]

9. url, view 만들기
cozmessages/urls.py
```
from django.urls import path
from . import views
urlpatterns = [
    path("", views.cozmessages),
]
```
config/settings.py
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cozmessages/', include("cozmessages.urls")),
]
```
cozmessages/views.py
```
from django.http import JsonResponse
from .models import Cozmessage

def cozmessages(request):
    
    all_messages = Cozmessage.objects.all()
```
cozmessages/serializers.py
```
```

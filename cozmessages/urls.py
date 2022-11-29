from django.urls import path
from . import views
urlpatterns = [
    path("", views.Cozmessages.as_view()),
    path("<str:githubId>/messages", views.MessagesByGithubId.as_view()),
    path("<str:githubId>/clear", views.MessageClear.as_view()),
]
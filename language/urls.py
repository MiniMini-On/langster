from django.urls import path
from . import views


urlpatterns = [
    path('training',views.SuggestionView.as_view()),
    path('test',views.LanguageTestView.as_view()),
]
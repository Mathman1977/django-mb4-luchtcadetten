
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/resultaten/', views.ResultsView.as_view(), name='resultaten'),
    path('<int:question_id>/stem/', views.vote, name='stem'),
]

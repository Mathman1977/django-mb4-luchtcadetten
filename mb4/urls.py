from django.urls import path
# from .views import (
#     IndexView,
#     )
from . import views
# from django.conf.urls.static import static

# app_name = 'mb4'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:reeks_id>/', views.detail, name='detail'),
    path('training/', views.training, name='training'),
    path('resultaten/', views.resultaten, name='resultaten'),
    path('uitgewerkt/<int:opg_id>', views.uitgewerkt, name='uitgewerkt'),

    path('fav/',views.fav, name='fav'),
    path('fav/aft',views.fav_aft, name='fav_aft'),

    # path('index/', views.IndexView.as_view(), name='index'),
     # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/statististieken/', views.ResultsView.as_view(), name='statistieken'),
    # path('<int:question_id>/oefen/', views.ExcView.as_view(), name='maak_oef'),
    # # path('about/',views.about, name='oef-about'),

    # path('add/',views.add, name='add'),
    # # path('2F2F/',views.toofast, name='2F2F'),
    # path('2F2F/77',views.toofast77, name='2F2F_77'),
    # path('fav/',views.fav, name='fav'),
    # path('fav/aft',views.fav_aft, name='fav_aft'),
    # path('',views.home, name='oef-home'),
    # # path('ingelogd/',views.ingelogd, name='ingelogd'),
    # # path('',PostListView.as_view(), name='oef-home'),
    # path('oef/',PostListView.as_view(), name='oef-home'),
    # path('user/<str:username>',UserPostListView.as_view(), name='user-posts'),
    # path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    # path('post/new/',PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete'),

]



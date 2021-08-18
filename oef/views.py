# from django.shortcuts import render,get_object_or_404
# from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from django.views.generic import (
#     ListView,
#     DetailView,
#     # CreateView,
#     # UpdateView,
#     # DeleteView
#     )
# # from .models import Post
# # from .forms import Oefening
# import random
# from .models import Opgave, Oefening

# def home(request):
#     context = {
#     #   # 'posts': Post.objects.all()
#     }
#     return render(request,'oef/home.html', {})



# @login_required
# def overview(request):
#     context = {
#     #   # 'posts': Post.objects.all()
#     }
#     return render(request,'oef/home.html', {})

# @login_required
# class IndexView(ListView):
#     template_name = 'oef/overview.html'
#     context_object_name = 'laatste_oef_lijst'

#     def get_queryset(self):
#         """
#         Return the last five published questions (not including those set to be
#         published in the future).
#         """
#         return Opgave.objects.filter(
#             pub_date__lte=timezone.now()
#         ).order_by('-pub_date')[:5]

# @login_required
# class ResultsView(DetailView):
#     model = Opgave
#     template_name = 'oef/statistieken.html'


# @login_required
# class ExcView(DetailView):
#     model = Opgave
#     template_name = 'oef/maken.html'




# # from django.http import HttpResponseRedirect
# # from django.shortcuts import get_object_or_404, render
# # from django.urls import reverse
# # from django.views import generic
# # from django.utils import timezone
# # from .models import Choice, Question

#  # path('', views.IndexView.as_view(), name='index'),
#  #    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#  #    path('<int:pk>/results/', views.ResultsView.as_view(), name='resultaten'),
#  #    path('<int:question_id>/vote/', views.vote, name='maak_oef'),

from django.urls import path

from . import views


app_name = "main"
urlpatterns = [
    path('', views.home, name='users-home'),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('profile/', views.profile, name='profile'),
]
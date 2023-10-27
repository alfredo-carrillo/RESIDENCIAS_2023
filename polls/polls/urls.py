from django.urls import path

from . import views




app_name = 'polls'
urlpatterns = [
    
   
    path('', views.Home.as_view(), name = 'home'),
    path("accounts/login/", views.LoginView.as_view(), name='register'),
    path("accounts/logout/", views.logout_view, name='log-out'),
    path('main/', views.MainView.as_view(), name='main'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('create-poll/', views.CreatePoll.as_view(), name='c-poll'),
    path('<int:pk>/update/', views.PollsUpdate.as_view(), name='update'),
    
    path('<int:pk>/delete/', views.PollDeleteView.as_view(), name='deletePoll'),
   
]



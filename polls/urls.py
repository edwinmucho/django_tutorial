from django.urls import path

from . import views

app_name= 'polls'
urlpatterns = [
    # Generic View를 사용 하기 위해 변경
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # path('', views.index, name='index'),    # ex: /polls/
    # path('<int:question_id>/', views.detail, name="detail"),    # ex: /polls/5/
    # path('<int:question_id>/results/', views.results, name="results"),  # ex: /polls/5/results/
    # path('<int:question_id>/vote/', views.vote, name="vote"),    # ex: /polls/5/vote/
]
from .views import index, rubric_bbs, BdCreateView
from django.urls import path

urlpatterns = [
    path('<int:rubric_id>/', rubric_bbs, name='rubric_bbs'),
    path('', index, name='index'),
    path('add/', BdCreateView.as_view(), name='add')
]
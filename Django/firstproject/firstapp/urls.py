from django.urls import path
from firstapp import views

urlpatterns=[
    path('first/', views.index, ),
    path('second/', views.rishabh, ),
    path('third/', views.example,),
    path('',views.template_demo,),
    path('form/',views.form_view,),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),

]
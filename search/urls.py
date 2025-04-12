from django.urls import path


from . import views

urlpatterns = [
  path('', views.search.as_view(), name='search'),
  path('result_edit/', views.result_new, name='result_new'),
  path('register/', views.signup_new, name='register'),
]

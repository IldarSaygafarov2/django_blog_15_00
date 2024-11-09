# http://127.0.0.1:8000/blog/
# http://127.0.0.1:8000/blog/categories
# http://127.0.0.1:8000/blog/categories/1

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('contacts/', views.contacts_page, name='contacts'),
    path('categories/<int:pk>/', views.category_page, name='category'),
    path('posts/<str:pk>/', views.post_detail, name='post_detail'),

    path('login/', views.login_view, name='login'),
    path('registration/', views.register_view, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('create/', views.create_article_view, name='create'),
    path('delete/<int:pk>/', views.delete_post, name='delete'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update'),
    path('search/', views.search, name='search'),
    path('vote/<int:post_id>/<str:action>/', views.add_vote, name='add_vote'),
]

# posts/all/
# posts/3


"""
сделать страницу контактов

создать html файл
cоздать для него def
создать новый path в urls.py

about/
faq/
"""

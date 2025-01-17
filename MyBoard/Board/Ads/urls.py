from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(PostsList.as_view()), name='posts_list'),
    path('<int:pk>/', cache_page(60*3)(PostDetail.as_view()), name='post'),
    path('post/create/', PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('category/<int:category_pk>/', cache_page(60*3)(CategoryList.as_view()), name='category_list'),
    path('personal/', Personal.as_view(), name='personal'),
    path('accept_response/<int:response_id>/', accept_response, name='accept_response'),
    path('deny_response/<int:response_id>/', deny_response, name='deny_response'),
    path('confirm/', ConfirmUser.as_view(), name='confirm_user'),
    path('posts/category/<int:pk>/subscribe/', subscribe, name='subscribe'),
]
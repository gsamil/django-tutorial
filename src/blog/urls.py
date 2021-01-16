from django.urls import path
from .views import (
    ArticleDetailView,
    ArticleListView
)

app_name = "articles"
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    # path('create/', product_create_view, name='article-create'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    # path('<int:id>/update', product_update_view, name='article-update'),
    # path('<int:id>/delete/', product_delete_view, name='article-delete'),
]

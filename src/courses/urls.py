from django.urls import path
from .views import (
    my_fbv,
    CourseView
)

app_name = "courses"
urlpatterns = [
    # path('', my_fbv, name='courses-list')

    path('', CourseView.as_view(template_name='contact.html'), name='article-list'),
    # path('create/', ArticleCreateView.as_view(), name='article-create'),
    # path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    # path('<int:id>/update', ArticleUpdateView.as_view(), name='article-update'),
    # path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]

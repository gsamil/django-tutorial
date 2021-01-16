from django.urls import path
from .views import (
    my_fbv,
    CourseView,
    CourseListView,
    MyCourseListView
)

app_name = "courses"
urlpatterns = [
    # path('', my_fbv, name='courses-list')

    path('', CourseListView.as_view(), name='article-list'),
    # path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/', CourseView.as_view(), name='courses-detail'),
    # path('<int:id>/update', ArticleUpdateView.as_view(), name='article-update'),
    # path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]

from django.urls import path
from pages.views import HomePageView, BlogDetailView, BlogDeleteView, BlogUpdateView, BlogCreateView

urlpatterns = [
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("", HomePageView.as_view(), name="home"),
    path("<int:pk>/edit/", BlogUpdateView.as_view(),name="post_edit"),
    path("<int:pk>/delete/", BlogDeleteView.as_view(),name="post_delete"),
    path("new/", BlogCreateView.as_view(), name="post_new"),
]

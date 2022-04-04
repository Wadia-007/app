from django.urls import path
from blog.views import SearchView, about, tc, advertise, contact, privacy, editorial, CategoryView, ContactView, PostListView, PostCreateView, PostUpdateView, PostDeleteView,postdetail
from blog import views

urlpatterns = [
    path('about', about.as_view(), name="about"),
    path('privacy', privacy.as_view(), name="privacy"),
    path('editorial', editorial.as_view(), name="editorial"),
    path('tc', tc.as_view(), name="tc"),
    path('advertise', advertise.as_view(), name="advertise"),
    path('contact', contact.as_view(), name="contact"),

    path('search', SearchView.as_view(), name="search"),
    path('category/<slug:slug>', CategoryView.as_view(), name="category"),
    path('contact-us',ContactView.as_view(), name="contact-us"),

    path('', PostListView.as_view(), name="index"),
    path('posts/<str:slug>', postdetail, name="post-detail"),
    path('posts', PostCreateView.as_view(), name="post-create"),
    path('posts/<slug:slug>/update', PostUpdateView.as_view(), name="post-update"),
    path('posts/<slug:slug>/delete', PostDeleteView.as_view(), name="post-delete"),
]
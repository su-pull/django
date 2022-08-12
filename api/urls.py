from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import CreateUserView, DocsListView, DocsRetrieveView, PostListView, PostRetrieveView


router = routers.DefaultRouter()

urlpatterns = [
    path('list-docs', DocsListView.as_view(), name='list-docs'),
    path('list-docs/<slug:slug>/', DocsRetrieveView.as_view(), name='docs_detail'),
    path('list-post', PostListView.as_view(), name='list-post'),
    path('list-post/<slug:slug>/', PostRetrieveView.as_view(), name='post_detail'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
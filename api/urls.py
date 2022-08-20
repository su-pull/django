from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import CreateUserView, DocsListView, DocsRetrieveView, TalkListView, TalkRetrieveView, BuildListView, BuildRetrieveView


router = routers.DefaultRouter()

urlpatterns = [
    path('list-docs', DocsListView.as_view(), name='list-docs'),
    path('list-docs/<slug:slug>/', DocsRetrieveView.as_view(), name='docs_detail'),
    path('list-talk', TalkListView.as_view(), name='list-talk'),
    path('list-talk/<slug:slug>/', TalkRetrieveView.as_view(), name='talk_detail'),
    path('list-build', TalkListView.as_view(), name='list-build'),
    path('list-build/<slug:slug>/', TalkRetrieveView.as_view(), name='build_detail'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]

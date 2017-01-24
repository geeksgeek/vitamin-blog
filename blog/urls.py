# blog/urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),		# ^$ 문자열이 아무것도 없는 경우
]

# mysite/urls.py

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [ 
	# url(r'^$', 'mysite.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'', include('blog.urls')),		# 들어오는 모든 접속 요청을 blog.urls 로 전송
]

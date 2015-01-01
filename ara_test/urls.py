from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'ara_test.views.ara_home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^teacher/new$', 'teacher.views.new_teacher', name='new_teacher'),
    url(r'^headmaster/new$', 'head_master.views.new_headmaster', name='new_headmaster'),
)

urlpatterns += patterns(
    'django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'login.html'}, name='login_page'),
    url(r'^logout/$', 'logout', {'next_page': 'home'}, name='logout_page')
)
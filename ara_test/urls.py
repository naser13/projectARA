from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'ara_test.views.ara_home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^teacher/new$', 'teacher.views.new_teacher', name='new_teacher'),
    url(r'^headmaster/new$', 'head_master.views.new_headmaster', name='new_headmaster'),
    url(r'^school/new$', 'school.views.new_school', name='new_school')
)

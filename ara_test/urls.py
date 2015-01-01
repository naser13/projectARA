from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import SignUpView

urlpatterns = patterns('',
    url(r'^$', 'ara_test.views.ara_home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^teacher/new$', 'teacher.views.new_teacher', name='new_teacher'),
    url(r'^headmaster/new$', 'head_master.views.new_headmaster', name='new_headmaster'),
    url(r'^sign_up$', SignUpView.as_view(), name='user_sign_up')
)

urlpatterns += patterns(
    'django.contrib.auth.views',
    url(r'^login/$' , 'login',
        {'template_name' : 'login.html'},
        name= 'login_page'),
    url(r'^logout/$' , 'logout',
        {'next_page' : 'home'},
        name='logout_page')
)
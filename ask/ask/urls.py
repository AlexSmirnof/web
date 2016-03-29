from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('qa.views',
	url(r'^$', 'new_questions', name='home'),
	url(r'^login/$', 'login', name='login'),
	url(r'^signup/$', 'signup', name='signup'),
	url(r'^question/(?P<id>[0-9]+)/$', 'one_question', name='question'),
	url(r'^ask/$', 'ask', name='ask'),
	url(r'^popular/$', 'populars', name='popular'),   
	url(r'^new/$', 'new_questions', name='new'),
	url(r'^answer/$', 'answer', name='answer'),    
)

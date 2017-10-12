"""url shemes for learning_logs"""

from django.conf.urls import url

from . import views

urlpatterns = [
    #Homepage
    url(r'^$', views.index, name = 'index'),
    #show all topics
    url(r'^topics/$', views.topics, name = 'topics'),
    #show topic's detail
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name = 'topic'),
    #page for new topic
    url(r'^new_topic/$', views.new_topic, name = 'new_topic'),
    #Page for new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    #Page for entry edit
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry')
    
]

"""url shemes for learning_logs"""

from django.conf.urls import url

from . import views

urlpatterns = [
    #Homepage
    url(r'^$', views.index, name = 'index'),
    #show all topics
    url(r'^topics/$', views.topics, name = 'topics'),
    #show topic's detail
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name = 'topic')

]

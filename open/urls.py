from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'open'

urlpatterns = [
    path('about/',views.AboutView.as_view(),name='about'),
    path('',views.StoryListView.as_view(),name='story_list'),
    url(r'^story/(?P<pk>\d+)/$',views.StoryDetailView.as_view(),name='story_detail'),
    path('story/create/',views.StoryCreateView.as_view(),name='story_create'),
    url(r'^story/(?P<pk>\d+)/update?$',views.StoryUpdateView.as_view(),name='story_update'),
    path('draftlist/',views.DraftListView.as_view(),name='draft'),
    url(r'^story/(?P<pk>\d+)/delete/$',views.StoryDeleteView.as_view(),name='story_delete'),
    url(r'^story/(?P<pk>\d+)/add_review_to_story/$',views.add_review_to_story,name='add_review_to_story'),
    url(r'^story/(?P<pk>\d+)/publish/$',views.story_publish,name='publish'),
    url(r'^story/(?P<pk>\d+)/review_approve/$',views.review_approval,name='review_approval'),
    url(r'^story/(?P<pk>\d+)/review_remove/$',views.review_deletion,name='review_deletion'),
]
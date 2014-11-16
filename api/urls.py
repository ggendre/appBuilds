from django.conf.urls import patterns, url

from api import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),

    # ex: /api/apps/
    url(r'^apps/$', views.apps, name='apps'),

    # ex: /api/app/create/
    #url(r'^apps/create/$', views.appCreate, name='appCreate'),
    # ex: /api/app/myApp/
    #url(r'^apps/(?P<appName>\w+)/$', views.appView, name='appView'),
    # ex: /api/app/myApp/update
    #url(r'^apps/(?P<appName>\w+)/update/$', views.appUpdate, name='appUpdate'),
    # ex: /api/app/myApp/destroy
    #url(r'^apps/(?P<appName>\w+)/destroy/$', views.appDestroy, name='appDestroy'),

    # ex: /api/app/myApp/builds
    url(r'^apps/(?P<appName>\w+)/builds/$', views.builds, name='builds'),
    # ex: /api/app/myApp/build/create/
    url(r'^apps/(?P<appName>\w+)/build/create/$', views.buildCreate, name='buildCreate'),
    # ex: /api/app/myApp/build/1.0.2/
    url(r'^apps/(?P<appName>\w+)/build/(?P<buildNumber>\w+)/$', views.buildView, name='buildView'),
    # ex: /api/app/myApp/build/1.0.2/update/
    url(r'^apps/(?P<appName>\w+)/build/(?P<buildNumber>\w+)/update/$', views.buildUpdate, name='buildUpdate'),
    # ex: /api/app/myApp/build/1.0.2/destroy/
    url(r'^apps/(?P<appName>\w+)/build/(?P<buildNumber>\w+)/destroy/$', views.buildDestroy, name='buildDestroy'),


    # ex: /api/team/create/
    # ex: /api/team/join/theirTeam/
    # ex: /api/team/myTeam/
    # ex: /api/team/myTeam/destroy/
    # ex: /api/team/myTeam/invite/toto
    # ex: /api/team/myTeam/remove/toto
    # ex: /api/team/myTeam/accept/toto
    # ex: /api/team/myTeam/decline/toto

    # ex: /api/team/myTeam/update
    # ex: /api/team/myTeam/accept/toto
    # ex: /api/team/myTeam/decline/toto
    
    

    # ex: /api/profile/
    # ex: /api/profile/create/
    # ex: /api/profile/update/
    # ex: /api/profile/destroy/
    
    

    # ex: /api/profiles/search (for team creation, a la github)

)
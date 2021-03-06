from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'planner.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^dashboard', 'planner.views.dashboard.dashboard', name='dashboard'),
                       url(r'^add_subject', 'planner.views.subjects.add_subject', name='add_subject'),
                       )

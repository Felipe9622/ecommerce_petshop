import debug_toolbar
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from tasks import views
from django.conf.urls import url



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^export-exl/$', views.export, name='export'),
    url(r'^export-csv/$', views.export, name='export'),
    path('', include('tasks.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('task/', include('tasks.urls')),
    #-------------------debug_toolbar----------------------#
    path('__debug__/', include(debug_toolbar.urls)),
    #-------------------debug_toolbar-end---------------------#

    
]

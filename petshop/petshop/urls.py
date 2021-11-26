import debug_toolbar
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('task/', include('tasks.urls')),
    #-------------------debug_toolbar----------------------#
    path('__debug__/', include(debug_toolbar.urls)),
    #-------------------debug_toolbar-end---------------------#

    
]

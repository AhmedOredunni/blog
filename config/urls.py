from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), #for login/logout
    path('accounts/', include('accounts.urls')), # for signing up app
    path('', include('blog.urls'))
]

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt.views import obtain_jwt_token

schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest')),
    path('api-token-auth', obtain_jwt_token),
    path('user/', include(('app_dir.user.urls', 'user'), namespace='user')),
    path('api/user/', include(('app_dir.user.api.urls', 'user_api'), namespace='user_api')),
    path('api/module/', include(('app_dir.module.api.urls', 'module_api'), namespace='module_api')),
    url(r'^$', schema_view)
]


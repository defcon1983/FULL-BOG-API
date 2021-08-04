from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from apps.blog.views import (
    CategoryListAPIView,
    BlogListAPIView,
    BlogCortoListAPIView
)
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

router = routers.DefaultRouter()
router.register('category-list', CategoryListAPIView)
router.register('blog-list', BlogListAPIView)
router.register('blog-corto-list', BlogCortoListAPIView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),

    path('', include('apps.users.urls')),

    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('docs/', include_docs_urls(title='documentacion DRF', public=True)),
]
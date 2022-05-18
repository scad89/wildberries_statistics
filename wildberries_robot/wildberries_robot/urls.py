from django.contrib import admin
from .yasg import urlpatterns as doc_urls
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from cards.views import ArticleViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,)

router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/statistics/', include('cards.urls')),
    path('api/v1/', include('authentication.urls')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += doc_urls

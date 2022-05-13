from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from cards.views import ArticleViewSet, RecordCardListView

router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)
router.register(r'cards', RecordCardListView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('api/v1/', include(router.urls)),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

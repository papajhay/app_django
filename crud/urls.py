from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.conf.urls.i18n import i18n_patterns
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    # formulaire setlang
    path('i18n/', include('django.conf.urls.i18n')),  
    
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    #  Documentation Swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    # API principale
    path('api/products/', include('app.products.api_urls')),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
] + debug_toolbar_urls()

# ===  TOUT LE SITE PUBLIC ET ADMIN EN MULTILINGUE ===
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('app.urls')), 
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

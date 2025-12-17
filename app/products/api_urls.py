from rest_framework.routers import DefaultRouter
from .api_views import ProductViewSet  # ← ici on importe depuis api_views

router = DefaultRouter()
router.register(r'', ProductViewSet, basename='product')

urlpatterns = router.urls
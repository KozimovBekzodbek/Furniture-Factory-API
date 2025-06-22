from rest_framework.routers import DefaultRouter
from common import views


router = DefaultRouter()
router.register(r'orders', views.OrderViewSet)
router.register(r'workers', views.WorkerViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'raw-materials', views.RawMaterialViewSet)
router.register(r'finished-products', views.FinishedProductViewSet)

urlpatterns = router.urls

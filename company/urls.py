from rest_framework.routers import SimpleRouter
from company import views


router = SimpleRouter()

router.register(r'company', views.CompanyViewSet)
router.register(r'tier', views.TierViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register(r'officecommission', views.OfficeCommissionViewSet)
urlpatterns = router.urls

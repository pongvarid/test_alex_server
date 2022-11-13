from rest_framework.routers import SimpleRouter
from account import views


router = SimpleRouter()

router.register(r'userprofile', views.AccountViewSet)
router.register(r'referrer', views.ReferrerViewSet)
router.register(r'commission', views.CommissionViewSet)

urlpatterns = router.urls

from rest_framework.routers import SimpleRouter
from product import views


router = SimpleRouter()

router.register(r'product', views.ProductViewSet)

urlpatterns = router.urls

from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from api_v1.views import ProductViewSet, LogoutView, OrderViewSet, OrderProductViewSet

app_name = "api_v1"

router = DefaultRouter()
router.register("products", ProductViewSet)
router.register("order", OrderViewSet)
router.register("orderproduct", OrderProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth'),
]
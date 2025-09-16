from django.urls import include, path
from reporting.views import ReportingViewSet
from reporting.views import OrderViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('orders', OrderViewSet, basename='orders')

urlpatterns = [
    path('reporting/', ReportingViewSet.as_view(), name='reporting'),
    path('', include(router.urls))
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view(), name='menu-items-list'),
    path('menu-items/<int:pk>/', views.SingleMenuItemsView.as_view(), name='menu-items-detail'),

    path('bookings/', include(router.urls)),
]

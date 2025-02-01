from django.utils.dateparse import parse_date
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from . import models
from . import serializers


class MenuItemsView(generics.ListCreateAPIView):
    queryset = models.Menu.objects.all().order_by('id')
    serializer_class = serializers.MenuSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class SingleMenuItemsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Menu.objects.all().order_by('id')
    serializer_class = serializers.MenuSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all().order_by('id')
    serializer_class = serializers.BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()

        date_booking = self.request.query_params.get('booking_date', None)

        if date_booking:
            date = parse_date(date_booking)
            if date:
                queryset = queryset.filter(booking_date=date).order_by('id')

        return queryset

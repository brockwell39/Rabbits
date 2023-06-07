from rest_framework import viewsets

# Create your views here.
from rest_framework.permissions import IsAuthenticated

from bunnies.models import Bunny, RabbitHole
from bunnies.permissions import RabbitHolePermissions
from bunnies.serializers import BunnySerializer, RabbitHoleSerializer


class RabbitHoleViewSet(viewsets.ModelViewSet):
    serializer_class = RabbitHoleSerializer
    permission_classes = (IsAuthenticated, RabbitHolePermissions)
    queryset = RabbitHole.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def filter_queryset(self, request, view, queryset):
        # the filter needs to make use of has_object_permission but not quite sure how to get it to work
        # print("Alex", permission_classes)
        for q in queryset:
            print(q)
            print("Alex", RabbitHolePermissions.has_object_permission(self, request, view, q))
        # print(queryset)
        # for x in queryset:
        #     print(x.has_object_permission)
        # queryset = super().filter_queryset(queryset, permission_classes)
        # print(permission_classes)
        return queryset


class BunnyViewSet(viewsets.ModelViewSet):
    serializer_class = BunnySerializer
    permission_classes = (IsAuthenticated,)
    queryset = Bunny.objects.all()
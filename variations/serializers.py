from rest_framework import serializers
from .models import *
from van.serializers import VanDetailSerializer


class VariationSerializer(serializers.ModelSerializer):
    guide_items = serializers.SerializerMethodField
    class Meta:
        model = Variation
        fields = ['user', 'van_items', 'driver_items', 'guide_items', 'from_date', 'to_date']

        def get_guideitems(self, obj):
            if obj.guide_items is None:
                obj.guide_items = 0

class DisplayVariations(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = '__all__'


class CalculateSerializer(serializers.ModelSerializer):
    van_items = VanDetailSerializer()
    class Meta:
        model = Variation
        fields = ['user', 'van_items', 'driver_items', 'guide_items', 'from_date', 'to_date']



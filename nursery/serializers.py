from rest_framework import serializers
from .models import Plant,Order,OrderProperty,Nursery
from users.models import CustomUser

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ("name",)

class NurserySerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.owner.name
        }

class PlantSerializer(serializers.ModelSerializer):
    nursery = NurserySerializer(read_only=True)
    class Meta:
        model = Plant
        fields = "__all__"
    
    def create(self, validated_data):
        validated_data.pop('nursery',None)
        if self.context['request'].user.is_authenticated:
            plant = Plant.objects.create(nursery=self.context['request'].user.nursery,**validated_data)
        else:
            raise serializers.ValidationError("You Are UnAuthenticated!!!")
        return plant

class OrderPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProperty
        fields = "__all__"
        extra_kwargs = {'order': {'required': False}}

    def to_representation(self, instance):
        return {
            'id': instance.plant.id,
            'order': instance.order.id,
            'quantity':instance.quantity,
        }

class OrderSerializer(serializers.ModelSerializer):
    plants = OrderPropertySerializer(many=True)

    class Meta:
        model = Order
        fields = ("id","owner","plants",)
        extra_kwargs = {'owner': {'read_only': True},
                        'plants':{'required':False}
                        }

    def create(self, validated_data):
        plants_data = validated_data.pop('plants',None)
        if not plants_data:
            raise serializers.ValidationError("You Forgot to Add Plants!!!")
        validated_data.pop('owner',None)
        order = Order.objects.create(owner=self.context['request'].user)
        for plant_data in plants_data:
            plant_data.pop('order',None)
            try:
                OrderProperty.objects.create(order=order, **plant_data)
            except Exception as e:
                raise serializers.ValidationError(e)
        return order

a={
    "plants": [
{
"plant":1,
"quantity":25
},
{
"plant":2,
"quantity":205
}
]
}
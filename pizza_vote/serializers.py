from rest_framework import serializers

from .models import Pizza, Topping


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ('name',)


class PizzaSerializer(serializers.ModelSerializer):
    toppings = ToppingSerializer(many=True)

    class Meta:
        model = Pizza
        fields = ('id', 'name', 'toppings')


class VoteSerializer(serializers.Serializer):
    choice_id = serializers.IntegerField()


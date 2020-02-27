from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Pizza, Vote
from .serializers import PizzaSerializer, VoteSerializer


class PizzaView(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


@api_view(['POST'])
def vote_view(request):
    """ Handle vote for specific pizza by id eg. {"choice_id":3} """
    pizza = get_object_or_404(Pizza, pk=request.data['choice_id'])
    serializer = VoteSerializer(data=request.data)
    if serializer.is_valid():
        obj, created = Vote.objects.get_or_create(pizza=pizza)
        obj.votes += 1
        obj.save()
        print(obj)
        return Response(f"Voted for {pizza}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def result_view(request):
    """ Return all pizzas voted for """
    all_obj = Vote.objects.all()
    result = {obj.pizza.name: obj.votes for obj in all_obj}
    print(result)
    return Response(result)

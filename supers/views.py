from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Super
from .models import SuperType
from . serializers import SupersSerializer
from super_types.serializers import SuperTypeSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['GET', 'POST'])
def supers_list(requst):
    if requst.method == 'GET':

        supertype_name = requst.query_params.get('super_type_id')
        
        supers = Super.objects.all()
        if supertype_name:
            supers = supers.filter(super_type_id=supertype_name)
        serializer = SupersSerializer(supers, many=True)
        return Response(serializer.data)

    elif requst.method == 'POST':
        serializer = SupersSerializer(data=requst.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    supers = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SupersSerializer(supers)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SupersSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def hero_villain_lists(request):
    heros = Super.objects.filter(super_type_id=1)
    villains = Super.objects.filter(super_type_id=2)
    heros_serializer = SupersSerializer(heros, many=True)
    villains_serilaizer = SupersSerializer(villains, many=True)

    custom_response_dictionary = {
        'heros': heros_serializer.data,
        'villains': villains_serilaizer.data
    }
    return Response(custom_response_dictionary)

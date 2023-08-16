from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def get_text(request):
    if request.method == 'POST':
        received_text = request.data.get('text')
        print(received_text)
        return Response({'result': received_text})

def set_speech(request):
    pass

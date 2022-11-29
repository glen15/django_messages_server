from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Cozmessage
from .serializers import CozmessageSerializer

class Cozmessages(APIView):

    def get(self, request):
        all_messages = Cozmessage.objects.all()
        serializer = CozmessageSerializer(all_messages, many=True)
        return Response(
            serializer.data
        )
    def post(self, request):
        serializer = CozmessageSerializer(data=request.data)
        if serializer.is_valid():
            new_message = serializer.save()
            return Response({"id" : new_message.id})
        else:
            return Response(serializer.errors)
        

class MessagesByGithubId(APIView):
    def get(self, request, githubId):
        roomname = request.query_params.get("roomname")
        if roomname:
            messages = Cozmessage.objects.filter(username=githubId, roomname=roomname)
        else:
            messages = Cozmessage.objects.filter(username=githubId)
        serializer = CozmessageSerializer(messages, many=True)
        return Response(serializer.data)

class MessageClear(APIView):
    def delete(self, request, githubId):
        messages = Cozmessage.objects.filter(username=githubId)
        messages.delete()
        return Response({"message": "message initialized!"})
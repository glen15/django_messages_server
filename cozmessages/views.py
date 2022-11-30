from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cozmessage, Submit
from .serializers import CozmessageSerializer, SubmitSerializer

class Cozmessages(APIView):

    def get_object(self, githubId):
        try:
            return Submit.objects.get(githubId=githubId)
        except Submit.DoesNotExist:
            return None

    def get(self, request):
        all_messages = Cozmessage.objects.all()
        serializer = CozmessageSerializer(all_messages, many=True)
        return Response(
            serializer.data
        )
    def post(self, request):
        githubId = request.data['username']
        github_user = self.get_object(githubId)
        if github_user:
            submit_serializer = SubmitSerializer(github_user, {"postMethod":True}, partial=True)
            if submit_serializer.is_valid():
                submit_serializer.save()
        
        serializer = CozmessageSerializer(data=request.data)
        if serializer.is_valid():
            new_message = serializer.save()
            return Response({"id" : new_message.id})
        else:
            return Response(serializer.errors)
        

class MessagesByGithubId(APIView):

    def get_object(self, githubId):
        try:
            return Submit.objects.get(githubId=githubId)
        except Submit.DoesNotExist:
            return None

    def get(self, request, githubId):
        github_user = self.get_object(githubId)
        if github_user:
            submit_serializer = SubmitSerializer(github_user, {"getMethod":True}, partial=True)
            if submit_serializer.is_valid():
                submit_serializer.save()
        
        roomname = request.query_params.get("roomname")
        if roomname:
            messages = Cozmessage.objects.filter(username=githubId, roomname=roomname)
        else:
            messages = Cozmessage.objects.filter(username=githubId)
        serializer = CozmessageSerializer(messages, many=True)
        return Response(serializer.data)

class MessageClear(APIView):
    def get_object(self, githubId):
        try:
            return Submit.objects.get(githubId=githubId)
        except Submit.DoesNotExist:
            return None

    def delete(self, request, githubId):
        github_user = self.get_object(githubId)
        if github_user:
            submit_serializer = SubmitSerializer(github_user, {"deleteMethod":True}, partial=True)
            if submit_serializer.is_valid():
                submit_serializer.save()

        messages = Cozmessage.objects.filter(username=githubId)
        messages.delete()
        return Response({"message": "message initialized!"})

class Submits(APIView):
    def get(self, request):
        print(request.data)
        all_list = Submit.objects.all()
        serializer = SubmitSerializer(all_list, many=True)
        return Response(
            serializer.data
        )

    def post(self, request):
        serializer = SubmitSerializer(data=request.data)
        if serializer.is_valid():
            new_submit = serializer.save()
            return Response(SubmitSerializer(new_submit).data)
        else:
            return Response(serializer.errors)


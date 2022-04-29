from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from django.core.files.storage import FileSystemStorage
from django.core.files.temp import NamedTemporaryFile
from rest_framework import authentication
from rest_framework import permissions
# Create your views here.

class Upload(APIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        # print(request.data.get("name"))
        # print(request.data)
        # newfile = request.data['file']
        # print(newfile)
        # file_dict = request.FILES
        # print(file_dict)
        # print(file_dict.name)
        return Response({"status":"ok",
                         "file":"file_example_WAV_1MG.wav"})
        print(request.FILES)
        # newfile = ...
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # uploaded_file_url = fs.url(filename)
        return Response({"status":"ok",
                        "file":"xxx.txt"})

class Predict(APIView):
    def get(self, request):
        return Response({"status":"ok",
                        "file":"xxx.txt"})
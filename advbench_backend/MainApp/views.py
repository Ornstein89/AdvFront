from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.core.files.temp import NamedTemporaryFile
from django.http import FileResponse, HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.parsers import FormParser, JSONParser, FileUploadParser, MultiPartParser
# Create your views here.

# def send_file(response, filename):

#     img = open("../advbench_frontend/dist/favicon.ico", 'rb')

#     response = FileResponse(img)

#     return response

# def send_js(request):
#     filename = request.path.strip("/")
#     data = open("../advbench_frontend/dist" + filename, "rb").read()
#     return HttpResponse(data, mimetype="application/javascript")

# class VueView(TemplateView):
#     template_name = "index.html"

class Upload(APIView):
    # https://stackoverflow.com/a/64582388/12691808
    
    # authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)
    parser_classes  = [FormParser, MultiPartParser, ]
    def post(self, request):
        # print(request.data.get("name"))
        # up_file = request.FILES['files']
        print(request.body)
        acceptedfile = None
        try:
            acceptedfile = request.data["files"]
            print("newfile = ", acceptedfile)
        except:
            return Response({"status":"error",
                         "message"  :"В отправленных данных не найден файл"})
        savedfileurl = None
        try:
            fs = FileSystemStorage(location="uploads")
            savedfilename = fs.save(acceptedfile.name, acceptedfile)
            savedfileurl = fs.url(savedfilename)
        except:
            return Response({"status":"error",
                             "message":f"Не удалось сохранить файл {acceptedfile.name} на сервере"})
        # print(newfile)
        # file_dict = request.FILES
        # print(file_dict)
        # print(file_dict.name)
        return Response({"status":"ok",
                         "fileurl"  :savedfileurl})
        print(request.FILES)
        # newfile = ...
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # uploaded_file_url = fs.url(filename)

class Predict(APIView):
    def get(self, request):
        return Response({"status":"ok",
                        "file":"xxx.txt"})
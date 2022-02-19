from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from ..models import User
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from ..custom import *


# Create your views here.

class RegisterAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSer
    permission_classes = [AllowAny,]


'''class SignupAPIView(APIView):
    permission_classes = [AllowAny,]

    def post(self,request):
        serializer=SignupAPIView(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            data=serializer.data
            return Response({'message':'user created successfully.','data':[]},status=HTTP_200_OK)
        return Response(get_serializer_errors(serializer),status=HTTP_400_BAD_REQUEST)'''


class SignupAPIView(APIView):
    permission_classes =[AllowAny,]
    def post(self,request):
        serializer=SignupSer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data=serializer.data
            return Response({'Success':'user created successfully','data':data},status=HTTP_200_OK)
        return Response(get_serializer_errors(serializer),status=HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    permission_classes = [AllowAny,]
    def post(self, request):
        serializer=LoginSer(data=request.data)
        if serializer.is_valid():
            return Response({'Success':'login successfully','data':serializer.data},status=HTTP_200_OK)
        return Response(get_serializer_errors(serializer),status=HTTP_400_BAD_REQUEST)


class UpdateAPIView(APIView):
    permission_classes =[IsAuthenticated,]
    def post(self, request):
        print(request.user)
        request.user.first_name=request.data.get('first_name')
        request.user.last_name=request.data.get('last_name')
        request.user.save()
        return Response({'Success':'user created successfully'},status=HTTP_200_OK)


class UpdateAPIView2(generics.UpdateAPIView):
    permission_classes =[IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class=UpdateSer1    

class DeleteAPIView(generics.DestroyAPIView):
    permission_classes =[IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class=DeleteSer

class DeleteAPIView1(APIView):
    permission_classes =[IsAuthenticated,]
    def delete(self,request):
        print(request.data.get('username'))
        request.user.delete()
        return Response({'Success':'user deleted successfully'},status=HTTP_200_OK)
    

class DeleteAPIView2(APIView):
    permission_classes =[IsAuthenticated,]
    def delete(self,request,**kwargs):
        try:
            user = User.objects.get(pk=self.kwargs.get('pk'))
            return Response({'Success':'user deleted successfully'},status=HTTP_200_OK)
        
        except Exception as e:
            return Response({'Error':str(e)},status=HTTP_400_BAD_REQUEST)



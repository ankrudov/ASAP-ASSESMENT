from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .serializers import MemberSerializer
from .models import Member


class MemberView(APIView):
    def post(self,request):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request, id=None):
        if id:
            item = Member.objects.get(id=id)
            serializer = MemberSerializer(item)
            return Response({"status":"success","data":serializer.data}, status=status.HTTP_200_OK)
        items = Member.objects.all()
        serializer = MemberSerializer(items, many=True)
        return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)


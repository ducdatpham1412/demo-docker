from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
import os


class Chat(GenericAPIView):
    def get(self, request):
        return Response({
            'success': os.environ.get('MYSQL_USER'),
        }, 200)

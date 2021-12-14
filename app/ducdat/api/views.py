from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status


class Ducdat(GenericAPIView):
    def get(self, request):
        res = {
            'name': 'Duc Dat',
            'school': 'Doffy Technology'
        }
        return Response(res, status=status.HTTP_200_OK)

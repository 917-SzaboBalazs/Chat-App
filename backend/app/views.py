from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class MyView(APIView):

    def get(self, request, *args, **kwargs):
        return Response(data={"message": "Hello"})

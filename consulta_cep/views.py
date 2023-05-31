from rest_framework.views import APIView
from rest_framework.response import Response
import requests

    
class ConsultaCep(APIView):
    
    def get(self, request):
        cep =  request.GET.get('cep')
        url = "https://brasilapi.com.br/api/cep/v1/" + cep
        response = requests.get(url)
        if  response.status_code == 200:
            data = response.json()
            return Response(data)
        else:
            return Response(status=response.status_code)
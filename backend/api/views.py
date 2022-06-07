# from django.http import HttpResponse, JsonResponse
import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     # request -> HttpRequest -> Django
#     # print(dir(request))
#     #request.body
#     # print(request.GET) #url query params
#     # print(request.POST)
#     # body = request.body #byte string of JSON data
#     # data = {}
#     # try:
#     #     data = json.loads(body) # string of JSON data -> Python dict
#     # except:
#     #     pass
#     # print(data)
#     # data['params'] = dict(request.GET)
#     # data['headers'] = dict(request.headers)
#     # data['content_type'] = request.content_type
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         data = ProductSerializer(instance).data
#         # data['id'] = model_data.id
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.price
#         # data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#     return Response(data)
#     #     json_data_str = json.dumps(data)
        
#     #     # model instance (model_data)
#     #     # turn a Python dict
#     #     # return JSON to my client
#     #     # serialization
#     # return JsonResponse(json_data_str, headers={"content-type": "application/json"})
    
@api_view(["POST"])
def api_home(request, *args, **kwargs):
    # Validates the format of the data being sent from the client is inline with the format depicted through serialzer
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        print(serializer.data)
        data = serializer.data
        return Response(data)
from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home (request,*args,**kwargs):
    data=request.data
    serializer=ProductSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
      # data = serializer.save()
      print(data)
      data=serializer.data
      return Response(serializer.data)
    return Response({'invalid':'not A GOd data'},status=400)
 
 
 
 
 
 
 
    # instance=Product.objects.all().order_by('?').first()
    # data={}
    # if instance:
    #   #  data=model_to_dict(instance,fields=['id','title','price','sale_price'])
    #    data= ProductSerializers(instance).data
    
    # return JsonResponse(data)


    # body = request.body # byte string of JSON data
    # data = {}
    # try:
    #     data = json.loads(body) # string of JSON data -> Python Dict
    # except:
    #     pass
    # print(data)
    # # data['headers'] = request.headers # request.META ->
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    # return JsonResponse(data)
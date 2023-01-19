from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict

def api_home (request,*args,**kwargs):

    model_data=Product.objects.all().order_by('?').first()
    data={}
    if model_data:
       data=model_to_dict(model_data,fields=['id','title','price'])
    return JsonResponse(data)


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
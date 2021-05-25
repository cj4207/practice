from django.views import View
from django.http import JsonResponse, request
from .models import Owner, Dog
import json
# Create your views here.

class SampleOwnerView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            Owner.objects.create(name=data['name'],email=data['email'],age=data['age'])
            return JsonResponse({"message":"SUCCESS!"},status=201)
        except KeyError:
            return JsonResponse({"message":"INVALID_KEY"}, status=400)
    
    def get(self, request):
        '''owners = Owner.objects.all()
        owner_list=[]
        for owner in owners:
            owner_={}
            owner_['name']=owner.name
            owner_['email']=owner.email
            owner_['age']=owner.age
            owner_list.append(owner_)'''
        owners = Owner.objects.all()
        owner_list=[]
        for owner in owners:
            owner_={}
            dogs = Dog.objects.filter(owner_id=owner.id)
            dog_list = [{'name':dog.name,'age':dog.age} for dog in dogs]
            owner_['name']=owner.name
            owner_['email']=owner.email
            owner_['age']=owner.age
            owner_['dogs']=dog_list
            owner_list.append(owner_)
        return JsonResponse({'result':owner_list}, status=200)

class SampleDogView(View): 
    def post(self, request):     
        try:
            data = json.loads(request.body)   
            dog_owner = Owner.objects.get(name=data['owner'])
            Dog.objects.create(name=data['name'],age=data['age'],owner=dog_owner)
            return JsonResponse({"message":"SUCCESS!"},status=201)
        except KeyError:
            return JsonResponse({"message":"INVALID_KEY"}, status=400)
    
    def get(self, request):
        dogs = Dog.objects.all()
        dogs_list=[]
        for dog in dogs:
            dog_={}
            owners = Owner.objects.filter(id=dog.owner_id)
            dog_owner = [owner.name for owner in owners]
            dog_['name']=dog.name
            dog_['age']=dog.age
            dog_['owner']=dog_owner
            dogs_list.append(dog_)
        return JsonResponse({'result':dogs_list}, status=200)
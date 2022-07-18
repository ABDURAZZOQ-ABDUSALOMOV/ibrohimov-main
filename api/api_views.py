from django.db.models import Q

from __init__ import *
from rest_framework.views import APIView
from rest_framework.response import Response
from user_model.models import User
from api.models import *
from user_model.models import *
from abconfig.settings import DOMAIN
from user_model.serializers import *

from api.api_views import *
from api.new_api_views import *



class ShopDetailView(APIView):
    def get(self, request, pk):

        response = {
            "status" : 200,
        }

        try:
            shop = Shop.objects.get(phone=pk)
            response['data'] = {
                'id' : shop.id,
                'name' : shop.name,
                'description' : shop.description,
                'img' : shop.image.url,
                'viloyat' : shop.viloyat.name,
                'tuman' : shop.tuman.name
                }

        except Exception as e:
            print(e)
            response = {
                "status" : 200,
                "data" : None
            }

        return Response(response)




class ShopFilterView(APIView):
    def get(self, request, pk1, pk2=0):

        resp = {
            'status' : 200,
            }

        payload = []


        if pk2 != 0:
            viloyat = Viloyat.objects.get(pk=pk1)
            tuman = Tuman.objects.get(pk=pk2)

            shops = Shop.objects.filter(Q(viloyat = viloyat) and Q(tuman = tuman))
        else:
            viloyat = Viloyat.objects.get(pk=pk1)


            shops = Shop.objects.filter(viloyat=viloyat)


        for shop in shops:
            payload.append({
                'id' : shop.id,
                'name' : shop.name,
                'description' : shop.description,
                'img' : shop.image.url,
                'viloyat' : shop.viloyat.name,
                'tuman' : shop.tuman.name
            })

        resp['data'] = payload

        return Response(resp)

class ShopsView(APIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


    def get(self, request):
        resp = {
            'status': 200

        }
        payload = []

        shops = Shop.objects.all()

        for shop in shops:
            payload.append({
                'id' : shop.id,
                'name' : shop.name,
                'description' : shop.description,
                'img' : str(DOMAIN + shop.image.url),
                'viloyat' : shop.viloyat.name,
                'tuman' : shop.tuman.name
            })


        resp['data'] = payload
        return Response(resp)

    def post(self, request):
        rd = request.data

        resp = {'status' : 200}

        try:
            name = rd['name']
            description = rd['description']
            password = rd['password']

            pk1 = int(rd['viloyat'])
            pk2 = int(rd['tuman'])
            img = request.FILES['image']
            viloyat = Viloyat.objects.get(pk=pk1)
            tuman = Tuman.objects.get(pk=pk2)


            Shop.objects.create(
                name=name,
                description=description,
                password=password,
                viloyat=viloyat,
                tuman=tuman,
                image=img
            )
        except Exception as e:
            resp = {'status' : 400}


        return Response(resp)


class UsersView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def get(self, request):
        response = {
            "status" : 200,
            "data" : []
            }
        users = User.objects.all()
        payload = []
        for i in users:
            payload.append({
                'id' : i.id,
                'first_name' : i.first_name,
                'last_name' : i.last_name,
                'phone' : i.phone,
                'img' : str(DOMAIN) + i.img.url,
            })


        response['data'] = payload

        return Response(response)

    def post(self, request):
        rd = request.data

        response = {
            'status' : 200
        }

        try:
            first_name = rd['first_name']
            last_name = rd['last_name']
            phone = rd['phone']

            password = '@Qwerty11'
            username = str(first_name + phone + last_name)

            img = request.FILES['img']
            email = username + '1234@gmail.com'

            new_user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,password=password, email=email, phone=phone, img=img)


            print()
            print(username)
            print(first_name)
            print(last_name)
            print(email)
            print(phone)
            print(password)
            print(img.name)
            print(img.size)
            print()

        except:
            response['status'] = 400


        return Response(response)




class UserTestView(APIView):
    def get(self, request, phone):
        response = {
            "status" : 200,
            }

        try:
            user = User.objects.get(phone=phone)
            response['data'] = {
                "id" : user.id,
                "first_name" : user.first_name,
                "last_name" : user.last_name,
                "phone" : user.phone,
                'img' : str(DOMAIN) + user.img.url,
                }

        except Exception as e:
            print(e)
            response = {
                "data" : None
                }

        return Response(response)



class ShopsViewV2(APIView):
    def get(self, request):



        payload = []

        shops = Shop.objects.all()

        for shop in shops:
            payload.append({
                'id' : shop.id,
                'name' : shop.name,
                'description' : shop.description,
                'img' : shop.image.url,
                'viloyat' : shop.viloyat.name,
                'tuman' : shop.tuman.name
            })



        return Response(payload)

    def post(self, request):
        rd = request.data

        resp = {'status' : 200}

        try:
            name = rd['name']
            description = rd['description']
            password = rd['password']

            pk1 = rd['viloyat']
            pk2 = rd['tuman']

            viloyat = Viloyat.objects.get(pk=pk1)
            tuman = Tuman.objects.get(pk=pk2)


            Shop.objects.create(
                name=name,
                description=description,
                password=password,
                viloyat=viloyat,
                tuman=tuman
            )
        except Exception as e:
            resp = {'status' : 400}


        return Response(resp)



class UserDetailView(APIView):
    def get(self, request, id):

        response = {
            "status" : 200,
        }

        try:
            shop = Shop.objects.get(phone=pk)
            response['data'] = {
                'id' : shop.id,
                'name' : shop.name,
                'description' : shop.description,
                'img' : shop.image.url,
                'viloyat' : shop.viloyat.name,
                'tuman' : shop.tuman.name
                }

        except Exception as e:
            print(e)
            response = {
                "status" : 200,
                "data" : None
            }

        return Response(response)


class TumanlarView(APIView):
    def get(self, request, pk):

        viloyat = Viloyat.objects.get(pk=pk)

        tumanlar = Tuman.objects.filter(viloyat=viloyat)

        response = {
            'status' : 200,
            'data' : []
        }

        data = []
        for i in tumanlar:
            data.append(
                {
                    'id' : i.id,
                    'name' : i.name,
                }
            )

        response['data'] = data


        return Response(response)






# ==============================================




# ==============================================
ShopDetailView = ShopDetailView.as_view()
ShopsView = ShopsView.as_view()
ShopFilterView = ShopFilterView.as_view()
ShopsViewV2 = ShopsViewV2.as_view()

UsersView = UsersView.as_view()
UserTestView = UserTestView.as_view()
UserDetailView =  UserDetailView.as_view()
TumanlarView = TumanlarView.as_view()
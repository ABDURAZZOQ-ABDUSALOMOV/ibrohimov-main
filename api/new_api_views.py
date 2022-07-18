
from urllib import response
from __init__ import *
from rest_framework.views import APIView
from rest_framework.response import Response
from user_model.models import User
from api.models import *
from user_model.models import *
from abconfig.settings import DOMAIN
from user_model.serializers import *
from django.db.models import Q
from api.api_views import *
from api.new_api_views import *


class GetShopsView(APIView):

    def get(self, request):
        response = {
            'status' : 200,
            'data' : []
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
                'tuman' : shop.tuman.name,
                'location' : {
                    'lon' : shop.lon,
                    'lat' : shop.lat,
                    }
            })


        response['data'] = payload
        return Response(response)

class PostShopsView(APIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def post(self, request):
        response = {'status' : 400}
        rd = request.data
        try:
            host = User.objects.get(pk=rd['host-id'])
            name = rd['name']
            desc = rd['description']
            password = rd['password']
            pk1 = int(rd['viloyat'])
            pk2 = int(rd['tuman'])
            img = request.FILES['image']
            viloyat = Viloyat.objects.get(pk=pk1)
            tuman = Tuman.objects.get(pk=pk2)

            lat = rd['lat']
            lon = rd['lon']

            print(lat)
            print(lon)

            new_shop = Shop.objects.create(
                host=host,
                name=name,
                description=desc,
                password=password,
                viloyat=viloyat,
                tuman=tuman,
                image=img,
                lat=lat,
                lon=lon
            )

            response['status'] = 200
            response['data'] = [
                {
                    'id' : new_shop.id,
                    'name' : new_shop.name,
                    'description' : new_shop.description,
                    'img' : str(DOMAIN + new_shop.image.url),
                    'viloyat' : new_shop.viloyat.name,
                    'tuman' : new_shop.tuman.name,
                    'location' : {
                        'lon' : new_shop.lon,
                        'lat' : new_shop.lat,
                    }
                }
            ]
        except Exception as e:
            print(e)



        return Response(response)


class AddMemberView(APIView):
    def post(self, request):
        response = {'status' : 200}
        rd = request.data

        user_id = int(rd['user-id'])
        shop_id = int(rd['shop-id'])

        shop = Shop.objects.get(pk=shop_id)
        user = User.objects.get(pk=user_id)
        shop.members.add(user)

        return Response(response)

class MembersListView(APIView):
    def get(self, request, shop_pk):
        response = {
            'status' : 200,
            'data' : []
            }

        try:
            shop = Shop.objects.get(pk=shop_pk)
            for i in shop.members.all():
                response['data'].append(
                    {
                        'id' : i.id,
                        'first_name' : i.first_name,
                        'last_name' : i.last_name,
                        'phone' : i.phone,
                        'image' : str(DOMAIN + i.img.url),
                    }
                )

        except:
            response = {
            'status' : 400,
            'data' : None
            }

        return Response(response)


class ProductsListView(APIView):
    def get(self, request, pk):
        response = {
            'status': 200,
            'data' : []
        }


        shop = Shop.objects.get(pk=pk)
        for i in Product.objects.filter(shop=shop):
            response['data'].append(
                {
                    'id' : i.id,
                    'image1' : str(DOMAIN + i.image1.url),
                    'image2' : str(DOMAIN + i.image2.url),
                    'image3' : str(DOMAIN + i.image3.url),
                    
                    'name' : i.name,
                    'description' : i.description,
                    'count' : i.count,

                    'money_type' : i.currency.name,
                    'type' : i.typee.name,

                    'entry_price' : i.entry_price,
                    'percent' : i.percent,
                    'selling_price' : i.selling_price,
                    'validity_period' : i.validity_period,
                    'enterprise' : i.enterprise,

                }
            )


        return Response(response)


# =================================================================================


GetShopsView = GetShopsView.as_view()
PostShopsView = PostShopsView.as_view()
AddMemberView = AddMemberView.as_view()
MembersListView = MembersListView.as_view()

ProductsListView = ProductsListView.as_view()


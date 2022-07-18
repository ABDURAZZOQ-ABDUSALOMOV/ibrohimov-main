

from django.urls import path
from .api_views import *
from .new_api_views import *
urlpatterns = [
    path('shop/<int:pk>/', ShopDetailView),
    path('shops/', ShopsView),

    path('shops/<int:pk1>/<int:pk2>/', ShopFilterView),
    path('shops/<int:pk1>/', ShopFilterView),

    path('users/', UsersView),
    path('user-test/<str:phone>/', UserTestView),

    path('regions/<int:pk>/', TumanlarView)
]

# New
urlpatterns += [
    path('shops/get/', GetShopsView),
    path('shops/post/', PostShopsView),
    path('shops/add-member/', AddMemberView),
    path('shops/members-list/<int:shop_pk>/', MembersListView),
    path('shops/products-list/<int:pk>/', ProductsListView),
    #MembersListView

#     path('shops/<int:pk>/', ),
#     path('shops/<int:pk>/<int:pk>/', ),

#     path('users/get/', ),
#     path('users/post/', ),

#     path('users-test/<int:phone>/', ),

#     path('regions/<int:pk>/', ),
]

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from api.models import Tuman, Viloyat
from api.views import homepage

from django.shortcuts import redirect

from user_model.models import User

def base(request):
    for i in range(10):
        User.objects.create_user(
            first_name=f'testUserfirstname{i}',
            last_name=f'testUserlastname{i}',
            email=f'lorem{i}ipsum@gmail.com',
            password='password',
            username = f'loremTest{i}'
        )
    return redirect('homePage')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('forPhone.urls')),
    path('api/', include('api.urls')),
    path('lorem-ipsum/', base),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

 

        
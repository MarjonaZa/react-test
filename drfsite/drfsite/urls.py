
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from women.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auz/', include('rest_framework.urls')),
    path('api/v1/women/', WomenListAPIView.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),

]


# router = MyCustomRouter()
# router.register(r'women', WomenViewSet, basename='women') #'^women/$' [name='men-list']>, суть basename в том что dvtcnj women идёт man как быховый
#!!!! если нет кюерисет (queryset = Women.objects.all()) то бейснейм обязателен т.к это штука берёт имя для марщрута
#print(router.urls)


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/womenlist', WomenListAPIView.as_view() ),
#     path('api/v1/womenlist/<int:pk>/' , WomenAPIUpdate.as_view()),
#     path('api/v1/womenAll/<int:pk>/' , WomenAPIAll.as_view()),
# ]



# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/womenlist' , WomenApiiew.as_view()), #откуда здесь .as_view?
#     # as_view Он позволяет Django использовать классы в маршрутах, как если бы это были функции.
#     path('api/v1/womenlist/<int:pk>/' , WomenApiiew.as_view())
# ]
from django.contrib.admin import action
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins, permissions
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Women, Category
from .permissinon import *
from .serializers import WomenSerializer
from rest_framework.permissions import *
# сласс APIView предсавтляет собой некий базовый функционал для работа различных классов
# представлений фрейсфорка джанго рест фреймворк (берёт на себя базовую обработку запросов(типа если нет пост запроса на к-н запрос то пишет что метод пост не разрешён))
# Create your views here.




# class WomenListAPIView(generics.ListCreateAPIView): #тепеь это представление делает всё тоже самое что и WomenApiiew но в 3 бляин сроки фух(*?*:?*8 крч это представление с помощью базового метода ListAPIView
#     queryset = Women.objects.all().select_related('user', 'cat') #ссылаеться на список записей возврщ клиенту
#     serializer_class = WomenSerializer #сериализатор который мы бедм применять
#     permission_classes = (IsAuthenticatedOrReadOnly, )

class WomenListAPIView(generics.ListCreateAPIView): #тепеь это представление делает всё тоже самое что и WomenApiiew но в 3 бляин сроки фух(*?*:?*8 крч это представление с помощью базового метода ListAPIView
    queryset = Women.objects.all() #ссылаеться на список записей возврщ клиенту
    serializer_class = WomenSerializer #сериализатор который мы бедм применять
    permission_classes = (IsAuthenticatedOrReadOnly, )



class WomenAPIUpdate(generics.RetrieveUpdateAPIView ):
    queryset = Women.objects.all().select_related('user', 'cat')
    #как-будто бы все данные но нет, с помощью UpdateAPIView метод queryset будет барть только 1 элемент
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )

class WomenAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all().select_related('user', 'cat')
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,  )



# class WomenViewSet(viewsets.ModelViewSet):
#      queryset = Women.objects.all() # вместо этого у нет >>гет куери сет
#      serializer_class = WomenSerializer
#      def get_queryset(self):
#          pk=self.kwargs.get('pk')
#
#          if not pk:
#              return Women.objects.all()[:4]
#          return Women.objects.filter(pk=pk)
#
#      @action(methods=['get'], detail=True) #  с помощью декоратора добавляем всякие разные маршруты // если я правильно помню тру это то чтобы отвечала за юрл тип /дай/12 (айди)
#      def category(self, request, pk=None): #http://127.0.0.1:8000/api/v1/women/category/ вот эти маршурты формируются благодаря именам
#          cats= Category.objects.get(pk=pk) #перебиираем коллекцию
#          return  Response({'cats': cats.name }) #  и берёт соответсвующие имена
#






# class WomenAPIView(APIView):
#       def get(self, request):
#           lst=Women.objects.all()
#           return Response({'posts':WomenSerializer(lst, many=True).data}) #вызывается джсонрендер и преобразовываеться все эит данные в джсон строку (юайтоую джсон строку)
#          # .data  представляет собой словарь преобразованных данных из таблицы вумен
#
#           # return Response({'titvdfdfle': 'Anvcxcvgelina jolie'})
#           # lst=Women.objects.all().values() #считаем все данные из бд
#           # return Response({'posts': list(lst)}) # по это не выолняем так как нет статей
#            #гет возврщ фиксированный данные в виде джсом строки
#
#      def post(self, request):
#            serializer = WomenSerializer(data=request.data)
#           serializer.is_valid(raise_exception=True)
#           serializer.save() #метод сейв автоматически вызовет метод create(views.py) и будт
#           return Response({'post': serializer.data}) #препобразовывает модель джанго в колллекцию
#          # преобразовывает модель джанго в словарь
#
#       def put(self, request, *args, **kwargs):
#           pk = kwargs.get("pk", None)
#           if not pk:
#               return Response({'error': 'Pk must be provided'})
#           try:
#              instance = Women.objects.get(pk=pk)
#           except:
#              return Response({'error': 'Women does not exist'})
#
#           serializer = WomenSerializer(data=request.data, instance=instance) # когда 2 таких аргумента метод сейв автоматически вызовает метод метод апдейт
#           serializer.is_valid(raise_exception=True)
#           serializer.save()
#           return Response({'post': serializer.data})
#      #НАПИШИ СЮДА ДЕФ ДЕЛЕТЕ
#       def delete(self, request, *args, **kwargs):
#           pk = kwargs.get("pk", None)
#           if not pk:
#               return Response({'error': 'Pk must be provided'})

#          instance = Women.objects.get(pk=pk)
#          instance.delete()
#          return Response({'deleted': f"True {pk}"})
#


# class WomenApiiew(generics.ListAPIView):
#     queryset= Women.objects.all()
#     serializer_class = WomenSerialazer
#
#

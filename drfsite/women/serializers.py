import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Women

# class WomenModel:
#     def __init__(self, title, content): #это  инициализатор создаём объекты этого класса
#         self.title=title
#         self.content=content

class WomenSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255) # отвечает за представление дданных в виде обычной строки
    content = serializers.CharField()

#
# def encode(): #мы будем выпольгнять кодирование преобразование объектов WomenModel в джосон формат
#     model= WomenModel('Anjela', 'content: Angella') #объект сериализации
#     model_sr= WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data) ,sep='\n')
# #data это уже сериализованне данные
#     json=JSONRenderer().render(model_sr.data) #JSONRenderer().render преобразует объект сериализации в байтовую джос строку котору. мы дальше передаёт клиенту а клиент уже дальше будет с ней чтото делать
#     print(json)


# 1 когда обхект моуль проганлаи через сериалзатор
# (2) он представляет сабой словарь,
# этот словарь мы пропустили через джсонрендер и получили байтовую сторкуи и
# уже эту байтовуб строку мы можем отдавать клиенту и он её парсит и чото ещё делает
# объект-> в словарь- > в джсон формат



# def decode():
#     strem=io.StringIO(b'{"title":"Anjela", "content":"Content:  Angella"}')
#     data=JSONParser().parse(strem.read)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)



















# class WomenSerialazer(serializers.ModelSerializer):
#     #МodelSerializer сериалазатор котрый работает с моделями биокс из таблицы бд бдует барть опред записи
#     #представлять из в джсон формате и отправлять как ответ на заарос пользорвателя\
#     class Meta:
#         model=Women
#         fields=('title', 'cat_id', 'image' )
#         #fields это поля которые мы будем исопльзоватеь для сериализации
#         #тоесть те которые будут обратно отправляться пользователю
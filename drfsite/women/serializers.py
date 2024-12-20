import io

from rest_framework import serializers
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    #создается скрыттое поле хиден и в этом скрытом поле по умолчанию прописывается текущиё пользователь  CurrentUserDefault
    class Meta:
        model = Women
        fields = ("id","title", "content", "image", "cat") #какие поля из бд будут возврашать обатно клиенту



# class WomenModel:
#     def __init__(self, title, content): #это  инициализатор создаём объекты этого класса
#         self.title=title
#         self.content=content





# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255) # отвечает за представление дданных в виде обычной строки
#     content = serializers.CharField()
#     image = serializers.ImageField()
#     time_created = serializers.DateTimeField(read_only=True)
#     time_updated = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Women.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title) #'title', если не можем вернуть ключь тайтл то возвращаем из модели вумен instance.titl
#         instance.content = validated_data.get('content', instance.content)
#         instance.image = validated_data.get('image', instance.image)
#         instance.time_updated = validated_data.get('time_updated', instance.time_updated)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
#         instance.cat_id = validated_data.get('cat_id', instance.cat_id)
#         instance.save()
#         return instance


   # когда при пост запросе делаем serializer.is_valid(raise_exception=True) #формирруеться словарь validated_data
       # return а тут возвращем полученный объект
    #Women.objects.create(**validated_data) тут добавляем новй объект  1

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
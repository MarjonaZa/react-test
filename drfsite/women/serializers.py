from rest_framework import serializers

from .models import Women


class WomenSerialazer(serializers.ModelSerializer):
    #МodelSerializer сериалазатор котрый работает с моделями биокс из таблицы бд бдует барть опред записи
    #представлять из в джсон формате и отправлять как ответ на зварос пользорвателя\
    class Meta:
        model=Women
        fields=('title', 'cat_id')
        #fields это поля которые мы будем исопльзоватеь для сериализации
        #тоесть те которые будут обратно отправляться пользователю
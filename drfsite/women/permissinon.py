from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission): #здесь с записями не работаем поэтому юзаем has_permission
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: #если метод безопасный
            return True #даём доступ для всех пользователей

        return bool(request.user and request.user.is_staff) #а иначе только для админа


class IsOwnerOrReadOnly(permissions.BasePermission):# а здесь мы делаем разрешение на уровне объекта для 1 записи

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user
    #для конкртерной азписси сравнивать юзера с тем юзером который пришел по запросу


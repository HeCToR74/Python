# from rest_framework import generics
from rest_framework.response import Response
from django.http import HttpResponseForbidden
from rest_framework.views import APIView
from .models import Enter, Room, Key, Permission
from .serializers import EnterSerializer, RoomSerializer, KeySerializer, PermissionSerializer
from django.contrib.auth.models import User
from datetime import datetime


class ListEnter(APIView):
    def get(self, request, key):    	
    	if Key.objects.filter(key=key).exists():
    		object_key = Key.objects.get(key=key)
    		if object_key.user.is_superuser:
	    		entrances = Enter.objects.all()        
	    		serializer = EnterSerializer(entrances, many=True)
	    		return Response({"Список входів:": serializer.data})
	    	else:
	    		return HttpResponseForbidden("<h3>У Вас немає прав для такої операції.</h3>")
    	else:
    		return HttpResponseForbidden("<h3>Ви використали недійсний ключ.</h3>")

class PostEnter(APIView):
	def post(self, request, key, room_id):		
		if Key.objects.filter(key=key).exists():
			object_key = Key.objects.get(key=key)
			today = datetime.strptime(datetime.today().strftime("%Y-%m-%d-%H.%M.%S"), "%Y-%m-%d-%H.%M.%S")
			expired = datetime.strptime(object_key.expired.strftime("%Y-%m-%d-%H.%M.%S"), "%Y-%m-%d-%H.%M.%S")
			if object_key.active and today < expired and Permission.objects.filter(user=object_key.user.id, 
				                                                                   room=room_id).exists():
			    enter = {"date": datetime.now(), 
			             "user": object_key.user.id, 
			             "room": room_id
			             }
			    serializer_enter = EnterSerializer(data=enter)
			    if serializer_enter.is_valid(raise_exception=True):
			    	enter_saved = serializer_enter.save()
			    return Response("Вхід {} успішно створено".format(enter_saved))		
			else:
				return HttpResponseForbidden("<h3>Помилка введення! Користувач {} не має доступу\
				    до кімнати {}</h3>".format(User.objects.get(id=object_key.user.id).username, \
				    	Room.objects.get(id=room_id).name))
		else:
			return HttpResponseForbidden("<h3>Ви використали недійсний ключ.</h3>")

class PostPermission(APIView):
	def post(self, request, key, user_key, room_id):
		if Key.objects.filter(key=key).exists():
			object_key = Key.objects.get(key=key)
			if object_key.user.is_superuser:
				if Key.objects.filter(key=user_key).exists() and Room.objects.filter(id=room_id).exists():
					permission = {"user": Key.objects.get(key=user_key).user.id, 
					              "room": room_id
					              }
					serializer_permission = PermissionSerializer(data=permission)
					if serializer_permission.is_valid(raise_exception=True):
						permission_saved = serializer_permission.save()
					return Response("Дозвіл {} надано".format(permission_saved))
				else:
					return HttpResponseForbidden("<h3>Такого користувацького ключа чи id кімнати не існує</h3>")
			else:
				return HttpResponseForbidden("<h3>У Вас немає прав для такої операції.</h3>")
		else:
			return HttpResponseForbidden("<h3>Ви використали недійсний ключ.</h3>")

class RemovePermission(APIView):
	def delete(self, request, key, user_key, room_id):
		if Key.objects.filter(key=key).exists():
			object_key = Key.objects.get(key=key)
			if object_key.user.is_superuser:
				if Permission.objects.filter(user=Key.objects.get(key=user_key).user.id, room=room_id).exists():
					permission = Permission.objects.filter(user=Key.objects.get(key=user_key).user.id, room=room_id)
					delete_object = str(permission[0])
					permission.delete()
					return Response("Дозвіл {} було скасованою".format(delete_object), status=204)
				else:
					return HttpResponseForbidden("<h3>Такого дозволу не існує.</h3>")
			else:
				return HttpResponseForbidden("<h3>У Вас немає прав для такої операції.</h3>")
		else:
			return HttpResponseForbidden("<h3>Ви використали недійсний ключ.</h3>")
			

from datetime import datetime
from django.shortcuts import render
from .models import UsersModel, MessagesModel


def get_list_messages():
	# The function returns a list of all messages from the database	
	return [{"user_name": UsersModel.objects.get(id=item.user_id).name,	"text": item.text,\
	"date": item.date} for item in MessagesModel.objects.all()]			

def index(request):
	user_name = "" 			
	if request.method == "POST":
		link = request.POST.get("link")
		button_in = request.POST.get("button_in")
		if link == "login":
			# post login
			if button_in == "Log in":
				# retrieve data from "login.html"
				user_name = request.POST.get("username")				
				user_password = request.POST.get("password")
				# by the user name we get the corresponding object from the database
				user = UsersModel.objects.get(name=user_name)
				# check the matching of the username with its password
				if user != None and user_password == user.password:
					user_name = user.name
				else:
					user_name = ""
			else:
				user_name = ""

		if link == "message":
			# post message			
			text =  request.POST.get("text")
			user_name = request.POST.get("user_name")
			message = MessagesModel.objects.create(text=text, date= datetime.now(),\
				user_id=UsersModel.objects.get(name=user_name).id)
			message.save()

	return render(request, "index.html", context={"user_name": user_name,\
		"messages": get_list_messages()})



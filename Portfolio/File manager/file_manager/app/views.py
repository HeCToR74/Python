from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from .models import Connection
from ftplib import FTP


def index(request):
    connections = Connection.objects.all()
    data = []
    path = '..'
    if request.method == "POST":
        action = request.POST.get("button")
        if action == "Створити":
            connection = Connection()
            connection.host = request.POST.get("create_host")
            connection.user = request.POST.get("create_user")
            connection.password = request.POST.get("create_password")
            connection.save()

        if action == "Видалити поточний хост":
            try:
                id = request.POST.get("select")
                connection = Connection.objects.get(id=id)
                connection.delete()
            except Connection.DoesNotExist:
                return HttpResponseNotFound("<h2>З'эднання не знайдено</h2>")

        if action == "Оновити":
            try:
                id = request.POST.get("select")
                connection = Connection.objects.get(id=id)
                connection.host = request.POST.get("edit_host")
                connection.user = request.POST.get("edit_user")
                connection.password = request.POST.get("edit_password")
                connection.save()
            except Connection.DoesNotExist:
                return HttpResponseNotFound("<h2>З'эднання не знайдено</h2>")

        if action == "Зв'язатися":
            try:
                id = request.POST.get("select")
                connection = Connection.objects.get(id=id)
                ftp = FTP(connection.host, connection.user, connection.password)
                data = ftp.nlst()
            except:
                return HttpResponseNotFound("<h2>З'эднання не знайдено</h2>")

        if action == "Завантажити/Перейти":
            id = request.POST.get("select")
            path_save = request.POST.get("path_save")
            filename = request.POST.get("filename")
            path = request.POST.get("path")
            if filename == '..':
                path = path.split('/')
                path.pop()
                path = '/'.join(path)
            else:
                path += '/' + filename
            connection = Connection.objects.get(id=id)
            ftp = FTP(connection.host, connection.user, connection.password)
            try:
                ftp.cwd(path)
                data = ftp.nlst()
            except:
                with open(path_save, 'wb') as f:
                    ftp.retrbinary('RETR ' + path, f.write)




    return render(request, "index.html", context={"connections": connections, "path": path, "data": data})



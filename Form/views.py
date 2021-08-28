from django.http import response
from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import User
from .qrcode import generate_qrcode
from .sendMail import mail
import json
import mimetypes
# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        id = datetime.now()
        id = id.strftime("%d%m%y%H%M%S")
        # print("ID:----->", id)
        status = generate_qrcode(id)
        if status == True:
            mail(email, id)
        user = User(name=name, email=email, uid=id)
        user.save()
    return render(request, 'index.html')


def jsonData(request):
    data = list(User.objects.values())
    map = {}
    for i in data:
        key = i['id']
        i.pop('id')
        map[key] = i

    response = HttpResponse(json.dumps(map), content_type='application/json')
    response['Content-Disposition'] = 'attachment; data.json"'
    return response
    
def ses(request):
    file_path = 'static/app.zip'
    f = open(file_path, 'rb')
    # mime_type = mimetypes.guess_extension(file_path)
    response = HttpResponse(f, content_type='application/zip')
    response['Content-Disposition'] = "attachment; app.zip"
    return response
    

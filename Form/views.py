from django.http import response
from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import User, Event
from .qrcode import generate_qrcode
from .sendMail import mail
from hashids import Hashids
import json


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
    

def login(request):
    return render(request, 'login.html')

def home(request):
    exist = False
    if request.method == "POST":
        email = request.POST.get('email')
        checkUser = User.objects.filter(email=email)
        if len(checkUser) == 1:
            exist = True

    if(exist):
        return render(request,'home.html')

    return render(request,'login.html')

def addEvent(request):
    if request.method == "POST":
        name = request.POST.get('event_name')
        id = datetime.now()
        id = id.strftime("%d%m%y%H%M%S")

        user = User.objects.get(email='elliot@gmail.com')
        event = Event(uid=user,eid=id, event_name=name)
        event.save()
    return render(request, 'addEvent.html')

def showEvent(request, eid):
    params = {}
    if request.method == "GET":
        h=Hashids()
        lst = eid.split('-')
        eid = h.decode(lst[0])[0]
        uid = h.decode(lst[1])[0]
        print(eid,"--",uid)
        event_name = Event.objects.get(eid=eid)
        print("-->",event_name.event_name)
        params = {'name': event_name.event_name}
    
    if request.method == "POST":
        pass
    return render(request, 'showEvent.html', params)

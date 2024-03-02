from django.shortcuts import render
import requests
from django.http import HttpResponseRedirect
import json

# Create your views here.
def home(request):
    
    url = 'https://api.freeapi.app/api/v1/todos'
    
    response = requests.get(url)
    object = response.json()
    # print(object)

    if object['success'] and object['data']:
        data = object['data']
        
        if request.method == 'POST':
            title = request.POST['task']
            new_data = {'title':title}
            requests.post(url, new_data)
            return HttpResponseRedirect('/')

    
    return render(request, 'base/home.html', context={'data':data})
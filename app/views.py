from django.shortcuts import render
import requests
from django.http import HttpResponseRedirect

# Create your views here.

object_list = []
def home(request, id=0):
    
    url = 'https://api.freeapi.app/api/v1/todos'
    
    response = requests.get(url)
    object = response.json()
    # print(object)


    if object['success'] and object['data']:
        data = object['data']
        object_list.clear()
        for i in data:
            title = i['title']
            id = i['_id']
            object_list.append({'title':title, 'id':id})
            
        
        if request.method == 'POST':
            new_title = request.POST['task']
            new_data = {'title':new_title}
            requests.post(url, json=new_data)
            return HttpResponseRedirect('/')
        
    return render(request, 'base/home.html', context={'objects':object_list})

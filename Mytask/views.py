from django.shortcuts import render
from .models import Task

def index(request):
    all_item= Task.objects.all()
    return render(request,'Mytask/index.html',{'all_item':all_item})

def all_item(request):
    all_item = Task.objects.all()
    return render(request, 'Mytask/result.html', {'all_item': all_item})

def search(request):
    try:
        text = request.POST.get('text', 'default')
        items = Task.objects.get(name=text)
    except:
        items='ooopps this item does not present in our database....'
    return render(request, 'Mytask/search.html', {'items': items})

def searchurl(request):
    try:
        texturl = request.POST.get('texturl', 'default')
        items = Task.objects.get(taskurl=texturl)
        print(texturl)
        if texturl==items:
            items=Task.object.get(taksurl=texturl)
    except:
        items='sorry these url is does not exist in our database......'
    return render(request, 'Mytask/searchurl.html', {'items': items})

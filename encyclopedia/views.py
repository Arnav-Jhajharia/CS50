from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from . import util
from django.urls import reverse
import random as rand
import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def title(request, name):
        if util.get_entry(name) != None:
           return HttpResponse(markdown2.markdown(util.get_entry(name)) + f'''<br> <a href = "edit/{name}"><button>edit</button></a>''')
        return HttpResponse("Page not found")
def search(request):
        search = request.GET.get('q')
        items = []
        
        if(search.lower() in (x.lower() for x in util.list_entries())):
            return HttpResponseRedirect(f"../../wiki/{search}")
        else:
            for item in util.list_entries():
                if((str(search)).lower() in item.lower()):
                    items.append(item)
        return render(request, "encyclopedia/search.html", {
                "search": str(search),
                "items": items 
            })
def edit(request, name):
    
    placeholder = util.get_entry(name);
    if request.method == 'POST':        
        form = (request.POST['edit'])
        util.save_entry(name, form)

        return HttpResponseRedirect(f"../../wiki/{name}")
    return render(request, "encyclopedia/edit.html", {
        "name": name,
        "value": placeholder,
    })     
 

def new(request):
    if request.method == 'POST':
        name = (request.POST['title'])
        title = (request.POST['new'])
        util.save_entry(name, title)
        return HttpResponseRedirect(f"../../wiki/{name}")
    return render(request, "encyclopedia/new.html")

def random(request):
   name = util.list_entries()
   ran = rand.randint(0, len(name) - 1)
#    if util.get_entry(name[ran]):
#         return HttpResponse(util.get_entry(name[ran]) + f'''<br> <a href = "edit/{name[ran]}"><button>edit</button></a>''')
#    return HttpResponse("Page not found")
   return HttpResponseRedirect(f"../../wiki/{name[ran]}")

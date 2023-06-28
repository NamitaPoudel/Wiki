from django.shortcuts import render, redirect
from markdown2 import Markdown
from . import util
import random


def index(request): 
    q = request.GET.get('q')
    if q != None:
        if util.get_entry(q) != None:
            return redirect('entries', pk=q)
        else:
            title = f"Search Containing \"{q}\""
    else:
        q= ''
        title = "All Pages"
    entries = list(filter(lambda x: q.lower() in x.lower(), util.list_entries()))
    return render(request, "encyclopedia/index.html", {
        "entries": entries,
        "title": title
    })


def entries(request, pk):
    entry = util.get_entry(pk)
    if entry == None:
        context = {"error": "No Such Entry"}
        return render(request,"encyclopedia/error.html", context)
    markdowner = Markdown()
    context = {"title": pk, "entry": markdowner.convert(entry)}
    return render(request, "encyclopedia/entries.html", context)


def createPage(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        if util.get_entry(title) != None or set(title) == {' '}:
            context = {"error": "Entry Already Exists/Invalid Entry!!"}
            return render(request, "encyclopedia/error.html", context)
        util.save_entry(title,description)
        context = {"title": title, "entry": Markdown().convert(description)}
        return render(request, "encyclopedia/entries.html", context)

    return render(request, "encyclopedia/create_page.html")


def editPage(request, pk):
    if request.method == 'POST':
        description = request.POST['description']
        util.save_entry(pk,description)
        context = {"title": pk, "entry": Markdown().convert(description)}
        return render(request, "encyclopedia/entries.html", context)
    
    description = util.get_entry(pk)
    context = {
        "title": pk,
        "entry": description
    }
    return render(request, "encyclopedia/edit.html", context)


def randomPage(request):
    entries = util.list_entries()
    entry = random.choice(entries)
    return redirect('entries', pk=entry)

from django.shortcuts import render, redirect

from . import util
import markdown2
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def pages(request, name):
    markdown_text = util.get_entry(name)
    if not markdown_text == None:
        html_content = markdown2.markdown(markdown_text)
        return render(request,f"encyclopedia/page.html", {
        "title": name,
        "content": html_content,})
    else:
        html_content = "<h1>404 Not Found<h1> <p>Oops! the page you are trying to reach does not seem like it exists. Would you like to create the page?</p>"
        return render(request,f"encyclopedia/page.html", {
            "title": name,
            "content": html_content,})
        
def search(request):
    name = request.GET.get("q", "")
    page_list = util.list_entries()
    if name in page_list:
        markdown_text = util.get_entry(name)
        html_content = markdown2.markdown(markdown_text)
        return render(request,f"encyclopedia/page.html", {
        "title": name,
        "content": html_content,})
    else:
        search_list = []
        for page in page_list:
            if set(page.lower()) > set(name.lower()):
                search_list.append(page)
        return render(request,f"encyclopedia/search.html", {"search_list": search_list,})
        
def random_page(request):
    page_list = util.list_entries()
    chosen_page = random.choice(page_list)
    markdown_text = util.get_entry(chosen_page)
    html_content = markdown2.markdown(markdown_text)
    return render(request,f"encyclopedia/page.html", {
        "title": chosen_page,
        "content": html_content,})

    
def new_page(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        if title.lower() in [entry.lower() for entry in util.list_entries()]:
            return render(request, "encyclopedia/new_page.html", {
                "error": "An entry with this title already exists."
            })
        util.save_entry(title, content)
        return redirect("pages", name = title)
    return render(request, "encyclopedia/new_page.html")

def edit_page(request, page):
    title = page
    markdown_text = util.get_entry(page)
    if request.method == "POST":
        content = request.POST["content"]
        util.save_entry(title, content)
        return redirect("pages", name = title)
    return render(request, "encyclopedia/edit.html", {"title": title, "original": markdown_text})
     
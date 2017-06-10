from django.shortcuts import render

def text_list(request):
    return render(request, "txct/text_list.html", {})

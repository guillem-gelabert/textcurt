from django.db.models import Q
from django.shortcuts import render
from django.utils import timezone
from .models import Text
from django.shortcuts import render, get_object_or_404
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_user_agents.utils import get_user_agent

def base(request):
    context = {
        "title": texts.title,
        "writer": texts.writer,
    }
    return render(request, "txct/base.html", context)

def index(request):
    return render(request, 'txct/index.html')

def text_5(request):
    texts = Text.objects.filter(read_time__range=(0,6)).order_by("read_time")
    paginator = Paginator(texts, 1) # Show 1 text per page

    page = request.GET.get('page')
    try:
        text = paginator.page(page)
    except PageNotAnInteger:
        text = paginator.page(1)
    except EmptyPage:
        text = paginator.page(paginator.num_pages)

    return render(request, 'txct/text_display.html', {'text': text})

def text_10(request):
    texts = Text.objects.filter(read_time__range=(7,12)).order_by("read_time")
    paginator = Paginator(texts, 1) # Show 1 text per page

    page = request.GET.get('page')
    try:
        text = paginator.page(page)
    except PageNotAnInteger:
        text = paginator.page(1)
    except EmptyPage:
        text = paginator.page(paginator.num_pages)

    return render(request, 'txct/text_display.html', {'text': text})

def text_15(request):
    texts = Text.objects.filter(read_time__range=(13,17)).order_by("read_time")
    paginator = Paginator(texts, 1) # Show 1 text per page

    page = request.GET.get('page')
    try:
        text = paginator.page(page)
    except PageNotAnInteger:
        text = paginator.page(1)
    except EmptyPage:
        text = paginator.page(paginator.num_pages)

    return render(request, 'txct/text_display.html', {'text': text})

def text_20(request):
    texts = Text.objects.filter(read_time__range=(18,22)).order_by("read_time")
    paginator = Paginator(texts, 1) # Show 1 text per page

    page = request.GET.get('page')
    try:
        text = paginator.page(page)
    except PageNotAnInteger:
        text = paginator.page(1)
    except EmptyPage:
        text = paginator.page(paginator.num_pages)

    return render(request, 'txct/text_display.html', {'text': text})

def text_25(request):
    texts = Text.objects.filter(read_time__range=(23,30)).order_by("read_time")
    paginator = Paginator(texts, 1) # Show 1 text per page

    page = request.GET.get('page')
    try:
        text = paginator.page(page)
    except PageNotAnInteger:
        text = paginator.page(1)
    except EmptyPage:
        text = paginator.page(paginator.num_pages)

    return render(request, 'txct/text_display.html', {'text': text})

from django.db.models import Q
from django.shortcuts import render
from django.utils import timezone
from .models import Text
from django.shortcuts import render, get_object_or_404
import json

def text_list(request):
    texts = Text.objects.order_by('read_time')
    return render(request, 'txct/text_list.html', {'texts': texts})

def index(request):
    return render(request, 'txct/index.html')

def text_detail(request, pk):
    text = get_object_or_404(Text, pk=pk)
    return render(request, 'txct/text_detail.html', {'text': text})

def text_5(request):
    texts = Text.objects.filter(Q(read_time__gt=0) & Q(read_time__lte=6)).order_by("?")[0]
    title = json.dumps(texts.title)
    return render(request, 'txct/text_5.html', {'texts': texts})

def text_10(request):
    texts = Text.objects.filter(Q(read_time__gt=6) & Q(read_time__lte=12)).order_by("?")[0]
    return render(request, 'txct/text_10.html', {'texts': texts})

def text_15(request):
    texts = Text.objects.filter(Q(read_time__gt=12) & Q(read_time__lte=16)).order_by("?")[0]
    return render(request, 'txct/text_15.html', {'texts': texts})

def text_20(request):
    texts = Text.objects.filter(Q(read_time__gt=16) & Q(read_time__lte=22)).order_by("?")[0]
    return render(request, 'txct/text_20.html', {'texts': texts})

def text_25(request):
    texts = Text.objects.filter(Q(read_time__gt=22) & Q(read_time__lte=35)).order_by("?")[0]
    return render(request, 'txct/text_25.html', {'texts': texts})

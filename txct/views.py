from django.shortcuts import render
from django.utils import timezone
from .models import Text
from django.shortcuts import render, get_object_or_404

def text_list(request):
    texts = Text.objects.order_by('read_time')
    return render(request, 'txct/text_list.html', {'texts': texts})

def text_detail(request, pk):
    text = get_object_or_404(Text, pk=pk)
    return render(request, 'txct/text_detail.html', {'text': text})

def text_5(request, pk):
    text = get_object_or_404(Text, pk=pk)
    return render(request, "txct/text_5.html", {'text': text})

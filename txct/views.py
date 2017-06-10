from django.shortcuts import render
from django.utils import timezone
from .models import Text

def text_list(request):
    texts = Text.objects.order_by('read_time')
    return render(request, 'txct/text_list.html', {'texts': texts})

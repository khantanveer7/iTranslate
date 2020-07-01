from django.shortcuts import render , HttpResponse
from googletrans import Translator
# Create your views here.
def home (request):
    return render(request, 'index.html')

def translate (request):
    text = request.POST.get('text')
    lang = request.POST.get('lang')

    trans = Translator()
    dt = trans.detect(text)
    dt2 = dt.lang

    translated = trans.translate(text , lang)
    tr = translated.text
    return render(request, 'translate.html' , {'translated': tr})
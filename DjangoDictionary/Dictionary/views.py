from django.shortcuts import render, HttpResponse

from  googletrans import Translator #--> does't work : fixed -> in pre-released version
# from translate import Translator

from .models import Dictionary

# Create your views here.
def home(request):
    if request.method == 'GET':
        return HttpResponse(render(request, 'home.html'), status=200)
    
    if request.method == 'POST':
        lang = request.POST.get("lang", None)
        txt = request.POST.get("txt", None)
        src = request.POST.get("src", None)
        print(lang,txt)
        translator = Translator()
        tr = translator.translate(txt,src=src, dest=lang)
        try:
            if tr.pronunciation:
                p =tr.pronunciation
            else:
                p = ''
        except:
            None
        obj = Dictionary.objects.create(word=txt, meaning=tr.text, targetlang=tr.dest, pronunciation=p, src=tr.src)
        obj.save()
        print(tr,tr.src)
        return HttpResponse(render(request, 'home.html', {"result":tr.text}), status=200)
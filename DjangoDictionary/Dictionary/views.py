from django.shortcuts import render, HttpResponse

from  googletrans import Translator #--> does't work : fixed -> in pre-released version
# from translate import Translator

# Create your views here.
def home(request):
    if request.method == 'GET':
        return HttpResponse(render(request, 'home.html'), status=200)
    
    if request.method == 'POST':
        lang = request.POST.get("lang", None)
        txt = request.POST.get("txt", None)
        print(lang,txt)
        translator = Translator()
        tr = translator.translate(txt, dest=lang)
        print(tr)
        return HttpResponse(render(request, 'home.html', {"result":tr.text}), status=200)
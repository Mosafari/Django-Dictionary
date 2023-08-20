from django.shortcuts import render, HttpResponse

from  googletrans import Translator #--> does't work : fixed -> in pre-released version
# from translate import Translator

from .models import Dictionary


# Error handling
def handler404(request,exceptin):
    print("here" +request.GET)
    return render(request, '404.html', status=404)

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
        records = Dictionary.objects.all()
        return HttpResponse(render(request, 'home.html', {"result":tr.text, "records" : records}), status=200)
    
# exporting records in excel file
import xlwt
def export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['ID', 'Text', 'Meaning', 'Src', 'Dest', 'Pronunciation', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Dictionary.objects.all().values_list('id', 'word', 'meaning', 'src', 'targetlang', 'pronunciation',)
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response
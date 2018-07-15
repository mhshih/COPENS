from concordance import concordance
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    try:
        keyword=request.POST['keyword']
        contexts=concordance(keyword=keyword)
        return HttpResponse('<br>'.join(contexts))
    except:
        return render(request,'index.htm',{})

from concordance import concordance
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    try:
        keyword=request.POST['keyword']
        selected_corpus_dir=request.POST['choice']
        contexts=concordance(keyword=keyword,corpus_dir=selected_corpus_dir)
        return HttpResponse('<br>'.join(contexts))
    except:
        return render(request,'index.htm',{})

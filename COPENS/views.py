from django.shortcuts import render
def home(request):
    return render(request,'index.htm',{})

from concordance import concordance
from django.http import HttpResponse
def concordance_api(request):
    keyword=request.GET['keyword']
    selected_corpus_dir=request.GET['choice']
    contexts=concordance(keyword=keyword,corpus_dir=selected_corpus_dir)
    return HttpResponse('<ol><li>'+'<li>'.join(contexts)+'</ol>')

from math import log
from sortedcollections import ValueSortedDict
from COPENS.models import CoNLLU
def sense_collocation(request): # Currently for dobj only...
    keyword=request.POST['keyword']
    sense_dep_scores=dict()
    for sense in set([c.sense for c in CoNLLU.objects.filter(head=keyword)]):
        dep_scores={}
        for rel in set([c.rel for c in CoNLLU.objects.filter(head=keyword,sense=sense)]):
            if rel!='dobj':continue
            for dep in set([c.dep for c in CoNLLU.objects.filter(head=keyword,sense=sense,rel=rel)]):
                W1RW2=[c.words for c in CoNLLU.objects.filter(head=keyword,sense=sense,rel=rel,dep=dep)]
                W1R=[c.words for c in CoNLLU.objects.filter(head=keyword,sense=sense,rel=rel)]
                W2=[c.words for c in CoNLLU.objects.filter(dep=dep)]
                logDice=14+log(2*len(W1RW2)/(len(W1R)+len(W2)))
                H=3
                logDiceH=14+log(H*len(W1RW2)/(len(W1R)+len(W2)))
                dep_scores[dep]=round(logDiceH,2),W1RW2,round(logDice,2)
        sense_dep_scores[sense]=sorted(dep_scores.items(),key=lambda dep_scores:dep_scores[1],reverse=True)
    return render(request,'dobj.htm',{'head':keyword,'rel':'dobj','sense_dep_scores':sense_dep_scores})

def collocation_api(request,head,sense,rel,dep):
    items=CoNLLU.objects.filter(head=head,sense=sense,rel=rel,dep=dep)
    return HttpResponse('<ol><li>'+'<li>'.join([item.words for item in items])+'</ol>')
    return HttpResponse([head,sense,rel,dep])

from extract_collocates_from_conllu import extract_senseid_children_collocates
SemEval_dir='SemEval-2007/'
target_sense_rel_dep_bundles=extract_senseid_children_collocates(conllu_filename=SemEval_dir+'Chinese_train_pos.xml.utf8.sentences.conllu.senseid')

from concordance import concordance
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    try:
        keyword=request.POST['keyword']
        selected_corpus_dir=request.POST['choice']
        if selected_corpus_dir=='SemEval-2007/':
            for sense,rel_dep_bundles in target_sense_rel_dep_bundles[keyword].items():
                for rel,dep_bundles in rel_dep_bundles.items():
                    pass
            sense_dep_scores=target_sense_rel_dep_bundles[keyword]
            return render(request,'dobj.htm',{'target':keyword,'sense_dep_scores':sense_dep_scores})
            return render(request,'SemEval-2007.htm',{'target':keyword,'target_deprels':['nsubj','dobj'],'senseid_deprel_form_bundles':target_sense_rel_dep_bundles[keyword]})
        contexts=concordance(keyword=keyword,corpus_dir=selected_corpus_dir)
        return HttpResponse('<ol><li>'+'<li>'.join(contexts)+'</ol>')
    except:
        return render(request,'index.htm',{})

def api(request,target,sense,rel,dep):
    lines=[bundle.bundle_id+' '.join(bundle.words) for bundle in target_sense_rel_dep_bundles[target][sense][rel][dep]]
    return HttpResponse('<br>'.join(lines))

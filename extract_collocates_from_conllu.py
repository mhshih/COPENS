## To Obtain Sense Collcates from CoNLL-U
### Input: query word
### Output: sense collocats with grammatical relations

class Vividict(dict):
    def __missing__(self, key):
        value = self[key] = type(self)() # retain local pointer to value
        return value                     # faster to return than dict lookup

def setattr_words(bundle):
    bundle.words=[]
    node=bundle.get_tree()
    while node:
        bundle.words.append(node.form)
        node=node.next_node

from collections import OrderedDict
from udapi.core.document import Document
def extract_senseid_children_collocates(conllu_filename):
    D=Document()
    D.load_conllu(conllu_filename)#'Chinese_train_pos.xml.utf8.sentences.conllu.senseid')
    target_senseid_deprel_form_bundles=Vividict()#defaultdict(dict)
    for bundle in D.bundles:
        setattr_words(bundle=bundle)
        node=bundle.get_tree()
        while node:
            target=node.form
            senseid=node.misc['senseid']
            if senseid:    # For a verb like 想, list all children of the sense node:
                for child in node.children:
                    if target_senseid_deprel_form_bundles[target][senseid][child.deprel][child.form]=={}:
                        target_senseid_deprel_form_bundles[target][senseid][child.deprel][child.form]=[bundle]
                    else:
                        target_senseid_deprel_form_bundles[target][senseid][child.deprel][child.form].append(bundle)
            node=node.next_node
    # To convert back to a common dictionaryu instance:
    d=dict(target_senseid_deprel_form_bundles)
    for target,senseid_deprel_form_bundles in target_senseid_deprel_form_bundles.items():
        d[target]=dict(senseid_deprel_form_bundles)
        for senseid,deprel_form_bundles in senseid_deprel_form_bundles.items():
            d[target][senseid]=dict(deprel_form_bundles)
            for deprel,form_bundles in deprel_form_bundles.items():
                #d[target][senseid][deprel]=dict(form_bundles)
                sorted_form_bundles=sorted(form_bundles.items(),key=lambda form_bundles:len(form_bundles[1]),reverse=True)
                d[target][senseid][deprel]=OrderedDict(sorted_form_bundles)
    return d

from sys import argv
if __name__=='__main__':
#   target_bundles=query_bundles(query='想',bundles=d.bundles)
    for target,senseid_deprel_form_bundles in extract_senseid_children_collocates(conllu_filename=argv[1]).items():
        for senseid,deprel_form_bundles in senseid_deprel_form_bundles.items():
            print(target,senseid)
            for deprel,form_bundles in deprel_form_bundles.items():
                for form,bundles in form_bundles.items():
                    continue
                    print(target)#,senseid,deprel,form,bundles)

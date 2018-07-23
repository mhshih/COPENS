# To fill the words attribute first:
from udapi.core.document import Document
D=Document()
D.load_conllu('SemEval-2007/Chinese_train_pos.xml.utf8.sentences.conllu.senseid')
for bundle in D.bundles:
    bundle.words=[]
    node=bundle.get_tree()
    while node:
        bundle.words.append(node.form)
        node=node.next_node

# Then save complete attributes to CoNLLU.sqlite3
from COPENS.models import CoNLLU
for bundle in D.bundles:
#   bundle.words=[]
    node=bundle.get_tree()
    while node:
        head=node.form
        sense=node.misc['senseid']
        if sense and head=='想':    # For a verb like 想, list all children of the sense node:
            for child in node.children:
                c=CoNLLU(head=head,sense=sense,rel=child.deprel,dep=child.form,words=' '.join(bundle.words))
                c.save()
                print(c.__str__())
        node=node.next_node


from udapi.core.document import Document
D=Document()
D.load_conllu('SemEval-2007/Chinese_train_pos.xml.utf8.sentences.conllu.senseid')

for bundle in D.bundles:
    bundle.words=[]
    node=bundle.get_tree()
    while node:
        bundle.words.append(node.form)
        node=node.next_node
    print(bundle.bundle_id,bundle.words)

import os
def concordance(keyword,corpus_dir):
    contexts=[]
    for filename in os.listdir(corpus_dir):
        print(corpus_dir+filename)
        for line in open(corpus_dir+filename):
            if keyword in line:
                contexts.append(line)
    return contexts

if __name__=='__main__':
    for context in concordance(keyword='的',corpus_dir='pttcorp/'):
        print(context)


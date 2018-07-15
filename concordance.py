def concordance(keyword):
    contexts=[]
    for line in open('ASBC_A/asbc_a_001.xml'):
        if keyword in line and '<sentence>' in line:
            contexts.append(line)
    return contexts

if __name__=='__main__':
    for context in concordance(keyword='本'):
        print(context)


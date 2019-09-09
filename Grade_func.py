def compgr(h):
    if h>=0.9 and h<1.0:
        m='A'
    elif h>=0.8 and h<0.9:
        m='B'
    elif h>=0.7 and h<0.8:
        m='C'
    elif h>=0.6 and h<0.7:
        m='D'
    elif h<0.6 and h>=0.1:
        m='F'
    else:
        m='Bad score'

    return m
inp=input('Enter score b/w 0.1 & 1.0...')
try:
    gr=float(inp)
    b=compgr(gr)
    print('The grade is....',b)

except:
    print('Bad score')

        

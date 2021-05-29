s = input('s =')

if len(s) == 1:
    print('Μήκος = 1')
else:
    if s == s[::-1]:
        adict = {}
        alist = []
        adict[s] = len(s)
        alist = list(s)
        print(adict,'\n', alist)
    else:
        print('όχι παλίνδρομο')
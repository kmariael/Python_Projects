import statistics as st 

def squares(*args):
    mo = st.mean(args)
    if len(args) == 1:
        return 0
    else:
        for x in args:
            sq = (mo-x)**2
            yield sq

for i in squares(1,2,3):
    print(i)

alist = list(squares(2,7,3,12))
print(alist)

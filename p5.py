import statistics as st

try:
    with open('inputdata.txt') as fin:
        datalist = fin.read().splitlines()
        xdata = []
        for i in datalist:
            xdata.append(float(i))
except Exception as error:
    print(error)
else:
    with open('outputdata.txt', 'w') as f:
        mn = round(st.mean(xdata), 3)
        s =  round(st.stdev(xdata), 3)
        line1 = 'Μέσος όρος = ' +str(mn) +'\n'
        line2 = 'Τυπική απόκλιση =' str(s)
        f.write(line1)
        f.write(line2)
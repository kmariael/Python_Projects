year = int(input('year ='))

disekto = False

if year%400 == 0:
    disekto = True
elif year%100 != 0 and year%4 == 0:
    disekto = True

print (disekto)
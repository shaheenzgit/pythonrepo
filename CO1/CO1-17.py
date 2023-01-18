diction={'red':'#FF0000','green':'#00FF00','black':'#000000','white':'#FFFFFF'}
print("sorted dictionary : ")
for w in sorted(diction,key=diction.get):
    print(w,diction[w])
print("Reverse Order : ")
for w in sorted(diction,key=diction.get,reverse=True):
    print(w,diction[w])


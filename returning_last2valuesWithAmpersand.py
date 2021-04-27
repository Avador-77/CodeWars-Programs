def formatting(name):
    arr = []
    for i in range(0,len(name)):
        if i == len(name) - 2:
            hold = name[i]['name']+" &"
            arr.append(hold)
        elif i == len(name) - 1:
            hold = name[i]['name']
            arr.append(hold)
        else:
            hold = name[i]['name']+","
            arr.append(hold)
    return "'"+' '.join(arr)+"'"

name = [{'name':'anjali'},{'name':'divyam'},{'name':'arti'},{'name':'shivam'},{'name':'nobita'},{'name':'rajshree'}]

print(formatting(name))
#arr = formatting(name)
#print()




    
l1 = [-4,-6,0,4,-2,12,-200]

print(list(filter(lambda x: x>=0, l1)))

print(list(map(lambda x: x/3, l1)))
x=0
l2 = [(1,),(1,2,3),(2,3),(1,2,3,4,5),(1,)]

# def getItemtoSort(item):
#     if isinstance(item, int):
#         return 1
#     else: return len(item)
l2.sort(key=lambda x:len(x))
# l2.sort(key = getItemtoSort)
print(l2)



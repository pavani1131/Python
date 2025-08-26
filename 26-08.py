# dict inbuilt functions
# A dictinoary is a collection of key-value pairs where each key is unique
#ex={'name': 'Alice' , 'age' : 25 , 'city' : 'NewYork'}
d={'name':'Pavani','age':21}
print(d.get('name'))
print(d.get('gender'))
print(list(d.keys()))
print(list(d.values()))

d1={'a':123,'b':456}
for c,d in d1.items():
    print(c,d)
d1.update({'e':789})
print(d1)
print(d1.pop('a'))
print(d1.pop('y','not found'))
print(d1.popitem())
d1.clear()
print(d1)
d3={'x':[1,2]}
shallow=d3.copy()
shallow['x'].append(3)
print(d3)

#shallowcopy
list1=[1,2,3,4,[3,4,5]]
list2=list1.copy()
list2[4][2]=35
print(list1)
print(list2)

#deep copy
import copy
list1=[1,2,3,4,[3,4,5]]
list3=copy.deepcopy(list1)
list3[4][0]=2
print(list3)

keys=['a','b','a','c']
values=[1,2,3,4]
print(dict(zip(keys,values)))


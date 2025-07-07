a = 5
b = 7.0
print(a + b)
print(type(a + b)) 
# print(type(a + b)) 12.0 <class 'float'>
str1="python"
print(str1[0]) #p
print(str1[-1]) #n
print(str1[2:5]) #tho
str2="abc"
str3="def"
print(str2+str3) #abcdef
# List: ordered Collection of heterogenous elements 
# Syntax: [1, 2, 3] 
# List is mutable, duplicates are allowed and indexing is possible 
# Tuple: Ordered Collection of items. 
# Syntax: (10,20,30) 
list1=[1,2,3,4,5]
print(list1[ : ])
tup1=(1,2,3,4)
print(tup1[-2: ])
# tup1[2]=0
# print(tup1) TypeError: 'tuple' object does not support item assignment
dict1={"abc":10,
       "def":20,
       "ghi":30,
       "ghi":60}
print(dict1)
print(dict1["abc"])
dict1["abc"]=40
print(dict1)
#  you cannot directly access a key using its value because dictionaries are designed to access values using keys
#  Can I have duplicate values and keys in a dictionary? What happens if I wanted try to duplicate key in a dictionary? 
dict2 = {
    "a": 100,
    "b": 200,
    "c": 100
}
print(dict2)
#  Yes, you can have duplicate values in a dictionary.
# No, you cannot have duplicate keys in a dictionary.
# If you try to define a dictionary with the same key more than once, the last value assigned to that key will overwrite the earlier one.
# Print all multiples of 17 using range. Numbers should start from -34 and end below 400.
print(list(range(-34,400,17)))
[-34, -17, 0, 17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255, 272, 289, 306, 323, 340, 357, 374, 391]




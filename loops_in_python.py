print("List Iteration")
l = ["geeks", "for", "geeks"]

for i in l:
    print(i)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)
print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s  %d" % (i, d[i]))
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i),
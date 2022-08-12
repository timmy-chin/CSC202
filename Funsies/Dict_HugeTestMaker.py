import random
listA = [(chr(random.randint(40,124))) for i in range(100)]
setA = list(set(listA))

list = [(key, ord(key)) for key in listA]
set = [(key, ord(key)) for key in setA]

for tuple in list:
    print(f"insert(dct, '{tuple[0]}', {tuple[1]})")

print(f'self.assertEqual(lsize(lst), {len(set)}, msg)')
for tuple in set:
    print("self.assertIn('"+tuple[0]+"', {lget(lst, i) for i in range("+str(len(set))+")}, msg)")


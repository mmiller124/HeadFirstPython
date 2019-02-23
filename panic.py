phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# D o n ' t _ p a n i c !
# 0 1 2 3 4 5 6 7 8 9 0 1
plist.pop(0)
# o n ' t _ p a n i c !
# 0 1 2 3 4 5 6 7 8 9 0 1
plist.pop(2)
# o n t _ p a n i c !
# 0 1 2 3 4 5 6 7 8 9 0 1
plist.insert(2,plist.pop(3))
# o n _ t p a n i c !
# 0 1 2 3 4 5 6 7 8 9 0 1
plist.insert(4,plist.pop(5))
# o n _ t a p n i c !
# 0 1 2 3 4 5 6 7 8 9 0 1
for i in range(4):
    plist.pop()
# o n _ t a p
# 0 1 2 3 4 5 6 7 8 9 0 1

# my_list.remove(object's_value)
# my_list.pop(index_value) - default is the last item on list
# my_list.extend(another_list)
# my_list.insert(index_value,my_object)

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)


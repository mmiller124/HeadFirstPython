phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# D o n ' t _ p a n i c !
# 0 1 2 3 4 5 6 7 8 9 0 1
new_phrase = ''.join(plist[1:3])

new_phrase = new_phrase + ''.join([plist[5],plist[4],plist[7],plist[6]])

# plist[start:stop:step] -> can be negative
# start = index value of the start of the slice default to 0
# stop = index of stop that IS NOT INCLUDED default to max index plus one
# step = stride to take for each value default to 1

# my_list.remove(object's_value)
# my_list.pop(index_value) - default is the last item on list
# my_list.extend(another_list)
# my_list.insert(index_value,my_object)


print(plist)
print(new_phrase)


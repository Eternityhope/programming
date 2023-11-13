from collections import Counter
my_list = ['a', 'b', 'c', 'a', 'b', 'a', 'd', 'b']
my_counter = Counter(my_list)
print(my_counter)                         

my_counter.update(['a', 'b', 'c'])   
print(my_counter)                         

del my_counter['a']                         
print(my_counter) 
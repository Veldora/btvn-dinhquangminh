##7
def get_even_list(l):
    for i in l:
        if i%2==1:
            l.remove(i)
    return l


##8
even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")

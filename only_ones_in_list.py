mylist = ['nowplaying', 'PBS', 'PBS', 'nowplaying', 'job', 'debate', 'thenandnow']


def only_ones_in_list(collection):
    temp_dict = dict()
    for i in collection:
        if i in temp_dict:
            temp_dict[i] += 1
        else:
            temp_dict[i] = 1
    res = list([i for i in temp_dict if temp_dict[i] == 1])
    return print(res)


only_ones_in_list(mylist)

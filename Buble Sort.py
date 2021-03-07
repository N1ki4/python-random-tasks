def bubble_sort(our_list):
    # We go through the list as many times as there are elements
    for i in range(len(our_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(our_list) - 1):
            if our_list[j] > our_list[j+1]:
                # Swap
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]


# def bubble_sorting(our_list):
#     last_item = len(our_list) - 1
#     for i in range(0, last_item):
#         for j in range(0, last_item):
#             if our_list[j] > our_list[j + 1]:
#                 our_list[j], our_list[j + 1] = our_list[j + 1], our_list[j]


arr = [3, 2, 13, 4, 6, 5, 7, 8, 1, 20]

bubble_sort(arr)
print(arr)

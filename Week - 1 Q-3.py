
def list_sort(list_of_strings):
    list_of_strings.sort(key=len)
    return list_of_strings

list_of_strings = ['glass', 'cup', 'bottle', 'medicine', 'plant', 'mouse', 'pen', 'mobile', 'laptop']
print(list_sort(list_of_strings))

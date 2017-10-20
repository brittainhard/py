a = [x for x in range(1000000)]


def binary_search(item, data):
    search_count = 0
    median = len(data) // 2
    for x in range(len(data)):
        search_count += 1
        if data[item] < data[median]:
            median = median // 2
        elif data[item] > data[median]:
            median = median * 2
        elif data[item] == data[median]:
            print(search_count)
            return data.index(median)
    else:
        raise IndexError("Cannot find item in list")


b = binary_search(6, a)

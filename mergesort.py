def shuffle(List1, List2):
    # initialize current indices of the two lists
    index1 = 0
    index2 = 0

    # initialize the new list
    new_list = []

    # obtain the lengths of the two lists
    l1 = len(List1)
    l2 = len(List2)

    # while the new list has not yet been formed
    while (len(new_list) < l1 + l2):

        # when the index of List 2 is out of range
        if (index2 > l2 - 1 and index1 <= l1 - 1):
            new_list.append(List1[index1])  # add from List 1
            index1 = index1 + 1  # update the index
            continue

        # when the index of List 1 is out of range
        if (index1 > l1 - 1 and index2 <= l2 - 1):
            new_list.append(List2[index2])  # add from List 2
            index2 = index2 + 1  # update the index
            continue

        # when item in List 1 is smaller
        if (List1[index1] < List2[index2]):
            new_list.append(List1[index1])  # add from List 1
            index1 = index1 + 1  # update index
            continue

        # when item in List 2 is smaller
        if (List2[index2] <= List1[index1]):
            new_list.append(List2[index2])  # add from List
            index2 = index2 + 1  # update index
            continue

    return new_list


def mergeSort(items):
    # base Case
    if len(items) == 1:
        return [items[0]]

    middle = len(items) // 2

    # divide
    left = mergeSort(items[:middle])
    right = mergeSort(items[middle:])

    # combine
    return shuffle(left, right)

def largestNumber(k, items):
    items = mergeSort(items)
    value = len(items) - k
    return items[value]


if __name__ == '__main__':
    List1 = [4, 5, 6, 7, 7, 1, 1, 2]
    k = 3
    print(mergeSort(List1))
    print(largestNumber(k, List1))


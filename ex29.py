def diff_color_lists( list1, list2 ):
    new_list = list1.difference(list2)
    return new_list


print(diff_color_lists(set(["White", "Black", "Red"]), set(["Red", "Green"])))

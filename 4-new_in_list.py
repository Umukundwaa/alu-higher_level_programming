def new_in_list(my_list, idx, element):
    # Make a copy of the original list
    new_list = my_list[:]

    # Check if the index is valid
    if idx < 0 or idx >= len(my_list):
        return new_list

    # Replace the element at the specified index
    new_list[idx] = element

    return new_list

#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
                print("wrong type")
                result.append(0)
                continue
            result.append(a / b)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        except Exception:
            # Just in case of unexpected error, append 0
            result.append(0)
    return result

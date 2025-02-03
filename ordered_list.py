def get_ordered_list():
    user_input = input("Enter a comma separated list of integers: ")
    lst = [int(x.strip()) for x in user_input.split(",")]
    return sorted(lst)

print(get_ordered_list())

def main():
    prompt_list = [int(x) for x in input().split()]

    while True:
        command = input()

        if command == "end":
            break

        command_lst = command.split()

        if command_lst[0] == "exchange":
            result = exchange(prompt_list, int(command_lst[1]))
            if result != "Invalid index":
                prompt_list = result
            else:
                print(result)

        elif command_lst[0] in ("max", "min"):
            print(max_min_even_odd(prompt_list, command_lst[0], command_lst[1]))

        elif command_lst[0] in ("first", "last"):
            print(first_last_even_odd(prompt_list, command_lst))

    print(f"[{', '.join(map(str, prompt_list))}]")


def exchange(lst, index):
    """Splits the list after the given index and exchanges the places of the two resulting sub-lists"""
    if index >= len(lst) or index < 0:
        return "Invalid index"
    return lst[index + 1:] + lst[:index + 1]


def max_min_even_odd(lst, mode, command):
    """"returns the INDEX of the max/min even/odd element"""
    filtered = [i for i, x in enumerate(lst) if x % 2 == (0 if command == "even" else 1)]

    if not filtered:
        return "No matches"

    if mode == "max":
        target = max(lst[i] for i in filtered)
    else:
        target = min(lst[i] for i in filtered)

    for i in reversed(filtered):
        if lst[i] == target:
            return i


def only_odd_nums(lst):
    """checks if the list contains only odd numbers"""
    return all(int(n) % 2 != 0 for n in lst)


def only_even_nums(lst):
    """checks if the list contains only even numbers"""
    return all(int(n) % 2 == 0 for n in lst)


def first_last_even_odd(lst, command):
    """extracts first/last odd/even numbers from a list"""
    # If there are not enough elements to satisfy the count, print as many as you can.
    # If there are zero even/odd elements, print an empty list "[]"
    segment, count, category = command[0], int(command[1]), command[2]

    if count > len(lst):
        return "Invalid count"

    filtered = [x for x in lst if x % 2 == (0 if category == "even" else 1)]

    if segment == "first":
        return filtered[:count]
    else:
        return filtered[-count:]


if __name__ == "__main__":
    main()

def insertion_sort(lst):
    ptr = 1

    while ptr < len(lst):
        if lst[ptr] < lst[ptr-1]:
            runner = ptr
            while runner >= 1 and lst[runner] < lst[runner-1]:
                lst[runner], lst[runner-1] = lst[runner-1], lst[runner]
                runner -= 1

        ptr += 1

    return lst

if __name__ == "__main__":
    print(insertion_sort([20, 4,3,2,9,0, -1, 45]))
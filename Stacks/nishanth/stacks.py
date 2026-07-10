def reverse_stack(stack):
    rev = []

    while len(stack) != 0:
        rev.append(stack.pop())

    stack[:] = rev


# Celebrity and largest Histogram Problem solved on Leetcode


def main():
    s = [1,2,3,4,5]
    reverse_stack(stack=s)

    print(s)

if __name__ == '__main__':
    main()
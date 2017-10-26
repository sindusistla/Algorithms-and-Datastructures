def isValidPair(left, right):
    if left == '(' and right == ')':
        return True
    if left == '[' and right == ']':
        return True
    if left == '{' and right == '}':
        return True
    return False


def isProperlyNested(S):
    stack = []

    for symbol in S:
        if symbol == '[' or symbol == '{' or symbol == '(':
            stack.append(symbol)
        else:
            if len(stack) == 0:
                return False
            last = stack.pop()
            if not isValidPair(last, symbol):
                return False

    if len(stack) != 0:
        return False

    return True


def main():
    N = int(input())

    for i in range(0, N):
        s = input()
        if isProperlyNested(s):
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
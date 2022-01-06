def fibonachi(num):
    if num < 1:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonachi(num - 1) + fibonachi(num - 2)

if __name__ == '__main__':
    print([fibonachi(num) for num in range(30)])
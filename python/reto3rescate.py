def list_operation(a, b, oper='add'):
    c = []
    if oper == 'add':
        for i in range(len(a)):
            c.append(a[i] + b[i])
    elif oper == 'sub':
        for i in range(len(a)):
            c.append(a[i] - b[i])
    elif oper == 'mult':
        for i in range(len(a)):
            c.append(a[i] * b[i])
    elif oper == 'div':
        for i in range(len(a)):
            c.append(a[i] / b[i])
    return c


def get_elem_index(a, elem=None):
    if elem == 'min':
        return min(a), a.index(min(a))
    elif elem == 'max':
        return max(a), a.index(max(a))
    else:
        return elem, a.index(elem)


def main():
    n = 0
    while n < 1:
        initial_data = input().split(' ')
        n, m = int(initial_data[0]), int(initial_data[1])
    actual_ex, request_ex = [], []

    for i in range(n):
        read_ex = 0
        while read_ex < 1:
            read_ex = int(input())
        actual_ex.append(read_ex)
        request_ex.append(0)

    for i in range(m):
        read_info = input().split(' ')
        branch, sis, dia = int(read_info[0]), int(
            read_info[1]), int(read_info[2])
        if 0 < branch <= n:
            if sis < 70 and dia < 50:
                request_ex[branch - 1] += 5
            elif 120 <= sis < 130 and 75 <= dia < 80:
                request_ex[branch - 1] += 10
            elif 130 <= sis < 150 and 80 <= dia < 90:
                request_ex[branch - 1] += 15
            elif 150 <= sis < 170 and 90 <= dia < 100:
                request_ex[branch - 1] += 25
            elif sis >= 170 and dia >= 100:
                request_ex[branch - 1] += 45
            elif sis >= 130 and dia < 80:
                request_ex[branch - 1] += 25

    final_ex = list_operation(actual_ex, request_ex, oper='sub')
    div_ex = list_operation(request_ex, actual_ex, oper='div')

    min_, index_min = get_elem_index(final_ex, elem='min')
    max_, index_max = get_elem_index(final_ex, elem='max')

    print(index_min + 1, min_)
    print(index_max + 1, max_)
    for i in range(n):
        print('{:} {:.2f}%'.format(i + 1, div_ex[i] * 100))


if __name__ == "__main__":
    main()

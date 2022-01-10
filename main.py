def digit(n):
    a = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    b = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    c = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    # 100の位の計算(nを100で割った整数を求める)
    d = n // 100
    # 10の位の計算(nからd * 100の値を引いた数を10で割った整数を求める)
    e = (n - d * 100) // 10
    # 1の位の計算(nからd * 100の値を引いた数を10で割った余りを求める)
    f = (n - d * 100) % 10
    if n >= 11 and n <= 19:  # nが11~19の数かを調べる
        return c[n - 11]
    elif d == 0:
        # 100の位があるか調べる
        if e == 0:
        # 10の位があるか調べる
            return a[f - 1]
        elif f == 0:
        # 1の位があるか調べる
            return b[e - 1]
        else:
            return b[e - 1] + " " + a[f - 1]
    elif e == 0:
        if f == 0:
            return a[d - 1] + " hundred"
        else:
            return a[d - 1] + " hundred " + a[f - 1]
    else:
        if f == 0:
            return a[d - 1] + " hundred " + b[e - 1]
        else:
            return a[d - 1] + " hundred " + b[e - 1] + " " + a[f - 1]


def integer_part(data):
    lists = ['thousand', 'million', 'billion', 'trillion']

    # 文字列検出
    try:
        int(data)
    except ValueError as e:
        print(-1)
        exit()

    # 負値検出
    if int(data) < 0:
        print(-1)
        exit()

    length = len(data)
    digit = length//3
    ans = ''
    if digit == 0:
        ans = digit(int(data))
    else:
        for i in range(digit+1):
            data, val = divmod(int(data), 1000)

            if val != 0:
                if i == 0 and val <= 999:
                    ans = digit(int(val))
                else:
                    ans = digit(int(val)) + ' ' + lists[i-1] + ' ' + ans

    ans = ans.capitalize()

    return ans


def decimal_part(data):
    # 文字列検出
    try:
        int(data)
    except ValueError as e:
        print(-1)
        exit()

    # 負値検出
    if int(data) < 0:
        print(-1)
        exit()

    length = len(data)
    ans = ''
    if length == 2:
        ans = digit(int(data))
    else:
        for i in range(length):
            val = data[i]
            if i == 0:
                ans = digit(int(val))
            else:
                ans = ans + ' ' + digit(int(val))

    return ans


def main():
    with open("input.txt") as f:
        for line in f:
            data = line.strip()

    data = data.split('.')
    if len(data) == 1:
        integer = integer_part(data[0])
        ans = integer
    elif len(data) == 2:
        integer = integer_part(data[0])
        decimal = decimal_part(data[1])
        ans = integer + ' point ' + decimal
    else:
        ans = -1

    print(ans)

if __name__ == '__main__':
    main()
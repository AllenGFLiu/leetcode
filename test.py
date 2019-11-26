def test(x):
    if x == 0: return True
    if x < 0: return False
    if x % 10 == 0: return False

    def inner_check(new_int):
        count = 0
        tmp_int = new_int
        last = tmp_int % 10
        if last == new_int:
            return True
        
        while tmp_int // 10:
            count += 1
            tmp_int = tmp_int // 10
        
        if tmp_int != last:
            return False

        tmp_int = (new_int - tmp_int*pow(10, count) - last) // 10
        
        return inner_check(tmp_int)

    return inner_check(x)


if __name__ == '__main__':
    print(test(121))
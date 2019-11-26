def test(strs):
    count = len(strs)
    if count == 0: return ''
    if count == 1: return strs[0]
    result = ''
    tmp_count = 1
    for index in range(len(strs[0])):
        for num in range(1, count):
            equal = False
            if len(strs[num]) >= index+1:
                tmp_count += 1
                if strs[num][index] == strs[0][index]:
                    equal = True
                    continue

        if index == 0 and not equal:
            return result

        if equal and tmp_count == count:
            result += strs[0][index]

    return result


if __name__ == '__main__':
    print(test(["c","acc","ccc"]))
def test(num1, num2):
    def inner_sum(num1, num2):
        i = len(num1) - 1 
        j = len(num2) - 1
        carry = 0
        res = ''
        
        while i >= 0 or j >= 0:
            v_i = int(num1[i]) if i >= 0 else 0 
            v_j = int(num2[j]) if j >= 0 else 0
            sum_value = v_i + v_j + carry 
            carry = sum_value // 10
            res = str(sum_value%10) + res
            i -= 1
            j -= 1
        
        if carry > 0:
            res = '1' + res

        return res

    x = len(num1) - 12
    y = len(num2) - 12
    
    
    j = y
    ten_count = 0
    sum_value = ''
    while j >= 0:
        ten_count = y-j
        i = x
        res = ''
        carry = 0
        while i >= 0:
            v_i = int(num1[i]) if i >= 0 else 0
            v_j = int(num2[j]) if j >= 0 else 0
            multiply_value = v_i * v_j + carry
            carry = multiply_value // 10
            res = str(multiply_value%10) + res
            i -= 1
        if carry > 0:
            res = str(carry) + res
        for _ in range(ten_count):
            res += '0'
        sum_value = inner_sum(sum_value, res)
        j -= 1
    
    return sum_value


if __name__ == '__main__':
    print(test('9', '99'))

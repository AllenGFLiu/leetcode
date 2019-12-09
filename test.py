def merge_sort(nums):
    
    def merge_array(array, p, q, r):
        pass

    def inner_sort(array, p, r):
        if p >= r: return

        q = (p+r) // 2
        inner_sort(array, p, q)
        inner_sort(array, q+1, r)
        merge_array(array, )

    inner_sort(nums, 0, len(nums)-1)

'''
我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。

（这里，平面上两点之间的距离是欧几里德距离。）

你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。

 

示例 1：

输入：points = [[1,3],[-2,2]], K = 1
输出：[[-2,2]]
解释： 
(1, 3) 和原点之间的距离为 sqrt(10)，
(-2, 2) 和原点之间的距离为 sqrt(8)，
由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
示例 2：

输入：points = [[3,3],[5,-1],[-2,4]], K = 2
输出：[[3,3],[-2,4]]
（答案 [[-2,4],[3,3]] 也会被接受。）
'''

from typing import Optional

# Solution 1: sort first ,then get points[:K]
def kClosest(points, K):
    points.sort(key=lambda point: point[0]**2+point[1]**2)
    return points[:K]

# Solution 2: divide and conquer
def kClosest(points, K):
    dist = lambda i: points[i][0]**2 + points[i][1]**2

    def work(p, r, K):
        if p >= r: return
        i = p
        j = r
        pivot = dist(random.randint(p, r))
        while p < r:
            while p < r and dist(p) < pivot: p += 1
            while p < r and dist(r) > pivot: r -= 1
            if dist(p) == pivot and dist(r) == pivot: break
            points[p], points[r] = points[r], points[p]
        
        if K <= p - i + 1:
            work(i, p, K)
        else:
            work(p+1, r, K-(p-i+1))


    work(0, len(points)-1, K)
    return points[:K]


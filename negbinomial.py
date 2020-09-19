import math

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def prob(n, p, r):
    return nCr(n-1, r-1)*(p**r)*(1-p)**(n-r)
def infoMeature(n, p, r):
    return float(-math.log2(prob(n, p, r)))

def sumProb(N, p, r):               #Khi thử với tham số N lớn
    sum = 0                         #Hàm sẽ trả về kết quả xấp xỉ bằng 1
    for i in range(r, N + 1):
        sum+=prob(i, p, r)
    return sum
    
def approxEntropy(N, p, r):                             #Entropy của 1 nguồn là trung bình lượng tin
    entropy = 0                                         # của tất cả các symbol nguồn thông tin
    for i in range(r, N + 1):                           #nên hàm approxEntropy trả về xấp xỉ entropy của nguồn tin geometric với số N lớn
        entropy += prob(i, p, r)*infoMeature(i, p, r)   
    return entropy
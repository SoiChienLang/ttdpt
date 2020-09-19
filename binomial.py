import math

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def prob(n, p, N):
    return nCr(N, n)*(((1-p)**(N-n))*(p**n))
    
    
def infoMeasure(n, p, N):
    return float(-math.log2(prob(n,p,N)))
    
    
def sumProb(N, p):              #Khi thử với tham số N lớn
    sum = 0                     #Hàm sẽ trả về kết quả xấp xỉ bằng 1
    for i in range(0, N + 1):
        sum += prob(i, p, N)
    return sum

def approxEntropy(N, p):                            #Entropy của 1 nguồn là trung bình lượng tin
    entropy = 0                                     # của tất cả các symbol nguồn thông tin
    for i in range(0, N + 1):                       #nên hàm approxEntropy trả về xấp xỉ entropy của nguồn tin geometric với số N lớn
        entropy+=prob(i, p, N)*infoMeasure(i, p, N) #Entropy với p=1/2 thực hiện với N=10000, p=1/2 xấp xỉ bằng 6.0
    return entropy
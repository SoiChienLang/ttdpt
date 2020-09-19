import math

def prob(n, p):
	return ((1-p)**(n-1))*p

def infoMeasure(n, p):
    return float(-math.log2(prob(n,p)))

def sumProb(N, p):              #Để kiểm chứng tổng xác suất của phân bố geometric bằng 1
    sum = 0                     #Thực hiện hàm sumProb(N, p) với số N lớn
    for i in range(1, N + 1):   #Kết quả trả về sẽ xấp xỉ bằng 1
        sum += prob(i, p)
    return sum

def approxEntropy(N, p):                        #Entropy của 1 nguồn là trung bình lượng tin
    entropy = 0                                 # của tất cả các symbol nguồn thông tin
    for i in range(1, N + 1):                   #nên hàm approxEntropy trả về xấp xỉ entropy của nguồn tin geometric với số N lớn
        entropy+=prob(i, p)*infoMeasure(i, p)   #Entropy với p=1/2 thực hiện với N=10000, p=1/2 xấp xỉ bằng 2
    return entropy

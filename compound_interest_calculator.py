p = float(input("Enter the principle amount : "))
if p == 0 :
    print("principle can't be zero")

r = float(input("Enter the annual interst rate(%) : "))
if r == 0 :
    print("rate vaule can't be zero")

t = float(input("Enter time duration : "))
if t == 0 :
    print("time duration can't be zero")

n = float(input("Enter the number of times interest is compounded per year : "))
if n == 0 :
    print("number can't be zero")

A = p * (1 + r/ (100*n ))**(n*t)

print("final amount : ", round(A, 2))
print("compound interest : ", round(A - p , 2))
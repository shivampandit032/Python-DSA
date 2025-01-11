
def fibo(n):
    if n <= 1:
        return n
    else :

        result = fibo(n-1)+fibo(n-2)    # this equation is called "Recurrence Realtion ".

        return result

n = int(input("Enter the number for which you want to find the fibonaci number : "))

result = fibo(n)

print(f"Result : {result}")
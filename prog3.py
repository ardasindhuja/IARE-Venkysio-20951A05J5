import time
start=time.time()
def reverse(string):
    if len(string)==0:
        return string
    else:
        return reverse(string[1:])+string[0]
a=str(input())
print(reverse(a))
end=time.time()
print(end - start)

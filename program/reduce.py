import functools as f
#reduce() with lambda()
x=[5,8,2,4,9,12,15]
ans=f.reduce((lambda a,b:a+b) ,x)
print(ans)

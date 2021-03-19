#withouut using list comprehension
a="python"
answer=[ ] #declare empty list
for x in a:
    answer.append(x)
print(answer)

#Using List comprehension
a="python"
answer=[x for x in a]
print(answer)
    

#How to change a set
#We add new element in existing set
#We remove element from existing set
#but we cannot change the value

#Add items
#suppose create a set
color={"red","blue","pink","orange"}
print("Color : ",color)
#Add single element in existing set means to add new color green in existing set color
#the use add()  inbuilt function
color.add("green")
print("After add color green : ",color)

#Add multiple elements to a existing set then use update()
color.update(["yellow","red","violet"])
print("After add multiple element : ",color)

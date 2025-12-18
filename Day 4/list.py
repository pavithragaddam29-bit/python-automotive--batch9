 #lists in python
food=[" idly","dosa","wada","poori","chapathi"]
print(food[0]) # printing the food items using the index number
print(food[1])
food[0]=" sambar"
print(food[0]) # replacing the itams 

food.append(" chapathi")
food.remove("wada")
food.pop(1) # removes according to index value
food.insert(0, "bonda")
food.sort()
food.clear()# clear list

for i in food:
    print(i)
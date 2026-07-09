myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

myFruitList[2] = "orange"
print(myFruitList)


myFinalAnswerTuple = ("apple","apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[2])
myFinalAnswerTuple[1] = "orange" : TypeError: A tuple is immutable

a = {"apple","apple", "banana", "pineapple", 1,1,1, False, False}
print(a)
print(type (a))

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple",
  "Paulo" : "cherry"
}
print(myFavoriteFruitDictionary)
print(myFavoriteFruitDictionary["Akua"])
myFavoriteFruitDictionary["Akua"] = "orange"
print(myFavoriteFruitDictionary)

print(type(myFavoriteFruitDictionary))
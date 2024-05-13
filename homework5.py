my_list = ["apple", "banana", "orange", "coconut", "grape", "lemon"]

print ("List: ", my_list)
print ("First element: ", my_list[0], "\nLast element: ", my_list[-1])
print ("Sublist: ", my_list[2:5])
my_list[2] = "kiwi"
print ("Modified list: ", my_list)

my_dict = {"цветок": "flower", "окно": "window", "стул": "chair", "словарь": "dictionary"}
print ("\nDictionary: ", my_dict)
print("Translation: ", my_dict.get("окно"))
my_dict.update ({"дверь": "door",
                 "ручка": "pen"})
my_dict.pop ("цветок")
print("Modified dictionary: ", my_dict)
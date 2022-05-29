# ----BIG O----
# also known as asymptotic analysis
# big O == bad scenerio
# omega  ==  best scenerio
# theta == mid case scenerio

# time and space complexity, which is the main purpose ?
# --------------------LIST-------------------------- #
num1 = 11
num2 = num1

print(f"The address of the varibale num1: {id(num1)}")
print(f"The address of the varibale num1: {id(num2)}")

num2 = 22

print(f"The address of the varibale num1: {id(num1)}")
print(f"The address of the varibale num1: {id(num2)}") # id has changed

# --------------------DICTIONARY-------------------------- #
dict1 = {
    "value": 11
}
dict2=dict1

print(f"The address of the varibale dict1: {id(dict1)}")
print(f"The address of the varibale dict2: {id(dict2)}")

dict2["value"] = 22
print(dict1["value"])

print(f"The address of the varibale dict1: {id(dict1)}")
print(f"The address of the varibale dict2: {id(dict2)}") # id didn't change and value changed


name = "Sam"
age = 29
height_m = 1.78
likes_python = True

print(f"Hello, {name}!")
print(f"{name} is {age} years old and {height_m} m tall.")
print(f"Likes Python: {likes_python}")

# age + 1 stays an int, so no .0 at the end
print(f"Next year {name} turns {age + 1}.")

print(type(name), type(age), type(height_m), type(likes_python))

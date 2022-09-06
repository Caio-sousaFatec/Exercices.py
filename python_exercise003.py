gender = input("are u male or female?")

height = float(input("what's ur height?"))


if gender == "male":
    ideal_height = (72.7*height) - 58
else:
    ideal_height = (62.1*height) - 44.7

print(f"your ideal height is {ideal_height}")

## that's all folks
total = 0
count = 0
while True:
   user_input = input("Enter a number")
   if user_input.lower() == "done":
       break
   try:
      number = float(user_input)
      total += number
      count += 1
   except ValueError:
      print("Invalid input!")
if count > 0:
    avarage = total / count
    print(f"Sum of input: {total}")
    print(f"Number of input: {count}")
    print(f"Avarage of input numbers: {avarage}")

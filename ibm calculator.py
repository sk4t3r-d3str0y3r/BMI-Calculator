weight = int(input("Give me your weight: "))

height = float(input("\nGive me your height: "))

bmi = (weight / height**2)

if (bmi <= 18.4): {
    print("You're underweight")}
elif (bmi >= 18.5 and bmi < 25): {
    print("You have a normal weight")}
elif (bmi >= 25 and bmi < 30): {
    print("You're overweight")}
elif (bmi >= 30): {
    print("You have obesity")}
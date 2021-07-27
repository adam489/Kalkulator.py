#Prosty kalkulator

#ta funkcja dodaje dwie liczby
def add(x , y):
    return x + y

#ta funkcja odejmuje dwie liczby
def subtract(x,y):
    return x - y

#ta funkcja mnoży dwie liczby
def multiply(x,y):
    return x * y

#ta funkcja dzieli dwie liczby
def divide(x,y):
    return x / y

print("Wybierz operacje: ")
print("1.Dodaj")
print("2.Odejmij") 
print("3.Pomnoż")
print("4.Podziel")



while True:
    #Tutaj użytkonik wybiera operację
    choice = input("Wybierz operacje(1/2/3/4): ")

    #Sprawdź czy wybrano jedną z opcji
    if choice in ('1','2','3','4'):
     num1 = float(input("Wprowadz pierwszą liczbę: "))
     num2 = float(input("Wprowadz druga liczbe: "))
     

    if choice == '1':
        print(num1, "+" ,num2,"=", add(num1,num2))

    elif choice == '2':
       print(num1, "-",num2, "=", subtract(num1,num2))

    elif choice == '3':
       print(num1, "*",num2,"=", multiply(num1,num2))

    elif choice == '4':
        print(num1, "/", num2, divide(num1,num2))
        break
else:
     print("Niewlasciwy wybor")


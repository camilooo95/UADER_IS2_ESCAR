#collatz

print("enter a number:")
try:
    number = (int(input()))
except ValueError:
          print("Please enter a valid INTEGER.")


def collatz(number):
    while number != 1:

        if number % 2==0:
            number = (number//2)
            #print(number)
            return (print(int(number)))

        elif number % 2==1:
            number = (3*number+1) 
            #print(number)
            return (print(int(number)))

        continue


collatz(number)
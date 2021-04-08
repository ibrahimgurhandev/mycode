fiz=['FizzBuzz' if number%15==0 else 'Fizz' if number%3==0 else 'Buzz' if number%5==0 else number for number in range(1,101)]
print(fiz)
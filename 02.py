n = int(input("Informe um número: "))
a = 0
b = 1

pertence = False

while a <= n:
    if a == n:
        pertence = True

    c = a + b
    a = b
    b = c

if pertence:
   print(f"O número {n} pertence à sequência de Fibonacci.")
else:
    print(f"O número {n} não pertence à sequência de Fibonacci.")

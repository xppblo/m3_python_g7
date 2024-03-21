import sys, time

print(sys.argv)
i = sys.argv[1]

i = int(sys.argv[1])

while i >0 :
    print(f"el valor de i es: {i}")
    time.sleep(1) # timepo de espera de 1 segudno
    i -= 1 #decremento de i (restando 1)
    
print("BOOOOOOOM!!")
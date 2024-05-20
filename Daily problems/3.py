# Take a number as input and print the multiplication table for it.

num = int(input("Enter a number to see its table: "))

table_limit = 10

for i in range(1,table_limit + 1):
    print(f"{num} X {i} = {num * i}")

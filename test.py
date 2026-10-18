def value(n):
    input_value = n
    value=0
    while input_value >= 10:
        value = 0

        for i in str(input_value): 
            if int(i) >=0:
                value=value+int(i)
        input_value=value   
    print(input_value)
    
n = int(input("Enter the value"))
value(n)



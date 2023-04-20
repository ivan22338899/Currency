with open('Currencies.csv', 'r') as csvfile:
    delimiter = ','
    column_index = 1
    min_value = float('infinity')
    max_value = 0
    total_sum = 0
    count = 0
    for row in csvfile:
    
        try:
            fields = row.split(delimiter)
            value = float(fields[column_index])
            value1 = float(fields[column_index])
            if value < min_value:
                min_value = value
            if value1 > max_value:
                max_value = value1
            total_sum += float(fields[column_index])
            count += 1
            sum1 = total_sum/count

        except ValueError:
            # якщо значення не може бути перетворене на тип float, пропускаємо його
            pass
        
    print("Мінімальне значення: ", min_value)
    print("Максимальне значення: ", max_value)
    print ("Середнє арифметичне курсу за цей період становить", sum1)
    
        
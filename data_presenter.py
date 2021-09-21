from csv import reader 

with open ('./CupcakeInvoices.csv', 'r') as read_obj:
    csv_reader = reader(read_obj) 

    for row in csv_reader:
        print(row)
        print(row[2])
        print((float(row[3]) * float(row[4])))

read_obj.close()
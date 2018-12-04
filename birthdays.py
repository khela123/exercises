class Birthdays:
    # xRead from an input file
    # xAdd entry to journal
    # xView entries
    # xSearch entries
    # Edit entries
    # Delete entries
    # xExport 

    def __init__(self):
        self.birthday_id = 1
        self.entries = []

    def read_input(self):
        row = []
        
        # with open('./journal.txt') as f:
        #     lines = f.readlines()
        import csv
        with open('./birthdays.csv',  newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print (row)

        # for row in lines:
        #     date, name = row.split('|')
        #     self.add_entry(date, name)

        # return lines


    def add_entry(self):
        import csv
        with open(r'birthdays.csv', 'a', newline='') as csvfile:
      		fieldnames = ['2001/06/16',' ', 'Aldrin A. Navarro']
    		writer = csv.writer(csvfile)
    		writer.writerow(fieldnames)

    csvfile.close()

birthdays = Birthdays()
birthdays.read_input()
print(birthdays)
birthdays = add_entry()
# birthdays.export_entries(file_name='birthdays.csv')
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


   
    def add_entry(self, date, text):s
        import csv
        with open('./birthdays.csv', 'w', newline='') as f:
            fieldnames = ['date', 'name']
            writer = csv.DictWriter(f, fieldnames= fieldnames)
            writer.writeheader()
            writer.writerow({'date': '3245235', 'name': 'dgasdg'})
   # def add_entry(self, date, text):
  #   	import csv
    	
		# with open('./birthdays.csv', 'w', newline='') as f:
		# 	fieldnames = ['date', 'name']
		#     writer = csv.DictWriter(f, fieldnames= fieldnames)
		#     write.writeheader()
		#     writer.writerow(['435', 'dfsg'])

		f.close()	

# birthdays = Birthdays()
# birthdays.read_input()
# print(birthdays)
# birthdays.export_entries(file_name='birthdays.csv')
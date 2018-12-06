import csv
class Birthdays:
    # xRead from an input file
    # xAdd entry to journal
    # xView entries
    # xSearch entries
    # Edit entries
    # Delete entries
    # xExport entries

    def __init__(self):
        self.birthday_id = 1
        self.entries = []

    def read_input(self):
        csvreader = []
        # results = {}

        # import csv
        with open('birthdays.csv', 'r') as csvfiles:
            csvreader = csv.reader(csvfiles, delimiter='\t')
            next(csvreader)

            for line in csvreader:
                print(line)

    def export_entries(self, file_name):
        csvreader = []
        # import csv
        with open('./birthdays.csv', 'r') as csvfiles:
            csvreader = csv.reader(csvfiles)

            with open('copy_birthdays.csv', 'w') as newfile:
                csvwriter = csv.writer(newfile,delimiter='\t')

                for line in csvreader:
                    csvwriter.writerow(line)

    def edit_entries(self, name, date):
        with open(r'birthdays.csv', 'a', newline='') as csvfile:
            fieldnames = ['2001/06/16', 'Aldrin A. Navarro']
            writer = csv.writer(csvfile)
            writer.writerow(fieldnames)
        

    def __str__(self):
        return 'Birthdays ' + str(self.birthday_id)

birthdays = Birthdays()
print(birthdays)
birthdays.read_input()
birthdays.edit_entries('date', 'name')
birthdays.export_entries(file_name='copy_birthdays.csv')
# birthdays.search_entries(query='Tallo')
import csv
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
        csvreader = []

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

    def edit_entry(self, name, date):
        with open(r'birthdays.csv', 'a', newline='') as csvfile:
            fieldnames = ['2001/06/16', 'Aldrin A. Navarro']
            writer = csv.writer(csvfile)
            writer.writerow(fieldnames)

            # w+
            # read,write, overwrite

        # csvfile.close()

    # def search_entries(self, query=''):
    #     matched_entries = [entry for entry in self.entries if query in entry['name']]
    #     print(matched_entries)
    #     return matched_entries            
    #     # birthdays.search_entries(query='Tallo')

    def __str__(self):
        return 'Birthdays ' + str(self.birthday_id)

birthdays = Birthdays()
birthdays.read_input()
print(birthdays)
birthdays.edit_entry('name', 'date')

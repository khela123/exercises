class Birthdays:    





    def export_entry(self, file_name):
        import csv
        with open('./birthdays.csv', 'r') as csvfiles
            csvreader = csv.reader(csvfiles, delimiter='\t')

            with open('copy_birthdays.csv', 'w') as newfile:
                csvwriter = csv.writer(newfile, delimiter='\t')

                for line in csvreader:
                    csvwriter.writerow(line)

    def read_input(self):
        # rows = []
        import csv
        with open('birthdays.csv', 'r') as csvfiles:
            csvreader = csv.reader(csvfiles, delimiter='\t')
            next(csvreader)

            for line in csvreader:
                print(line)

    def view_entries(self):
        import csv
        with open('birthdays.csv','r') as csvfiles:
            csvreader = csv.DictReader(csvfiles)

            for line in csvreader:
                print (line)

    def search_entries(self, query=''):
        matched_entries = [entry for entry in self.entries if query in entry['name']]
        print(matched_entries)
        return matched_entries            
        # ournal.search_entries(query='Tallo')

    def edit_entry(self, name, date)
        import csv
        with open(r'birthdays.csv', 'a', newline='') as csvfile:
            fieldnames = ['2001/06/16', 'Aldrin A. Navarro']
            writer = csv.writer(csvfile)
            writer.writerow(fieldnames)

        csvfile.close()


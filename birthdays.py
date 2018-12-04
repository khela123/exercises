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
        rows = []
        
        # with open('./journal.txt') as f:
        #     lines = f.readlines()
        import csv
        with open('./birthdays.csv',  newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print (row)

        for line in rows:
            # date, name = row.split('|')
            self.add_entry(date, name)

        return row
    def add_entry(self, date, name):
        self.entries.append({
            'date': date,
            'name': name
        })

    # def export_entries(self, file_name):
    #     with open(file_name, 'w') as f:
    #         f.writelines([
    #             '{date}|{name}'.format_map(entry)
    #             for entry in self.entries
    #         ])

    # def view_entries(self):
    #         print('Date\t   | Name')
    #         print('---' * 8)
    #         for entry in self.entries:
    #             date, text = entry.values()
    #             print(date, '|', end=' ')
    #             print(name)    



birthdays = Birthdays()
birthdays.read_input()
print(birthdays)
# birthdays.export_entries(file_name='birthdays2.csv')
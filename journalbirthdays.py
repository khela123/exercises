import csv
# import sys
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
        with open('birthdays.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            date = []
            name = []
            for row in reader:
                date = row[0]
                name = row[1]
                self.add_entry(name,date)
                # print(date)
                # print(name)

    def add_entry(self,name,date):
        self.entries.append({
            'date': date,
            'name': name
            })

    def view_entries(self):
        print('  Date          |        Name        ')
        print('---' * 11)
        for entry in self.entries:
            date, name = entry.values()
            print(date, ',', name)

    def search_entry(self, query=''):
        searchinput = input("Input chuchu you want to search: ")
        matched_entries = [entry for entry in self.entries if searchinput in entry['name'].lower()]

        print(matched_entries)
        return matched_entries

    def edit_entry(self):
      # choice = input("Do you want to edit? y/n")
        inputindex = int (input("Input index that you want to edit: "))
        inputelement = input("Input (n) for name and (d) for date: ")

        if inputelement in ("n", "N"):
            newname = input("New Name: ")
            self.entries[inputindex]['name'] = newname
        elif inputelement in ("d", "D"):
            newdate = input("New Date: ")
            self.entries[inputindex]["date"] = newdate
        else:
            print("Invalid input!")
            self.view_entries()

    def delete_entry(self):
        indextodel = int (input("Input index that you want to delete: "))
        print("Deleted: ",self.entries[indextodel])

        self.entries.pop(indextodel)
        self.view_entries()

        return self.entries

    def export_entries(self, file_name):
        with open(file_name, 'w') as f:
            f.writelines([
                '{date},\t{name} \n'.format_map(entry)
                for entry in self.entries
            ])
            
    def __str__(self):
        return 'Birthdays ' + str(self.birthday_id)


birthdays = Birthdays()
print(birthdays)
birthdays.read_input()
birthdays.view_entries()
birthdays.search_entry(query ="")
birthdays.edit_entry()
birthdays.delete_entry()
birthdays.export_entries(file_name='copy_birthdays.txt')
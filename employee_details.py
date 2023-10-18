# Create a Class to Create, retrieve, update, and 
# delete employee details from the dictionary. 

#     Employee details are ID, Name, DOB, Blood Group, and Address. 
# (Validate all the details are in the correct format)
#     ID should be created by the class for the new employee created 
# dynamically. other details can be given while creating the object. 
#     Should able to retrieve employee details by name or by ID or by both
#  information. 
#     Delete employee details should work with employee ID or name. if a 
# Duplicate name is available should ask for an ID. Always ask for 
# confirmation while deleting
# The above questions for this week

class Employee:
    def __init__(self, name, dob, bg, address):
        # self.__id = None
        self.__name = name
        self.__dob = dob
        self.__blood_group = bg
        self.__address = address

    def details(self):
        print(self.__name, self.__dob, self.__blood_group, self.__address, sep=', ')

    def update(self, name, dob, bg, address):
        self.__name = name if name else self.__name
        self.__dob = dob if dob else self.__dob
        self.__blood_group = bg if bg else self.__blood_group
        self.__address = address if address else self.__address

    def get_name(self):
        return self.__name

class HRMS:
    def __init__(self):
        self.emp_dict = {}
        self.last_id = 0

    def __create_id(self):
        self.last_id += 1
        return self.last_id

    def create(self, name, dob, bg, address):
        # name = input('Enter name')
        # dob = input('Enter dob')
        # blood_group = input('Enter blood group')
        # address = input('Enter address')
        self.emp_dict[self.__create_id()] = Employee(name, dob, bg, address)

    def update(self, count=3):
        if not count:
            return

        eid = int(input("Press Enter id you want to update"))
        if eid not in self.emp_dict:
            print('Employee Not Found. Enter correct Employee id.')
            self.update(count-1)
            return

        name = input('Enter name')
        dob = input('Enter dob')
        bg = input('Enter blood group')
        address = input('Enter address')
        self.emp_dict[eid].update(name, dob, bg, address)

    def delete(self, count=3):
        print('''Press 1: for giving id
      2: for giving name''')
        val = input('Enter your answer: ')
        if val == '1':
            self.__delete_by_id(3)
            return 
        elif val == '2':
            self.__delete_by_name()
            return
        else:
            print('Wrong option. Enter valid option again.\n')
            self.delete(count-1)

    def __delete_by_id(self, count=3, eid = None):
        if not count:
            return

        if not eid:
            eid = int(input("Press Enter id you want to delete"))

        if eid not in self.emp_dict:
            print('Employee Not Found. Enter correct Employee id.')
            self.__delete_by_id(count - 1)
            return

        if input("Conform Deletion press 'y' for 'yes' and 'n' for no:") == 'y':
            temp = self.emp_dict[eid]
            self.emp_dict[eid] = None
            del temp

    def __delete_by_name(self, count=3):
        if not count:
            return
        eids = []
        ename = int(input("Press Enter name you want to delete"))
        temp = 0
        for eid, val in self.emp_dict.items():
            if val.get_name() == ename:
                eids.append(eid)

        if len(eids) == 1:
            self.__delete_by_id(eid=eids[0])
        elif len(eids) > 1:
            print('Multiple names found!')
            self.__delete_by_id()
        else:
            print('Employee not found!')
            self.__delete_by_name(count-1)

    def details(self):
        print(self.emp_dict)
        for i, v in self.emp_dict.items():
            print('Emp id', i, end=': ')
            if v:
                v.details()
            else:
                print()

    def __get_id_name(self):
        eid = input("Enter id: ")
        ename = input("Enter name: ")

        if eid and ename:
            return int(eid), ename
        elif eid:
            return int(eid), None
        else:
            return None, ename

    def get(self, count=3):
        if not count:
            return
        
        eid, ename = self.__get_id_name()

        if ename and eid:
            if eid in self.emp_dict and str(self.emp_dict[eid].get_name()) == ename:
                print('Emp id', eid, end = ': ')
                self.emp_dict[eid].details()
                return
            print('Employee nt found!')
            self.get(count-1)

        elif eid:
            if eid in self.emp_dict:
                print('Emp id', eid, end = ': ')
                self.emp_dict[eid].details()
                return
            self.get(count-1)
        elif ename:
            eids = []
            for eid, val in self.emp_dict.items():
                if str(val.get_name()) == ename:
                    eids.append(eid)
            if not eids:
                print('Employee nt found!')
                self.get(count-1)
            
            for eid in eids:
                print('Emp id', eid, end = ': ')
                self.emp_dict[eid].details()
        else:
            self.get(count-1)


a = HRMS()
# a.create(1, 1, 1, 1)
# a.create(2, 2, 2, 2)
# a.create(3, 3, 3, 3)
# a.create(3, 4, 4, 4)
# a.details()

# a.update()
# a.details()
# a.delete()
# a.details()
# a.get()
operations = [None, a.create, a.get, a.update, a.delete]

print('''----- HRMS Portal ------
Select one option:
1: to create
2: get details
3: to update
4: to delete
''')
while True:
    index = int(input())
    func  = operations[index]
    func()
    a.get()

    print('press y to continue')
    x = input()
    if x != 'y':
        break
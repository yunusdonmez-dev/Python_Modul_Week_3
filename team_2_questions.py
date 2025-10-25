# Q1==================================================
class Rectangle():
    def __init__(self,width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
rect = Rectangle(5, 7)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

# Q2==================================================
class School():
    def __init__(self, name, foundation_year):
        self.name = name
        self.foundation_year = foundation_year
        self.students = []
        self.teachers = {}
        
    def add_new_student(self, student_name, class_name): 
        self.students.append({"name": student_name, "class": class_name})

    def add_new_teacher(self, teacher_name, branch):
        self.teachers[teacher_name] = branch
        
    def view_student_list(self):
        for student in self.students:
            print(f"{student['name']} - Class: {student['class']}")
            
    def view_teacher_list(self):
        for teacher, branch in self.teachers.items():
            print(f"{teacher} - Branch: {branch}")  
            
my_school = School("Nilufer High School", 2014)
my_school.add_new_student("Helin", "10A")
my_school.add_new_student("Aya", "11B")
my_school.add_new_teacher("Ms. Hulya", "Math")
my_school.add_new_teacher("Ms. Yasemin", "Physics")

my_school.view_student_list()
my_school.view_teacher_list()

# Q3==================================================
class Shape():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
class Rectangle(Shape):
    def calculate_area(self):
        return self.width * self.height
    
        
class Square(Shape):
    def calculate_area(self):
        return self.width * self.width
        
rectangle = Rectangle(4, 8)
square = Square(6,6)
        
print("Rectange Area:", rectangle.calculate_area())
print("Square Area:", square.calculate_area())
        
# Q4==================================================
class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
class OffRoadVehicle(Vehicle):
    def __init__(self, make, model, year, four_wheel_drive):
        super().__init__(make, model, year)
        self.four_wheel_drive = four_wheel_drive
        
        
    
class SportsCar(Vehicle): 
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed = max_speed
        
suv = OffRoadVehicle("Toyota", "Land Cruiser", 2022, True)
sportscar = SportsCar("Ferrari", "F8 Tributo", 2023, 340)

print("Off-Road Vehicle:")
print(f"Make: {suv.make}, Model: {suv.model}, Year: {suv.year}, 4x4: {suv.four_wheel_drive}")

print("\nSports Car:")
print(f"Make: {sportscar.make}, Model: {sportscar.model}, Year: {sportscar.year}, Max Speed: {sportscar.max_speed} km/h")       


# Q5==================================================

class Customer():
    def __init__(self, name, surname, tc_identification, phone):
        self.name = name
        self.surname = surname
        self.tc_identification = tc_identification
        self.phone = phone

    def display_information(self):
        print(f"Name: {self.name} {self.surname}")
        print(f"TC ID: {self.tc_identification}")
        print(f"Phone: {self.phone}")
    
    
class Account(Customer):
    def __init__(self, customer, account_number, balance):
        self.customer = customer
        self.account_number = account_number
        self.balance = balance
        
    def display_information(self):                   #bilgi gosterme metodu
        print(f"Name; {self.customer.name} {self.customer.surname}")
        print(f"TC ID: {self.customer.tc_identification}")
        print(f"Phone: {self.customer.phone}")
        
    def deposit(self, amount):                      #para yatirma metodu(deposit)
        self.balance += amount                      #şu anki bakiye üzerine yeni yatırılan parayı ekler.
        print(f"{amount} TL deposited. New balance: {self.balance}. TL")
        
    def money_check(self, amount):               #para cekme metodu
        if amount <= self.balance:       
            self.balance -= amount               #cekilmek istenen para cikariliyor sonuc guncel para
            print(f"{amount} TL withdrawn. Remaining balance: {self.balance} TL")
        else:
            print("Insufficient balance! Transaction cancelled.")
            
    def display_balance(self):                      #bakiye gosterme metodu
        print(f"Current balance: {self.balance}")
        
customer1 = Customer("Yasemin", "Kalemli", "3452347689","05324562398" )             #musteri olustur
account1 = Account(customer1, "TR12345", 1300)                                      #hesap olustur
account1.display_information()                      #musteri bilgilerini gosterir
customer1.display_information()

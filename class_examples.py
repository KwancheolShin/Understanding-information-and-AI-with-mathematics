class Student:
  def __init__(self,name,age,student_id,major): #클래스의 속성을 초기화(정의)한다.
    self.name = name
    self.age = age
    self.student_id = student_id
    self.major = major

  def introduce_name(self): #클래스 안에 클래스의 메서드(함수)를 만들어 사용할 수 있다.
    print(f"제 이름은 {self.name}입니다.")

  def introduce_age(self): #클래스 안에 클래스의 메서드(함수)를 만들어 사용할 수 있다.
    print(f"제 나이는 {self.age} 입니다.")

  def introduce_major(self): #클래스 안에 클래스의 메서드(함수)를 만들어 사용할 수 있다.
    print(f"제 전공은 {self.major} 입니다.")

  def introduce(self,greeting): #클래스 안에 클래스의 메서드(함수)를 만들어 사용할 수 있다.
    print(f"{greeting} 저는 {self.name}입니다. {self.age}살이고 {self.major} 전공을 공부하고 있습니다.")


#학생을 여러 명 등록하고 관리하는 class를 만들어보자.
class StudentManager:
  def __init__(self):
    self.students = [] # 학생 객체를 저장할 빈 리스트를 만든다

  def add_student(self,student):
    self.students.append(student)
    # 리스트는 append함수를 이용해서 값을 추가할 수 있다. append 메서드를 이용해서 학생 객체를 리스트에 추가한다.

  def show_students(self):
    print("학생 목록:")
    for student in self.students:
      print(f"이름: {student.name}, 나이: {student.age}, 학번: {student.student_id}, 전공: {student.major}")

  def count_students(self):
    print(f"총 학생수는 {len(self.students)}명 입니다.")
    


class Calculator:
  def __init__(self,year,price,owner):
    self.year = 2025
    self.price = price
    self.owner = owner

  def info(self):
    print(f"{self.owner} 소유의 계산기 입니다. {self.year}년산 이며 가격은 {self.price}입니다.")

  def add(self, a, b):
    return a+b

  def subtract(self,a,b):
    return a-b

  def average(self, *args): #*args는 갯수가 정해지지 않은 인자를 자유롭게 받을때 사용한다.
    return sum(args)/len(args)



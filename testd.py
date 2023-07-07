class Student:
	def __init__(self, name=None, age=0):
        self.__name = name
        self.__age = age
		# name 변수와 age변수를 private 으로 설정 하십시오
	def getAge(self):
		#age 변수 리턴
        return self.__age

	def getName(self):
		#name 변수 리턴
        return self.__name

	def setAge(self, age):
		#age 변수 변경
        self.__age = age

	def setName(self, name):
		#name 변수 변경
        self.__name = name

#객체 생성
obj = Student("Hong", 20)

name = obj.getName() #메소드를 통해서 리턴 받으십시오
age = obj.getAge() #메소드를 통해서 리턴 받으십시오
print(name, age)

#객체 속성 변경
# 메소드를 이용하여 obj 객체의 name을 "Hong" 에서 "Kim" 으로 변경하시오
obj.setName("Kim")
# 메소드를 이용하여 obj 객체의 age를 20에서 30으로 변경하십시오
obj.setAge(30)

name = obj.getName() #메소드를 통해서 리턴 받으십시오
age = obj.getAge()#메소드를 통해서 리턴 받으십시오
print(name, age)
def my_country(country="Rwanda"):
    print(f"Hello from {country}")

def greet(*names):  
    for name in names:
        print(f"Hello {name}")

def sum(*numbers):
    answer = 0
    for number in numbers:
        answer+=number
    return answer

# def multiply(*numbers):
#     product = 1
#     for num in numbers:
#         answer*=num
#     return product  
def student_attributes(**kwargs):
    for key,value in kwargs .items():
        print(f"{key}:{value}")


#def concatenate_args(*args,sep =""):
   # return sep.join(args)

def concatenate_args(*args):
    answers = ""
    for string in args:
        answers+=string
    return answers




def concatenate_kwargs(**kwargs):
   result = ""
   for key,value in kwargs.items():
    result+=value
   return result 







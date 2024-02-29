def greet_user(username):
    """인사말"""
    print(f"hello,{username.title()}")
    username = 'jeon'

input_name = 'jesse'
greet_user(input_name) #함수 호출
input_name = 'kim'
print(input_name)

#greet_user("cheese") #함수 호출
# help(greet_user)
#print(greet_user.__doc__)
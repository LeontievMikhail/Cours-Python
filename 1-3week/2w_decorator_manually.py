def my_shiny_new_decorator(a_function_to_decorate):
    def the_wrapper_around_the_original_function():
        print("i any code, which the  work ")
        a_function_to_decorate()
        print("i double code, printing after")
    return the_wrapper_around_the_original_function

def a_stand_alone_function():
    print("i a simple fn")

a_stand_alone_function()

a_stand_alone_function_decorated=my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()

print("______________-")

@my_shiny_new_decorator
def anothet_stand_alone_funciton():
    print("arbaiten suki")

anothet_stand_alone_funciton()


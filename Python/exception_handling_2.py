#raise and finally prctice
#raising custom exceptions - the custom exceptions should be raised as instances of a class 
#and these classes should inherit the Exception class 

class Accident(Exception):      #defining a class that inherits Exception 
    def __init__(self, msg):
        self.msg=msg
    
    def print_exception(self):
        print("User defined Exception: ", self.msg)

try:
    raise Accident('crash between two cars ')  #using the class defined above and raised a custom exception
except Accident as e:
    e.print_exception()


#finally 
def process_file():
    try:
        f=open("c:\\open_file.txt")  #opening a file 
        x=1/0        #division by zero throws exception
    except FileNotFoundError as e:     #here we are handling file related exceptions, but not handling zero division, so execution will stop here and remaining things also will not get executed 
        print("File Not Found ")
    finally:
        print("cleaning up the file ")
        f.close()              #but for handling files, close() is also one of the important task. But this will not executed if written without finally 
                               #bcz of zero division exception. Since it is not handled it will not allow remaining part of the program to be executed 
                               

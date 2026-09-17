# from abc import ABC, abstractmethod 

# class Institite_10000CODERS(ABC): # main asbtarct base clas
    
#     @abstractmethod  # decorator
#     def k_coders(self): # abstrct method :-- parent
#         pass
       
# class Agentic_AI(Institite_10000CODERS):
#     def __init__(self):
#         print("agentic ai course")

#     def k_coders(self): # same
#         print("agentyc ai 1st batch")   

# class Data_Science(Institite_10000CODERS):
#     def __init__(self):
#         print("ds course") 

#     def k_coders(self): # same
#         print("ds 25th batch")    


# obj2=Data_Science()
# obj1=Agentic_AI()

# print(obj2.k_coders )# ds 25th batch

#     # import ABC 
#     # make it parent  to parent


from abc import ABC, abstractmethod 

main_bal=1000 # global var
ph_pay_pin="123456"

class Zepto(ABC):

    @abstractmethod
    def payement(self):
        pass 

class ZeptoApp(Zepto):
    def __init__(self):
        pass 

    def payement(self,inc_pinNumber):
        amt=500.12 
        if inc_pinNumber == ph_pay_pin:
            if amt > main_bal:
                print("insuffcinet funds")
            else:
                print("payment done .. ")    
        
obj=ZeptoApp()
obj.payement(input("enter pin to proceddw with payment")) # 123456
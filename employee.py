"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

# Base employee class for all others to inherit from (abstract class, do not instantiate)
class Employee(object):
    # Initialise the employee (minus their base pay type)
    def __init__(self, name, commission_count, commission_pay):
        self.name = name
        self.commission_count = commission_count
        self.commission_pay = commission_pay

    # Return the total pay of the employee
    def get_pay(self):
        return self.get_base_pay() + self.get_commission_pay()

    # Convert this employee to a string containing their names and the details of their employment
    def __str__(self):
        # Start with their name
        string = self.name
        # Add information about their base pay (determined by sub type)
        string += " " + self.get_base_string()
        # Add their commission pay
        string += self.get_commission_str()
        # Add their total pay
        string += ".  Their total pay is " + str(self.get_pay()) + "."
        # Return the string
        return string

    # Get this employee's pay for commissions
    def get_commission_pay(self):
        return self.commission_count * self.commission_pay

    # Get the string containing this employee's pay for commissions
    def get_commission_str(self):
        # No string if there were no commissions
        if self.commission_count == 0:
            return ""
        # Only one commission is labelled as "a bonus commission"
        elif self.commission_count == 1:
            return " and receives a bonus commission of " + str(self.commission_pay)
        # Any more is labelled as "a commission for {n} contract(s)"
        else:
            return " and receives a commission for " + str(self.commission_count) + " contract(s) at " + str(self.commission_pay) + "/contract"

    # Get the base pay of the employee (abstract method)
    def get_base_pay():
        pass

    # Get information about their base pay (abstract method)
    def get_base_string():
        pass

# Salary employee (works on a monthly pay)
class SalaryEmployee(Employee):
    # Initialise SalaryEmployee (assuming no contracts by default)
    def __init__(self,name,monthly_pay,commission_count = 0,commission_pay = 0):
        super(SalaryEmployee,self).__init__(name,commission_count,commission_pay)
        self.monthly_pay = monthly_pay

    # Get the base pay of the employee
    def get_base_pay(self):
        return self.monthly_pay

    # Get the base information string of the employee
    def get_base_string(self):
        return "works on a monthly salary of " + str(self.monthly_pay)

class ContractEmployee(Employee):
    # Initialise ContractEmployee (assuming no contracts by default)
    def __init__(self,name,contract_hours,contract_pay_per_hour,commission_count = 0,commission_pay = 0):
        super(ContractEmployee,self).__init__(name,commission_count,commission_pay)
        self.contract_hours = contract_hours
        self.contract_pay_per_hour = contract_pay_per_hour
    
    # Get the base pay of the employee
    def get_base_pay(self):
        return self.contract_hours * self.contract_pay_per_hour
        
    # Get the base information string of the employee
    def get_base_string(self):
        return "works on a contract of " + str(self.contract_hours) + " hours at " + str(self.contract_pay_per_hour) + "/hour"
        

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie',4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = ContractEmployee('Charlie',100,25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryEmployee('Renee',3000,4,200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractEmployee('Jan',150,25,3,220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryEmployee('Robbie',2000,1,1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = ContractEmployee('Ariel',120,30,1,600)

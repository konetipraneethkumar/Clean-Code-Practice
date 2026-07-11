"""
from Ramayanam Garikipati Narasimha rao Garu said:
our income Should divide 4 parts like this
1/2 th % - should use for our daily needs and Entertainment
1/4 th % - Future Needs
1/8 th % - donation
1/8 th % - Reserved funds.
reference URL :- https://youtube.com/shorts/lHi83IcsJ1U?si=lgaip1nGG75o9i7z

"""
import json

# Goal 1 user enter the salary and the money instantly divided into 4 parts as specified
class SalaryAllocation:
    HOUSE_AND_ENTERTAINMENT_SLAB = 1/2
    FUTURE_GOALS_SLAB = 1/4
    DONATION_SLAB = 1/8
    RESERVED_SLAB = 1/8
    TITLE = "Salary Allocation"

    def __init__(self,salary_amount):
        if salary_amount <= 0:
            raise ValueError("Salary amount must be greater than zero")
        self.salary_amount = salary_amount


    def display_salary(self):
        """ Displlaing salary allocation title """
        return f"{self.Title} for {self.salary_amount}"


    def house_and_entertainment(self):
        """ House_And_Entertainment Calculation """
        return self.salary_amount * self.HOUSE_AND_ENTERTAINMENT_SLAB


    def future_goals(self):
        """ Future_Goals Calculation """
        return self.salary_amount * self.FUTURE_GOALS_SLAB


    def donation(self):
        """ Donation Calculation """
        return self.salary_amount * self.DONATION_SLAB


    def reserved(self):
        """ Reserved_Amount Calculation """
        return self.salary_amount * self.RESERVED_SLAB


    def json_response(self):
        """ Displaying Json Response """

         return json.dumps({
             "Title": self.display_salary(),
             "Salary": self.salary_amount,
             "House And Entertainment": self.house_and_entertainment(),
             "Future Goals": self.future_goals(),
             "Donation": self.donation(),
             "Reserved": self.reserved()
         })

obj = SalaryAllocation(100000)
x=obj.json_response()
print(x)
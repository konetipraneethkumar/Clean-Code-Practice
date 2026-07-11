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
    """ class Variables"""
    HOUSE_AND_ENTERTAINMENT_SLAB = 1/2
    FUTURE_GOALS_SLAB = 1/4
    DONATION_SLAB = 1/8
    RESERVED_SLAB = 1/8
    TITLE = "Salary Allocation"


    def __init__(self,salary_amount) -> None:
        """ Constructor with default parameter salary_amount """
        if salary_amount <= 0:
            raise ValueError("Salary amount must be greater than zero")
        self.salary_amount = salary_amount


    def display_salary(self) -> str:
        """ Returning the salary allocation title."""
        return f"{self.TITLE} for {self.salary_amount}"


    def house_and_entertainment(self) -> float:
        """ House_And_Entertainment Calculation """
        return self.salary_amount * self.HOUSE_AND_ENTERTAINMENT_SLAB


    def future_goals(self) -> float:
        """ Future_Goals Calculation """
        return self.salary_amount * self.FUTURE_GOALS_SLAB


    def donation(self) -> float:
        """ Return the allocated donation amount."""
        return self.salary_amount * self.DONATION_SLAB


    def reserved(self) -> float:
        """ Reserved_Amount Calculation """
        return self.salary_amount * self.RESERVED_SLAB


    def to_json(self) -> str:
        """ Displaying Json Response """

        data =  json.dumps({
             "title": self.display_salary(),
             "salary": self.salary_amount,
             "house_and_entertainment": self.house_and_entertainment(),
             "future_goals": self.future_goals(),
             "donation": self.donation(),
             "reserved": self.reserved()
         })
        return data

if __name__ == "__main__":
    obj = SalaryAllocation(100000)
    x = obj.to_json()
    print(json.dumps(x, indent=4))

### what worked well
Copilot was able to make some suggetions regarding alternative code to facilitate divison by 0
On the same suggetion it was able to include a try and except block that was not to broad to point out the specific error
It was able to provide inline feedback if typed the correct prompt
### challenges
Sometime copilot suggested codes were too advanced to challenge or understand
### prompt engineering tips i learned
paraphrasing can make a diffirence by asking the same question differently
### code copilot generated

def basic_calculate(self, num1, op, num2):
        """Perform basic calculation; validate inputs and handle division by zero."""
        if op not in self.operators:
            raise ValueError(f"Unsupported operator: {op!r}")
        try:
            a = float(num1)
            b = float(num2)
        except (TypeError, ValueError):
            raise TypeError("num1 and num2 must be numbers")
        try:
            return self.operators[op](a, b)
        except ZeroDivisionError:
            raise ZeroDivisionError("Division by zero")

### My productivity assessment           
On the scale of 1-10, my assessment on the copilot utilization will definetly be close to 8.
This is because once i know to prompt and the expected results i should be able to maximize the potential.
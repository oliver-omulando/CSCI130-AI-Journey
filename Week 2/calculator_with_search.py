# calculator_with_search.py
#Oliver Omulando CSCI 130
# smart calculator with Equation solver
# Users can search concepts from chapter 3

import operator
import math



class smartCalculator:
    '''Smart Calculator with Basic Operations and Search Capability'''

    def __init__(self):
        self.operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '^': operator.pow
        }

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

    def solve_for_x(self, target, operation, known_value, x_position='left'):
        '''Solve simple equations like: x + 5 = 10 or 3 * x = 15.
           Uses a simple brute-force search approach to find x.'''

        # search range
        min_x = -100
        max_x = 100
        step = 0.1

        current_x = min_x
        best_x = None
        best_difference = float('inf')
        while current_x <= max_x:
            # calculate the result with current x
            if x_position == 'left':
                result = self.operators[operation](current_x, known_value)
            else:
                result = self.operators[operation](known_value, current_x)

            # check how close we are to the target
            difference = abs(result - target)
            if difference < best_difference:
                best_difference = difference
                best_x = current_x

            current_x += step

        return best_x

    def equation_solver_menu(self):
        ''' Interactive menu for solving. '''
        print("\n" + "="*50)
        print("EQUATION SOLVER(using search)")
        print("="*50)
        print("I can solve equations like:")
        print("  x + 5 = 10")
        print("  3 * x = 15")
        print(" 10 - x = 7")
        print("  x / 2 = 8")
        print(" 20 / x = 4")

        # Get equations parts from user
        equation = input("Enter your equation (e.g., x + 5 = 10): ")
        # Parse the equation
        try:
            left_side, right_side = equation.split("=")
            right_side = right_side.strip()
            left_side = left_side.strip()
        except Exception:
            print("Invalid equation format.")
            return
        # Determine the operation and known value
        for op in self.operators.keys():
            if op in left_side:
                operation = op
                parts = left_side.split(op)
                if 'x' in parts[0]:
                    x_position = 'left'
                    known_value = float(parts[1])
                else:
                    x_position = 'right'
                    known_value = float(parts[0])
                target = float(right_side)
                break
        else:
            print("Invalid equation format.")
            return

        # Solve for x
        result = self.solve_for_x(target, operation, known_value, x_position)
        if result is not None:
            print(f"Solution: x = {result}")
        else:
            print("No solution found.")

    def visualize_search(self, target, operation, known_value, x_position='left'):
        '''Show the search process step by step to help understand how search algorithms explore possibilities.'''
        print("\n SEARCHING FOR SOLUTION...")
        print (f" Goal: Find x where ", end="")
        if x_position == 'left':
            print (f"x {operation} {known_value} = {target}")
        else:
            print (f"{known_value} {operation} x = {target}")

        # show first few search steps
        test_values = [-10, -5, 0, 5, 10, 15, 20]
        print("\n Testing values:")
        print("_" * 40)

        for x in test_values:
            if x_position == 'left':
                result = self.operators[operation](x, known_value)
            else:
                result = self.operators[operation](known_value, x)

            distance = abs(result - target)
            if distance < 0.0001:
                print(f" x = {x:6.1f} => Result = {result:6.1f} (FOUND IT!)")
                return x
            else:
                print(f" x = {x:6.1f} => Result = {result:6.1f} [off by {distance:.1f}]")

        print("\n...continuing detailed search...")
        # Now do the full search
        return self.solve_for_x(target, operation, known_value, x_position)

def main():
    ''' Main program loop '''
    calc = smartCalculator()
    while True:
        print("\n" + "="*50)
        print("SMART CALCULATOR WITH AI ASSISTANCE")
        print("="*50)
        print("1. Basic Calculation")
        print("2. Solve equation (using search)")
        print("3. See Search Visualization")
        print("4. About search algorithms")
        print("5. Exit")

        choice = input("\nChoose option (1-5): ")

        if choice == '1':
            # Get two numbers and operation from user, then calculate
            try:
                num1 = float(input("Enter first number: "))
                op = input("Enter operator (+, -, *, /, ^): ")
                num2 = float(input("Enter second number: "))
                result = calc.basic_calculate(num1, op, num2)
                print(f"Result: {num1} {op} {num2} = {result}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == '2':
            calc.equation_solver_menu()
        elif choice == '3':
            print("\nLet's solve: x + 5 = 12")
            result = calc.visualize_search(12, '+', 5, 'left')
            print(f"\n Solution: x = {result}")
        elif choice == '4':
            print("\n ABOUT SEARCH ALGORITHMS")
            print("-"*40)
            print("This calculator uses a simple linear search:")
            print(" It tries different values for x")
            print(" checks if each value solves the equation")
            print(" keeps track of the best answer")
            print(" this is similar to brute force search")
            print("\nReal search algorithms (chapter 3) are smarter:")
            print("BFS: Explores all possibilities level by level")
            print("DFS: Explores one path deeply before trying others")
            print("A*: Uses heuristics to search more efficiently")
        elif choice == '5':
            print("\nThanks for using SmartCalculator! Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
    
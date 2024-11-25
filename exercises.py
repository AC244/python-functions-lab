# Function to calculate the area of a triangle
def calculate_area_triangle(base, height):
    return (base * height) / 2

# Call the function
print('Exercise 1:', calculate_area_triangle(10, 5))


# Function to calculate simple interest
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Call the function
print('Exercise 2:', simple_interest(1000, 5, 2))


# Function to apply a discount
def apply_discount(price, discount_percentage):
    return price - (price * (discount_percentage / 100))

# Call the function
print('Exercise 3:', apply_discount(100, 25))


# Function to convert temperature
def convert_temperature(temp, unit):
    if unit == 'C':
        return (temp * 9/5) + 32  # Celsius to Fahrenheit
    elif unit == 'F':
        return (temp - 32) * 5/9  # Fahrenheit to Celsius
    else:
        return "Invalid unit. Use 'C' or 'F'."

# Call the function
print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))


# Function to calculate the sum of all numbers from 1 to n
def sum_to(n):
    return sum(range(1, n + 1))

# Call the function
print('Exercise 5:', sum_to(6))


# Function to find the largest of three numbers
def largest(a, b, c):
    return max(a, b, c)

# Call the function
print('Exercise 6:', largest(1, 2, 3))


# Function to calculate the tip
def calculate_tip(bill_amount, tip_percentage):
    return bill_amount * (tip_percentage / 100)

# Call the function
print('Exercise 7:', calculate_tip(50, 20))


# Function to calculate the product of an arbitrary number of numbers
def product(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Call the function
print('Exercise 8:', product(2, 5, 5))


# Function to perform basic arithmetic operations
def basicCalculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b if b != 0 else "Division by zero is not allowed."
    else:
        return "Invalid operation. Use 'add', 'subtract', 'multiply', or 'divide'."

# Call the function
print('Exercise 9 Result:', basicCalculator(10, 5, "subtract"))

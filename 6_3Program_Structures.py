#Write a function with a variable named x, and an outer script with a global variable x. Inside the function, print x and explain which scope's x was used based on the LEGB rule.
# Global variable
x = "Global"
def outer_function():
    # Enclosing scope variable
    x = "Enclosing"

    def inner_function():
        # Local scope variable
        x = "local"
        print(f"Inner scope (L): {x}")  # uses local x
    inner_function()
    print(f"Outer scope (E): {x}")  # uses enclosing x

outer_function()
print(f"Global scope (G): {x}")  # uses global x
print(f"Built-in scope (B): {len}")  # uses built-in name  
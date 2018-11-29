# Overview of lambda function

# Function to apply
def times2(var):
    return var * 2

if __name__ == "__main__":

    print("Individual run: 5 * 2 = ", times2(5))

    # Create a sequence
    seq = [2, 4, 6, 8]
    # Map takes a function and the sequence you want to map onto the function, return a <map> object
    print("Map function: ", map(times2, seq))
    # If you want to return the list, cast the map() as a list
    print("Map function cast as list: ", list(map(times2, seq)))

    print("-- -- --")

    # Rewrite the function as a lambda expression
    # The 'var' before the colon is the arguement, everything after is the returned
    print("Using lambda: ", list(map(lambda var:var*2, seq)))
    # Think of lambda as a function without the clutter - it places in things like 'def' and 'return'
    # Lambda is generally used with map()
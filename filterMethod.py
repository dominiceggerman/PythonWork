# Overview of filter method

# Function to apply


if __name__ == "__main__":
    
    # Sequence
    seq = [1, 2, 3, 4, 5]
    print("Sequence: ", seq)

    # Can pass a function or lambda to filter, which will filter out and return boolean values
    print("Filter object: ", filter(lambda num: num % 2 == 0, seq))
    print("Cast as list: ", list(filter(lambda num: num % 2 == 0, seq)))
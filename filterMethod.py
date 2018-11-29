# Overview of filter method

# Function to apply


if __name__ == "__main__":
    
    # Sequence
    seq = [1, 2, 3, 4, 5]
    print("Sequence: ", seq)

    # Can pass a function or lambda to filter, which will filter out and return boolean values
    print("Filter object: ", filter(lambda num: num % 2 == 0, seq))
    print("Cast as list: ", list(filter(lambda num: num % 2 == 0, seq)))

    print("-- -- --")

    # Example of conditional in lambda
    seq2 = ['soup','dog','salad','cat','great']
    print("String sequence to filter: ", seq2)
    print("Lambda filter with conditional: ", list(filter(lambda st:"s" in st, seq2)))
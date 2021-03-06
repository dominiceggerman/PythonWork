# By Dominic Eggerman
# Pull data from csv and return array (without pandas)

# Pull data to simple array
def pullToArray(filename):
    with open(filename, mode="r") as infile:
        data = [line.strip().split(",") for line in infile]
    return data

if __name__ == "__main__":

    filename = input("Enter file path: ")
    arr = pullToArray(filename)
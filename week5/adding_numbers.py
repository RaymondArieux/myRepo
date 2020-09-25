import sys
def add_them_all(filename):
    sum = 0
    ### Your code here
    with open(filename, "r") as f:
        for line in f.readlines():
            string_int = int(line,10)
            sum = sum + string_int
    ### End of your code
    return sum
if __name__ == "__main__":
    fname = sys.argv[1]
    print(f"Processing {fname}")
    print(add_them_all(fname))
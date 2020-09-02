import logging
logging.basicConfig(level=logging.DEBUG)

def squared_threes():
    return_value=[]
    # your code goes here
    return_value = [value **2 for value in range(0,100,3)]
    #end shouldnt go beyond here
    return return_value

if __name__=="__main__":
    for x in squared_threes():
        print(x)
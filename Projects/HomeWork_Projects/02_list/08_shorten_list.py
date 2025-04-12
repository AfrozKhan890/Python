# Fill out the function shorten(lst) which removes elements from the end of lst, which is a  list, and prints each item it removes 
# until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a 
# main() function for you which gets a list and passes it into your function once you run the program. For the autograder
# to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.


Max_length = 3

def shorten(lst):
    while len(lst) > Max_length:
        itemRemoved = lst.pop()  
        print("Removed:", itemRemoved)

def get_lst():
    lst = []
    element= input("Enter an element (or press enter to stop): ")
    while element!= "":
        lst.append(element)
        element= input("Enter an element (or press enter to stop): ")
    return lst

def main():
    lst = get_lst()
    print("Original list:", lst)
    shorten(lst)
    print("Final list:", lst)

main()

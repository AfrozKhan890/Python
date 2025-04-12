# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.


lst = []
def get_first_element(lst):
    element= input("Enter the element or press enter to stop.");
    while element != "":
        lst.append(element)
        element = input("Enter the element or press enter to stop. ")
    if lst: 
        print("First element in the list is:", lst[0]) 
    else:
        print("The list is empty.")
        
def main():
    get_first_element(lst)

main()
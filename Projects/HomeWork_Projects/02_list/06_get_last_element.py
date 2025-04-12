# # Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.


lst = []
def get_last_element(lst):
    element= input("Enter the element or press enter to stop.");
    while element != "":
        lst.append(element)
        element = input("Enter the element or press enter to stop. ")
    if lst: 
        print("Last element in the list is:", lst[-1]) 
    else:
        print("The list is empty.")
        
def main():
    get_last_element(lst)

main()
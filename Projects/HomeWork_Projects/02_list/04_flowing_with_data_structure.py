def add_three_copies(lst, data):
    for _ in range(3):
        lst.append(data)  
        
def main():
    message = input("Enter a message to copy: ") 
    
    messages = []
    print("List before:", messages)
    
    add_three_copies(messages, message)
    
    print("List after:", messages)

if __name__ == "__main__":
    main()

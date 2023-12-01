class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        if not self.is_empty():
            popped_item = self.items.pop()
            print(f"Popped {popped_item} from the stack.")
            return popped_item
        else:
            print("Cannot pop from an empty stack.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Cannot peek into an empty stack.")
            return None

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    # Create a stack
    stack = Stack()

    while True:
        print("\nOptions:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Stack Size")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            item = input("Enter the item to push onto the stack: ")
            stack.push(item)
        elif choice == "2":
            stack.pop()
        elif choice == "3":
            top_item = stack.peek()
            if top_item is not None:
                print(f"Top of the Stack: {top_item}")
        elif choice == "4":
            print(f"Stack Size: {stack.size()}")
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

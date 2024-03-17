class My_sort:
    def __init__(self):
        self.liste = []

    def liste_input(self):
        self.liste = input("Please enter numbers (max 10): ").strip().split()[:10]
        #input("Please enter numbers (max 10): "):
        #This prompts the user to enter a sequence of numbers, with a message "Please enter numbers (max 10): ". The input provided by the user is captured as a string.
        # The strip() method is used to remove any leading or trailing whitespace characters 
        # from the input string. 
        # This ensures that there are no unnecessary spaces before or after the numbers entered 
        # by the user.
        # The split() method without any arguments splits the input string into a list 
        # of substrings based on whitespace characters (spaces, tabs, newlines, etc.). 
        # Each substring in the resulting list represents a number entered by the user.
        # [:10]: This is a slice operation that limits the list to the first 10 elements. 
        # If the user entered more than 10 numbers, only the first 10 numbers will be 
        # retained in the list. 
        # If there are fewer than 10 numbers, all of them will be kept.s
        # elf.liste = ...: Finally, the resulting list of numbers (as strings) or 
        # the first 10 numbers entered by the user is assigned to the liste attribute of 
        # the My_sort object. This attribute holds the numbers that will be sorted and 
        # processed further in the program.
        
        if len(self.liste) > 10:
            print("Entered more than 10 numbers. Taking first 10.")

        self.liste = list(map(int, self.liste))  
        # The map() function applies the function int() to each element of the iterable self.liste. 
        # Here, int() converts each element of self.liste (which are initially strings) into integers.

    def fill_empty(self):
        n = len(self.liste)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.liste[j] > self.liste[j+1]:
                    self.liste[j], self.liste[j+1] = self.liste[j+1], self.liste[j]

    def display(self):
        print("Sorted list:", self.liste)


Enter_liste = My_sort()
Enter_liste.liste_input()
Enter_liste.fill_empty()
Enter_liste.display()

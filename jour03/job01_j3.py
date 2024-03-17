class Task:  
    def __init__(self, title, description, due_date, completed): 

        self.__title = title         
        self.__description = description
        self.__due_date = due_date
        self.__completed = completed
      
    def get_title(self): 
        return self.__title
    
    def set_title(self, title): 
        self.__title = title
    
    def get_description(self):
        return self.__description
    
    def set_description(self, description):
        self.__description = description

    def get_due_date(self):
        return self.__due_date
    
    def set_due_date(self, due_date):
        self.__due_date = due_date

    def get_completed(self):
        return self.__completed 
    
    def set_completed(self, completed):
       self.__completed = completed

   
        



# demonstration of observer pattern

class Kens:
    def __init__(self, fname="Ken", lname="New", posts:list=[]):
        self.fname = fname 
        self.lname = lname
        self.posts = posts
        self.observers = []
        self.events = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)
    
    #loop through subscribed observers; self here represents the broadcasting object
    # messager passes the broadcasting object to the observer update method
    def notify_observers(self, event_data):
        messager = self
        for observer in self.observers:
            observer.update(messager=messager, event_data=event_data)
    
    #function to be called by each observer; self here represents the observer object
    def update(self, messager, event_data):
        self.events.append(event_data)
        print(f"{self.fname} {self.lname} got a message from {messager.fname} {messager.lname}: {event_data}")

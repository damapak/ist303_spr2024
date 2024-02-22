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

#instantiate some Kens
# for use in an interactive session: import observer, then assign k1,k2,k3,k4 = observer.main()
def main():
  k1 = Kens(fname="Ken",lname="Masters",posts=[23,45,66])
  k2 = Kens(fname="Ken",lname="Just Ken",posts=[12,13])
  k3 = Kens(fname="Ken",lname="Obi")
  k4 = Kens(fname="Ken",lname="YouDigIt")
  k1.add_observer(k2)
  k1.add_observer(k3)
  return k1, k2, k3, k4
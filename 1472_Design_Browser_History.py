class Node:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.curr = self.head
        

    def visit(self, url: str) -> None:
        self.curr.next = Node(url)
        self.curr.next.prev = self.curr 
        self.curr = self.curr.next
        self.curr.next = None
        

    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev 
            steps -= 1
        
        return self.curr.url
        
        
    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next 
            steps -= 1
        
        return self.curr.url
                
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


"""
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage,]
        self.forwardHistory = [] 
        

    def visit(self, url: str) -> None:
        self.history.append(url)
        self.forwardHistory = []
        

    def back(self, steps: int) -> str:
        for i in range(steps):
            if len(self.history) > 1:
                self.forwardHistory.append(self.history[-1])
                self.history.pop()
                #print(self.history)
            else:
                break
        
        return self.history[-1] if self.history else None

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.forwardHistory:
                self.history.append(self.forwardHistory[-1])
                self.forwardHistory.pop()
            else:
                break
        
        return self.history[-1] if self.history else None
"""
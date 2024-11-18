class Pila:
    def __init_(self):
        self.items = []
        
        
    def is_empty(self):
        return len(self.items) == 0
    
    
    def push(self, item):
        self.items.append(item)
        
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
        
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
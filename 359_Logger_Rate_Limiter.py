class Logger:

    def __init__(self):
        self.oldMessageMap = {}
        self.newMessageMap = {}
        self.lastSeen = 0
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if timestamp >= self.lastSeen + 20:
            self.oldMessageMap.clear()
            self.newMessageMap.clear()
            self.lastSeen = timestamp
        elif timestamp >= self.lastSeen + 10:
            self.oldMessageMap = self.newMessageMap
            self.newMessageMap = {}
            self.lastSeen = timestamp

        if message in self.newMessageMap:
            return False
        if message in self.oldMessageMap and self.oldMessageMap[message] + 10 > timestamp:
            return False
        
        self.newMessageMap[message] = timestamp
        
        return True
        
        
        
class Logger1:

    def __init__(self):
        self.messageMap = {}
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messageMap or timestamp >= self.messageMap[message]:
            self.messageMap[message] = timestamp + 10
            return True
        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
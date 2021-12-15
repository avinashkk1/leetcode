"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        empDict = {emp.id: emp for emp in employees}

        def dfs(id):
            totImportance = 0
            for subordinate in empDict[id].subordinates:
                totImportance += dfs(subordinate)
            
            totImportance += empDict[id].importance
            return totImportance

        return dfs(id)

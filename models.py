from helpers import today

#Task class
class Task:
    def __init__(self, id, description, status = "not_done", createdAt = None, updatedAt = None):
        self.id = id
        self.description = description
        self.status = status

        now = today()

        self.createdAt = createdAt if createdAt else now
        self.updatedAt = updatedAt if updatedAt else now
    #toDict method to make object json friendly
    def toDict(self):
        return self.__dict__
    #str for list function
    def __str__(self):
        main = f"TASK: {self.description}\nID: {self.id}\nSTATUS: {self.status}\nCREATED_AT: {self.createdAt}"
        addition = f"\nUPDATED_AT: {self.updatedAt}" if self.updatedAt != self.createdAt else ""

        return main + addition
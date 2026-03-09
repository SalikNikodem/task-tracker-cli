from helpers import today


class Task:
    def __init__(self, id, description, status = "not_done", createdAt = None, updatedAt = None):
        self.id = id
        self.description = description
        self.status = status

        now = today()

        self.createdAt = createdAt if createdAt else now
        self.updatedAt = updatedAt if updatedAt else now

    def toDict(self):
        return self.__dict__

    def __str__(self):
        main = f"TASK: {self.description}\nID: {self.id}\nSTATUS: {self.status}\nCREATED_AT: {self.createdAt}"
        addition = f"\nUPDATED_AT: {self.updatedAt}" if self.updatedAt != self.createdAt else ""

        return main + addition
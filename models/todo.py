from models.todoCreate import TodoCreate


class Todo(TodoCreate):
    id: int
    completed: bool = False
from fastapi import HTTPException
from services.todo_service import TodoService, TodoCreate, Todo

class TodoController:
    def __init__(self):
        self.todo_service = TodoService()

    def create_todo(self, todo: TodoCreate):
        return self.todo_service.create_todo(todo)

    def get_todos(self):
        return self.todo_service.get_todos()

    def get_todo(self, todo_id: int):
        todo = self.todo_service.get_todo(todo_id)
        if todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        return todo

    def update_todo(self, todo_id: int, updated_todo: TodoCreate):
        todo = self.todo_service.update_todo(todo_id, updated_todo)
        if todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        return todo

    def delete_todo(self, todo_id: int):
        if self.todo_service.delete_todo(todo_id):
            return {"message": "Todo deleted successfully"}
        raise HTTPException(status_code=404, detail="Todo not found")
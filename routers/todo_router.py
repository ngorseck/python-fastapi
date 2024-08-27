from fastapi import APIRouter
from controllers.todo_controller import TodoController, TodoCreate, Todo

router = APIRouter()
todo_controller = TodoController()

@router.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    return todo_controller.create_todo(todo)

@router.get("/todos", response_model=list[Todo])
def get_todos():
    return todo_controller.get_todos()

@router.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    return todo_controller.get_todo(todo_id)

@router.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoCreate):
    return todo_controller.update_todo(todo_id, updated_todo)

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    return todo_controller.delete_todo(todo_id)

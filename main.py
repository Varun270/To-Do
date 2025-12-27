from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.database import init_db
from app.schemas import TaskCreate
from app.crud import create_task, get_tasks
from app.logging_config import logger

app = FastAPI(title="To-Do API")

templates = Jinja2Templates(directory="app/templates")

@app.on_event("startup")
def startup():
    init_db()
    logger.info("Database initialized")


@app.post("/api/tasks", response_model=dict)
def add_task(task: TaskCreate):
    try:
        task_id = create_task(task)
        return {"message": "Task created", "task_id": task_id}
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=500, detail="Task creation failed")

@app.get("/api/tasks", response_model=list[dict])
def list_tasks():
    tasks = get_tasks()
    return [dict(task) for task in tasks]

@app.get("/", response_class=HTMLResponse)
def view_tasks(request: Request):
    tasks = get_tasks()
    return templates.TemplateResponse(
        "tasks.html",
        {"request": request, "tasks": tasks}
    )

@app.get("/add", response_class=HTMLResponse)
def add_task_page(request: Request):
    return templates.TemplateResponse("add_task.html", {"request": request})

@app.post("/add")
async def add_task_form(request: Request):
    form = await request.form()
    task = TaskCreate(
        title=form["title"],
        description=form.get("description"),
        due_date=form.get("due_date"),
        status=form.get("status", "pending")
    )
    create_task(task)
    return RedirectResponse("/", status_code=303)


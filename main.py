from fastapi import FastAPI

app = FastAPI(
    title='{{cookiecutter.project_title}}',
    version='{{cookiecutter.project_version}}',
    description='{{cookiecutter.project_description}}'
)


@app.get("/")
async def root():
    return {"message": "Hello {{cookiecutter.service_name}}"}

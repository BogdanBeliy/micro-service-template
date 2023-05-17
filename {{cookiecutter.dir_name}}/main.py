import traceback
from urllib.request import Request

from fastapi import FastAPI
from starlette import status
from starlette.responses import JSONResponse

app = FastAPI(
    title='{{cookiecutter.project_title}}',
    version='{{cookiecutter.project_version}}',
    description='{{cookiecutter.project_description}}'
)

@app.exception_handler(status.HTTP_500_INTERNAL_SERVER_ERROR)
async def private_exception_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    log = Logger("API - PRIVATE EXCEPTION")
    log.error(message=traceback.format_exc())
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"error": "internalServerError"},
    )


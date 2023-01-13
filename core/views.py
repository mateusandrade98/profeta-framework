from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from jinja2 import Template
from typing import Dict
from aiofile import async_open

router = APIRouter()


# render template
async def render(template: str, data: Dict) -> HTMLResponse:
    async with async_open('templates/%s.html' % template) as file_:
        HTML = Template(await file_.read())
        await file_.close()
    return HTMLResponse(HTML.render(data))


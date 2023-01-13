from fastapi import APIRouter
from fastapi.responses import Response, HTMLResponse
from core.config import settings
from os.path import isfile
from aiofile import async_open
import magic

routeStatic = APIRouter()


@routeStatic.get('/%s/{filename}' % settings.PUBLIC_FOLDER)
async def file(filename: str) -> Response:
    _path = '%s/%s' % (settings.PUBLIC_FOLDER, filename)

    # file not found
    if not isfile(_path):
        return HTMLResponse(content='file not found.', status_code=404)

    # read and return file bytes
    async with async_open(_path, mode='rb') as _file:
        fileBytes = await _file.read()
        await _file.close()

    mime = magic.Magic(mime=True)
    return Response(content=fileBytes, status_code=200, media_type=mime.from_file(_path))

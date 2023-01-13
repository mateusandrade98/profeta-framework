from core.views import router, render


@router.get('/')
async def index():
    data = {}
    return await render('login', data)



from starlette.responses import Response, JSONResponse


async def home(request):
    return JSONResponse({'hello': 'world'})

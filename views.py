from starlette.responses import Response, UJSONResponse as JSONResponse


async def home(request):
    return JSONResponse({'hello': 'world'})

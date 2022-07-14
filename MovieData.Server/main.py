
from fastapi import FastAPI
from py import code #import class FastAPI() từ thư viện fastapi
from map import actor, data_map, get_film, histo_chart, line_chart, pie_process, type_pie, pyramid_chart, heat_chart, processHeat
app = FastAPI() # gọi constructor và gán vào biến app


@app.get("/api/map") # giống flask, khai báo phương thức get và url
async def root(): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    data = data_map()
    print(data)
    return {'data':data}


# trả về 20 film phổ biến nhất của quốc gia đó + 20 film phổ biến nhất trên toàn thế giới
@app.get("/api/film/{code}") # giống flask, khai báo phương thức get và url
async def root(code: str): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    if len(code) > 4:
        return {'data': ''}
    else:
        data = get_film(code.upper())
        return {'data':data}

@app.get("/api/chart/pie/{code}") # giống flask, khai báo phương thức get và url
async def root(code: str): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    if len(code) > 4:
        return {'data': ''}
    else:
        data = type_pie(code.upper())
        return {'data':data}

@app.get("/api/chart/line/{code}") # giống flask, khai báo phương thức get và url
async def root(code: str): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    if len(code) > 4:
        return {'data': ''}
    else:
        data = line_chart(code.upper())
        return {'data':data}
@app.get("/api/chart/histo/{code}") # giống flask, khai báo phương thức get và url
async def root(code: str): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    if len(code) > 4:
        return {'data': ''}
    else:
        data = histo_chart(code.upper())
        return data
@app.get("/api/chart/pyramid/{code}") # giống flask, khai báo phương thức get và url
async def root(code: str): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    if len(code) > 4:
        return {'data': ''}
    else:
        data = pyramid_chart(code.upper())
        return data
@app.get("/api/chart/heat/{code}") # giống flask, khai báo phương thức get và url
async def root(code: str): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    if len(code) > 4:
        return {'data': ''}
    else:
        data = processHeat(heat_chart(code.upper()), code.upper())
        return data
@app.get("/api/chart/table/{code}") # giống flask, khai báo phương thức get và url
async def root(code: str): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    if len(code) > 4:
        return {'data': ''}
    else:
        data = pie_process(code.upper())
        return data
@app.get("/api/table/actor/{code}") # giống flask, khai báo phương thức get và url
async def root(code: str): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    if len(code) > 4:
        return {'data': ''}
    else:
        data = actor(code.upper())
        return data
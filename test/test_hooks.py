from .decorix_test import app

app.b().register(test=lambda: print("=====start====="))
app.a().register(test=lambda resulte: print(resulte))
app.f().register(test=lambda: print("=====end====="))

app.b().register(test2=lambda: print("=====start2====="))
app.a().register(test2=lambda resulte: print(resulte))
app.f().register(test2=lambda: print("=====end2====="))

app.h().register(test=lambda error, message, traceback , exception: print(f"""
    {error}:{message}
    traceback:{traceback}
    model:{exception}
"""))

app.h().register(test2=lambda error, message, traceback , exception: print(f"""
    {error}     :{message}
    traceback   :{traceback}
    model       :{exception}
"""))

@app.h().handler("test")
def handler():
    print(12+"=====handl the type error=====")

@app.h().handler("test2")
def handler2():
    print(12+"=====handl the type error=====")

@app.b().before("test")
@app.a().after("test")
@app.f()._finally("test")
def worker():
    print("=====working=====")
    return "=====working is ready====="

@app.b().before("test2")
@app.a().after("test2")
@app.f()._finally("test2")
def worker2():
    print("=====working=====")
    return "=====working is ready====="

handler2()
worker()
worker2()
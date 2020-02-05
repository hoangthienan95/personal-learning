https://fastapi.tiangolo.com/tutorial/intro/

**Concurrency** : `asynchronous` is being able to wait for a task to finish while doing something else. When that task is done, it can wait until the server has finished its current task to pick it up again

**Parallelism** is when you divide work to multiple workers. These workers can be `synchronous` (stuck waiting for a long task and do nothing else) or `asynchronous` (do other stuff while waiting).

Web usually needs async (alot of waiting for database/service etc) while ML training/inference needs parallelism (not alot of waiting, just alot of **CPU bound** work to be done). Combining them together is beneficial

**Order matters**

Fix paths before dynamic paths. Because path operations are evaluated in order, you need to make sure that the path for fixed paths like `/users/me` is declared before the one for `/users/{user_id}`, otherwise  the path for `/users/{user_id}` would match also for `/users/me`, "thinking" that it's receiving a parameter `user_id` with a value of `"me"`.
`
**Predefine sets of path values using Enums**

```python
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}
```

**Path parameters containing paths**

In order to capture a path like `/files/home/johndoe/myfile.txt` with `/files/{file_path}`, do:

```py
@app.get("/files/{file_path:path}")
async def read_user_me(file_path: str):
    return {"file_path": file_path}
```



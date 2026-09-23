from fastapi import FastAPI

app = FastAPI()

users = {
    1: {
        "name": "Praveen",
        "email": "praveen@gmail.com",
        "age": 22
    }
}


# GET API
@app.get("/")
def home():
    return {"message": "FastAPI is workingjkhbk!"}


# PATCH API
@app.patch("/users/{user_id}")
def update_user(user_id: int, data: dict):

    if user_id not in users:
        return {"message": "User not found"}

    users[user_id].update(data)

    return {
        "message": "User updated successfully",
        "user": users[user_id]
    }
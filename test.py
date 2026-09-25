# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get("https://www.google.com/search?q=pachai+payaru&sca_esv=b5ea7be7985888f6&biw=1920&bih=928&sxsrf=APpeQntH53vR_7BHqLoDDztptu7c4jB58g%3A1785227945907&ei=qWpoaoPtNoeeseMP2KTt0Ag&vsep=2&oq=double+occupancy&gs_lp=Egxnd3Mtd2l6LXNlcnAiEGRvdWJsZSBvY2N1cGFuY3lIAFAAWABwAHgBkAEAmAEAoAEAqgEAuAESyAEA-AEGmAIAoAIAmAMAkgcAoAcAsgcAuAcAwgcAyAcAgAgB&sclient=gws-wiz-serp&gs_ivs=1")

# # Scroll code
# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     import time
#     time.sleep(10)
   
#     new_height = driver.execute_script("return document.body.scrollHeight")

#     if new_height == last_height:
#       continue

#     last_height = new_height


  #################################################
# import pyautogui
# import time

# time.sleep(3)

# pyautogui.keyDown('ctrl')
# time.sleep(0.2)
# pyautogui.press('end')
# time.sleep(0.2)
# pyautogui.keyUp('ctrl')


# import pyautogui
# import time

# time.sleep(5)

# for _ in range(20):
#     pyautogui.press('end')
#     time.sleep(0.1)
# import time
# time.sleep(2)
# def process_patient():
#     print("===== Patient Processing Started =====")

#     # Step 1: Get patient details
#     patient_name = get_patient_name()
#     patient_age = get_patient_age()

#     print("Patient Name:", patient_name)
#     print("Patient Age:", patient_age)

#     # Step 2: Validate patient
#     is_valid = validate_patient(patient_name, patient_age)

#     if is_valid:
#         print("Patient validation successful")

#         # Step 3: Calculate amount
#         amount = calculate_amount(patient_age)

#         # Step 4: Save patient
#         save_patient(patient_name, patient_age, amount)

#         # Step 5: Send notification
#         send_notification(patient_name)

#     else:
#         print("Patient validation failed")

#     print("===== Patient Processing Completed =====")


# def get_patient_name():
#     return "John"


# def get_patient_age():
#     return 25


# def validate_patient(name, age):
#     if name != "" and age > 0:
#         return True

#     return False


# def calculate_amount(age):
#     if age < 18:
#         amount = 100
#     else:
#         amount = 500

#     return amount


# def save_patient(name, age, amount):
#     print("Saving patient...")
#     print("Name:", name)
#     print("Age:", age)
#     print("Amount:", amount)


# def send_notification(name):
#     print("Notification sent to:", name)


# # Starting the complete process
# process_patient()


# from fastapi import FastAPI

# app = FastAPI()

# users = {
#     1: {
#         "name": "Praveen",
#         "email": "praveen@gmail.com",
#         "age": 22
#     }
# }


# @app.patch("/users/{user_id}")
# def update_user(user_id: int, data: dict):

#     if user_id not in users:
#         return {"message": "User not found"}

#     # Update only the fields sent by the client
#     users[user_id].update(data)

#     return {
#         "message": "User updated successfully",
#         "user": users[user_id]
#     }
# def decorator(func):

#     def wrapper():
#         print("Before function execution")
#         func()
#         print("After function execution")

#     return wrapper


# @decorator
# def display():
#     print("Display function execution")


# display().
#######################################################################################

# numbers=[15,83,73,88]
# largest_number=0
# for number in numbers:
#     if number>largest_number:
#         largest_number=number
# print(largest_number)
#######################################################################################

# numbers = [89, 83, 73, 88]

# largest = numbers[0]
# second_largest = numbers[0]

# for number in numbers:
#     if number > largest:
#         second_largest = largest
#         largest = number
#     elif number > second_largest and number != largest:
#         second_largest = number

# print("Largest:", largest)
# print("Second largest:", second_largest)



# import threading
# import time

# def task1():
#     for i in range(5):
#         print("Task 1")
#         time.sleep(1)

# def task2():
#     for i in range(5):
#         print("Task 2")
#         time.sleep(1)

# t1 = threading.Thread(target=task1)
# t2 = threading.Thread(target=task2)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("Both tasks completed")


import threading 
import time

#from matplotlib.pylab import rint 

def task1():
    for i in range(5):
        print("task 1")
        time.sleep(1)

def task2():
    for i in range(5):
        print("task 2")
        time.sleep(1)

t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()
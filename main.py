# contn = True
# print("Welcome to the Calculator")
# while contn:
#     # getting user input, not safe, if you don't input number/float, it will crash
#     num1 = float(input("Please write the first number: "))
#     num2 = float (input("Please write the second number: "))
#     contn2 = True
#
#     while contn2:
#         contn2 = False
#         operation = input("Choose an operation: 1 is for +, 2 is for -, 3 is for *, 4 is for /: ")
#         if operation == "1":
#             result = num1 + num2
#         elif operation == "2":
#             result = num1 - num2
#         elif operation == "3":
#             result = num1 * num2
#         elif operation == "4":
#             if num2 != 0:
#                 result = num1 / num2
#             else:
#                 result = "Cannot divide by zero!"
#         else:
#             result = "Unknown option."
#             contn2 = True
#
#     print(result)
#     notAdded = True
#     while notAdded:
#         again = input("Do you want to continue? A / N: ")
#         if again.lower() == "a":
#             contn = True
#             notAdded = False
#         elif again.lower() == "n":
#             contn = False
#             notAdded = False
#         else:
#             notAdded = True
#
#
import logging

FORMAT = '%(asctime)s %(levelname)s %(message)s'

logging.basicConfig(
    filemode="a",
    filename="export.log",
    format=FORMAT,
    level=logging.INFO
)
logging.warning("Ahoj")
logging.info("info")
logging.fatal("fatal")

logging.info("Write info")

try:
    1/0
except ZeroDivisionError as e:
    logging.error("Cannot divide by zero!", exc_info=True)

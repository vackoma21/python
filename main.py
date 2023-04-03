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
    filemode="w",
    filename="export.log",
    format=FORMAT,
    level=logging.INFO
)

logger = logging.getLogger(__name__)
# different name for each module
handler = logging.FileHandler("test.log")
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("geh")
# logging.warning("Ahoj")
# logging.info("info")
# logging.fatal("fatal")
#
# logging.info("Write info")
#
try:
    with open("file.txt") as file:
        date = file.read()
    # 1/0
except Exception as e:
    logger.error("Cannot divide by zero!", exc_info=True)

# except ZeroDivisionError as e

try:
    x = int(input("A: "))
    y = int(input("B: "))
    print(x/y)
except ValueError as e:
    print("Not a number")
    logger.error("Not a number", exc_info=True)
except ZeroDivisionError as e:
    logger.error("Zero division", exc_info=True)
except:
    logger.error("Error", exc_info=True)

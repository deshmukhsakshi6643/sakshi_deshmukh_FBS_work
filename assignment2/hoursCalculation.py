second = int(input("Enter seconds:"))

hours = second // 3600
second = second % 3600
min = second // 60
second = second % 60
print(f'Hours:{hours} , Min:{min} , Second:{second}')
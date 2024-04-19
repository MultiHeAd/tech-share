import sys

if len(sys.argv) > 1:
    command = sys.argv[1]
    if command == "greet":
        name = sys.argv[2] if len(sys.argv) > 2 else "World"
        print(f"Hello, {name}!")
    elif command == "sum":
        numbers = map(int, sys.argv[2:])
        print(f"The sum is: {sum(numbers)}")
    else:
        print("Unknown command")
else:
    print("No command provided")

# python sys.argv.py greet John
# python sys.argv.py sum 1 2 3

# git测试，修改内容

"""
内部传参版本：
def process_command(command, *args):
    if command == "greet":
        name = args[0] if args else "World"
        print(f"Hello, {name}!")
    elif command == "sum":
        numbers = map(int, args)
        print(f"The sum is: {sum(numbers)}")
    else:
        print("Unknown command")

# 直接调用函数，传递参数
process_command('greet', 'Alice')
process_command('sum', '1', '2', '3')
process_command('greet')

"""

# print(sys.version)
# print(sys.platform)
# import copy
# v1=[[1],1,2]
# v2=copy.deepcopy(v1)
# print(id(v1[0]))
# print(id(v2[0]))

# print([x for x in range(1, 101) if x % 2 == 0])

# def num():
#     return [lambda x:i*x for i in range(4)]
#
# result = [m(2) for m in num()]
# print(result)

# dict ={}
# dict['name']=123
# data=dict.items()
# print(data)


# v1=[1,2,3]
# start,*end=v1
# print(f"start={start}\nend={end}")


content = input('请输入值: ')

result = 1
num_list = content.split('*')
for num_str in num_list:
    try:
        num = int(num_str)  # 尝试将字符串转换为整数
        result *= num
    except ValueError:  # 如果转换失败，捕获异常
        print(f"输入数据有误: {num_str}")
        break  # 跳出循环

# 如果循环正常结束，则打印结果
else:
    print(result)
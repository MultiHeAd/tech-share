import re

# text = "123豆6豆东渡"
# data = re.search("豆\d豆",text)
# if data:
#     print(data.group())
#



# text = "单词123 单词123"
# pattern = r'(单词\d+)\s\1'  # \1 引用第一个捕获组的内容
# match = re.search(pattern, text)
# if match:
#     print(match.group())  # 输出: 单词123 单词123



# text = "island is beautiful"
# match = re.findall(r'\bis\b', text)
# print(match)  # 输出: ['is']，不匹配 "island" 中的 "is"


dict = {
    1:"苹果",
    2:"西瓜",
    3:"香蕉",
}

res = ";".join(["{}.{}".format(k,v) for k,v in dict.items()])
print(res)
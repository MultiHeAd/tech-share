"""
启动服务端：redis-server.exe redis.windows.conf
启动客户端：redis-cli.exe
"""

"""
数据类型
"""

"""
keys * 
查找全数据

1.string
设置键值,不存在是添加，存在是修改
set key value

查找值
get key 

设置键值和过期时间，以秒为单位
setex key seconds value

设置多个值,如果值是一串内容，比如"hello world"则需要加引号，否则则不用
mset a1 python a2 java a3 go

往对应值后面增加内容 append
append a1 haha

取多个值
mget a1 a2 a3

"""



"""
补充（键命令）
支持正则表达
keys pattern

判断键是否存在
exists keys

设置过期时间
expire key seconds   expire a1 3

查看剩余有效时间
ttl key
"""


"""
2.hash type
设置一个键值对的值属性
hset key field value


同理多个值属性
hmset key1 field1 value1 fields value2...

获取属性的值 field就是属性，同样也支持加上m格式，一次拿多个值 hmget(hmget user2 name age)
hget keys field

返回hash类下全部的值
hvals keys (hvals user2)

删除部分属性
hedl key field1 field2

查看属性
hkeys key
"""


"""
3.list
列表元素类型是str

插入数据“前后左右”
lpush key value1 value2

查看列表的元素  start 和 end是索引
lrange key start end

设置索引元素值
lset key index value

"""

"""
4.set & zset

set:
往集合里添加元素，没有顺序
sadd key member1 member2 member3

查看所有元素
smembers key

删除元素
srem key member1 member2 member3


zset:
sorted set , 有序集合
元素为string类型

"""


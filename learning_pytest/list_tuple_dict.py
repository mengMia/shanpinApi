def get_info():
    name = "ET"
    age = 20
    # 返回的是元组
    # return name, age

    # 返回的是list
    # return [name, age]

    #返回的是dict
    return {name: age}
if __name__ == '__main__':
    result = get_info()
    # print(result['ET'])
# todo: 元组
# todo: 创建一个tuple
# tuple_t = ()
# print(type(tuple_t))
# print(tuple_t)
#

# todo: 访问tuple
# tuple_t1 = (1, 2, 5, 7, 9)
# # 取tuple_t1中的元素
# print(tuple_t1[0])
# print(type(tuple_t1[0]))
# #取tuple_t1中的部分片段，结果还是一个元组
# print(tuple_t1[0:1])
# print(type(tuple_t1[0:1]))
#
# print(tuple_t1[0 : 4])
#

# todo: 更新tuple
# # 更新元组中的元素，直接添加肯定是不行，通过切片拼接
# animals = ("龙猫", "泰迪", "叮当喵")
# animals = animals[:2] + ("小猪佩奇",) + animals[2:]
# print(animals)

# todo: 删除tuple
# # 删除元组中的元素，直接删除也不行，通过切片拼接实现
# animals = ("龙猫", "泰迪", "叮当喵")
# animals = animals[:1] + animals[2:]
# print(animals)

# todo：使用in 和 not in
# animals = ("龙猫", "泰迪", "小猪佩奇", "叮当喵")
# longmao = "龙猫"
# taidi_xiaozhu = ("泰迪", "小猪佩奇")
# longmao_in = longmao in animals
# taidi_xiaozhu_in = taidi_xiaozhu in animals
# print(longmao_in)
# print(taidi_xiaozhu_in)
#
#
# animals2 = ("龙猫", ("泰迪", "小猪佩奇"), "叮当喵")
# taidi_xiaozhu_in = taidi_xiaozhu in animals2
# print(taidi_xiaozhu_in)

# todo: list和tuple组合
# tuple_list = ([1, 2, 3], ["apple", "orange", "banana"])
# print(type(tuple_list))
# print(tuple_list)
# # tuple_list[0] = [4, 5] 报错
# tuple_list[0][0] = 3
# print(tuple_list)



# todo: 列表
# a = [1,2, 3]
# a.append(3)
# print(a)
# a.append([3, 5])
# print(a)
# a.extend([3, 5])
# print(a)
# a.insert(2, "hi")
# print(a)

# a = 2
# print(id(a))
# a = 3
# print(id(a))



# todo: 字典


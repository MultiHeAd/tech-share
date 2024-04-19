# class solution():
#     def __init__(self,content):
#         self.data = content
#
# sol = solution(123)
# print(sol.data)


class Police():
    def __init__(self,name,role):
        self.name = name
        self.role = role
        if self.role == "队员":
            self.hit_points = 200
        else:
            self.hit_points = 500

    def show_status(self):
        message = "警察{}的剩余生命值为：{}".format(self.name,self.hit_points)
        print(message)

    def bomb(self,terrorist_list):
        for terrorist in terrorist_list:
            terrorist.blood -= 200
            terrorist.show_status()



class Terrorist:
    def __init__(self,name,blood=300):
        self.name = name
        self.blood = blood


    def shoot(self,police_object):
        police_object.hit_points -= 5
        police_object.show_status()

    def strafe(self,police_object_list):
        for police_object in police_object_list:
            police_object.hit_points -= 8
            police_object.show_status()

    def show_status(self):
        msg = "恐怖分子{}的剩余生命值为：{}".format(self.name,self.blood)
        print(msg)


def run():
    p1 = Police("佩奇","队员")
    p2 = Police("涛涛","队长")
    t1 = Terrorist("alex")
    t2 = Terrorist("佩小奇")


    t1.shoot(p1)
    t1.strafe([p1,p2])
    t2.shoot(p2)
    p1.bomb([t1,t2])
    p1.bomb([t1])


run()

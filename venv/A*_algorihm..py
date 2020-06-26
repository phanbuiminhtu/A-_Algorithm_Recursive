import sys, math
from multiprocessing import Process
import time

class Square:
    def __init__(self, distance, x, y, status="non-block", check=False):
        self.status = status
        self.distance = distance
        self.x = x
        self.y = y
        self.prev = []
        self.next = []
        self.check = check

    def setnext(self, other):
        if other.status == "non-block":
            self.next.append(other)

    def setprev(self, other):
        if other.distance - self.distance == 1 and other.check is False and other.status is "non-block":
            self.prev = other

    def setcheck(self, check):
        self.check = check

    def setstatus(self, status):
        self.status = status

    def getdistance(self):
        return self.distance


main_list = []


def find_path(x_ori, y_ori, x_goal, y_goal, obstacle):
    start = time.time()
    tempo_list = []
    shortest_dis = max(abs(x_ori - x_goal), abs(y_ori - y_goal))

    block22 = Square(shortest_dis, x_ori, y_ori, check=True)
    print("block22:", block22.x, block22.y)

    block11 = Square(max(abs((x_ori - 1) - x_goal), abs((y_ori + 1) - y_goal)), x_ori - 1, y_ori + 1)
    block12 = Square(max(abs(x_ori - x_goal), abs((y_ori + 1) - y_goal)), x_ori, y_ori + 1)
    block13 = Square(max(abs((x_ori + 1) - x_goal), abs((y_ori + 1) - y_goal)), x_ori + 1, y_ori + 1)

    block21 = Square(max(abs((x_ori - 1) - x_goal), abs(y_ori - y_goal)), x_ori - 1, y_ori)
    block23 = Square(max(abs((x_ori + 1) - x_goal), abs(y_ori - y_goal)), x_ori + 1, y_ori)

    block31 = Square(max(abs((x_ori - 1) - x_goal), abs((y_ori - 1) - y_goal)), x_ori - 1, y_ori - 1)
    block32 = Square(max(abs(x_ori - x_goal), abs((y_ori - 1) - y_goal)), x_ori, y_ori - 1)
    block33 = Square(max(abs((x_ori + 1) - x_goal), abs((y_ori - 1) - y_goal)), x_ori + 1, y_ori - 1)

    tempo_list.extend([block33, block32, block11, block31, block23, block21, block12, block13])
    tempo_list = [elem for elem in tempo_list if elem.x >= 0 and elem.y >= 0]  # remove negative coordinate

    print("before remove:", len(tempo_list))

    for item in main_list:
        for elem in tempo_list:
            if elem.x == item.x and elem.y == item.y:
                tempo_list.remove(elem)
    for item in main_list:
        for elem in tempo_list:
            if elem.x == item.x and elem.y == item.y:
                tempo_list.remove(elem)
    print("after remove:", len(tempo_list))
    print("")
    main_list.append(block22)
    # check obstacle
    for ele in tempo_list:
        if ele.x == x_goal and ele.y == y_goal:
            return 1
        for obs in obstacle:
            if ele.x == obs.x and ele.y == obs.y:
                tempo_list.remove(ele)
    for ele in tempo_list:
        if ele.x == x_goal and ele.y == y_goal:
            return 1
        for obs in obstacle:
            if ele.x == obs.x and ele.y == obs.y:
                tempo_list.remove(ele)
    # print item in tempo_list
  #  for item in tempo_list:
   #     print("debug in tempo:", item.x, item.y)

    for elem in tempo_list:
        if elem.getdistance() < shortest_dis:
            block22.setnext(elem)
    if not block22.next:
        for elem in tempo_list:
            if elem.distance == block22.distance and elem.check == False:
                block22.setnext(elem)

    if not block22.next:
        for elem in tempo_list:
            if elem.distance - block22.distance == 1 and elem.check == False:
                block22.setnext(elem)

    for block in block22.next:
        if block.check == False:
            end = time.time()
            print("time executed:",end-start)
            time.sleep(end - start)
            thread = Process(target=find_path, args=(block.x, block.y, x_goal, y_goal, obstacle,))

            thread.start()

if __name__ == "__main__":
    ob = [Square(4, 4, 0, "block"), Square(4, 4, 1, "block"), Square(4, 4, 2, "block"), Square(4, 4, 3, "block")]
    find_path(0, 1, 7, 0, ob)
    for i in main_list:
        print(i.x, i.y)

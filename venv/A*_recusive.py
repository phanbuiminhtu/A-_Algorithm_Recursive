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

record_list = []
def add_block(x_ori, y_ori, x_goal, y_goal, obstacle,main_list):
    tempo_list = []
    shortest_dis = max(abs(x_ori - x_goal), abs(y_ori - y_goal))

    block22 = Square(shortest_dis, x_ori, y_ori, check=True)  # current block
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

   # print("before remove:", len(main_list))

    for item in record_list:
        for elem in tempo_list:
            if elem.x == item.x and elem.y == item.y:
                tempo_list.remove(elem)
    for item in record_list:
        for elem in tempo_list:
            if elem.x == item.x and elem.y == item.y:
                tempo_list.remove(elem)


    # check obstacle to remove from tempo list
    for ele in tempo_list:
        for obs in obstacle:
            if ele.x == obs.x and ele.y == obs.y:
                tempo_list.remove(ele)
    for elem in tempo_list:
        for obs in obstacle:
            if elem.x == obs.x and elem.y == obs.y:
                tempo_list.remove(elem)

    # add element closer to goal to main list and "next list" of block22
    for elem in tempo_list:
        if elem.getdistance() < shortest_dis or elem.getdistance()==1 or elem.getdistance()==0:
            block22.setnext(elem)
            main_list.append(elem)
            record_list.append(elem)
    for elem in block22.next:
        print("block in block22.next:",elem.x,elem.y)
    # tell the function to go along the obstacle
    if not block22.next:
        for elem in tempo_list:
            if elem.distance == block22.distance and elem not in record_list:
                print("block being added when dis == 0:",elem.x,elem.y)
                block22.setnext(elem)
                main_list.append(elem)
                record_list.append(elem)
    if not block22.next:
        for elem in tempo_list:
            if elem.distance - block22.distance == 1 and elem not in record_list:
                print("block being added when dis == 1:", elem.x, elem.y)
                block22.setnext(elem)
                main_list.append(elem)
                record_list.append(elem)
    print("")
    return main_list

def find_path(x_ori, y_ori, x_goal, y_goal, obstacle,main_list):
    #check if two point are overlap
    print("X ori, Y ori:", x_ori, y_ori)
    if x_ori == x_goal and y_ori == y_goal:
        print("what's up!")
        return record_list

    #check if goal block is in record list
    for block in record_list:
        #print("debbug:",block.x,block.y)
        if block.x == x_goal and block.y == y_goal:
            print("what's upppppppppp!!!!!!!!!!!!!!!!")
            return record_list
    if not main_list:
        block_list= add_block(x_ori, y_ori, x_goal, y_goal, obstacle,main_list)
        block_list2 = block_list[:]
    else:
        block_list2 = main_list[:]
   # print("length of main list:",len(main_list))
    for item in main_list:
        add_block(item.x, item.y, x_goal, y_goal, obstacle,block_list2)
    block_list2 = [x for x in block_list2 if x not in main_list]
    print("length of block list 2 after slice:",len(block_list2))
    for item in block_list2:
        return find_path(item.x,item.y,x_goal,y_goal,obstacle,block_list2)

if __name__ == "__main__":
    ob = [Square(4, 4, 0, "block"), Square(4, 4, 1, "block"), Square(4, 4, 2, "block"), Square(4, 4, 3, "block")]
    main_list = []
    x = find_path(1, 7, 10, 7, ob,main_list)
    print("length of record list:",len(record_list))
    for i in x:
        print("blocks in record:",i.x,i.y)

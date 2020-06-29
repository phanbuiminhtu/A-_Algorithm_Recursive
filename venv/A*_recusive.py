import sys, math

class Square:
    def __init__(self, x, y, distance, status="non-block", check=False):
        self.status = status
        self.distance = distance
        self.x = x
        self.y = y
        self.prev = None
        self.next = []
        self.check = check

    def setnext(self, other):
        if other.status == "non-block":
            self.next.append(other)

    def setprev(self, other):
        self.prev = other

    def setcheck(self, check):
        self.check = check

    def setstatus(self, status):
        self.status = status

    def getdistance(self):
        return self.distance

record_list = []
path_list =[]
def add_block(x_ori, y_ori, x_goal, y_goal, obstacle,main_list):
    tempo_list = []
    shortest_dis = max(abs(x_ori - x_goal), abs(y_ori - y_goal))

    block22 = Square(x_ori, y_ori,shortest_dis, check=True)  # current block
    print("block22:", block22.x, block22.y)

    block11 = Square(x_ori - 1, y_ori + 1, max(abs((x_ori - 1) - x_goal), abs((y_ori + 1) - y_goal)))
    block12 = Square(x_ori, y_ori + 1,max(abs(x_ori - x_goal), abs((y_ori + 1) - y_goal)))
    block13 = Square(x_ori + 1, y_ori + 1,max(abs((x_ori + 1) - x_goal), abs((y_ori + 1) - y_goal)))

    block21 = Square(x_ori - 1, y_ori,max(abs((x_ori - 1) - x_goal), abs(y_ori - y_goal)))
    block23 = Square(x_ori + 1, y_ori,max(abs((x_ori + 1) - x_goal), abs(y_ori - y_goal)))

    block31 = Square(x_ori - 1, y_ori - 1,max(abs((x_ori - 1) - x_goal), abs((y_ori - 1) - y_goal)))
    block32 = Square(x_ori, y_ori - 1,max(abs(x_ori - x_goal), abs((y_ori - 1) - y_goal)))
    block33 = Square(x_ori + 1, y_ori - 1,max(abs((x_ori + 1) - x_goal), abs((y_ori - 1) - y_goal)))

    tempo_list.extend([block33, block32, block11, block31, block23, block21, block12, block13])
    tempo_list = [elem for elem in tempo_list if elem.x >= 0 and elem.y >= 0]  # remove negative coordinate

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
            elem.setprev(block22)
            path_list.append(elem)
            main_list.append(elem)
            record_list.append(elem)
    '''
    for elem in block22.next:
        print("block in block22.next:",elem.x,elem.y)
    '''
    # tell the function to go along the obstacle
    if not block22.next:
        for elem in tempo_list:
            if elem.distance == block22.distance and elem not in record_list:
                #print("block being added when dis == 0:",elem.x,elem.y)
                block22.setnext(elem)
                main_list.append(elem)
                record_list.append(elem)
    if not block22.next:
        for elem in tempo_list:
            if elem.distance - block22.distance == 1 and elem not in record_list:
                #print("block being added when dis == 1:", elem.x, elem.y)
                block22.setnext(elem)
                main_list.append(elem)
                record_list.append(elem)
    print("")
    return main_list

def find_path(x_ori, y_ori, x_goal, y_goal, obstacle, main_list):
    #check if two point are overlap
    print("X ori, Y ori:", x_ori, y_ori)
    print("block to find",x_goal,y_goal)
    if x_ori == x_goal and y_ori == y_goal:
        print("what's up!")
        return record_list

    #check if goal block is in record list
    for block in record_list:
        if block.x == x_goal and block.y == y_goal:
            print("what's upppppppppp!!!!!!!!!!!!!!!!")
            return record_list
    if not main_list:
        block_list= add_block(x_ori, y_ori, x_goal, y_goal, obstacle,main_list)
        block_list2 = block_list[:]
    else:
        block_list2 = main_list[:]
    for item in main_list:
        add_block(item.x, item.y, x_goal, y_goal, obstacle,block_list2)
    block_list2 = [x for x in block_list2 if x not in main_list]
    for item in block_list2:
        return find_path(item.x,item.y,x_goal,y_goal,obstacle,block_list2)

path_list1 = []
def show_path(x_ori,y_ori,x_goal,y_goal,path):
   #print("x goal, y goal:",x_goal,y_goal)
    if x_ori == x_goal and y_ori == y_goal:
        return path_list1
    for block in path:
        goal_block = block
        if goal_block.x == x_goal and goal_block.y == y_goal:
          #  print("current block:", x_goal, y_goal)
            path_list1.append(goal_block)
            break
    '''
    print("current block on check:",goal_block.x,goal_block.y)
    print("previuos block:",goal_block.prev.x,goal_block.prev.y)
    print("path list before change:", len(path_list))
    print("")
    '''
    if goal_block.x != x_goal and goal_block.y != y_goal:
       # print("find the pivot")
        record_list.clear()
        find_path(x_ori,y_ori,x_goal,y_goal,ob,main_list)
       # print("path list after change:",len(path_list))
        return show_path(x_ori, y_ori,x_goal,y_goal, path)
    return show_path(x_ori,y_ori,goal_block.prev.x,goal_block.prev.y,path)

if __name__ == "__main__":
    ob = [Square(4, 0,4, "block"), Square(4, 1,4, "block"), Square(4, 2,4, "block"), Square(4, 3, 4, "block")]
    main_list = []
    x_ori = int(input("input your X origin:"))
    y_ori = int(input("input your y origin:"))
    x_goal = int(input("input your x goal:"))
    y_goal = int(input("input your y goal:"))
    block_record = find_path(x_ori,y_ori,x_goal,y_goal,ob,main_list)

    '''
    for i in path_list:
        print("blocks in path list:",i.x,i.y,"       previous block:",i.prev.x,i.prev.y)
    '''

    block_path = show_path(x_ori,y_ori,x_goal,y_goal,path_list)
    for i in path_list1:
        print("blocks in path list 1:",i.x,i.y,"       previous block:",i.prev.x,i.prev.y)


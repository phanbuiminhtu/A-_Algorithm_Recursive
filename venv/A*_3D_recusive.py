import sys, math

class Square:
    def __init__(self, x, y,z, distance):
        self.distance = distance
        self.x = x
        self.y = y
        self.z = z
        self.prev = None
        self.next = []

    def setnext(self, other):
        self.next.append(other)

    def setprev(self, other):
        self.prev = other

    def getdistance(self):
        return self.distance

record_list = []
path_list =[]
def add_block(x_ori, y_ori,z_ori, x_goal, y_goal,z_goal, obstacle,main_list):
    tempo_list = []
    shortest_dis = max(abs(x_ori - x_goal), abs(y_ori - y_goal),abs(z_ori - z_goal))

    block222 = Square(x_ori,y_ori,z_ori,shortest_dis)  # current block
    print("block222:", block222.x, block222.y,block222.z)

    block111 = Square(x_ori - 1, y_ori + 1,z_ori-1, max(abs((x_ori - 1) - x_goal), abs((y_ori + 1) - y_goal),abs((z_ori-1) - z_goal)))
    block121 = Square(x_ori, y_ori + 1,z_ori-1,max(abs(x_ori - x_goal), abs((y_ori + 1) - y_goal),abs((z_ori-1) - z_goal)))
    block131 = Square(x_ori + 1, y_ori + 1,z_ori-1,max(abs((x_ori + 1) - x_goal), abs((y_ori + 1) - y_goal),abs((z_ori-1) - z_goal)))
    block211 = Square(x_ori - 1, y_ori,z_ori-1,max(abs((x_ori - 1) - x_goal), abs(y_ori - y_goal),abs((z_ori-1) - z_goal)))
    block221 = Square(x_ori, y_ori,z_ori-1, max(abs((x_ori - 1) - x_goal), abs(y_ori - y_goal),abs((z_ori-1) - z_goal)))
    block231 = Square(x_ori + 1, y_ori,z_ori-1,max(abs((x_ori + 1) - x_goal), abs(y_ori - y_goal),abs((z_ori-1) - z_goal)))
    block311 = Square(x_ori - 1, y_ori - 1,z_ori-1,max(abs((x_ori - 1) - x_goal), abs((y_ori - 1) - y_goal),abs((z_ori-1) - z_goal)))
    block321 = Square(x_ori, y_ori - 1,z_ori-1,max(abs(x_ori - x_goal), abs((y_ori - 1) - y_goal),abs((z_ori-1) - z_goal)))
    block331 = Square(x_ori + 1, y_ori - 1,z_ori-1,max(abs((x_ori + 1) - x_goal), abs((y_ori - 1) - y_goal),abs((z_ori-1) - z_goal)))

    block112 = Square(x_ori - 1, y_ori + 1, z_ori,max(abs((x_ori - 1) - x_goal), abs((y_ori + 1) - y_goal), abs(z_ori - z_goal)))
    block122 = Square(x_ori, y_ori + 1, z_ori,max(abs(x_ori - x_goal), abs((y_ori + 1) - y_goal), abs(z_ori - z_goal)))
    block132 = Square(x_ori + 1, y_ori + 1, z_ori,max(abs((x_ori + 1) - x_goal), abs((y_ori + 1) - y_goal), abs(z_ori - z_goal)))
    block212 = Square(x_ori - 1, y_ori, z_ori,max(abs((x_ori - 1) - x_goal), abs(y_ori - y_goal), abs(z_ori - z_goal)))
    block232 = Square(x_ori + 1, y_ori, z_ori,max(abs((x_ori + 1) - x_goal), abs(y_ori - y_goal), abs(z_ori - z_goal)))
    block312 = Square(x_ori - 1, y_ori - 1, z_ori,max(abs((x_ori - 1) - x_goal), abs((y_ori - 1) - y_goal), abs(z_ori - z_goal)))
    block322 = Square(x_ori, y_ori - 1, z_ori,max(abs(x_ori - x_goal), abs((y_ori - 1) - y_goal), abs(z_ori - z_goal)))
    block332 = Square(x_ori + 1, y_ori - 1, z_ori - 1,max(abs((x_ori + 1) - x_goal), abs((y_ori - 1) - y_goal), abs(z_ori - z_goal)))

    block113 = Square(x_ori - 1, y_ori + 1, z_ori + 1,max(abs((x_ori - 1) - x_goal), abs((y_ori + 1) - y_goal), abs((z_ori + 1) - z_goal)))
    block123 = Square(x_ori, y_ori + 1, z_ori + 1,max(abs(x_ori - x_goal), abs((y_ori + 1) - y_goal), abs((z_ori + 1) - z_goal)))
    block133 = Square(x_ori + 1, y_ori + 1, z_ori + 1,max(abs((x_ori + 1) - x_goal), abs((y_ori + 1) - y_goal), abs((z_ori + 1) - z_goal)))
    block213 = Square(x_ori - 1, y_ori, z_ori + 1,max(abs((x_ori - 1) - x_goal), abs(y_ori - y_goal), abs((z_ori + 1) - z_goal)))
    block223 = Square(x_ori, y_ori, z_ori+1,max(abs((x_ori - 1) - x_goal), abs(y_ori - y_goal), abs((z_ori + 1) - z_goal)))
    block233 = Square(x_ori + 1, y_ori, z_ori + 1,max(abs((x_ori + 1) - x_goal), abs(y_ori - y_goal), abs((z_ori + 1) - z_goal)))
    block313 = Square(x_ori - 1, y_ori - 1, z_ori + 1,max(abs((x_ori - 1) - x_goal), abs((y_ori - 1) - y_goal), abs((z_ori + 1) - z_goal)))
    block323 = Square(x_ori, y_ori - 1, z_ori + 1,max(abs(x_ori - x_goal), abs((y_ori - 1) - y_goal), abs((z_ori + 1) - z_goal)))
    block333 = Square(x_ori + 1, y_ori - 1, z_ori + 1,max(abs((x_ori + 1) - x_goal), abs((y_ori - 1) - y_goal), abs((z_ori + 1) - z_goal)))

    tempo_list.extend([block331, block321, block111, block311, block231, block211, block121, block131, block221,block112,
                       block122,block132,block212,block232,block312,block322,block332,block113,block123,block133,block213,block223,block233,block313,block323,block333])
    tempo_list = [elem for elem in tempo_list if elem.x >= 0 and elem.y >= 0]  # Remove negative coordinate

    for item in record_list:
        for elem in tempo_list:
            if elem.x == item.x and elem.y == item.y and elem.z == item.z:
                tempo_list.remove(elem)
    for item in record_list:
        for elem in tempo_list:
            if elem.x == item.x and elem.y == item.y and elem.z == item.z:
                tempo_list.remove(elem)


    # Check obstacle to remove from tempo list
    for ele in tempo_list:
        for obs in obstacle:
            if ele.x == obs.x and ele.y == obs.y and ele.z == obs.z:
                tempo_list.remove(ele)
    for ele in tempo_list:
        for obs in obstacle:
            if ele.x == obs.x and ele.y == obs.y and ele.z == obs.z:
                tempo_list.remove(ele)
    for ele in tempo_list:
        for obs in obstacle:
            if ele.x == obs.x and ele.y == obs.y and ele.z == obs.z:
                tempo_list.remove(ele)

    # Add element closer to goal to main list and "next list" of block22
    for elem in tempo_list:
        if elem.getdistance() < shortest_dis or elem.getdistance()==1 or elem.getdistance()==0:
            block222.setnext(elem)
            elem.setprev(block222)
            path_list.append(elem)
            main_list.append(elem)
            record_list.append(elem)
    '''
    for elem in block222.next:                                      #debbug
        print("block in block222.next:",elem.x,elem.y,elem.z)      
    '''
    #tell the function to go along the obstacle
    if not block222.next:
        for elem in tempo_list:
            if elem.distance == block222.distance and elem not in record_list:
                #print("block being added when dis == 0:",elem.x,elem.y)     #debbug
                block222.setnext(elem)
                main_list.append(elem)
                record_list.append(elem)
    if not block222.next:
        for elem in tempo_list:
            if elem.distance - block222.distance == 1 and elem not in record_list:
                #print("block being added when dis == 1:", elem.x, elem.y)    #debbug
                block222.setnext(elem)
                main_list.append(elem)
                record_list.append(elem)
    print("")
    return main_list

def find_path(x_ori, y_ori,z_ori, x_goal, y_goal,z_goal, obstacle, main_list):
    #print("X ori, Y ori:", x_ori, y_ori)      #debbug
    #print("block to find",x_goal,y_goal)      #debbug

    # check if two point are overlap
    if x_ori == x_goal and y_ori == y_goal and z_ori == z_goal:
        print("what's up!")
        return record_list

    #check if goal block is in record list
    for block in record_list:
        if block.x == x_goal and block.y == y_goal and block.z == z_goal:
            print("what's upppppppppp!!!!!!!!!!!!!!!!")
            return record_list
    if not main_list:
        block_list= add_block(x_ori, y_ori,z_ori, x_goal, y_goal,z_goal, obstacle,main_list)
        block_list2 = block_list[:]
    else:
        block_list2 = main_list[:]
    for item in main_list:
        add_block(item.x, item.y,item.z, x_goal, y_goal,z_goal, obstacle,block_list2)
    block_list2 = [x for x in block_list2 if x not in main_list]
    '''
    for item in block_list2:                                            #debbug
        print("block in block list 2:",item.x,item.y)    
    '''
    for item in block_list2:
        #print("block being put in to find path:",item.x,item.y)        #debbug
        return find_path(item.x,item.y,item.z,x_goal,y_goal,z_goal,obstacle,block_list2)

path_list1 = []
def show_path(x_ori,y_ori,z_ori,x_goal,y_goal,z_goal,path):
    #print("x goal, y goal:",x_goal,y_goal)           #debbug
    if x_ori == x_goal and y_ori == y_goal and z_ori == z_goal:
        print("")
        print("Shortest path found!")
        return path_list1
    for block in path:
        goal_block = block
        if goal_block.x == x_goal and goal_block.y == y_goal and goal_block.z == z_goal:
          #print("current block:", x_goal, y_goal)   #debbug
            path_list1.append(goal_block)
            break
        if  goal_block.prev.x == x_goal and goal_block.prev.y == y_goal  and goal_block.prev.z == z_goal:
            path_list1.append(goal_block.prev)
            print("")
            print("Shortest path found!")
            return path_list1
    '''                                                                       
    print("current block on check:",goal_block.x,goal_block.y)               #debbug
    print("previuos block:",goal_block.prev.x,goal_block.prev.y)
    print("path list before change:", len(path_list))    
    print("")
    '''
    if goal_block.x != x_goal or goal_block.y != y_goal or goal_block.z != z_goal:
        print("find the pivot")
        record_list.clear()
        find_path(x_ori,y_ori,z_ori,x_goal,y_goal,z_goal,ob,main_list)
       # print("path list after change:",len(path_list))    #debbug
        return show_path(x_ori, y_ori,z_ori,x_goal,y_goal,z_goal, path)
    return show_path(x_ori,y_ori,z_ori,goal_block.prev.x,goal_block.prev.y,goal_block.prev.z,path)

if __name__ == "__main__":
    ob = []
    main_list = []
    path_list2 = []
    x_ori = int(input("input your X origin:"))
    y_ori = int(input("input your y origin:"))
    z_ori = int(input("input your z origin:"))
    x_goal = int(input("input your x goal:"))
    y_goal = int(input("input your y goal:"))
    z_goal = int(input("input your z goal:"))
    print("")
    while True:
        print("Type any non-integer value to quit.")
        try:
            x_ob = int(input("input x coordinate of obstacle:"))
            y_ob = int(input("input y coordinate of obstacle:"))
            z_ob = int(input("input z coordinate of obstacle:"))
            print("")
            ob.append(Square(x_ob,y_ob,z_ob,0))
        except ValueError:
            break

    for i in ob:
        print("x ob, y ob:",i.x,i.y,i.z)
    block_record = find_path(x_ori, y_ori,z_ori, x_goal, y_goal, z_goal, ob, main_list)
    show_path(x_ori,y_ori,z_ori, x_goal, y_goal, z_goal,path_list)

    for i in path_list1:
        path_list2.insert(0, i)

    for i in path_list2:
        print("blocks in path list 2:",i.x,i.y,i.z)


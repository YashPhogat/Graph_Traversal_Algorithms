import math
import time
import heapq

start = time.time()
filebuff = open("input4_2.txt")

# print(filebuff.read(), "\n")
algoname = filebuff.readline()
second_line = filebuff.readline()
third_line = filebuff.readline()
fourth_line = filebuff.readline()
fifth_line = filebuff.readline()

mat_dimension = tuple(map(int, second_line.split()))
start_state = tuple(reversed(tuple(map(int, third_line.split()))))
elev_threshold = int(fourth_line)
number_of_target = int(fifth_line)
# print(start_state)
goal = []

for line in range(number_of_target) :
    goal += [tuple(reversed(tuple(map(int, filebuff.readline().split()))))]

z_elevation = []

for h in range(mat_dimension[1]) :
    z_elevation += [list(map(int, filebuff.readline().split()))]

filebuff.close()

# print(goal)
# print(algoname,mat_dimension[0], mat_dimension[1], start_state, goal, elev_threshold, number_of_target)
# print(z_elevation[goal[1][1]][goal[1][0]])
# ==============The order is for accessing elevations is reversed compared to Goal state entry===========
adjacency_list = {}
adjacency_cost = {}


def build_adjacency_list() :
    for h in range(mat_dimension[1]) :
        for w in range(mat_dimension[0]) :
            adjacency_list[tuple((h, w))] = []
            # if tuple(h,w) in adjacency_list.keys():
            if abs(z_elevation[h][w] - z_elevation[h][w - 1]) <= elev_threshold and w - 1 >= 0 :
                adjacency_list[tuple((h, w))] += [tuple((h, w - 1))]
                # adjacency_cost[((h, w), (h, w - 1))] = 10
            if abs(z_elevation[h][w] - z_elevation[h - 1][w - 1]) <= elev_threshold and w - 1 >= 0 and h - 1 >= 0 :
                adjacency_list[tuple((h, w))] += [tuple((h - 1, w - 1))]
                # adjacency_cost[((h, w), (h - 1, w - 1))] = 14
            if abs(z_elevation[h][w] - z_elevation[h - 1][w]) <= elev_threshold and h - 1 >= 0 :
                adjacency_list[tuple((h, w))] += [tuple((h - 1, w))]
                # adjacency_cost[((h, w), (h - 1, w))] = 10
            if h + 1 < mat_dimension[1] and w + 1 < mat_dimension[0] and abs(
                    z_elevation[h][w] - z_elevation[h + 1][w + 1]) <= elev_threshold :
                adjacency_list[tuple((h, w))] += [tuple((h + 1, w + 1))]
                # adjacency_cost[((h, w), (h + 1, w + 1))] = 14
            if w + 1 < mat_dimension[0] and abs(z_elevation[h][w] - z_elevation[h][w + 1]) <= elev_threshold :
                adjacency_list[tuple((h, w))] += [tuple((h, w + 1))]
                # adjacency_cost[((h, w), (h, w + 1))] = 10
            if h + 1 < mat_dimension[1] and abs(z_elevation[h][w] - z_elevation[h + 1][w]) <= elev_threshold :
                adjacency_list[(h, w)] += [(h + 1, w)]
                # adjacency_cost[((h, w), (h + 1, w))] = 10
            if h + 1 < mat_dimension[1] and w - 1 >= 0 and abs(
                    z_elevation[h][w] - z_elevation[h + 1][w - 1]) <= elev_threshold :
                adjacency_list[(h, w)] += [(h + 1, w - 1)]
                # adjacency_cost[((h, w), (h + 1, w - 1))] = 14
            if w + 1 < mat_dimension[0] and h - 1 >= 0 and abs(
                    z_elevation[h][w] - z_elevation[h - 1][w + 1]) <= elev_threshold :
                adjacency_list[(h, w)] += [(h - 1, w + 1)]
                # adjacency_cost[((h, w), (h - 1, w + 1))] = 14


# make_node = {}
# def make_node():
#     for h in range(mat_dimension[1]):
#         for w in range(mat_dimension[0]):
#             make


build_adjacency_list()


#
# for k,v in adjacency_list.items():
#     print(k,"==>", v)
#
# for k,v in adjacency_cost.items():
#     print(k,"==>", v)
# print(adjacency_list.items())


def bfs(para) :
    # for state in goal:
    root = start_state
    explored = {}
    parent = {}
    path = [para]
    queue = list()
    # level = dict()
    queue.append(root)
    parent[root] = None
    # level[root] = 0
    # for neighbour in adjacency_list[root]:
    #     queue.append(neighbour)
    #     parent[neighbour] = root
    count = 1
    while True :
        # print(count)
        count += 1
        if len(queue) is 0:
            return None
        popped_node = queue.pop(0)
        explored[popped_node] = True
        # path[para] += [popped_node]
        if popped_node == para :
            while parent[popped_node] is not None :
                path += [parent[popped_node]]
                popped_node = parent[popped_node]
            print(len(path))
            return path
        else:
            for neighbour in adjacency_list[popped_node] :
                if neighbour not in explored.keys() :  # and neighbour not in queue:
                    queue.append(neighbour)
                    explored[neighbour] = True
                    parent[neighbour] = popped_node

        # print(queue)


def build_adjacency_cost(parent, neighbour):

    if parent[0] == neighbour[0] or parent[1] == neighbour[1]:
        return 10
    else:
        return 14
    # if abs(z_elevation[h][w] - z_elevation[h][w - 1]) <= elev_threshold and w - 1 >= 0 :
    #     adjacency_list[tuple((h, w))] += [tuple((h, w - 1))]
    #     adjacency_cost[((h, w), (h, w - 1))] = 10
    # if abs(z_elevation[h][w] - z_elevation[h - 1][w - 1]) <= elev_threshold and w - 1 >= 0 and h - 1 >= 0 :
    #     adjacency_list[tuple((h, w))] += [tuple((h - 1, w - 1))]
    #     adjacency_cost[((h, w), (h - 1, w - 1))] = 14
    # if abs(z_elevation[h][w] - z_elevation[h - 1][w]) <= elev_threshold and h - 1 >= 0 :
    #     adjacency_list[tuple((h, w))] += [tuple((h - 1, w))]
    #     adjacency_cost[((h, w), (h - 1, w))] = 10
    # if h + 1 < mat_dimension[1] and w + 1 < mat_dimension[0] and abs(
    #         z_elevation[h][w] - z_elevation[h + 1][w + 1]) <= elev_threshold :
    #     adjacency_list[tuple((h, w))] += [tuple((h + 1, w + 1))]
    #     adjacency_cost[((h, w), (h + 1, w + 1))] = 14
    # if w + 1 < mat_dimension[0] and abs(z_elevation[h][w] - z_elevation[h][w + 1]) <= elev_threshold :
    #     adjacency_list[tuple((h, w))] += [tuple((h, w + 1))]
    #     adjacency_cost[((h, w), (h, w + 1))] = 10
    # if h + 1 < mat_dimension[1] and abs(z_elevation[h][w] - z_elevation[h + 1][w]) <= elev_threshold :
    #     adjacency_list[(h, w)] += [(h + 1, w)]
    #     adjacency_cost[((h, w), (h + 1, w))] = 10
    # if h + 1 < mat_dimension[1] and w - 1 >= 0 and abs(
    #         z_elevation[h][w] - z_elevation[h + 1][w - 1]) <= elev_threshold :
    #     adjacency_list[(h, w)] += [(h + 1, w - 1)]
    #     adjacency_cost[((h, w), (h + 1, w - 1))] = 14
    # if w + 1 < mat_dimension[0] and h - 1 >= 0 and abs(
    #         z_elevation[h][w] - z_elevation[h - 1][w + 1]) <= elev_threshold :
    #     adjacency_list[(h, w)] += [(h - 1, w + 1)]
    #     adjacency_cost[((h, w), (h - 1, w + 1))] = 14


def ucs(para) :
    # for state in goal:
    root = start_state
    explored = {}
    parent = {}
    path = [para]
    queue = list()
    path_cost = {}
    open = {}
    parent[root] = None
    path_cost[root] = 0
    open[root] = True
    queue.append([path_cost[root], root])
    heapq.heapify(queue)
    # level[root] = 0
    # for neighbour in adjacency_list[root]:
    #     queue.append(neighbour)
    #     parent[neighbour] = root
    count = 1
    while True :
        # print(count)
        count += 1
        flag = 0
        if len(queue) is 0 :
            return None
        # popped_node = queue.pop(0)
        popped_node = heapq.heappop(queue)[1]
        open[popped_node] = False
        # explored[popped_node] = True
        # path[para] += [popped_node]
        if popped_node == para :
            while parent[popped_node] is not None :
                path += [parent[popped_node]]
                popped_node = parent[popped_node]
            print(path_cost[para])
            return path
        else:
            for neighbour in adjacency_list[popped_node] :
                if neighbour not in explored.keys() and open.get(neighbour) != True :
                    # queue.append(neighbour)
                    path_cost[neighbour] = path_cost[popped_node] + build_adjacency_cost(popped_node, neighbour)
                    heapq.heappush(queue, [path_cost[neighbour], neighbour])
                    open[neighbour] = True
                    parent[neighbour] = popped_node
                elif open[neighbour] is True :
                    if path_cost[popped_node] + build_adjacency_cost(popped_node, neighbour) < path_cost[neighbour] :
                        path_cost[neighbour] = path_cost[popped_node] + build_adjacency_cost(popped_node, neighbour)
                        parent[neighbour] = popped_node
                        heapq.heappush(queue, [path_cost[neighbour], neighbour])
                        # for i, t in enumerate(queue) :
                        #     if t[1] == neighbour :
                        #         queue[i][0] = path_cost[neighbour]
                        #         flag = 1
                        #         # heapq.heapify(queue)
                        #         break
                        # heapq.heapify(queue)
                # elif neighbour in explored.keys():
                #     if path_cost[popped_node] + adjacency_cost[(popped_node, neighbour)] < path_cost[neighbour]:
                #         explored.pop(neighbour)
                #         # queue.append(neighbour)
                #         path_cost[neighbour] = path_cost[popped_node] + adjacency_cost[(popped_node, neighbour)]
                #         heapq.heappush(queue, (path_cost[neighbour], neighbour))
                #         parent[neighbour] = popped_node
            explored[popped_node] = True
            # if flag == 1:
            #     heapq.heapify(queue)
            # sorted_queue = sorted([(x, path_cost[x]) for x in queue], key=lambda x: x[1])
            # queue = list(map(lambda x: x[0], sorted_queue))
            # print(sorted_queue, "====>", queue, "\n")


heur = dict()
# f_time_avg = 0
def heuristic(current_node, goal_node):
    # fstart = time.time()
    # global f_time_avg
    dx = abs(current_node[0] - goal_node[0])
    dy = abs(current_node[1] - goal_node[1])
    dz = abs(z_elevation[current_node[0]][current_node[1]] - z_elevation[goal_node[0]][goal_node[1]])
    heur[current_node] = 10*(dx+dy) - 6*min(dx, dy) + dz#math.sqrt(dx**2 + dy**2 + dz**2)#10*(dx+dy) - 6*min(dx, dy) + dz
    # print("Current Node", current_node, "-> Goal Node: ", goal_node, "\n", dx, "====", dy, "===",
    # dz, "\n", 10*(dx+dy) - 6*min(dx, dy) + dz)
    #     return 10*(dx+dy) - 6*min(dx, dy)
    # return 10*(dx+dy) - 6*min(dx, dy) + dz
    # f_time_avg += time.time() - fstart
    return heur[current_node]
    # return max(dx, dy)
    # return 0


astar_elev = {}


def elevation(curr_nd, child_nd):
    # if (curr_nd,child_nd) in astar_elev.keys():
    #     return astar_elev[(curr_nd,child_nd)]
    # else:
    return abs(z_elevation[curr_nd[0]][curr_nd[1]] - z_elevation[child_nd[0]][child_nd[1]])
        # return astar_elev[(curr_nd, child_nd)]


def a_star(para) :
    # for state in goal:
    global f_time_avg
    root = start_state
    explored = {}
    parent = {}
    path = [para]
    queue = list()
    path_cost = {}
    final_cost = {}
    open = {}
    heur.clear()
    parent[root] = None
    path_cost[root] = 0
    final_cost[root] = 0#path_cost[root] + heuristic(root, para)
    queue.append([final_cost[root], root])
    open[root] = True
    heapq.heapify(queue)
    # level[root] = 0
    # for neighbour in adjacency_list[root]:
    #     queue.append(neighbour)
    #     parent[neighbour] = root
    count = 1
    # func_call = 0
    # first_if = 0
    # second_if = 0
    # sec_if_start = 0
    while True:
        count +=1

        if len(queue) is 0 :
            return None
        # heapq.heapify(queue)
        flag = 0
        popped_node = heapq.heappop(queue)[1]
        open[popped_node] = False
        if popped_node == para:
            while parent[popped_node] is not None :
                path += [parent[popped_node]]
                popped_node = parent[popped_node]
            print(path_cost[para])
            # print("Heur time", f_time_avg)
            # print("1st If Time:", first_if)
            # print("2nd If Time:", second_if)
            # print("Count", count)
            return path
        else:

            for neighbour in adjacency_list[popped_node]:
                newcs = path_cost[popped_node] + build_adjacency_cost(popped_node, neighbour) + \
                        elevation(popped_node, neighbour)

                if explored.get(neighbour) != True and open.get(neighbour) != True:
                    # first_if_start = time.time()
                    path_cost[neighbour] = newcs
                    # func_call+=1
                    final_cost[neighbour] = newcs + heuristic(neighbour, para)
                    open[neighbour] = True
                    heapq.heappush(queue, [final_cost[neighbour], neighbour])
                    parent[neighbour] = popped_node
                    # first_if += time.time() - first_if_start
                elif open[neighbour] is True:
                    # sec_if_start = time.time()

                    if newcs < path_cost[neighbour]:
                        path_cost[neighbour] = newcs

                        f_newcs = newcs + heur[neighbour]
                        final_cost[neighbour] = f_newcs
                        parent[neighbour] = popped_node
                        heapq.heappush(queue, [final_cost[neighbour], neighbour])
                        # for i in queue:
                        #     if i[1] == neighbour:
                        #         flag = 1
                        #         # print(queue[i],"==")
                        #         i[0] = f_newcs
                        #         # print(queue[i], "\n")
                        #
                        #         break
                        # heapq.heapify(queue)
                    # second_if += time.time() - sec_if_start

            explored[popped_node] = True
            # if flag == 1:
            #     heapq.heapify(queue)


output_buff = open("output.txt", 'w')
algoname = algoname.rstrip()
# print(algoname)
str2 = ''
if algoname == "BFS" and start_state[0] >=0 and start_state[1]>=0:
    str2 = ''
    for param in goal:
        returned = bfs(param)
        if returned is None:
            str2 += "FAIL\n"
        else:
            sol = [t[::-1] for t in returned]
            # print(str(sol))
            str_ans = list(reversed(sol));
            str1 = [str(x).strip('()') for x in str_ans]
            for x in str1:
                str2 += x.replace(" ", '') + " "
            str2 += "\n"
        # print(list(reversed(sol)), "\n")
# print(len(sol))
# #
if algoname == "UCS" and start_state[0] >=0 and start_state[1]>=0:
    str2 = ''
    for param in goal :
        returned = ucs(param)
        if returned is None :
            str2 += "FAIL\n"
        else :
            sol = [t[: :-1] for t in returned]
            # print(str(sol))
            str_ans = list(reversed(sol));
            str1 = [str(x).strip('()') for x in str_ans]

            for x in str1 :
                str2 += x.replace(" ", '') + " "
            str2 += "\n"
        # print(list(reversed(sol)), "\n")
# #     # print(ucs(param))
# #
# # # print("\n\n")
if algoname == "A*" and start_state[0] >=0 and start_state[1]>=0:
    str2 = ''
    for param in goal:

        if 0 <= param[0] < mat_dimension[1] and 0 <= param[1] < mat_dimension[0] :
            returned = a_star(param)
            if returned is None :
                str2 += "FAIL\n"
            else:
                sol = [t[: :-1] for t in returned]
                # print(str(sol))
                str_ans = list(reversed(sol));
                str1 = [str(x).strip('()') for x in str_ans]

                for x in str1 :
                    str2 += x.replace(" ", '') + " "
                str2 += "\n"
        else:
            str2 += "FAIL\n"
        # print(list(reversed(sol)), "\n")
if start_state[0] <0 or start_state[1]<0:
    str2 = "FAIL"
output_buff.write(str2.rstrip())
output_buff.close()
print("Time:", time.time() - start)

from station import *
from line import *
class Graph:

    def __init__(self, lst_line=[]):
        self.lst_line = lst_line

    def get_station(self, line, id):
        for i in self.lst_line:
            if i.get_line() == line:
                return i.get_lst_station()[id-1]

    def build_graph(self):
        graph = {}
        for i in self.lst_line:
            stations = i.get_lst_station()
            for id, sta in enumerate(stations):
                temp = []
                if id - 1 > -1:
                    temp.append(stations[id-1])
                if id + 1 < len(stations):
                    temp.append(stations[id+1])
                if sta not in graph.keys():
                    lst = []
                    for check in graph.keys():
                        if sta.get_name() == check.get_name():
                            lst = graph[check]
                            graph[check] = graph[check] + temp
                    graph[sta] = lst
                graph[sta] = graph[sta] + temp
        return graph


def get_data(filename):
      with open(filename, 'r') as f:
          data = f.readlines()
          lst = []
          req = []
          temp = ''
          for i in data:
              if i[0] == '#':
                  temp = i[1:-1]
              elif i[0].isdigit():
                  lst.append(temp + ':' + i[:-1])
              else:
                  req.append(i)
      return lst, req


def get_stations(lst):
      lst_station = []
      for i in lst:
          tmplst = i.split(":")
          if len(tmplst) == 3:
              tmplst.append(None)
          else:
              del tmplst[3]
          lst_station.append(Station(tmplst))
      return lst_station

def get_lines(lst_station):
      lst_line = []
      tmpdict = {}
      for i in lst_station:
          tmpline = i.get_line()
          if tmpline not in tmpdict.keys():
              tmpdict[tmpline] = []
          tmpdict[tmpline].append(i)
      for i, j in tmpdict.items():
          lst_line.append(Line(i,j))
      return lst_line

def bfs_paths(graph, start, end):
    queue = [[start, [start]]]
    path_name = []
    path_name.append(start.get_name())
    while queue:
        [vertex, path] = queue.pop(0)
        for next in graph[vertex]:
            if not check_name_path(path, next.get_name()):
                if next == end:
                    yield path + [next]
                else:
                    queue.append([next, path + [next]])

def print_list(lst):
    for i in lst:
        i.print_name()
    print()

def check_name_path(lst, name):
    for i in lst:
        if i.get_name() == name:
            return True
    return False

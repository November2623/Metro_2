from graph import *
from train import *
from argparse import ArgumentParser
def process_argparse():
    parser = ArgumentParser()
    parser.add_argument('File', help='a file containing a list of stations',
                        type=str)
    return parser.parse_args()
def get_start_end_station(list):
    start = []
    end = []
    train_total = []

    for element in list:
        if 'START' in element:
            temp  = (element.strip()).split('=')
            temp1 = temp[1].split(':')
            for ele in temp1:
                if ele.isdigit():
                    ele = int(ele)
                    start.append(ele)
                else:
                    start.append(ele)
        elif 'END' in element:
            temp  = (element.strip()).split('=')
            temp1 = temp[1].split(':')
            for ele in temp1:
                if ele.isdigit():
                    ele = int(ele)
                    end.append(ele)
                else:
                    end.append(ele)
        elif 'TRAINS' in element:
            temp = (element.strip()).split("=")
            train_total.append(int(temp[1]))
    return start, end, train_total

def main():
    args = process_argparse()
    lst, req = get_data(args.File)
    lst_station = get_stations(lst)
    lst_line = get_lines(lst_station)
    graph = Graph(lst_line)
    get_start_end_station(req)
    start_pos, end_pos, train_total = get_start_end_station(req)
    map = graph.build_graph()
    start = graph.get_station(start_pos[0],start_pos[1])
    end = graph.get_station(end_pos[0],end_pos[1])

    a = list(bfs_paths(map, start, end))[0]
    print_list(a)

    lst_train = [Train(i, start) for i in range(1,train_total[0] + 1)]

    route = 0
    while check_loop(lst_train, end) and route < 100:
        route += 1
        print("Route: ", route)
        for i in lst_train:
          if i.get_length_path() < len(a):
            for j, sta in enumerate(a):
              if i.get_cur() == sta and i.get_cur() != end:
                next = a[j+1]
            i.move_to_station(next, len(a))

        for j in a:
          j.print_status()
        print()

main()

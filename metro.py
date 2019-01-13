from graph import *
from train import *
from argparse import ArgumentParser
def process_argparse():
    parser = ArgumentParser()
    parser.add_argument('File', help='a file containing a list of stations',
                        type=str)
    return parser.parse_args()

def main():
    args = process_argparse()
    lst, req = get_data(args.File)
    lst_station = get_stations(lst)
    lst_line = get_lines(lst_station)
    graph = Graph(lst_line)

    map = graph.build_graph()
    start = graph.get_station('Red Line', 15)
    end = graph.get_station('Blue Line', 36)

    a = list(bfs_paths(map, start, end))[0]
    print_list(a)

    lst_train = [Train(i, start) for i in range(1,31)]

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

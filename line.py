class Line:

    def __init__(self, name, lst_station=[]):
        self.name = name
        self.lst_station = lst_station


    def get_line(self):
        return self.name

    def get_lst_station(self):
        return self.lst_station

    def find_station(self, name):
        for i in self.lst_station:
          if i.get_name() == name:
            return i

    def print(self):
        print(self.name, end=': ')
        for i in self.lst_station:
            print(i.get_name(),end = ' -> ')
        print()

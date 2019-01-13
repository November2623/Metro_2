class Train:

    def __init__(self, id, start):
        self.id = id
        self.cur_sta = start
        self.checkmove = 0
        self.path = [start]


    def move_to_station(self, station, n):
        self.checkmove += 1
        if self.cur_sta.get_line() != station.get_line():
            check = 2
        else:
            check = 1
        if self.checkmove >= check and station.get_aval() is True:
          if self.cur_sta:
              self.cur_sta.set_check()
          if len(self.path) == n - 1:
              self.cur_sta.pop_train()
              self.cur_sta = station
              self.path.append(station)
              station.add_train(self)
          elif len(self.path) < n:
              self.cur_sta.pop_train()
              station.set_check()
              self.cur_sta = station
              self.path.append(station)
              station.add_train(self)
          self.checkmove = 0



    def get_cur(self):
        return self.cur_sta

    def get_id(self):
        return self.id

    def get_path(self):
        return self.path

    def get_length_path(self):
        return len(self.path)

    def check_end(self, end):
        if self.cur_sta == end:
          return True
        return False


def check_loop(lst_train, end):
    for i in lst_train:
      if i.check_end(end) == False:
        return True
    return False

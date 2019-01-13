class Station:

    def __init__(self, station):
        self.line =  station[0]
        self.id = station[1]
        self.name = station[2]
        self.transfer = station[3]
        self.check = True
        self.train = []

    def print_name(self):
        print(self.name,end=' -> ')

    def get_line(self):
        return self.line

    def get_name(self):
        return self.name

    def get_trans(self):
        return self.transfer

    def get_id(self):
        return self.id

    def get_aval(self):
        return self.check

    def set_check(self):
        if self.check is not True:
          self.check = True
        else:
          self.check = False

    def set_trans(self, trans):
        self.line = self.trans

    def add_train(self, train):
        self.train.append(train)

    def pop_train(self):
        if len(self.train) > 0:
          self.train.pop(0)

    def print_status(self):
        if len(self.train) > 0:
          self.print_name()
          for i in self.train:
            print(i.get_id(), end=' ')
          print()

class Station:

    def __init__(self, station):
        self.line = station[0]
        self.id = station[1]
        self.name = station[2]
        if station[3] is not None:
            station[3] = station[3][1:]
        self.transfer = station[3]
        self.check = True
        self.train = []
        self.checktrans = False

    def print_name(self):
        print(self.name, end=' -> ')

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

    def set_checktrans(self):
        if self.checktrans is False:
            self.checktrans = True
        else:
            self.checktrans = False

    def set_trans(self, trans):
        self.line = self.trans

    def add_train(self, train):
        self.train.append(train)

    def pop_train(self):
        if len(self.train) > 0:
            self.train.pop(0)

    def print_status(self):
        if len(self.train) > 0:
            if self.checktrans is True and self.transfer is not None:
                line = self.transfer
            else:
                line = self.line
            print(self.name + '(' + line + ':' + self.id + ')', end='-')
            for i in self.train:
                print(i.get_id(), end=' ')
            print()

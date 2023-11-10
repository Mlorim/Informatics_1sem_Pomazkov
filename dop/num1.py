class Type():
    def __init__(self, arg1, arg2, is_dict=0):
        self.arg1 = arg1
        self.arg2 = arg2
        self.is_dict = is_dict
        if not is_dict:
            print(self.add())

    def add(self):
        if isinstance(self.arg1, type(self.arg2)):
            if isinstance(self.arg1, dict):
                for i in self.arg2.keys():
                    if i in self.arg1.keys():
                        self.arg1[i] = Type(self.arg1[i], self.arg2[i], is_dict=1).add()
                    else:
                        self.arg1[i] = self.arg2[i]
                return self.arg1
            else:
                return self.arg1 + self.arg2
        else:
            return 'Input types mismatch'

t = Type({1: 3}, {1: 3, 3: 4})
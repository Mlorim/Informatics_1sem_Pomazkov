class Aircraft():
    def __init__(self, is_pass, cond, sits, pass_num):
        self.is_pass = is_pass
        self.sits = sits
        self.pass_num = pass_num
        self.cond = cond

    '''
    try:
        def __init__(self, is_pass, cond, sits, pass_num):
        self.is_pass = is_pass
        self.sits = sits
        self.pass_num = pass_num
        self.cond = cond
        
    except Exception:
        def __init__(self, is_pass, cond):
        self.is_pass = is_pass
        self.cond = cond
    '''

    def filling(self):
        if self.is_pass:
            if self.sits != 0:
                print('Наполнение: ', round(self.pass_num / self.sits, 2))
            else:
                print('Введено нулевое число мест')
        else:
            print('Судно не предназначено для перевозок пассажиров.')
        if not (self.cond):
            print('Требуется ремонт')


new_airplane = Aircraft(True, False, 100, 100)
new_airplane.filling()


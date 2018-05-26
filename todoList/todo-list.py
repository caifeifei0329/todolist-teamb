


def create_user():
    TodoDB.add_user(5, 'zhangjing', '123456')


def get_user():
    TodoDB.select_user()



def delete():
    pass



def read():
    pass


if __name__ == "__main__":
    create_user()
    get_user()
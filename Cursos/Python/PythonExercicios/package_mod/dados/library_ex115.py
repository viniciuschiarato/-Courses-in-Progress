def file_exist(file_name):
    try:
        a = open(file_name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

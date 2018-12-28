import re
import pymysql.cursors


def address(path):
    def wrapper(func):
        def wrap_func(*args, **kwargs):
            request = args[0]
            match_object = re.search(r'GET\s\/(\w+)|POST\s\/(\w+)', request).groups()
            if path == match_object[1]:
                firstname = re.search(r'firstname=(\w+)', request).groups()[0]
                lastname = re.search(r'lastname=(\w+)', request).groups()[0]
                data={
                    "firstname": firstname,
                    "lastname":lastname   
                        }
                print(data)
                connection = pymysql.connect(
                             host='localhost',
                             user='root',
                             password='',
                             db='data',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
                try:
                    with connection.cursor() as cursor:
                        sql = "INSERT INTO `name` (`name`, `lastname`) VALUES (%s, %s)"
                        cursor.execute(sql, (firstname, lastname))
                    connection.commit()

                finally:
                    connection.close()

            if path == match_object[0]:
                func(*args, **kwargs)
            else:
                kwargs['match'] = False
                func(*args, **kwargs)

        return wrap_func
    return wrapper
import uuid
import csv

USERS_FILE = '../dataBase/users.csv'
# TODO: Need to hash the password in this module, and error heandling in every function, need doucomentation on the functions 
def create_user(name, mail, password):
    user_id = uuid.uuid4().hex
    
    account = {'user_id': user_id,
              'name': name,
              'mail': mail,
              'password': password}
    
    with open(USERS_FILE, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=account.keys())
        writer.writerow(account)

    return get_user(name, password)


def delete_user(user_id):
    users = []
    removed_user = None
    fields = None
    
    with open(USERS_FILE, 'r') as csvfile:
        reader = csv.reader(csvfile)
        fields = next(reader)
        for row  in reader:
            if row[0] != user_id:
                users.append(row)
            else:
                removed_user = row
                break


    with open(USERS_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)
        writer.writerows(users)
    # TODO: need to remove all user expenses and categories data where and when to do it?
    return removed_user         # Do I need to return it as a json dict   

def get_user(name, password):
    user = None
    with open(USERS_FILE, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None) 
        for row  in reader:
            if row[1] == name and row[3] == password:
                user = row
                break

    return user     # Do I need to return it as a json dict   



def main():
    print('hi')
    print(create_user('avi kaufman', 'avrikaufman@gmail.com', '123'))
    print(get_user('avi kaufman', '123'))
    # print(delete_user('dacececf0b6d4555998237c00e5245f1'))
    # print(delete_user('e662fa3c08e94206a8504819d81a9046'))
if __name__ == '__main__':
    main()


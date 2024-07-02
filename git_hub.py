import psycopg2

conn = psycopg2.connect(database='lesson',
                        user='postgres',
                        host='localhost',
                        password='703',
                        port=5432)

cursor = conn.cursor()

# create_Teach_table = '''create table teach(
#     id serial primary key,
#     name varchar(100) not null,
#     age int ,
#     email varchar(100) not null,
#     phone_number int
# );
# '''

# cursor.execute(create_Teach_table)
# conn.commit()

class User:

    def __init__(self,name:str,age:int,email:str,phone_number:int):
        self.name = name
        self.age = age
        self.email = email
        self.phone_number = phone_number

    def save(self):
        insert_into_query = ''' insert into teach(name,age,email,phone_number)
        values(%s,%s,%s,%s);
        '''
        data = (self.name,self.age,self.email,self.phone_number)
        cursor.execute(insert_into_query,data)
        conn.commit()

    def get_user(self):
        select_query = '''select * from teach;
        '''
        cursor.execute(select_query)
        return cursor.fetchall
    
Support_Teacher = User('Ulug\'bek',23,'ulug\'bek@gmail.com',945566744)
Teacher = ('Jasur Mavlonov',23,'jasur@gmail.com',9999999)

Teacher.save()

# Support_Teacher.get_user()
# print(Support_Teacher.get_user)






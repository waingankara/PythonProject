import psycopg2


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = """
        CREATE TABLE homeworkUpload (
                                    id SERIAL PRIMARY KEY,
                                    standard varchar(10) NOT NULL,
                                    division varchar(10) NOT NULL,
                                    subject varchar(50) NOT NULL,
                                    date_of_homework  timestamp NOT NULL,
                                    teacher_name  varchar(100)  NOT NULL,
                                    type_of_homework  varchar(20)  NOT NULL,
                                    desc_of_homework varchar(2000) NOT NULL,
                                    upload_timestamp timestamp NOT NULL
        )
        """

    try:
        conn = psycopg2.connect(host="ec2-35-171-31-33.compute-1.amazonaws.com", port="5432", database="d956fup5kvskk5", user="cltbvwwddpvocq", password="dd36a41744868363a7c73dbf33a3860e403728d119dff56c5b58215329dfc8e7")

        cur = conn.cursor()
        # create table one by one

        cur.execute(commands)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



def create_homework(homework):
    """ create tables in the PostgreSQL database"""
    commands = """
        insert into homeworkUpload (standard,division,subject,date_of_homework,teacher_name ,type_of_homework, desc_of_homework, upload_timestamp )
        values (%s,%s,%s,%s,%s,%s,%s,%s)
        """

    try:
        conn = psycopg2.connect(host="ec2-35-171-31-33.compute-1.amazonaws.com", port="5432",database="d956fup5kvskk5", user="cltbvwwddpvocq", password="dd36a41744868363a7c73dbf33a3860e403728d119dff56c5b58215329dfc8e7")

        cur = conn.cursor()
        cur.execute(commands, homework)

        conn.commit()
        count = cur.rowcount
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def get_homeworks():
        commands = """
               SELECT id as srNo, standard,division,subject, to_char( date_of_homework, 'DD-MON-YYYY') as date_of_homework,
                 teacher_name,type_of_homework,desc_of_homework,to_char( upload_timestamp, 'DD-MON-YYYY') as upload_date FROM homeworkUpload
               """

        try:
            conn = psycopg2.connect(host="ec2-35-171-31-33.compute-1.amazonaws.com", port="5432", database="d956fup5kvskk5",
                                    user="cltbvwwddpvocq",
                                    password="dd36a41744868363a7c73dbf33a3860e403728d119dff56c5b58215329dfc8e7")

            cur = conn.cursor()
            cur.execute(commands)
            rows = cur.fetchall()


            cur.close()
            conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        return rows
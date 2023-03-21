import psycopg2
import psycopg2.extras as ext

def run_sql(sql, values = None):
    #set up a variable for the connection
    conn = None
    #set up an emplty list
    results = []
    #try to connect to the database
    try:
        conn = psycopg2.connect("dbname='task_manager'")
    #get cursor from db which is an object
        cur = conn.cursor(cursor_factory=ext.DictCursor)
    #execute the sql
        cur.execute(sql, values)
    #commit the execution
        conn.commit()
    #get results
        results = cur.fetchall()
    #close the db connection
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
       print(error)
    finally:
        if conn is not None:
            conn.close()
    #return the list that we've set up
    return results
    

# def run_sql(sql, values = None):
#     conn = None
#     results = []
#     try:
#         conn = psycopg2.connect("dbname='task_manager'")
#         cur = conn.cursor(cursor_factory=ext.DictCursor)
#         cur.execute(sql, values)
#         conn.commit()
#         results = cur.fetchall()
#         cur.close()
#     except(Exception, psycopg2.DatabaseError) as error:
#        print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#     return results
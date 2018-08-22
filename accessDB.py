# By Dominic Eggerman

# Connect to database
def connect(usr, pswrd):
    # Establish connection with username and password
    connection = psycopg2.connect(dbname="insightprod",
                                    user=usr,
                                    password=pswrd,
                                    host="insightproddb")
    print("Successfully connected to database...")
    return connection

# Query database
def query(conn, start_date, pipe_id, point):
    
    # Create SQL statement
    statement = """SELECT loc.name, eod.gas_day, eod.scheduled_cap, eod.operational_cap  
                    FROM analysts.location_role_eod_history_v AS eod
                    INNER JOIN maintenance.location_role AS lr ON eod.location_role_id = lr.id
                    INNER JOIN maintenance.location AS loc ON lr.location_id = loc.id
                    WHERE eod.gas_day >= {0}
                    AND loc.name ILIKE {2}
                    ORDER BY eod.gas_day
    """.format(start_date, pipe_id, point)
    print(statement)

    # Read to pandas dataframe
    print("Querying database...")
    df = pd.read_sql(statement, conn)
    return df


# Run
if __name__ == "__main__":
    # Imports
    import getpass
    import psycopg2
    import pandas as pd

    # User entries
    # username = input('Enter username: ')
    # password = getpass.getpass('Enter password: ')
    # date = input("Enter start date: ")
    # pipeline_id = input("Enter pipeline id: ")
    # point_name = input("Enter point name: ")

    # Connect, query, and print df
    connection = connect(username, password)
    df = query(connection, date, pipeline_id, point_name)
    print(df)

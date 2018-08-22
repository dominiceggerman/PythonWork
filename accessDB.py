# By Dominic Eggerman

# Connect to database
def connect(usr, pswrd):
    # Establish connection with username and password
    connection = psycopg2.connect(dbname="gasaprod",
                                    user=usr,
                                    password=pswrd,
                                    host="gasaproddb")
    print("Successfully connected to database...")
    return connection

# Query database
def query(conn):
    # Create SQL statement
    statement = """SELECT * FROM maintenance.location AS loc
                    WHERE pipeline_id = 274
                    AND name ILIKE '%carti%'
                    ORDER BY loc.name;"""

    # Read to pandas dataframe
    df = pd.read_sql(statement, conn)
    return df


# Run
if __name__ == "__main__":
    # Imports
    import getpass
    import psycopg2
    import pandas as pd

    username = input('Enter username: ')
    password = getpass.getpass('Enter password: ')
    connection = connect(username, password)
    df = query(connection)
    print(df)

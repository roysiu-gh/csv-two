import sqlite3, csv, sys, time, os

class ContainsIDException(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)

def convert(csv_name, db_name, table_name, external_header_row=[], commit=False, dev=False): #checktablename for injection, auto increment, remove ID
    """Convert a CSV into an SQL database, if database and table exists, append data.
    Do not include ID column; if included, raise ContainsIDException

    Keyword arguments:
        csv_name -- CSV input file
        db_name -- name if database file to output to
        table_name -- name of table within database to write to
        external_header_row -- list of names of table columns (default [])
            note that only the first item when each item is split with " " as delimeter will be used
            if false, header row will be extracted from the first row of the csv
        commit = commit changes if true (default False)
        dev = delete file in db_name if true (default False)
    
    Raises:
        ContainsIDException -- if header row contains ID column
    """

    extract_value_names = lambda x:",".join([ item.split()[0] for item in x.split(",") ]) 
    
    if dev and os.path.isfile(db_name): os.remove(db_name)
    with sqlite3.connect(db_name) as connection:  # Set context manager for database
        cursor = connection.cursor()
        with open(csv_name) as csvf:  # Set context manager for csv
            
            if not external_header_row: config_ln = csvf.readline()  # Get configurations for database columns from header row
            else: config_ln = external_header_row #iterator or string?
            
            iden="ID INTEGER PRIMARY KEY AUTOINCREMENT"            
            command = "CREATE TABLE IF NOT EXISTS {table} ({iden}, {conf});".format(table=table_name, iden=iden, conf=config_ln) #table and conf not secure
            cursor.execute(command)
            
            val_nams = extract_value_names(config_ln)
            if "id" in [ x.lower()for x in val_nams ]: raise ContainsIDException
            
            reader = csv.reader(csvf, delimiter=",", quotechar="\"")  # Instantiate csv reader
            for row in reader:
                for index, item in enumerate(row):  # Insert NULL into empty fields
                    if not item: row[index] = "NULL"
                wqm = "INSERT INTO {table} ({names}) VALUES ({vals})".format( table=table_name, names=val_nams, vals="?,"*(len(row)-1)+"?" )
                command_args = ( wqm, (*row,) )
                cursor.execute(*command_args)
            
            if commit: connection.commit()
            #----
            while True:
                ans = input("print recrds to stdout? y/n\n").lower()
                if ans == "y":
                    cursor.execute("SELECT * FROM {}".format(table_name))
                    for r in cursor.fetchall():
                        print(r)
                    break
                elif ans == "n":
                    break
                print("'{}' not a valid option".format(ans))
        
if __name__ == "__main__":
    pass 

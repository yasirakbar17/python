import mysql.connector
import pandas as pd

database_config = {
    'host': 'localhost',
    'user': 'nama_user',
    'password': 'password',
    'database': 'nama_database'
}

koneksi = mysql.connector.connect(**database_config) #membuat koneksi
cursor = koneksi.cursor()
query = "SELECT * FROM NAMA TABEL" #nama tabel
cursor.execute(query)
column = [description[0] for description in cursor.description]

df = pd.DataFrame(cursor.fetchall(), columns=column) # Membuat DataFrame

cursor.close()
conn.close()  # Menutup koneksi

dfcolumn_names = [description[0] for description in cursor.description]  # Menampilkan DataFrame

df = pd.DataFrame(cursor.fetchall(), columns=column_names) # Membuat DataFrame

cursor.close() 
conn.close()  # Menutup koneksi


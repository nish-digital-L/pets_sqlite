import streamlit as st
import sqlite3
DATABASE = 'test.db'

con= sqlite3.connect(DATABASE)
cur = con.cursor()# sqliteを操作するカーソルオブジェクトを作成

cur.execute('SELECT * FROM Pets')#全表示
#cur.execute('DELETE FROM warriors WHERE class="steel"')#classがbronzeのrecordを削除
#cur.execute('DROP TABLE warriors')#データベースからテーブルを削除
#print (cur.fetchall())

rows = cur.fetchall()
for i,j in rows:
    #print(i,j)
    #print(f"{i} has a :{j}:") 
    st.write(f"{i} has a :{j}:")


# 4.データベースにデータをコミット
con.commit()

# 5.データベースの接続を切断
cur.close()
con.close()
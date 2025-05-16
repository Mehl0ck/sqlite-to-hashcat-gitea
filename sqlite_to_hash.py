import sqlite3
from base64 import b64encode,b64decode



if __name__ == '__main__':
    con = sqlite3.connect("gitea.db")  #  <-- change this if needed
    cur = con.cursor()
    row = cur.execute("select passwd_hash_algo, salt, passwd from user ").fetchall()

    for r in row:
        algorithm = "sha256"
        iterations = r[0].split('$')[1]
        base64_salt = b64encode(bytes.fromhex(r[1])).decode()
        base64_hash = b64encode(bytes.fromhex(r[2])).decode()
        print(f"{algorithm}:{iterations}:{base64_salt}:{base64_hash}")


    cur.close()
    con.close()

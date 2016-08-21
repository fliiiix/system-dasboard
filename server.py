from bottle import route, get, post, run, template, request
import sqlite3

con = sqlite3.connect('dasboard.db')

@post('/')
def index():
    
    j = request.json
    cursor = con.cursor()
    cursor.execute("INSERT INTO dns_status (host_id, hosts_md5, resolv_md5, config_md5, local_ip, remote_ip) VALUES (?, ?, ?, ?, ?, ?)", 
                                           (j['host_id'], j['hosts'], j['resolv'], j['config'], j['local'], j['remote']))
    con.commit()
    return 'ok\n'

@get('/createdb')
def createdb():
    cursor = con.cursor()
    cursor.execute('DROP TABLE IF EXISTS dns_status')
    cursor.execute('''CREATE TABLE dns_status (
                                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                                               host_id VARCHAR(100),
                                               hosts_md5 VARCHAR(32), 
                                               resolv_md5 VARCHAR(32), 
                                               config_md5 VARCHAR(32), 
                                               local_ip VARCHAR(15), 
                                               remote_ip VARCHAR(15),
                                               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    con.commit()
    return 'yo'

run(host='192.168.17.174', port=8888)


from bottle import route, get, post, run, template, request, static_file
import sqlite3

con = sqlite3.connect('dasboard.db')

@post('/')
def create_dns_status():
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


@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./web/dist')

run(host='0.0.0.0', port=8888)


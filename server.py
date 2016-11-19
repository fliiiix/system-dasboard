from bottle import route, get, post, redirect, run, template, request, static_file
import sqlite3
import json

con = sqlite3.connect('dashboard.db')

@post('/')
def create_dns_status():
    j = request.json
    cursor = con.cursor()
    cursor.execute("INSERT INTO dns_status (host_id, hosts_md5, resolv_md5, config_md5, local_ip, remote_ip) VALUES (?, ?, ?, ?, ?, ?)", 
                                           (j['host_id'], j['hosts'], j['resolv'], j['config'], j['local'], j['remote']))
    con.commit()
    return 'ok\n'

class SetEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, set):
      return list(obj)
    return json.JSONEncoder.default(self, obj)

@get('/dns_status')
def get_dns_status():
  cursor = con.cursor()

  t = ('aegaeon.l33t.network',)
  cursor.execute('SELECT * FROM dns_status WHERE host_id=? ORDER BY created_at DESC', t)
  host1 = cursor.fetchone()

  t = ('janus.l33t.network',)
  cursor.execute('SELECT * FROM dns_status WHERE host_id=? ORDER BY created_at DESC', t)
  host2 = cursor.fetchone()

  data = {host1, host2}

  return json.dumps(data, cls=SetEncoder)


@post('/dns_status')
def post_dns_status():
  cursor = con.cursor()
  # some validation would be nice xD
  cursor.execute('INSERT INTO dns_status_expected_values (resolv_md5, remote_ip, local_ip, config_md5, hosts_md5) VALUES(?, ?, ?, ?, ?)', request.json.values())
  con.commit()
  'ok'


"""
should be probably removed
"""
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

    cursor.execute('DROP TABLE IF EXISTS dns_status_expected_values')
    cursor.execute('''CREATE TABLE dns_status_expected_values (
                                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                                               hosts_md5 VARCHAR(32), 
                                               resolv_md5 VARCHAR(32), 
                                               config_md5 VARCHAR(32), 
                                               local_ip VARCHAR(15), 
                                               remote_ip VARCHAR(15),
                                               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    con.commit()
    return 'yo'

@get('/')
def index():
  redirect('/index.html')

"""
Serve the web ui
"""
@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./web/dist')

run(host='0.0.0.0', port=8888)


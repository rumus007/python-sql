from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import psycopg2
# postgres://wdcynmgj:uWKB7inHMuqT3Z5vgbEIrhJMfI4ukosb@mahmud.db.elephantsql.com/wdcynmgj


# Sample connection to ElephantSQL
conn = psycopg2.connect(
    database="wdcynmgj",
    user="wdcynmgj",
    password="uWKB7inHMuqT3Z5vgbEIrhJMfI4ukosb",
    host="mahmud.db.elephantsql.com",
    port="5432"
)


class APIServer(BaseHTTPRequestHandler):
    #function to set http headers
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    #function to fetch all data from table
    def do_GET(self):
        if self.path == '/students':
            self._set_headers()

            conn.autocommit = True
            cur = conn.cursor()
            sql = '''SELECT * FROM utstudents'''
            cur.execute(sql)
            results = cur.fetchall()
            conn.commit()

            self.wfile.write(json.dumps(results).encode())
        else:
            # get single data from table
            id = int(self.path.split('/')[-1])

            conn.autocommit = True
            cur = conn.cursor()

            sql = '''SELECT * FROM utstudents WHERE id = %s'''

            cur.execute(sql, (id,))
            results = cur.fetchall()

            conn.commit()

            if results:
                self._set_headers()
                self.wfile.write(json.dumps(results).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps(
                    {'message': 'Student not found'}).encode())

    #function to insert data into table
    def do_POST(self):
        if self.path == '/students':
            content_length = int(self.headers['Content-Length'])
            data = json.loads(self.rfile.read(content_length))
            # load data from json
            firstname = data['firstname']
            lastname = data['lastname']
            address = data['address']
            city = data['city']
            course_enrolled = data['course_enrolled']
            # insert data into table
            conn.autocommit = True
            cur = conn.cursor()

            sql = '''INSERT INTO utstudents (firstname, lastname, address, city, course_enrolled) VALUES (%s, %s, %s, %s, %s)'''

            cur.execute(sql, (firstname, lastname,
                        address, city, course_enrolled))
            print("Data inserted successfully")

            conn.commit()

            self._set_headers(201)
            self.wfile.write(json.dumps(
                {'message': "Data inserted successfully"}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps(
                {'message': 'Endpoint not found'}).encode())

    #function to update data into table
    def do_PUT(self):
        id = int(self.path.split('/')[-1])
        # get single data from table
        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length))
        # load data from json
        firstname = data['firstname']
        lastname = data['lastname']
        address = data['address']
        city = data['city']
        course_enrolled = data['course_enrolled']
        # update data into table
        conn.autocommit = True
        cur = conn.cursor()

        sql = '''UPDATE utstudents SET firstname = %s, lastname = %s, address = %s, city = %s, course_enrolled = %s WHERE id = %s'''

        cur.execute(sql, (firstname, lastname,
                          address, city, course_enrolled, id))

        conn.commit()

        self._set_headers(201)
        self.wfile.write(json.dumps(
            {'message': "Data updated successfully"}).encode())

    #function to delete data from table
    def do_DELETE(self):
        id = int(self.path.split('/')[-1])
        # delete data from table
        conn.autocommit = True
        cur = conn.cursor()
        sql = '''DELETE FROM utstudents WHERE id = %s'''
        cur.execute(sql, (id,))
        conn.commit()

        self._set_headers(201)
        self.wfile.write(json.dumps(
            {'message': "Data daleted successfully"}).encode())

        

#function to run server
def run_server():
    host = 'localhost'
    port = 8000
    server_address = (host, port)

    httpd = HTTPServer(server_address, APIServer)
    print(f'Starting server on {host}:{port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()

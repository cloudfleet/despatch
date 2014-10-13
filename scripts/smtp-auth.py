import yaml, socket
from flask import Flask, request, make_response


app = Flask(__name__)

config = yaml.safe_load(open("config/relay-config.yml"))

@app.route('/auth')
def auth_smtp_request():
    try:
        username = request.headers.get("Auth-User")
        password = request.headers.get("Auth-Pass")

        if username in ['doublemalt.bonniecloud.com', 'kermit.bonniecloud.com'] and password == 'password':
            resp = make_response("Authenticated!", 200)
            resp.headers['Auth-Status'] = 'OK'
            resp.headers['Auth-Server'] = socket.gethostbyname(config["host"])
            resp.headers['Auth-Port'] = config["port"]
            resp.headers['Auth-Pass'] = config["pass"]
            resp.headers['Auth-User'] = config["user"]
            return resp
        else:
            raise

    except:
        resp = make_response("No valid authentication!", 200)
        resp.headers['Auth-Status'] = 'Invalid login or password'
        return resp


if __name__ == '__main__':
    app.run(port=6666)

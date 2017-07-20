from urllib.parse import urlencode
from chalice import Chalice


app = Chalice(app_name='query-args-as-a-service')


@app.route('/query-string-pls', methods=['POST'])
def query_string():
    return urlencode(app.current_request.json_body)

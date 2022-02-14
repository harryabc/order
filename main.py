from flask import Flask, request, abort
import json
import requests

from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
 

@app.route('/api/order', methods=['POST'])
def create_order():
    goods_id = request.values.get('goods_id')
    num = request.values.get('num')
    order_id = str(goods_id) + '0002'

    data = {
        'status': 200,
        'message': '创建订单成功！',
        'order_id': order_id
    }
    res = jsonify(data)
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

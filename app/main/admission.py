u"""江西高招查询."""

from flask import request, jsonify
from app.main import main
import re
from app.spiders import filters


@main.route('/api/admission', methods=['POST'])
def admission():
    """To get the admission for high scholl students of JiangXi."""
    code = request.json.get('code')
    pid = request.json.get('sfzh')  # personal id
    code_re = re.compile(r'\d{10}$')
    pid_re = re.compile(r'\d{4}$')

    if code_re.match(code) and pid_re.match(pid):
        resp = filters(code, pid)
        return jsonify(resp)
    else:
        return jsonify({
            'message': u'请输入正确的信息',
            'status': 0
        })

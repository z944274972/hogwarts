# -*- coding: utf-8 -*-
# @Time     :  2021/1/24 17:26
# @Author   :  zhangyuxin
# @Email    :  zhangyuxin.aikebo@bytedance.com
# @File     :  mitmproxy_demo.py


from mitmproxy import http


class Counter:
    def request(flow: http.HTTPFlow) -> None:
        if "baidu" in flow.request.pretty_url :
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                b"xiix",  # (optional) content
                {"Content-Type": "text/html"}  # (optional) headers
            )

addons = [
    Counter()
]
#!/usr/bin/python2
# _*_coding:utf-8 _*_
from wsgiref.simple_server import make_server
def index(arg):
    # 返回一个含有html代码的字符串
    return "<h1>%s</h1>" %(arg)
def manage(arg):
    return arg
URLS = {
    "/index": index,
    "/manage": manage,
}
def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ['PATH_INFO']
    if url in URLS.keys():
        func_name = URLS[url]
        ret = func_name(url)
    else:
        ret = "404"
    return ret
if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    httpd.serve_forever()
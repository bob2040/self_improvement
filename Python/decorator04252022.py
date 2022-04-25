from dataclasses import dataclass


router_table = {}


def router(url):
    def outer(func):
        def inner():
            func()
        router_table[url] = inner
        return inner
    return outer


@router("index.html")
def index():
    print('Function index is running...')


@router("centre.html")
def centre():
    print('Function centre is running...')


@router("mail.html")
def mail():
    print('Function mail is running...')


def error():
    print('Error,No this function in the router_table.')


def request_url(url):
    func = error
    if url in router_table:
        func = router_table[url]
    func()


request_url("index.html")
request_url("centre.html")
request_url("mail.html")
request_url("login.html")



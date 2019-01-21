import base64, hashlib, hmac
from urllib import request

def base64_module():
    data = base64.b64encode(b'binary\x00string')
    print(data)

    url1 = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
    url2 = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
    print(url1)
    print(url2)


def hashlib_moudle():
    md5 = hashlib.md5()
    md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
    print(md5.hexdigest())

def hmac_module():
    message = b'Hello, world!'
    key = b'secret'
    h = hmac.new(key, message, digestmod='MD5')
    print(h.hexdigest())

def urllib_module():

    with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', data.decode('utf-8'))

def decode_Text():
    s = base64.de

def main():
    urllib_module()


if __name__ == "__main__":
    main()
# encoding=utf8

def save_img(imgLocate, ir):
    try:
        fp = open(imgLocate, 'wb')
        fp.write(ir.content)
        fp.close()
        return True
    except Exception as Err:
        print (Err)

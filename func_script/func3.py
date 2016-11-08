#coding: utf-8

def set_passline(passline):
    def cmp(val):
        if val >= passline:
            print ('Pass')
        else:
            print ('failed')
    return cmp

f_100 = set_passline(60)
f_150 = set_passline(90)
print f_100(89)
print f_150(50)

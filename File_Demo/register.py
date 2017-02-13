#encoding:utf-8

myfile= open("user.txt","a")
while True:
        account = raw_input("请输入账号：")
        password = raw_input("password:")
        if account == '':
            print '请输入账号'
            continue
        if password == '':
            print '请输入密码'
            continue
        str = "%s:%s" % (account,password)



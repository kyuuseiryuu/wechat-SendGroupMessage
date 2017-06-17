#coding=utf8
# 默认发送空消息，不会被好友发现，如果有消息的话就是群发消息了
message = '''

'''[1:-1]
# 默认发送间隔时间 1s，时间间隔太短容易被封，发所有消息都将会失败！
timeout = 1
# 下次是否自动登录不扫描二维码
auto_login = False       
# True:二维码在控制台中扫描;False:则将二维码图片下载下来扫描
enable_cmd_qr = False     
block_width = 2  

# 自动改备注
auto_set_alias = True

# 保存信息到指定文件夹
save_to_file = False
# 保存路径
pathname = 'info'

if __name__ == '__main__':
    print 'message:',message
    print 'timeout:',timeout
    print 'auto_login:',auto_login
    print 'enable_cmd_qr:',enable_cmd_qr
    print 'block_width',block_width
    print 'save_to_file',save_to_file
    print 'pathname',pathname

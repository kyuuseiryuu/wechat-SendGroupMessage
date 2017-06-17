#coding=utf8
import thread
import time
import os
try:
    import itchat
except:
    os.system('pip install itchat')
    import itchat
import config
from itchat.content import *

@itchat.msg_register(NOTE)
def on_note_msg(msg):
    NickName = msg.User.NickName
    UserName = msg.User.UserName
    RemarkName = msg.User.RemarkName
    name = RemarkName or NickName
    print '\n\nTO:',NickName,'\nTips:',msg.Content
    what = in_black_list_or_delete(msg.Content)
    if what and config.auto_set_alias:
        new_name = u'AAA_' + what + '.' + name
        print '\nOps~[',NickName,'] delete you.','auto set alias'
        print name,'=>',new_name,'\n'
        itchat.set_alias(UserName,new_name)

def in_black_list_or_delete(msg_content):
    if u'拒收' in msg_content:
        return u'拉黑'
    if u'发送朋友验证' in msg_content:
        return u'删除'
    return ''

def send_group_message(message,friends,timeout):
    friends_len = len(friends)
    for index in range(friends_len):
        UserName = friends[index]['UserName']
        NickName = friends[index]['NickName']
        info = str(index+1)+'/'+str(friends_len)+'\tTo:'+NickName
        if itchat.send_msg(msg=message, toUserName=UserName):
            info += '\tSUCCESS!'
        else:
            info += '\tFAILED!'
        print info
        if timeout:
            time.sleep(timeout)

def mkdir(path):
    if(os.path.isdir(path)):
        return
    os.mkdir(path)

def save_to_file(friends):
    mkdir(config.pathname)
    m = config.pathname + '/' + friends[0]['NickName']+".min.json"
    fm = open(m,'w+')
    fm.write('[\n')
    f_len = len(friends)
    for index in range(f_len):
        f = friends[index]
        s = {
            "NickName":f.NickName,
            "RemarkName":f.RemarkName,
            "City":f.City,
            "HeadImgUrl":f.HeadImgUrl,
            "Sex":f.Sex
        }
        print(u'NickName:%s\nRemark：%s\n----------' % (f.NickName,f.RemarkName))
        save_str = str(s).replace("'",'"').replace('u"','"')
        fm.write('\t' + save_str)
        if index + 1 < f_len:
            fm.write(',\n')
    fm.write('\n]')
    fm.close()

def start():
    auto_login = config.auto_login
    if config.enable_cmd_qr:
        itchat.auto_login(hotReload=auto_login,enableCmdQR=config.block_width)
    else:
        itchat.auto_login(hotReload=auto_login)
    thread.start_new_thread(itchat.run,())
    friends = itchat.get_friends(True) 
    print 'Total friends:',len(friends)-1
    print 'Starting...'
    itchat.send_msg(msg=u'正在检测，结束后将在此通知您.',toUserName='filehelper')
    if config.save_to_file:
        save_to_file(friends)
    send_group_message(config.message,friends[1:],config.timeout)   #不包括自己，0 是自己
    print 'Finally waiting...'
    time.sleep(3)
    print 'Completed! Exit after 3s.'
    time.sleep(3)
    itchat.send_msg(msg=u'检测完成！被删除的已备注，请在通讯录中查看~',toUserName='filehelper')
    itchat.logout()

if __name__ == '__main__':
    print 'core.py'


    
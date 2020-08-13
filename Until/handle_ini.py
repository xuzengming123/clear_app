from configparser import ConfigParser
import os
ConfigPath = os.path.abspath('../Config')

class HandleInit:
    def load_ini(self):
        '''
        加载
        :return:
        '''
        filePath = ConfigPath + '\server.ini'
        conf = ConfigParser()
        conf.read(filePath,encoding='utf-8')
        return conf

    def get_inivalue(self,key,node=None):
        '''
        获取ini文件的value
        :param key: key
        :param node: 节点
        :return:
        '''
        if node is None:
            node = 'server'
        conf = self.load_ini()
        try:
            data = conf.get(node,key)
        except Exception as e:
            print('没有获取到ini文件的值')
            data = None
        return data

handle_init = HandleInit()
if __name__ == '__main__':
    print(handle_init.get_inivalue('online_host','server'))
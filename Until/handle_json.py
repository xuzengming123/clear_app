import json


class HandleJson:
    def read_json(self,JsonFilePath):
        '''
        加载
        :param JsonFilePath: json文件路径
        :return:
        '''
        with open(JsonFilePath,encoding='utf-8') as f:
            data = json.load(f)
        return data

    def get_jsonvalue(self,JsonFilePath,key):
        '''
        获取json文件的值
        :param JsonFilePath:json文件路径
        :param key:key
        :return:
        '''
        data = self.read_json(JsonFilePath)
        if key:
            return data.get(key)
        else:
            return None

    def write_value(self,file_path,data):
        '''
        写入
        :param file_path:
        :param data:
        :return:
        '''
        data_value = json.dumps(data)
        with open(file_path, 'w') as f:
            f.write(data_value)

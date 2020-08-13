from Config import header




class HandleHeader:
    def add_to_header(self,key,value):
        common_header = header.headers
        common_header[key] = value
        return common_header

    def add_head(self,*key):
        a = key
        print(a)

'''
拿到追加header的数据，是字典格式，
追加到header里面'''


ahv = HandleHeader()
if __name__ == '__main__':

    headers = {'xxx':'bbb','ccc':'ddd'}
    # print(ahv.add_to_header('xzc','asd'))
    print(ahv.add_head(headers))
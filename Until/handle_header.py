from Config import header




class HandleHeader:
    def add_to_header(self,value):
        common_header = header.headers
        common_header.update(value)
        return common_header


'''
拿到追加header的数据，是字典格式，
追加到header里面'''


ath = HandleHeader()
if __name__ == '__main__':
    headers = {'xxx':'bbb','ccc':'ddd'}
    print(ath.add_to_header(headers))
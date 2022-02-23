import pandas as pd
import requests

# 设置经纬度，应用的ky, 搜索关键字 城市 页码
mylocation = "113.93041,22.53332"
myappkey = "e93c1fedee515eb39ffc141b708b1ff5"
myky = "舞蹈"
mycity = "深圳"
page_num = 1
myrad = 50000
# 网站链接
url1 = "https://restapi.amap.com/v3/place/around?" \
       "keywords="+myky + \
       "&city="+mycity + \
       "&key=" + myappkey + \
       "&location=" + mylocation + \
       "&radius=" + str(myrad) + \
       "&distance&page="


def get_info():
    page_list = []
    name_list = []
    add_list = []
    tel_list = []
    type_list = []
    for i in range(1, 101):
        page_num = str(i)
        page = requests.get(url=url1 + str(page_num))
        print(i)
        print(page)

        for info in page.json().get('pois'):

            # print(info.get('name'), info.get('address'), info.get('type'), info.get('tel'))
            page_list.append(i)
            name_list.append(info.get('name'))
            add_list.append(info.get('address'))
            tel_list.append(info.get('tel'))
            type_list.append(info.get('type'))

    df1 = pd.DataFrame({"页码": page_list, "名称": name_list, "类别": type_list, "地址": add_list, "电话": tel_list})
    df1.to_excel("1234.xlsx", index=False)


get_info()

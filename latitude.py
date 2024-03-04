
import requests
import json

def get_location_x_y(place):
    # place = input("请输入您要查询的地址")
    url = 'https://restapi.amap.com/v3/geocode/geo?parameters'
    parameters = {
        'key': '34a3919efd50bc3a8ed75ee6cf32069f',
        'address': '%s' % place
    }
    page_resource = requests.get(url, params=parameters)
    text = page_resource.text  # 获得数据是json格式
    data = json.loads(text)  # 把数据变成字典格式
    location = data["geocodes"][0]['location']
    return location


if __name__ == '__main__':
    print(get_location_x_y("西安电子科技大学"))
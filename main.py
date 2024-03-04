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
 print (location)
 return location

def main():
    from_place = input("请输入起始地址：")
    from_location = get_location_x_y(from_place)

    # Get location data for the destination
    to_place = input("请输入目的地：")
    to_location = get_location_x_y(to_place)

    url = "https://restapi.amap.com/v3/direction/driving?"

    parameters = {
        'key': '34a3919efd50bc3a8ed75ee6cf32069f',
        'origin': str(from_location),
        'destination': str(to_location),
        'output': 'json',               #返回值为json
        'strategy':'20',                #返回的结果会优先考虑高速路，并且会考虑路况躲避拥堵，与高德地图的“躲避拥堵&高速优先”策略一致
    }
    try:
        response = requests.get(url,params=parameters)
        data = json.loads(response.text)
        # print ('data',data)
        guidance = data['route']['paths'][0]['steps']
        print('guidance',guidance)
        poluline = data['route']['paths'][0]['steps']
        for i in guidance:
            instruction = i['instruction']
            print ('instruction',instruction)
        # for i in poluline:
        #     instruction = i['polyline']
        #     print(poluline)

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    main()

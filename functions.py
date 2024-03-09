import requests
import json
import os
template_html_path = r'D:\pythonProject\map\template.html'
map_html_path =  r'D:\pythonProject\map\map.html'
# template_html_path = r'D:\pythonProject\map\template.html'
# map_html_path = r'D:\pythonProject\map\map.html'

################################################################
# 输入名称place返回POI
def get_location_x_y(place):
    url = 'https://restapi.amap.com/v3/geocode/geo?parameters'
    parameters = {
        'key': '34a3919efd50bc3a8ed75ee6cf32069f',
        'address': '%s' % place
    }
    page_resource = requests.get(url, params=parameters)
    text = page_resource.text
    data = json.loads(text)
    location = data["geocodes"][0]['location']
    print(location)
    return location

def path(from_location_POI,to_location_POI):

    url = "https://restapi.amap.com/v3/direction/driving?"

    parameters = {
        'key': '34a3919efd50bc3a8ed75ee6cf32069f',
        'origin': str(from_location_POI),
        'destination': str(to_location_POI),
        'output': 'json',
        'strategy':'20',
    }
    try:
        response = requests.get(url, params=parameters)
        data = json.loads(response.text)
        guidance = data['route']['paths'][0]['steps']
        path = []
        for i in guidance:
            polyline = i['polyline']
            for point in polyline.split(';'):
                lng, lat = point.split(',')
                path.append([float(lng), float(lat)])

        return path

    except Exception as e:
        print(f"Error: {str(e)}")

def html_path(path_data,start_point,approach_point,end_point):
    with open(template_html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    path_content = ""
    start_path_content = ""
    end_path_content = ""
    approach_point_content = ""
    #遍历所有path信息，将规划路径的所有点写入
    print(path_data)
    for point in path_data:
        path_content += f"    new AMap.LngLat({point[0]}, {point[1]}),\n"
    html_content = html_content.replace('path_data', path_content)

    #写入途经点
    for point in approach_point:
        approach_point_content += f"    path.push([{point[0]}, {point[1]}]);\n"
    html_content = html_content.replace('approach_point_flag', approach_point_content)

    #写入起点
    start_path_content += f"    path.push([{start_point[0]}, {start_point[1]}]);\n"
    html_content = html_content.replace('start_point_flag', start_path_content)
    #写入终点
    end_path_content += f"    path.push([{end_point[0]}, {end_point[1]}]);\n"
    html_content = html_content.replace('end_point_flag', end_path_content)

    with open(map_html_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

def start_point_func (start_point_0, start_point):
    with open(template_html_path, 'r', encoding='utf-8') as file:

        html_content = file.read()

    start_path_content = ""
    start_path_content += f"    path.push([{start_point[0]}, {start_point[1]}]);\n"
    html_content = html_content.replace('start_point_flag',start_path_content)

    with open('map.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

def end_point (end_point_0, end_point_1):
    with open(template_html_path, 'r', encoding='utf-8') as file:

        html_content = file.read()

    end_path_content = ""

    end_path_content += f"    path.push([{end_point_0}, {end_point_1}]);\n"

    html_content = html_content.replace('end_point_flag',end_path_content)

    with open('map.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

def approach_point (approach_point_data):
    with open(template_html_path, 'r', encoding='utf-8') as file:

        html_content = file.read()

    approach_path_content = ""
    for point in approach_point_data:
        approach_path_content += f"     path.push([{point[0]}, {point[1]}),\n"

    html_content = html_content.replace('approach_point_flag',approach_path_content)

    with open('map.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

def openHtml():
    cmd_str = "start chrome.exe http://localhost:63342/map/map.html?_ijt=s9rk442m0finm6phts9jdrlmjo&_ij_reload=RELOAD_ON_SAVE"
    f = os.popen(cmd_str)
    f.close()
import requests, json
def get_data(city_name, pro_name):
    """
    返回四天内的天气预报数据
    :param city_name: str,根据传入的城市名字来输出对应的城天气数据
    :param pro_name:  str,根据转入的区域名字来输出对应的城市区域天气数据
    """
    if city_name=="广州":
        data01={"荔湾区":440103,"越秀区":440104,"海珠区":440104,"天河区":440106,"白云区":440111,"黄埔区":440112,"番禺区":440113,"花都区":440114,"南沙区":440115,"从化区":440117,"增城区":440118}
        if pro_name in data01.keys():
            return json.loads(requests.get(f"https://restapi.amap.com/v3/weather/weatherInfo?city={data01[pro_name]}&key=f90d437f76b853c77ceb58b8a51b0f5f&extensions=all").text)

    elif city_name=="北京":
        data01 = {"东城区":110101, "西城区":110102, "朝阳区":110105, "丰台区":110106, "石景山区":110107, "海淀区":110108, "门头沟区":110109, "房山区":110111, "通州区":110112,
                  "顺义区":110113, "昌平区":110114, "大兴区":110115, "怀柔区":110116, "平谷区":110117, "密云区":110118, "延庆区":110119}
        if pro_name in data01.keys():
            return json.loads(requests.get(f"https://restapi.amap.com/v3/weather/weatherInfo?city={data01[pro_name]}&key=f90d437f76b853c77ceb58b8a51b0f5f&extensions=all").text)

    elif city_name=="上海":
        data01 = {"黄浦区":310101, "徐汇区":310104, "长宁区":310105, "静安区":310106, "普陀区":310107, "虹口区":310109, "杨浦区":310110, "闵行区":310112, "宝山区":310113, "嘉定区":310114,
                  "浦东新区":310115, "金山区":310116, "松江区":310117, "青浦区":310118, "奉贤区":310120, "崇明区":310151}
        if pro_name in data01.keys():
            return json.loads(requests.get(f"https://restapi.amap.com/v3/weather/weatherInfo?city={data01[pro_name]}&key=f90d437f76b853c77ceb58b8a51b0f5f&extensions=all").text)

    elif city_name=="成都":
        data01 = {"锦江区":510104, "青羊区":510105, "金牛区":510106, "武侯区":510107, "成华区":510108, "龙泉驿区":510112, "青白江区":510113, "新都区":510114, "温江区":510115,
                  "双流区":510116, "郫都区":510117, "金堂县":510121, "大邑县":510129, "蒲江县":510131, "新津区":510118, "都江堰市":510181, "彭州市":510182, "邛崃市":510183, "崇州市":510184}
        if pro_name in data01.keys():
            return json.loads(requests.get(f"https://restapi.amap.com/v3/weather/weatherInfo?city={data01[pro_name]}&key=f90d437f76b853c77ceb58b8a51b0f5f&extensions=all").text)

def api(code):
    url = "https://eolink.o.apispace.com/34324/air/v001/aqi"
    payload = {"areacode": code}
    headers = {"X-APISpace-Token": "7vh9hi92lgvl25wkrmqhvxdqxrb29n4q"}
    response = json.loads(requests.request("GET", url, params=payload, headers=headers).text)
    return response["result"]["realtimeAqi"]["pm25"]

def get_pm(city_name,pro_name):
    """
    返回当天内的pm2.5数据
    :param city_name: str,根据传入的城市名字来输出对应的城天气数据
    :param pro_name:  str,根据转入的区域名字来输出对应的城市区域天气数据
    """
    if city_name == "广州":
        data01={"荔湾区":101280106,"越秀区":101280107,"海珠区":101280108,"天河区":101280109,"白云区":101280110,"黄埔区":101280111,"番禺区":101280102,"花都区":101280105,"南沙区":101280112,"从化区":101280103,"增城区":101280104}
        return api(data01[pro_name])

    if city_name == "北京":
        data01 = {"东城区":101011600,"西城区":101011700,"朝阳区":101010300,"丰台区":101010900,
             "石景山区":101011000,"海淀区":101010200,"门头沟区":101011400,"房山区":101011200,"通州区":101010600,
             "顺义区":101010400,"昌平区":101010700,"大兴区":101011100,"怀柔区":101010500,"平谷区":101011500,
             "密云区":101011300,"延庆区":101010800}
        return api(data01[pro_name])

    if city_name == "上海":
        data01 = {"黄浦区":101020400,"徐汇区":101021200,
             "长宁区":101021300,"静安区":101021400,"普陀区":101021500,"虹口区":101021600,"杨浦区":101021700,
             "闵行区":101020200,"宝山区":101020300,"嘉定区":101020500,"浦东新区":101020600,"金山区":101020700,
             "松江区":101020900,"青浦区":101020800,"奉贤区":101021000,"崇明区":101021100}
        return api(data01[pro_name])

    if city_name == "成都":
        data01 = {"锦江区":101270116,"青羊区":101270117,"金牛区":101270118,
             "武侯区":101270119,"成华区":101270120,"龙泉驿区":101270102,"青白江区":101270115,"新都区":101270103,
             "温江区":101270104,"双流区":101270106,"郫都区":101270107,"金堂县":101270105,"大邑县":101270108,
             "蒲江区":101270109,"新津区":101270110,"都江堰市":101270111,"彭州市":101270112,"邛崃市":101270113,
             "崇州市":101270114}
        return api(data01[pro_name])

def get_rh(city_name,pro_name):
    if city_name=="广州":
        data01={"荔湾区":440103,"越秀区":440104,"海珠区":440104,"天河区":440106,"白云区":440111,"黄埔区":440112,"番禺区":440113,"花都区":440114,"南沙区":440115,"从化区":440117,"增城区":440118}
        if pro_name in data01.keys():
            return json.loads(requests.get(f"https://restapi.amap.com/v3/weather/weatherInfo?city={data01[pro_name]}&key=f90d437f76b853c77ceb58b8a51b0f5f").text)["lives"][0]["humidity"]

    elif city_name=="北京":
        data01 = {"东城区":110101, "西城区":110102, "朝阳区":110105, "丰台区":110106, "石景山区":110107, "海淀区":110108, "门头沟区":110109, "房山区":110111, "通州区":110112,
                  "顺义区":110113, "昌平区":110114, "大兴区":110115, "怀柔区":110116, "平谷区":110117, "密云区":110118, "延庆区":110119}
        if pro_name in data01.keys():
            return json.loads(requests.get(f"https://restapi.amap.com/v3/weather/weatherInfo?city={data01[pro_name]}&key=f90d437f76b853c77ceb58b8a51b0f5f").text)["lives"][0]["humidity"]

    elif city_name=="上海":
        data01 = {"黄浦区":310101, "徐汇区":310104, "长宁区":310105, "静安区":310106, "普陀区":310107, "虹口区":310109, "杨浦区":310110, "闵行区":310112, "宝山区":310113, "嘉定区":310114,
                  "浦东新区":310115, "金山区":310116, "松江区":310117, "青浦区":310118, "奉贤区":310120, "崇明区":310151}
        if pro_name in data01.keys():
            return json.loads(requests.get(f"https://restapi.amap.com/v3/weather/weatherInfo?city={data01[pro_name]}&key=f90d437f76b853c77ceb58b8a51b0f5f").text)["lives"][0]["humidity"]

    elif city_name=="成都":
        data01 = {"锦江区":510104, "青羊区":510105, "金牛区":510106, "武侯区":510107, "成华区":510108, "龙泉驿区":510112, "青白江区":510113, "新都区":510114, "温江区":510115,
                  "双流区":510116, "郫都区":510117, "金堂县":510121, "大邑县":510129, "蒲江县":510131, "新津区":510118, "都江堰市":510181, "彭州市":510182, "邛崃市":510183, "崇州市":510184}
        if pro_name in data01.keys():
            return json.loads(requests.get(f"https://restapi.amap.com/v3/weather/weatherInfo?city={data01[pro_name]}&key=f90d437f76b853c77ceb58b8a51b0f5f").text)["lives"][0]["humidity"]
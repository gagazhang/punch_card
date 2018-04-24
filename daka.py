#!/usr/bin python3
# -*- coding: utf-8 -*-
import requests
import json

def daka_function():
    url = "https://iflyapp.iflytek.com:6443/AttendanceService/iflytekservices/Client/AttendanceByiFly"
    headers = {"Content-Type":"application/json; charset=UTF-8","User-Agent":"okhttp/3.8.1"}
    # data={"IMEI":"861337038437962","UserID":"4XkAEXpNSh2uhrqeGZLh8IDvfe0=","OpeType":"Client010","TimeStamp":"1524536187235","PassWord":"2rWjy01VIET3P30nkapB0Q==","UserAccount":"qsfu","Token":"6veBC.gVGoVu4D9khqRVxMj2gzm2yid8s3gLuzVCZFZhIV62O1nIULIPV3Wg4eNTqY8vIkpx0_fYZrEORCeVsFzeHU0oh7uRDnD0vLtwQzQ="}
    data={"OpeType":"Client005","AuthID":"a7c23015049547e5bcc3da4a494c002a","UserName":"付秋实","UserAccount":"qsfu","VirtualEnable":"0","LngLat":"kDhe5vLDM6C.CnnhXkY52ElnJP76Ph8P4WS34sEminA=","TimeStamp":"1524552322857","Token":"6veBC.gVGoVu4D9khqRVxMj2gzm2yid8s3gLuzVCZFZhIV62O1nIULIPV3Wg4eNTqY8vIkpx0_fYZrEORCeVsFzeHU0oh7uRDnD0vLtwQzQ=","UserID":"4XkAEXpNSh2uhrqeGZLh8IDvfe0=","IMEI":"861337038437962","OrgName":"知学产品管理部知学宝产品线（待封存）","UserCode":"20130079","PointType":"6","AppVersion":"2.0.1005","PhoneType":"Android","AttendanceAreaID":"29"}
    response = requests.post(url=url,headers=headers,data=json.dumps(data),verify=False)
    print(response.text)
    # print(json.dumps(data))



if __name__ == '__main__':
    daka_function()
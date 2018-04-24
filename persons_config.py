#!/usr/bin python3
# -*- coding: utf-8 -*-

'''
打卡的人员列表维护


个人打卡的数据示例如下：

"AppVersion":"2.0.1005",
"AreaCode":"",
"AttendanceAreaID":"29",
"AuthID":"a7c23015049547e5bcc3da4a494c002a",
"IMEI":"861337038437962",
"LngLat":"kDhe5vLDM6C.CnnhXkY52ElnJP76Ph8P4WS34sEminA=",
"OpeType":"Client005",
"OrgName":"知学产品管理部知学宝产品线（待封存）",
"PhoneType":"Android",
"PointType":"6",
"TimeStamp":"1524552322857",
"Token":"6veBC.gVGoVu4D9khqRVxMj2gzm2yid8s3gLuzVCZFZhIV62O1nIULIPV3Wg4eNTqY8vIkpx0_fYZrEORCeVsFzeHU0oh7uRDnD0vLtwQzQ=",
"UserAccount":"qsfu",
"UserCode":"20130079",
"UserID":"4XkAEXpNSh2uhrqeGZLh8IDvfe0=",
"UserName":"付秋实",
"VirtualEnable":"0"
'''

_qsfu = {
    "AppVersion":"2.0.1005",
    "AreaCode":"",
    "AttendanceAreaID":"29",
    "AuthID":"a7c23015049547e5bcc3da4a494c002a",
    "IMEI":"861337038437962",
    "LngLat":"kDhe5vLDM6C.CnnhXkY52ElnJP76Ph8P4WS34sEminA=",
    "OpeType":"Client005",
    "OrgName":"知学产品管理部知学宝产品线（待封存）",
    "PhoneType":"Android",
    "PointType":"6",
    "TimeStamp":"1524552322857",
    "Token":"6veBC.gVGoVu4D9khqRVxMj2gzm2yid8s3gLuzVCZFZhIV62O1nIULIPV3Wg4eNTqY8vIkpx0_fYZrEORCeVsFzeHU0oh7uRDnD0vLtwQzQ=",
    "UserAccount":"qsfu",
    "UserCode":"20130079",
    "UserID":"4XkAEXpNSh2uhrqeGZLh8IDvfe0=",
    "UserName":"付秋实",
    "VirtualEnable":"0"
}

_weizhang4 = {
    "AppVersion":"1.0.1014",
    "AreaCode":"08",
    "AttendanceAreaID":"29",
    "AuthID":"16af029edcf14aaca43027e2b9e96f23",
    "IMEI":"868217030274931",
    "LngLat":"LrOeCs.J29ld_ak_.cTseBY0tnYYKhVD9XzwLzsqZEU=",
    "OpeType":"Client005",
    "OrgName":"知学产品管理部知学宝产品线（待封存）",
    "PhoneType":"Android",
    "PointType":"6",
    "TimeStamp":"1524562314918",
    "Token":"Ce18TeiwrOUlkXbOV3qHRnBAsKH91InZSW0UmWrkna2B5Vj_pKDeksng2IflKP9CTMOPvO0eFniA95kU1s2KdrqbOWqloZxuMRC6B6SCnxw=",
    "UserAccount":"weizhang4",
    "UserCode":"20120014",
    "UserID":"ZjyO22L2QoeKK26k2JCxGIDvfe0=",
    "UserName":"张伟",
    "VirtualEnable":"0"
}

person_list=[_weizhang4]

if __name__=="__main__":
    print(person_list)
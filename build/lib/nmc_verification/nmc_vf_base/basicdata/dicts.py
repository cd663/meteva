#!/usr/bin/python3.6
# -*- coding:UTF-8 -*-

gds_station_data_element_name_id = {
    "经度":1,
    "纬度":2,
    "测站高度":3,
    "测站级别（short）":4,
    "测站类型（short）":5,
    "气压传感器海拔高度":6,
    "温湿传感器离地面高度":7,
    "温湿传感器距水面高度":8,
    "风速传感器距地面高度":9,
    "风传感器距甲板平台高度":10,
    "风速传感器距水面高度":11,
    "移动平台移动方向":12,
    "移动平台移动速度":13,
    "海盐传感器距海面深度":14,
    "浪高传感器距海面高度":15,
    "浮标方位":16,
    "总水深":17,
    "海面/水面以下深度":18,
    "船面距海面高度":19,
    "方位或方位角":20,
    "字符型站名":21,
    "风向":201,
    "风速":203,
    "1分钟平均风向":205,
    "1分钟平均风速":207,
    "2分钟平均风向":209,
    "2分钟平均风速":211,
    "10分钟平均风向":213,
    "10分钟平均风速":215,
    "最大风速的风向":217,
    "最大风速":219,
    "瞬时风向":221,
    "瞬时风速":223,
    "极大风速的风向":225,
    "极大风速":227,
    "过去6小时极大瞬时风速的风向":229,
    "过去6小时极大瞬时风速":231,
    "过去12小时极大瞬时风速的风向":233,
    "过去12小时极大瞬时风速":235,
    "风力(short)":237,
    "海平面气压":401,
    "3小时变压":403,
    "24小时变压":405,
    "本站气压":407,
    "最高气压":409,
    "最低气压":411,
    "气压":413,
    "日平均气压":415,
    "日平均海平面气压":417,
    "高度（探空）":419,
    "位势高度（探空）":421,
    "温度":601,
    "最高气温":603,
    "最低气温":605,
    "24小时变温":607,
    "过去24小时最高气温":609,
    "过去24小时最低气温":611,
    "日平均气温":613,
    "露点温度":801,
    "温度露点差":803,
    "相对湿度":805,
    "最小相对湿度":807,
    "日平均相对湿度":809,
    "水汽压":811,
    "日平均水汽压":813,
    "降水量":1001,
    "1小时降水":1003,
    "3小时降水":1005,
    "6小时降水":1007,
    "12小时降水":1009,
    "24小时降水":1011,
    "日总降水":1013,
    "20-08时降水量":1015,
    "08-20时降水量":1017,
    "20-20时降水量":1019,
    "08-08时降水量":1021,
    "蒸发":1023,
    "蒸发（大型）":1025,
    "可降水分（预报降水量）":1027,
    "1分钟平均水平能见度":1201,
    "10分钟平均水平能见度":1203,
    "最小水平能见度":1205,
    "水平能见度（人工）":1207,
    "总云量":1401,
    "低云量":1403,
    "云底高度":1405,
    "低云状（short）":1407,
    "中云状（short）":1409,
    "高云状（short）":1411,
    "日平均总云量":1413,
    "日平均低云量":1415,
    "云量(低云或中云)":1417,
    "云类型(short)":1419,
    "现在天气（short）":1601,
    "过去天气1（short）":1603,
    "过去天气2（short）":1605,
    "龙卷类型（short）":1801,
    "龙卷所在方位（short）":1803,
    "最大冰雹直径":1805,
    "雷暴（short）":1807,
    "电流强度（闪电定位）":1809,
    "地面温度":2001,
    "最高地面温度":2003,
    "最低地面温度":2005,
    "过去12小时最低地面温度":2007,
    "5cm地温":2009,
    "10cm地温":2011,
    "15cm地温":2013,
    "20cm地温":2015,
    "40cm地温":2017,
    "80cm地温":2019,
    "160cm地温":2021,
    "320cm地温":2023,
    "草面（雪面）温度":2025,
    "草面（雪面）最高温度":2027,
    "草面（雪面）最低温度":2029,
    "日平均地面温度":2031,
    "日平均5cm地温":2033,
    "日平均10cm地温":2035,
    "日平均15cm地温":2037,
    "日平均20cm地温":2039,
    "日平均40cm地温":2041,
    "日平均80cm地温":2043,
    "日平均160cm地温":2045,
    "日平均320cm地温":2047,
    "日平均草面（雪面）温度":2049,
    "地面状态（short）":2201,
    "积雪深度":2203,
    "雪压":2205,
    "电线积冰直径":2207,
    "电线积冰-现象（short）":2209,
    "电线积冰-南北方向直径":2211,
    "电线积冰-南北方向厚度":2213,
    "电线积冰-南北方向重量":2215,
    "电线积冰-东西方向直径":2217,
    "电线积冰-东西方向厚度":2219,
    "电线积冰-东西方向重量":2221,
    "船上结冰原因（short）":2223,
    "船上结冰厚度":2225,
    "船上结冰速度（short）":2227,
    "海冰密集度（short）":2229,
    "冰情发展（short）":2231,
    "冰总量和类型（short）":2233,
    "冰缘方位":2235,
    "冰情（short）":2237,
    "最高气压出现时间":10001,
    "最低气压出现时间":10003,
    "最高气温出现时间":10005,
    "最低气温出现时间":10007,
    "最小相对湿度出现时间":10009,
    "最大风速出现时间":10011,
    "极大风速出现时间":10013,
    "最高地面温度出现时间":10015,
    "最低地面温度出现时间":10017,
    "草面（雪面）最低温度出现时间":10019,
    "草面（雪面）最高温度出现时间":10021,
    "最小水平能见度出现时间":10023,
    "天气出现时间":10025,
    "海表最高温度出现时间":10027,
    "海表最低温度出现时间":10029,
    "最大波高出现时间":10031,
    "风速表类型":2401,
    "湿球温度测量方法":2403,
    "海面温度测量方法":2405,
    "洋流测量方法":2407,
    "气压倾向特征":2409,
    "海面温度":2601,
    "湿球温度":2603,
    "海面盐度":2605,
    "海表最高温度":2607,
    "海表最低温度":2609,
    "海水温度":2611,
    "海水盐度":2613,
    "海面海流方向":2801,
    "海面海流速度":2803,
    "洋流方向和速度的平均周期（short）":2805,
    "表层海洋面流速":2807,
    "表层海洋面波向":2809,
    "海流方向":2811,
    "海流速度":2813,
    "波浪方向":3001,
    "波浪周期":3003,
    "波浪高度":3005,
    "风浪方向":3007,
    "风浪周期":3009,
    "风浪高度":3011,
    "第一涌浪方向":3013,
    "第一涌浪周期":3015,
    "第一涌浪高度":3017,
    "第二涌浪方向":3019,
    "第二涌浪周期":3021,
    "第二涌浪高度":3023,
    "有效波高":3025,
    "有效波高的周期":3027,
    "平均波高":3029,
    "平均波周期":3031,
    "最大波高":3033,
    "最大波高的周期":3035,
    "人工测量浪高":3037,
    "仪器测量浪高":3039,
    "浪级代码(short)":3041
}

class m1_value_column:
    站号 = 0
    经度 = 1
    纬度 = 2
    拔海高度 = 3
    站点级别 = 4
    总云量 =5
    风向 = 6
    风速 = 7
    气压 = 8
    小时变压 = 9
    过去天气1 = 10
    过去天气2 =11
    降水6小时 =12
    低云状 =13
    低云量 =14
    低云高 =15
    露点 =16
    能见度 =17
    现在天气 =18
    温度 =19
    中云状 =20
    高云状 =21
    标志1 =22
    标志2 =23
    日变温 = 24
    日变压 =25

class m2_value_column:
    站号 = 0
    经度 = 1
    纬度 = 2
    拔海高度 = 3
    位势高度 = 4
    温度 = 5
    温度露点差 = 6
    风向 = 7
    风速 = 8

class m8_value_column:
    站号 = 0
    经度 = 1
    纬度 = 2
    拔海高度 = 3
    天气现象1 = 4
    风向1 = 5
    风速1 = 6
    最低温度 = 7
    最高温度 = 8
    天气现象2 = 9
    风向2 = 10
    风速2 = 11

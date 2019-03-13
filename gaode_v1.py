# -*- coding: utf-8 -*-
import requests
import re
import json
import pandas as pd
import os
import math
from bs4 import BeautifulSoup
import time
from selenium import webdriver
# chrome_options = webdriver.ChromeOptions()
# driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
# arealist = []
# host = 'https://ditu.amap.com/search?query=%E9%85%92%E5%BA%97&city=310000&geoobj=121.443993%7C31.166179%7C121.454293%7C31.179398&_src=around&zoom=16'
# driver.get(host)
# time.sleep(1)
# html = driver.page_source
# soup = BeautifulSoup(html,'lxml')
# contents = soup.select('li')
# # contents = soup.find(class_='city-province').select('li')
# for content in contents:
#     try:
#         code = content.attrs['adcode']
#         aera = content.text
#         jsondata = {}
#         jsondata['code'] = code
#         jsondata['aera'] = aera
#         arealist.append(jsondata)
#     except:
#         continue
# print(arealist)
#
# driver.close()


arealist = [
  {
    'aera': '全国',
    'code': '100000'
  },
  {
    'aera': '北京',
    'code': '110000'
  },
  {
    'aera': '天津',
    'code': '120000'
  },
  {
    'aera': '沈阳',
    'code': '210100'
  },
  {
    'aera': '大连',
    'code': '210200'
  },
  {
    'aera': '上海',
    'code': '310000'
  },
  {
    'aera': '南京',
    'code': '320100'
  },
  {
    'aera': '苏州',
    'code': '320500'
  },
  {
    'aera': '杭州',
    'code': '330100'
  },
  {
    'aera': '青岛',
    'code': '370200'
  },
  {
    'aera': '郑州',
    'code': '410100'
  },
  {
    'aera': '武汉',
    'code': '420100'
  },
  {
    'aera': '长沙',
    'code': '430100'
  },
  {
    'aera': '广州',
    'code': '440100'
  },
  {
    'aera': '深圳',
    'code': '440300'
  },
  {
    'aera': '重庆',
    'code': '500000'
  },
  {
    'aera': '成都',
    'code': '510100'
  },
  {
    'aera': '西安',
    'code': '610100'
  },
  {
    'aera': '香港',
    'code': '810000'
  },
  {
    'aera': '澳门',
    'code': '820000'
  },
  {
    'aera': '合肥',
    'code': '340100'
  },
  {
    'aera': '芜湖',
    'code': '340200'
  },
  {
    'aera': '蚌埠',
    'code': '340300'
  },
  {
    'aera': '淮南',
    'code': '340400'
  },
  {
    'aera': '马鞍山',
    'code': '340500'
  },
  {
    'aera': '淮北',
    'code': '340600'
  },
  {
    'aera': '铜陵',
    'code': '340700'
  },
  {
    'aera': '安庆',
    'code': '340800'
  },
  {
    'aera': '黄山',
    'code': '341000'
  },
  {
    'aera': '滁州',
    'code': '341100'
  },
  {
    'aera': '阜阳',
    'code': '341200'
  },
  {
    'aera': '宿州',
    'code': '341300'
  },
  {
    'aera': '六安',
    'code': '341500'
  },
  {
    'aera': '亳州',
    'code': '341600'
  },
  {
    'aera': '池州',
    'code': '341700'
  },
  {
    'aera': '宣城',
    'code': '341800'
  },
  {
    'aera': '福州',
    'code': '350100'
  },
  {
    'aera': '厦门',
    'code': '350200'
  },
  {
    'aera': '莆田',
    'code': '350300'
  },
  {
    'aera': '三明',
    'code': '350400'
  },
  {
    'aera': '泉州',
    'code': '350500'
  },
  {
    'aera': '漳州',
    'code': '350600'
  },
  {
    'aera': '南平',
    'code': '350700'
  },
  {
    'aera': '龙岩',
    'code': '350800'
  },
  {
    'aera': '宁德',
    'code': '350900'
  },
  {
    'aera': '广州',
    'code': '440100'
  },
  {
    'aera': '韶关',
    'code': '440200'
  },
  {
    'aera': '深圳',
    'code': '440300'
  },
  {
    'aera': '珠海',
    'code': '440400'
  },
  {
    'aera': '汕头',
    'code': '440500'
  },
  {
    'aera': '佛山',
    'code': '440600'
  },
  {
    'aera': '江门',
    'code': '440700'
  },
  {
    'aera': '湛江',
    'code': '440800'
  },
  {
    'aera': '茂名',
    'code': '440900'
  },
  {
    'aera': '肇庆',
    'code': '441200'
  },
  {
    'aera': '惠州',
    'code': '441300'
  },
  {
    'aera': '梅州',
    'code': '441400'
  },
  {
    'aera': '汕尾',
    'code': '441500'
  },
  {
    'aera': '河源',
    'code': '441600'
  },
  {
    'aera': '阳江',
    'code': '441700'
  },
  {
    'aera': '清远',
    'code': '441800'
  },
  {
    'aera': '东莞',
    'code': '441900'
  },
  {
    'aera': '中山',
    'code': '442000'
  },
  {
    'aera': '潮州',
    'code': '445100'
  },
  {
    'aera': '揭阳',
    'code': '445200'
  },
  {
    'aera': '云浮',
    'code': '445300'
  },
  {
    'aera': '南宁',
    'code': '450100'
  },
  {
    'aera': '柳州',
    'code': '450200'
  },
  {
    'aera': '桂林',
    'code': '450300'
  },
  {
    'aera': '梧州',
    'code': '450400'
  },
  {
    'aera': '北海',
    'code': '450500'
  },
  {
    'aera': '防城港',
    'code': '450600'
  },
  {
    'aera': '钦州',
    'code': '450700'
  },
  {
    'aera': '贵港',
    'code': '450800'
  },
  {
    'aera': '玉林',
    'code': '450900'
  },
  {
    'aera': '百色',
    'code': '451000'
  },
  {
    'aera': '贺州',
    'code': '451100'
  },
  {
    'aera': '河池',
    'code': '451200'
  },
  {
    'aera': '来宾',
    'code': '451300'
  },
  {
    'aera': '崇左',
    'code': '451400'
  },
  {
    'aera': '贵阳',
    'code': '520100'
  },
  {
    'aera': '六盘水',
    'code': '520200'
  },
  {
    'aera': '遵义',
    'code': '520300'
  },
  {
    'aera': '安顺',
    'code': '520400'
  },
  {
    'aera': '毕节',
    'code': '520500'
  },
  {
    'aera': '铜仁',
    'code': '520600'
  },
  {
    'aera': '黔西南布依族苗族自治州',
    'code': '522300'
  },
  {
    'aera': '黔东南苗族侗族自治州',
    'code': '522600'
  },
  {
    'aera': '黔南布依族苗族自治州',
    'code': '522700'
  },
  {
    'aera': '兰州',
    'code': '620100'
  },
  {
    'aera': '嘉峪关',
    'code': '620200'
  },
  {
    'aera': '金昌',
    'code': '620300'
  },
  {
    'aera': '白银',
    'code': '620400'
  },
  {
    'aera': '天水',
    'code': '620500'
  },
  {
    'aera': '武威',
    'code': '620600'
  },
  {
    'aera': '张掖',
    'code': '620700'
  },
  {
    'aera': '平凉',
    'code': '620800'
  },
  {
    'aera': '酒泉',
    'code': '620900'
  },
  {
    'aera': '庆阳',
    'code': '621000'
  },
  {
    'aera': '定西',
    'code': '621100'
  },
  {
    'aera': '陇南',
    'code': '621200'
  },
  {
    'aera': '临夏回族自治州',
    'code': '622900'
  },
  {
    'aera': '甘南藏族自治州',
    'code': '623000'
  },
  {
    'aera': '石家庄',
    'code': '130100'
  },
  {
    'aera': '唐山',
    'code': '130200'
  },
  {
    'aera': '秦皇岛',
    'code': '130300'
  },
  {
    'aera': '邯郸',
    'code': '130400'
  },
  {
    'aera': '邢台',
    'code': '130500'
  },
  {
    'aera': '保定',
    'code': '130600'
  },
  {
    'aera': '张家口',
    'code': '130700'
  },
  {
    'aera': '承德',
    'code': '130800'
  },
  {
    'aera': '沧州',
    'code': '130900'
  },
  {
    'aera': '廊坊',
    'code': '131000'
  },
  {
    'aera': '衡水',
    'code': '131100'
  },
  {
    'aera': '哈尔滨',
    'code': '230100'
  },
  {
    'aera': '齐齐哈尔',
    'code': '230200'
  },
  {
    'aera': '鸡西',
    'code': '230300'
  },
  {
    'aera': '鹤岗',
    'code': '230400'
  },
  {
    'aera': '双鸭山',
    'code': '230500'
  },
  {
    'aera': '大庆',
    'code': '230600'
  },
  {
    'aera': '伊春',
    'code': '230700'
  },
  {
    'aera': '佳木斯',
    'code': '230800'
  },
  {
    'aera': '七台河',
    'code': '230900'
  },
  {
    'aera': '牡丹江',
    'code': '231000'
  },
  {
    'aera': '黑河',
    'code': '231100'
  },
  {
    'aera': '绥化',
    'code': '231200'
  },
  {
    'aera': '大兴安岭',
    'code': '232700'
  },
  {
    'aera': '郑州',
    'code': '410100'
  },
  {
    'aera': '开封',
    'code': '410200'
  },
  {
    'aera': '洛阳',
    'code': '410300'
  },
  {
    'aera': '平顶山',
    'code': '410400'
  },
  {
    'aera': '安阳',
    'code': '410500'
  },
  {
    'aera': '鹤壁',
    'code': '410600'
  },
  {
    'aera': '新乡',
    'code': '410700'
  },
  {
    'aera': '焦作',
    'code': '410800'
  },
  {
    'aera': '濮阳',
    'code': '410900'
  },
  {
    'aera': '许昌',
    'code': '411000'
  },
  {
    'aera': '漯河',
    'code': '411100'
  },
  {
    'aera': '三门峡',
    'code': '411200'
  },
  {
    'aera': '南阳',
    'code': '411300'
  },
  {
    'aera': '商丘',
    'code': '411400'
  },
  {
    'aera': '信阳',
    'code': '411500'
  },
  {
    'aera': '周口',
    'code': '411600'
  },
  {
    'aera': '驻马店',
    'code': '411700'
  },
  {
    'aera': '济源',
    'code': '419001'
  },
  {
    'aera': '武汉',
    'code': '420100'
  },
  {
    'aera': '黄石',
    'code': '420200'
  },
  {
    'aera': '十堰',
    'code': '420300'
  },
  {
    'aera': '宜昌',
    'code': '420500'
  },
  {
    'aera': '襄阳',
    'code': '420600'
  },
  {
    'aera': '鄂州',
    'code': '420700'
  },
  {
    'aera': '荆门',
    'code': '420800'
  },
  {
    'aera': '孝感',
    'code': '420900'
  },
  {
    'aera': '荆州',
    'code': '421000'
  },
  {
    'aera': '黄冈',
    'code': '421100'
  },
  {
    'aera': '咸宁',
    'code': '421200'
  },
  {
    'aera': '随州',
    'code': '421300'
  },
  {
    'aera': '恩施土家族苗族自治州',
    'code': '422800'
  },
  {
    'aera': '仙桃',
    'code': '429004'
  },
  {
    'aera': '潜江',
    'code': '429005'
  },
  {
    'aera': '天门',
    'code': '429006'
  },
  {
    'aera': '神农架林区',
    'code': '429021'
  },
  {
    'aera': '长沙',
    'code': '430100'
  },
  {
    'aera': '株洲',
    'code': '430200'
  },
  {
    'aera': '湘潭',
    'code': '430300'
  },
  {
    'aera': '衡阳',
    'code': '430400'
  },
  {
    'aera': '邵阳',
    'code': '430500'
  },
  {
    'aera': '岳阳',
    'code': '430600'
  },
  {
    'aera': '常德',
    'code': '430700'
  },
  {
    'aera': '张家界',
    'code': '430800'
  },
  {
    'aera': '益阳',
    'code': '430900'
  },
  {
    'aera': '郴州',
    'code': '431000'
  },
  {
    'aera': '永州',
    'code': '431100'
  },
  {
    'aera': '怀化',
    'code': '431200'
  },
  {
    'aera': '娄底',
    'code': '431300'
  },
  {
    'aera': '湘西土家族苗族自治州',
    'code': '433100'
  },
  {
    'aera': '海口',
    'code': '460100'
  },
  {
    'aera': '三亚',
    'code': '460200'
  },
  {
    'aera': '三沙',
    'code': '460300'
  },
  {
    'aera': '儋州',
    'code': '460400'
  },
  {
    'aera': '长春',
    'code': '220100'
  },
  {
    'aera': '吉林',
    'code': '220200'
  },
  {
    'aera': '四平',
    'code': '220300'
  },
  {
    'aera': '辽源',
    'code': '220400'
  },
  {
    'aera': '通化',
    'code': '220500'
  },
  {
    'aera': '白山',
    'code': '220600'
  },
  {
    'aera': '松原',
    'code': '220700'
  },
  {
    'aera': '白城',
    'code': '220800'
  },
  {
    'aera': '延边朝鲜族自治州',
    'code': '222400'
  },
  {
    'aera': '南京',
    'code': '320100'
  },
  {
    'aera': '无锡',
    'code': '320200'
  },
  {
    'aera': '徐州',
    'code': '320300'
  },
  {
    'aera': '常州',
    'code': '320400'
  },
  {
    'aera': '苏州',
    'code': '320500'
  },
  {
    'aera': '南通',
    'code': '320600'
  },
  {
    'aera': '连云港',
    'code': '320700'
  },
  {
    'aera': '淮安',
    'code': '320800'
  },
  {
    'aera': '盐城',
    'code': '320900'
  },
  {
    'aera': '扬州',
    'code': '321000'
  },
  {
    'aera': '镇江',
    'code': '321100'
  },
  {
    'aera': '泰州',
    'code': '321200'
  },
  {
    'aera': '宿迁',
    'code': '321300'
  },
  {
    'aera': '南昌',
    'code': '360100'
  },
  {
    'aera': '景德镇',
    'code': '360200'
  },
  {
    'aera': '萍乡',
    'code': '360300'
  },
  {
    'aera': '九江',
    'code': '360400'
  },
  {
    'aera': '新余',
    'code': '360500'
  },
  {
    'aera': '鹰潭',
    'code': '360600'
  },
  {
    'aera': '赣州',
    'code': '360700'
  },
  {
    'aera': '吉安',
    'code': '360800'
  },
  {
    'aera': '宜春',
    'code': '360900'
  },
  {
    'aera': '抚州',
    'code': '361000'
  },
  {
    'aera': '上饶',
    'code': '361100'
  },
  {
    'aera': '沈阳',
    'code': '210100'
  },
  {
    'aera': '大连',
    'code': '210200'
  },
  {
    'aera': '鞍山',
    'code': '210300'
  },
  {
    'aera': '抚顺',
    'code': '210400'
  },
  {
    'aera': '本溪',
    'code': '210500'
  },
  {
    'aera': '丹东',
    'code': '210600'
  },
  {
    'aera': '锦州',
    'code': '210700'
  },
  {
    'aera': '营口',
    'code': '210800'
  },
  {
    'aera': '阜新',
    'code': '210900'
  },
  {
    'aera': '辽阳',
    'code': '211000'
  },
  {
    'aera': '盘锦',
    'code': '211100'
  },
  {
    'aera': '铁岭',
    'code': '211200'
  },
  {
    'aera': '朝阳',
    'code': '211300'
  },
  {
    'aera': '葫芦岛',
    'code': '211400'
  },
  {
    'aera': '呼和浩特',
    'code': '150100'
  },
  {
    'aera': '包头',
    'code': '150200'
  },
  {
    'aera': '乌海',
    'code': '150300'
  },
  {
    'aera': '赤峰',
    'code': '150400'
  },
  {
    'aera': '通辽',
    'code': '150500'
  },
  {
    'aera': '鄂尔多斯',
    'code': '150600'
  },
  {
    'aera': '呼伦贝尔',
    'code': '150700'
  },
  {
    'aera': '巴彦淖尔',
    'code': '150800'
  },
  {
    'aera': '乌兰察布',
    'code': '150900'
  },
  {
    'aera': '兴安盟',
    'code': '152200'
  },
  {
    'aera': '锡林郭勒盟',
    'code': '152500'
  },
  {
    'aera': '阿拉善盟',
    'code': '152900'
  },
  {
    'aera': '银川',
    'code': '640100'
  },
  {
    'aera': '石嘴山',
    'code': '640200'
  },
  {
    'aera': '吴忠',
    'code': '640300'
  },
  {
    'aera': '固原',
    'code': '640400'
  },
  {
    'aera': '中卫',
    'code': '640500'
  },
  {
    'aera': '西宁',
    'code': '630100'
  },
  {
    'aera': '海东',
    'code': '630200'
  },
  {
    'aera': '海北藏族自治州',
    'code': '632200'
  },
  {
    'aera': '黄南藏族自治州',
    'code': '632300'
  },
  {
    'aera': '海南藏族自治州',
    'code': '632500'
  },
  {
    'aera': '果洛藏族自治州',
    'code': '632600'
  },
  {
    'aera': '玉树藏族自治州',
    'code': '632700'
  },
  {
    'aera': '海西蒙古族藏族自治州',
    'code': '632800'
  },
  {
    'aera': '太原',
    'code': '140100'
  },
  {
    'aera': '大同',
    'code': '140200'
  },
  {
    'aera': '阳泉',
    'code': '140300'
  },
  {
    'aera': '长治',
    'code': '140400'
  },
  {
    'aera': '晋城',
    'code': '140500'
  },
  {
    'aera': '朔州',
    'code': '140600'
  },
  {
    'aera': '晋中',
    'code': '140700'
  },
  {
    'aera': '运城',
    'code': '140800'
  },
  {
    'aera': '忻州',
    'code': '140900'
  },
  {
    'aera': '临汾',
    'code': '141000'
  },
  {
    'aera': '吕梁',
    'code': '141100'
  },
  {
    'aera': '济南',
    'code': '370100'
  },
  {
    'aera': '青岛',
    'code': '370200'
  },
  {
    'aera': '淄博',
    'code': '370300'
  },
  {
    'aera': '枣庄',
    'code': '370400'
  },
  {
    'aera': '东营',
    'code': '370500'
  },
  {
    'aera': '烟台',
    'code': '370600'
  },
  {
    'aera': '潍坊',
    'code': '370700'
  },
  {
    'aera': '济宁',
    'code': '370800'
  },
  {
    'aera': '泰安',
    'code': '370900'
  },
  {
    'aera': '威海',
    'code': '371000'
  },
  {
    'aera': '日照',
    'code': '371100'
  },
  {
    'aera': '莱芜',
    'code': '371200'
  },
  {
    'aera': '临沂',
    'code': '371300'
  },
  {
    'aera': '德州',
    'code': '371400'
  },
  {
    'aera': '聊城',
    'code': '371500'
  },
  {
    'aera': '滨州',
    'code': '371600'
  },
  {
    'aera': '菏泽',
    'code': '371700'
  },
  {
    'aera': '成都',
    'code': '510100'
  },
  {
    'aera': '自贡',
    'code': '510300'
  },
  {
    'aera': '攀枝花',
    'code': '510400'
  },
  {
    'aera': '泸州',
    'code': '510500'
  },
  {
    'aera': '德阳',
    'code': '510600'
  },
  {
    'aera': '绵阳',
    'code': '510700'
  },
  {
    'aera': '广元',
    'code': '510800'
  },
  {
    'aera': '遂宁',
    'code': '510900'
  },
  {
    'aera': '内江',
    'code': '511000'
  },
  {
    'aera': '乐山',
    'code': '511100'
  },
  {
    'aera': '南充',
    'code': '511300'
  },
  {
    'aera': '眉山',
    'code': '511400'
  },
  {
    'aera': '宜宾',
    'code': '511500'
  },
  {
    'aera': '广安',
    'code': '511600'
  },
  {
    'aera': '达州',
    'code': '511700'
  },
  {
    'aera': '雅安',
    'code': '511800'
  },
  {
    'aera': '巴中',
    'code': '511900'
  },
  {
    'aera': '资阳',
    'code': '512000'
  },
  {
    'aera': '阿坝藏族羌族自治州',
    'code': '513200'
  },
  {
    'aera': '甘孜藏族自治州',
    'code': '513300'
  },
  {
    'aera': '凉山彝族自治州',
    'code': '513400'
  },
  {
    'aera': '西安',
    'code': '610100'
  },
  {
    'aera': '铜川',
    'code': '610200'
  },
  {
    'aera': '宝鸡',
    'code': '610300'
  },
  {
    'aera': '咸阳',
    'code': '610400'
  },
  {
    'aera': '渭南',
    'code': '610500'
  },
  {
    'aera': '延安',
    'code': '610600'
  },
  {
    'aera': '汉中',
    'code': '610700'
  },
  {
    'aera': '榆林',
    'code': '610800'
  },
  {
    'aera': '安康',
    'code': '610900'
  },
  {
    'aera': '商洛',
    'code': '611000'
  },
  {
    'aera': '天津市市辖区',
    'code': '120100'
  },
  {
    'aera': '拉萨',
    'code': '540100'
  },
  {
    'aera': '日喀则',
    'code': '540200'
  },
  {
    'aera': '昌都',
    'code': '540300'
  },
  {
    'aera': '林芝',
    'code': '540400'
  },
  {
    'aera': '山南',
    'code': '540500'
  },
  {
    'aera': '那曲',
    'code': '540600'
  },
  {
    'aera': '阿里',
    'code': '542500'
  },
  {
    'aera': '乌鲁木齐',
    'code': '650100'
  },
  {
    'aera': '克拉玛依',
    'code': '650200'
  },
  {
    'aera': '吐鲁番',
    'code': '650400'
  },
  {
    'aera': '哈密',
    'code': '650500'
  },
  {
    'aera': '昌吉回族自治州',
    'code': '652300'
  },
  {
    'aera': '博尔塔拉蒙古自治州',
    'code': '652700'
  },
  {
    'aera': '巴音郭楞蒙古自治州',
    'code': '652800'
  },
  {
    'aera': '阿克苏',
    'code': '652900'
  },
  {
    'aera': '克孜勒苏柯尔克孜自治州',
    'code': '653000'
  },
  {
    'aera': '喀什',
    'code': '653100'
  },
  {
    'aera': '和田',
    'code': '653200'
  },
  {
    'aera': '伊犁哈萨克自治州',
    'code': '654000'
  },
  {
    'aera': '塔城',
    'code': '654200'
  },
  {
    'aera': '阿勒泰',
    'code': '654300'
  },
  {
    'aera': '石河子',
    'code': '659001'
  },
  {
    'aera': '阿拉尔',
    'code': '659002'
  },
  {
    'aera': '图木舒克',
    'code': '659003'
  },
  {
    'aera': '五家渠',
    'code': '659004'
  },
  {
    'aera': '昆明',
    'code': '530100'
  },
  {
    'aera': '曲靖',
    'code': '530300'
  },
  {
    'aera': '玉溪',
    'code': '530400'
  },
  {
    'aera': '保山',
    'code': '530500'
  },
  {
    'aera': '昭通',
    'code': '530600'
  },
  {
    'aera': '丽江',
    'code': '530700'
  },
  {
    'aera': '普洱',
    'code': '530800'
  },
  {
    'aera': '临沧',
    'code': '530900'
  },
  {
    'aera': '楚雄彝族自治州',
    'code': '532300'
  },
  {
    'aera': '红河哈尼族彝族自治州',
    'code': '532500'
  },
  {
    'aera': '文山壮族苗族自治州',
    'code': '532600'
  },
  {
    'aera': '西双版纳傣族自治州',
    'code': '532800'
  },
  {
    'aera': '大理白族自治州',
    'code': '532900'
  },
  {
    'aera': '德宏傣族景颇族自治州',
    'code': '533100'
  },
  {
    'aera': '怒江傈僳族自治州',
    'code': '533300'
  },
  {
    'aera': '迪庆藏族自治州',
    'code': '533400'
  },
  {
    'aera': '杭州',
    'code': '330100'
  },
  {
    'aera': '宁波',
    'code': '330200'
  },
  {
    'aera': '温州',
    'code': '330300'
  },
  {
    'aera': '嘉兴',
    'code': '330400'
  },
  {
    'aera': '湖州',
    'code': '330500'
  },
  {
    'aera': '绍兴',
    'code': '330600'
  },
  {
    'aera': '金华',
    'code': '330700'
  },
  {
    'aera': '衢州',
    'code': '330800'
  },
  {
    'aera': '舟山',
    'code': '330900'
  },
  {
    'aera': '台州',
    'code': '331000'
  },
  {
    'aera': '丽水',
    'code': '331100'
  }
]


# arealist = [
#   {
#     'aera': '全国',
#     'code': '100000'
#   },
#   {
#     'aera': '北京',
#     'code': '110000'
#   },
#   {
#     'aera': '天津',
#     'code': '120000'
#   },
#   {
#     'aera': '沈阳',
#     'code': '210100'
#   },
#   {
#     'aera': '大连',
#     'code': '210200'
#   },
#   {
#     'aera': '上海',
#     'code': '310000'
#   },
#   {
#     'aera': '南京',
#     'code': '320100'
#   },
#   {
#     'aera': '苏州',
#     'code': '320500'
#   }]
# arealist = [
#   {
#     'aera': '上海',
#     'code': '310000'
#   }]
def ConvertTo(datalist,name):
    xls_name = name + str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) + '.xlsx'
    exp_file_name = os.path.join('E:/', xls_name)
    writer = pd.ExcelWriter(exp_file_name)
    df = pd.DataFrame(datalist)
    df.to_excel(writer, name, index=False)
    writer.save()
    writer.close()


def GetAllShops(keyword):
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'amapuuid': 'b3866274-926b-4584-879d-5d60923160b9',
        'referer': 'https://ditu.amap.com/?amapexchange=%2F',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    datalist = []

    pp = 0
    for areadict in arealist:
      pp+=1
      if pp >10:
        break
        url = 'https://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=30&pagenum={pn}&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=16&city={code}&_src=around&keywords={keyword}'.format(pn = 1,code=areadict['code'],keyword =keyword)
        try:
            text = requests.get(url,headers = headers).text
            data = json.loads(text)
            total = data['data']['total']
            tp = math.ceil(int(total)/30)+1
        except:
            # chrome_options = webdriver.ChromeOptions()
            # driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
            # driver.get('https://ditu.amap.com/')
            print('拖动验证码！！')
            print(url)
            time.sleep(30)
            tp =2
        # tp=2
        for i in range(1,int(tp)):
            url = 'https://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=30&pagenum={pn}&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=16&city={code}&_src=around&keywords={keyword}'.format(pn=i, code=areadict['code'], keyword=keyword)
            try:
                text = requests.get(url, headers=headers, timeout=3).text
                data = json.loads(text)
                datas = data['data']['poi_list']
            except:
                try:
                    datas = data
                except:
                    # chrome_options = webdriver.ChromeOptions()
                    # driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
                    # driver.get('https://ditu.amap.com/')
                    # print('拖动验证码！！')
                    # print(url)
                    # time.sleep(30)
                    # try:
                    #     driver.close()
                    # except:
                    #     pass
                    continue
            print(len(datas))
            for d in datas:
                jd = {}
                try:
                    jd['评分'] = d['rating']
                except:
                    jd['评分'] = ' '
                try:
                    jd['电话'] = d['tel']
                except:
                    jd['电话'] = ' '
                try:
                    jd['区号'] = d['areacode']
                except:
                    jd['区号'] = ' '
                try:
                    jd['城市'] = d['cityname']
                except:
                    jd['城市'] = ' '
                try:
                    jd['id'] = d['id']
                except:
                    jd['id'] = ' '
                try:
                    jd['链接'] = 'https://ditu.amap.com/place/{}'.format(d['id'])
                except:
                    jd['链接'] =' '
                try:
                    jd['地址'] = d['address']
                except:
                    jd['地址'] = ' '
                try:
                    jd['名字'] = d['name']
                except:
                    jd['名字'] = ' '
                try:
                    jd['坐标'] = d['entrances'][0]
                except:
                    jd['坐标'] = []
                ks = list(jd.keys())

                if jd[ks[0]] ==jd[ks[1]] ==jd[ks[2]] ==jd[ks[3]] ==jd[ks[4]] ==jd[ks[5]] ==jd[ks[6]] == ' ':
                    continue
                datalist.append(jd)
                print(jd)
    return datalist


def GetAllShops_2(keyword):
    headers = {'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Host':'m.amap.com',
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Mobile Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
   }
    datalist = []
    for areadict in arealist:
        print(areadict)
        for i in range(1,100):
            time.sleep(0.5)

            url = 'http://m.amap.com/service/poi/keywords.json?pagenum={pn}&user_loc=undefined&geoobj=&city={code}&keywords=灵子舞蹈&cluster_state=5&client_network_class=4&pagesize=30'.format(pn=i, code=areadict['code'])
            print(url)
            try:
                text = requests.get(url, headers=headers, timeout=3).text
            except:
                try:
                    text = requests.get(url, headers=headers, timeout=3).text
                except:
                    continue

            try:
                data = json.loads(text)
                datas = data['poi_list']
            except Exception as e:
                print(e)
                break
            print(len(datas))
            for d in datas:
                jd = {}
                try:
                    jd['电话'] = d['tel']
                except:
                    jd['电话'] = ' '

                if len(jd['电话'])<5:
                    continue
                try:
                    jd['区号'] = d['areacode']
                except:
                    jd['区号'] = ' '
                try:
                    jd['城市'] = d['cityname']
                except:
                    jd['城市'] = ' '

                try:
                    jd['链接'] = 'https://ditu.amap.com/place/{}'.format(d['id'])
                except:
                    jd['链接'] = ' '
                try:
                    jd['地址'] = d['address']
                except:
                    jd['地址'] = ' '
                try:
                    jd['名字'] = d['disp_name']
                except:
                    jd['名字'] = ' '

                ks = list(jd.keys())

                if jd[ks[0]] == jd[ks[1]] == jd[ks[2]] == jd[ks[3]] == jd[ks[4]] == jd[ks[5]] == ' ':
                    continue
                datalist.append(jd)
                print(jd)

            if len(datas)<30:
                break
    return datalist


keyword = '灵子舞蹈'
DATAS = GetAllShops_2(keyword)

ConvertTo(DATAS,keyword)
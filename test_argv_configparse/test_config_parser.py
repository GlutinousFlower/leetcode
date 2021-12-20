# -*- coding: utf-8 -*-
# @Time : 2021/12/20 2:53 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : test_config_parser.py

import configparser


config = configparser.ConfigParser()
config.read("config.ini", encoding="utf-8")
# 获取所用的section节点
print(config.sections())
#获取指定section 的options。即将配置文件某个section 内key 读取到列表中：
print(config.options("db"))
#获取指点section下指点option的值
print(config.get("db", "db_port"))
#获取指点section的所用配置信息
print(config.items("db"))

#修改某个option的值，如果不存在该option 则会创建
config.set("db", "db_port", "69")  #修改db_port的值为69
config.write(open("config.ini", "w"))
print(config.get('db','db_port'))

if not config.has_section("default"):  # 检查是否存在section,新建section
    config.add_section("default")
if not config.has_option("default","test"):
    config.set('default','test','ceshi')
    config.write(open("config.ini", "w"))

#检查section或option是否存在，bool值
print(config.has_section("db")) #是否存在该section
print(config.has_option("db", "option"))  #是否存在该option

# 删除section 和 option
config.remove_section("default") #整个section下的所有内容都将删除
config.write(open("config.ini", "w"))  #删除需要写入权限
# -*- coding: utf-8 -*-
# @Time : 2022/2/23 5:27 下午
# @Author : xiaoluping
# @Email : xiaoluping@yuanfudao.com
# @File : sign_connect.py

import requests

url = 'https://infra-api.zhenguanyu.com/infra-phoenix-console/api/running/service/1448/env/testing/pods'
headers = {
    'cookie': 'JSESSIONID=D7BF21D3FE510227016367BDA856B03F; PERSISTENT=fAprN%2Bd9OPP11Ato5Vb0nS4QaRXkkoreA5%2F9V49%2Fo461Z%2BEeUil0mk%2BTo%2FRUIEPDVDZaWVuV9R3sHzjVGSeybNBIKwEWOsYxwPQCuyjHml%2BF6wnG7jb4wj2Z2LxS60pcUC0RwMCH007RT%2BZG0gJMDQKSbbVtWJ%2F3CyRcKlA4qmU%3D; SESS=WEun%2FE6CsKhxOZSTbQZHOAdJ89olnZmjQyanGQJULvzQaceZhJvo9Ns3eWbw6VPN; SESS_V2=fAprN%2Bd9OPP11Ato5Vb0nS4QaRXkkoreA5%2F9V49%2Fo461Z%2BEeUil0mk%2BTo%2FRUIEPDVDZaWVuV9R3sHzjVGSeybNBIKwEWOsYxwPQCuyjHml%2BF6wnG7jb4wj2Z2LxS60pcUC0RwMCH007RT%2BZG0gJMDQKSbbVtWJ%2F3CyRcKlA4qmU%3D'

}

res = requests.get(url=url, header=headers)
print(res.json())

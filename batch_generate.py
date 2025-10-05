import os
import re  # 加了这行，修复 NameError
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import random

# 配置
template_file = 'trx/index.html'  # 模板路径
items = [
    'boost', 'chain', 'charge', 'community', 'connect', 'credit', 'earn', 'energy',
    'fee', 'future', 'global', 'growth', 'join', 'lease', 'mine', 'network', 'node',
    'official', 'pool', 'portal', 'power', 'release', 'rent', 'saving', 'secure',
    'smart', 'stake', 'update', 'usdt', 'wallet'
]  # 29 个原来的文件夹（排除 trx）

# 读取模板
with open(template_file, 'r', encoding='utf-8') as f:
    template_html = f.read()

soup_template = BeautifulSoup(template_html, 'html.parser')

# 调试打印原值
title_old = soup_template.find('title').text if soup_template.find('title') else 'No title'
h1_old = soup_template.find('h1').text if soup_template.find('h1') else 'No h1'
date_old = 'No date'
date_p = soup_template.find('p', string=re.compile(r'Last updated: \d{4}-\d{2}-\d{2}'))
if date_p:
    date_old = date_p.text
print(f"原 title: '{title_old}'")
print(f"原 h1: '{h1_old}'")
print(f"原日期: '{date_old}'")

print("模板读取成功！开始生成 29 个原来的中转页...")

# 为每个生成
for item in items:
    # 复制模板
    soup = BeautifulSoup(template_html, 'html.parser')
    
    # 修改 <title>（英文）
    title_tag = soup.find('title')
    if title_tag:
        title_tag.string = f'🌐 {item.capitalize()} Energy Rental · Global Edition'
    
    # 修改 <h1>（英文，第一个 h1）
    h1_tag = soup.find('h1')
    if h1_tag:
        h1_tag.string = f'🌐 {item.capitalize()} Energy Rental · Global Edition'
    
    # 修改日期（随机 2025-10-01 到 10-05，匹配 p 标签文本）
    start_date = datetime(2025, 10, 1)
    random_days = random.randint(0, 4)
    mod_date = (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')
    date_p = soup.find('p', string=re.compile(r'Last updated: \d{4}-\d{2}-\d{2}'))
    if date_p:
        date_p.string = f'Last updated: {mod_date}'
    
    # 保存
    dir_path = item
    os.makedirs(dir_path, exist_ok=True)
    new_file = os.path.join(dir_path, 'index.html')
    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    
    print(f'✅ Generated: {dir_path}/index.html | New Title/H1: "🌐 {item.capitalize()} Energy Rental · Global Edition" | New Date: {mod_date}')

print('Batch complete! 记事本打开 boost/index.html 检查 <title> 和 <h1>！')
print('上传: git add . && git commit -m "Fix HTML title/h1 for 29 pages" && git push')
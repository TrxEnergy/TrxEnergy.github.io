import os
import re
from datetime import datetime, timedelta
import random

# 配置
template_file = 'trx/index.html'  # 模板路径
items = [
    'boost', 'chain', 'charge', 'community', 'connect', 'credit', 'earn', 'energy',
    'fee', 'future', 'global', 'growth', 'join', 'lease', 'mine', 'network', 'node',
    'official', 'pool', 'portal', 'power', 'release', 'rent', 'saving', 'secure',
    'smart', 'stake', 'update', 'usdt', 'wallet'
]  # 29 个（你的仓库文件夹，排除 trx）

# 读取模板
with open(template_file, 'r', encoding='utf-8') as f:
    template_content = f.read()

print("模板读取成功！开始生成 29 个页面...")

# 为每个项目生成
for item in items:
    content = template_content
    
    # 修改 h1/title（第一行 # ...，全英文）
    item_cap = item.capitalize()  # e.g., 'boost' → 'Boost', 'usdt' → 'Usdt'
    h1_new = f'# 🌐 {item_cap} Energy Rental · Global Edition'
    content = re.sub(r'^# .*$', h1_new, content, flags=re.MULTILINE)
    
    # 修改日期（随机 2025-10-01 到 10-05）
    start_date = datetime(2025, 10, 1)
    random_days = random.randint(0, 4)
    mod_date = (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')
    content = content.replace('Last updated: 2025-10-05', f'Last updated: {mod_date}')
    
    # 创建/确保子文件夹
    dir_path = item
    os.makedirs(dir_path, exist_ok=True)
    
    # 保存 index.html（覆盖如果存在）
    new_file = os.path.join(dir_path, 'index.html')
    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    if os.path.exists(new_file):
        print(f'✅ Generated: {dir_path}/index.html | Title/H1: "{h1_new}" | Date: {mod_date}')
    else:
        print(f'❌ Failed: {dir_path}/index.html')

print('Batch complete! 检查: dir boost （看 index.html）')
print('上传: git add . && git commit -m "Batch add 29 index.html for folders" && git push')
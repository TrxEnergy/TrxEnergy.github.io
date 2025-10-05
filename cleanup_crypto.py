import os
import shutil

# crypto 文件夹列表（从截图提取，排除 trx/usdt）
crypto_folders = [
    'ada', 'avax', 'bch', 'bnb', 'btc', 'cro', 'dai', 'doge', 'dot', 'eth',
    'hbar', 'hype', 'leo', 'link', 'ltc', 'mnt', 'okb', 'shib', 'sol', 'sui',
    'ton', 'uni', 'usdc', 'usde', 'wlfi', 'xlm', 'xmr', 'xrp'
]

deleted = 0
for folder in crypto_folders:
    folder_path = os.path.join('.', folder)
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print(f'✅ Deleted folder: {folder}')
        deleted += 1
    else:
        print(f'⏭️ No folder: {folder}')

print(f'Crypto cleanup complete! Deleted {deleted} folders. Run `git add . && git commit -m "Cleanup crypto folders" && git push` to update.')
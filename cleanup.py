import os

# 获取所有子文件夹
folders = [d for d in os.listdir('.') if os.path.isdir(d)]

# 排除 trx
folders = [f for f in folders if f != 'trx']

deleted = 0
for folder in folders:
    index_path = os.path.join(folder, 'index.html')
    if os.path.exists(index_path):
        os.remove(index_path)
        print(f'✅ Deleted: {folder}/index.html')
        deleted += 1
    else:
        print(f'⏭️ No index.html in {folder}')

print(f'Cleanup complete! Deleted {deleted} files. Run `git add . && git commit -m "Cleanup batch index.html" && git push` to update.')
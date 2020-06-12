"""
# 备份文件
cp db.sqlite3 db.sqlite3.bak
# 导出sql并去掉__old
sqlite3 db.sqlite3 ".dump" | sed s/__old//g > db.sql
# 删除源文件
rm db.sqlite3
# 重新导入数据
sqlite3 db.sqlite3 < db.sql
"""


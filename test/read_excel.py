# coding=utf-8
import xlrd
# 打开exlce表格，参数是文件路径
data = xlrd.open_workbook('TestCase.xlsx')

# table = data.sheets()[0]           #  通过索引顺序获取
# table = data.sheet_by_index(0)     #  通过索引顺序获取
table = data.sheet_by_name(u'Sheet1')  # 通过名称获取

nrows = table.nrows  # 获取总行数
print(nrows)
ncols = table.ncols  # 获取总列数
print(ncols)

#　获取一行或一列的值，参数是第几行
print(table.row_values(1))  # 获取第一行值
print(table.col_values(1))  # 获取第一列值
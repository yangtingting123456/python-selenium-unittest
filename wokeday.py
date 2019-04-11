import datetime
import time
#需求：要求自动填写工时系统，在工作日能够正常填写，不是工作日不填写工时
# 获取当前时间
t_date = datetime.date.today()
print(t_date)
t_date
# 获取第几周
week = t_date.strftime("%W")
print(week)
# 获取星期几
week_day = t_date.strftime("%w")
print(week_day)

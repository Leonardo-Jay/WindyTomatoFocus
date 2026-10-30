# -*- coding: utf-8 -*-

import sqlite3  
import json
from os import path
from datetime import datetime, timedelta

pathl = path.join(path.dirname(path.realpath(__file__)), 'shujuku', 'schedule.db')

def databaseinit(filename,db_path,nowdate):
    if not path.exists(filename):  
        # 如果文件不存在，则创建文件并写入数据  
        data = {"value": 6.0,"goonday": 0,"setaim1":0,"setaim2":0,"setaim3":1,"setaim4":0,"setaim5":0}  # 使用浮点数表示double类型  
        with open(filename, 'w') as f:  
            json.dump(data, f)  # 将字典写入文件  
       # print(f"文件{filename}已创建并写入数据。")  
        with open(filename, 'r') as f:  
            content = json.load(f)  
            value = content['value']  # 从字典中提取'value'键对应的值  
           # print(f"提取的数值为：{value}")  # 打印提取的数值
    else:  
        # 如果文件已存在，可以选择读取或做其他处理  
        #print(f"文件{filename}已存在。")  
        # 示例：读取文件内容  
        with open(filename, 'r') as f:  
            content = json.load(f)  
            value = content['value']  # 从字典中提取'value'键对应的值  
            #print(f"提取的数值为：{value}")  # 打印提取的数值
    # 连接到数据库  
    conn = sqlite3.connect(db_path)  
    # 创建一个Cursor对象  
    cur = conn.cursor() 
    # 创建一个表  
    cur.execute('''  
    CREATE TABLE IF NOT EXISTS day_notetime (  
        date DATE PRIMARY KEY,  
        morning_focus_time INTEGER,  
        afternoon_focus_time INTEGER,  
        evening_focus_time INTEGER,  
        goal_setting_time INTEGER,  
        is_completed BOOLEAN
    )  
    ''')   
    #插入每天的数据
    cur.execute('''  
        SELECT * FROM day_notetime WHERE date = ?  
    ''', (nowdate,))  
    if cur.fetchone() is None:  
        # 如果没有找到记录，则插入  
        cur.execute('''  
            INSERT INTO day_notetime (date, morning_focus_time, afternoon_focus_time, evening_focus_time, goal_setting_time, is_completed)  
            VALUES (?, ?, ?, ?, ?, ?)  
        ''', (nowdate, 0, 0, 0, value, 0))  
        conn.commit()  
        #print("数据插入成功")  
    else:  
        print("当天的数据已经存在，跳过插入")
    cur.close()
    conn.close()
      
def xiugaijson(filename,datazhi,axis):#修改存储默认值的json文件中的默认每日目标值
    if path.exists(filename):  
        # 读取文件内容到字典  
        with open(filename, 'r') as f:  
            data = json.load(f)  
        if axis == 1:
            # 修改字典中的值  
            data['value'] = datazhi
        elif axis == 2:
            data['setaim1'] = datazhi
        elif axis == 3:
            data['setaim2'] = datazhi
        elif axis == 4:
            data['setaim3'] = datazhi
        elif axis == 5:
            data['setaim4'] = datazhi
        elif axis == 6:
            data['setaim5'] = datazhi
        # 将修改后的字典写回文件  
        with open(filename, 'w') as f:  
            json.dump(data, f)  
        #print(f"文件{filename}中的值已更新为",data['value']," or ",data['setaim1'],data['setaim2'],data['setaim3'],data['setaim4'],)  
    else:  
        print(f"文件{filename}不存在，无法更新值。")
def tiqujson(filename):
    with open(filename, 'r') as f:  
        data = json.load(f)  
    return data
def resetgoonday(filename):
    with open(filename, 'r') as f:  
        data = json.load(f) 
    data['goonday'] = 0
    with open(filename, 'w') as f:  
        json.dump(data, f)
    print("goonday修改成功")
def clear_day_notetime_table(db_path,nowdate):  
    try:  
        # 连接到数据库  
        conn = sqlite3.connect(db_path)  
        # 创建一个Cursor对象  
        cur = conn.cursor()  
          
        # 清空day_notetime表中的数据  
        cur.execute('''  
            DELETE FROM day_notetime  
        ''')  
        # 提交更改  
        conn.commit()  
        #print("数据清空成功")  
        cur.execute('''  
            SELECT * FROM day_notetime WHERE date = ?  
        ''', (nowdate,))  
        if cur.fetchone() is None:  
            # 如果没有找到记录，则插入  
            cur.execute('''  
                INSERT INTO day_notetime (date, morning_focus_time, afternoon_focus_time, evening_focus_time, goal_setting_time, is_completed)  
                VALUES (?, ?, ?, ?, ?, ?)  
            ''', (nowdate, 0, 0, 0, 6, 0))  
            conn.commit()  
            #print("数据插入成功")  
    except sqlite3.Error as e:  
        print(f"发生错误: {e}")  
      
    finally:  
        # 关闭Cursor和Connection  
        if cur:  
            cur.close()  
        if conn:  
            conn.close()
# 执行 UPDATE 语句    
def xiugai(db_path,nowdate):
    conn = sqlite3.connect(db_path)  
    # 创建一个Cursor对象  
    cur = conn.cursor() 
    cur.execute('''  
    UPDATE day_notetime  
    SET morning_focus_time = ?,
    afternoon_focus_time = ?,
    evening_focus_time = ?,
    goal_setting_time = ?
    WHERE date = ?  
    ''',(30,10,20,40,nowdate))  
def tiqusettime(data,axis):#提取数据库的设定目标值
    conn = sqlite3.connect(pathl )  
    # 创建一个Cursor对象  
    cur = conn.cursor() 
    if axis == 0:
        sql = '''  SELECT goal_setting_time FROM day_notetime WHERE date = ?  '''
    elif axis == 1:
        sql = '''  SELECT morning_focus_time, afternoon_focus_time, evening_focus_time FROM day_notetime WHERE date = ?  '''
    elif axis == 2:
        sql = '''  SELECT is_completed FROM day_notetime WHERE date = ?  '''
    try:  
        cur.execute(sql, (data,))  
        # 获取查询结果
        result = cur.fetchone()
        if result:  
            if len(result) >1:
                return result
            #print("找到的goal_setting_time为:", result[0])# 如果找到了记录，打印goal_setting_time  
            #print("result的长度：",len(result))
            return result[0]
        else:  
            # 如果没有找到记录  
            #print("没有找到匹配的记录")
            if axis == 1:
                return [0,0,0]
            else:
                return 0
    finally:  
        cur.close()  
        conn.close()
def update_goal_setting_time(date_str, new_goal_setting_time_str):  #修改数据库的每日目标值
    try:  
        conn = sqlite3.connect(pathl ) 
        # 创建一个Cursor对象  
        cur = conn.cursor()  
        # 构造SQL更新语句  
        sql = '''  
            UPDATE day_notetime
            SET goal_setting_time = ?  
            WHERE date = ?  
        '''  
        cur.execute(sql, (new_goal_setting_time_str, date_str))  
        # 提交事务  
        conn.commit()  
        #print("goal_setting_time更新成功")  
    except sqlite3.Error as e:   
        # 如果发生错误，回滚事务并打印错误消息  
        conn.rollback()  
        print(f"数据库更新错误: {e}")  
    finally:   
        cur.close() 
def update_time(date_str, time_str,axis):  #修改数据库的每日上午、下午、晚上的时间
    shangwu,xiawu,wanshang = tiqusettime(date_str,1)
    try:  
        conn = sqlite3.connect(pathl ) 
        # 创建一个Cursor对象  
        cur = conn.cursor()  
        if axis == 1:
            sql = '''  UPDATE day_notetime
            SET morning_focus_time = ?  
            WHERE date = ?  '''
            time_str += shangwu
        elif axis == 2:
            sql = '''  UPDATE day_notetime
            SET afternoon_focus_time = ?  
            WHERE date = ?  '''
            time_str += xiawu
        elif axis == 3:
            sql = '''  UPDATE day_notetime
            SET evening_focus_time  = ?  
            WHERE date = ?  '''
            time_str += wanshang
        elif axis == 4:
            sql = '''  UPDATE day_notetime
            SET is_completed  = ?  
            WHERE date = ?  '''
        cur.execute(sql, (time_str, date_str))  
        # 提交事务  
        conn.commit()  
        #print("update_time更新成功")  
    except sqlite3.Error as e:   
        # 如果发生错误，回滚事务并打印错误消息  
        conn.rollback()  
        print(f"数据库更新错误: {e}")  
    finally:   
        cur.close()         
def add_learnedtime(date_str, time_str,add_time_str):
    hour = time_str.hour 
    if 0 <= hour < 12:  
        update_time(date_str,add_time_str,1)
        #print("现在是上午")
    elif 12 <= hour < 18:  
        update_time(date_str,add_time_str,2)
       # print("现在是下午")
    else:  
        update_time(date_str,add_time_str,3)
       # print("现在是晚上")
    
#charu()
#xiugai()

# 执行查询本周学了多久/本月学了多久/本年学了多久
def page3search_time(nowdate,axis):
    date_obj = datetime.fromisoformat(str(nowdate)).date()
    if axis == 1:
        rightdate = date_obj - timedelta(days=date_obj.weekday())#周一
        #print(rightdate,"print(rightdate)")
    elif axis == 2:
        rightdate = date_obj.replace(day=1)
        #print(rightdate,"print(rightdate)")
    else:
        rightdate = date_obj.replace(month=1, day=1)  
        #print(rightdate,"print(rightdate)")
    try:  
        conn = sqlite3.connect(pathl ) 
        # 创建一个Cursor对象  
        cur = conn.cursor() 
        sql = '''  
            SELECT SUM(morning_focus_time + afternoon_focus_time + evening_focus_time) AS total_study_time  
            FROM day_notetime  
            WHERE date >= ? AND date <= ?  
            '''  
        cur.execute(sql, (rightdate, date_obj))  #date_obj是截止到当天
        # 获取查询结果  
        row = cur.fetchone()  
        if row:  
            total_study_time = round(row[0]/60,1) 
            #print(f"本周一共学了 {total_study_time} 小时")  
        else:  
            total_study_time = 0
            #print("本周没有学习记录")
        # 提交事务  
        conn.commit() 
        return total_study_time
    except sqlite3.Error as e:   
        # 如果发生错误，回滚事务并打印错误消息  
        conn.rollback()  
        print(f"数据库更新错误: {e}")  
    finally:   
        cur.close()
# 执行查询本周完成目标/本月完成目标/本年完成目标数
def page3search_goal(nowdate,axis):
    date_obj = datetime.fromisoformat(str(nowdate)).date()
    if axis == 1:
        rightdate = date_obj - timedelta(days=date_obj.weekday())#周一
        #print(rightdate,"print(rightdate)")
    elif axis == 2:
        rightdate = date_obj.replace(day=1)
        #print(rightdate,"print(rightdate)")
    else:
        rightdate = date_obj.replace(month=1, day=1)  
        #print(rightdate,"print(rightdate)")
    finish_goal = 0
    try:  
        conn = sqlite3.connect(pathl ) 
        # 创建一个Cursor对象  
        cur = conn.cursor() 
        sql = '''  
            SELECT date,is_completed 
            FROM day_notetime  
            WHERE date >= ? AND date <= ?  
            '''  
        cur.execute(sql, (rightdate, date_obj))  #date_obj是截止到当天
        # 获取查询结果  
        rows = cur.fetchall() 
        #print("rowsbase:",rows)
        if rows:  
            for row in rows:
                daterow , goalrow = row
                if goalrow == True:
                    finish_goal += 1
                
            #print(f"本周共完成 {finish_goal} 天目标")  
        else:  
            finish_goal = 0
            #print("本周没有完成任何目标")
        # 提交事务  
        conn.commit() 
        return finish_goal
    except sqlite3.Error as e:   
        # 如果发生错误，回滚事务并打印错误消息  
        conn.rollback()  
        print(f"数据库更新错误: {e}")  
    finally:   
        cur.close()
#page3search_time(nowdate,1)
#page3search_goal(nowdate,1)
# 执行查询本周完成目标/本月完成目标/本年完成目标数
def page3search_avg(nowdate,axis):
    date_obj = datetime.fromisoformat(str(nowdate)).date()
    rightdate = '2024-01-01'
    total_study_minutes = 0  
    non_zero_days_count = 0  
    if axis == 1:
        sql = '''  
            SELECT date, (morning_focus_time + afternoon_focus_time + evening_focus_time) AS total_study_time  
            FROM day_notetime  
            WHERE date >= ? AND date <= ?  
            '''  
    elif axis ==2:
        sql = '''  
            SELECT date,morning_focus_time
            FROM day_notetime  
            WHERE date >= ? AND date <= ?  
            '''
    elif axis ==3:
        sql = '''  
            SELECT date,afternoon_focus_time
            FROM day_notetime  
            WHERE date >= ? AND date <= ?  
            '''
    elif axis ==4:
        sql = '''  
            SELECT date,evening_focus_time
            FROM day_notetime  
            WHERE date >= ? AND date <= ?  
            '''
    try:  
        conn = sqlite3.connect(pathl ) 
        # 创建一个Cursor对象  
        cur = conn.cursor() 
        cur.execute(sql, (rightdate,date_obj))  
        rows = cur.fetchall() 
        #print("rows:",rows)
        # 获取查询结果  
        for row in rows:  
            date, total_time = row  
            total_time_minutes = total_time  
            if total_time_minutes > 0:  
                total_study_minutes += total_time_minutes  
                non_zero_days_count += 1  
  
        if non_zero_days_count > 0:  
            average_study_time = round(total_study_minutes / non_zero_days_count / 60, 1)  
            #print(f"{non_zero_days_count}天{total_study_minutes}小时平均每天学了 {average_study_time} 小时（排除0学习时间的天数）")  
        else:  
            #print("没有有效的学习记录")  
            average_study_time = 0
        conn.commit()  # 对于SELECT语句，通常不需要提交，但保持一致性  
        return average_study_time
    except sqlite3.Error as e:  
        conn.rollback()  
        print(f"数据库查询错误: {e}")  
    finally:  
        cur.close()  
        conn.close()  # 确保数据库连接被关闭
# 查询连续目标天数
def page2search_goalday(nowdate):
    date_obj = datetime.fromisoformat(str(nowdate)).date()  
    #print(date_obj)
    try:  
        conn = sqlite3.connect(pathl) 
        # 创建一个Cursor对象  
        cur = conn.cursor() 
        sql = '''  
            SELECT is_completed 
            FROM day_notetime  
            WHERE date >= ? AND date <= ?  
            '''  
        cur.execute(sql, ('2024-01-01', date_obj))  #date_obj是截止到当天
        # 获取查询结果  
        rows = cur.fetchall() 
       # print("rowsbase:",rows,"rows[i]",rows[6])
        finish_goal = 0
        if rows:  
            for i in range(len(rows)-1,-1,-1):
                if rows[i][0] != 0:
                    finish_goal += 1
                else:
                    break
            #print(f"共完成{finish_goal}天目标")  
        else:  
            finish_goal = 0
            #print("本周没有完成连续目标天数")
        # 提交事务  
        conn.commit() 
        return finish_goal
    except sqlite3.Error as e:   
        # 如果发生错误，回滚事务并打印错误消息  
        conn.rollback()  
        print(f"查询连续目标天数错误: {e}")  
    finally:   
        cur.close()
#page3search_avg(nowdate,3)
def test1(db_path):
    
    # 连接到数据库  
    conn = sqlite3.connect(db_path)  
    # 创建一个Cursor对象  
    cur = conn.cursor() 
    # # 查询所有记录  
    cur.execute('SELECT * FROM day_notetime')  
    rows = cur.fetchall()  
    for row in rows:  
        print(row)  
    # 关闭连接  
    conn.close()

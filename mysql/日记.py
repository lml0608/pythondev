# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

'''
三规式

第一规式：列不可拆分
第二规式：唯一标识，主键
第三规式：引用主键
后一个范式都是在前一个范式的基础上建立的


数据库的完整性：
为了保证数据的准确性，数据类型
数字：int decimal
字符串：char,varchar,text
日期：datetime
布尔：bit

char,varchar区别：


约束：

主键  primary key
非空：not null
唯一：unique
默认：default
外键：foreign key

逻辑删除：
重要数据不能删，不做物理删除，逻辑删除
修改表结构，新增一个字段，isDelete，标识是否删除

修改表名：alter table T_classes rename T_students;

剔除重复行:DISTINCT,     SELECT DISTINCT isDelete from subjects;

范围 查询
in
between  and
select * from subjects where id BETWEEN 3 and 5;

is null
is not null


聚合
多行数据进行统计

select COUNT(*) from subjects;
select MAX(id) from subjects;
select min(id) from subjects;
select sum(id) from subjects;
select avg(id) from subjects;

分组
select gender as 性别,COUNT(gender) from student GROUP BY gender;

select gender as 性别,COUNT(gender) from student GROUP BY gender HAVING gender=0;

where对原始数据集进行过滤，having对GROUP BY的结果集进行刷选

排序


关系的存储
连接查询
自关联
字查询
内置函数
视图
事务

'''


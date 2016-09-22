# MySQL笔记

> 使用MySQL数据库也有一阵子时间了，因为不是DBA，所有也很少去研究高级的问题，只停留在增删查改和编写存储过程及MySQL函数等一些基础操作上，现在把目前遇到的自觉为比较重要的知识记下来，同时方便自己以后查阅回忆。
>
>


***
## 1.表连接
通常需要同时获取多个表中的字段，可以用表连接实现。
表连接分 内连接 和 外连接 两种
* 内连接：仅选出两张表中相互匹配的记录，不匹配的则不出现。
* 外连接：
	外连接又分左连接和右连接。
	* 左连接：包含所有的左边表中的记录甚至是右边表中没有和它匹配的记录。(left join TABLE on ...)
	* 右接接：包含所有的右边表中的记录甚至是左边表中没有和它匹配的记录。(right join TABLE on ...)
	* 左右连接类似，二者可以相互转化。

因此基于某些方面的考虑，我尽量使用外连接，因为如果使用内连接，有时可能因为某张数据表的某个字段尚未完善，导致无法查到整条记录。
***
## 2.存储过程与函数
可以将一些复杂且常用的查询写成存储过程或函数，以简化开发者的工作，同时减少数据在数据库和应用服务器之间的传输。
存储过程于函数的区别在于函数必须有返回值，而存储过程没有，存储过程的参数可以使用IN, OUT, INOUT类型，而函数只能是IN类型。
* 存储过程
	* 创建：create procedure sp_name([pro_parmeter[,..]]) 
		[characteristic ..] routine_body; 
    * 调用： call sp_name([parameter[,..]])
    * 查看：show procedure status, show create procedure sp_name\G

* 函数
	* 创建：create function sp_name([func_parameter[,...])
	   returns type
       [characteristic ...] routine_body
    * 调用： select sp_name([parameter[,..]])
	* 查看：show function status, show create function sp_name\G

routine_body是SQL代码的内容，可以用BEGIN...END来表示SQL代码的开始和结束。

***

## 3.其他
* delimiter命令修改语句的结束符号
* 变量
	* 定义：declare var_name[,...] type [default value]
	* 赋值：
	1.直接赋值：set var_name = expr[, var_name =  expr]...
	2.也可以通过查询将结果赋值给变量，这要求查询返回的结果必须只有一行：select col_name[,...] into var_name[,...] table_expr;
* 流程控制：
	* if语句：
    ```
    if search_condition then statement_list
        [else if search_condition  then statement_list]
        [else statement_list]
    end if
    ```
	* case 语句
    ```
    case case_value 
        when when_value then statement_list
        [when when_value then statement_list]...
        [else statement_list]
    end case
    ```
或者
    ```
    case
        when search_condition then statement_list
        [when search_condition then statement_list]...
        [else statement_list]
    end case
    ```

#### 
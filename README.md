# 数据库课程设计：FileSearcher

## 一、软件使用方法：

1. 请下载我们提供的[release版本](https://github.com/Youggls/Filesearcher)

2. 在本地计算机安装`MySQL Server`

3. 修改`'./bin/config.json'`文件，填入相应的本地数据库配置

## 二、项目介绍：

### 1. 项目功能简介：

`FileSeacher`项目主要用来实现文件搜索功能，支持个人PC全部文件的搜索。
搜索完成后会在GUI界面上返回一个Table（详见附录1图1），覆盖了文件名、文件路径、文件修改时间等基本信息，双击某行，可以跳转到该文件所在的父文件夹（详见附录1图2）。
若没有搜索到相关文件，会提示没有搜索到文件（详见附录1图3）

### 2. 项目开发环境：

`FileSeahcer`项目是基于`Python3.6`开发的，主要用到了`PyQT5`以及`PyMySQL`包开发，前者用来实现GUI，后者用来与数据库进行交互。

### 3. 项目外部依赖环境：

`FileSeacher`项目中，文件信息存储是通过数据库进行存储的，故需要用户计算机安装`MySQL Server5.6`或更高版本。

### 4. 项目支持的系统版本：

`FileSeacher`项目目前支持`Windows10`以及`MacOS`操作系统

## 三、项目实现方法介绍：

### 1. 数据库部署：

#### 数据库表定义

本项目针对文件信息在数据库中的存储，建立了一个`FileInfo`表用来存储文件信息，该表主要字段定义如下：

| Field         | Type         | Null | Key | Default |
|---------------|--------------|------|-----|---------|
| hash_id       | varchar(100) | NO   | PRI | NULL    |
| name          | varchar(100) | NO   |     | NULL    |
| modify_time   | varchar(30)  | NO   |     | NULL    |
| size          | varchar(20)  | YES  |     | NULL    |
| isFolder      | tinyint(1)   | YES  |     | NULL    |
| pre_folder_id | varchar(100) | YES  | MUL | NULL    |

* `hash_id`字段为表的主键，用来唯一标识文件信息，通过`Python`外部调用`hashlib.md5()`生成，类型为`varchar(100)`
* `name`字段为文件名，类型为`varchar(100)`
* `modify_time`为文件修改时间，类型为`varchar(30)`
* `size`为文件大小，类型为`varcahr(20)`，单位是KB
* `isFolder`为是否为文件夹的布尔值，为文件夹则为`1`，不为文件夹则为`0`，类型为`tinyint(1)`
* `pre_folder_id`为该文件（夹）父级目录的哈希值，参考本表的`hash_id`字段，当文件夹为根目录时，该字段等于本身的`hash_id`

#### 数据库函数实现：

数据库中，定义了一个`getFullPath(hash_id varchar(100))`函数，用来给定某个文件来递归查询全路径，详见附录2所示源代码。

### 2. 数据库交互部分实现简介：

与数据库的交互部分，使用了`PyMySQL`包进行交互，为了交互数据便利性以及开发效率，本项目实现了一个`dbConnector`包，提供了针对该项目需求的若干接口。

方法名|参数|方法作用|返回值
-----|----|-------|-----
`walk_path`|无|遍历文件系统|无
`init_database`|无|重新初始化数据库|无
`search_file`|文件名|搜索文件名|`FileInfo`对象的`list`

`FileInfo`对象是储存文件信息的一个类，用来储存文件的基本信息，在此不再赘述，详见附录1源代码

### 3. GUI实现简介：

`FileSearcher`项目的GUI部分主要使用`PyQt5`包来实现，并导入项目中实现的`dbConnector`包，实现其接口。为了提高代码规范性、可读性以及开发效率，本项目实现了一个`dbInterface`包，提供界面接口。

方法/槽函数|参数|方法作用
----------|----|----
`initUI`|无|采用水平、垂直布局，实现界面的初始化
`showResult`|搜索关键字|使用`QTableView`显示搜索结果
`openDir`|无|连接在搜索结果界面双击搜索结果的信号，打开文件所在文件夹。
`toolTip`|无|连接在搜索结果界面单机搜索结果的信号，并在下方“Result”一栏显示所选结果的文本信息。
`center`|无|将界面居中
`closeEvent`|无|重写closeEvent，使用`QMessageBox`实现应用弹出“是否退出窗口”
`__read_config`|无|读取数据库配置文件`config.json`

## 四、实现过程中的问题

1. 跨平台问题的解决：

    本小组成员日常开发环境不同，`Windows`和`MacOS`的路径差异导致了很大的问题，后来我们通过在外部配置`config.json`文件判断软件运行环境，针对跨平台问题进行了优化

2. 文件名中所带的引号：

    由于文件名为字符串类型，若插入数据时，文件名带有引号，例如：

    ```sql
    insert into table values('file'name');
    ```

    会引发异常，不能正确匹配

    故我们使用了转义字符解决该问题

    ```sql
    insert into table values('file\'name');
    ```

## 五、小组分工简介：

姓名|学号|分工
----|----|---
李沛尧|1712901|负责数据库搭建、与数据库交互模块
杨添凯|1712950|负责GUI的实现及美化

## 附录一

图1![Image Alt Text](http://www.youggls.top/图1.jpg "图1")

图2![Image Alt Text](http://www.youggls.top/图2.jpg "图2")

图3![Image Alt Text](http://www.youggls.top/图3.jpg "图3")

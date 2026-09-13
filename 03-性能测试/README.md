性能测试

一、项目简介

基于 LoadRunner 对 WebTours 系统进行性能测试，录制并优化登录业务脚本，添加事务、集合点、检查点和参数化，模拟多用户并发登录场景，分析系统性能表现。

二、技术栈与工具

\- 性能测试工具：LoadRunner

\- 脚本语言：C

\- 被测系统：WebTours

\- 测试协议：Web（HTTP/HTML）

三、项目结构

03-性能测试/

├── README.md

├── 脚本/

│ └── login\_script.c 

└── 报告

四、关键技术点

1\. 关联（Correlation）

\- 使用 `web\_reg\_save\_param\_ex` 函数，从服务器响应中动态提取 `userSession` 值。

\- 左右边界：`LB=userSession value=`，`RB=>\\n<table border`。

\- 作用：解决登录过程中 session 动态变化导致的脚本回放失败问题。

2\. 事务（Transaction）\*\*

\- 使用 `lr\_start\_transaction("login")` 和 `lr\_end\_transaction("login", LR\_AUTO)` 定义登录事务。

\- 作用：统计登录操作的响应时间。

3\. 集合点（Rendezvous）\*\*

\- 使用 `lr\_rendezvous("login")` 设置集合点。

\- 作用：模拟多用户同时并发登录，测试系统在并发压力下的表现。

4\. 检查点（Checkpoint）

\- 使用 `web\_reg\_find("Text=Welcome, <b>{username}")` 设置文本检查点。

\- 作用：验证登录是否成功，确保脚本执行结果正确。

5\. 参数化（Parameterization）

\- 使用 `{username}` 和 `{password}` 参数化登录账号。

\- 作用：模拟不同用户登录，避免使用同一账号导致的数据冲突。

6\. 思考时间（Think Time）

\- 使用 `lr\_think\_time(85)` 模拟用户操作间隔。

\- 作用：更真实地模拟用户行为。

五、测试执行流程

1\. 使用 LoadRunner VuGen 录制 WebTours 登录脚本。

2\. 对脚本进行关联、参数化、事务、集合点、检查点等优化。

3\. 在 Controller 中设置并发用户数、集合点策略和场景计划。

4\. 执行场景，模拟多用户并发登录。

5\. 使用 Analysis 分析测试结果，查看事务响应时间、TPS、并发数等指标。

六、项目产出

\- LoadRunner 性能测试脚本

\- 登录业务性能测试场景

\- 性能测试结果分析

七、说明

本项目为软件测试培训期间完成的性能测试实践项目，重点体现 LoadRunner 脚本录制与优化能力、关联和参数化等核心技术点的使用，以及性能测试场景设计和结果分析能力。


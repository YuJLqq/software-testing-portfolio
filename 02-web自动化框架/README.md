Web 自动化测试框架

一、项目简介

基于 Python + Selenium 搭建的 Web UI 自动化测试脚本，结合 Excel 数据驱动，对订单页面进行自动化测试，覆盖测试数据读取、用例执行、断言验证等流程。

二、技术栈

1\.编程语言：Python

2\.自动化工具：Selenium

3\.测试数据：Excel（.xls）

4\.测试页面：HTML

三、项目结构

| 文件 | 说明 |

|------|------|

| `do\_case.py` | 测试执行主脚本，读取用例并调度执行 |

| `read\_case.py` | 读取 Excel 测试数据，实现数据驱动 |

| `test\_def.py` | Selenium 操作封装类，提供页面操作的基础方法 |

| `order.xls` | 测试数据文件，存放订单相关测试用例数据 |

| `orderweb.html` | 自动化测试执行后生成的 HTML 测试报告 |

四、项目内容

1\. Selenium 操作封装（test\_def.py）

对 Selenium 常用操作进行二次封装，提供统一的调用接口，包括：

\- `testOpen`：打开页面并最大化窗口

\- `testPosition`：支持 id、name、link、class、xpath 五种定位方式，内置重试机制，定位失败自动截图

\- `testInput`：输入框清空并输入内容

\- `testClick`：点击元素

\- `testFrame`：支持进入、返回父级、返回默认三种 frame 切换

\- `testSelect`：支持按索引、value、文本三种方式操作下拉框

\- `testJs`：执行 JavaScript 脚本

\- `testImage`：上传图片

\- `testSleep`：强制等待

2\. 测试数据读取（read\_case.py）

\- 读取  [order.xls](02-Web自动化框架/order.xls)中的测试数据。

\- 将测试数据与测试步骤分离，实现数据驱动。

3\. 自动化测试执行（do\_case.py）

\- 调用封装好的操作方法，按 Excel 中的测试数据执行测试步骤。

\- 对页面元素进行定位、操作和断言验证。

4\. 测试报告生成

\- 测试执行完成后，生成[orderweb.html](02-Web自动化框架/orderweb.html)测试报告。

\- 报告中展示每条用例的执行结果。




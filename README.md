# CRM系统

###一、用途

​	该系统主要用于客户和学生关系管理，也有一些内部员工可以使用的小功能，如：会议室预定等；

​	客户管理主要涉及到客户信息的录入和销售相关的客户分配，学生管理主要是班主任和讲师对学生学习情况进行记录，还提供问卷调查功能。

###二、业务机制

1. 工作安排

根据对销售人员的以往业绩的分析制定每个销售人员的销售任务，综合多方面数据对销售人员进行权重的评定。在工作分配时，通过权重进行排序，权重大的优先安排任务。分配任务时，按照权重排序从高到低顺位循环分配。（若销售人员被分配任务以达到目标值则跳过，若所有销售人员都达到目标值则将剩余销售任务重复之前的方案进行分配）。

2. 销售进度状态

销售人员得到任务后对应的客户状态改为开始接洽，记录起始时间，订单状态从公司资源更改为销售人员的个人资源，其他人在订单转移前不可接触订单信息。

销售人员在跟进订单时，每一次与客户接洽都会在数据库中生成一条记录。

若订单在十五日内被销售人员转化成功，则将该客户的状态由待转化变为转化成功，并在正式客户表中生成该客户的记录。在销售人员的订单记录中将这笔订单的状态改为转化成功。

若当前与客户接洽的销售人员三天未跟进订单或是在十五天内未促成交易。则相关订单信息会被移动到公司公共资源中，并且原先跟进订单的销售人员不可以选择继续跟进（直至该订单再次被移入公司公共资源）。原销售人员的订单跟进记录中会显示有一单未能转化，并显示原因（重新接手该订单后即使转化成功，本条记录不会被覆盖）。

3. 业绩考核

在销售人员的订单记录中记录了销售人员从第一笔业务到最近一笔业务的所有信息。可以为销售人员的业绩考核提供：接单数，转化率，订单未转化原因等数据。
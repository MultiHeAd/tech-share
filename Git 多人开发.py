"""正规的gitflow工作流"""

# 面试题：如何多人开发？
# 每个人都有自己的分支，分别开发，最后合并
# 例如：main主分支下面有dev分支检查，通过dev再拆分出a,b,c,d...分支

# 每个人都只在自己的分支开发，做完后代码review

# 大公司可能会有release预发布，这个分支，测试，小bug修复完成后才能上线

# git tag 打标签取代冗长的哈希值
# git tag -a +版本 -m "备注"
# git push origin --tags

# 邀请新人，给权限，允许下载和上传
# git checkout -b dev 创建并切换

# 邀请成员进组织，需要拿到名字
# 成员会接受到邮件


# code review: settings可以设置添加特殊的分支，比如限定谁有权限，代码需要review才能合并
# pull request: 如果有需要code review有权限的人需要check无误后进行合并


# 测试可能由测试团队做或者是负责人处理
# 新开一个release分支检查并修改小分支，这里不推荐加新功能，都检查完和master/main合并


# 给开源代码提交代码
# 先Fork，把源代码拷贝一份到自己的仓库
# 从自己的仓库拉代码到本地进行二次开发，bug修复或功能增加后，再上传回自己的云端
# 给源代码作者提交修复bug的申请（pull request）（在自己的界面）
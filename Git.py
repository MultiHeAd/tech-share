# 工作区分为已管理，新修改的部分
# 工作区内容提交到暂存区 用下面命令，文件会变成绿色
# git add .
# 暂存区检验无问题后提交到版本库，用commit命令
# git commit -m'更改的版本名称'
# 暂存区用来缓存
#   git init
#   git config --global user.email "you@example.com"
#   git config --global user.name "Your Name"

#   git status
#   git log

"""
回滚：返回之前的版本
git reset --hard +版本号

reset之后前面的内容没了，先用
git reflog
git reset --hard +版本号
"""
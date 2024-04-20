# rebase的作用1：将多个提交记录整合成一个
# git rebase -i + 老版本版本号   表示将从老版本开始到当前版本合并
# git rebase -i + HEAD~3   表示将从当前版本起下一个最新的三个版本合并，也就是说总共4个


# 最好在合并记录的时候，不要和已push到远程仓库放到一起，会很麻烦


# 存在分支情况下的rebase操作：
"""
第一步切换到 branch分支
第二步执行 git rebase master 变基
第三步回到master   git merge dev

把功能合并，不存在分支
"""
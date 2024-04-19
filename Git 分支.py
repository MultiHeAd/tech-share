#  分支，指针，只保存修改的部分，其他部分用指针指向前一个版本

#  修bug：比如c4正在开发功能，老版本出bug了回滚到c3，修bug写c5让老功能恢复正常，最后将c4和c5合并

#  主干名叫master，分支可以取名，比如开发叫dev，修复bug叫bug，最后分别合并回master
#  按q推出less浏览模式

"""
命令：
git branch   查看当前路径是什么分支或者是主干
git branch +名字   增加新分支，*是当前所处位置
git checkout +名字   切换分支，不影响master
合并:
第一步切换回master  git checkout master
第二步：git merge dev
第三步：手动解决冲突

<<<<<<< HEAD
这是 master 分支的内容
=======
这是 dev 分支的内容
>>>>>>> dev

第四步：合并内容
git add .
git commit -m "合并 dev 到 master，解决冲突"

第五步：删除分支
git branch -d +名字




"""
#用python脚本执行git命令，提交到github仓库
import os
os.system('git add --all')
os.system('git commit -m "add photos"')
os.system('git push -u origin master')
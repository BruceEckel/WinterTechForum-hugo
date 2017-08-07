@echo off
hugo
py -3 deploy.py
cd ..\WinterTechForum.github.io
@echo on
git commit -a -m "update"
git push
cd ..\WinterTechForum-hugo

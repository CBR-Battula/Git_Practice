@CBR-Battula ➜ /workspaces/Git_Practice (master) $ touch test.py
@CBR-Battula ➜ /workspaces/Git_Practice (master) $ vi test.py
@CBR-Battula ➜ /workspaces/Git_Practice (master) $ git add .
@CBR-Battula ➜ /workspaces/Git_Practice (master) $ git add test.py
@CBR-Battula ➜ /workspaces/Git_Practice (master) $ git commit -m "jsf"
[master 08fb038] jsf
 1 file changed, 1 insertion(+)
 create mode 100644 test.py
@CBR-Battula ➜ /workspaces/Git_Practice (master) $ git push origin master
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 286 bytes | 286.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/CBR-Battula/Git_Practice
   7344e1d..08fb038  master -> master

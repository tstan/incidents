#!/usr/bin/fish

git pull
cp ~/dev/cfslo-incident-viewer/data/* raw/
python convert.py
git add -A
git commit -m "Daily update"
git push

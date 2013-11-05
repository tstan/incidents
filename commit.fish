#!/usr/bin/fish

git pull
cp ~/gst_dashboard/data/* raw/
python convert.py
git add -A
git commit -m "Daily update" --author "SLUGIS <joe.larson@fire.ca.gov>"
git push

import os
import itertools
from datetime import datetime

import geojson

from etc.inctypes import types
from etc.jrsdtns import jrsdtns


def good_line(line):
    fields = line.split("|")
    return len(fields) > 9 and fields[0].startswith("CAD") and fields[7] \
        and fields[8] and fields[4]

def good_lines(file_path):
    with open(file_path) as open_file:
        return [line.strip() for line in open_file if good_line(line)]

def uniq_lines(dir_path):
    dir_path = os.path.join(dir_path, "")
    all_lines = (good_lines(dir_path + f) for f in os.listdir(dir_path))
    all_lines = itertools.chain(*all_lines)
    lam = lambda line: line.split("|")[1]
    sorted_lines = sorted(all_lines, key=lam)
    grouped_lines = itertools.groupby(sorted_lines, lam)
    return (max(g) for k, g in grouped_lines)

def lines_to_geo(line):
    fields = line.split("|")
    point = geojson.Point([float(fields[7]), float(fields[8])])
    try:
        jrsdtn = jrsdtns.get(fields[10], "")
    except IndexError:
        jrsdtn = "Unknown"
    dt = datetime.strptime(fields[4], "%Y%m%d%H%M%S")
    category, inc_type = types.get(fields[5], ('Unknown', 'Unknown'))
    properties = {
        "event_id": fields[1],
        "incident_id": fields[2],
        "type": fields[5],
        "details": fields[6],
        "address": fields[9],
        "jrsdtn": jrsdtn,
        "category": category,
        "time": dt.time().isoformat(),
        "date": dt.date().isoformat()
    }
    return geojson.Feature(geometry=point, properties=properties)

def group_geo_by_day(points):
    days = {}
    for point in points:
        days.setdefault(point.properties["date"], []).append(point)
    for day, points in days.items():
        days[day] = geojson.FeatureCollection(points) 
    return days

def days_to_files(days):
    for day, points in days.items():
        day = datetime.strptime(day, "%Y-%m-%d").strftime("%Y_%m%d_Log")
        filename = "geojson/{}.geojson".format(day)
        with open(filename, "w") as open_file:
            open_file.write(geojson.dumps(points) + "\n")

if __name__ == "__main__":
    geo = map(lines_to_geo, uniq_lines("raw"))
    days = group_geo_by_day(geo)
    days_to_files(days)

# CAL FIRE San Luis Obispo Incidents Data

## File structure

* `convert.py`: Python script used to convert the raw, unformatted logs into GeoJSON format
* `commit.fish`: Script used to commit new logs every day
* `raw/`: Contains the raw, unformatted logs from the [CAD](https://en.wikipedia.org/wiki/Computer-aided_dispatch) servers
* `geojson/`: Contains the GeoJSON formatted logs generated from the `convert.py` script
* `etc/`: Contains files used by the `convert.py` script

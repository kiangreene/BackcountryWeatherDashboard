from noaa_sdk import NOAA
import json
from typing import Iterable
from pandas import json_normalize


n = NOAA()
point_weather_json = n.points_forecast(40.7314, -73.8656, type='forecastGridData')

print(json.dumps(point_weather_json, indent=2))

# see what fields there are in the json / what the data looks like
for k ,v in point_weather_json["properties"].items():
    dict_info = None
    vals_info = None
    maybeLenOrValue = len(v) if isinstance(v, Iterable) and not isinstance(v, str) else v
    if isinstance(v, dict) :
        if v.get("values", None) == None:
            dict_info = "no values: " + ",".join(v.keys())
        else:
            isUomValsFmt = set(v.keys()) == set(["uom", "values"])
            if isUomValsFmt:
                dict_info = "uomvalsfmt"
            else:
                dict_info = v.keys()
            record_info = None
            if len(v["values"]) >= 1:
                record_info = v["values"][0].keys()
            vals_info = f"values_info - len:{len(v['values'])} record: {record_info}"
    print(k, type(v), maybeLenOrValue, dict_info, vals_info)

    # fields that I want (maybe)
    fields_oi = ["updateTime", "elevation", "forecastOffice", "temperature", "maxTemperature", "minTemperature",
                 "windChill", "skyCover", "windDirection", "windSpeed", "windGust", "probabilityOrPrecipitation",
                 "quantitativePrecipitation", "iceAccumulation", "snowfallAmount", "snowLevel", "visibility",
                 "transportWindSpeed", "transportWindDirection"]

    # need to filter data
    # convert validTime into something I can read
    filtered_dict = {k: v for (k, v) in point_weather_json["properties"].items() if k in fields_oi}

import dateutil.parser
datetime.fromisoformat('2024-04-26T18:00:00+00:00')

import isodate
isodate.parse_duration('PT1H')
isodate.parse_datetime('2024-04-26T18:00:00+00:00')

filtered_dict = {}
for (k,v) in point_weather_json["properties"].items():
    if k in fields_oi:
        print(f'In fields_oi: {k}')
        filtered_dict[k] = v
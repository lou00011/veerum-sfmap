import googlemaps
import json
import pandas as pd
from sqlalchemy import create_engine
import secret
from toolz import functoolz as f

FILE_PATH = '/home/pl/Downloads/Film_Locations_in_San_Francisco.csv'
gmaps = googlemaps.Client(key=secret.GOOGLE_MAP_BACKEND_KEY)
engine = create_engine('sqlite:///../veerum-project/film.db')


def openFile():
  with open(FILE_PATH, encoding='utf-8-sig') as handle:
    assert handle is not None, 'file handle error'
    df = pd.read_csv(handle)
    assert df is not None, 'failed to create dataframe from csv'
    return df


def query_gmap_geocode(addrStr):
  # The location field in CSV after dataframe transformation may be 'nan' if the field is empty, which is of type float, otherwise it is a string
  if(isinstance(addrStr, float)):
    return None, None

  result = gmaps.geocode(
      address=addrStr,
      region='US',
      bounds={
          "northeast": {
              "lat": 37.838069,
              "lng": -122.353992,
          },
          "southwest": {
              "lat": 37.705006,
              "lng": -122.514352,
          }
      }
  )
  return result


def gmap_query_result_to_latlng(result_list):
  # parsing result. If no result, return pair of None
  # if multiple result, take the first one
  if not result_list or result_list is None:
    return None, None

  head, *tail = result_list

  if head is None:
    return None, None

  location = head['geometry']['location']

  if not location:
    return None, None

  print('adding ({},{}) pair'.format(location['lat'], location['lng']))
  return location['lat'], location['lng']


def add_to_data_frame(df):
  df['lat'], df['long'] = zip(
      *df['Locations'].map(lambda x: f.pipe(
        x
        , query_gmap_geocode
        , gmap_query_result_to_latlng)))
  return df


def insert_to_db(df, engine):
  df.to_sql('films', engine)


def main():
  df = openFile()
  df = add_to_data_frame(df)
  insert_to_db(df, engine)

main()

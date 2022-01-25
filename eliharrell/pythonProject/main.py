# This is a sample Python script.
import ee
ee.Authenticate()
ee.Initialize()

landsat = False
sentinel_collection = "COPERNICUS/S2_SR"
landsat_collection = "LANDSAT/S2_SR"
if landsat:
    collection = "LANDSAT/S2_SR"
else:
    collection = "COPERNICUS/S2_SR"

col_sent = ee.ImageCollection(collection)

if landsat:
    clouds = 'CLOUD_COVER'
else:
    clouds = 'CLOUDY_PIXEL_PERCENTAGE'

clouds = col_sent.filter()

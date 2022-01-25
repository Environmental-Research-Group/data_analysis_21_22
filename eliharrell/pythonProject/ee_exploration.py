import ee
ee.Authenticate()
ee.Initialize()

landsat = True
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

var dataset = ee.Image('AHN/AHN2_05M_RUW');
var elevation = dataset.select('elevation');
var elevationVis = {
  min: -5.0,
  max: 30.0,
};
Map.setCenter(5.76583, 51.855276, 16);
Map.addLayer(elevation, elevationVis, 'Elevation');
import ee

# Initialize the Earth Engine module.
ee.Initialize()

# Print metadata for a DEM dataset.
if __name__ == '__main__':
   print(ee.Image('USGS/SRTMGL1_003').getInfo())


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import ee

# Initialize the Earth Engine module.
ee.Initialize()

# Print metadata for a DEM dataset.
if __name__ == '__main__':
   print(ee.Image('USGS/SRTMGL1_003').getInfo())

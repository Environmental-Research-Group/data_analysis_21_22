import ee
ee.Initialize()
if __name__=='__main__':
    print(ee.Image('USGS/SRTMGL1_003').getInfo())
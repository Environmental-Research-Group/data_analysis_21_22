import ee

ee.initialize()

if __name__ == '__main__':
    print(ee.image('USGS/SRTMGL1_003').getInfo())
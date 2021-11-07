from snappy import ProductIO
import snappy
import jpy

def LatLon_from_XY(product, x, y):
    geoPosType = jpy.get_type('org.esa.snap.core.datamodel.GeoPos')
    geocoding = product.getSceneGeoCoding()
    geo_pos = geocoding.getGeoPos(snappy.PixelPos(x, y), geoPosType())
    if str(geo_pos.lat)=='nan':
        raise ValueError('x, y pixel coordinates not in this product')
    else:
        return geo_pos.lat, geo_pos.lon


def main():
    pass


if __name__ == "__main__":

    main()
import shapefile
class Belajar(object):
    def __init__(self,namafile):
        self.sf = shapefile.Reader(namafile)
    def hitungGaris(self):
        rec = self.sf.shapes()
        return len(rec)
    def selectCountries(self,COUNTRIES):
        i = 0
        for a in self.sf.records():
            if a[8] == COUNTRIES:
                return i
            i = i + 1
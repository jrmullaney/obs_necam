from lsst.pipe.tasks.ingest import ParseTask
from astropy.time import Time
import re
    
class NecamParseTask(ParseTask):

    def translateDate(self, md):

        date = md.get("DATE-OBS")
        date = [date[0:4], date[4:6], date[6:]]
        date = '-'.join(date)
        t = Time(date, format='iso', out_subfmt='date').iso
                
        return t
     
"""

 Summary:
    Contains the Conduit unit type classes.
    This holds all of the data read in from the culvert units in the dat file.
    Can be called to load in the data and read and update the contents 
    held in the object.

 Author:  
     Matthew Shallcross

 Copyright:  
     Duncan Runnacles 2016

 TODO:

 Updates:

"""


from ship.isis.datunits.isisunit import AIsisUnit
from ship.data_structures.rowdatacollection import RowDataCollection
from ship.isis.datunits import ROW_DATA_TYPES as rdt
from ship.data_structures import dataobject as do

import logging
logger = logging.getLogger(__name__)
"""logging references with a __name__ set to this module."""


class SymmetricalConduitUnit(AIsisUnit):
    '''Class for dealing with SymmetricalConduit units in the .dat file.'''

    # Class constants
    UNIT_TYPE = 'Symmetrical Conduit'
    CATEGORY = 'Conduit'
    FILE_KEY = 'CONDUIT'
    

    def __init__(self):
        '''Constructor.
        '''
        AIsisUnit.__init__(self)
        self.unit_type = SymmetricalConduitUnit.UNIT_TYPE
        self.unit_category = SymmetricalConduitUnit.CATEGORY
        self.has_datarows = True
        self.has_ics = True
        
        self.head_data = {'section_label': 'SymConduit', 'spill': '',
                          'distance': 0.0, 'rowcount': 0 }

        self.row_collection = RowDataCollection()
        self.row_collection.initCollection(do.FloatData(0, rdt.CHAINAGE, format_str='{:>10}', no_of_dps=3))
        self.row_collection.initCollection(do.FloatData(1, rdt.ELEVATION, format_str='{:>10}', no_of_dps=3))
        self.row_collection.initCollection(do.FloatData(2, rdt.COLEBROOK, format_str='{:>10}', no_of_dps=5))
        
    def readUnitData(self, unit_data, file_line):
        """Reads the unit data into the geometry objects.
        
        See Also:
            AIsisUnit - readUnitData for more information.
        
        Args:
            unit_data (list): The section of the isis dat file pertaining 
                to this section 
        """
        file_line = self._readHeadData(unit_data, file_line)
        file_line = self._readRowData(unit_data, file_line)
        self.head_data['rowcount'] = self.row_collection.getNumberOfRows()
        return file_line - 1
        

    def _readHeadData(self, unit_data, file_line):            
        """Format the header data for writing to file.
        
        Args:
            unit_data (list): containing the data to read.
        """
        self.head_data['comment'] = unit_data[file_line + 0][8:].strip()
        self._name = self.head_data['section_label'] = unit_data[file_line + 2][:12].strip()
        self.head_data['spill'] = unit_data[file_line + 2][12:].strip()
        self.head_data['distance'] = unit_data[file_line + 3][0:10].strip()
        self.unit_length = int(unit_data[file_line + 4].strip())
        return file_line + 5
 
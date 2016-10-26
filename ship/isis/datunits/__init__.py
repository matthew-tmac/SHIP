from ship.utils import utilfunctions as uf

"""Enum for all row data keys used in Isis units.

The 'QMARK' relates to the '?' in the initial conditions part of the .dat file.
"""
ROW_DATA_TYPES = uf.enum('CHAINAGE', 'ELEVATION', 'ROUGHNESS', 'PANEL_MARKER',
                         'RPL', 'BANKMARKER', 'EASTING', 'NORTHING', 
                         'DEACTIVATION', 'SPECIAL', 'EMBANKMENT', 'OPEN_START',
                         'OPEN_END', 'SPRINGING_LEVEL', 'SOFFIT_LEVEL', 
                         'CULVERT_INVERT', 'CULVERT_SOFFIT', 'CULVERT_AREA',
                         'CULVERT_CD_PART', 'CULVERT_CD_FULL', 
                         'CULVERT_DROWNING', 'TIME', 'LABEL', 'FLOW', 'STAGE',
                         'FROUDE_NO', 'VELOCITY', 'UMODE', 'USTATE', 'QMARK', 'COLEBROOK') 

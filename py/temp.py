

class Token(object):
    """Represents a part of an address string"""
    Name = None         # short name for this token
    ColumnName = None   # corresponding column name in spreadsheet
    Optional = False    # If true, this token may not be present
    Regex = '\w'       # Regular expression to match

    def __init__(self, regex=None, optional=False):
        if regex is not None:
            self.Regex = regex
        self.Optional = optional

class StreetNumber(Token):
    """Number of a street"""
    Name = "num"
    ColumnName = 'street_number'
    Regex = '\d+'
    
class StreetName(Token):
    """Name of the street"""
    Name = 's1'
    ColumnName = 'street_name'
    
class CrossStreet(Token):
    """Name of the cross street"""
    Name = 's2'
    ColumnName = 'cross_street'

class Relation(Token):
    """Directional relation between address and actual point (N/S/E/W/etc)"""
    Name = 'rel'
    ColumnName = 'relation'

class Distance(Token):
    """Distance between geocoded point and actual point"""
    Name = 'dist'
    ColumnName = 'distance_offset'
    Regex = '\d+(?:\.\d*)?\s*(?:m|miles|mi|feet|yards|meters)?'

class Whitespace(Token):
    """Represents non-essential space characters.  Also includes '.,;'"""
    Name = 'space'
    ColumnName = None
    Regex = '[\s,;.]+'

class AddressParser(object):
    pass


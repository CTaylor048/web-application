from collections.abc import Callable, Iterable, Mapping
import datetime, inspect, json, math, os, re, socket, time, threading
from queue import Queue

"""
-----------------------------------DATA-TYPES-----------------------------------
address
address-ip
address-ip-benchmarking
address-ip-local
address-ip-local-link
address-ip-local-unique
address-ip-loopback
address-ip-multicast
address-ip-unspecified
address-ipv4
address-ipv4-benchmarking
address-ipv4-broadcast
address-ipv4-dummy
address-ipv4-local
address-ipv4-local-link
address-ipv4-local-unique
address-ipv4-loopback
address-ipv4-mask
address-ipv4-multicast
address-ipv4-netmask
address-ipv4-networkmask
address-ipv4-prefix-length
address-ipv4-subnetmask
address-ipv4-subnetworkmask
address-ipv4-unicast
address-ipv4-unspecified
address-ipv4-wildcardmask
address-ipv6
address-ipv6-4to6
address-ipv6-ipv4-mapped
address-ipv6-6to4
address-ipv6-anycast
address-ipv6-benchmarking
address-ipv6-documentation
address-ipv6-global
address-ipv6-local
address-ipv6-local-link
address-ipv6-local-unique
address-ipv6-loopback
address-ipv6-multicast
address-ipv6-teredo
address-ipv6-unspecified
address-mac-broadcast
address-mac-multicast
address-mac-multicast-ipv4
address-mac-multicast-ipv6
address-mac-unicast
array
array-boolean
array-bytes
array-number
array-object
array-string
array-string-array
array-string-array-object
array-string-boolean
array-string-number
array-string-object
base64
binary
boolean
bytes
bytes-array
bytes-array-object
bytes-object
character
coordinates-geographic
coordinates-geographic-ddd
coordinates-geographic-ddm
coordinates-geographic-dms
coordinates-geographic-latitude
coordinates-geographic-latitude-ddd
coordinates-geographic-latitude-ddm
coordinates-geographic-latitude-dms
coordinates-geographic-longitude
coordinates-geographic-longitude-ddd
coordinates-geographic-longitude-ddm
coordinates-geographic-longitude-dms
date
decimal
hexadecimal
html
html-tag
identifier
number
number-float
number-integer
object
octal
port
port-ephemeral
port-ephemeral-dynamic
port-ephemeral-private
port-ephemeral-registered
port-ephemeral-unregistered
port-nonephemeral
port-wellknown
string
string-array
string-array-object
string-boolean
string-number
string-number-float
string-number-integer
string-object
timestamp
timestamp-date
timestamp-time
timestamp-zone
url

--------------------------------------------------------------------------------
ip   | internet_protocol
ipv4 | internet_protocol_v4
ipv6 | internet_protocol_v6
mac  | media_access_control
"""

"""
-------------------------------------ERRORS-------------------------------------
ArrayLengthError: variable-name={} variable-length={len()} length=<eq|ge|gt|le|lt>{}
ClipboardCopyError: 
DepreciationError: name={} value={}
DirectoryNotFoundError: path={}
FileNotFoundError: path={}
FileSizeError: file-path={} file-size={} size=<eq|ge|gt|le|lt>{} (bytes)
KeyError: variable-name= key={}
IndexError: variable-name={} variable-length={len()} index={}
ParseHTTPBytesError
StringLengthError: variable-name={} variable-length={len()} length=<eq|ge|gt|le|lt>{}
SendPacketError
TypeError: variable-name= variable-value={} variable-type={type()} type=
UnsetError: variable-name=
ValueError: variable-name= variable-value={}

-------------------------------REGULAR-EXPRESSIONS------------------------------
\[(.+):\]                           .slice($1)
\[:(.+)\]                           .slice(0, $1)
\[(.+):(.+)\]                       .slice($1, $2)
\[(.+):(.+)\[(.+):\](.+)?\]         .slice($1, $2.slice($3)$4)
\[(.+):(.+)\[(.+):(.+)\](.+)?\]     .slice($1, $2.slice($3, $4)$5)
.slice\((.+)\)                      [$1:]
.slice\(0, (.+)\)                   [:$1]
.slice\((.+), (.+)\)                [$1:$2]
(\w+).length                        len($1)
len\((\w+)\)                        $1.length
f"(.+)"                             `$1`
`(.+)`                              f"$1"
(\{)                                $$$1
= (.+) if (.+) else (.+)            = $2 ? $1 : $3
= (.+) ? (.+) : (.+)                = $2 if $1 else $3

----------------------------OBJECT-INSTANCE-ACCESS------------------------------
print(util.dump(globals()))
getattr(globals()['app'], 'main')
getattr(globals().get('app'), 'main')

--------------------------------------------------------------------------------
"C:\Program Files (x86)\VSCode\resources\app\out\vs\workbench\contrib\terminal\browser\media\shellIntegration.ps1"
util.system_log(__file__, inspect.currentframe().f_lineno, f"")
"""

class util:
    """
    Utilities

    1.  Description: 
    
    2.  Class Attributes: 
    
    3.  Instance Attributes: 
    
    4.  Class Functions: 

    5.  Instance Functions: 

    """
    def __init__(self):
        pass
    
    DEGREES_TO_RADIANS = math.pi / 180
    RADIANS_TO_DEGREES = 180 / math.pi
    SPHERE_RADIUS = 6371000

    FILE_TIMESTAMP_MILLISECONDS = 'milliseconds'
    FILE_TIMESTAMP_SECONDS = 'seconds'

    GEOGRAPHIC_COORDINATES_PATTERN_DECIMAL_DEGREES_LATITUDE = r"(?P<decimal_degrees>(-|\+)?([0-9]|[0-8][0-9])(\.\d+)?)"
    GEOGRAPHIC_COORDINATES_PATTERN_DECIMAL_DEGREES_LONGITUDE = r"(?P<decimal_degrees>(-|\+)?([0-9]|[0-9][0-9]|0[0-9][0-9]|1[0-7][0-9])(\.\d+)?)"
    GEOGRAPHIC_COORDINATES_PATTERN_DECIMAL_MINUTES = r"(?P<decimal_minutes>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9][0-9]))"
    GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LATITUDE = r"(?P<degrees>[0-8][0-9])"
    GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LONGITUDE = r"(?P<degrees>0[0-9][0-9]|1[0-7][0-9])"
    GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LATITUDE = r"(?P<direction>N|S)"
    GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LONGITUDE = r"(?P<direction>E|W)"
    GEOGRAPHIC_COORDINATES_PATTERN_MINUTES = r"(?P<minutes>0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])"
    GEOGRAPHIC_COORDINATES_PATTERN_SECONDS = r"(?P<seconds>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(\.\d+)?)"
    GEOGRAPHIC_COORDINATES_DDM_PATTERN_LATITUDE_OPT1 = r"^(?P<degrees>[0-8][0-9])(?P<decimal_minutes>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9][0-9]))(?P<direction>N|S)$"
    GEOGRAPHIC_COORDINATES_DDM_PATTERN_LATITUDE_OPT2 = r"^(?P<degrees>[0-9]|[0-8][0-9])(°|\*)?(?P<decimal_minutes>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9]|[0-9][0-9]))'?(?P<direction>N|S)$"
    GEOGRAPHIC_COORDINATES_DDM_PATTERN_LONGITUDE_OPT1 = r"^(?P<degrees>0[0-9][0-9]|1[0-7][0-9])(?P<decimal_minutes>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9][0-9]))(?P<direction>E|W)$"
    GEOGRAPHIC_COORDINATES_DDM_PATTERN_LONGITUDE_OPT2 = r"^(?P<degrees>[0-9]|0[0-9][0-9]|1[0-7][0-9])(°|\*)?(?P<decimal_minutes>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9]|[0-9][0-9]))'?(?P<direction>E|W)$"
    GEOGRAPHIC_COORDINATES_DMS_PATTERN_LATITUDE_OPT1 = r"^(?P<degrees>[0-8][0-9])(?P<minutes>0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(?P<seconds>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(\.\d+)?)(?P<direction>N|S)$"
    GEOGRAPHIC_COORDINATES_DMS_PATTERN_LATITUDE_OPT2 = r"^(?P<degrees>[0-9]|[0-8][0-9])(°|\*)?(?P<minutes>[0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])'?(?P<seconds>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(\.\d+)?)\"?(?P<direction>N|S)$"
    GEOGRAPHIC_COORDINATES_DMS_PATTERN_LONGITUDE_OPT1 = r"^(?P<degrees>0[0-9][0-9]|1[0-7][0-9])(?P<minutes>0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(?P<seconds>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(\.\d+)?)(?P<direction>E|W)$"
    GEOGRAPHIC_COORDINATES_DMS_PATTERN_LONGITUDE_OPT2 = r"^(?P<degrees>[0-9]|[0-9][0-9]|0[0-9][0-9]|1[0-7][0-9])(°|\*)?(?P<minutes>[0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])'?(?P<seconds>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(\.\d+)?)\"?(?P<direction>E|W)$"

    HASH_MD5 = 'md5'
    HASH_SHA1 = 'sha1'
    HASH_SHA224 = 'sha224'
    HASH_SHA256 = 'sha256'
    HASH_SHA384 = 'sha384'
    HASH_SHA512 = 'sha512'

    NUMBER_PLACEMENT = {
        13:  'trillions',
        12:  'hundred billions',
        11:  'ten billions',
        10:  'billions',
         9:  'hundred millions',
         8:  'ten millions',
         7:  'millions',
         6:  'hundred thousands',
         5:  'ten thousands',
         4:  'thousands',
         3:  'hundreds',
         2:  'tens',
         1:  'ones',
         0:  '',
        -1:  'tenths', 
        -2:  'hundredths',
        -3:  'thousandths',
        -4:  'ten thousandths',
        -5:  'hundred thousandths',
        -6:  'millionths',
        -7:  'ten millionths',
        -8:  'hundred millionths',
        -9:  'billionths',
        -10: 'ten billionths',
        -11: 'hundred billionths',
        -12: 'trillionths',
        -13: 'ten trillionths', 
        -14: 'hundred trillionths'
    }

    REFERENCE_TAG_ABBREVIATIONS = 'ABBREVIATIONS'
    REFERENCE_TAG_ACRONYMS = 'ACRONYMS'
    REFERENCE_TAG_DEFINITIONS = 'DEFINITIONS'
    REFERENCE_TAG_LIST = 'LIST'
    REFERENCE_TAG_NAME = 'NAME'
    REFERENCE_TAG_OBJECT = 'OBJECT'
    REFERENCE_TAG_QUESTIONS = 'QUESTIONS'
    REFERENCE_TAG_SOURCE = 'SOURCE'
    REFERENCE_TAG_SUBTITLE = 'SUBTITLE'
    REFERENCE_TAG_TABLE = 'TABLE'
    REFERENCE_TAG_TITLE = 'TITLE'

    TABLE_ORIENTATION_VERTICAL = 'vertical'
    TABLE_ORIENTATION_HORIZONTAL = 'horizontal'

    TIME_DAYS_OF_WEEK = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    TIME_MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    TIME_QUARTERS = ['First', 'Second', 'Third', 'Fourth']

    TIMESTAMP_OPTION_MILLISECONDS = 'milliseconds'
    TIMESTAMP_OPTION_OBJECT = 'object'
    TIMESTAMP_OPTION_SECONDS = 'seconds'
    TIMESTAMP_OPTION_STRING = 'string'

    TIMESTAMP_PATTERN_YEAR = r"(?P<year>19[7-9][0-9]|[2-9][0-9][0-9][0-9])"
    TIMESTAMP_PATTERN_MONTH = r"(?P<month>0[1-9]|1[0-2])"
    TIMESTAMP_PATTERN_DAY = r"(?P<day>0[1-9]|1[0-9]|2[0-9]|3[0-2])"
    TIMESTAMP_PATTERN_HOUR = r"(?P<hour>0[0-9]|1[0-9]|2[0-3])"
    TIMESTAMP_PATTERN_MINUTE = r"(?P<minute>0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])"
    TIMESTAMP_PATTERN_SECOND = r"(?P<second>0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])"
    TIMESTAMP_PATTERN_MILLISECOND = r"(?P<millisecond>\d\d\d)?"
    TIMESTAMP_PATTERN_ZONE = r"(?P<zone>[A-I]|[K-Z])?"

    TIMEZONE_DESIGNATIONS = {
        'A': 'Etc/GMT-1',
        'B': 'Etc/GMT-2',
        'C': 'Etc/GMT-3',
        'D': 'Etc/GMT-4',
        'E': 'Etc/GMT-5',
        'F': 'Etc/GMT-6',
        'G': 'Etc/GMT-7',
        'H': 'Etc/GMT-8',
        'I': 'Etc/GMT-9',
        'K': 'Etc/GMT-10',
        'L': 'Etc/GMT-11',
        'M': 'Etc/GMT-12',
        'N': 'Etc/GMT+1',
        'O': 'Etc/GMT+2',
        'P': 'Etc/GMT+3',
        'Q': 'Etc/GMT+4',
        'R': 'Etc/GMT+5',
        'S': 'Etc/GMT+6',
        'T': 'Etc/GMT+7',
        'U': 'Etc/GMT+8',
        'V': 'Etc/GMT+9',
        'W': 'Etc/GMT+10',
        'X': 'Etc/GMT+11',
        'Y': 'Etc/GMT+12',
        'Z': 'GMT',
    }
    TIMEZONE_DESIGNATION_OFFSETS = {
        'A': +1,
        'B': +2,
        'C': +3,
        'D': +4,
        'E': +5,
        'F': +6,
        'G': +7,
        'H': +8,
        'I': +9,
        'K': +10,
        'L': +11,
        'M': +12,
        'N': -1,
        'O': -2,
        'P': -3,
        'Q': -4,
        'R': -5,
        'S': -6,
        'T': -7,
        'U': -8,
        'V': -9,
        'W': -10,
        'X': -11,
        'Y': -12,
        'Z': +0,
    }
 
    path: str = 'c:\\projects'
    variables: dict[str, str] = {
        'root-certificate-authority-path': 'c:\\projects\\.certificates\\root-certificate-authority\\1', 
        'root-certificate-authority-certificate': 'c:\\projects\\.certificates\\root-certificate-authority\\1\\root-ca.pem', 
        'root-certificate-authority-privatekey': 'c:\\projects\\.certificates\\root-certificate-authority\\1\\root-ca.key', 
        'intermediate-certificate-authority-path': 'c:\\projects\\.certificates\\intermediate-certificate-authority', 
        'client-certificate-path': 'c:\\projects\\.certificates\\root-certificate-authority\\1', 
        'client-certificate': 'c:\\projects\\.certificates\\root-certificate-authority\\1\\root-ca.pem', 
        'client-privatekey': 'c:\\projects\\.certificates\\root-certificate-authority\\1\\root-ca.key', 
        'web-server-path': 'c:\\projects\\.certificates\\web-server\\14', 
        'web-server-certificate': 'c:\\projects\\.certificates\\web-server\\14\\projects.pem', 
        'web-server-privatekey': 'c:\\projects\\.certificates\\web-server\\14\\projects.key', 
        'vpn-server-path': 'c:\\projects\\.certificates\\vpn-server\\0', 
        'vpn-server-certificate': 'c:\\projects\\.certificates\\vpn-server\\0\projects.pem', 
        'vpn-server-privatekey': 'c:\\projects\\.certificates\\vpn-server\\0\\projects.key', 
    }

    """
    COORDINATES
    cartesian   = (x, y, z)
    cylindrical = (r, azimuth, height)
    geographic  = (latitude, longitude, altitude)
    polar       = (r, theta)
    spherical   = (r, theta, phi)
    """

    def arguments(parameters: dict[str]|list[str], arguments: list[str]):
        object = {}
        if isinstance(parameters, dict):
            for index, key in enumerate(parameters.keys()):
                object[key] = arguments[index] if len(arguments) > index else parameters[key]
        if isinstance(parameters, list):
            for index, key in enumerate(parameters):
                object[key] = arguments[index] if len(arguments) > index else ''
        return object
    def ispattern(value: str, pattern: str) -> bool:
        return bool(re.match(pattern, value))
    def istype(value, types: str):
        if value == None: return False
        def toBinary(value: str, type: str) -> str:
            if bool(re.match(r"^(0|1)+$", value)):
                return value
            elif type.startswith('address-ipv4') or type.startswith('address-internet_protocol_v4'):
                return util.address_ipv4(value)
            elif type.startswith('address-ipv6') or type.startswith('address-internet_protocol_v6'):
                return util.address_ipv6(value)
            elif type.startswith('address-mac') or type.startswith('address-media_access_control'):
                return util.address_mac(value)
        def istype(value, type: str):
            if type == 'address':
                return istype(value, 'address-ipv4') or istype(value, 'address-ipv6') or istype(value, 'address-mac')
            if type == 'address-ip' or type == 'address-internet_protocol':
                return istype(value, 'address-ipv4') or istype(value, 'address-ipv6')
            if type == 'address-ip-local' or type == 'address-internet_protocol-local':
                return istype(value, 'address-ipv4-local') or istype(value, 'address-ipv6-local')
            if type == 'address-ip-local-link' or type == 'address-internet_protocol-local-link':
                return istype(value, 'address-ipv4-local-link') or istype(value, 'address-ipv6-local-link')
            if type == 'address-ip-local-unique' or type == 'address-internet_protocol-local-unique':
                return istype(value, 'address-ipv4-local-unique') or istype(value, 'address-ipv6-local-unique')
            if type == 'address-ip-loopback' or type == 'address-internet_protocol-loopback':
                return istype(value, 'address-ipv4-loopback') or istype(value, 'address-ipv6-loopback')
            if type == 'address-ip-multicast' or type == 'address-internet_protocol-multicast':
                return istype(value, 'address-ipv4-multicast') or istype(value, 'address-ipv6-multicast')
            if type == 'address-ip-unspecified' or type == 'address-internet_protocol-unspecified':
                return istype(value, 'address-ipv4-unspecified') or istype(value, 'address-ipv6-unspecified')
            if type == 'address-ipv4' or type == 'address-internet_protocol_v4':
                if istype(value, 'string'):
                    if istype(value, 'binary'):
                        return len(value) == 32
                    else:
                        assert isinstance(value, str)
                        strings = value.split('.')
                        if len(strings) == 4:
                            for string in strings:
                                if len(string) < 0 or len(string) > 3: return False
                                if not istype(string, 'string-number'): return False
                                if int(string) < 0 or int(string) > 255: return False
                            return True
            if type == 'address-ipv4-benchmarking' or type == 'address-internet_protocol_v4-benchmarking':
                if istype(value, 'address-ipv4'):
                    value = toBinary(value, type)
                    return value[0:15] == '110001100001001'
            if type == 'address-ipv4-broadcast' or type == 'address-internet_protocol_v4-broadcast':
                if istype(value, 'address-ipv4'):
                    value = toBinary(value, type)
                    return value == '11111111111111111111111111111111'
            if type == 'address-ipv4-dummy' or type == 'address-internet_protocol_v4-dummy':
                if istype(value, 'address-ipv4'):
                    value = toBinary(value, type)
                    return value == '11000000000000000000000000001000'
            if type == 'address-ipv4-local' or type == 'address-internet_protocol_v4-local':
                return istype(value, 'address-ipv4-local-link') or istype(value, 'address-ipv4-local-unique')
            if type == 'address-ipv4-local-link' or type == 'address-internet_protocol_v4-local-link':
                if istype(value, 'address-ipv4'):
                    value = toBinary(value, type)
                    return value[0:16] == '1010100111111110'
            if type == 'address-ipv4-local-unique' or type == 'address-internet_protocol_v4-local-unique':
                if istype(value, 'address-ipv4'):
                    value = toBinary(value, type)
                    return value[0:8] == '10100000' or value[0:12] == '101011000001' or value[0:16] == '1100000010101000'
            if type == 'address-ipv4-loopback' or type == 'address-internet_protocol_v4-loopback':
                if istype(value, 'address-ipv4'):
                    value = toBinary(value, type)
                    return value[0:8] == '01111111'
            if type == 'address-ipv4-mask' or type == 'address-internet_protocol_v4-mask':
                return istype(value, 'address-ipv4-netmask') or istype(value, 'address-ipv4-subnetmask') or istype(value, 'address-ipv4-wildcardmask')
            if type == 'address-ipv4-multicast' or type == 'address-internet_protocol_v4-multicast':
                if istype(value, 'address-ipv4'):
                    value = toBinary(value, type)
                    return value[0:4] == '1110'
            if type == 'address-ipv4-netmask' or type == 'address-internet_protocol_v4-netmask':
                if istype(value, 'address-ipv4'):
                    value = toBinary(value, type)
                    if '0' in value:
                        return value.find('0') > value.rfind('1')
                    else:
                        return value == '11111111111111111111111111111111'
            if type == 'address-ipv4-networkmask' or type == 'address-internet_protocol_v4-networkmask':
                if istype(value, 'address-ipv4'):
                    value = toBinary(value, type)
                    if '0' in value:
                        return value.find('0') > value.rfind('1')
                    else:
                        return value == '11111111111111111111111111111111'
            if type == 'address-ipv4-prefix-length' or type == 'address-internet_protocol_v4-prefix-length':
                if istype(value, 'number') or istype(value, 'string-number'):
                    return bool(re.match(r"^(0?[0-9]|1[0-9]|2[0-9]|3[1-2])$", f"{value}"))
            if type == 'address-ipv4-subnetmask' or type == 'address-internet_protocol_v4-subnetmask':
                if istype(value, 'address-ipv4'):
                    value = toBinary(value, type)
                    if '0' in value:
                        return value.find('0') > value.rfind('1')
                    else:
                        return value == '11111111111111111111111111111111'
            if type == 'address-ipv4-subnetworkmask' or type == 'address-internet_protocol_v4-subnetworkmask':
                if istype(value, 'address-ipv4'):
                    value = toBinary(value, type)
                    if '0' in value:
                        return value.find('0') > value.rfind('1')
                    else:
                        return value == '11111111111111111111111111111111'
            if type == 'address-ipv4-unicast' or type == 'address-internet_protocol_v4-unicast':
                if istype(value, 'address-ipv4'):
                    return not (istype(value, 'address-ipv4-broadcast') or istype(value, 'address-ipv4-dummy') or istype(value, 'address-ipv4-mask') or istype(value, 'address-ipv4-multicast') or istype(value, 'address-ipv4-unspecified'))
            if type == 'address-ipv4-unspecified' or type == 'address-internet_protocol_v4-unspecified':
                if istype(value, 'address-ipv4'):
                    value = toBinary(value, type)
                    return value == '00000000000000000000000000000000'
            if type == 'address-ipv4-wildcardmask' or type == 'address-internet_protocol_v4-wildcardmask':
                if istype(value, 'address-ipv4'):
                    value = toBinary(value, type)
                    if '1' in value:
                        return value.find('1') > value.rfind('0')
                    else:
                        return value == '00000000000000000000000000000000'
            if type == 'address-ipv6' or type == 'address-internet_protocol_v6':
                if istype(value, 'string'):
                    if istype(value, 'binary'):
                        return len(value) == 128
                    else:
                        assert isinstance(value, str)
                        strings = value.split(':')
                        if len(strings) == 8:
                            for string in strings:
                                if len(string) < 0 or len(string) > 4: return False
                                if not istype(string, 'hexadecimal'): return False
                            return True
                        elif '::' in value:
                            return bool(re.match(r"^(:|[0-9]|[A-F]|[a-f])+$", value)) and len(value) <= 39
            if type == 'address-ipv6-4to6' or type == 'address-internet_protocol_v6-4to6':
                if istype(value, 'address-ipv6'):
                    value = toBinary(value, type)
                    return value[0:96] == '000000000000000000000000000000000000000000000000000000000000000000000000000000001111111111111111'
            if type == 'address-ipv6-ipv4-mapped' or type == 'address-internet_protocol_v6-internet_protocol_v4-mapped':
                if istype(value, 'address-ipv6'):
                    value = toBinary(value, type)
                    return value[0:96] == '000000000000000000000000000000000000000000000000000000000000000000000000000000001111111111111111'
            if type == 'address-ipv6-6to4' or type == 'address-internet_protocol_v6-6to4':
                if istype(value, 'address-ipv6'):
                    value = toBinary(value, type)
                    return value[0:16] == '0010000000000010'
            if type == 'address-ipv6-anycast' or type == 'address-internet_protocol_v6-anycast':
                return istype(value, 'address-ipv6-global')
            if type == 'address-ipv6-benchmarking' or type == 'address-internet_protocol_v6-benchmarking':
                if istype(value, 'address-ipv6'):
                    value = toBinary(value, type)
                    return value[0:48] == '001000000000000100000000000000100000000000000000'
            if type == 'address-ipv6-documentation' or type == 'address-internet_protocol_v6-documentation':
                if istype(value, 'address-ipv6'):
                    value = toBinary(value, type)
                    return value[0:32] == '00100000000000010000110110111000'
            if type == 'address-ipv6-global' or type == 'address-internet_protocol_v6-global':
                if istype(value, 'address-ipv6'):
                    value = toBinary(value, type)
                    return value[0:3] == '001'
            if type == 'address-ipv6-local' or type == 'address-internet_protocol_v6-local':
                return istype(value, 'address-ipv6-local-link') or istype(value, 'address-ipv6-local-unique')
            if type == 'address-ipv6-local-link' or type == 'address-internet_protocol_v6-local-link':
                if istype(value, 'address-ipv6'):
                    value = toBinary(value, type)
                    return value[0:10] == '1111111010'
            if type == 'address-ipv6-local-unique' or type == 'address-internet_protocol_v6-local-unique':
                if istype(value, 'address-ipv6'):
                    value = toBinary(value, type)
                    return value[0:7] == '1111110'
            if type == 'address-ipv6-loopback' or type == 'address-internet_protocol_v6-loopback':
                if istype(value, 'address-ipv6'):
                    value = toBinary(value, type)
                    return value == '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001'
            if type == 'address-ipv6-multicast' or type == 'address-internet_protocol_v6-multicast':
                if istype(value, 'address-ipv6'):
                    value = toBinary(value, type)
                    return value[0:8] == '11111111'
            if type == 'address-ipv6-teredo' or type == 'address-internet_protocol_v6-teredo':
                if istype(value, 'address-ipv6'):
                    value = toBinary(value, type)
                    return value[0:32] == '00100000000000010000000000000000'
            if type == 'address-ipv6-unspecified' or type == 'address-internet_protocol_v6-unspecified':
                if istype(value, 'address-ipv6'):
                    value = toBinary(value, type)
                    return value == '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
            if type == 'address-mac' or type == 'address-media_access_control':
                if istype(value, 'string'):
                    if istype(value, 'binary'):
                        return len(value) == 48
                    else:
                        assert isinstance(value, str)
                        strings = value.split('-')
                        if len(strings) == 6:
                            for string in strings:
                                if len(string) != 2: return False
                                if not istype(string, 'hexadecimal'): return False
                            return True
            if type == 'address-mac-broadcast' or type == 'address-media_access_control-broadcast':
                if istype(value, 'address-mac'):
                    value = toBinary(value, type)
                    return value == '111111111111111111111111111111111111111111111111'
            if type == 'address-mac-multicast' or type == 'address-media_access_control-multicast':
                return istype(value, 'address-mac-multicast-ipv4') or istype(value, 'address-mac-multicast-ipv6')
            if type == 'address-mac-multicast-ipv4' or type == 'address-media_access_control-multicast-internet_protocol_v4':
                if istype(value, 'address-mac'):
                    value = toBinary(value, type)
                    return value[0:25] == '0000000100000000010111100'
            if type == 'address-mac-multicast-ipv6' or type == 'address-media_access_control-multicast-internet_protocol_v6':
                if istype(value, 'address-mac'):
                    value = toBinary(value, type)
                    return value[0:16] == '0011001100110011'
            if type == 'address-mac-unicast' or type == 'address-media_access_control-unicast':
                if istype(value, 'address-mac'):
                    return not (istype(value, 'address-mac-broadcast') or istype(value, 'address-mac-multicast'))
            if type == 'array':
                return isinstance(value, array) or isinstance(value, list)
            if type == 'array-boolean':
                if istype(value, 'array'):
                    for value_ in value:
                        if not istype(value_, 'boolean'): return False
                    return True
            if type == 'array-bytes':
                if istype(value, 'array'):
                    for value_ in value:
                        if not istype(value_, 'bytes'): return False
                    return True
            if type == 'array-number':
                if istype(value, 'array'):
                    for value_ in value:
                        if not istype(value_, 'number'): return False
                    return True
            if type == 'array-object':
                if istype(value, 'array'):
                    for value_ in value:
                        if not istype(value_, 'object'): return False
                    return True
            if type == 'array-string':
                if istype(value, 'array'):
                    for value_ in value:
                        if not istype(value_, 'string'): return False
                    return True
            if type == 'array-string-array':
                if istype(value, 'array'):
                    for value_ in value:
                        if not istype(value_, 'string-array'): return False
                    return True
            if type == 'array-string-array-object':
                if istype(value, 'array'):
                    for value_ in value:
                        if not istype(value_, 'string-array-object'): return False
                    return True
            if type == 'array-string-boolean':
                if istype(value, 'array'):
                    for value_ in value:
                        if not istype(value_, 'string-boolean'): return False
                    return True
            if type == 'array-string-number':
                if istype(value, 'array'):
                    for value_ in value:
                        if not istype(value_, 'string-number'): return False
                    return True
            if type == 'array-string-object':
                if istype(value, 'array'):
                    for value_ in value:
                        if not istype(value_, 'string-object'): return False
                    return True
            if type == 'base64':
                if istype(value, 'string'):
                    return bool(re.match(r"^(\+|/|[0-9]|=|[A-Z]|[a-z])+$", value))
            if type == 'binary':
                if istype(value, 'string'):
                    return bool(re.match(r"^(0|1)+$", value))
            if type == 'boolean':
                return isinstance(value, bool)
            if type == 'bytes':
                return isinstance(value, bytes) or isinstance(value, bytearray)
            if type == 'bytes-array':
                if istype(value, 'bytes'):
                    return istype(util.byt2str(value), 'string-array')
            if type == 'bytes-array-object':
                if istype(value, 'bytes'):
                    return istype(util.byt2str(value), 'string-array-object')
            if type == 'bytes-object':
                if istype(value, 'bytes'):
                    return istype(util.byt2str(value), 'string-object')
            if type == 'character':
                if istype(value, 'string'):
                    return bool(re.match(r"^([A-Z]|[a-z])$", value))
            if type == 'coordinates-geographic':
                return istype(value, 'coordinates-geographic-ddd') or istype(value, 'coordinates-geographic-ddm') or istype(value, 'coordinates-geographic-dms')
            if type == 'coordinates-geographic-ddd':
                if istype(value, 'string'):
                    return istype(value, 'coordinates-geographic-latitude-ddd') or istype(value, 'coordinates-geographic-longitude-ddd')
                elif istype(value, 'array-number') or istype(value, 'array-string'):
                    if len(value) == 2:
                        return istype(value[0], 'coordinates-geographic-latitude-ddd') and istype(value[1], 'coordinates-geographic-longitude-ddd')
            if type == 'coordinates-geographic-ddm':
                if istype(value, 'string'):
                    return istype(value, 'coordinates-geographic-latitude-ddm') or istype(value, 'coordinates-geographic-longitude-ddm')
                elif istype(value, 'array-string'):
                    if len(value) == 2:
                        return istype(value[0], 'coordinates-geographic-latitude-ddm') and istype(value[1], 'coordinates-geographic-longitude-ddm')
            if type == 'coordinates-geographic-dms':
                if istype(value, 'string'):
                    return istype(value, 'coordinates-geographic-latitude-dms') or istype(value, 'coordinates-geographic-longitude-dms')
                elif istype(value, 'array-string'):
                    if len(value) == 2:
                        return istype(value[0], 'coordinates-geographic-latitude-dms') and istype(value[1], 'coordinates-geographic-longitude-dms')
            if type == 'coordinates-geographic-latitude':
                if istype(value, 'string'):
                    return istype(value, 'coordinates-geographic-latitude-ddd') or istype(value, 'coordinates-geographic-latitude-ddm') or istype(value, 'coordinates-geographic-latitude-dms')
            if type == 'coordinates-geographic-latitude-ddd':
                if istype(value, 'string') or istype(value, 'number'):
                    return bool(re.match(util.GEOGRAPHIC_COORDINATES_PATTERN_DECIMAL_DEGREES_LATITUDE, f"{value}")) or bool(re.match(r"^-?90(\.0+)?$", f"{value}"))
            if type == 'coordinates-geographic-latitude-ddm':
                if istype(value, 'string'):
                    pattern = ""
                    if '°' in value or '*' in value:
                        if value[0] == 'N' or value[0] == 'S':
                            pattern = r"^(?P<direction>N|S)(?P<degrees>[0-9]|[0-8][0-9])(°|\*)?(?P<decimal_minutes>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9]|[0-9][0-9]))'?$"
                        if value[-1] == 'N' or value[-1] == 'S':
                            pattern = r"^(?P<degrees>[0-9]|[0-8][0-9])(°|\*)?(?P<decimal_minutes>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9]|[0-9][0-9]))'?(?P<direction>N|S)$"
                    else:
                        if value[0] == 'N' or value[0] == 'S':
                            pattern = r"^(?P<direction>N|S)(?P<degrees>[0-8][0-9])(?P<decimal_minutes>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9][0-9]))(?P<direction>N|S)$"
                        if value[-1] == 'N' or value[-1] == 'S':
                            pattern = r"^(?P<degrees>[0-8][0-9])(?P<decimal_minutes>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9][0-9]))$"
                    return bool(re.match(pattern, value))
            if type == 'coordinates-geographic-latitude-dms':
                if istype(value, 'string'):
                    pattern = ""
                    if '°' in value or '*' in value:
                        if value[0] == 'N' or value[0] == 'S':
                            pattern = r"^(?P<direction>N|S)(?P<degrees>[0-9]|[0-8][0-9])(°|\*)?(?P<minutes>[0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])'?(?P<seconds>[0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9](.\d+)?)\"?$"
                        if value[-1] == 'N' or value[-1] == 'S':
                            pattern = r"^(?P<degrees>[0-9]|[0-8][0-9])(°|\*)?(?P<minutes>[0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])'?(?P<seconds>[0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9](.\d+)?)\"?(?P<direction>N|S)$"
                    else:
                        if value[0] == 'N' or value[0] == 'S':
                            pattern = r"^(?P<direction>N|S)(?P<degrees>[0-8][0-9])(?P<minutes>0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(?P<seconds>0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9](.\d+)?)$"
                        if value[-1] == 'N' or value[-1] == 'S':
                            pattern = r"^(?P<degrees>[0-8][0-9])(?P<minutes>0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(?P<seconds>0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9](.\d+)?)(?P<direction>N|S)$"
                    return bool(re.match(pattern, value))
            if type == 'coordinates-geographic-longitude':
                if istype(value, 'string'):
                    return istype(value, 'coordinates-geographic-longitude-ddd') or istype(value, 'coordinates-geographic-longitude-ddm') or istype(value, 'coordinates-geographic-longitude-dms')
            if type == 'coordinates-geographic-longitude-ddd':
                if istype(value, 'string') or istype(value, 'number'):
                    return bool(re.match(util.GEOGRAPHIC_COORDINATES_PATTERN_DECIMAL_DEGREES_LONGITUDE, f"{value}")) or bool(re.match(r"^-?180(\.0+)?$", f"{value}"))
            if type == 'coordinates-geographic-longitude-ddm':
                if istype(value, 'string'):
                    pattern = ""
                    if '°' in value or '*' in value:
                        if value[0] == 'E' or value[0] == 'W':
                            pattern = r"^(?P<direction>E|W)(?P<degrees>[0-9]|0[0-9][0-9]|1[0-7][0-9])(°|\*)?(?P<decimal_minutes>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9]|[0-9][0-9]))'?$"
                        if value[-1] == 'E' or value[-1] == 'W':
                            pattern = r"^(?P<degrees>[0-9]|0[0-9][0-9]|1[0-7][0-9])(°|\*)?(?P<decimal_minutes>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9]|[0-9][0-9]))'?(?P<direction>E|W)$"
                    else:
                        if value[0] == 'E' or value[0] == 'W':
                            pattern = r"^(?P<direction>E|W)(?P<degrees>0[0-9][0-9]|1[0-7][0-9])(?P<decimal_minutes>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9][0-9]))$"
                        if value[-1] == 'E' or value[-1] == 'W':
                            pattern = r"^(?P<degrees>0[0-9][0-9]|1[0-7][0-9])(?P<decimal_minutes>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9][0-9]))(?P<direction>E|W)$"
                    return bool(re.match(pattern, value))
            if type == 'coordinates-geographic-longitude-dms':
                if istype(value, 'string'):
                    pattern = ""
                    if '°' in value or '*' in value:
                        if value[0] == 'E' or value[0] == 'W':
                            pattern = r"^(?P<direction>E|W)(?P<degrees>[0-9]|[0-9][0-9]|0[0-9][0-9]|1[0-7][0-9])(°|\*)?(?P<minutes>[0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])'?(?P<seconds>[0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9](.\d+)?)\"?$"
                        if value[-1] == 'E' or value[-1] == 'W':
                            pattern = r"^(?P<degrees>[0-9]|[0-9][0-9]|0[0-9][0-9]|1[0-7][0-9])(°|\*)?(?P<minutes>[0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])'?(?P<seconds>[0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9](.\d+)?)\"?(?P<direction>E|W)$"
                    else:
                        if value[0] == 'E' or value[0] == 'W':
                            pattern = r"^(?P<direction>E|W)(?P<degrees>0[0-9][0-9]|1[0-7][0-9])(?P<minutes>0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(?P<seconds>0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9](.\d+)?)$"
                        if value[-1] == 'E' or value[-1] == 'W':
                            pattern = r"^(?P<degrees>0[0-9][0-9]|1[0-7][0-9])(?P<minutes>0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(?P<seconds>0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9](.\d+)?)(?P<direction>E|W)$"
                    return bool(re.match(pattern, value))
            if type == 'date':
                return isinstance(value, datetime.datetime)
            if type == 'decimal':
                return isinstance(value, int)
            if type == 'hexadecimal':
                if istype(value, 'string'):
                    return bool(re.match(r"^([0-9]|[A-F]|[a-f])+$", value))
            if type == 'html':
                pass
            if type == 'html-tag':
                if istype(value, 'string'):
                    strings = '!doctype|a|abbr|address|area|article|aside|audio|b|base|bb|bdi|bdo|big|blockquote|br|button|canvas|caption|cite|code|col|colgroup|data|datalist|dd|del|details|dfn|dialog|div|dl|dt|em|embed|fieldset|figcaption|figure|footer|form|h1|h2|h3|h4|h5|h6|head|header|hr|html|i|iframe|img|input|ins|kbd|label|legend|li|link|main|map|mark|meta|meter|nav|noscript|object|ol|optgroup|option|p|param|picture|polyline|polygon|pre|progress|q|rp|rt|ruby|s|samp|script|section|select|small|source|span|strong|style|sub|summary|sup|svg|table|tbody|td|template|textarea|tfoot|th|thead|tr|track|u|ul|var|video|wbr'.split('|')
                    return value in strings
            if type == 'identifier':
                if istype(value, 'string'):
                    return bool(re.match(r"^([0-9]|[A-Z]|[a-z]|_)+$", value))
            if type == 'number':
                return istype(value, 'number-float') or istype(value, 'number-integer')
            if type == 'number-float':
                return isinstance(value, float)
            if type == 'number-integer':
                return isinstance(value, int)
            if type == 'object':
                return isinstance(value, dict) or isinstance(value, object)
            if type == 'octal':
                if istype(value, 'string'):
                    return bool(re.match(r"^[0-7]+$", value))
            if type == 'port':
                if istype(value, 'number') or istype(value, 'string-number'):
                    return 0 <= int(value) and int(value) <= 65535
            if type == 'port-ephemeral':
                if istype(value, 'number') or istype(value, 'string-number'):
                    return 1024 <= int(value) and int(value) <= 65535
            if type == 'port-ephemeral-registered':
                if istype(value, 'number') or istype(value, 'string-number'):
                    return 1024 <= int(value) and int(value) <= 49151
            if type == 'port-ephemeral-unregistered' or type == 'port-ephemeral-dynamic' or type == 'port-ephemeral-private':
                if istype(value, 'number') or istype(value, 'string-number'):
                    return 49152 <= int(value) and int(value) <= 65535
            if type == 'port-nonephemeral' or type == 'port-wellknown':
                if istype(value, 'number') or istype(value, 'string-number'):
                    return 0 <= int(value) and int(value) <= 1023
            if type == 'string':
                return isinstance(value, str)
            if type == 'string-array':
                if istype(value, 'string'):
                    if len(value) >= 2:
                        return value[0] == '[' and value[-1] == ']'
            if type == 'string-array-object':
                if istype(value, 'string'):
                    if len(value) >= 4:
                        return value[0] == '[' and value[-1] == ']' and value[1] == '{' and value[-2] == '}'
            if type == 'string-boolean':
                if istype(value, 'string'):
                    assert isinstance(value, str)
                    return value.lower() == 'true' or value.lower() == 'false'
            if type == 'string-number':
                 return istype(value, 'string-number-float') or istype(value, 'string-number-integer')
            if type == 'string-number-float':
                if istype(value, 'string'):
                    return bool(re.match(r"^(-|\+)?\d+\.\d+$", value))
            if type == 'string-number-integer':
                if istype(value, 'string'):
                    return bool(re.match(r"^(-|\+)?\d+$", value))
            if type == 'string-object':
                if istype(value, 'string'):
                    if len(value) >= 2:
                        return value[0] == '{' and value[-1] == '}'
            if type == 'timestamp':
                if istype(value, 'string'):
                    pattern = ""
                    if '-' in value:
                        print(f"DepreciationError: name=timestamp (legacy) value=YYYY-MM-DDTHH:MM:SS")
                        if len(value) == 4 or len(value) == 5:   pattern = f"{util.TIMESTAMP_PATTERN_YEAR}"
                        if len(value) == 7 or len(value) == 8:   pattern = f"{util.TIMESTAMP_PATTERN_YEAR}-{util.TIMESTAMP_PATTERN_MONTH}"
                        if len(value) == 10 or len(value) == 11: pattern = f"{util.TIMESTAMP_PATTERN_YEAR}-{util.TIMESTAMP_PATTERN_MONTH}-{util.TIMESTAMP_PATTERN_DAY}"
                        if len(value) == 13 or len(value) == 14: pattern = f"{util.TIMESTAMP_PATTERN_YEAR}-{util.TIMESTAMP_PATTERN_MONTH}-{util.TIMESTAMP_PATTERN_DAY}T{util.TIMESTAMP_PATTERN_HOUR}"
                        if len(value) == 16 or len(value) == 17: pattern = f"{util.TIMESTAMP_PATTERN_YEAR}-{util.TIMESTAMP_PATTERN_MONTH}-{util.TIMESTAMP_PATTERN_DAY}T{util.TIMESTAMP_PATTERN_HOUR}:{util.TIMESTAMP_PATTERN_MINUTE}"
                        if len(value) == 19 or len(value) == 20: pattern = f"{util.TIMESTAMP_PATTERN_YEAR}-{util.TIMESTAMP_PATTERN_MONTH}-{util.TIMESTAMP_PATTERN_DAY}T{util.TIMESTAMP_PATTERN_HOUR}:{util.TIMESTAMP_PATTERN_MINUTE}:{util.TIMESTAMP_PATTERN_SECOND}"
                        if len(value) == 23 or len(value) == 24: pattern = f"{util.TIMESTAMP_PATTERN_YEAR}-{util.TIMESTAMP_PATTERN_MONTH}-{util.TIMESTAMP_PATTERN_DAY}T{util.TIMESTAMP_PATTERN_HOUR}:{util.TIMESTAMP_PATTERN_MINUTE}:{util.TIMESTAMP_PATTERN_SECOND}.{util.TIMESTAMP_PATTERN_MILLISECOND}"
                    else: 
                        if len(value) == 4 or len(value) == 5:   pattern = f"{util.TIMESTAMP_PATTERN_YEAR}"
                        if len(value) == 6 or len(value) == 7:   pattern = f"{util.TIMESTAMP_PATTERN_YEAR}{util.TIMESTAMP_PATTERN_MONTH}"
                        if len(value) == 8 or len(value) == 9:   pattern = f"{util.TIMESTAMP_PATTERN_YEAR}{util.TIMESTAMP_PATTERN_MONTH}{util.TIMESTAMP_PATTERN_DAY}"
                        if len(value) == 11 or len(value) == 12: pattern = f"{util.TIMESTAMP_PATTERN_YEAR}{util.TIMESTAMP_PATTERN_MONTH}{util.TIMESTAMP_PATTERN_DAY}T{util.TIMESTAMP_PATTERN_HOUR}"
                        if len(value) == 13 or len(value) == 14: pattern = f"{util.TIMESTAMP_PATTERN_YEAR}{util.TIMESTAMP_PATTERN_MONTH}{util.TIMESTAMP_PATTERN_DAY}T{util.TIMESTAMP_PATTERN_HOUR}{util.TIMESTAMP_PATTERN_MINUTE}"
                        if len(value) == 15 or len(value) == 16: pattern = f"{util.TIMESTAMP_PATTERN_YEAR}{util.TIMESTAMP_PATTERN_MONTH}{util.TIMESTAMP_PATTERN_DAY}T{util.TIMESTAMP_PATTERN_HOUR}{util.TIMESTAMP_PATTERN_MINUTE}{util.TIMESTAMP_PATTERN_SECOND}"
                        if len(value) == 19 or len(value) == 20: pattern = f"{util.TIMESTAMP_PATTERN_YEAR}{util.TIMESTAMP_PATTERN_MONTH}{util.TIMESTAMP_PATTERN_DAY}T{util.TIMESTAMP_PATTERN_HOUR}{util.TIMESTAMP_PATTERN_MINUTE}{util.TIMESTAMP_PATTERN_SECOND}.{util.TIMESTAMP_PATTERN_MILLISECOND}"
                    return bool(re.match(f"^{pattern}{util.TIMESTAMP_PATTERN_ZONE}$", value))
            if type == 'timestamp-date':
                if istype(value, 'string'):
                    if '-' in value:
                        print(f"DepreciationError: name=timestamp (legacy) value=YYYY-MM-DD")
                        return bool(re.match(f"^{util.TIMESTAMP_PATTERN_YEAR}-{util.TIMESTAMP_PATTERN_MONTH}-{util.TIMESTAMP_PATTERN_DAY}{util.TIMESTAMP_PATTERN_ZONE}$", value))
                    else:
                        return bool(re.match(f"^{util.TIMESTAMP_PATTERN_YEAR}{util.TIMESTAMP_PATTERN_MONTH}{util.TIMESTAMP_PATTERN_DAY}{util.TIMESTAMP_PATTERN_ZONE}$", value))
            if type == 'timestamp-time':
                if istype(value, 'string'):
                    if ':' in value:
                        print(f"DepreciationError: name=timestamp (legacy) value=HH:MM:SS")
                        return bool(re.match(f"^{util.TIMESTAMP_PATTERN_HOUR}:{util.TIMESTAMP_PATTERN_MINUTE}:{util.TIMESTAMP_PATTERN_SECOND}{util.TIMESTAMP_PATTERN_ZONE}$", value))
                    else:
                        return bool(re.match(f"^{util.TIMESTAMP_PATTERN_HOUR}{util.TIMESTAMP_PATTERN_MINUTE}{util.TIMESTAMP_PATTERN_SECOND}{util.TIMESTAMP_PATTERN_ZONE}$", value))
            if type == 'timestamp-zone':
                if istype(value, 'string'):
                    return bool(re.match(util.TIMESTAMP_PATTERN_ZONE, value))
            
            if type[-2:len(type)] == '[]':
                if istype(value, 'array'):
                    for value_ in value:
                        if not istype(value_, type[0:-2]):
                            return False
                    return True
            return False
        delimiter = None
        if '|' in types: delimiter = '|'
        if '&' in types: delimiter = '&'
        if delimiter == None:
            return istype(value, types)
        else:
            results = []
            for type in types.split(delimiter):
                results.append(istype(value, type))
            if delimiter == '|': return True in results
            if delimiter == '&': return not False in results
    def importModule(name: str):
        # if util.importModule(''): import 
        return not name in dir()
    def invalidateType(value, types: str) -> bool:
        valid = util.istype(value, types)
        if not valid: util.system_log(__file__, inspect.currentframe().f_lineno, f"TypeError: variable-name=value variable-value={value} variable-type=${type(value)}")
        return not valid

    def get(method: str, *arguments):
        return getattr(globals()['util'], method)(*arguments)
    # a
    def abbreviation(string: str, delimiter: str = ' ') -> str:
        specials = {
            'child-to-parent synchronization': 'CSYNC',
            'domain name system security': 'DNSSEC',
            'domain name system security extensions': 'DNSSEC',
            'domain name system security lookaside validation': 'DLV',
            'domain name system key': 'DNSKEY',
            'domain name system stateful operations': 'DSO',
            'high level data link control': 'HDLC',
            'gateway to gateway protocol': 'GGP',
            'identifier': 'ID',
            'inter domain policy routing': 'IDPR',
            'inter domain policy routing protocol': 'IDPR',
            'inter domain routing protocol': 'IDRP',
            'internet control message protocol v6': 'ICMPv6',
            'internet protocol v4': 'IPv4',
            'internet protocol v6': 'IPv6',
            'internet protocol secure': 'IPSec',
            'internet protocol secure key': 'IPSECKEY',
            'internet stream protocol': 'ST',
            'inverse address resolution protocol': 'InARP',
            'naming authority pointer': 'NAPTR',
            'netbios': 'NetBIOS',
            'netbios datagram distribution server': 'NBDDS',
            'netbios name server': 'NBNS',
            'nimrod locator': 'NIMLOC',
            'path maximum transmission unit discovery': 'PMTUD',
            'resource record digital signature': 'RRSIG',
            'resource reservation protocol': 'RSVP',
            'secure multipurpose internet mail extensions': 'SMIME',
            'secure shell': 'SSH',
            'secure shell fingerprint': 'SSHFP',
            'service locator': 'SRV',
            'service binding': 'SVCB',
            'transaction signature': 'TSIG',
            'transport layer security': 'TLS', 
        }
        for specialBefore, specialAfter in specials.items():
            if specialBefore.lower() == string.lower() or specialBefore.replace(' ', '_').lower() == string.lower():
                return specialAfter
        nString = ''
        for substring in string.split(delimiter):
            nString += substring[0]
        return nString
    def address_binary(value: int|str) -> str:
        if util.istype(value, 'address&binary'):
            return value
        if util.istype(value, 'number|string-number'):
            return util.address_prefix_length_to_mask(value)
        elif util.istype(value, 'address-ipv4'):
            return util.address_ipv4(value)
        elif util.istype(value, 'address-ipv6'):
            return util.address_ipv6(value)
        elif util.istype(value, 'address-mac'):
            return util.address_mac(value)
        else:
            util.system_log(__file__, inspect.currentframe().f_lineno, f"TypeError: variable-name=value variable-value={value} variable-type={type(value)} type=address|binary|number|string-number")
    def address_broadcast(address: str, netmask: int|str) -> str:
        address = util.address_binary(address)
        netmask = util.address_binary(netmask)
        prefix_length = util.address_mask_to_prefix_length(netmask)
        return address[0:prefix_length].ljust(32, '1')
    def address_decimal(value: int|str) -> str:
        return util.bin2dec(util.address_binary(value))
    def address_family(value: str, short: bool = True) -> str:
        if util.istype(value, 'address-internet_protocol_v4'):
            return 'internet_protocol_v4'
        elif util.istype(value, 'address-internet_protocol_v6'):
            return 'internet_protocol_v6'
        elif util.istype(value, 'address-media_access_control'):
            return 'media_access_control'
        else:
            util.system_log(__file__, inspect.currentframe().f_lineno, f"TypeError: variable-name=value variable-value={value} variable-type={type(value)} type=address")
    def address_hexadecimal(value: int|str) -> str:
        return util.bin2hex(util.address_binary(value))
    def address_ip_to_mac_multicast(value: str) -> str:
        if util.istype(value, 'address-ipv4'):
            return util.address_ipv4_to_mac_multicast(value)
        if util.istype(value, 'address-ipv6'):
            return util.address_ipv6_to_mac_multicast(value)
    def address_ipv4(value: str = None) -> str:
        output = ''
        if value == None:
            for i in range(4): output += util.dec2bin(util.random(0, 255), 8)
        else:
            if '.' in value:
                value: str = value
                for octet in value.split('.'): output += util.dec2bin(int(octet), 8)
            else:
                for i in range(0, 32, 8): output += ('' if output == '' else '.') + str(util.bin2dec(value[i:i + 8]))
        return output
    def address_ipv4_broadcast(address: str, netmask: int|str) -> str:
        address = util.address_binary(address)
        netmask = util.address_binary(netmask)
        prefix_length = util.address_mask_to_prefix_length(netmask)
        return address[0:prefix_length].ljust(32, '1')
    def address_ipv4_network_identifier(address: str, netmask: int|str) -> str:
        address = util.address_binary(address)
        netmask = util.address_binary(netmask)
        prefix_length = util.address_mask_to_prefix_length(netmask)
        return address[0:prefix_length].ljust(32, '0')
    def address_ipv4_to_ipv6_4to6(value: str) -> str:
        value = util.address_binary(value)
        return '000000000000000000000000000000000000000000000000000000000000000000000000000000001111111111111111' + value
    def address_ipv4_to_ipv6_6to4(value: str) -> str:
        value = util.address_binary(value)
        return '0010000000000010' + value + '00000000000000000000000000000000000000000000000000000000000000000000000000000000'
    def address_ipv4_to_ipv6_mapped(value: str) -> str:
        value = util.address_binary(value)
        return '000000000000000000000000000000000000000000000000000000000000000000000000000000001111111111111111' + value
    def address_ipv4_to_mac_multicast(value: str) -> str:
        value = util.address_binary(value)
        return util.hex2bin('01005E') + '0' + value[9:32]
    def address_ipv6(value: str = None) -> str:
        output = ''
        if value == None:
            for i in range(8): output += util.dec2bin(util.random(0, 65535), 16)
        elif ':' in value:
            value: str = value
            quartets = value.split(':')
            if len(value) == 39:
                for quartet in value.split(':'): output += util.hex2bin(quartet)
            else:
                aArray = [(util.pad(quartet, 4, '0', 'left')) for quartet in quartets]
                bArray = []
                a = aArray.index('0000') if '0000' in aArray else -1
                for i in range(len(aArray)):
                    bArray.append(util.hex2bin(aArray[i]))
                    if i == a: bArray.extend((util.hex2bin('0000')) for j in range(8 - len(aArray)))
                output = ''.join(bArray)
        else:
            aArray = []
            for i in range(0, 128, 16):
                hexadecimal = util.bin2hex(value[i:i+16])
                for j in range(len(hexadecimal)):
                    if hexadecimal[j] != '0' or j == 3:
                        hexadecimal = hexadecimal[j:]
                        break
                aArray.append(hexadecimal)
            bArray = []
            for i in range(8):
                if (i == 0 and aArray[i] == '0') or i != 0 and aArray[i-1] != '0' and aArray[i] == '0':
                    bArray.append([i, 0])
                if aArray[i] == '0':
                    bArray[len(bArray) - 1][1] += 1
            bArray.sort(key=(lambda value : value[1]), reverse=True)
            if len(bArray) > 0 and bArray[0][1] > 1:
                i = 0
                while i < 8:
                    if i == bArray[0][0]:
                        output += ('' if len(output) == 0 or output[-1] == ':' else ':') + ':'
                        i += bArray[0][1] - 1
                    else:
                        output += aArray[i] + ('' if i == 7 else ':')
                    i += 1
            else:
                output = ':'.join(aArray)
        return output
    def address_ipv6_local_link_to_mac(value: str) -> str:
        universal_local_bit = '1' if value[70] == '0' else '0'
        return value[64:70] + universal_local_bit + value[71:88] + value[104:128]
    def address_ipv6_to_ipv4(value: str) -> str:
        if util.istype(value, 'address-ipv6-4to6'):
            return value[96:128]
        if util.istype(value, 'address-ipv6-6to4'):
            return value[16:48]
    def address_ipv6_to_mac(value: str) -> str:
        value = util.address_binary(value)
        if util.istype(value, 'address-ipv6-local-link'):
            return util.address_ipv6_local_link_to_mac(value)
        if util.istype(value, 'address-ipv6-multicast'):
            return util.address_ipv6_to_mac_multicast(value)
    def address_ipv6_to_mac_multicast(value: str) -> bool:
        value = util.address_binary(value)
        return util.hex2bin('3333') + value[96:128]
    def address_is_ipv4_broadcast(value: str, network_identifier: str, subnetmask: str) -> bool:
        value = util.address_binary(value)
        if value == util.address_ipv4('255.255.255.255'): return True
        return value == util.address_broadcast(network_identifier, subnetmask)
    def address_mac(value: str) -> str:
        output = ''
        if value == None:
            for i in range(6): output += util.dec2bin(util.random(0, 255), 8)
        else:
            value: str = value
            if '-' in value:
                output = ''.join([(util.hex2bin(hexadecimal)) for hexadecimal in value.split('-')])
            else:
                output = '-'.join([(util.bin2hex(value[i:i+8])) for i in range(0, 48, 8)])
        return output
    def address_mac_to_ipv6_local_link(address: str, network_prefix: str) -> str:
        if len(network_prefix) != 64: return util.system_log(__file__, inspect.currentframe().f_lineno, f"StringLengthError: variable-name=network_prefix variable-length={len(network_prefix)} length=eq64")
        address = util.address_binary(address)
        interface_identifier = address[0:24] + util.hex2bin('fffe') + address[24:48]
        universal_local_bit = '1' if interface_identifier[7] == '0' else '0'
        interface_identifier = interface_identifier[0:6] + universal_local_bit + interface_identifier[7:64]
        return network_prefix + interface_identifier
    def address_mask_from_addresses(addresses: list[str]) -> str:
        for index, address in enumerate(addresses):
            addresses[index] = util.address_binary(address)
        prefix_length = 0
        for bitIndex in range(0, 32):
            bit = None
            for index, address in enumerate(addresses):
                if not index == 0 and not address[bitIndex] == bit:
                    bit = None
                    break
                bit = address[bitIndex]
            prefix_length = bitIndex
            if bit == None:
                break
        return util.address_prefix_length_to_mask(prefix_length)
    def address_mask_to_prefix_length(value: str) -> str:
        # networkmask|subnetworkmask: 11110000..., wildcardmask: 00001111...
        value = util.address_binary(value)
        if value.count('1') == 32 or value.count('0') == 32:
            return 32
        else:
            character = '1' if value.find('0') > value.rfind('1') else '0'
            return value.count(character)
    def address_mask_to_wildcardmask(value: str) -> str:
        value = util.address_binary(value)
        prefix_length = value.count('1')
        return ''.ljust(prefix_length, '0') + ''.ljust(32 - prefix_length, '1')
    def address_network_identifier(address: str, netmask: int|str) -> str:
        address = util.address_binary(address)
        prefix_length = netmask if util.istype(netmask, 'number') else util.address_mask_to_prefix_length(netmask)
        return address[0:prefix_length].ljust(32, '0')
    def address_prefix_length_to_mask(prefix_length: int|str) -> str:
        prefix_length = int(prefix_length)
        return ''.ljust(prefix_length, '1') + ''.ljust(32 - prefix_length, '0')
    def address_prefix_length_to_wildcardmask(prefix_length: int|str) -> str:
        prefix_length = int(prefix_length)
        return ''.ljust(prefix_length, '0') + ''.ljust(32 - prefix_length, '1')
    def address_prefix_length_to_address_count(prefix_length: int|str) -> int:
        prefix_length = int(prefix_length)
        return 2 ** (32 - prefix_length)
    def address_string(value: int|str) -> str:
        if util.istype(value, 'binary'):
            if util.istype(value, 'address-internet_protocol_v4'):
                return util.address_ipv4(value)
            elif util.istype(value, 'address-internet_protocol_v6'):
                return util.address_ipv6(value)
            elif util.istype(value, 'address-media_access_control'):
                return util.address_mac(value)
            else:
                return util.system_log(__file__, inspect.currentframe().f_lineno, f"TypeError: variable-name=value variable-value={value} variable-type={type(value)} type=address")
        elif util.istype(value, 'address'):
            return value
        elif util.istype(value, 'number|string-number'):
            return util.address_ipv4(util.address_prefix_length_to_mask(value))
        else:
            return util.system_log(__file__, inspect.currentframe().f_lineno, f"TypeError: variable-name=value variable-value={value} variable-type={type(value)} type=address|binary|number|string-number")
    def address_subnetting(network_identifier: str, netmask: int|str, subnets: int):
        network_identifier = util.address_binary(network_identifier)
        netmask = util.address_binary(netmask)
        subnets = int(subnets)
        # 
        network_identifier = util.address_network_identifier(network_identifier, netmask)
        # 
        network_mask_prefix_length = netmask.index('0')
        network_extension_length = None
        if subnets == 1:
            return [netmask, [network_identifier]]
        # subnets must be a power of 2
        for bit_length in range(1, 32, 1):
            if (2 ** bit_length) >= subnets:
                subnets = 2 ** bit_length
                network_extension_length = bit_length
                break
        if network_extension_length == None:
            return []
        network_identifiers = []
        wildcardmask_prefix_length = 32 - (network_mask_prefix_length + network_extension_length)
        subnetmask = ''.ljust(network_mask_prefix_length, '1') + ''.ljust(network_extension_length, '1') + ''.ljust(wildcardmask_prefix_length, '0')
        # cycle through bit combinations in network_extension
        for x in range(0, 2 ** network_extension_length, 1):
            network_identifiers.append(network_identifier[0:network_mask_prefix_length] + util.dec2bin(x, network_extension_length) + ''.ljust(wildcardmask_prefix_length, '0'))
        return [subnetmask, network_identifiers]
    def address_type(value: str) -> str:
        pass
    def address_wildcardmask_to_mask(value: str) -> str:
        value = util.address_binary(value)
        prefix_length = value.count('0')
        return ''.ljust(prefix_length, '1') + ''.ljust(32 - prefix_length, '0')
    def address_wildcardmask_to_prefix_length(value: str) -> str:
        value = util.address_binary(value)
        return value.count('0')
    def algebra_prime_factorization(number: int) -> list[int]:
        factors = []
        if number < 0:
            number *= -1
            factors += [-1]
        while number > 1:
            for i in range(2, int(number**0.5) + 1):
                if number % i == 0:
                    factors += [i]
                    number //= i
                    break
            else:
                factors += [number]
                break
        return factors
    def algebra_fraction_difference(fraction1: list[int], fraction2: list[int]) -> list[int]:
        most_common_denominator = fraction1[1] * fraction2[1]
        multiple_fraction1 = most_common_denominator / fraction1[1]
        multiple_fraction2 = most_common_denominator / fraction2[1]
        return util.algebra_fraction_simplify([(fraction1[0] * multiple_fraction1) - (fraction2[0] * multiple_fraction2), most_common_denominator])
    def algebra_fraction_quotient(fraction1: list[int], fraction2: list[int]) -> list[int]:
        return util.algebra_fraction_simplify([fraction1[0] / fraction2[0], fraction1[1] / fraction2[1]])
    def algebra_fraction_product(fraction1: list[int], fraction2: list[int]) -> list[int]:
        return util.algebra_fraction_simplify([fraction1[0] * fraction2[0], fraction1[1] * fraction2[1]])
    def algebra_fraction_simplify(fraction: list[int]) -> list[int]:
        def removeCommonFactors(fractionPrimeFactors: list[list[int]]) -> list[list[int]]:
            for primeFactor in fractionPrimeFactors[0]:
                if primeFactor in fractionPrimeFactors[1]:
                    fractionPrimeFactors[0].remove(primeFactor)
                    fractionPrimeFactors[1].remove(primeFactor)
                    return removeCommonFactors(fractionPrimeFactors)
            return fractionPrimeFactors
        fractionPrimeFactors = removeCommonFactors([util.algebra_prime_factorization(n) for n in fraction])
        fractionPrimeFactors = [([1] if len(primeFactors) == 0 else primeFactors) for primeFactors in fractionPrimeFactors]
        return [util.statistics_product(primeFactors) for primeFactors in fractionPrimeFactors]
    def algebra_fraction_sum(fraction1: list[int], fraction2: list[int]) -> list[int]:
        most_common_denominator = fraction1[1] * fraction2[1]
        multiple_fraction1 = most_common_denominator / fraction1[1]
        multiple_fraction2 = most_common_denominator / fraction2[1]
        return util.algebra_fraction_simplify([(fraction1[0] * multiple_fraction1) + (fraction2[0] * multiple_fraction2), most_common_denominator])
    def algebra_factor(number: int) -> list[list[int]]:
        factors = []
        n = abs(number)
        ns = str(float(n))
        power = len(ns[ns.index('.')+1:])
        n = n if power == 1 else int(n * 10**power)
        for aNumber in range(0, n+1, 1):
            for bNumber in range(0, n+1, 1):
                product = aNumber * bNumber
                if product == n and not ([aNumber, bNumber] in factors or [bNumber, aNumber] in factors):
                    factors += [[aNumber, bNumber]]
                    factors += [[-aNumber, -bNumber]]
        if str(number)[0] == '-':
            for index, pair in enumerate(factors):
                factors[index][0] = -factors[index][0]
        return factors
    def algebra_factoring(number: int) -> list[list[int]]:
        return uti.algebra_factor(number)
    def algebra_quadratic_formula(a: float, b: float, c: float) -> tuple[float, float]:
        try:
            return ((-b)+math.sqrt(b**2-4*a*c))/(a*2), ((-b)-math.sqrt(b**2-4*a*c))/(a*2)
        except:
            return 0, 0
    def algorithm_fibonacci(n: int, results: dict[int, int] = {}) -> int:
        if n == 0 or n == 1:
            return n
        if n in results:
            return results[n]
        result = util.algorithm_fibonacci(n - 1, results) + util.algorithm_fibonacci(n - 2, results)
        results[n] = result
        return result
    def algorithm_tribonacci(n: int, results: dict[int, int] = {}) -> int:
        if n == 0 or n == 1:
            return 0
        if n == 2:
            return 1
        if n in results:
            return results[n]
        result = util.algorithm_tribonacci(n - 1, results) + util.algorithm_tribonacci(n - 2, results) + util.algorithm_tribonacci(n - 3, results)
        results[n] = result
        return result
    def algorithm_sum_possible(amount: int, numbers: list[int], results: dict[int, bool] = {}) -> bool:
        # finds if one or more numbers in the array can add up to be equal to the target.
        # use number in numbers one time
        # seen = set()
        # for num in numbers:
        #     if amount == num:
        #         return True
        #     elif amount - num in seen:
        #         return True
        #     else:
        #         seen.add(num)
        # return False
        # use number in numbers multiple times
        if amount == 0:
            return True
        if amount < 0:
            return False
        if amount in results:
            return results[amount]
        for number in numbers:
            subAmount = amount - number
            if util.algorithm_sum_possible(subAmount, numbers, results):
                results[amount] = True
                return True
        results[amount] = False
        return False
    def arithmetic_greatest_common_denominator(denominator1: int, denominator2: int) -> int:
        if denominator2 == 0:
            return denominator1
        return util.arithmetic_greatest_common_denominator(denominator2, denominator1 % denominator2)
    def arithmetic_least_common_denominator(denominators: list[int]) -> int:
        lcd = denominators[0]
        for i in range(len(denominators)):
            lcd = (lcd * denominators[i]) / util.arithmetic_greatest_common_denominator(lcd, denominators[i])
        return lcd
    # b
    def base64_encode(data: bytes) -> str:
        if util.importModule('base64'): import base64
        return base64.b64encode(data).decode('utf-8')
    def base64_decode(data: str) -> bytes:
        if util.importModule('base64'): import base64
        return base64.decodebytes(data.encode('utf-8'))
    def boolean(value: str):
        return value.lower() in ['y', 'yes', '1', 't', 'true']
    def bytes_format(value: bytes|int, fractionDigits:int = 2) -> str:
        if util.invalidateType(value, 'bytes|number'): return ''
        if util.istype(value, 'bytes'):
            value = util.byt2dec(value)
        if value < 1024:
            return f"{value} B"
        elif value < 1048576:
            return f"{(value / 1024):.{fractionDigits}f} KB"
        elif value < 1073741824:
            return f"{(value / 1048576):.{fractionDigits}f} MB"
        elif value < 1099511627776:
            return f"{(value / 1073741824):.{fractionDigits}f} GB"
        else:
            return f"{(value / 1099511627776):.{fractionDigits}f} TB"
            # c
    # c
    def capitalize(string: str) -> str:
        return ' '.join([substring.capitalize() for substring in string.split(' ')])
    def cartesian_point_in_rectangle(point: list[float], rectangle: list[list[float]]) -> bool:
        x, y = point
        xs = [corner[0] for corner in rectangle]
        yx = [corner[1] for corner in rectangle]
        xMin = min(xs)
        xMax = max(xs)
        yMin = min(yx)
        yMax = max(yx)
        return (xMin <= x and x <= xMax) and (yMin <= y and y <= yMax)
    def cartesian_polygon_centroid(points: list[float]) -> list[float]:
        # initialize the centroid coordinates
        x = 0
        y = 0
        area = 0
        # iterate through the polygon's vertices
        j = len(points) - 1
        for i in range(len(points)):
            xi = points[i][0]
            yi = points[i][1]
            xj = points[j][0]
            yj = points[j][1]
            # calculate the cross product between two consecutive vertices.
            crossProduct = xi * yj - xj * yi
            area += crossProduct
            # update the x and y coordinates of the centroid based on the cross product and vertex coordinates.
            x += (xi + xj) * crossProduct
            y += (yi + yj) * crossProduct
            i += 1
            j = i - 1
        area /= 2
        x /= (6 * area)
        y /= (6 * area)
        return [x, y]
    def cartesian_to_azimuth(point1: list[float], point2: list[float]) -> float:
        x1, y1 = point1
        x2, y2 = point2
        dx = x2 - x1
        dy = y2 - y1
        theta = math.atan2(dy, dx)
        degrees = theta * util.RADIANS_TO_DEGREES
        azimuth = (90 - degrees)
        azimuth = util.mathematics_constrain(azimuth, 0, 360)
        return azimuth
    def cartesian_to_cylindrical(point1: list[float], point2: list[float]) -> list[float]:
        x1, y1, z1 = point1
        x2, y2, z2 = point2
        dx = x2 - x1
        dy = y2 - y1
        dz = z2 - z1
        r = (dx**2 + dy**2 + dz**2)**0.5
        azimuth = math.atan2(dy, dx) * util.RADIANS_TO_DEGREES
        height = math.atan2(dz, r)
        return [r, azimuth, height]
    def cartesian_to_distance(point1: list[float], point2: list[float]) -> float:
        length1 = len(point1)
        length2 = len(point2)
        if length1 == 2 and length2 == 2:
            x1, y1 = point1
            x2, y2 = point2
            dx = x2 - x1
            dy = y2 - y1
            distance = (dx**2 + dy**2)**0.5
            return distance
        if length1 == 3 and length2 == 3:
            x1, y1, z1 = point1
            x2, y2, z2 = point2
            dx = x2 - x1
            dy = y2 - y1
            dz = z2 - z1
            distance = (dx**2 + dy**2 + dz**2)**0.5
            return distance
    def cartesian_to_elevation(point1: list[float], point2: list[float]) -> float:
        x1, y1, z1 = point1
        x2, y2, z2 = point2
        dx = x2 - x1
        dy = y2 - y1
        dz = z2 - z1
        r = (dx**2 + dy**2 + dz**2)**0.5
        phi = math.acos(dz / r)
        degrees = phi * util.RADIANS_TO_DEGREES
        elevation = 90 - degrees
        return elevation
    def cartesian_in(point: list[float], polygon: list[list[float]]) -> bool:
        n = len(polygon)
        inside = False
        j = n - 1
        for i in range(n):
            if (polygon[i][1] <= point[1] and polygon[j][1] >= point[1] or polygon[j][1] <= point[1] and polygon[i][1] >= point[1]):
                if (point[0] <= (polygon[j][0] - polygon[i][0]) * (point[1] - polygon[i][1]) / (polygon[j][1] - polygon[i][1]) + polygon[i][0]):
                    inside = not inside
            j = i
        return inside
    def cartesian_to_midpoint(point1: list[float], point2: list[float]) -> list[float]:
        length1 = len(point1)
        length2 = len(point2)
        if length1 == 2 and length2 >= 2:
            x1, y1 = point1
            x2, y2 = point2
            midpoint = [(x1 + x2) / 2, (y1 + y2) / 2]
            return midpoint
        if length1 == 3 and length2 == 3:
            x1, y1, z1 = point1
            x2, y2, z2 = point2
            midpoint = [(x1 + x2) / 2, (y1 + y2) / 2, (z1 + z2) / 2]
            return midpoint
    def cartesian_to_polar(point1: list[float], point2: list[float]) -> list[float]:
        x1, y1, z1 = point1
        x2, y2, z2 = point2
        dx = x2 - x1
        dy = y2 - y1
        dz = z2 - z1
        r = (dx**2 + dy**2) ** 0.5
        theta = math.atan2(dy, dx)
        return [r, theta]
    def cartesian_to_slope(point1: list[float], point2: list[float]) -> float:
        x1, y1 = point1
        x2, y2 = point2
        dx = x2 - x1
        dy = y2 - y1
        return dy / dx
    def cartesian_to_spherical(point1: list[float], point2: list[float]) -> list[float]:
        x1, y1, z1 = point1
        x2, y2, z2 = point2
        dx = x2 - x1
        dy = y2 - y1
        dz = z2 - z1
        r = (dx**2 + dy**2 + dz**2)**0.5
        theta = math.atan2(dy, dx)
        phi = math.acos(dz / r)
        return [r, theta, phi]
    def cartesian_to_theta(point1: list[float], point2: list[float]) -> float:
        x1, y1 = point1[0], point1[1]
        x2, y2 = point2[0], point2[1]
        dx = x2 - x1
        dy = y2 - y1
        theta = math.atan2(dy, dx) * util.RADIANS_TO_DEGREES
        return theta
    def clone(value):
        if util.importModule('copy'): import copy
        return copy.deepcopy(value)
    def css_encode(value: dict) -> str:
        string = ''
        for cssKey, cssValue in value.items():
            if cssValue == None: continue
            if len(cssValue) == 0: continue
            string += ('' if len(string) == 0 else '; ') + cssKey + ': ' + cssValue
        return string
    def css_decode(value: str) -> dict:
        object = {}
        value = value.strip(' ')
        if value[-1] == ';':
            value = value[0:-1]
        for entry in value.split(';'):
            pair = entry.split(':')
            object[pair[0].strip(' ')] = pair[1].strip(' ')
        return object
    def csv_encode(entries: list[dict]) -> str:
        if entries == []: return ''
        string = ''
        header = [(f'"{field_name}"') for field_name in entries[0].keys()]
        string = ','.join(header)
        for index, entry in enumerate(entries):
            values = [('' if value == '' else f'"{value}"') for value in entry.values()]
            string += f"\n{','.join(values)}"
        return string
    def csv_decode(csv_string: str) -> list[dict]:
        if util.importModule('csv'): import csv
        csv_data = []
        reader = csv.reader(csv_string.splitlines())
        headers = next(reader)
        for row in reader:
            row_dict = dict(zip(headers, row))
            csv_data.append(row_dict)
        return csv_data
    def cylindrical_to_cartesian(r: float, azimuth: float, height: float) -> list[float]:
        azimuth *= util.DEGREES_TO_RADIANS
        x = r * math.cos(azimuth)
        y = r * math.sin(azimuth)
        z = height
        return [x, y, z]
    # d
    def degrees_to_radians(degrees: float|int) -> float:
        return degrees * util.DEGREES_TO_RADIANS
    def dump(value: dict|list, tabs: int = 0):
        if isinstance(value, array|object):
            value = value.data
        def tab(count: int, size: int = 4):
            return " " * count * size
        def get(value, tabs: int = 0) -> str:
            if value == None:
                return 'None'
            elif isinstance(value, bool):
                return str(value)
            elif isinstance(value, float|int):
                return str(value)
            elif isinstance(value, str):
                return '\'' + value + '\''
            elif isinstance(value, dict|list):
                return util.dump(value, tabs)
            else:
                return str(value)
        if isinstance(value, dict):
            string = '{\n'
            end = [key for key in value.keys()][-1] if len(value.keys()) > 0 else None
            for key, item in value.items():
                string += tab(tabs+1) + get(key) + ': ' + get(item, tabs+1) + ('' if key == end else ',') + '\n'
            string += tab(tabs) + '}'
        if isinstance(value, list):
            string = '[\n'
            end = value[-1] if len(value) > 0 else None
            for item in value:
                string += tab(tabs+1) + get(item, tabs+1) + ('' if item == end or end == None else ',') + '\n'
            string += tab(tabs) + ']'
        return string
    # e
    def entries_contains(entries: list[dict], *values) -> bool:
        filters = dict((values[i], values[i+1]) for i in range(0, len(values), 2))
        for entry in entries:
            for filterKey, filterValue in filters.items():
                if entry[filterKey] == filterValue:
                    return True
        return False
    def entries_excludes(entries: list[dict], *values) -> bool:
        filters = dict((values[i], values[i+1]) for i in range(0, len(values), 2))
        for entry in entries:
            for filterKey, filterValue in filters.items():
                if entry[filterKey] == filterValue:
                    return False
        return True
    def entries_includes(entries: list[dict], *values) -> bool:
        filters = dict((values[i], values[i+1]) for i in range(0, len(values), 2))
        for entry in entries:
            for filterKey, filterValue in filters.items():
                if entry[filterKey] == filterValue:
                    return True
        return False
    def entries_filter(entries: list[dict], *values) -> list[dict]:
        return util.entries_filter_and(entries, *values)
    def entries_filter_and(entries: list[dict], *values) -> list[dict]:
        filters = []
        for i in range(0, len(values), 2): filters.append({ 'key': values[i], 'value': values[i + 1] })
        filtered = []
        for entry in entries:
            matches = 0
            for filter in filters:
                if entry[filter['key']] == filter['value']: matches += 1
            if matches == len(filters): filtered.append(entry)
        return filtered
    def entries_filter_or(entries: list[dict], *values) -> list[dict]:
        filters = []
        for i in range(0, len(values), 2): filters.append({ 'key': values[i], 'value': values[i + 1] })
        filtered = []
        for entry in entries:
            matches = 0
            for filter in filters:
                if entry[filter['key']] == filter['value']: matches += 1
            if matches > 0: filtered.append(entry)
        return filtered
    def entries_find(entries: list[dict], *values) -> dict|None:
        return util.entries_find_and(entries, *values)
    def entries_find_and(entries: list[dict], *values) -> dict|None:
        filters = []
        for i in range(0, len(values), 2): filters.append({ 'key': values[i], 'value': values[i + 1] })
        for i in range(len(entries)):
            matches = 0
            for filter in filters:
                if entries[i][filter['key']] == filter['value']: matches += 1
            if matches == len(filters): return { 'index': i, 'value': entries[i] }
        return None
    def entries_find_or(entries: list[dict], *values) -> dict|None:
        filters = []
        for i in range(0, len(values), 2): filters.append({ 'key': values[i], 'value': values[i + 1] })
        for i in range(len(entries)):
            matches = 0
            for filter in filters:
                if entries[i][filter['key']] == filter['value']: matches += 1
            if matches > 0: return { 'index': i, 'value': entries[i] }
        return None
    def entries_remove(entries: list[dict], values: list) -> list[dict]:
        identifierKey = ''
        if entries == []: 
            return []
        identifierKey = 'id' if 'id' in entries[0] else 'identifier'
        identifiers: list[str] = [(value[identifierKey] if isinstance(value, dict) else value) for value in values]
        nEntries = []
        for entry in entries:
            if not entry[identifierKey] in identifiers: nEntries.append(entry)
        return nEntries
    def entries_remove_filter(entries: list[dict], *values) -> list[dict]:
        filtered = util.entries_filter_and(entries, *values)
        return util.entries_remove(entries, filtered)
    def entries_update(entries: list[dict], entry: dict) -> list[dict]:
        identifierKey = ''
        if entries == []: return []
        else: identifierKey = 'id' if 'id' in entries[0] else 'identifier'
        for index in range(len(entries)):
            if entries[index][identifierKey] == entry[identifierKey]:
                entries[index] = entry
                break
        return entries
    # f
    def file_append(path: str, value: bytes|dict|int|float|list|str):
        if isinstance(value, bytes):
            pass
        elif isinstance(value, str):
            value = value.encode()
        elif isinstance(value, array|dict|list|object):
            value = util.json_encode(value)
            assert isinstance(value, str)
            value = value.encode()
        else:
            value = str(value).encode()
        file = open(path, 'ab')
        file.write(value)
        file.close()
    def _file_append_json(path: str, value: dict|list):
        if not os.path.isfile(path):
            util.file_write(path, '[]')
        file = open(path, 'rb')
        data = file.read().decode()
        file.close()
        if not util.istype(data, 'string-array'):
            data = '[]'
        data = util.json_decode(data)
        assert isinstance(data, list)
        data.append(value)
        data = util.json_encode(data)
        assert isinstance(data, str)
        data = data.encode()
        file = open(path, 'wb')
        file.write(data)
        file.flush()
        file.close()
    def file_append_json(path: str, value: dict|list):
        if not os.path.isfile(path):
            util.file_write(path, '[]')
        file = open(path, 'rb')
        data = file.read().decode()
        file.close()
        data: list = util.json_decode(data)
        data.append(value)
        data: str = util.json_encode(data)
        data = data.encode()
        file = open(path, 'wb')
        file.write(data)
        file.flush()
        file.close()
    def file_directory(path: str, excludedPaths: list[str] = [], deep: int = None) -> dict:
        directory = {}
        def isExcludedPath(path: str) -> bool:
            path = path.lower()
            for excludedPath in excludedPaths:
                excludedPath = excludedPath.lower()
                if '**\\' == excludedPath[:3] and '\\*' == excludedPath[-2:]:
                    if excludedPath[2:-1] in path: return True
                elif '**\\' == excludedPath[:3]:
                    if path.endswith(excludedPath[2:]): return True
                elif '\\*' == excludedPath[-2:]:
                    if path.startswith(excludedPath[:-1]): return True
                else:
                    if path == excludedPath: return True
            return False
        def directoryItem(name: str, path: str) -> dict:
            return {
                'isdir': 1 if os.path.isdir(path) else 0,
                'items': {},
                'name': name,
                'path': path,
                'size': util.file_size(path),
                'timestamp': util.file_timestamp(path, 'milliseconds'),
            }
        if deep != None:
            deep = len(path.split('\\')) + deep
        for (path, folders, files) in os.walk(path):
            if deep != None:
                if len(path.split('\\')) >= deep: continue
            if isExcludedPath(path): continue
            items = directory
            for name in path.split('\\'):
                if name in items:
                    items = items[name]['items']
            for name in folders:
                if isExcludedPath(f"{path}\\{name}"): continue
                items[name] = directoryItem(name, f"{path}\\{name}")
            for name in files:
                if isExcludedPath(f"{path}\\{name}"): continue
                items[name] = directoryItem(name, f"{path}\\{name}")
        return directory
    def file_hash(path: str, mode: str = 'md5') -> str:
        data = util.file_read(path)
        if mode == util.HASH_MD5:
            return util.hash_md5(data)
        elif mode == util.HASH_SHA1:
            return util.hash_sha1(data)
        elif mode == util.HASH_SHA224:
            return util.hash_sha224(data)
        elif mode == util.HASH_SHA256:
            return util.hash_sha256(data)
        elif mode == util.HASH_SHA384:
            return util.hash_sha384(data)
        elif mode == util.HASH_SHA512:
            return util.hash_sha512(data)
        else:
            util.system_log(__file__, inspect.currentframe().f_lineno, f"ValueError: {mode}")
            return ''
    def file_path(path: str, option: str = None) -> dict[str, str]|str:
        delimiter = '/' if '/' in path else '\\'
        # example: C:\\path\\filename.ext
        value = {
            # example: c:\\folder
            'dirname': path[0:path.rindex(delimiter)] if delimiter in path else None,
            # example: filename.ext
            'basename': path[path.rindex(delimiter) + 1:] if delimiter in path else None,
            # example: ext
            'extension': path[path.rindex('.') + 1:] if '.' in path else None,
            # example: filename
            'filename': path[path.rindex(delimiter) + 1: path.rindex('.')] if delimiter in path and '.' in path else None,
        }
        return value if option == None else value[option]
    def file_read(path: str, size: int = None) -> bytes:
        file = open(path, 'rb')
        data = file.read(size)
        file.close()
        return data
    def file_read_data(path: str) -> dict:
        dataTypes = {
            'list':{
                'lines': 'multiple', 
                'type': 'object', 
            }, 
            'name': {
                'lines': 'single', 
                'type': 'string', 
            },
            'reference': {
                'lines': 'single', 
                'type': 'array', 
            }, 
            'subtitle': {
                'lines': 'single', 
                'type': 'string', 
            },
            'table': {
                'lines': 'multiple', 
                'type': 'object', 
            }, 
            'title': {
                'lines': 'single', 
                'type': 'string', 
            },
        }
        def isBlank(line: str):
            return line.strip(' ') == ''
        def hasKey(key: str, line: str):
            return line.find(key) == 0
        def getLines(lines, index):
            value = ''
            while index < len(lines):
                line = lines[index]
                if isBlank(line): break
                value += ('' if value == '' else '\n') + line
                index += 1
            return value, index
        def getValue(key: str, string: str):
            if key == 'list':
                return [(line.strip(' ')) for line in string.split('\n')]
            if key == 'name':
                return string
            if key == 'reference':
                return [(substring.strip(' ')) for substring in string.split(',')]
            if key == 'subtitle':
                return string
            if key == 'table':
                def getHeaders(string: str, delimiter: str = '     '):
                    headers = {}
                    delimiterLength = len(delimiter)
                    stringLength = len(string)
                    sIndex = 0
                    cIndex = 0
                    while cIndex < len(string):
                        if cIndex == stringLength -1:
                            header = string[sIndex:cIndex + 1].strip(' ')
                            headers[header] = [sIndex, -1]
                        if string[cIndex:cIndex + delimiterLength] == delimiter and string[cIndex + delimiterLength] != ' ':
                            header = string[sIndex:cIndex + delimiterLength - 1].strip(' ')
                            headers[header] = [sIndex, cIndex + delimiterLength - 1]
                            sIndex = cIndex + delimiterLength
                        cIndex += 1
                    return headers
                entries = []
                lines = string.split('\n')
                headers = getHeaders(lines[0])
                for index in range(1, len(lines), 1):
                    line = lines[index]
                    entries.append({})
                    for header in headers:
                        indexes = headers[header]
                        sIndex = indexes[0]
                        eIndex = len(line) if indexes[1] == -1 else indexes[1]
                        entries[len(entries)-1][header] = line[sIndex:eIndex].strip(' ')
                return entries
            if key == 'title':
                return string
        def decode(string: str):
            data = {}
            lines = string.replace('\r', '').split('\n')
            index = 0
            for key, dataType in dataTypes.items():
                if dataType['type'] == 'array':
                    data[key] = []
                if dataType['type'] == 'object':
                    data[key] = {}
                if dataType['type'] == 'string':
                    data[key] = ''
            while index < len(lines):
                line = lines[index]
                for key, dataType in dataTypes.items():
                    if hasKey(key, line):
                        keyvalue = line[len(key) + 1:len(line)].strip(' ')
                        value = None
                        if dataType['lines'] == 'single':
                            value = getValue(key, keyvalue)
                        if dataType['lines'] == 'multiple':
                            value, index = getLines(lines, index + 1)
                            value = getValue(key, value)
                        if dataType['type'] == 'array':
                            data[key].append(value)
                        if dataType['type'] == 'object':
                            data[key][keyvalue] = value
                        if dataType['type'] == 'string':
                            data[key] = value
                        break
                index += 1
            return data
        data = util.file_read_string(path)
        data = decode(data)
        return data
    def file_read_json(path: str) -> dict|list:
        data: bytes = util.file_read(path)
        data = data.decode()
        return util.json_decode(data)
    def file_read_list(path: str) -> list:
        data = util.file_read(path).decode()
        return [(val.strip(' \r')) for val in data.split('\n') if val.strip(' ') != '']
    def file_read_string(path: str, size: int = None) -> str:
        data = util.file_read(path).decode()
        return data
    def file_size(path: str) -> int:
        # bytes
        return os.path.getsize(path)
    def file_timestamp(path: str, options: str = 'milliseconds') -> int:
        # returns milliseconds
        if options == 'milliseconds':
            return int(os.path.getmtime(path) * 1000)
        else:
            return int(os.path.getmtime(path))
    def file_write(path: str, value: bytes|dict|int|float|list|str):
        forbiddenCharacters = {
            '"': '&quot;', 
            '*': '&ast;', 
            '/': '&sol;', 
            ':': '&colon;', 
            '<': '&lt;', 
            '>': '&gt;', 
            '?': '&quest;', 
            '\\': '&bsol;', 
            '|': '&verbar;', 
        }
        pathInfo = util.path_info(path)
        changedFilename = False
        filename: str = util.path_info(path, 'filename')
        for forbiddenCharacter, replacementCharacter in forbiddenCharacters.items():
            if forbiddenCharacter in filename:
                changedFilename = True
                filename = filename.replace(forbiddenCharacter, replacementCharacter)
        if changedFilename:
            path = f"{pathInfo['dirname']}\\{filename}.{pathInfo['extension']}"
        if isinstance(value, bytes):
            pass
        elif isinstance(value, str):
            value = value.encode()
        elif isinstance(value, dict|list):
            value = util.json_encode(value).encode()
        elif isinstance(value, array|object):
            value = util.json_encode(value.data).encode()
        else:
            value = str(value).encode()
        file = open(path, 'wb')
        file.write(value)
        file.close()
    def file_write_data(path: str, data: dict):
        pass
    def file_write_json(path: str, value: dict|list):
        value = util.json_encode(value).encode()
        util.file_write(path, value)
    def file_write_list(path: str, value: list):
        value = '\n'.join(value).encode()
        util.file_write(path, value)
    def fraction_to_percentage(numerator: float, denominator: float) -> float:
        return round(numerator / denominator * 100, 3)
    # g
    def geographic_ddd_to_ddm(point: list[str]) -> list[str]:
        if not util.istype(point, 'coordinates-geographic-ddd'):
            raise ValueError(f"ValueError: variable-name=point variable-value={point} >>> Invalid format")
        point = [float(point[0]), float(point[1])]
        degrees = int(abs(point[0]))
        minutes = int((abs(point[0]) - degrees) * 60)
        seconds = int(round((abs(point[0]) - degrees - minutes / 60) * 3600, 0))
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            degrees += 1
        direction = 'N' if point[0] >= 0 else 'S'
        decimal_minutes = minutes + seconds/60
        latitude = f"{degrees:02d}{decimal_minutes:05.2f}{direction}"
        degrees = int(abs(point[1]))
        minutes = int((abs(point[1]) - degrees) * 60)
        seconds = int(round((abs(point[1]) - degrees - minutes / 60) * 3600, 0))
        if seconds == 60:
            minutes += 1
            seconds = 0
        if minutes == 60:
            degrees += 1
            minutes = 0
        direction = 'E' if point[1] >= 0 else 'W'
        decimal_minutes = minutes + seconds/60
        longitude = f"{degrees:03d}{decimal_minutes:05.2f}{direction}"
        return [latitude, longitude]
    def geographic_ddd_to_dms(point: list[str]) -> list[str]:
        if not util.istype(point, 'coordinates-geographic-ddd'):
            raise ValueError(f"ValueError: variable-name=point variable-value={point} >>> Invalid format")
        point = [float(point[0]), float(point[1])]
        degrees = int(abs(point[0]))
        minutes = int((abs(point[0]) - degrees) * 60)
        seconds = int(round((abs(point[0]) - degrees - minutes / 60) * 3600, 0))
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            degrees += 1
        direction = 'N' if point[0] >= 0 else 'S'
        latitude = f"{degrees:02d}{minutes:02d}{seconds:02d}{direction}"
        degrees = int(abs(point[1]))
        minutes = int((abs(point[1]) - degrees) * 60)
        seconds = int(round((abs(point[1]) - degrees - minutes / 60) * 3600, 0))
        if seconds == 60:
            minutes += 1
            seconds = 0
        if minutes == 60:
            degrees += 1
            minutes = 0
        direction = 'E' if point[1] >= 0 else 'W'
        longitude = f"{degrees:03d}{minutes:02d}{seconds:02d}{direction}"
        return [latitude, longitude]
    def geographic_ddm_to_ddd(point: list[str]) -> list[str]:
        if '°' in point[0] or '*' in point[0]:
            if point[0][0] == 'N' or point[0][0] == 'S':
                pattern = r"^(?P<direction>N|S)(?P<degrees>[0-9]|[0-8][0-9])(°|\*)?(?P<decimal_minutes>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9]|[0-9][0-9]))'?$"
            if point[0][-1] == 'N' or point[0][-1] == 'S':
                pattern = r"^(?P<degrees>[0-9]|[0-8][0-9])(°|\*)?(?P<decimal_minutes>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9]|[0-9][0-9]))'?(?P<direction>N|S)$"
        else:
            if point[0][0] == 'N' or point[0][0] == 'S':
                pattern = r"^(?P<direction>N|S)(?P<degrees>[0-8][0-9])(?P<decimal_minutes>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9][0-9]))(?P<direction>N|S)$"
            if point[0][-1] == 'N' or point[0][-1] == 'S':
                pattern = r"^(?P<degrees>[0-8][0-9])(?P<decimal_minutes>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9][0-9]))$"
        match = re.match(pattern, point[0])
        groups = match.groupdict()
        degrees = int(groups["degrees"])
        minutes = float(groups['decimal_minutes'])
        direction = groups["direction"]
        decimal_degrees = degrees + minutes/60
        decimal_degrees *= 1 if direction == 'N' else -1
        latitude = f"{decimal_degrees:.6f}"
        if '°' in point[1] or '*' in point[1]:
            if point[1][0] == 'E' or point[1][0] == 'W':
                pattern = r"^(?P<direction>E|W)(?P<degrees>[0-9]|0[0-9][0-9]|1[0-7][0-9])(°|\*)?(?P<decimal_minutes>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9]|[0-9][0-9]))'?$"
            if point[1][-1] == 'E' or point[1][-1] == 'W':
                pattern = r"^(?P<degrees>[0-9]|0[0-9][0-9]|1[0-7][0-9])(°|\*)?(?P<decimal_minutes>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9]|[0-9][0-9]))'?(?P<direction>E|W)$"
        else:
            if point[1][0] == 'E' or point[1][0] == 'W':
                pattern = r"^(?P<direction>E|W)(?P<degrees>0[0-9][0-9]|1[0-7][0-9])(?P<decimal_minutes>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9][0-9]))$"
            if point[1][-1] == 'E' or point[1][-1] == 'W':
                pattern = r"^(?P<degrees>0[0-9][0-9]|1[0-7][0-9])(?P<decimal_minutes>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9][0-9]))(?P<direction>E|W)$"
        match = re.match(pattern, point[1])
        groups = match.groupdict()
        degrees = int(groups["degrees"])
        minutes = float(groups['decimal_minutes'])
        direction = groups["direction"]
        decimal_degrees = degrees + minutes/60
        decimal_degrees *= 1 if direction == 'E' else -1
        longitude = f"{decimal_degrees:.6f}"
        return [latitude, longitude]
    def geographic_ddm_to_dms(point: list[str]) -> list[str]:
        if '°' in point[0] or '*' in point[0]:
            if point[0][0] == 'N' or point[0][0] == 'S':
                pattern = r"^(?P<direction>N|S)(?P<degrees>[0-9]|[0-8][0-9])(°|\*)?(?P<decimal_minutes>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9]|[0-9][0-9]))'?$"
            if point[0][-1] == 'N' or point[0][-1] == 'S':
                pattern = r"^(?P<degrees>[0-9]|[0-8][0-9])(°|\*)?(?P<decimal_minutes>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9]|[0-9][0-9]))'?(?P<direction>N|S)$"
        else:
            if point[0][0] == 'N' or point[0][0] == 'S':
                pattern = r"^(?P<direction>N|S)(?P<degrees>[0-8][0-9])(?P<decimal_minutes>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9][0-9]))(?P<direction>N|S)$"
            if point[0][-1] == 'N' or point[0][-1] == 'S':
                pattern = r"^(?P<degrees>[0-8][0-9])(?P<decimal_minutes>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9][0-9]))$"
        match = re.match(pattern, point[0])
        groups = match.groupdict()
        degrees = int(groups["degrees"])
        minutes = float(groups['decimal_minutes'])
        direction = groups["direction"]
        decimal_degrees = degrees + minutes/60
        decimal_degrees *= 1 if direction == 'N' else -1
        latitude = f"{decimal_degrees}"
        if '°' in point[1] or '*' in point[1]:
            if point[1][0] == 'E' or point[1][0] == 'W':
                pattern = r"^(?P<direction>E|W)(?P<degrees>[0-9]|0[0-9][0-9]|1[0-7][0-9])(°|\*)?(?P<decimal_minutes>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9]|[0-9][0-9]))'?$"
            if point[1][-1] == 'E' or point[1][-1] == 'W':
                pattern = r"^(?P<degrees>[0-9]|0[0-9][0-9]|1[0-7][0-9])(°|\*)?(?P<decimal_minutes>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9]|[0-9][0-9]))'?(?P<direction>E|W)$"
        else:
            if point[1][0] == 'E' or point[1][0] == 'W':
                pattern = r"^(?P<direction>E|W)(?P<degrees>0[0-9][0-9]|1[0-7][0-9])(?P<decimal_minutes>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9][0-9]))$"
            if point[1][-1] == 'E' or point[1][-1] == 'W':
                pattern = r"^(?P<degrees>0[0-9][0-9]|1[0-7][0-9])(?P<decimal_minutes>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9][0-9]))(?P<direction>E|W)$"
        match = re.match(pattern, point[1])
        groups = match.groupdict()
        degrees = int(groups["degrees"])
        minutes = float(groups['decimal_minutes'])
        direction = groups["direction"]
        decimal_degrees = degrees + minutes/60
        decimal_degrees *= 1 if direction == 'E' else -1
        longitude = f"{decimal_degrees}"
        return util.geographic_ddd_to_dms([latitude, longitude])
    def geographic_dms_to_ddd(point: list[str]) -> list[str]:
        if '°' in point[0] or '*' in point[0]:
            if point[0][0] == 'N' or point[0][0] == 'S':
                pattern = r"^(?P<direction>N|S)(?P<degrees>[0-9]|[0-8][0-9])(°|\*)?(?P<minutes>[0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])'?(?P<seconds>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(\.\d+)?)\"?$"
            if point[0][-1] == 'N' or point[0][-1] == 'S':
                pattern = r"^(?P<degrees>[0-9]|[0-8][0-9])(°|\*)?(?P<minutes>[0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])'?(?P<seconds>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(\.\d+)?)\"?(?P<direction>N|S)$"
        else:
            if point[0][0] == 'N' or point[0][0] == 'S':
                pattern = r"^(?P<direction>N|S)(?P<degrees>[0-8][0-9])(?P<minutes>0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(?P<seconds>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(\.\d+)?)$"
            if point[0][-1] == 'N' or point[0][-1] == 'S':
                pattern = r"^(?P<degrees>[0-8][0-9])(?P<minutes>0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(?P<seconds>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(\.\d+)?)(?P<direction>N|S)$"
        match = re.match(pattern, point[0])
        groups = match.groupdict()
        degrees = int(groups["degrees"])
        minutes = int(groups["minutes"])
        seconds = float(groups["seconds"])
        direction = groups["direction"]
        decimal_degrees = degrees + minutes/60 + seconds/3600
        decimal_degrees *= 1 if direction == 'N' else -1
        latitude = f"{decimal_degrees}"
        if '°' in point[1] or '*' in point[1]:
            if point[1][0] == 'E' or point[1][0] == 'W':
                pattern = r"^(?P<direction>E|W)(?P<degrees>[0-9]|[0-9][0-9]|0[0-9][0-9]|1[0-7][0-9])(°|\*)?(?P<minutes>[0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])'?(?P<seconds>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(\.\d+)?)\"?$"
            if point[1][-1] == 'E' or point[1][-1] == 'W':
                pattern = r"^(?P<degrees>[0-9]|[0-9][0-9]|0[0-9][0-9]|1[0-7][0-9])(°|\*)?(?P<minutes>[0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])'?(?P<seconds>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(\.\d+)?)\"?(?P<direction>E|W)$"
        else:
            if point[1][0] == 'E' or point[1][0] == 'W':
                pattern = r"^(?P<direction>E|W)(?P<degrees>0[0-9][0-9]|1[0-7][0-9])(?P<minutes>0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(?P<seconds>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(\.\d+)?)$"
            if point[1][-1] == 'E' or point[1][-1] == 'W':
                pattern = r"^(?P<degrees>0[0-9][0-9]|1[0-7][0-9])(?P<minutes>0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(?P<seconds>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(\.\d+)?)(?P<direction>E|W)$"
        match = re.match(pattern, point[1])
        groups = match.groupdict()
        degrees = int(groups["degrees"])
        minutes = int(groups["minutes"])
        seconds = float(groups["seconds"])
        direction = groups["direction"]
        decimal_degrees = degrees + minutes/60 + seconds/3600
        decimal_degrees *= 1 if direction == 'E' else -1
        longitude = f"{decimal_degrees}"
        return [latitude, longitude]
    def geographic_dms_to_ddm(point: list[str]) -> list[str]:
        if '°' in point[0] or '*' in point[0]:
            if point[0][0] == 'N' or point[0][0] == 'S':
                pattern = r"^(?P<direction>N|S)(?P<degrees>[0-9]|[0-8][0-9])(°|\*)?(?P<minutes>[0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])'?(?P<seconds>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(\.\d+)?)\"?$"
            if point[0][-1] == 'N' or point[0][-1] == 'S':
                pattern = r"^(?P<degrees>[0-9]|[0-8][0-9])(°|\*)?(?P<minutes>[0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])'?(?P<seconds>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(\.\d+)?)\"?(?P<direction>N|S)$"
        else:
            if point[0][0] == 'N' or point[0][0] == 'S':
                pattern = r"^(?P<direction>N|S)(?P<degrees>[0-8][0-9])(?P<minutes>0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(?P<seconds>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(\.\d+)?)$"
            if point[0][-1] == 'N' or point[0][-1] == 'S':
                pattern = r"^(?P<degrees>[0-8][0-9])(?P<minutes>0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(?P<seconds>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(\.\d+)?)(?P<direction>N|S)$"
        match = re.match(pattern, point[0])
        groups = match.groupdict()
        degrees = int(groups["degrees"])
        minutes = int(groups["minutes"])
        seconds = float(groups["seconds"])
        direction = groups["direction"]
        decimal_minutes = minutes + seconds/60
        latitude = f"{degrees:02d}{decimal_minutes:05.2f}{direction}"
        if '°' in point[1] or '*' in point[1]:
            if point[1][0] == 'E' or point[1][0] == 'W':
                pattern = r"^(?P<direction>E|W)(?P<degrees>[0-9]|[0-9][0-9]|0[0-9][0-9]|1[0-7][0-9])(°|\*)?(?P<minutes>[0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])'?(?P<seconds>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(.\d+)?)\"?$"
            if point[1][-1] == 'E' or point[1][-1] == 'W':
                pattern = r"^(?P<degrees>[0-9]|[0-9][0-9]|0[0-9][0-9]|1[0-7][0-9])(°|\*)?(?P<minutes>[0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])'?(?P<seconds>([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(.\d+)?)\"?(?P<direction>E|W)$"
        else:
            if point[1][0] == 'E' or point[1][0] == 'W':
                pattern = r"^(?P<direction>E|W)(?P<degrees>0[0-9][0-9]|1[0-7][0-9])(?P<minutes>0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(?P<seconds>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(.\d+)?)$"
            if point[1][-1] == 'E' or point[1][-1] == 'W':
                pattern = r"^(?P<degrees>0[0-9][0-9]|1[0-7][0-9])(?P<minutes>0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(?P<seconds>(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(.\d+)?)(?P<direction>E|W)$"
        match = re.match(pattern, point[1])
        groups = match.groupdict()
        degrees = int(groups["degrees"])
        minutes = int(groups["minutes"])
        seconds = float(groups["seconds"])
        direction = groups["direction"]
        decimal_minutes = minutes + seconds/60
        longitude = f"{degrees:03d}{decimal_minutes:05.2f}{direction}"
        return [latitude, longitude]
    def geographic_to_azimuth(point1: list[float], point2: list[float]) -> float:
        latitude1 = point1[0] * util.DEGREES_TO_RADIANS
        longitude1 = point1[1] * util.DEGREES_TO_RADIANS
        latitude2 = point2[0] * util.DEGREES_TO_RADIANS
        longitude2 = point2[1] * util.DEGREES_TO_RADIANS
        differenceLatitude = latitude2 - latitude1
        differenceLongitude = longitude2 - longitude1
        y = math.sin(differenceLongitude) * math.cos(latitude2)
        x = math.cos(latitude1) * math.sin(latitude2) - math.sin(latitude1) * math.cos(latitude2) * math.cos(differenceLongitude)
        theta = math.atan2(y, x)
        theta = util.mathematics_constrain(theta, 0, math.pi * 2)
        azimuth = theta * util.RADIANS_TO_DEGREES
        return azimuth
    def geographic_to_azimuth_rhumb(point1: list[float], point2: list[float]) -> float:
        latitude1 = point1[0] * util.DEGREES_TO_RADIANS
        longitude1 = point1[1] * util.DEGREES_TO_RADIANS
        latitude2 = point2[0] * util.DEGREES_TO_RADIANS
        longitude2 = point2[1] * util.DEGREES_TO_RADIANS
        differenceLatitude = latitude2 - latitude1
        differenceLongitude = longitude2 - longitude1
        if abs(differenceLongitude) > math.pi:
            differenceLongitude = -(2 * math.pi - differenceLongitude) if differenceLongitude > 0 else (2 * math.pi + differenceLongitude)
        aa = math.log(math.tan(latitude2 / 2 + math.pi / 4) / math.tan(latitude1 / 2 + math.pi / 4))
        theta = math.atan2(differenceLongitude, aa)
        theta = util.mathematics_constrain(theta, 0, math.pi * 2)
        azimuth = theta * util.RADIANS_TO_DEGREES
        return azimuth
    def geographic_to_cartesian(latitude: float, longitude: float, altitude: float) -> list[float]:
        r = util.SPHERE_RADIUS + altitude
        theta = (longitude if longitude >= 0 else 360 + longitude) * util.DEGREES_TO_RADIANS
        phi = (90 - latitude) * util.DEGREES_TO_RADIANS
        x = r * math.sin(phi) * math.cos(theta)
        y = r * math.sin(phi) * math.sin(theta)
        z = r * math.cos(phi)
        return [x, y, z]
    def geographic_to_center_point(point1: list[float], point2: list[float]) -> list[float]:
        distance = util.geographic_to_distance(point1, point2)
        azimuth = util.geographic_to_azimuth(point1, point2)
        return util.geographic_to_destination_point(point1, azimuth, distance/2)
    def geographic_to_destination_point(point: list[float], azimuth: float, distance: float) -> list[float]:
        # destination point from start point having traveled the given distance on the given initial bearing
        # distance: meters
        latitude = point[0] * util.DEGREES_TO_RADIANS
        longitude = point[1] * util.DEGREES_TO_RADIANS
        theta = azimuth * util.DEGREES_TO_RADIANS
        angularDistance = distance / util.SPHERE_RADIUS
        destinationLatitude = math.asin(math.sin(latitude) * math.cos(angularDistance) + math.cos(latitude) * math.sin(angularDistance) * math.cos(theta))
        destinationLongitude = longitude + math.atan2(math.sin(theta) * math.sin(angularDistance) * math.cos(latitude), math.cos(angularDistance) - math.sin(latitude) * math.sin(destinationLatitude))
        destinationLatitude *= util.RADIANS_TO_DEGREES
        destinationLongitude *= util.RADIANS_TO_DEGREES
        return [destinationLatitude, destinationLongitude]
    def geographic_to_distance(point1: list[float], point2: list[float]) -> float:
        # distance along the surface of the earth from source point to destination point, great circle (shortest distance)
        # haversine formula
        latitude1 = point1[0] * util.DEGREES_TO_RADIANS
        longitude1 = point1[1] * util.DEGREES_TO_RADIANS
        latitude2 = point2[0] * util.DEGREES_TO_RADIANS
        longitude2 = point2[1] * util.DEGREES_TO_RADIANS
        differenceLatitude = latitude2 - latitude1
        differenceLongitude = longitude2 - longitude1
        a = math.sin(differenceLatitude / 2) ** 2 + math.cos(latitude1) * math.cos(latitude2) * math.sin(differenceLongitude / 2) ** 2
        c = 2 * math.atan2(a ** 0.5, (1 - a) ** 0.5)
        distance = util.SPHERE_RADIUS * c
        return distance
    def geographic_to_distance_offset(point: list[float], pointStart: list[float], pointEnd: list[float]) -> float: # inaccurate
        # distance of a point from a great-circle path (sometimes called cross track error)
        angularDistance = util.geographic_to_distance(pointStart, point) / util.SPHERE_RADIUS
        theta1 = util.geographic_to_azimuth(pointStart, point) * util.DEGREES_TO_RADIANS
        theta2 = util.geographic_to_azimuth(pointStart, pointEnd) * util.DEGREES_TO_RADIANS
        aa = math.asin(math.sin(angularDistance) * math.sin(theta1 - theta2))
        return aa * util.SPHERE_RADIUS
    def geographic_to_distance_rhumb(point1: list[float], point2: list[float]) -> float:
        # distance traveling from starting point to destination point along a rhumb line
        latitude1 = point1[0] * util.DEGREES_TO_RADIANS
        longitude1 = point1[1] * util.DEGREES_TO_RADIANS
        latitude2 = point2[0] * util.DEGREES_TO_RADIANS
        longitude2 = point2[1] * util.DEGREES_TO_RADIANS
        differenceLatitude = latitude2 - latitude1
        differenceLongitude = longitude2 - longitude1
        if abs(differenceLongitude) > math.pi:
            differenceLongitude = -(2 * math.pi - differenceLongitude) if differenceLongitude > 0 else (2 * math.pi + differenceLongitude)
        aa = math.log(math.tan(latitude2 / 2 + math.pi / 4) / math.tan(latitude1 / 2 + math.pi / 4))
        stretchFactor = differenceLatitude / aa if abs(aa) > 10e-12 else math.cos(latitude1)
        angularDistance = (differenceLatitude * differenceLatitude + stretchFactor * stretchFactor * differenceLongitude * differenceLongitude) ** 0.5
        distance = angularDistance * util.SPHERE_RADIUS
        return distance
    def geographic_to_elevation(point1: list[float], point2: list[float]) -> float: # inaccurate
        [x1, y1, z1] = util.geographic_to_cartesian(point1[0], point1[1], point1[2])
        [x2, y2, z2] = util.geographic_to_cartesian(point2[0], point2[1], point2[2])
        dx = x2 - x1
        dy = y2 - y1
        dz = z2 - z1
        distance = (dx ** 2 + dy ** 2 + dz ** 2) ** 0.5
        vx = dx / distance
        vy = dy / distance
        vz = dz / distance
        elevation = 90.0 - (180.0 / math.pi) * math.acos(vx * x1 + vy * y1 + vz * z1)
        return elevation
    def geographic_to_intermediate_point(point1: list[float], point2: list[float], fractionOfDistance: float = 0.5) -> list[float]:
        distance = util.geographic_to_distance(point1, point2)
        latitude1 = point1[0] * util.DEGREES_TO_RADIANS
        longitude1 = point1[1] * util.DEGREES_TO_RADIANS
        latitude2 = point2[0] * util.DEGREES_TO_RADIANS
        longitude2 = point2[1] * util.DEGREES_TO_RADIANS
        a = math.sin((1 - fractionOfDistance) * distance) / math.sin(distance)
        b = math.sin(fractionOfDistance * distance) / math.sin(distance)
        x = a * math.cos(latitude1) * math.cos(longitude1) + b * math.cos(latitude2) * math.cos(longitude2)
        y = a * math.cos(latitude1) * math.sin(longitude1) + b * math.cos(latitude2) * math.sin(longitude2)
        z = a * math.sin(latitude1) + b * math.sin(latitude2)
        latitude = math.atan2(z, (x ** 2 + y ** 2) ** 0.5) * util.RADIANS_TO_DEGREES
        longitude = math.atan2(y, x) * util.RADIANS_TO_DEGREES
        return [latitude, longitude]
    def geographic_to_intersection_point(point1: list[float], azimuth1: float, point2: list[float], azimuth2: float) -> list[float]|None:
        # point of intersection of two paths defined by point and bearing
        latitude1 = point1[0] * util.DEGREES_TO_RADIANS
        longitude1 = point1[1] * util.DEGREES_TO_RADIANS
        latitude2 = point2[0] * util.DEGREES_TO_RADIANS
        longitude2 = point2[1] * util.DEGREES_TO_RADIANS
        differenceLatitude = latitude2 - latitude1
        differenceLongitude = longitude2 - longitude1
        theta1 = azimuth1 * util.DEGREES_TO_RADIANS
        theta2 = azimuth2 * util.DEGREES_TO_RADIANS
        angularDistance = 2 * math.asin(math.sqrt(math.sin(differenceLatitude / 2) * math.sin(differenceLatitude / 2) + math.cos(latitude1) * math.cos(latitude2) * math.sin(differenceLongitude / 2) * math.sin(differenceLongitude / 2)))
        if abs(angularDistance) < math.ulp(1.0):
            return [point1[0], point1[1]]
        initialAzimuth = (math.sin(latitude2) - math.sin(latitude1) * math.cos(angularDistance)) / (math.sin(angularDistance) * math.cos(latitude1))
        finalAzimuth = (math.sin(latitude1) - math.sin(latitude2) * math.cos(angularDistance)) / (math.sin(angularDistance) * math.cos(latitude2))
        initialAzimuth = math.acos(math.min(math.max(initialAzimuth, -1), 1))
        finalAzimuth = math.acos(math.min(math.max(finalAzimuth, -1), 1))
        initialTheta = initialAzimuth if math.sin(longitude2 - longitude1) > 0 else 2 * math.pi - initialAzimuth
        finalTheta = 2 * math.pi - finalAzimuth if math.sin(longitude2 - longitude1) > 0 else finalAzimuth
        angle1 = theta1 - initialTheta
        angle2 = finalTheta - theta2
        if math.sin(angle1) == 0 and math.sin(angle2) == 0:
            return None
        if math.sin(angle1) * math.sin(angle2) < 0:
            return None
        aa = -math.cos(angle1) * math.cos(angle2) + math.sin(angle1) * math.sin(angle2) * math.cos(angularDistance)
        bb = math.atan2(math.sin(angularDistance) * math.sin(angle1) * math.sin(angle2), math.cos(angle2) + math.cos(angle1) * aa)
        destinationLatitude = math.asin(math.min(math.max(math.sin(latitude1) * math.cos(bb) + math.cos(latitude1) * math.sin(bb) * math.cos(theta1), -1), 1))
        cc = math.atan2(math.sin(theta1) * math.sin(bb) * math.cos(latitude1), math.cos(bb) - math.sin(latitude1) * math.sin(destinationLatitude))
        destinationLongitude = longitude1 + cc
        destinationLatitude *= util.RADIANS_TO_DEGREES
        destinationLongitude *= util.RADIANS_TO_DEGREES
        return [destinationLatitude, destinationLongitude]
    def _geographic_to_midpoint(point1: list[float], point2: list[float]) -> list[float]:
        latitude1 = point1[0] * util.DEGREES_TO_RADIANS
        longitude1 = point1[1] * util.DEGREES_TO_RADIANS
        latitude2 = point2[0] * util.DEGREES_TO_RADIANS
        longitude2 = point2[1] * util.DEGREES_TO_RADIANS
        differenceLatitude = latitude2 - latitude1
        differenceLongitude = longitude2 - longitude1
        bx = math.cos(latitude2) * math.cos(differenceLatitude)
        by = math.cos(latitude2) * math.sin(differenceLatitude)
        latitude = math.atan2(math.sin(latitude1) + math.sin(latitude2), ((math.cos(latitude1) + bx) ** 2 + by ** 2) ** 0.5) * util.RADIANS_TO_DEGREES
        longitude = point1[1] + (math.atan2(by, math.cos(longitude1) + bx) * util.RADIANS_TO_DEGREES)
        return [latitude, longitude]
    def geographic_to_midpoint(point1: list[float], point2: list[float]) -> list[float]:
        azimuth = util.geographic_to_azimuth(point1, point2)
        distance = util.geographic_to_distance(point1, point2)
        latitude, longitude = util.geographic_to_destination_point(point1, azimuth, distance/2)
        return [latitude, longitude]
    def geographic_to_spherical(latitude: float, longitude: float, altitude: float) -> list[float]:
        r = util.SPHERE_RADIUS + altitude
        theta = (longitude if longitude >= 0 else 360 + longitude) * util.DEGREES_TO_RADIANS
        phi = (90 - latitude) * util.DEGREES_TO_RADIANS
        return [r, theta, phi]
    def geometry_area_circle(radius: float) -> float:
        return math.pi * radius ** 2
    def geometry_area_cylinder(radius: float, height: float) -> float:
        return 2 * math.pi * radius * height + 2 * math.pi * radius ** 2
    def geometry_area_rectangle(length: float, width: float) -> float:
        return length * width
    def geometry_area_semicircle(radius: float) -> float:
        return (math.pi * radius ** 2) / 2
    def geometry_area_sphere(radius: float) -> float:
        return 4 * math.pi * radius ^ 2
    def geometry_area_square(length: float) -> float:
        return length ** 2
    def geometry_area_triangle(base: float, height: float) -> float:
        return (height * base) / 2
    def geometry_distance_formula(point1: list[float], point2: list[float]) -> float:
        return util.cartesian_to_distance(point1, point2)
    def geometry_midpoint_formula(point1: list[float], point2: list[float]) -> float:
        return util.cartesian_to_midpoint(point1, point2)
    def geometry_perimeter_circle(radius: float) -> float:
        return 2 * math.pi * radius
    def geometry_perimeter_semicircle(radius: float) -> float:
        return (math.pi * radius) + 2 * radius
    def geometry_perimeter_square(length: float) -> float:
        return 4 * length
    def geometry_perimeter_rectangle(length: float, width: float) -> float:
        return 2 * (length + width)
    def geometry_perimeter_triangle(sideA: float, sideB: float, sideC: float) -> float:
        return sideA + sideB + sideC
    def geometry_pythagorean_theorem(a: float = None, b: float = None, c: float = None) -> float:
        if a and b:
            return math.sqrt(a**2+b**2)
        if b and c:
            return math.sqrt(c**2-b**2)
        if c and a:
            return math.sqrt(c**2-a**2)
    def geometry_right_triangle(sideA: float = None, sideB: float = None, sideC: float = None, angleA: float = None, angleB: float = None, angleC: float = None) -> dict:
        values = {
            "sideA" : None,
            "sideB" : None,
            "sideC" : None,
            "angleA": None,
            "angleB": None,
            "angleC": 90,
            "h": None,
            "area": None,
            "perimeter": None
        }
        if sideA and sideB:
            values["sideA"] = sideA
            values["sideB"] = sideB
            values["sideC"] = math.sqrt(values["sideA"]**2+values["sideB"]**2)
            values["angleA"] = math.asin(values["sideA"]/values["sideC"])*util.RADIANS_TO_DEGREES
            values["angleB"] = math.asin(values["sideB"]/values["sideC"])*util.RADIANS_TO_DEGREES
        if sideB and sideC:
            values["sideB"] = sideB
            values["sideC"] = sideC
            values["sideA"] = math.sqrt(values["sideC"]**2-values["sideB"]**2)
            values["angleA"] = math.asin(values["sideA"]/values["sideC"])*util.RADIANS_TO_DEGREES
            values["angleB"] = math.asin(values["sideB"]/values["sideC"])*util.RADIANS_TO_DEGREES
        if sideC and sideA:
            values["sideC"] = sideC
            values["sideA"] = sideA
            values["sideB"] = math.sqrt(values["sideC"]**2-values["sideA"]**2)
            values["angleA"] = math.asin(values["sideA"]/values["sideC"])*util.RADIANS_TO_DEGREES
            values["angleB"] = math.asin(values["sideB"]/values["sideC"])*util.RADIANS_TO_DEGREES
        if sideA and angleA:
            values["sideA"] = sideA
            values["angleA"] = angleA
            values["sideC"] = values["sideA"]/math.sin(values["angleA"]*util.DEGREES_TO_RADIANS)
            values["sideB"] = math.sqrt(values["sideC"]**2-values["sideA"]**2)
            values["angleB"] = values["angleC"] - values["angleA"]
        if sideB and angleA:
            values["sideB"] = sideB
            values["angleA"] = angleA
            values["sideC"] = values["sideB"]/math.cos(values["angleA"]*util.DEGREES_TO_RADIANS)
            values["sideA"] = math.sqrt(values["sideC"]**2-values["sideB"]**2)
            values["angleB"] = values["angleC"] - values["angleA"]
        if sideC and angleA:
            values["sideC"] = sideC
            values["angleA"] = angleA
            values["sideA"] = values["sideC"]*math.sin(values["angleA"]*util.DEGREES_TO_RADIANS)
            values["sideB"] = math.sqrt(values["sideC"]**2-values["sideA"]**2)
            values["angleB"] = values["angleC"] - values["angleA"]
        if sideA and angleB:
            values["sideA"] = sideA
            values["angleB"] = angleB
            values["sideC"] = values["sideA"]/math.cos(values["angleB"]*util.DEGREES_TO_RADIANS)
            values["sideB"] = math.sqrt(values["sideC"]**2-values["sideA"]**2)
            values["angleA"] = values["angleC"] - values["angleB"]
        if sideB and angleB:
            values["sideB"] = sideB
            values["angleB"] = angleB
            values["sideC"] = values["sideB"]/math.sin(values["angleB"]*util.DEGREES_TO_RADIANS)
            values["sideA"] = math.sqrt(values["sideC"]**2-values["sideB"]**2)
            values["angleA"] = values["angleC"] - values["angleB"]
        if sideC and angleB:
            values["sideC"] = sideC
            values["angleB"] = angleB
            values["sideB"] = values["sideC"]*math.sin(values["angleB"]*util.DEGREES_TO_RADIANS)
            values["sideA"] = math.sqrt(values["sideC"]**2-values["sideB"]**2)
            values["angleA"] = values["angleC"] - values["angleB"]
        values["h"] = (values["sideA"]*values["sideB"])/values["sideC"]
        values["area"] = (values["sideA"]*values["sideB"])/2
        values["perimeter"] = values["sideA"]+values["sideB"]+values["sideC"]
        return values
    def geometry_volume_cone(radius: float, height: float) -> float:
        return math.pi * radius ** 2 * (height / 3)
    def geometry_volume_cube(length: float) -> float:
        return length ** 3
    def geometry_volume_cylinder(radius: float, height: float) -> float:
        return math.pi * radius ** 2 * height
    def geometry_volume_sphere(radius: float) -> float:
        return (4/3) * math.pi * radius ** 3
    # h
    def hash_md5(value: bytes|str) -> str:
        if util.importModule('hashlib'): import hashlib
        return hashlib.md5(value if type(value) == bytes else value.encode()).hexdigest()
    def hash_sha1(value: bytes|str) -> str:
        if util.importModule('hashlib'): import hashlib
        return hashlib.sha1(value if type(value) == bytes else value.encode()).hexdigest()
    def hash_sha224(value: bytes|str) -> str:
        if util.importModule('hashlib'): import hashlib
        return hashlib.sha224(value if type(value) == bytes else value.encode()).hexdigest()
    def hash_sha256(value: bytes|str) -> str:
        if util.importModule('hashlib'): import hashlib
        return hashlib.sha256(value if type(value) == bytes else value.encode()).hexdigest()
    def hash_sha384(value: bytes|str) -> str:
        if util.importModule('hashlib'): import hashlib
        return hashlib.sha384(value if type(value) == bytes else value.encode()).hexdigest()
    def hash_sha512(value: bytes|str) -> str:
        if util.importModule('hashlib'): import hashlib
        return hashlib.sha512(value if type(value) == bytes else value.encode()).hexdigest()
    def html_decode(string: str) -> dict:
        object = {}
        tags = []
        string = ''.join([line.strip(' ') for line in string.split('\r\n') if line != ''])

        def getTag(start: int):
            value = ''
            for i in range(start, len(string)):
                if string[i] == '>': break
                value += string[i]
            value = value.strip(' ')
            value = value.strip('/')
            value = value.strip(' ')
            tag = value[:value.index(' ') if ' ' in value else len(value)]
            return value

        for i in range(len(string)):
            if string[i] == '<':
                getTag(i+1)

        return object
    def html_encode(object: dict) -> str:
        pass
    # i
    def identifier(value: str = None) -> str:
        if value:
            nString = ''
            allowedCharacters = '- 0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z _ a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
            notAllowedFirstCharacters = '0 1 2 3 4 5 6 7 8 9'.split(' ')
            for i in range(0, len(value), 1):
                character = value[i]
                if i == 0 and character in notAllowedFirstCharacters:
                    nString += '_' + character
                elif not character in allowedCharacters:
                    nString += '_'
                else:
                    nString += character
            return nString.lower()
        else:
            # ULID: 128-bit | 16-characters
            # GUID: 128-bit util.dec2hex(util.timestamp())
            allowedFirstCharacters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
            allowedCharacters = '0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
            identifier = ''
            identifier += util.random(allowedFirstCharacters)
            for i in range(0, 9, 1):
                identifier += util.random(allowedCharacters)
            return identifier
    # j
    def javascript_run(path: str):
        if util.importModule('js2py'): import js2py
        """
        eval_res, tempfile = js2py.run_file(path)
        tempfile.calling_function("")
        """
        # runs in only ECMAScript 5
        return js2py.eval_js(path)
    def json_encode(value: dict|list) -> str:
        def typeConversion(value):
            # convert array to list and object to dict
            if isinstance(value, array|object):
                value = value.data
            if isinstance(value, dict):
                for k, v in value.items():
                    if isinstance(v, array|object):
                        value[k] = v.data
                        typeConversion(value[k])
            if isinstance(value, list):
                for i, v in enumerate(value):
                    if isinstance(v, array|object):
                        value[i] = v.data
                        typeConversion(value[i])
            return value
        value = typeConversion(value)
        try:
            return json.dumps(value)
        except:
            util.system_log(__file__, inspect.currentframe().f_lineno, f"TypeError: variable-name=value variable-type={type(value)} type=array|object")
            if isinstance(value, dict):
                return "{}"
            if isinstance(value, list):
                return "[]"
    def json_decode(value: str) -> dict|list:
        try:
            return json.loads(value)
        except:
            util.system_log(__file__, inspect.currentframe().f_lineno, f"TypeError: variable-name=value variable-type={type(value)} type=string-array|string-object")
            if util.istype(value, 'string-array'):
                return []
            if util.istype(value, 'string-object'):
                return {}
    # k

    # l
    def len(value, base: int = 1) -> int:
        if value == None: return 0
        if str(len(value) / base).split('.')[1] != '0': 
            util.system_log(__file__, inspect.currentframe().f_lineno, f"ValueError: variable-name=value variable-value={value}")
        return int(len(value) / base)
    def logic_gate_and(inputs: list[bool]) -> bool:
        # (A ⋅ B) = AND
        return all(inputs)
    def logic_gate_buffer(inputs: list[bool]) -> bool:
        # BUFFER
        return inputs[0]
    def logic_gate_imply(inputs: list[bool]) -> bool:
        # (A' + B) = IMPLY
        return (not all(inputs[:-1])) or inputs[-1]
    def logic_gate_nand(inputs: list[bool]) -> bool:
        # (A ⋅ B)' = AND + NOT = NAND
        return not all(inputs)
    def logic_gate_nimply(inputs: list[bool]) -> bool:
        # (A' + B)' = IMPLY + NOT = NIMPLY
        return not ((not all(inputs[:-1])) or inputs[-1])
    def logic_gate_not(inputs: list[bool]) -> bool:
        # A' = NOT
        return not inputs[0]
    def logic_gate_nor(inputs: list[bool]) -> bool:
        # (A + B)' = OR + NOT = NOR
        return not any(inputs)
    def logic_gate_or(inputs: list[bool]) -> bool:
        # (A + B) = OR
        return any(inputs)
    def logic_gate_xnor(inputs: list[bool]) -> bool:
        # (A ⋅ B) + (A' ⋅ B') = XOR + NOT = XNOR
        return not (sum(inputs) % 2 == 1)
    def logic_gate_xor(inputs: list[bool]) -> bool:
        # (A ⋅ B') + (A' ⋅ B) = XOR
        return sum(inputs) % 2 == 1
    # m
    def mathematics_constrain(number: float, minimum: float, maximum: float) -> float:
        if minimum <= number and number <= maximum:
            return number
        if number > maximum:
            return minimum + (number % maximum)
        if number < minimum:
            return number % maximum
    def mathematics_length(value: dict|list, base: int = 1) -> int:
        return int(len(value) / base)
    def mathematics_random(*values):
        if util.importModule('random'): import random
        # 1. list item
        if isinstance(values[0], list):
            index = random.randint(0, len(values[0])-1)
            return values[0][index]
        # 2. number range
        range = [0, values[0]] if len(values) == 1 else [values[0], values[1]]
        if len(values) == 1 or len(values) == 2:
            return random.randint(range[0], range[1])
        # 3. number range + round to nth place
        if len(values) == 3:
            placement = values[2]
            if placement > 0:
                random_number = random.randint(range[0], range[1])
                return util.mathematics_round(random_number, placement)
            if placement < 0:
                multiple = 10**-placement
                range = [int(range[0]*multiple), int(range[1]*multiple)]
                random_number = random.randint(range[0], range[1])
                return util.mathematics_round(random_number, placement) / multiple
    def mathematics_round(number: float, placement: int = 1) -> int|float:
        number_whole, number_rational = str(float(number)).split('.')
        if placement > 0:
            v = number / 10**placement
            number = round(round(v, 1) * 10**placement, 1)
        elif placement < 0 and len(number_rational) > -placement:
            number = round(number, -placement)
        number = util.mathematics_simplify(number)
        return number
    def mathematics_simplify(number: int|float) -> int|float:
        return int(number) if str(number)[-2:] == '.0' else number
    def mathematics_volume(x: float, y: float, z: float) -> float:
        return x * y * z
    def matrix_addition(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
        rows = len(matrix1)
        columns = len(matrix1[0])
        nMatrix = [[0] * columns for i in range(rows)]
        for i in range(rows):
            for j in range(columns):
                nMatrix[i][j] = matrix1[i][j] + matrix2[i][j]
        return nMatrix
    def matrix_combination(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
        return 
    def matrix_multiplication(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
        rows = len(matrix1)
        columns = len(matrix1[0])
        nMatrix = [[0] * columns for i in range(rows)]
        for i in range(rows):
            row = [0] * columns
            for j in range(columns):
                for k in range(columns):
                    row[k] += matrix1[i][j] * matrix2[j][k]
            nMatrix[i] = row
        return nMatrix
    def matrix_subtraction(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
        rows = len(matrix1)
        columns = len(matrix1[0])
        nMatrix = [[0] * columns for i in range(rows)]
        for i in range(rows):
            for j in range(columns):
                nMatrix[i][j] = matrix1[i][j] - matrix2[i][j]
        return nMatrix
    # n
    def network_ip() -> str:
        return socket.gethostbyname(socket.gethostname())
    def network_mtu(address: str) -> int:
        size = 1500
        def ping(size: int):
            res = os.popen(f'ping {address} -f -n 1 -l {size}').read()
            return not 'Packet needs to be fragmented but DF set.' in res
        while True:
            if ping(size):
                return size
            else:
                size -= 10
    def network_online(address: tuple = ('8.8.8.8', 53)) -> bool:
        try:
            socket.setdefaulttimeout(1)
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP).connect(address)
            return True
        except:
            return False
        finally:
            socket.setdefaulttimeout(None)
    def network_port() -> int:
        return util.random(1024, 65535)
    def network_port_registered() -> int:
        return util.random(1024, 49151)
    def network_port_unregistered() -> int:
        return util.random(49152, 65535)
    # o

    # p
    def pad(string: str, length: int, pad: str = ' ', type = 'l') -> str:
        length = length - len(string)
        if length <= 0: return string
        if type == 'l' or type == 'left':
            return ''.ljust(length, pad) + string
        if type == 'b' or type == 'both':
            left = length / 2 if length % 2 == 0 else (length - 1) / 2
            right = length - left
            return ''.ljust(left, pad) + string + ''.ljust(right, pad)
        if type == 'r' or type == 'right':
            return string + ''.ljust(length, pad)
    def path_info(path: str, option: str = None) -> dict[str, str]|str:
        delimiter = '/' if '/' in path else '\\'
        # example: C:\\path\\filename.ext
        value = {
            # example: c:\\folder
            'dirname': path[0:path.rindex(delimiter)] if delimiter in path else None,
            # example: filename.ext
            'basename': path[path.rindex(delimiter) + 1:] if delimiter in path else None,
            # example: ext
            'extension': path[path.rindex('.') + 1:] if '.' in path else None,
            # example: filename
            'filename': path[path.rindex(delimiter) + 1: path.rindex('.')] if delimiter in path and '.' in path else None,
        }
        return value if option == None else value[option]
    def polar_to_cartesian(r: float, theta: float) -> list[float]:
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        return [x, y]
    # q
    # r
    def radians_to_degrees(radians: float):
        return radians * util.RADIANS_TO_DEGREES
    def random(*values):
        if util.importModule('random'): import random
        # start and end included
        if isinstance(values[0], list):
            index = random.randint(0, len(values[0])-1)
            return values[0][index]
        range = [0, values[0]] if len(values) == 1 else [values[0], values[1]]
        random_number = random.randint(range[0], range[1])
        if len(values) == 3:
            random_number = int(round(random_number / values[2], 0) * values[2])
        return random_number
    def reference_encode(data: dict) -> str:
        pass
    def reference_decode(data: str) -> dict:
        results = {
            'ABBREVIATIONS': {},
            # key: {string: string}
            'ACRONYMS': {},
            # key: {string: string}
            'DEFINITIONS': {},
            # key: {string: string}
            'LIST': {},
            # key: [string]
            'NAME': '',
            # string
            'OBJECT': {},
            # key: {string: string}
            'QUESTIONS': {},
            # [{question: string, answers: [string], comment: string}]
            'SOURCE': [],
            # [string]
            'SUBTITLE': '',
            # string
            'TABLE': {},
            # key: [{string: string}]
            'TITLE': '',
            # string
        }
        # 
        def getTagValue(tagKey: str, line: str) -> str:
            tagValue: str = line[0+len(tagKey)+1:]
            tagValue = tagValue.strip(' ')
            tagValue = util.identifier() if tagValue == '' else tagValue
            return tagValue
        def getTagContent(lines: list, index: int, endKey = '') -> list[str]:
            tagContent = []
            while index + 1 < len(lines):
                index += 1
                line: str = lines[index]
                if line.startswith('#') or line.startswith('-----'): continue
                if line == endKey:
                    break
                tagContent += [line]
            return tagContent
        # 
        lines = [line.strip(' ') for line in data.splitlines()]
        index = -1
        while index < len(lines) - 1:
            index += 1
            line = lines[index]
            # line bypass
            if line.startswith('#') or line.startswith('-----'): continue
            # 
            tagKey = 'ABBREVIATIONS'
            if line.startswith(tagKey):
                tag = results[tagKey]
                assert isinstance(tag, dict)
                tagValue = getTagValue(tagKey, line)
                tagContentLines = getTagContent(lines, index)
                tagContent = dict([(s.lower().strip(' ') for s in line.split(':')) for line in tagContentLines])
                tag[tagValue] = tagContent
                index += len(tagContent) + 1
            tagKey = 'ACRONYMS'
            if line.startswith(tagKey):
                tag = results[tagKey]
                assert isinstance(tag, dict)
                tagValue = getTagValue(tagKey, line)
                tagContentLines = getTagContent(lines, index)
                tagContent = dict([(s.strip(' ') for s in line.split(':')) for line in tagContentLines])
                tagContent = dict((sk.upper(), sv) for sk, sv in tagContent.items())
                tag[tagValue] = tagContent
                index += len(tagContent) + 1
            tagKey = 'DEFINITIONS'
            if line.startswith(tagKey):
                tag = results[tagKey]
                assert isinstance(tag, dict)
                tagValue = getTagValue(tagKey, line)
                tagContentLines = getTagContent(lines, index)
                tagContent = dict([(s.strip(' ') for s in line.split(':')) for line in tagContentLines])
                tag[tagValue] = tagContent
                index += len(tagContent) + 1
            tagKey = 'LIST'
            if line.startswith(tagKey):
                tag = results[tagKey]
                assert isinstance(tag, dict)
                tagValue = getTagValue(tagKey, line)
                tagContentLines = getTagContent(lines, index)
                tagContent = tagContentLines
                tag[tagValue] = tagContent
                index += len(tagContent) + 1
            tagKey = 'NAME'
            if line.startswith(tagKey):
                tag = results[tagKey]
                assert isinstance(tag, str)
                tag = getTagValue(tagKey, line)
            tagKey = 'OBJECT'
            if line.startswith(tagKey):
                tag = results[tagKey]
                assert isinstance(tag, dict)
                tagValue = getTagValue(tagKey, line)
                tagContentLines = getTagContent(lines, index)
                tagContent = dict([(s.strip(' ') for s in line.split(':')) for line in tagContentLines])
                tag[tagValue] = tagContent
                index += len(tagContent) + 1
            tagKey = 'QUESTIONS'
            if line.startswith(tagKey):
                tag = results[tagKey]
                assert isinstance(tag, dict)
                tagValue = getTagValue(tagKey, line)
                tagContentLines = getTagContent(lines, index, 'BREAK')
                tagContent = []
                i = 0
                # ignore initial empty lines
                while tagContentLines[0] == '':
                    tagContentLines.pop(0)
                while i < len(tagContentLines):
                    if tagContentLines[i] == '':
                        tagContent.append({ 'question': '', 'answers': [], 'comment': '' })
                        j = i - 1
                        while j >= 0 and len(tagContentLines[j]) > 0:
                            if j == 0 or tagContentLines[j-1] == '':
                                tagContent[-1]['question'] = tagContentLines[j]
                            elif tagContentLines[j].startswith('###'):
                                tagContent[-1]['comment'] = tagContentLines[j]
                            else:
                                tagContent[-1]['answers'] = [tagContentLines[j]] + tagContent[-1]['answers']
                            j -= 1
                    i += 1
                tag[tagValue] = tagContent
                index += len(tagContent) + 1
            tagKey = 'SOURCE'
            if line.startswith(tagKey):
                tag = results[tagKey]
                assert isinstance(tag, list)
                tagValue = getTagValue(tagKey, line)
                tag.append(tagValue)
            tagKey = 'SUBTITLE'
            if line.startswith(tagKey):
                tag = results[tagKey]
                assert isinstance(tag, str)
                tag = getTagValue(tagKey, line)
            tagKey = 'TABLE'
            if line.startswith(tagKey):
                tag = results[tagKey]
                assert isinstance(tag, dict)
                tagValue = getTagValue(tagKey, line)
                tagContentLines = getTagContent(lines, index)
                tagContent = util.table_decode(tagContentLines)
                tag[tagValue] = tagContent
                index += len(tagContent) + 1
            tagKey = 'TITLE'
            if line.startswith(tagKey):
                tag = results[tagKey]
                assert isinstance(tag, str)
                tag = getTagValue(tagKey, line)
        return results
    def regular_expression_match(pattern: str, value: str) -> bool:
        return bool(re.match(pattern, value))
    def round(number: float, placement: int) -> float|int:
        # round non integer numbers by nth placement
        return round(number * (10 ** placement)) / (10 ** placement)
    # s
    def statistics_correlation_coefficient(numbers1: list[float], numbers2: list[float]):
        if len(numbers1) != len(numbers2): raise ValueError("Lists must have the same length.")
        xMean = util.statistics_mean(numbers1)
        yMean = util.statistics_mean(numbers2)
        xStandardDeviation = util.statistics_standard_deviation(numbers1)
        yStandardDeviation = util.statistics_standard_deviation(numbers2)
        if xStandardDeviation == 0 or yStandardDeviation == 0: return 0.0
        zScores1 = [(number - xMean) / xStandardDeviation for number in numbers1]
        zScores2 = [(number - yMean) / yStandardDeviation for number in numbers2]
        zScoresProduct = [zScore1 * zScore2 for zScore1, zScore2 in zip(zScores1, zScores2)]
        zScoreSum = util.statistics_sum(zScoresProduct)
        return (1 / (len(numbers1) - 1)) * zScoreSum
    def statistics_correlation_matrix(numbers: list[float]):
        return 
    def statistics_count(numbers: list[float]) -> float:
        return len(numbers)
    def statistics_maximum(numbers: list[float]) -> float:
        return max(*numbers)
    def statistics_mean(numbers: list[float]) -> float:
        return sum(numbers) / len(numbers)
    def statistics_median(numbers: list[float]) -> float:
        numbers.sort()
        n = len(numbers)
        if n % 2 == 0:
            return (numbers[math.floor(n / 2)] + numbers[math.floor((n / 2) - 1)]) / 2
        else:
            return numbers[math.floor((n / 2) - .5)]
    def statistics_minimum(numbers: list[float]) -> float:
        return min(*numbers)
    def statistics_mode(numbers: list[float]) -> float:
        frequencyCounts = {}
        maxFrequency = 0
        modes = []
        # Count the occurrences of each number
        for number in numbers:
            frequencyCounts[number] = (frequencyCounts[number] if number in frequencyCounts else 0) + 1
            maxFrequency = max(maxFrequency, frequencyCounts[number])
        # Find the numbers with the maximum frequency
        for number in frequencyCounts.keys():
            if frequencyCounts[number] == maxFrequency:
                modes.append(number)
        # return number with greatest occurrence
        return modes[0]
    def statistics_range(numbers: list[float]) -> float:
        return max(*numbers) - min(*numbers)
    def statistics_product(numbers: list[int]) -> int:
        if len(numbers) == 0: return 0
        product = 1
        for number in numbers: product *= number
        return int(product) if str(product)[-2:] == '.0' else product
    def statistics_standard_deviation(numbers: list[float]):
        return math.sqrt(util.statistics_variation(numbers))
    def statistics_sum(numbers: list[float]) -> float:
        return sum(numbers)
    def statistics_variation(numbers: list[float]) -> float:
        n = len(numbers)
        mean = util.statistics_mean(numbers)
        return sum([((number - mean) ** 2) for number in numbers]) / (n - 1)
    def string_conversion_encode(value: bool|dict|int|float|list) -> str:
        if value == None:
            return value
        elif util.istype(value, 'array'):
            return util.json_encode(value)
        elif util.istype(value, 'boolean'):
            return f"{value}"
        elif util.istype(value, 'number'):
            return f"{value}"
        elif util.istype(value, 'object'):
            return util.json_encode(value)
        else:
            return value
    def string_conversion_decode(value: str) -> bool|dict|int|float|list:
        if value == None:
            return value
        elif util.istype(value, 'string-array'):
            return util.json_decode(value)
        elif util.istype(value, 'string-boolean'):
            return value.lower() == 'true'
        elif util.istype(value, 'string-number-float'):
            return float(value)
        elif util.istype(value, 'string-number-integer'):
            return int(value)
        elif util.istype(value, 'string-object'):
            return util.json_decode(value)
        else:
            return value
    def spherical_to_cartesian(r: float, theta: float, phi: float) -> list[float]:
        x = r * math.sin(phi) * math.cos(theta)
        y = r * math.sin(phi) * math.sin(theta)
        z = r * math.cos(phi)
        return [x, y, z]
    def spherical_to_geographic(r: float, theta: float, phi: float) -> list[float]:
        latitude = 90 - (phi * util.RADIANS_TO_DEGREES)
        longitude = theta * util.RADIANS_TO_DEGREES
        longitude = longitude - 360 if longitude > 180 else longitude
        altitude = r - util.SPHERE_RADIUS
        return [latitude, longitude, altitude]
    def system_abspath(path: str):
        return os.path.dirname(os.path.abspath(path))
    def system_command(value: str):
        os.system(value)
    def system_log(path: str, line: int, *values):
        #example: util.system_log(__file__, inspect.currentframe().f_lineno, 'message')
        path = path[0].upper() + path[1:]
        output = ''
        for value in values:
            output += str(value)
        print(f"file:{path}:{line}", output)
        return None
    def system_module(name: str):
        return name in dir()
    def system_pid() -> int:
        return os.getpid()
    # t
    def table_encode(entries: list[dict[str, int|str]], orientation = 'vertical', delimiter: str = '     ') -> str:
        if entries == []: return ""
        headers = [*entries[0].keys()]
        rows = [[*entry.values()] for entry in entries]
        results = ""
        if orientation == 'vertical' or orientation == 'v':
            maxColumnLengths = []
            for x in range(len(headers)):
                maxColumnLengths.append(0)
                for y in range(1+len(rows)):
                    cell = str(headers[x] if y == 0 else rows[y-1][x]).strip(' ')
                    maxColumnLengths[x] = len(cell) if len(cell) > maxColumnLengths[x] else maxColumnLengths[x]
            results = delimiter.join([str(headers[x]).ljust(maxColumnLengths[x], ' ') for x in range(len(headers))])
            for row in rows:
                results += '\n' + delimiter.join([str(row[x]).ljust(maxColumnLengths[x], ' ') for x in range(len(row))])
            return results
        if orientation == 'horizontal' or orientation == 'h':
            maxColumnLengths = []
            for x in range(len(rows)+1):
                maxColumnLengths.append(0)
                for y in range(len(headers)):
                    cell = str(headers[y] if x == 0 else rows[x-1][y]).strip(' ')
                    maxColumnLengths[x] = len(cell) if len(cell) > maxColumnLengths[x] else maxColumnLengths[x]
            for y in range(len(headers)):
                results += "" if y == 0 else "\n"
                for x in range(len(rows)+1):
                    cell = str(headers[y] if x == 0 else rows[x-1][y]).ljust(maxColumnLengths[x], ' ')
                    results += cell
                    results += delimiter if x < len(rows) else ""
            return results
        return ""
    def _table_decode(string: str, delimiter: str = '     ') -> list[dict[str, int|str]]:
        entries = [  ]
        def getHeaders(string: str, delimiter: str) -> dict[str, list[int]]:
            headers = {  }
            indexStart = 0
            dLength = len(delimiter)
            index = 0
            while index < len(string):
                if index == len(string)-1:
                    value = string[indexStart:index+1].strip(' ')
                    headers[value] = [indexStart, -1]
                if string[index:index+dLength] == delimiter and string[index+dLength] != ' ':
                    value = string[indexStart:index+dLength-1].strip(' ')
                    headers[value] = [indexStart, index+dLength-1]
                    indexStart = index+dLength
                index += 1
            return headers
        lines = [line for line in string.split('\n') if len(line.strip(' ')) > 0]
        headers = getHeaders(lines[0], delimiter)
        for i in range(1, len(lines)):
            line = lines[i]
            entry = {  }
            for header, indexes in headers.items():
                indexStart = indexes[0]
                indexEnd = len(line) if indexes[1] == -1 else indexes[1]
                entry[header] = line[indexStart:indexEnd].strip(' ')
            entries.append(entry)
        return entries
    def table_decode(data: list|str, delimiter: str = '     ') -> list[dict[str, int|str]]:
        # NOTE: each header name must be unique
        rows = [  ]
        if util.istype(data, 'array-string'):
            lines = data
        if util.istype(data, 'string'):
            lines = data.splitlines()
        lines = [line for line in lines if len(line.strip(' ')) > 0]
        headers = [header.strip(' ') for header in lines[0].split(delimiter) if len(header.strip(' ')) > 0]
        if len(headers) == 0:
            raise ValueError(f"Invalid table format: no headers found.")
        for line in lines[1:]:
            cells = [cell.strip(' ') for cell in line.split(delimiter) if len(cell) > 0]
            if len(cells) != len(headers):
                raise ValueError("Invalid table format: row has incorrect number of columns.")
            row = dict(zip(headers, cells))
            rows.append(row)
        return rows
    def timestamp(value: datetime.datetime|int|str = None, convert_to: str = None) -> datetime.datetime|int|str:
        def convert(date: datetime.datetime, option: str) -> datetime.datetime|int|str:
            if option == None:
                return date
            if option.lower() == util.TIMESTAMP_OPTION_MILLISECONDS:
                return round((date.timestamp()) * 1000)
            if option.lower() == util.TIMESTAMP_OPTION_OBJECT:
                return date
            if option.lower() == util.TIMESTAMP_OPTION_SECONDS:
                return round(date.timestamp())
            if option.lower() == util.TIMESTAMP_OPTION_STRING:
                return date.strftime('%Y%m%dT%H%M%S') + 'Z'
            # if len(option) == 1 and util.regular_expression_match(r"^([A-I]|[K-Z])$"):
            #     zone_utc_offset = util.TIMEZONE_DESIGNATION_OFFSETS[option]
            #     timezoneTO = datetime.timezone(datetime.timedelta(hours=zone_utc_offset))
            #     return date.astimezone(timezoneTO)
        def getString(value) -> dict:
            if '-' in value:
                if len(value) == 4 or len(value) == 5:   pattern = f"{util.TIMESTAMP_PATTERN_YEAR}"
                if len(value) == 7 or len(value) == 8:   pattern = f"{util.TIMESTAMP_PATTERN_YEAR}-{util.TIMESTAMP_PATTERN_MONTH}"
                if len(value) == 10 or len(value) == 11: pattern = f"{util.TIMESTAMP_PATTERN_YEAR}-{util.TIMESTAMP_PATTERN_MONTH}-{util.TIMESTAMP_PATTERN_DAY}"
                if len(value) == 13 or len(value) == 14: pattern = f"{util.TIMESTAMP_PATTERN_YEAR}-{util.TIMESTAMP_PATTERN_MONTH}-{util.TIMESTAMP_PATTERN_DAY}T{util.TIMESTAMP_PATTERN_HOUR}"
                if len(value) == 16 or len(value) == 17: pattern = f"{util.TIMESTAMP_PATTERN_YEAR}-{util.TIMESTAMP_PATTERN_MONTH}-{util.TIMESTAMP_PATTERN_DAY}T{util.TIMESTAMP_PATTERN_HOUR}:{util.TIMESTAMP_PATTERN_MINUTE}"
                if len(value) == 19 or len(value) == 20: pattern = f"{util.TIMESTAMP_PATTERN_YEAR}-{util.TIMESTAMP_PATTERN_MONTH}-{util.TIMESTAMP_PATTERN_DAY}T{util.TIMESTAMP_PATTERN_HOUR}:{util.TIMESTAMP_PATTERN_MINUTE}:{util.TIMESTAMP_PATTERN_SECOND}"
                if len(value) == 23 or len(value) == 24: pattern = f"{util.TIMESTAMP_PATTERN_YEAR}-{util.TIMESTAMP_PATTERN_MONTH}-{util.TIMESTAMP_PATTERN_DAY}T{util.TIMESTAMP_PATTERN_HOUR}:{util.TIMESTAMP_PATTERN_MINUTE}:{util.TIMESTAMP_PATTERN_SECOND}.{util.TIMESTAMP_PATTERN_MILLISECOND}"
            else: 
                if len(value) == 4 or len(value) == 5:   pattern = f"{util.TIMESTAMP_PATTERN_YEAR}"
                if len(value) == 6 or len(value) == 7:   pattern = f"{util.TIMESTAMP_PATTERN_YEAR}{util.TIMESTAMP_PATTERN_MONTH}"
                if len(value) == 8 or len(value) == 9:   pattern = f"{util.TIMESTAMP_PATTERN_YEAR}{util.TIMESTAMP_PATTERN_MONTH}{util.TIMESTAMP_PATTERN_DAY}"
                if len(value) == 11 or len(value) == 12: pattern = f"{util.TIMESTAMP_PATTERN_YEAR}{util.TIMESTAMP_PATTERN_MONTH}{util.TIMESTAMP_PATTERN_DAY}T{util.TIMESTAMP_PATTERN_HOUR}"
                if len(value) == 13 or len(value) == 14: pattern = f"{util.TIMESTAMP_PATTERN_YEAR}{util.TIMESTAMP_PATTERN_MONTH}{util.TIMESTAMP_PATTERN_DAY}T{util.TIMESTAMP_PATTERN_HOUR}{util.TIMESTAMP_PATTERN_MINUTE}"
                if len(value) == 15 or len(value) == 16: pattern = f"{util.TIMESTAMP_PATTERN_YEAR}{util.TIMESTAMP_PATTERN_MONTH}{util.TIMESTAMP_PATTERN_DAY}T{util.TIMESTAMP_PATTERN_HOUR}{util.TIMESTAMP_PATTERN_MINUTE}{util.TIMESTAMP_PATTERN_SECOND}"
                if len(value) == 19 or len(value) == 20: pattern = f"{util.TIMESTAMP_PATTERN_YEAR}{util.TIMESTAMP_PATTERN_MONTH}{util.TIMESTAMP_PATTERN_DAY}T{util.TIMESTAMP_PATTERN_HOUR}{util.TIMESTAMP_PATTERN_MINUTE}{util.TIMESTAMP_PATTERN_SECOND}.{util.TIMESTAMP_PATTERN_MILLISECOND}"
            return re.match(f"^{pattern}{util.TIMESTAMP_PATTERN_ZONE}$", value).groupdict()
        date = datetime.datetime.now(tz=datetime.timezone.utc)
        if value == None:
            return convert(date, convert_to if convert_to else util.TIMESTAMP_OPTION_SECONDS)
        elif isinstance(value, datetime.datetime):
            return convert(value, convert_to)
        elif isinstance(value, int):
            date = None
            if len(str(value)) <= 10:
                date = datetime.datetime.fromtimestamp(value)
            if len(str(value)) == 13:
                date = datetime.datetime.fromtimestamp(value / 1000)
            return convert(date, convert_to)
        elif isinstance(value, str):
            if value.lower() == util.TIMESTAMP_OPTION_MILLISECONDS or value.lower() == util.TIMESTAMP_OPTION_OBJECT or value.lower() == util.TIMESTAMP_OPTION_SECONDS or value.lower() == util.TIMESTAMP_OPTION_STRING:
                return convert(date, value)
            elif bool(getString(value)):
                groups = getString(value)
                year = int(groups["year"])
                month = int(groups["month"]) if "month" in groups else 1
                day = int(groups["day"]) if "day" in groups else 1
                hour = int(groups["hour"]) if "hour" in groups else 0
                minute = int(groups["minute"]) if "minute" in groups else 0
                second = int(groups["second"]) if "second" in groups else 0
                microsecond = int(groups["millisecond"]) * 1000 if "millisecond" in groups else 0
                zone = groups["zone"] if "zone" in groups and groups['zone'] else 'Z'
                zone_utc_offset = util.TIMEZONE_DESIGNATION_OFFSETS[zone]
                timezone = datetime.timezone(datetime.timedelta(hours=zone_utc_offset))
                date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second, microsecond=microsecond, tzinfo=timezone)
                date = date.astimezone(datetime.timezone.utc)
                return convert(date, convert_to)
    def timestamp_calculator_addition(timestampStart: datetime.datetime|int|str = None, years: int = 0, days: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0) -> datetime.datetime:
        timestampStart = util.timestamp(timestampStart, util.TIMESTAMP_OPTION_SECONDS)
        duration = 0
        duration = duration+(years*365*24*60*60)
        duration = duration+(days*24*60*60)
        duration = duration+(hours*60*60)
        duration = duration+(minutes*60)
        duration = duration+(seconds)
        timestampEnd = timestampStart + duration
        timestampEnd = util.timestamp(timestampEnd, util.TIMESTAMP_OPTION_OBJECT)
        return timestampEnd
    def timestamp_calculator_difference(timestamp1: datetime.datetime|int|str, timestamp2: datetime.datetime|int|str = None) -> dict:
        timestamp1 = util.timestamp(timestamp1, util.TIMESTAMP_OPTION_SECONDS)
        timestamp2 = util.timestamp(timestamp2, util.TIMESTAMP_OPTION_SECONDS)
        difference = abs(timestamp2 - timestamp1)
        years   = difference//(365*24*60*60)
        days    = (difference//(24*60*60))-((years*365))
        hours   = (difference//(60*60))-((years*365*24)+(days*24))
        minutes = (difference//(60))-((days*24*60)+(hours*60))
        seconds = (difference)-((days*24*60*60)+(hours*60*60)+(minutes*60))
        timestamp_difference = util.timestamp(difference, util.TIMESTAMP_OPTION_STRING)
        return {
            'years': years,
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds,
        }
    def timestamp_date(timestamp: datetime.datetime|int|str = None) -> str:
        timestamp = util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT)
        year = f"{timestamp.year}"
        month = f"{timestamp.month}".rjust(2, '0')
        day = f"{timestamp.day}".rjust(2, '0')
        return f"{year}-{month}-{day}"
    def timestamp_day(timestamp: datetime.datetime|int|str = None) -> str:
        timestamp = util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT)
        return f"{timestamp.day}".ljust(2, '0')
    def timestamp_difference(timestamp1: datetime.datetime|int|str, timestamp2: datetime.datetime|int|str = None, short: bool = True) -> str:
        timestamp1 = util.timestamp(timestamp1, util.TIMESTAMP_OPTION_SECONDS)
        timestamp2 = util.timestamp(util.TIMESTAMP_OPTION_SECONDS) if timestamp2 == None else util.timestamp(timestamp2, util.TIMESTAMP_OPTION_SECONDS)
        difference = abs(timestamp2 - timestamp1)
        if difference == 0: return 'Now'
        if difference <= 1: return '1sec' if short else '1 second'
        if difference <= 2: return '2sec' if short else '2 seconds'
        if difference <= 3: return '3sec' if short else '3 seconds'
        if difference <= 4: return '4sec' if short else '4 seconds'
        if difference <= 5: return '5sec' if short else '5 seconds'
        if difference <= 10: return '10sec' if short else '10 seconds'
        if difference <= 20: return '20sec' if short else '20 seconds'
        if difference <= 30: return '30sec' if short else '30 seconds'
        if difference <= 60: return '1min' if short else '1 minute'
        if difference <= 120: return '2min' if short else '2 minutes'
        if difference <= 180: return '3min' if short else '3 minutes'
        if difference <= 240: return '4min' if short else '4 minutes'
        if difference <= 300: return '5min' if short else '5 minutes'
        if difference <= 600: return '10min' if short else '10 minutes'
        if difference <= 1200: return '20min' if short else '20 minutes'
        if difference <= 1800: return '30min' if short else '30 minutes'
        if difference <= 3600: return '1h' if short else '1 hour'
        if difference <= 7200: return '2h' if short else '2 hours'
        if difference <= 10800: return '3h' if short else '3 hours'
        if difference <= 14400: return '4h' if short else '4 hours'
        if difference <= 18000: return '5h' if short else '5 hours'
        if difference <= 21600: return '6h' if short else '6 hours'
        if difference <= 43200: return '12h' if short else '12 hours'
        if difference <= 86400: return '1d' if short else '1 day'
        if difference <= 172800: return '2d' if short else '2 days'
        if difference <= 259200: return '3d' if short else '3 days'
        if difference <= 345600: return '4d' if short else '4 days'
        if difference <= 432000: return '5d' if short else '5 days'
        if difference <= 864000: return '10d' if short else '10 days'
        if difference <= 1728000: return '20d' if short else '20 days'
        if difference <= 2592000: return '1mo' if short else '1 month' # 30 days
        if difference <= 5184000: return '2mo' if short else '2 months'
        if difference <= 7776000: return '3mo' if short else '3 months'
        if difference <= 10368000: return '4mo' if short else '4 months'
        if difference <= 12960000: return '5mo' if short else '5 months'
        if difference <= 15552000: return '6mo' if short else '6 months'
        if difference <= 31536000: return '1yr' if short else '1 year'
        if difference <= 63072000: return '2yr' if short else '2 years'
        if difference <= 94608000: return '3yr' if short else '3 years'
        if difference <= 126144000: return '4yr' if short else '4 years'
        if difference <= 157680000: return '5yr' if short else '5 years'
        if difference <= 315360000: return '10yr' if short else '10 years'
    def timestamp_hour(timestamp: datetime.datetime|int|str = None) -> str:
        timestamp = util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT)
        return f"{timestamp.hour}".rjust(2, '0')
    def timestamp_minute(timestamp: datetime.datetime|int|str = None) -> str:
        timestamp = util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT)
        return f"{timestamp.minute}".rjust(2, '0')
    def timestamp_month(timestamp: datetime.datetime|int|str = None, short: bool = False) -> str:
        timestamp = util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT)
        return timestamp.strftime("%b") if short else timestamp.strftime("%B")
    def timestamp_quarter(timestamp: datetime.datetime|int|str = None, short: bool = False) -> str:
        timestamp = util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT)
        quarter = math.ceil((timestamp.month) / 3)
        return f"Q{quarter}" if short else util.TIME_QUARTERS[quarter-1]
    def timestamp_second(timestamp: datetime.datetime|int|str = None) -> str:
        timestamp = util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT)
        return f"{timestamp.minute}".rjust(2, '0')
    def timestamp_time(timestamp: datetime.datetime|int|str = None, short: bool = False) -> str:
        timestamp = util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT)
        hour = f"{timestamp.hour}".rjust(2, '0')
        minute = f"{timestamp.minute}".rjust(2, '0')
        second = f"{timestamp.second}".rjust(2, '0')
        millisecond = f"{timestamp.microsecond / 1000:.0f}".rjust(3, '0')
        # TODO: regarding millisecond == 1000, increase second by one
        if millisecond == '1000': millisecond = '999'
        return f"{hour}:{minute}:{second}" if short else f"{hour}:{minute}:{second}.{millisecond}"
    def timestamp_to_zone(timestamp: datetime.datetime|int|str, zone: str) -> datetime.datetime:
        timestamp: datetime.datetime = util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT)
        zone_utc_offset = util.TIMEZONE_DESIGNATION_OFFSETS[zone]
        timezone = datetime.timezone(datetime.timedelta(hours=zone_utc_offset))
        return timestamp.astimezone(timezone)
    def timestamp_weekday(timestamp: datetime.datetime|int|str = None, short: bool = False) -> str:
        timestamp = util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT)
        weekday = util.TIME_DAYS_OF_WEEK[(timestamp.weekday()+1)%7]
        return weekday[0:3] if short else weekday
    def timestamp_year(timestamp: datetime.datetime|int|str = None) -> str:
        timestamp = util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT)
        return f"{timestamp.year}"
    def title(string: str) -> str:
        lowers = [
            'a', 'at',
            'be',
            'for',
            'in',
            'of',
            'nor',
        ]
        uppers = [
            'arcnet', 'arp', 'atm',
            'ciaddr', 'chaddr',
            'dhcp', 'drarp',
            'giaddr',
            'hdlc',
            'icmp', 'ieee', 'ip', 'id',
            'mac', 
            'ok',
            'rarp', 'rfc',
            'siaddr', 'sha', 'spa',
            'tha', 'tpa',
            'udp',
            'yiaddr'
        ]
        specials = [
            'ICMPv6', 'InARP', 'IPv4', 'IPv6'
        ]
        def convert(string: str) -> str:
            if string == '': return ''
            if string in lowers: return string
            if string in uppers: return string.upper()
            for special in specials:
                if special.lower() == string:
                    return special
            return string.capitalize()
        return ' '.join([convert(substring.lower()) for substring in string.split('_')])
    
    # u
    def uri_encode(object: dict) -> str:
        uriString = ''
        return uriString
    def uri_decode(relative: str, absolute: str = None):
        # example: http://username:password@hostname:9090/path?arg=value#anchor
        # relative path: relative-part [ ? query ] [ # fragment ] (cannot begin with '/')
        # absolute path: scheme ":" hierarchal-part [ "?" query ]
        uriObject = {
            'scheme': None,
            'username': None,
            'password': None,
            'authority': None,
            'host': None,
            'port': None,
            'path': None,
            'query': None,
            'fragment': None,
        }
        def getFirstIndex(string: str, characters: list[str]) -> int|None:
            # get index of each character in string
            indexes = [(string.find(character)) for character in characters]
            # filter numbers less than 0
            indexes = [(index) for index in indexes if index > 0]
            # sort ascending
            indexes.sort(reverse=False)
            # return first number or null
            return None if len(indexes) == 0 else indexes[0]
        # build target uri
        target = None
        if absolute != None:
            # absolute must end with '/' and relative cannot start with '/'
            target = absolute + ('' if absolute[-1] == '/' else '/') + (relative[1:] if relative[0] == '/' else relative)
        else:
            target = relative

        target_partial = target
        if '://' in target:
            uriObject['scheme'] = target[:target.index('://')]
            target_partial = target[target.index('://')+3:]
        if '@' in target:
            string = target_partial[:target_partial.index('@')]
            uriObject['username'], uriObject['password'] = string.split(':')
            target_partial = target_partial[target_partial.index('@')+1:]
        index = getFirstIndex(target_partial, ['/', '?', '#'])
        if index == None:
            uriObject['authority'] = target_partial
            target_partial = ''
        else:
            uriObject['authority'] = target_partial[:index]
            target_partial = target_partial[index:]
        if ':' in uriObject['authority']:
            uriObject['host'] = uriObject['authority'][:uriObject['authority'].index(':')]
            uriObject['port'] = uriObject['authority'][uriObject['authority'].index(':')+1:]
        else:
            uriObject['host'] = uriObject['authority']
        if len(target_partial) > 0 and '/' == target_partial[0]:
            index = getFirstIndex(target_partial, ['?', '#'])
            if index == None:
                uriObject['path'] = target_partial
                target_partial = ''
            else:
                uriObject['path'] = target_partial[:index]
                target_partial = target_partial[index:]
        else:
            uriObject['path'] = '/'
        if len(target_partial) > 0 and '?' == target_partial[0]:
            target_partial = target_partial[1:]
            index = getFirstIndex(target_partial, ['#'])
            if index == None:
                uriObject['query'] = target_partial
                target_partial = ''
            else:
                uriObject['query'] = target_partial[:index]
                target_partial = target_partial[index:]
        else:
            pass
        if len(target_partial) > 0 and '#' == target_partial[0]:
            uriObject['fragment'] = target_partial[1:]
        else:
            pass
        return uriObject
    def uri_query_encode(object: dict) -> str:
        queries = [(f"{queryKey}={queryValue}") for queryKey, queryValue in object.items()]
        return '&'.join(queries)
    def uri_query_decode(string: str) -> str:
        query = {}
        if not '=' in string: return query
        string = string[string.index('?')+1:] if '?' in string else string
        for pair in string.split('&'):
            queryKey, queryValue = pair.split('=', 1)
            query[queryKey] = queryValue
        return query
    # v
    def volume(x: float, y: float, z: float) -> float:
        return x * y * z
    # w

    # x

    # y

    # z

    def _dict(value) -> dict:
        return value
    def _int(value) -> int:
        return value
    def _list(value) -> list:
        return value
    def _str(value) -> str:
        return value

    # ascii functions
    # default bits per character (size) = 8
    def _dataT_(data, datatype: str):
        types = 'bin byt cha dec hex oct str'.split(' ')
        for type in types:
            if type == datatype: continue
            method = F"{datatype}2{type}"
            print(method, getattr(globals()['util'], method)(data))
    # binary
    def __len__(data: str, length: int):
        while True:
            if len(data) % length == 0:
                break
            data = '0' + data
        return data
    def bin2byt(bin: str) -> bytes:
        if len(bin) == 0: return bytes()
        length = math.ceil(len(bin)/8)
        return util.bin2dec(bin).to_bytes(length, 'big')
    def bin2cha(bin: str) -> str:
        return util.dec2cha(util.bin2dec(bin))
    def bin2dec(bin: str) -> int:
        if len(bin) == 0: return 0
        return int(bin, 2)
    def bin2hex(bin: str) -> str:
        bin = util.__len__(bin, 4)
        hex = ''
        for i in range(0, len(bin), 4):
            hex += util.dec2hex(util.bin2dec(bin[i:i+4]))
        return hex
    def bin2oct(bin: str) -> str:
        return util.dec2oct(util.bin2dec(bin))
    def bin2str(bin: str, size: int = 8) -> str: # 8 bpc
        bin = util.__len__(bin, size)
        str = ''
        for i in range(0, len(bin), size):
            str += util.dec2cha(util.bin2dec(bin[i:i+size]))
        return str
    def bin2bol(bin: str) -> bool:
        return bin == '1'
    def bin2decs(bin: str, size: int = 8) -> list:
        bin = util.__len__(bin, size)
        decs = []
        for i in range(0, len(bin), size):
            decs.append(util.bin2dec(bin[i:i+size]))
        return decs
    def bin2hexs(bin: str) -> str:
        return '0x' + util.bin2hex(bin).upper()
    # bytes
    def byt2bin(byt: bytes) -> str:
        bin = ''
        for dec in byt:
            bin += util.dec2bin(dec, 8)
        return bin
    def byt2dec(byt: bytes) -> int:
        return util.bin2dec(util.byt2bin(byt))
    def byt2cha(byt: bytes) -> str:
        return util.bin2cha(util.byt2bin(byt))
    def byt2hex(byt: bytes) -> str:
        return bytes.hex(byt)
    def byt2oct(byt: bytes) -> str:
        return util.bin2oct(util.byt2bin(byt))
    def byt2str(byt: bytes, size: int = 8) -> str: # 8 bpc
        bin = util.byt2bin(byt)
        bin = util.__len__(bin, size)
        str = ''
        for i in range(0, len(bin), size):
            str += util.bin2cha(bin[i:i+size])
        return str
    # character
    def cha2bin(cha: str, len = None) -> str:
        return util.dec2bin(util.cha2dec(cha), len)
    def cha2byt(cha: str) -> str:
        return util.dec2byt(util.cha2dec(cha))
    def cha2dec(cha: str) -> str:
        return ord(cha)
    def cha2hex(cha: str) -> str:
        return util.dec2hex(util.cha2dec(cha))
    def cha2oct(cha: str) -> str:
        return util.dec2oct(util.cha2dec(cha))
    def cha2str(cha: str, size: int = 8) -> str: # 8 bpc
        return util.bin2str(util.cha2bin(cha), size)
    # decimal
    def dec2bin(dec: int, len: int = None) -> str:
        if len == None: return format(dec, 'b')
        else: return format(int(dec), '0' + str(int(len)) + 'b')
    def dec2byt(dec: int) -> bytes:
        return util.bin2byt(util.dec2bin(dec))
    def dec2cha(dec: int) -> str:
        return chr(dec)
    def dec2hex(dec: int, len: int = None) -> str:
        if len == None: return format(dec, 'x')
        else: return format(int(dec), '0' + str(int(len)) + 'x')
    def dec2oct(dec: int, len: int = None) -> str:
        if len == None: return format(dec, 'o')
        else: return format(int(dec), '0' + str(int(len)) + 'o')
    def dec2str(dec: int, size: int = 8) -> str: # 8 bpc
        return util.bin2str(util.dec2bin(dec), size)
    def decs2bin(decs: list, len: int = None) -> str: # 8 size
        bin = ''
        for dec in decs:
            bin += util.dec2bin(dec, len)
        return bin
    # hexadecimal
    def hex2bin(hex: str) -> str:
        return util.dec2bin(util.hex2dec(hex), len(hex) * 4)
    def hex2byt(hex: str) -> bytes:
        return util.bin2byt(util.hex2bin(hex))
    def hex2cha(hex: str) -> str:
        return util.dec2cha(util.hex2dec(hex))
    def hex2dec(hex: str) -> int:
        return int(hex, 16)
    def hex2oct(hex: str) -> str:
        return util.dec2oct(util.hex2dec(hex))
    def hex2str(hex: str, size: int = 8) -> str: # 8 bpc
        return util.bin2str(util.hex2bin(hex), size)
    # octal
    def oct2bin(oct: str, len = None) -> str:
        return util.dec2bin(util.oct2dec(oct), len)
    def oct2byt(oct: str) -> bytes:
        return util.bin2byt(util.oct2bin(oct))
    def oct2cha(oct: str) -> str:
        return util.dec2cha(util.oct2dec(oct))
    def oct2dec(oct: str) -> int:
        return int(oct, 8)
    def oct2hex(oct: str) -> str:
        return util.dec2hex(util.oct2dec(oct))
    def oct2str(oct: str, size: int = 8) -> str: # 8 bpc
        return util.bin2str(util.oct2bin(oct), size)
    # string
    def str2bin(str: str, size: int = 8) -> str: # 8 bpc
        bin = ''
        for dec in util.str2decs(str):
            bin += util.dec2bin(dec, size)
        return bin
    def str2byt(str: str, size: int = 8) -> bytes: # 8 bpc
        return util.bin2byt(util.str2bin(str, size))
    def str2cha(str: str, size: int = 8) -> str: # 8 bpc
        return util.dec2cha(util.str2dec(str, size))
    def str2dec(str: str, size: int = 8) -> int: # 8 bpc
        return util.bin2dec(util.str2bin(str, size))
    def str2hex(str: str, size: int = 8): # 8 bpc
        # return str.encode('utf-8').hex()
        hex = ''
        for dec in util.str2decs(str):
            hex += util.dec2hex(dec, size/4)
        return hex
    def str2oct(str: str, size: int = 8) -> str: # 8 bpc
        return util.dec2oct(util.str2dec(str, size))
    def str2decs(str: str) -> list[int]:
        decs = []
        for cha in str:
            decs.append(util.cha2dec(cha))
        return decs

class array:
    def __init__(self, *values):
        self.data: list = []
        for value in values:
            if isinstance(value, array|list|tuple):
                self.data.extend(value)
            else:
                self.data.append(value)
    def __add__(self, other):
        return self.__class__(self.data, other)
    def __contains__(self, item):
        return item in self.data
    """def __copy__(self):
        inst = self.__class__.__new__(self.__class__)
        inst.__dict__.update(self.__dict__)
        inst.__dict__["data"] = self.__dict__["data"][:]
        return inst"""
    def __delitem__(self, index):
        del self.data[index]
    def __eq__(self, other):
        return self.data == self.__cast(other)
    def __ge__(self, other):
        return self.data >= self.__cast(other)
    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.__class__(self.data[index])
        else:
            return self.data[index]
    def __gt__(self, other):
        return self.data > self.__cast(other)
    def __iadd__(self, other):
        if isinstance(other, array):
            self.data += other.data
        elif isinstance(other, list):
            self.data += other
        elif isinstance(other, tuple):
            self.data += list(other)
        else:
            self.data += [other]
        return self
    def __imul__(self, other):
        self.data *= other
        return self
    def __le__(self, other):
        return self.data <= self.__cast(other)
    def __len__(self):
        return len(self.data)
    def __lt__(self, other):
        return self.data < self.__cast(other)
    def __mul__(self, other):
        return self.__class__(self.data * other)
    def __radd__(self, other):
        return self.__class__(other, self.data)
    def __repr__(self) -> str:
        return f'{repr(self.data)}'
    def __setitem__(self, index, value):
        self.data[index] = value
    __rmul__ = __mul__
    def __cast(self, other):
        return other.data if isinstance(other, array) else other
    
    def fromdata(data: bytes|dict|list|str):
        nArray = array()
        if data == None:
            return nArray
        if util.istype(data, 'array'):
            nArray.append(*data)
        elif util.istype(data, 'bytes-array'):
            nArray.append(*util.json_decode(util.byt2str(data)))
        elif util.istype(data, 'bytes-object'):
            nArray = array.fromobject(util.json_decode(util.byt2str(data)))
        elif util.istype(data, 'object'):
            nArray = array.fromobject(data)
        elif util.istype(data, 'string-array'):
            nArray.append(*util.json_decode(data))
        elif util.istype(data, 'string-object'):
            nArray = array.fromobject(util.json_decode(data))
        elif util.istype(data, 'string'):
            nArray = array.fromstring(data)
        else:
            util.system_log(__file__, inspect.currentframe().f_lineno, f"TypeError: variable-name=data variable-value={data} variable-type={type(data)} type=array|bytes-array|bytes-object|object|string-array|string-object|string")
        return nArray
    def fromobject(data: dict, delimiter: str = ': '):
        return array([(f"{key}{delimiter}{value}") for key, value in data.items()])
    def fromstring(data: str):
        nArray = array()
        # data = 'value'
        if not ',' in data and not ':' in data:
            for substring in data.strip(' ,').split(','):
                nArray.append(substring)
        # data = 'value,value,value...'
        if ',' in data and not ':' in data:
            for substring in data.strip(' ,').split(','):
                nArray.append(substring)
        # data = 'value:value:value...'
        if not ',' in data and ':' in data:
            for substring in data.strip(' :').split(':'):
                nArray.append(substring)
        # data = 'value,value:value,value:value:value,value...'
        if ',' in data and ':' in data:
            for substring in data.strip(' ,').split(','):
                nArray.append(array(substring.strip(' :').split(':')))
        return nArray
    def generate(*args):
        size = len(args)
        start = 0 if size == 1 else args[0]
        stop = args[0] if size == 1 else args[1]
        step = args[2] if size == 3 else (1 if start < stop else -1)
        for i in range(start, stop, step):
            yield i

    # def append(self, value): self.data.append(value)
    def clear(self):
        self.data.clear()
    def copy(self):
        return self.__class__(self)
    def count(self, value):
        return self.data.count(value)
    def extend(self, other):
        if isinstance(other, array):
            self.data.extend(other.data)
        else:
            self.data.extend(other)
    # def index(self, value, *args): self.data.index(value, *args)
    def insert(self, index, value):
        self.data.insert(index, value)
    def pop(self, index: int = -1):
        return self.data.pop(index)
    # def remove(self, value): self.data.remove(value)
    def reverse(self):
        self.data.reverse()
    def sort(self, **kwargs):
        self.data.sort(**kwargs)
    
    def any(self) -> bool:
        return any(self)
    def append(self, *values):
        for value in values:
            self.data.append(value)
        return self
    def clone(self):
        if util.importModule('copy'): import copy
        return copy.deepcopy(self)
    def dump(self):
        return util.dump(self.data)
    def empty(self) -> bool:
        return len(self) == 0
    def every(self, callback) -> bool:
        arguments = len(str(inspect.signature(callback)).strip('()').split(', '))
        for index, value in enumerate(self):
            if arguments == 1:
                if not callback(value): return False
            if arguments == 2:
                if not callback(value, index): return False
            if arguments == 3:
                if not callback(value, index, self): return False
        return True
    def excludes(self, *values) -> bool:
        for value in values:
            if value in self:
                return False
        return True
    def find(self, callback):
        arguments = len(str(inspect.signature(callback)).strip('()').split(', '))
        for index, value in enumerate(self):
            if arguments == 1:
                if callback(value): return value
            if arguments == 2:
                if callback(value, index): return value
            if arguments == 3:
                if callback(value, index, self): return value
        return None
    def findindex(self, callback) -> int|None:
        arguments = len(str(inspect.signature(callback)).strip('()').split(', '))
        for index, value in enumerate(self):
            if arguments == 1:
                if callback(value): return index
            if arguments == 2:
                if callback(value, index): return index
            if arguments == 3:
                if callback(value, index, self): return index
        return None
    def findvalue(self, callback):
        return self.find(callback)
    def filter(self, callback):
        arguments = len(str(inspect.signature(callback)).strip('()').split(', '))
        nArray = array()
        for index, value in enumerate(self):
            if arguments == 1:
                if callback(value): nArray.append(value)
            if arguments == 2:
                if callback(value, index): nArray.append(value)
            if arguments == 3:
                if callback(value, index, self): nArray.append(value)
        return nArray
    def fill(self, value):
        for index in range(len(self)):
            self[index] = value
        return self
    def get(self, index: int, defaultvalue = None):
        if index < 0:
            value = self[index + len(self)]
        elif index >= len(self):
            value = None
        else:
            value = self[index]
        return defaultvalue if value == None else value
    def getFirst(self):
        return self.get(0)
    def getLast(self):
        return self.get(-1)
    def hash(self, mode: str = util.HASH_MD5) -> str:
        data = util.json_encode(self.data)
        if mode == util.HASH_MD5:
            return util.hash_md5(data)
        elif mode == util.HASH_SHA1:
            return util.hash_sha1(data)
        elif mode == util.HASH_SHA224:
            return util.hash_sha224(data)
        elif mode == util.HASH_SHA256:
            return util.hash_sha256(data)
        elif mode == util.HASH_SHA384:
            return util.hash_sha384(data)
        elif mode == util.HASH_SHA512:
            return util.hash_sha512(data)
        else:
            util.system_log(__file__, inspect.currentframe().f_lineno, f"ValueError: variable-name=mode variable-value={mode}")
            return ''
    def includes(self, *values) -> bool:
        for value in values:
            if not value in self:
                return False
        return True
    def index(self, value, start: int = 0) -> int:
        for index in range(start, len(self)):
            if self[index] == value: return index
        return -1
    def join(self, delimiter: str = '') -> str:
        return delimiter.join(self.data)
    def json(self) -> str:
        return util.json_encode(self.data)
    def map(self, callback):
        arguments = len(str(inspect.signature(callback)).strip('()').split(', '))
        nArray = array()
        for index, oldValue in enumerate(self):
            if arguments == 1:
                newValue = callback(oldValue)
            if arguments == 2:
                newValue = callback(oldValue, index)
            if arguments == 3:
                newValue = callback(oldValue, index, self)
            nArray.append(oldValue if newValue == None else newValue)
        return nArray
    def product(self) -> int:
        if len(self) == 0:
            return 0
        value = 1
        for number in self:
            value *= number
        return value
    def push(self, *values):
        for value in values:
            self.append(value)
        return self
    def random(self, *index):
        nArray = self.slice(*index)
        return util.random(nArray.data)
    def remove(self, *values): 
        return self.removevalues(*values)
    def removeduplicates(self):
        def filter(item, index):
            return self.index(item) == index
        nArray = self.filter(filter)
        self.clear()
        self.append(*nArray)
    def removeindexes(self, *values):
        values = [value for value in values]
        positiveIndexes = [value for value in values if value >= 0]
        positiveIndexes.sort(reverse=True)
        negativeIndexes = [value for value in values if value < 0]
        negativeIndexes.sort(reverse=False)
        indexes = [*positiveIndexes, *negativeIndexes]
        for index in indexes:
            self.pop(index)
        return self
    def removevalues(self, *values):
        for value in values:
            index = self.index(value)
            if not index == -1:
                self.pop(index)
        return self
    def replaceindex(self, index: int, value):
        self[index] = value
        return self
    def replacevalue(self, oldvalue, newvalue):
        index = self.index(oldvalue)
        if not index == None:
            self[index] = newvalue
        return self
    def resize(self, newSize: int):
        oldSize = self.size()
        if oldSize > newSize:
            self.splice(newSize, oldSize - newSize)
        if oldSize <  newSize:
            for i in range(newSize - oldSize):
                self.append(None)
        return self
    def set(self, index, value):
        self.data.insert(index, value)
        return self
    def shuffle(self):
        nArray = array()
        while len(self) > 0:
            index = util.random(len(self)-1)
            nArray.append(self[index])
            self.pop(index)
        self.data = nArray.data
        return self
    def size(self) -> int:
        return len(self)
    def slice(self, *args):
        start = (args[0] if args[0] >= 0 else args[0] + len(self)) if len(args) > 0 else 0
        stop = (args[1] if args[1] >= 0 else args[1] + len(self)) if len(args) > 1 else len(self)
        nArray = array()
        for i in range(start, stop):
            if i >= len(self): continue
            nArray.append(self[i])
        return nArray
    def some(self, callback) -> bool:
        arguments = len(str(inspect.signature(callback)).strip('()').split(', '))
        for index, value in enumerate(self):
            if arguments == 1:
                if callback(value): return True
            if arguments == 2:
                if callback(value, index): return True
            if arguments == 3:
                if callback(value, index, self): return True
        return False
    def splice(self, index, rcount, *values):
        for i in range(rcount):
            self.pop(index)
        for index_, value in enumerate(values):
            self.insert(index_ + index, value)
        return self
    def sum(self) -> int:
        value = 0
        for value_ in self:
            value += value_
        return value

    def add(self, *args): return self.push(*args)
    def clr(self, *args): return self.clear(*args)
    def cnt(self, *args): return self.count(*args)
    def cpy(self, *args): return self.copy(*args)
    def exc(self, *args): return self.excludes(*args)
    def fnd(self, *args): return self.findindex(*args)
    def fndi(self, *args): return self.find(*args)
    def fndv(self, *args): return self.findvalue(*args)
    def flt(self, *args): return self.filter(*args)
    def idx(self, *args): return self.index(*args)
    def inc(self, *args): return self.includes(*args)
    def ins(self, *args): return self.insert(*args)
    def ran(self, *args): return self.random(*args)
    def rem(self, *args): return self.remove(*args)
    def remi(self, *args): return self.removeindexes(*args)
    def remv(self, *args): return self.removevalues(*args)
    def rev(self, *args): return self.reverse(*args)
    def shf(self, *args): return self.shuffle(*args)
    def slc(self, *args): return self.slice(*args)
    def spl(self, *args): return self.splice(*args)
    def str(self, *args): return self.__repr__(*args)
    def ___(self, *args): return self.___(*args)

class object:
    def __init__(self, *values):
        self.data: dict = {}
        for value in values:
            if isinstance(value, object):
                self.data.update(dict((key, val) for key, val in value.data.items()))
            elif isinstance(value, dict):
                self.data.update(dict((key, val) for key, val in value.items()))
            else:
                self.data.update(object.fromdata(value))
    def __add__(self, other):
        return self.__class__(self.data, other)
    def __contains__(self, item):
        return item in self.data
    def __delitem__(self, key):
        del self.data[key]
    def __eq__(self, other):
        return self.data == self.__cast(other)
    def __getitem__(self, key):
        return self.data[key]
    def __iadd__(self, other):
        if isinstance(other, object):
            self.data.update(other.data)
        elif isinstance(other, dict):
            self.data.update(other)
        return self
    def __len__(self):
        return len(self.data)
    def __radd__(self, other):
        return self.__class__(other, self.data)
    def __repr__(self) -> str:
        return f'{repr(self.data)}'
    def __setitem__(self, key, value):
        self.data[key] = value
    def __cast(self, other):
        return other.data if isinstance(other, object) else other
    
    def fromdata(data: dict|bytes|list|str):
        nObject = object()
        if data == None:
            return nObject
        if util.istype(data, 'array'):
            nObject = object.fromarray(data)
        elif util.istype(data, 'bytes-array'):
            nObject = object.fromarray(util.json_decode(util.byt2str(data)))
        elif util.istype(data, 'bytes-object'):
            nObject.update(util.json_decode(util.byt2str(data)))
        elif util.istype(data, 'object'):
            nObject.update(data)
        elif util.istype(data, 'string-object'):
            nObject.update(util.json_decode(data))
        elif util.istype(data, 'string'):
            nObject = object.fromstring(data)
        else:
            util.system_log(__file__, inspect.currentframe().f_lineno, f"TypeError: variable-name=data variable-value={data} variable-type={type(data)} type=array|bytes-array|bytes-object|object|string-object|string")
        return nObject
    def fromarray(data: list|tuple):
        nObject = object()
        # data = [['key','value'],['key','value']...]
        if not False in [(util.istype(item, 'array') and len(item) == 2) for item in data]:
            for index in range(0, len(data), 1):
                nObject[data[index][0]] = data[index][1]
        # data = ['key','value','key','value'...]
        elif (not False in [(util.istype(item, 'number|string')) for item in data]) and len(data) % 2 == 0:
            for index in range(0, len(data), 2):
                nObject[data[index]] = data[index + 1]
        else:
            util.system_log(__file__, inspect.currentframe().f_lineno, f"TypeError: variable-name=data variable-value={data} variable-type={type(data)} type=array")
        return nObject
    def fromkeys(keys: list, value = None):
        return object(dict.fromkeys(keys, value))
    def fromstring(data: str, delimiterPairs: str = ',', delimiterPair: str = ':'):
        return object(dict(substring.strip(f" {delimiterPair}").split(delimiterPair) for substring in data.strip(f" {delimiterPairs}").split(delimiterPairs)))
    
    def clear(self):
        self.data.clear()
    def copy(self):
        return object(self.data.copy())
    def get(self, key, defaultvalue = None):
        return self.data.get(key, defaultvalue)
    def items(self):
        return self.data.items()
    def keys(self) -> array:
        return array(*self.data.keys())
    def pop(self, key, defaultvalue = None):
        return self.data.pop(key, defaultvalue)
    def popitem(self):
        return self.data.popitem()
    def setdefault(self, key, defaultvalue = None):
        return self.data.setdefault(key, defaultvalue)
    def update(self, iterable):
        self.data.update(iterable)
    def values(self) -> list:
        return [*self.data.values()]
    
    def append(self, key, value):
        self.data[key] = value
        return self
    def clone(self):
        return util.clone(self)
    def count(self) -> int:
        return len(self)
    def dump(self) -> str:
        return util.dump(self.data)
    def empty(self) -> bool:
        return len(self.keys()) == 0
    def excludes(self, *values) -> bool:
        return self.excludeskeys(*values)
    def excludeskeys(self, *values) -> bool:
        keys = self.keys()
        for value in values:
            if value in keys:
                return False
        return True
    def excludesvalues(self, *values) -> bool:
        values_ = self.values()
        for value in values:
            if value in values_:
                return False
        return True
    def hash(self, mode: str = util.HASH_MD5) -> str:
        data = util.json_encode(self.data)
        if mode == util.HASH_MD5:
            return util.hash_md5(data)
        elif mode == util.HASH_SHA1:
            return util.hash_sha1(data)
        elif mode == util.HASH_SHA224:
            return util.hash_sha224(data)
        elif mode == util.HASH_SHA256:
            return util.hash_sha256(data)
        elif mode == util.HASH_SHA384:
            return util.hash_sha384(data)
        elif mode == util.HASH_SHA512:
            return util.hash_sha512(data)
        else:
            util.system_log(__file__, inspect.currentframe().f_lineno, f"ValueError: variable-name=mode variable-value={mode}")
            return ''
    def includes(self, *values: (int|str)) -> bool:
        return self.includeskeys(*values)
    def includeskeys(self, *values: (int|str)) -> bool:
        keys = self.keys()
        for value in values:
            if value not in keys:
                return False
        return True
    def includesvalues(self, *values) -> bool:
        values_ = self.values()
        for value in values:
            if value not in values_:
                return False
        return True
    def iskey(self, key: str) -> bool:
        return key in self.keys()
    def istype(self, key, datatype: str) -> bool:
        return util.istype(self.get(key), datatype)
    def isvalue(self, key: str, value) -> bool:
        return self.get(key) == value
    def isvaluein(self, key: str, value) -> bool:
        return value in self.get(key)
    def json(self) -> str:
        return util.json_encode(self.data)
    def lower(self):
        object_ = self.copy()
        for key, value in object_.items():
            if isinstance(key, str):
                del self[key]
                self[key.lower()] = value
        return self
    def order(self, *keys: (int|str)):
        cObject = self.copy()
        self.clear()
        for key in keys:
            if key in cObject:
                self[key] = cObject[key]
        return self
    def sort(self):
        keys = self.keys()
        keys.sort()
        for key in keys:
            value = self[key]
            del self[key]
            self[key] = value
        return self
    def remove(self, *values):
        return self.removekeys(*values)
    def removekeys(self, *values):
        for value in values:
            if value in self.keys():
                del self.data[value]
        return self
    def removevalues(self, *values):
        nObject = { }
        for key, value in self.items():
            if value not in values:
                nObject[key] = value
        self.data = nObject
        return self
    def replacekey(self, oldkey: int|str, newkey: int|str):
        if oldkey in self:
            value = self[oldkey]
            del self[oldkey]
            self[newkey] = value
        return self
    def replacevalue(self, value, newvalue):
        for key in self.keys():
            if self[key] == value:
                self[key] = newvalue
        return self
    def set(self, key: int|str, value):
        self.data[key] = value
        return self
    def size(self) -> int:
        return len(self)
    def toitems(self, dimensions: int = 1) -> array:
        nArray = array()
        if dimensions == 1:
            for key, value in self.items():
                nArray.append(key, value)
        if dimensions == 2:
            for key, value in self.items():
                nArray.append(array(key, value))
        return nArray
    def tostring(self, delimiterPairs: str = ', ', delimiterPair: str = ': ') -> str:
        nArray = array()
        for key, value in self.items():
            nArray.append(f"{key}{delimiterPair}{value}")
        return nArray.join(delimiterPairs)
    def upper(self):
        object_ = self.copy()
        for key, value in object_.items():
            if isinstance(key, str):
                del self[key]
                self[key.upper()] = value
        return self

    def clr(self, *args): return self.clear(*args)
    def cnt(self, *args): return self.count(*args)
    def cpy(self, *args): return self.copy(*args)
    def exc(self, *args): return self.excludes(*args)
    def exck(self, *args): return self.excludeskeys(*args)
    def excv(self, *args): return self.excludesvalues(*args)
    def inc(self, *args): return self.includes(*args)
    def inck(self, *args): return self.includeskeys(*args)
    def incv(self, *args): return self.includesvalues(*args)
    def key(self, *args): return self.keys(*args)
    def rem(self, *args): return self.remove(*args)
    def remk(self, *args): return self.removekeys(*args)
    def remv(self, *args): return self.removevalues(*args)
    def setd(self, *args): return self.setdefault(*args)
    def str(self, *args): return self.__repr__(*args)
    def upd(self, *args): return self.update(*args)
    def val(self, *args): return self.values(*args)
    def ___(self, *args): return self.___(*args)

# ___________________________________________________________________________________________________________________________________________________#

class app:
    def __init__(self):
        pass
    
    arguments_: object|dict[str, str] = object()
    configuration_: object|dict[str, int|str] = object()
    instance = None
    isConfigurationFile = True
    name: str
    variables_: object = object({
        # do not insert blank entries
    })
    executionTimerIdentifier: str = None
    executionTimerTimestamp: int = None
    executionTimerPerformance: dict[str, list]|object = object({

    })
    executionTimerEntries: dict[str, list]|object = object({

    })

    def main(path: str, arguments: list[str] = []) -> None:
        print(f"{app.getProcessIdentifier()}.{util.path_info(path, 'filename')}.{__name__}\n")
        # path: string = the path of client file, argument: __file__
        # arguments: string[] = list of values passed into client, argument: sys.argv[1:]
        # 
        app.variables_.update(util.variables)
        path = path.lower()
        app.variables('file', path)
        app.variables('name', util.path_info(path, 'filename'))
        app.variables('path', util.path_info(path, 'dirname'))
        app.getArguments(arguments)
        if os.path.isfile(f"{app.variables('path')}\\configuration.json"): 
            app.configuration_ = app.getConfiguration()
        # call entry point of program
        # main = getattr(globals()['Main'], 'main')
        # main()

    def arguments(key: str = None) -> str:
        if key == None:
            return app.arguments_
        if not app.arguments_.iskey(key): util.system_log(__file__, inspect.currentframe().f_lineno, f"KeyError: object=app.arguments key={key}")
        # automatic type conversion
        data = app.arguments_.get(key, None)
        data = util.string_conversion_decode(data)
        return data

    def configuration(key: str = None, value = None, write: bool = False) -> dict|list|object|str:
        if key == None:
            return app.configuration_
        elif value == None:
            if not app.configuration_.iskey(key): util.system_log(__file__, inspect.currentframe().f_lineno, f"KeyError: object=app.configuration key={key}")
            data = app.configuration_.get(key, None)
            data = util.string_conversion_decode(data)
            return data
        else:                
            value = util.string_conversion_encode(value)
            if app.configuration_.iskey(key):
                app.configuration_.set(key, value)
            else:
                util.system_log(__file__, inspect.currentframe().f_lineno, f"KeyError: object=app.configuration key={key}")
            if write: app.setConfiguration()
            return app.configuration(key)

    def confirm(message: str, onInvalidResponseMessage: str = 'invalid') -> bool:
        message = message if message[-2:] == '?: ' else f"{message}?: "
        while True:
            value = input(message)
            if not value == '': 
                if value.lower() in ['y', 'yes', '1']:
                    return True
                if value.lower() in ['n', 'no', '0']:
                    return False
            print(onInvalidResponseMessage)

    def copyToClipboard(text: str):
        import pyperclip
        try: pyperclip.copy(text)
        except pyperclip.PyperclipException as e: print(f"ClipboardCopyError: {e}")

    def _executionTimerStart(identifier: str = util.identifier()) -> None:
        app.executionTimerIdentifier = identifier
        app.executionTimerTimestamp = util.timestamp(util.TIMESTAMP_OPTION_MILLISECONDS)

    def _executionTimerEnd() -> None:
        milliseconds = util.timestamp(util.TIMESTAMP_OPTION_MILLISECONDS) - app.executionTimerTimestamp
        if app.executionTimerPerformance.iskey(app.executionTimerIdentifier):
            app.executionTimerPerformance.get(app.executionTimerIdentifier).append(milliseconds)
        else:
            app.executionTimerPerformance.set(app.executionTimerIdentifier, [milliseconds])
        average = int(util.statistics_mean(app.executionTimerPerformance.get(app.executionTimerIdentifier)))
        print(f"ExecutionTimer: identifier:{app.executionTimerIdentifier} milliseconds:{milliseconds:04d} average:{average:04d}")

    def executionTimerStart(identifier: str = util.identifier()) -> None:
        app.executionTimerEntries.set(identifier, util.timestamp(util.TIMESTAMP_OPTION_MILLISECONDS))

    def executionTimerEnd(identifier: str = None, log: bool = True) -> int:
        if not identifier:
            identifier = app.executionTimerEntries.keys().get(0)
        if not app.executionTimerEntries.iskey(identifier): return -1
        milliseconds = util.timestamp(util.TIMESTAMP_OPTION_MILLISECONDS) - app.executionTimerEntries.get(identifier)
        app.executionTimerEntries.pop(identifier)
        if app.executionTimerPerformance.iskey(identifier):
            app.executionTimerPerformance.get(identifier).append(milliseconds)
        else:
            app.executionTimerPerformance.set(identifier, [milliseconds])
        average = int(util.statistics_mean(app.executionTimerPerformance.get(identifier)))
        if log: print(f"ExecutionTimer: identifier:{identifier} milliseconds:{milliseconds:04d} average:{average:04d}")
        return milliseconds

    def exit() -> None:
        if util.importModule('sys'): import sys
        sys.exit(0)

    def getArguments(values: list[str]) -> object:
        keys = list(range(0, len(values)))
        for index, key in enumerate(keys):
            app.arguments_.set(key, values[index] if len(values) > index else None)
    
    def getConfiguration(path: str = '') -> object:
        # read application's configuration file
        data = object()
        if os.path.isfile(path):
            extension = util.path_info(path, 'extension')
            data: bytes = util.file_read(path)
            if extension == 'json':
                data = object.fromdata(data)
            if extension == 'txt':
                data = object.fromstring(data.decode(), ': ', '\r\n')
        elif os.path.isfile(f"{app.variables('path')}\\configuration.json"):
            data: bytes = util.file_read(f"{app.variables('path')}\\configuration.json")
            data = object.fromdata(data)
        elif os.path.isfile(f"{app.variables('path')}\\configuration.txt"):
            data: bytes = util.file_read(f"{app.variables('path')}\\configuration.txt")
            data = object.fromstring(data.decode(), ': ', '\r\n')
        else:
            util.system_log(__file__, inspect.currentframe().f_lineno, f"FileNotFoundError: path={app.variables('path')}\\configuration.json|txt")
        # find and replace configuration variable key with the variable value
        def setIfVariable(oldValue: str):
            if not isinstance(oldValue, str):
                return [False, oldValue]
            for variableKey, variableValue in app.variables_.items():
                if f"%{variableKey}%" in oldValue:
                    newValue = oldValue.replace(f'%{variableKey}%', variableValue)
                    return [True, newValue]
            return [False, oldValue]
        def iterate(cObject: dict|object):
            for key, value in cObject.items():
                updated, newValue = setIfVariable(value)
                if isinstance(value, dict|object):
                    iterate(value)
                elif updated:
                    cObject[key] = newValue
        assert isinstance(data, object)
        iterate(data)
        return data

    def getCurrentWorkingDirectory() -> str:
        return os.getcwd()

    def getDeviceMemory() -> int:
        return 0

    def getDeviceType() -> None:
        return

    def getGlobalVariables() -> dict[str]:
        return globals()
    
    def getInstance():
        return app.instance

    def getName() -> str:
        return app.variables('name')

    def getProcessIdentifier() -> int:
        return os.getpid()

    def isArgument(key: str) -> bool:
        return app.arguments_.iskey(key)
    
    def isArguments() -> bool:
        return any(app.arguments_.values())

    def isDeviceCharging() -> bool:
        return

    def isOnline(address: tuple[str, int] = ('8.8.8.8', 53)) -> bool:
        try:
            socket.setdefaulttimeout(1000)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP).connect(address)
            return True
        except:
            return False
        finally:
            socket.setdefaulttimeout(None)

    def open() -> None:
        pass

    def prompt(message: str, defaultValue: str = None, onVerification = None, onInvalidResponseMessage: str = 'invalid') -> tuple[str, bool]:
        # onVerification: function|string
        message = message if message[-2:] == ': ' else f"{message}: "
        # message = f"{message[:-2]} ({onVerification}): " if isinstance(onVerification, str) and onVerification.count('|') <= 5 else message
        message = message if defaultValue == None else f"{message[:-2]} ({defaultValue}): "
        while True:
            value = input(message)
            if not defaultValue == None and value.lower() in ['y', 'yes', '1', '']:
                return defaultValue, False
            else:
                if onVerification == None:
                    return value, not value == defaultValue
                else:
                    if isinstance(onVerification, str):
                        valid = False
                        verificationValues = [verificationValue for verificationValue in onVerification.strip(' ').strip('|').split('|')]
                        for verificationValue in verificationValues:
                            if verificationValue.startswith('{') and verificationValue.endswith('}'):
                                if util.istype(value, verificationValue.strip('{}')): 
                                    valid = True
                                    break
                            elif verificationValue == value: 
                                valid = True
                                break
                        if valid: 
                            return value, not value == defaultValue
                    if type(onVerification).__name__ == 'function':
                        if onVerification(value):
                            return value, not value == defaultValue
            print(onInvalidResponseMessage)

    def setArguments(keys: list[str]) -> object:
        for index, key in enumerate(keys):
            app.arguments_.set(key, app.arguments_.get(index, None))
            app.arguments_.pop(index)
    
    def setConfiguration(data: dict = None) -> None:
        data: object = object(app.configuration_) if data == None else object(data)
        # replace each configuration value containing a variable value with the variable's key
        def setIfVariable(oldValue: str):
            if not isinstance(oldValue, str):
                return [False, oldValue]
            for variableKey, variableValue in app.variables_.items():
                if variableValue in oldValue:
                    newValue = oldValue.replace(variableValue, f'%{variableKey}%')
                    return [True, newValue]
            return [False, oldValue]
        def iterate(cObject: dict|object):
            for key, value in cObject.items():
                updated, newValue = setIfVariable(value)
                if isinstance(value, dict|object):
                    iterate(value)
                elif updated:
                    cObject[key] = newValue
        iterate(data)
        # write configuration to file
        if os.path.isfile(f"{app.variables('path')}\\configuration.json"):
            util.file_write(f"{app.variables('path')}\\configuration.json", data)
        elif os.path.isfile(f"{app.variables('path')}\\configuration.txt"):
            data = '\r\n'.join((f"{key}: {value}") for key, value in data.items())
            util.file_write(f"{app.variables('path')}\\configuration.txt", data)

    def setInterval(milliseconds: int, callback, *args, **kwargs) -> threading.Timer:
        class Interval(threading.Thread):
            def __init__(self, milliseconds: int, function, args, kwargs):
                super().__init__()
                self.milliseconds: int = milliseconds
                self.function = function
                self.args: tuple = args
                self.kwargs: tuple = kwargs
                self.finished: threading.Event = threading.Event()
                self.start()
            def cancel(self):
                self.finished.set()
            def run(self):
                self.finished.wait(self.milliseconds / 1000)
                if not self.finished.is_set():
                    self.function(*self.args, **self.kwargs)
                    self.run()
        interval = Interval(milliseconds, callback, args, kwargs)
        return interval

    def setName(name: str) -> None:
        app.variables('name', name)

    def setTimeout(milliseconds: int, callback, *args, **kwargs) -> threading.Timer:
        timeout = threading.Timer(milliseconds / 1000, callback, args, kwargs)
        timeout.start()
        return timeout

    def simulateKey() -> None:
        pass

    def variables(key: str = None, value = None) -> None|object|str:
        if not key == None:
            if key[0] == '%' and key[-1] == '%':
                key = key[1:][:-1]
        if key == None:
            return app.variables_
        elif value == None:
            data = app.variables_.get(key, None)
            # automatic type conversion
            if util.istype(data, 'string-number'):
                return int(data)
            if util.istype(data, 'string-boolean'):
                return util.boolean(data)
            return data
        else:
            # automatic type conversion
            if util.istype(value, 'number'):
                value = str(value)
            app.variables_.set(key, value)
    
    def wait(milliseconds: int, callback) -> None:
        pass

    # data
    def clearData():
        pass
    def getData():
        pass
    def removeData():
        pass
    def setData():
        pass

class Logger(threading.Thread):
    def __init__(self, path: str = None):
        super().__init__()
        self.queue = Queue()
        self.path = path
        self.stopped = False
        self.start()

    def __out(self):
        if self.path == None: 
            return
        if self.queue.empty():
            return
        entry = self.queue.get()
        timestamp = entry['timestamp']
        stamp = util.timestamp_date(util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT))
        util.file_append(f"{self.path}\\{stamp}.txt", f"{util.json_encode(entry)}\n")
        util.file_append_json(f"{self.path}\\{stamp}.json", entry)

    def run(self):
        while True:
            if self.stopped: break
            self.__out()

    def print(self, entry: dict|str):
        if isinstance(entry, str):
            print(f"\n{entry}")
        if isinstance(entry, dict):
            print(f"\n{Logger.dump(entry)}")

    def put(self, entry: dict):
        timestamp = util.timestamp(util.TIMESTAMP_OPTION_OBJECT)
        timestamp = f"{util.timestamp_date(timestamp)}T{util.timestamp_time(timestamp)}"
        entry_ = { 'timestamp': timestamp }
        entry_.update(entry)
        self.queue.put(entry_)
        print(f'\n{Logger.dump(entry_)}')
        return self

    def out(path: str, entry: dict):
        timestamp = util.timestamp(util.TIMESTAMP_OPTION_OBJECT)
        timestamp = f"{util.timestamp_date(timestamp)}T{util.timestamp_time(timestamp)}"
        entry_ = { 'timestamp': timestamp }
        entry_.update(entry)
        print(f"\n{Logger.dump(entry_)}")
        if not path == None:
            stamp = util.timestamp_date(util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT))
            util.file_append_json(f"{path}\\{stamp}.json", entry_)

    def stop(self) -> None:
        self.stopped = True

    def dump(entry: dict) -> str:
        def get(value) -> str:
            if value == None:
                return 'null'
            elif isinstance(value, bool):
                return str(value)
            elif isinstance(value, float|int):
                return str(value)
            elif isinstance(value, str):
                return value
            elif isinstance(value, dict|object):
                string = '{'
                end = [key for key in value.keys()][-1] if len(value.keys()) > 0 else None
                for key, val in value.items():
                    string += f"{get(key)}: {get(val)}" + ('' if key == end else ', ')
                string += '}'
                return string
            elif isinstance(value, list|array):
                string = '['
                end = value[-1]
                for val in value:
                    string += get(val) + ('' if val == end else ', ')
                string += ']'
                return string
        string = f"{entry['timestamp']}: "
        end = [key for key in entry.keys()][-1]
        for key, val in entry.items():
            if key == 'timestamp': continue
            string += f"{get(key)}: {get(val)}" + ('' if key == end else ', ')
        return string

# ___________________________________________________________________________________________________________________________________________________#

"""



"""

def plot_relation():
    import matplotlib.pyplot
    matplotlib.pyplot.xlabel('x-axis')
    matplotlib.pyplot.ylabel('y-axis')
    points = [
        [
            0.5,2,5.4,10.6,15.2,22.2
        ], # x-axis
        [
            2904,3400,4500,6100,7500,10000
        ]  # y-axis
    ]
    matplotlib.pyplot.plot(*points, color='black', linestyle='solid', linewidth=1, marker='o', markersize=1)
    matplotlib.pyplot.grid(color = 'black', linestyle = 'solid', linewidth = 0.5)
    matplotlib.pyplot.show()
# plot_relation()

def geographic_coordinates_format(coordinate: list|str) -> str:
    latitude = 0
    longitude = 0
    if isinstance(coordinate, list):
        latitude = coordinate[0]
        longitude = coordinate[1]
    if isinstance(coordinate, str):
        latitude, longitude = coordinate.split(', ' if ',' in coordinate else ' ', 1)
        latitude = float(latitude)
        longitude = float(longitude)
    if latitude < 0:
        latitude *= -1
        latitude = f"{latitude:09.6f}"
        latitude = f"-{latitude}"
    else:
        latitude = f" {latitude:09.6f}"
    if longitude < 0:
        longitude *= -1
        longitude = f"{longitude:010.6f}"
        longitude = f"-{longitude}"
    else:
        longitude = f" {longitude:010.6f}"
        # 00.000000
    return f"{latitude} {longitude}"
# 
def geographic_coordinates():
    p1=[36.244667, -115.025000] # LSV
    p1_to_p2_azimuth = 256+10.5
    p1_to_p2_distance = 5*1852
    # 
    # p1_to_p2_azimuth = util.geographic_to_azimuth(p1, p2)
    # p1_to_p2_distance = util.geographic_to_distance(p1, p2)
    # magnetic_variation = -10.6
    # print(f"azimuth: {p1_to_p2_azimuth:.1f}T {p1_to_p2_azimuth + magnetic_variation:.1f}M")
    # print(f"distance: {p1_to_p2_distance:.0f}m {p1_to_p2_distance * 0.000539957:.5f}nm")

    p2 = util.geographic_to_destination_point(p1, p1_to_p2_azimuth, p1_to_p2_distance)
    print(f"point_2: {p2[0]:.6f} {p2[1]:.6f}")
# geographic_coordinates()
def geographic_arc_points():
    # arc leg degrees<=20°|distance<=1
    # arc = [ 27.302506 89.413029 ]
    # p1  = [ 27.399747 89.420309 ]
    # p2  = [ 27.358193 89.323473 ]
    arc = [float(coord) for coord in "36.244667 -115.025000".strip(' ').split(' ')]
    p1 =  [float(coord) for coord in "36.586310 -115.115825".strip(' ').split(' ')]
    p2 =  [float(coord) for coord in "36.589833 -114.949667".strip(' ').split(' ')]
    direction = 1 # 1=to_right -1=to_left
    point_count = 1
    # 
    arc_radius = (util.geographic_to_distance(arc, p1) + util.geographic_to_distance(arc, p2)) / 2
    arc_to_p1_azimuth = util.geographic_to_azimuth(arc, p1)
    arc_to_p2_azimuth = util.geographic_to_azimuth(arc, p2)
    azimuth_start = int(arc_to_p1_azimuth)
    azimuth_end   = int(arc_to_p2_azimuth)
    arc_degrees = 0
    for degree in range(1, 360, 1) if direction == 1 else range(-1, -360, -1):
        if (azimuth_start + degree)%360 == azimuth_end:
            arc_degrees = degree
    leg_degrees = arc_degrees/(point_count+1)
    arc_to_point_azimuth = azimuth_start
    print(f"radius: {arc_radius:.0f}m {arc_radius/1852:.1f}nm")
    print(f"arc_to_p1={azimuth_start}° arc_to_p2={azimuth_end}°")
    print(f"arc_degrees={abs(arc_degrees):.0f}° leg_degrees={abs(leg_degrees):.0f}°")
    for index in range(point_count):
        arc_to_point_azimuth = (arc_to_point_azimuth+leg_degrees)%360
        latitude, longitude = util.geographic_to_destination_point(arc, arc_to_point_azimuth, arc_radius)
        print(f"ARC{index:02x} {latitude:.6f} {longitude:.6f} {arc_to_point_azimuth:03.0f}°".upper())
# geographic_arc_points()

def interactive_map_tools_special_use_airspace():
    z={}
    a=util.file_read_json('C:\\references\\aviation\\special-use-airspace.geojson')
    b=a['features']
    for c in b:
        if not c['geometry']['type'] == 'Polygon': continue
        _ = util.identifier()
        __ = ''
        sc = ''
        if c['properties']['NAME'][:2] == 'A-':
            __ = 'Alert Area'
            sc = '#FF00FF'
        elif c['properties']['NAME'][:2] == 'R-':
            __ = 'Restricted Area'
            sc = '#0000FF'
        elif c['properties']['NAME'][:2] == 'P-':
            __ = 'Prohibited Area'
            sc = '#0000FF'
        elif c['properties']['NAME'][:2] == 'W-':
            __ = 'Warning Area'
            sc = '#0000FF'
        elif 'MOA' in c['properties']['NAME']:
            __ = 'Military Operating Area'
            sc = '#FF0000'
        else:
            continue
        paths = []
        for d in c['geometry']['coordinates']:
            for e in d:
                paths.append({ 'lat': e[1], 'lng': e[0] })
        z[_] = {
            'collection': __,
            'description': f"GLOBAL_ID={c['properties']['GLOBAL_ID']}",
            'enabled': False,
            'fillColor': sc,
            'fillOpacity': 0,
            'identifier': _,
            'name': c['properties']['NAME'],
            'paths': paths,
            'strokeColor': sc,
            'strokeOpacity': 1,
            'strokeWeight': 2,
        }
    z = {
        'circle': {},
        'marker': {},
        'polygon': z,
        'polyline': {},
    }
    util.file_write(f'C:\\projects\\json\\interactive-map-tools.map-objects.{util.identifier()}.json', z)
# interactive_map_tools_special_use_airspace()
def interactive_map_tools_special_use_airspace_shorten_polygon_coordinates():
    GLOBAL_ID = "89985718-F7E9-4226-B684-265F823C1D0C"
    azimuth_margin = 1
    distance_margin = 0
    # 
    points = []
    data = util.file_read_json('C:\\references\\aviation\\special-use-airspace.geojson')
    for feature in  data["features"]:
        if not feature["properties"]["GLOBAL_ID"] == GLOBAL_ID: continue
        # coordinate[0]=longitude, coordinate[1]=latitude, coordinate[2]=elevation
        for index, coordinate in enumerate(feature["geometry"]["coordinates"][0]):
            # point = [0=index, 1=latitude, 2=longitude, 3=azimuth_from_previous, 4=distance_from_previous, 5=visible]
            points.append([index, coordinate[1],coordinate[0], 0, 0, True])
            if index == 0: continue
            points[-1][3] =  util.geographic_to_azimuth([points[-2][1],points[-2][2]], [points[-1][1],points[-1][2]])
            points[-1][4] = util.geographic_to_distance([points[-2][1],points[-2][2]], [points[-1][1],points[-1][2]])
    points[0][3] =  util.geographic_to_azimuth([points[-1][1],points[-1][2]], [points[0][1],points[0][2]])
    points[0][4] = util.geographic_to_distance([points[-1][1],points[-1][2]], [points[0][1],points[0][2]])
    pPoint = points[0]
    if util.geographic_to_distance([points[0][1],points[0][2]], [points[-1][1],points[-1][2]]) == 0:
        points[-1][5] = False
    for index, cPoint in enumerate(points):
        if index == 0: continue
        in_azimuth_margin = abs(pPoint[3] - cPoint[3]) < azimuth_margin
        in_distance_margin = abs(pPoint[4] - cPoint[4]) < distance_margin
        if in_azimuth_margin or in_distance_margin:
            pPoint[5] = False
        pPoint = cPoint
    for index, point in enumerate(points):
        line = f"{index:03d} {point[1]:.6f}, {point[2]:.6f} {point[3]:.1f}°T/{point[4]:.0f}m"
        if point[5]: print(line)
    filtered = 0
    for index, point in enumerate(points):
        if point[5]: print(f"{point[1]:.6f} {point[2]:.6f}")
        else: filtered += 1
    print(f"filtered={filtered}")
    # for index, point in enumerate(points):
    #     lat, lng = util.geographic_ddd_to_dms([point[1],point[2]])
    #     if point[5]: print(f"{lat} {lng}")
# interactive_map_tools_special_use_airspace_shorten_polygon_coordinates()
def interactive_map_tools_special_use_airspace_polygon_to_circle():
    GLOBAL_ID = '8D66B2D1-304A-4313-A3C1-61BBDD9BE68F'
    collection = "Alert Area"
    fillColor = "#FF00FF"
    fillOpacity = "0"
    strokeColor = "#FF00FF"
    strokeOpacity = "0.75"
    strokeWeight = "2"
    # 
    data = util.file_read_json('C:\\references\\aviation\\special-use-airspace.geojson')
    circleEntry = {
        "center": { "lat": 0, "lng": 0 },
        "collection": collection,
        "description": f"GLOBAL_ID={GLOBAL_ID}",
        "enabled": True,
        "fillColor": fillColor,
        "fillOpacity": fillOpacity,
        "identifier": util.identifier(),
        "name": "",
        "radius": 0,
        "strokeColor": strokeColor,
        "strokeOpacity": strokeOpacity,
        "strokeWeight": strokeWeight,
    }
    for feature in  data["features"]:
        if not feature["properties"]["GLOBAL_ID"] == GLOBAL_ID: continue
        diameter = 0
        indexGreatestDistance = 0
        # coordinate[0]=longitude, coordinate[1]=latitude, coordinate[2]=elevation
        point1 = [feature["geometry"]["coordinates"][0][0][1],feature["geometry"]["coordinates"][0][0][0]]
        # point1~southernmost
        for index, coordinate in enumerate(feature["geometry"]["coordinates"][0]):
            if index == 0: continue
            distance = util.geographic_to_distance(point1,[coordinate[1],coordinate[0]])
            if distance > diameter:
                diameter = distance
                indexGreatestDistance = index
        point2 = [feature["geometry"]["coordinates"][0][indexGreatestDistance][1],feature["geometry"]["coordinates"][0][indexGreatestDistance][0]]
        azimuth = util.geographic_to_azimuth(point1, point2)
        center = util.geographic_to_destination_point(point1, azimuth, diameter / 2)
        circleEntry["center"]["lat"] = center[0]
        circleEntry["center"]["lng"] = center[1]
        circleEntry["name"] = feature["properties"]["NAME"]
        circleEntry["radius"] = util.mathematics_round(diameter / 2, 1)
        break
    # print(circleEntry)
    print('identifier ', circleEntry["identifier"])
    print('name       ', circleEntry["name"])
    print('collection ', circleEntry["collection"])
    print('description', circleEntry["description"])
    print('radius     ', circleEntry["radius"])
    print('center     ', circleEntry["center"])
# interactive_map_tools_special_use_airspace_polygon_to_circle()

def flightgear_military_training_route():
    ident = '296'
    # 
    a=util.file_read_json('c:\\projects\\json\\military-training-routes-segment.geojson')
    b=[{ 'identifier': aa['properties']['IDENT'], 'object-identifier': aa['properties']['OBJECTID'], 'coordinates': aa['geometry']['coordinates'] } for aa in a['features'] if ident == aa['properties']['IDENT']]
    c=""""""
    for bb in b:
        _ = [f"{_[1]} {_[0]}" for _ in bb['coordinates']]
        bba = geographic_coordinates_format(_[0])
        bbb = geographic_coordinates_format(_[1])
        print(f"{bb['identifier']} {bb['object-identifier']} {bba} {bbb}")
    for i, bb in enumerate(b):
        _ = [f"{_[1]} {_[0]}" for _ in bb['coordinates']]
        bba = geographic_coordinates_format(_[0])
        bbb = geographic_coordinates_format(_[1])
        print(f"{bba}\n{bbb}" if i == 0 else f"{bbb}")
        c += f"{bba}\n{bbb}" if i == 0 else f"{bbb}"
        c += "\n"
    c= c if len(c) > 0 else """
    """
    d = [_ for _ in c.splitlines() if len(_) > 0]
    for i, dd in enumerate(d):
        dda, ddb = dd.split(' ', 1)
        dda = float(dda)
        ddb = float(ddb)
        ia = f"{i+1}".rjust(2, '0')
        # print(f"{ia} {dda:.5f} {ddb:.5f}")
        # print(f"{dda:.5f} {ddb:.5f}")
        print(f"""    <wp>
      <type type="string">basic</type>
      <ident type="string">STPT{ia}</ident>
      <lon type="double">{ddb:.5f}</lon>
      <lat type="double">{dda:.5f}</lat>
    </wp>
""", end="")
# flightgear_military_training_route()
def flightgear_special_use_airspace_to_hsd_lines():
    filename = "P-56A"
    GLOBAL_ID = "EED92347-3285-4391-B469-3B547AC268AD"
    # 
    points = []
    data = util.file_read_json('C:\\references\\aviation\\special-use-airspace.geojson')
    for feature in  data["features"]:
        if not feature["properties"]["GLOBAL_ID"] == GLOBAL_ID: continue
        feature["geometry"]["coordinates"]
        # coordinate[0]=longitude, coordinate[1]=latitude, coordinate[2]=elevation
        for index, coordinate in enumerate(feature["geometry"]["coordinates"][0]):
            points.append([coordinate[1], coordinate[0]])
    if points[0] == points[-1]:
        points = points[:-1]
    data = f"""<?xml version="1.0"?>
<PropertyList>
  <version type="int">2</version>
  <route>\n"""
    for index, point in enumerate(points):
        data += f"""    <wp>
      <type type="string">basic</type>
      <ident type="string">{index+1:02d}</ident>
      <lon type="double">{point[1]:6f}</lon>
      <lat type="double">{point[0]:6f}</lat>
    </wp>\n"""
    data += f"""  </route>
</PropertyList>"""
    util.file_write(f"c:\\projects\\applications\\flightgear\\routes\\hsd-lines\\{filename}.fgfp", data)
# flightgear_special_use_airspace_to_hsd_lines()
def flightgear_suggested_airports_to_table():
    a="""
LKKB *** 
BKPR *   
CYVR *   
EDDC **  
EDDF ****
EDDH *** 
EDDI ****
EDDK ****
EDDL *** 
EDDP *** 
EDDS *** 
EDDT *** 
EDDV *   
EDDW **  
EDFH **  
EDLN *** 
EDVE **  
EDXW *** 
EEKE **  
EFHF **  
EFHK **  
EEPU **  
EETN **  
EETU **  
EGFF **  
EGGP *** 
EGGW *** 
EGKA *** 
EGKK ****
EGLL *** 
EGPH **  
EGSH **  
EGUL *** 
EGUN *** 
EHAM ****
EHEH **  
EHLE *** 
EHVK **  
EIDW *** 
ELLX **  
ENAL **  
ENSD **  
ENVA *** 
ESGP **  
FACT *   
FAJS *   
FHAW *   
GCFV *   
GE99 *   
KABQ *   
HECA *   
KATL *   
KAUS *** 
KBWI *** 
KCGS **  
KDCA *** 
KDEN **  
KDTW **  
KFHR *   
KHAF *   
KHWD **  
KIAD *   
KIND *** 
KJAN *** 
KJFK *** 
KLAS ****
KLAX *** 
KLSV *** 
KLWD **  
KMTN **  
KNID **  
KNUQ **  
KOAK **  
KORD **  
KOSH **  
KOXB **  
KPDX **  
KPHX **  
KRDU **  
KRNO **  
KSAN *   
KSEA **  
KSFO ****
KSLC *   
KSJC *   
LDSP **  
LDZU *   
LFFE *** 
LFML *   
LFPG ****
LFPH *** 
LFPL *** 
LFPO ****
LFPZ *** 
LFRJ **  
LFSB *** 
LHBP *   
LILN **  
LILV **  
LIMC *** 
LIME **  
LIML *** 
LIMW *   
LIPA **  
LJCE *   
LJLJ *   
LJPZ *   
LPLA *   
LQSA *   
LOWI ****
LROP **  
LSGS *   
LSZH **  
LSZB **  
LSZS *** 
PANC *** 
LYBE *** 
LYPG *   
LYTV *   
MUHA *   
NZAA *   
OMAA *   
OOMS *   
PHNL *   
PHOG *   
RJTT *** 
RKSI *** 
RPLL *** 
TDPD **  
TFFF *** 
TFFG **  
TIST **  
TJSJ *** 
TKPK **  
TNCM *** 
TQPF **  
VIDP **  
VHHH *   
WSSS ****
YBAS *   
YBBN *** 
YPDN *   
YSCB *   
YSSY *   
    """
    b = [ab for ab in a.splitlines() if not ab.strip(' ') == '']
    b.sort()
    c = []
    for i, ba in enumerate(b):
        icao, rate = ba.strip(' ').split(' ')
        b[i] = f"{icao} {len(rate)}"
        if not ba[0] in c:
            c += [ba[0]]
    d = [[] for i in range(len(c))]
    rows = 0
    for cIndex, ca in enumerate(c):
        for ba in b:
            if ba[0] == ca: d[cIndex] += [ba]
        rows = len(d[cIndex]) if rows < len(d[cIndex]) else rows
    matrix = [['      ' for ri in range(rows)] for ci in range(len(c))]
    output = ""
    rIndex = 0
    for rIndex in range(rows):
        columns = []
        for cIndex in range(len(c)): columns += [d[cIndex][rIndex] if rIndex < len(d[cIndex]) else '      ']
        output += f"|{'  '.join(columns)}|\n"
    print(output)
# flightgear_suggested_airports_to_table()
def flightgear_suggested_airports_to_interactive_map_tools_object_file():
    a="""
BKPR,Pristina/International Airport,42.572833,21.035833
CYVR,Vancouver International Airport,49.194667,-123.182500
EDDC,Dresden Airport,51.134333,13.768000
EDDF,Frankfurt Main Airport,50.033333,8.570500
EDDH,Hamburg Airport,53.630333,9.988167
EDDK,Koeln/Bonn Airport,50.866000,7.142667
EDDL,Duesseldorf Airport,51.281000,6.757333
EDDP,Leipzig/Halle Airport,51.424000,12.236333
EDDS,Stuttgart Airport,48.689833,9.222000
EDDV,Hannover Airport,52.460167,9.683500
EDDW,Bremen Airport,53.047333,8.786667
EDFH,Frankfurt-Hahn Airport,49.945833,7.261000
EDLN,Moenchengladbach Airport,51.230333,6.504500
EDVE,Braunschweig-Wolfsburg Airport,52.319333,10.558833
EDXW,Sylt Airport,54.911667,8.342333
EEKE,Kuressaare Airport,58.230000,22.509500
EEPU,Parnu Airport,58.418833,24.472833
EETN,Lennart Meri Tallinn Airport,59.413333,24.832500
EETU,Tartu Airport,58.307500,26.687000
EFHF,Helsinki Malmi Airport,60.253833,25.044167
EFHK,Helsinki Vantaa Airport,60.317167,24.963333
EGFF,Cardiff Airport,51.396667,-3.343333
EGGP,Liverpool Airport,53.333667,-2.849667
EGGW,London Luton Airport,51.874667,-0.368333
EGKA,Shoreham Airport,50.835500,-0.297167
EGKK,London Gatwick Airport,51.148000,-0.190333
EGLL,London Heathrow Airport,51.477500,-0.461333
EGPH,Edinburgh Airport,55.950000,-3.372500
EGSH,Norwich Airport,52.675833,1.282833
EGUL,Lakenheath Airport,52.409333,0.561000
EGUN,Mildenhall Airport,52.362000,0.486333
EHAM,Amsterdam Schiphol Airport,52.308000,4.764167
EHEH,Eindhoven Airport,51.450000,5.374500
EHLE,Lelystad Airport,52.453333,5.513833
EHVK,Volkel Airport,51.657167,5.707833
EIDW,Dublin International Airport,53.421333,-6.270000
ELLX,Luxembourg Airport,49.623333,6.204500
ENAL,Alesund/Vigra Airport,62.562500,6.119667
ENSD,Sandane/Anda Airport,61.830000,6.105833
ENVA,Trondheim/Vaernes Airport,63.457500,10.924167
ESGP,Goteborg/Save Airport,57.775500,11.870500
FACT,Cape Town International Airport,-33.971333,18.604333
FHAW,Ascension Aux Af Airport,-7.969667,-14.393667
GCFV,Fuerteventura Airport,28.452833,-13.863833
GE99,Heaven's Landing Airport,34.914167,-83.459500
HECA,Cairo International Airport,30.111333,31.413833
KABQ,Albuquerque International Sunport,35.039000,-106.608333
KATL,Hartsfield/Jackson Atlanta International,33.636667,-84.427833
KAUS,Austin-Bergstrom International Airport,30.194500,-97.669833
KBWI,Baltimore/Washington International,39.175667,-76.669000
KCGS,College Park Airport,38.980500,-76.922167
KDCA,Ronald Reagan Washington National Airport,38.851500,-77.037667
KDEN,Denver International Airport,39.861667,-104.673167
KDTW,Detroit Metro Wayne County Airport,42.212500,-83.353333
KFHR,Friday Harbor Airport,48.522000,-123.024333
KHAF,Half Moon Bay Airport,37.513500,-122.501167
KHWD,Hayward Executive Airport,37.659000,-122.121667
KIAD,Washington Dulles International Airport,38.947500,-77.460000
KIND,Indianapolis International Airport,39.717333,-86.294667
KJAN,Jackson-Medgar Wiley Evers,32.311167,-90.075833
KJFK,John F Kennedy International Airport,40.640000,-73.778667
KLAS,Harry Reid International Airport,36.080000,-115.152167
KLAX,Los Angeles International Airport,33.942500,-118.408000
KLSV,Nellis AFB Airport,36.236167,-115.034333
KLWD,Lamoni Municipal Airport,40.632333,-93.902167
KMTN,Martin State Airport,39.325667,-76.413833
KNID,China Lake Naws (Armitage Field),35.685333,-117.695167
KNUQ,Moffett Federal Airfield Airport,37.416167,-122.049167
KOAK,San Francisco Bay Oakland International Airport,37.721333,-122.221167
KORD,Chicago O'Hare International Airport,41.977000,-87.908167
KOSH,Wittman Regional Airport,43.984333,-88.557000
KOXB,Ocean City Municipal Airport,38.310500,-75.124000
KPDX,Portland International Airport,45.588667,-122.596833
KPHX,Phoenix Sky Harbor International Airport,33.434333,-112.011500
KRDU,Raleigh-Durham International Airport,35.877667,-78.787500
KRNO,Reno/Tahoe International Airport,39.499167,-119.768167
KSAN,San Diego International Airport,32.733500,-117.189667
KSEA,Seattle-Tacoma International Airport,47.449833,-122.311833
KSFO,San Francisco International Airport,37.618833,-122.375500
KSJC,Norman Y Mineta San Jose International Airport,37.363000,-121.928667
KSLC,Salt Lake City International Airport,40.788333,-111.977833
LDSP,Zracna Luka Split/Kastela Airport,43.539000,16.298000
LFFE,Enghien Moisselles Airport,49.045500,2.352000
LFML,Marseille Provence Airport,43.436667,5.215000
LFPG,Paris Charles De Gaulle Airport,49.009833,2.547833
LFPH,Chelles Le Pin Airport,48.897833,2.607500
LFPL,Lognes Emerainville Airport,48.822000,2.622833
LFPO,Paris Orly Airport,48.723333,2.379500
LFPZ,St.Cyr L'Ecole Airport,48.810333,2.073333
LFRJ,Landivisiau Airport,48.530333,-4.151667
LFSB,Bale-Mulhouse Airport,47.590000,7.529167
LHBP,Budapest Liszt Ferenc International,47.439500,19.262000
LILN,Varese/Venegono Airport,45.742167,8.888000
LILV,Valbrembo Airport,45.720500,9.593667
LIMC,Milano/Malpensa Airport,45.630000,8.723000
LIME,Bergamo/Orio Al Serio Airport,45.668833,9.700333
LIML,Milano/Linate Airport,45.449500,9.278333
LIMW,Aosta Airport,45.738333,7.367500
LIPA,Aviano Airport,46.030000,12.598833
LJCE,Cerklje Ob Krki Airport,45.900000,15.530333
LJLJ,Ljubljana/Brnik Airport,46.224500,14.456167
LJPZ,Portoroz/Secovlje Airport,45.473333,13.615000
LKKB,Kbely Airport,50.121333,14.543667
LOWI,Innsbruck Airport,47.260333,11.343833
LPLA,Lajes Airport,38.762000,-27.090833
LQSA,Sarajevo International Airport,43.824500,18.331833
LROP,Henri Coanda Airport,44.571167,26.085000
LSGS,Sion Airport,46.219167,7.327000
LSZB,Bern Belp Airport,46.912167,7.499500
LSZH,Zurich Airport,47.458000,8.548000
LSZS,Samedan Airport,46.534500,9.884167
LYBE,Beograd/Nikola Tesla Airport,44.819500,20.307000
LYPG,Podgorica Airport,42.359500,19.252000
LYTV,Tivat Airport,42.404667,18.723333
MUHA,La Habana/Jose Marti International,22.989167,-82.409167
NZAA,Auckland Airport,-37.008000,174.791667
OMAA,Abu Dhabi International Airport,24.433000,54.651167
OOMS,Muscat International Airport,23.600167,58.283667
PANC,Ted Stevens Anchorage International,61.174167,-149.998167
PHNL,Daniel K Inouye International Airport,21.317833,-157.920333
PHOG,Kahului Airport,20.898667,-156.430500
RJTT,Tokyo International. Airport,35.553333,139.781167
RKSI,Incheon International Airport,37.462500,126.439167
RPLL,Ninoy Aquino International Airport,14.510000,121.013667
TDPD,Roseau/Douglas Charles - International,15.546667,-61.301333
TFFF,Martinique Aime Cesaire Airport,14.592167,-60.996333
TFFG,Grand Case Airport,18.100500,-63.048833
TIST,Cyril E King Airport,18.337333,-64.973333
TJSJ,Luis Munoz Marin International Airport,18.439333,-66.002167
TKPK,Basseterre/Robert L. Bradshaw Airport,17.311167,-62.718667
TNCM,Princess Juliana International Airport,18.041000,-63.109000
TQPF,Clayton J Lloyd International Airport,18.204833,-63.053833
VHHH,Hong Kong International Airport,22.308833,113.914667
VIDP,Indira Gandhi International Airport,28.568667,77.112167
WSSS,Singapore Changi International Airport,1.359167,103.989333
YBAS,Alice Springs Airport,-23.808333,133.900833
YBBN,Brisbane Airport,-27.384167,153.117500
YPDN,Darwin Airport,-12.414667,130.876667
YSCB,Canberra Airport,-35.307000,149.195000
YSSY,Sydney/Kingsford Smith Airport,-33.946167,151.177167
    """
    lines = a.splitlines()
    markers = {}
    entries = []
    for line in lines:
        if line == '': continue
        icao, name, latitude, longitude = line.split(',')
        latitude = float(latitude)
        longitude = float(longitude)
        identifier = util.identifier()
        coordinates = geographic_coordinates_format([latitude, longitude])
        entries.append({
            'Identifier': icao,
            'Name': name,
            "Coordinates": coordinates,
        })
        markers[identifier] = {
            'identifier': identifier,
            'name': name,
            'enabled': True,
            'collection': 'FlightGear Suggested Airports',
            'description': "",
            'label': icao,
            'position': { 'lat': latitude, 'lng': longitude },
            'opacity': 1,
        }
    util.file_write_json("c:\\projects\\json\\interactive-map-tools.additions.flightgear-suggested-airports.json", markers)
    util.file_write_json("c:\\projects\\json\\flightgear-suggested-airports.json", entries)
# flightgear_suggested_airports_to_interactive_map_tools_object_file()
def flightgear_tanker_station_route():
    log="""
    NAME CENTER COURSE ALTITUDE AIRSPEED TIME
    "W-161A SOUTH" [32.55370397181299,-79.03983848946656] 110.08672954661951 FL200 250 05
    "R-4806E" [36.958368508806586,-115.20923640749879] 000 FL100 250 04
    "R-4806E" [36.997257464995520,-115.20916666666668] 000 FL100 250 05
    """
    """
    363800N 1151803W
    371700N 1151803W
    371700N 1151104W
    371200N 1150703W
    364800N 1150704W
    """
    # return
    # pointTL = [float(coord) for coord in util.geographic_dms_to_ddd('371500N 1151803W'.split(' '))]
    # pointTR = [float(coord) for coord in util.geographic_dms_to_ddd('371500N 1150703W'.split(' '))]
    # pointBL = [float(coord) for coord in util.geographic_dms_to_ddd('364440N 1151803W'.split(' '))]
    # pointBR = [float(coord) for coord in util.geographic_dms_to_ddd('364440N 1150703W'.split(' '))]
    # center_left = util.geographic_to_center_point(pointTL, pointBL)
    # center_right = util.geographic_to_center_point(pointTR, pointBR)
    # center = util.geographic_to_center_point(center_left, center_right)
    # course = util.geographic_to_azimuth(center_left, center_right)
    # print(f"center={center}")
    # return
    # 
    filename = "R-4806E"
    center = [36.99725746499552, -115.20916666666668]
    course = 0
    altitude = 20000
    airspeed = 250
    groundspeed = 336 # use https://aerotoolbox.com/airspeed-conversions/
    time_leg = 4 # minutes
    iteratation_count = 10
    # 
    turn_characteristics = [
        { "altitude":  5000, "speed": 200, "distance":   7135 },
        { "altitude":  5000, "speed": 250, "distance":  10875 },
        { "altitude":  5000, "speed": 300, "distance":  15660 },
        { "altitude": 10000, "speed": 200, "distance":   8095 },
        { "altitude": 10000, "speed": 250, "distance":  12355 },
        { "altitude": 10000, "speed": 300, "distance":  17675 },
        { "altitude": 15000, "speed": 200, "distance":   9390 },
        { "altitude": 15000, "speed": 250, "distance":  14170 },
        { "altitude": 15000, "speed": 300, "distance":  20160 },
        { "altitude": 20000, "speed": 200, "distance":  10780 },
        { "altitude": 20000, "speed": 250, "distance":  16255 },
        { "altitude": 20000, "speed": 300, "distance":  23340 },
        { "altitude": 25000, "speed": 200, "distance":  12630 },
        { "altitude": 25000, "speed": 250, "distance":  18795 },
        { "altitude": 25000, "speed": 300, "distance":  26610 },
        { "altitude": 30000, "speed": 200, "distance":  14620 },
        { "altitude": 30000, "speed": 250, "distance":  21560 },
        { "altitude": 30000, "speed": 300, "distance":  29940 },
    ]
    distance_turn_diameter = None
    for entry in turn_characteristics:
        if entry["altitude"] == altitude and entry["speed"] == airspeed:
            distance_turn_diameter = entry["distance"]
    if not distance_turn_diameter: return print("ParameterValueError: altitude or airspeed not found.")
    distance_leg = ((time_leg / 60) * groundspeed) * 1852
    distance_route = util.geometry_circumference(distance_turn_diameter/2) + (distance_leg*2)
    duration = ((distance_route*iteratation_count)/1852)/groundspeed
    duration_hours = int(duration)
    duration_minutes = util.mathematics_round((duration-duration_hours)*60, 1)
    point1 = util.geographic_to_destination_point(center, (course+90)%360, distance_turn_diameter/2)
    point1 = util.geographic_to_destination_point(point1, course, distance_leg/2)
    point2 = util.geographic_to_destination_point(center, (course-90)%360, distance_turn_diameter/2)
    point2 = util.geographic_to_destination_point(point2, (course+180)%360, distance_leg/2)
    print(f"course={course:.1f} | {(course+180)%360:.1f}")
    print(f"duration={duration_hours:02d}{duration_minutes:02d}")
    print(F"STPT01 {point1[0]:.6f} {point1[1]:.6f}")
    print(F"STPT02 {point2[0]:.6f} {point2[1]:.6f}")
    # iteratation_count_calculated = (time_duration*60) / util.mathematics_round(((distance_route/1852) / groundspeed)*60, 1)
    data = f"""<?xml version="1.0"?>
<PropertyList>
  <version type="int">2</version>
  <flight-rules type="string">F</flight-rules>
  <flight-type type="string">X</flight-type>
  <cruise>
    <altitude-ft type="int">{altitude}</altitude-ft>
    <knots type="int">{airspeed}</knots>
  </cruise>
  <route>
"""
    for count in range(iteratation_count):
        data += f"""    <wp>
      <type type="string">basic</type>
      <ident type="string">STPT01</ident>
      <lon type="double">{point1[1]:.6F}</lon>
      <lat type="double">{point1[0]:.6F}</lat>
    </wp>
    <wp>
      <type type="string">basic</type>
      <ident type="string">STPT02</ident>
      <lon type="double">{point2[1]:.6F}</lon>
      <lat type="double">{point2[0]:.6F}</lat>
    </wp>       
"""
    data += """  </route>
</PropertyList>
"""
    util.file_write(f"c:\\projects\\applications\\flightgear\\routes\\TANKER\\{filename} - FL{altitude/100:.0f} {airspeed}KN {time_leg:02d}MIN.fgfp", data)
# flightgear_tanker_station_route()
def flightgear_waypoint_altitude():
    lines="""
    """[1:-1].splitlines()
    # 
    entries = []
    for line in lines:
        if line.strip(' ') == '': continue
        entries.append([data for data in line.split(' ') if not data == ''])
    total_distance = 0
    for index, entry in enumerate(entries):
        if index == 0: continue
        aEntry = entries[index-1]
        bEntry = entries[index]
        total_distance += util.geographic_to_distance([float(aEntry[1]),float(aEntry[2])],[float(bEntry[1]),float(bEntry[2])])
    altitude_difference = abs(float(entries[0][3]) - float(entries[-1][3]))
    sideA = altitude_difference
    sideB = total_distance*3.28084
    sideC = math.sqrt(sideA**2+sideB**2)
    angleA = math.asin(sideA/sideC)*util.RADIANS_TO_DEGREES
    flight_path_angle = angleA
    total_distance = 0
    print(f"{entries[0][0]}-{entries[-1][0]} FPA={flight_path_angle:.3f}°")
    print(f"altitude_difference={altitude_difference:.0f}ft")
    direction = 1 if float(entries[0][3]) < float(entries[-1][3]) else -1
    for index, entry in enumerate(entries):
        if index == 0: continue
        aEntry = entries[index-1]
        bEntry = entries[index]
        distance = util.geographic_to_distance([float(aEntry[1]),float(aEntry[2])],[float(bEntry[1]),float(bEntry[2])])
        total_distance += distance
        angleA = flight_path_angle*util.DEGREES_TO_RADIANS
        sideB = total_distance*3.28084
        sideC = sideB/math.cos(angleA)
        sideA = math.sqrt(sideC**2-sideB**2)
        altitude = float(entries[0][3]) + (sideA*direction)
        print(f"{aEntry[0]}-{bEntry[0]} distance={distance:05.0f}m/{distance*3.28084:06.0f}ft total_distance={total_distance:05.0f}m/{total_distance*3.28084:06.0f}ft altitude={altitude:05.0f}ft")
        # print(f"{bEntry[0]} altitude={altitude:05.0f}FT")
# flightgear_waypoint_altitude()
def flightgear_waypoint_encoder():
    # IDENTIFIER LATITUDE LONGITUDE ALTITUDE
    lines="""
    """[1:-1].splitlines()
    # 
    text = ""
    for index, line in enumerate(lines):
        if line.strip(' ') == '': continue
        waypoint = [data for data in line.split(' ') if not data == '']
        text += f"""    <wp>
      <type type="string">basic</type>
"""
        if len(waypoint) == 4:
            text += f"""      <alt-restrict type="string">at</alt-restrict>
      <altitude-ft type="double">{waypoint[3]}</altitude-ft>
"""
        text += f"""      <ident type="string">{waypoint[0]}</ident>
      <lon type="double">{waypoint[2]}</lon>
      <lat type="double">{waypoint[1]}</lat>
    </wp>
"""
    text = text[:-1]
    print(text)
    app.copyToClipboard(text)
# flightgear_waypoint_encoder()

def military_airfield_table_builder(location_identifier: str, owner: str):
    ROW = {}
    import requests
    headers = {
        'Authorization': 'Basic 3f647d1c-a3e7-415e-96e1-6e8415e6f209-ADIP'
    }
    url = "https://adip.faa.gov/agisServices/public-api/getAirportDetails"
    data = {'locId': location_identifier}
    x: requests.Response = requests.post(url=url, headers=headers, json=data)
    data = x.json()
    # 
    # 
    # 
    # name
    name: str = data['name']
    name = name.replace('AAF', 'Army Airfield')
    name = name.replace('AFB', 'Air Force Base')
    name = name.replace('ARB', 'Air Reserve Base')
    name = name.replace('CGS', 'Coast Guard Station')
    name = name.replace('CGAS', 'Coast Guard Air Station')
    name = name.replace('FLD', 'Field')
    name = name.replace('LRRS', 'Long Range Radar Site')
    name = name.replace('MCAS', 'Marine Corps Air Station')
    name = name.replace('MCAF', 'Marine Corps Air Facility')
    name = name.replace('NAF', 'Naval Air Facility')
    name = name.replace('NALF', 'Naval Auxiliary Landing Field')
    name = name.replace('NAS', 'Naval Air Station')
    name = name.replace('NOLF', 'Naval Outlying Landing Field')
    name = name.replace('NS', 'Naval Station')
    name = name.replace('SELF', 'Strategic Expeditionary Landing Field')
    name = name.strip(' ')
    name = util.capitalize(name)
    ROW['Name'] = name
    # international civil aviation organization code
    international_civil_aviation_organization_code: str = data['icaoId']
    international_civil_aviation_organization_code = international_civil_aviation_organization_code.upper()
    ROW['ICAO'] = international_civil_aviation_organization_code
    # owner
    # owner: str = data['ownerName'] 
    # owner = owner.replace('U.S. ', '').strip(' ')
    # owner = util.capitalize(owner)
    ROW['Owner'] = owner
    # coordinates
    latitude = data['arpLatitude']
    if latitude < 0:
        latitude *= -1
        latitude = f"{latitude:08.5f}"
        latitude = f"-{latitude}"
    else:
        latitude = f" {latitude:08.5f}"
    longitude = data['arpLongitude']
    if longitude < 0:
        longitude *= -1
        longitude = f"{longitude:09.5f}"
        longitude = f"-{longitude}"
    else:
        longitude = f" {longitude:09.5f}"
    coordinates = f"{latitude} {longitude}"
    ROW['Coordinates'] = coordinates
    # 
    # 
    # 
    print(util.dump(ROW))
    # 
    util.file_append_json('c:\\projects\\json\\united-states-military-airfields.json', ROW)
    return ROW
# military_airfield_table_builder('LDR', 'Coast Guard')
def military_airfields_builder():
    def name_alter(name: str):
        name = name.upper()
        name = name.replace('AAF', 'Army Airfield')
        name = name.replace('AHP', 'Army Heliport')
        name = name.replace('AUX', 'Auxiliary')
        name = name.replace('AFB', 'Air Force Base')
        name = name.replace('ARB', 'Air Reserve Base')
        name = name.replace("AS", "Airstrip")
        name = name.replace('CGS', 'Coast Guard Station')
        name = name.replace('CGAS', 'Coast Guard Air Station')
        name = name.replace("EAF", "Expeditionary Airfield")
        name = name.replace('FLD', 'Field')
        name = name.replace('LRRS', 'Long Range Radar Site')
        name = name.replace('MCAS', 'Marine Corps Air Station')
        name = name.replace('MCAF', 'Marine Corps Air Facility')
        name = name.replace('MCOLF', 'Marine Corps Outlying Landing Field')
        name = name.replace('NAF', 'Naval Air Facility')
        name = name.replace('NALF', 'Naval Auxiliary Landing Field')
        name = name.replace('NAS', 'Naval Air Station')
        name = name.replace('NOLF', 'Naval Outlying Landing Field')
        name = name.replace('NSF', 'Navy Support Facility')
        name = name.replace('NS', 'Naval Station')
        name = name.replace('SELF', 'Strategic Expeditionary Landing Field')
        return util.capitalize(name)
    a=util.file_read_json("c:\\projects\\json\\airports.geojson")
    b=[aa for aa in a['features'] if aa['properties']['MIL_CODE'] == 'MIL']
    c=util.file_read_json('c:\\projects\\json\\airfields-military.json')
    d=util.file_read_json('c:\\projects\\json\\airfields-military-additions.json')
    known_identifiers = [ca['Identifier'] for ca in [*c, *d]] # identifiers
    blocked_identifiers='AZ38,CPZ3,NV72'.split(',')
    entries = []
    for ba in b:
        identifier = ba['properties']['ICAO_ID'] if ba['properties']['ICAO_ID'] else ba['properties']['IDENT']
        if identifier in known_identifiers or identifier in blocked_identifiers: continue
        coordinates = [ba['geometry']['coordinates'][1], ba['geometry']['coordinates'][0]]
        entries.append({
            'Name': '',
            'Identifier': identifier,
            'Owner': '',
            'Coordinates': geographic_coordinates_format(coordinates)
        })
    entries.sort(key=lambda entry : entry['Identifier'])
    import requests
    for entry in entries:
        response: requests.Response = requests.post(
            url="https://adip.faa.gov/agisServices/public-api/getAirportDetails",
            headers={'Authorization': 'Basic 3f647d1c-a3e7-415e-96e1-6e8415e6f209-ADIP'},
            json={'locId': entry['Identifier']}
        )
        data = response.json()
        if not 'runways' in data: continue
        if data['runways'] == []: continue
        entry['Name'] = name_alter(data['name'])
        entry['Owner'] = util.capitalize(data['ownershipType'])
        if input(util.dump(entry)).lower() == 'y':
            util.file_append_json('c:\\projects\\json\\airfields-military-additions.json', entry)
# military_airfields_builder()
def military_airfields_to_interactive_map_tools_markers():
    # "aptwasx6in":{ "collection":"","description":"","enabled":true,"identifier":"aptwasx6in","label":"A","name":"__MARKER__","opacity":"1","position":{"lat":49.01,"lng":2.563} }
    a=util.file_read_json('c:\\projects\\json\\airfields-military-additions.json')
    a.sort(key=lambda entry : entry['Name'])
    markers = {}
    for aa in a:
        identifier = util.identifier()
        coordinates = aa['Coordinates'].split(' ')
        latitude = float(coordinates[0])
        longitude = float(coordinates[1])
        markers[identifier] = {
            'collection': 'United States Military Airfields',
            'description': '',
            'enabled': True,
            'identifier': identifier,
            'label': aa['Identifier'],
            'name': aa['Name'],
            'opacity': 1,
            'position': { 'lat': latitude, 'lng': longitude }
        }
    print(util.json_encode(markers))
# military_airfields_to_interactive_map_tools_markers()

def aviation_skyvector_navigation_log_decoder():
    data="""
    """
    lines = [line.strip(' ') for line in data.splitlines() if line]
    identifiers_length = int(len(lines) / 3)
    for i in range(identifiers_length):
        identifier = lines[i]
        latitude = lines[identifiers_length+(i*2)]
        longitude = lines[identifiers_length+(i*2)+1]
        latitude = f"{latitude[2:-1]}{latitude[0]}"
        longitude = f"{longitude[2:-1]}{longitude[0]}"
        latitude, longitude = util.geographic_ddm_to_ddd([latitude, longitude])
        print(identifier, latitude, longitude)
    #     print(f"""    <wp>
    #   <type type="string">basic</type>
    #   <ident type="string">{identifier}</ident>
    #   <lon type="double">{longitude}</lon>
    #   <lat type="double">{latitude}</lat>
    # </wp>""")
# aviation_skyvector_navigation_log_decoder()
def aviation_fuel_consumption_converter():
    gallons_to_pounds = 6.71994640597474133439198074585020
    pounds_to_gallons = 0.14881071061978924359570807210321
    engine_count = 4
    # 
    pounds_per_hour = 4392
    gallons_per_hour = pounds_per_hour * pounds_to_gallons
    # 
    # gallons_per_hour = 315.4
    # pounds_per_hour = gallons_per_hour * gallons_to_pounds
    gallons_per_minute = gallons_per_hour / 60
    pounds_per_minute = pounds_per_hour / 60
    gallons_per_minute_total = gallons_per_minute*engine_count
    gallons_per_hour_total = gallons_per_hour*engine_count
    pounds_per_minute_total = pounds_per_minute*engine_count
    pounds_per_hour_total = pounds_per_hour*engine_count
    print(f"gph= {gallons_per_hour} (1x) lb/min= {pounds_per_minute_total:0.0f} lb/hr= {pounds_per_hour_total:0.0f}")
# aviation_fuel_consumption_converter()
def aviation_fuel_calculator1():
    # enter parameter values here ...
    # route requires per line fix data in the following order (name distance ground_speed true_airspeed altitude)
    # on flight level changes, calculate approximate calibrated airspeed by taking the highest altitude between the two fixes and using it in (https://aerotoolbox.com/airspeed-conversions/)
    # weight fuel value represents weight at takeoff
    # weight payload includes crew/passenger weight excluding fuel
    aircraft_type = 'C-32B'
    weight_fuel = 12385+4891.55
    weight_payload = 600
    idling_minutes = 15
    altitude_departure = 650
    speed_liftoff = 160
    route ="""
    SALVE 43.5 303 294 18000
    KUSSO 7.5  346 346 19000
    TRRCH 6.5  331 331 20000
    JAYXX 26.7 387 387 29000
    -TOC- 37.7 450 450 39000
    TRYTN 46.9 465 465 39000
    LOOSE 62.4 505 465 39000
    -TOD- 655.7 510 465 39000
    GVE   113.9 510 465 0
    BOOYA 44.1 499 448 0
    BUKYY 34.2 471 420 0
    JAYBO 35.0 459 398 0
    HEDGE 9.0  435 377 0
    CANNY 12.6 395 371 0
    ESSSO 13.4 354 362 0
    PAATS 7.5  365 352 0
    RANSM 16.6 343 347 0
    WOJIK 20.0 313 284 0
    PSOUT 7.4  279 347 0
    MKORD 3.0  266 260 0
    CISON 8.1  261 257 2000
    FENKA 2.0  251 251 2000
    KWRI  6.4  150 150 130

    """
    route="""
    MESCA 26.0  300 312 15200
    NOCHI 38.1  377 375 27000
    TOC   35.9  445 445 35000
    ELP   142.1 479 450 35000
    INK   155.3 500 450 35000
    GEEKY 173.0 525 450 35000
    SNGGL 46.3  485 411 24000
    NNJUH 19.0  444 387 20000
    DARRB 35.1  376 321 12000
    GRCIA 5.0   352 316 11000
    BOOVE 9.6   318 284 9000
    ISABL 7.9   276 249 7000
    HOKAG 6.8   227 209 3000
    WEGTO 5.3   182 176 2500
    KNFW  6.6   155 155 650
    """
    # 
    # 
    # 
    fuel_consumption = util.file_read_json('c:\\projects\\applications\\flightgear\\fuel-consumption.json')
    aircraft_fuel_consumption = fuel_consumption[aircraft_type]
    entries_ground = aircraft_fuel_consumption['Ground']
    entries_ascent = aircraft_fuel_consumption['Ascent']
    entries_descent = aircraft_fuel_consumption['Descent']
    entries_cruise = aircraft_fuel_consumption['Cruise']
    def flight_level_changed(entries, altitude, speed, rate, weight, log = False):
        altitude_range = [0, 0]
        rate_range = [0, 0]
        matrix01 = [[[[0,0],[0,0]],[[0,0],[0,0]]],[[[0,0],[0,0]],[[0,0],[0,0]]]] # 1D=weight 2D=altitude 3D=rate 4D=speed
        matrix1 = [[[[0,0],[0,0]],[[0,0],[0,0]]],[[[0,0],[0,0]],[[0,0],[0,0]]]] # 1D=weight 2D=altitude 3D=rate 4D=speed
        matrix2 = [[[0,0],[0,0]],[[0,0],[0,0]]] # 1D=weight 2D=altitude 3D=rate
        matrix3 = [[0,0],[0,0]] # 1D=weight 2D=altitude
        matrix4 = [0,0] # 1D=weight
        # [[[[W1A1R1S1,W1A1R1S2],[W1A1R2S1,W1A1R2S2]],[[W1A2R1S1,W1A2R1S2],[W1A2R2S1,W1A2R2S2]]],[[[W2A1R1S1,W2A1R1S2],[W2A1R2S1,W2A1R2S2]],[[W2A2R1S1,W2A2R1S2],[W2A2R2S1,W2A2R2S2]]]]
        # [[[[ 0 0 0 0, 0 0 0 1],[ 0 0 1 0, 0 0 1 1]],[[ 0 1 0 0, 0 1 0 1],[ 0 1 1 0, 0 1 1 1]]],[[[ 1 0 0 0, 1 0 0 1],[ 1 0 1 0, 1 0 1 1]],[[ 1 1 0 0, 1 1 0 1],[ 1 1 1 0, 1 1 1 1]]]]
        # locate adjacent altitudes and rates
        for index, entry in enumerate(entries):
            if index == 0: continue
            if (entries[index-1]['Altitude'] <= altitude and altitude <= entries[index]['Altitude']):
                altitude_range = [entries[index-1]['Altitude'], entries[index]['Altitude']]
            if (entries[index-1]['Rate'] <= rate and rate <= entries[index]['Rate']):
                rate_range = [entries[index-1]['Rate'], entries[index]['Rate']]
        if log: print(f"ALT={altitude:.0f} SPD={speed:.0f} RATE={rate:.0f} ALT-RNG={altitude_range} RATE-RNG={rate_range}")
        if rate < 1000: rate_range = [0, 1000]
        # locate applicable entry speeds that correlate with given altitude and speed
        # store entry's fuel pounds per matching (altitude/speed/rate/weight) parameters
        for w in range(2):
            for a in range(2):
                for r in range(2):
                    for aIndex, aEntry in enumerate(entries):
                        for bIndex, bEntry in enumerate(entries):
                            if aIndex == bIndex: continue
                            if not (aEntry['Altitude'] == altitude_range[a] and bEntry['Altitude'] == altitude_range[a]): continue
                            if not (aEntry['Rate'] == rate_range[r] and bEntry['Rate'] == rate_range[r]): continue
                            if not (aEntry['Weight'] == w and bEntry['Weight'] == w): continue
                            if (aEntry['Speed'] <= speed and speed <= bEntry['Speed']):
                                matrix01[w][a][r][0] = aEntry['Speed']
                                matrix1[w][a][r][0] = aEntry['Pounds']
                                matrix01[w][a][r][1] = bEntry['Speed']
                                matrix1[w][a][r][1] = bEntry['Pounds']
                                # print(F"W{w+1}A{a+1}R{r+1}S1={aIndex} {aEntry['Speed']} {aEntry['Pounds']}")
                                # print(F"W{w+1}A{a+1}R{r+1}S2={bIndex} {bEntry['Speed']} {bEntry['Pounds']}")
        if rate < 1000:
            for w in range(2):
                for a in range(2):
                    for aIndex, aEntry in enumerate(entries_cruise):
                        for bIndex, bEntry in enumerate(entries_cruise):
                            if aIndex == bIndex: continue
                            if not (aEntry['Altitude'] == altitude_range[a] and bEntry['Altitude'] == altitude_range[a]): continue
                            if not (aEntry['Weight'] == w and bEntry['Weight'] == w): continue
                            if (aEntry['Speed'] <= speed and speed <= bEntry['Speed']):
                                matrix01[w][a][0][0] = aEntry['Speed']
                                matrix1[w][a][0][0] = aEntry['Pounds']
                                matrix01[w][a][0][1] = bEntry['Speed']
                                matrix1[w][a][0][1] = bEntry['Pounds']
                                # print(F"W{w+1}A{a+1}R1S1={aIndex} {aEntry['Speed']} {aEntry['Pounds']}")
                                # print(F"W{w+1}A{a+1}R1S2={bIndex} {bEntry['Speed']} {bEntry['Pounds']}")
        if log: print(f"matrix01=", matrix01)
        if log: print(f"matrix1=", matrix1)
        # missing data in matrix1
        missing_data = ""
        for w in range(2):
            for a in range(2):
                for r in range(2):
                    if matrix01[w][a][r][0] == 0: missing_data += f"W{w+1}A{a+1}R{r+1}S1 "
                    if matrix01[w][a][r][1] == 0: missing_data += f"W{w+1}A{a+1}R{r+1}S2 "
        if missing_data:
            print("Error: matrix1 missing data")
            print(f"FLC ALT={altitude:.0f} SPD={speed:.0f} RATE={rate:.0f} ALT-RNG={altitude_range} RATE-RNG={rate_range}", missing_data)
        # calculate pounds using proportionals of parameters (speed/rate/altitude/weight)
        # 1. determine difference between lowest and highest parameter in matrix
        # 2. determine difference between matrix lowest parameter and aircraft parameter
        # 3. calculate the proportion and apply to pounds
        # proportion parameter - speed
        for w in range(2):
            for a in range(2):
                for r in range(2):
                    lowest = min(matrix1[w][a][r][0], matrix1[w][a][r][1])
                    highest = max(matrix1[w][a][r][0], matrix1[w][a][r][1])
                    matrix2[w][a][r] = lowest + (abs(matrix1[w][a][r][1] - matrix1[w][a][r][0]) * ((speed - matrix01[w][a][r][0]) / (matrix01[w][a][r][1] - matrix01[w][a][r][0])))
        if log: print(f"matrix2=", matrix2)
        # proportion parameter - rate
        for w in range(2):
            for a in range(2):
                lowest = min(matrix2[w][a][0], matrix2[w][a][1])
                highest = max(matrix2[w][a][0], matrix2[w][a][1])
                matrix3[w][a] = lowest + (abs(matrix2[w][a][1] - matrix2[w][a][0]) * ((rate - rate_range[0]) / (rate_range[1] - rate_range[0])))
        if log: print(f"matrix3=", matrix3)
        # proportion parameter - altitude
        for w in range(2):
            lowest = min(matrix3[w][0], matrix3[w][1])
            highest = max(matrix3[w][0], matrix3[w][1])
            matrix4[w] = lowest + (abs(matrix3[w][1] - matrix3[w][0]) * ((altitude - altitude_range[0]) / (altitude_range[1] - altitude_range[0])))
        if log: print(f"matrix4=", matrix4)
        # proportion parameter - weight
        lowest = min(matrix4[0], matrix4[1])
        highest = max(matrix4[0], matrix4[1])
        pounds = lowest + (abs(matrix4[1] - matrix4[0]) * weight)
        if log: print(f"pounds={pounds:.0f}\n")
        return round(pounds)
    def flight_level_unchanged(entries, altitude, speed, weight, log = False):
        altitude_range = [0, 0]
        matrix01 = [[[0,0],[0,0]],[[0,0],[0,0]]] # 1D=weight 2D=altitude 3D=speed
        matrix1 = [[[0,0],[0,0]],[[0,0],[0,0]]] # 1D=weight 2D=altitude 3D=speed
        matrix2 = [[0,0],[0,0]] # 1D=weight 2D=altitude
        matrix3 = [0,0] # 1D=weight
        # [[[W1A1S1,W1A1S2],[W1A2S1,W1A2S2]],[[W2A1S1,W2A1S2],[W2A2S1,W2A2S2]]]
        # [[[ 0 0 0, 0 0 1],[ 0 1 0, 0 1 1]],[[ 1 0 0, 1 0 1],[ 1 1 0, 1 1 1]]]
        # locate adjacent altitudes
        for index, entry in enumerate(entries):
            if index == 0: continue
            if (entries[index-1]['Altitude'] <= altitude and altitude <= entries[index]['Altitude']):
                altitude_range = [entries[index-1]['Altitude'], entries[index]['Altitude']]
        if log: print(f"ALT={altitude:.0f} SPD={speed:.0f} ALT-RNG={altitude_range}")
        # locate applicable entry speeds that correlate with given altitude 
        # store entry's fuel pounds per matching (altitude/speed/weight) parameters
        for w in range(2):
            for a in range(2):
                for aIndex, aEntry in enumerate(entries):
                    for bIndex, bEntry in enumerate(entries):
                        if aIndex == bIndex: continue
                        if not (aEntry['Altitude'] == altitude_range[a] and bEntry['Altitude'] == altitude_range[a]): continue
                        if not (aEntry['Weight'] == w and bEntry['Weight'] == w): continue
                        if (aEntry['Speed'] <= speed and speed <= bEntry['Speed']):
                            matrix01[w][a][0] = aEntry['Speed']
                            matrix1[w][a][0] = aEntry['Pounds']
                            matrix01[w][a][1] = bEntry['Speed']
                            matrix1[w][a][1] = bEntry['Pounds']
                            # print(F"W{w+1}A{a+1}S1={aIndex} {aEntry['Speed']} {aEntry['Pounds']}")
                            # print(F"W{w+1}A{a+1}S2={bIndex} {bEntry['Speed']} {bEntry['Pounds']}")
        if log: print(f"matrix01=", matrix01)
        if log: print(f"matrix1=", matrix1)
        # missing data in matrix1
        missing_data = ""
        for w in range(2):
            for a in range(2):
                if matrix01[w][a][0] == 0: missing_data += f"W{w+1}A{a+1}S1 "
                if matrix01[w][a][1] == 0: missing_data += f"W{w+1}A{a+1}S2 "
        if missing_data:
            print("Error: matrix1 missing data")
            print(f"FLUC ALT={altitude:.0f} SPD={speed:.0f} ALT-RNG={altitude_range}", missing_data)
        # calculate pounds using proportionals of parameters (speed/rate/altitude/weight)
        # 1. determine difference between lowest and highest parameter in matrix
        # 2. determine difference between matrix lowest parameter and aircraft parameter
        # 3. calculate the proportion and apply to pounds
        # proportion parameter - speed
        for w in range(2):
            for a in range(2):
                lowest = min(matrix1[w][a][0], matrix1[w][a][1])
                highest = max(matrix1[w][a][0], matrix1[w][a][1])
                matrix2[w][a] = lowest + (abs(matrix1[w][a][1] - matrix1[w][a][0]) * ((speed - matrix01[w][a][0]) / (matrix01[w][a][1] - matrix01[w][a][0])))
        if log: print(f"matrix2=", matrix2)
        # proportion parameter - altitude
        for w in range(2):
            lowest = min(matrix2[w][0], matrix2[w][1])
            highest = max(matrix2[w][0], matrix2[w][1])
            matrix3[w] = lowest + (abs(matrix2[w][1] - matrix2[w][0]) * ((altitude - altitude_range[0]) / (altitude_range[1] - altitude_range[0])))
        if log: print(f"matrix3=", matrix3)
        # proportion parameter - weight
        lowest = min(matrix3[0], matrix3[1])
        highest = max(matrix3[0], matrix3[1])
        pounds = lowest + (abs(matrix3[1] - matrix3[0]) * weight)
        if log: print(f"pounds={pounds:.0f}\n")
        return round(pounds)
    def _flight_level_unchanged(entries, altitude, speed, weight, log = False):
        altitude_range = [0, 0]
        matrix01 = [[[0,0],[0,0]], [[0,0],[0,0]]] # 1D=altitude 2D=speed, 3D=weight [[[A1S1W1, A1S1W2], [A1S2W1, A1S2W2]], [[A2S1W1, A2S1W2], [A2S2W1, A2S2W2]]]
        matrix1 = [[[0,0],[0,0]], [[0,0],[0,0]]] # 1D=altitude 2D=speed, 3D=weight [[[A1S1W1, A1S1W2], [A1S2W1, A1S2W2]], [[A2S1W1, A2S1W2], [A2S2W1, A2S2W2]]]
        matrix02 = [[0,0],[0,0]] # 1D=altitude 2D=speed [[A1S1, A1S2], [A2S1, A2S2]]
        matrix2 = [[0,0],[0,0]] # 1D=altitude 2D=speed [[A1S1, A1S2], [A2S1, A2S2]]
        matrix3 = [[0],[0]] # 1D=altitude [A1, A2]
        # locate adjacent altitudes
        for index, entry in enumerate(entries):
            if index == 0: continue
            if (entries[index-1]['Altitude'] <= altitude and altitude <= entries[index]['Altitude']):
                altitude_range = [entries[index-1]['Altitude'], entries[index]['Altitude']]
        if log: print(f"alt={altitude:.0f} spd={speed:.0f}", altitude_range)
        # locate applicable entry speeds that correlate with given altitude and speed
        # store entry's fuel pounds per matching (altitude/speed/weight) parameters
        for index, entry in enumerate(entries):
            if index == 0: continue
            for a in range(2):
                for w in range(2):
                    if entries[index]['Altitude'] == altitude_range[a] and entries[index]['Weight'] == w and (entries[index-1]['Speed'] <= speed and speed <= entries[index]['Speed']):
                        matrix01[a][0][w] = entries[index-1]['Speed']
                        matrix1[a][0][w] = entries[index-1]['Pounds']
                        matrix01[a][1][w] = entries[index]['Speed']
                        matrix1[a][1][w] = entries[index]['Pounds']
        if log: print(f"matrix01=[[[A1S1W1, A1S1W2], [A1S2W1, A1S2W2]], [[A2S1W1, A2S1W2], [A2S2W1, A2S2W2]]]", matrix01)
        if log: print(f"matrix1=[[[A1S1W1, A1S1W2], [A1S2W1, A1S2W2]], [[A2S1W1, A2S1W2], [A2S2W1, A2S2W2]]]", matrix1)
        for a in range(2):
            for s in range(2):
                if matrix1[a][s][0] == 0 or matrix1[a][s][1] == 0:
                    print("Error: matrix1 missing data")
                    print(f"{altitude:.0f}", f"{speed:.0f}", altitude_range)
                    print(f"matrix01=[[[A1S1W1, A1S1W2], [A1S2W1, A1S2W2]], [[A2S1W1, A2S1W2], [A2S2W1, A2S2W2]]]", matrix01)
        # use aircraft weight capacity proportion to calculate an aligning fuel weight proportional valve
        for a in range(2):
            for s in range(2):
                matrix02[a][s] = matrix01[a][s][0] + ((matrix01[a][s][1] - matrix01[a][s][0]) * weight)
                matrix2[a][s] = matrix1[a][s][0] + ((matrix1[a][s][1] - matrix1[a][s][0]) * weight)
        if log: print(f"matrix02=[[A1S1, A1S2], [A2S1, A2S2]]", matrix02)
        if log: print(f"matrix2=[[A1S1, A1S2], [A2S1, A2S2]]", matrix2)
        # use aircraft speed proportion to calculate an aligning fuel weight proportional valve
        for a in range(2):
            matrix3[a] = matrix2[a][0] + ((matrix2[a][1] - matrix2[a][0]) * ((speed - matrix02[a][0]) / (matrix02[a][1] - matrix02[a][0])))
        if log: print(f"matrix3=[A1, A2]", matrix3)
        # use rate proportion to calculate an aligning fuel weight proportional valve
        if matrix3[0] == matrix3[1]:
            pounds = matrix3[0]
        else:
            pounds = matrix3[0] + ((matrix3[1] - matrix3[0]) * ((altitude - altitude_range[0]) / (altitude_range[1] - altitude_range[0])))
        if log: print(f"pounds={pounds:.0f}\n")
        return round(pounds)
    
    def ground(time):
        matrix1 = []
        for entry in entries_ground:
            eThrottle = int(entry['Throttle'])
            ePounds = float(entry['Pounds'])
            if eThrottle < 15:
                matrix1 += [ePounds]
        pounds_mean = util.statistics_mean(matrix1)
        return pounds_mean * time
    def ascent(altitude, speed, rate, weight):
        return flight_level_changed(entries_ascent, altitude, speed, rate, weight)
    def descent(altitude, speed, rate, weight):
        return flight_level_changed(entries_descent, altitude, speed, rate, weight)
    def cruise(altitude, speed, weight):
        return flight_level_unchanged(entries_cruise, altitude, speed, weight)
    # enter aircraft characteristics here ...
    weight_fuel_maximum = aircraft_fuel_consumption['Characteristics']['Weight Fuel Maximum']
    weight_aircraft_empty = aircraft_fuel_consumption['Characteristics']['Weight Aircraft Empty']
    weight_aircraft_maximum = aircraft_fuel_consumption['Characteristics']['Weight Takeoff Maximum']
    # 
    # 
    # 
    weight_fuel_initial = weight_fuel
    weight_capacity = weight_aircraft_maximum - weight_aircraft_empty
    weight_gross = weight_aircraft_empty + weight_payload + weight_fuel
    weight_capacity_proportion = (weight_payload + weight_fuel) / weight_capacity
    # 
    altitude = altitude_departure
    distance = 0
    speed = speed_liftoff
    time = 0
    weight_fuel_required = 0
    fixes = [line.split() for line in route.splitlines() if line.strip(' ')]
    for fix in fixes:
        fix_name = fix[0]
        fix_distance = float(fix[1])
        fix_ground_speed = int(fix[2])
        fix_true_airspeed = int(fix[3])
        fix_altitude = int(fix[4])
        altitude_difference = fix_altitude - altitude
        speed_difference = fix_true_airspeed - speed
        minutes_to_fix = (fix_distance / fix_ground_speed) * 60
        feet_per_minute = abs(altitude_difference) / minutes_to_fix
        knots_per_minute = abs(speed_difference) / minutes_to_fix
        weight_fuel_per_minute_to_fix = 0
        phase = ''
        for i in range(round(minutes_to_fix)):
            if speed_difference > 0:
                speed += knots_per_minute
            if speed_difference < 0:
                speed -= knots_per_minute
            if altitude_difference > 0:
                phase = 'A'
                altitude += feet_per_minute
                weight_fuel_per_minute = ascent(altitude, speed, feet_per_minute, weight_capacity_proportion)
            if altitude_difference == 0:
                phase = 'C'
                weight_fuel_per_minute = cruise(altitude, speed, weight_capacity_proportion)
            if altitude_difference < 0:
                phase = 'D'
                altitude -= feet_per_minute
                weight_fuel_per_minute = descent(altitude, speed, feet_per_minute, weight_capacity_proportion)
            weight_fuel_per_minute_to_fix += weight_fuel_per_minute
            weight_fuel -= weight_fuel_per_minute
            if weight_fuel < 0: return print('Error: initial fuel weight insufficient')
            weight_fuel_required += weight_fuel_per_minute
            weight_capacity_proportion = (weight_payload + weight_fuel) / weight_capacity
        # weight_fuel_per_minute_to_fix /= round(minutes_to_fix)
        print(f"to {fix_name.ljust(5, ' ')} {fix_altitude:05.0f}FT {fix_true_airspeed:03.0f}kn/TAS {feet_per_minute:04.0f}FPM/{phase} {minutes_to_fix:03.0f}MIN {weight_fuel_per_minute_to_fix:05.0f}LB {weight_fuel:05.0F}LB")
        altitude = fix_altitude
        distance += fix_distance
        speed = fix_true_airspeed
        time += minutes_to_fix
    weight_gross_final = weight_aircraft_empty + weight_payload + weight_fuel
    weight_gross_initial = weight_gross_final + weight_fuel_required
    load_weight_initial = ((weight_gross_initial - weight_aircraft_empty) / weight_capacity) * 100
    weight_fuel_ground = ground(idling_minutes)
    # print(weight_gross_initial, weight_gross_final)
    print(f"time={time:.0f}min distance={distance:.1f}nm\ngross-weight-initial={weight_gross_initial:.0f}lb weight-fuel-initial={weight_fuel_initial:.0f}lb weight-payload={weight_payload:.0f}lb load-initial={load_weight_initial:03.0f}%\nfuel-weight-ground={weight_fuel_ground:.0f}lb fuel-weight-takeoff={weight_fuel_initial-weight_fuel_ground:.0f}lb fuel-weight-flight={weight_fuel_required}lb fuel-weight-total={weight_fuel_required+weight_fuel_ground:.0f}lb")
# aviation_fuel_calculator1()
def aviation_fuel_calculator2():
    aircraft_type = 'E-8R'
    weight_fuel_intitial = 29000
    time_flight_hours = 1
    time_flight_minutes = 23
    time_hold_minutes = 30
    time_ground_departure = 15
    time_ground_destination = 15
    # 
    fuel_consumption = util.file_read_json('c:\\projects\\applications\\flightgear\\fuel-consumption.json')
    aircraft_fuel_consumption = fuel_consumption[aircraft_type]
    pounds_per_hour = aircraft_fuel_consumption['Characteristics']['lb/hr']
    def ground(time):
        matrix1 = []
        for entry in aircraft_fuel_consumption['Ground']:
            eThrottle = int(entry['Throttle'])
            ePounds = float(entry['Pounds'])
            if eThrottle < 15:
                matrix1 += [ePounds]
        pounds_mean = util.statistics_mean(matrix1)
        return pounds_mean * time
    # 
    weight_fuel_ground = ground(time_ground_departure) + ground(time_ground_destination)
    weight_fuel_flight = pounds_per_hour * (time_flight_hours + (time_flight_minutes / 60))
    weight_fuel_hold = pounds_per_hour * (time_hold_minutes / 60)
    time_fuel_intitial_hours = math.floor(weight_fuel_intitial / pounds_per_hour)
    time_fuel_intitial_minutes = ((weight_fuel_intitial / pounds_per_hour) - time_fuel_intitial_hours) * 60
    weight_fuel_total = weight_fuel_ground + weight_fuel_flight + weight_fuel_hold
    # time-fuel-intitial={time_fuel_intitial_hours:02.0f}{time_fuel_intitial_minutes:02.0f} 
    print(f"weight-fuel-ground={weight_fuel_ground:.0f}LB weight-fuel-flight={weight_fuel_flight:.0f}LB weight-fuel-hold={weight_fuel_hold:.0f}LB weight-fuel-total={weight_fuel_total:.0f}LB")
# aviation_fuel_calculator2()
def aviation_fuel_calculator3():
    # update variables here...
    aircraft_type = 'C-32B'
    weight_fuel_intitial = 29000
    altitude_cruise = 35000
    altitude_hold = 2100
    time_flight_hours = 1
    time_flight_minutes = 23
    time_hold_minutes = 30
    time_ground_departure = 15
    time_ground_destination = 15
    # 
    fuel_consumption = util.file_read_json('c:\\projects\\applications\\flightgear\\fuel-consumption.json')
    altitudes = [0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000]
    # altitudes = altitudes[:altitudes.index(altitude_cruise)+1]
    altitude_range_cruise = []
    for index, altitude in enumerate(altitudes):
        if index == 0: continue
        if altitudes[index-1] <= altitude_cruise and altitude_cruise <= altitudes[index]: altitude_range_cruise = [altitudes[index-1], altitudes[index]]
    altitude_range_hold = []
    for index, altitude in enumerate(altitudes):
        if index == 0: continue
        if altitudes[index-1] <= altitude_hold and altitude_hold <= altitudes[index]: altitude_range_hold = [altitudes[index-1], altitudes[index]]
    def ground(minutes):
        matrix1 = []
        for entry in fuel_consumption[aircraft_type]['Ground']:
            eThrottle = int(entry['Throttle'])
            ePounds = float(entry['Pounds'])
            if eThrottle < 15:
                matrix1 += [ePounds]
        pounds_mean = util.statistics_mean(matrix1)
        return pounds_mean * minutes
    def cruise(altitudes):
        matrix1 = [[[],[]] for i in range(len(altitudes))]
        matrix2 = [[] for i in range(len(altitudes))]
        for a, altitude in enumerate(altitudes):
            matrixS = [[],[]]
            for entry in (fuel_consumption[aircraft_type]['Cruise']):
                for w in range(2):
                    if entry['Altitude'] == altitude and entry['Weight'] == w:
                        matrix1[a][w] += [entry['Pounds']]
                        matrixS[w] += [entry['Speed']]
                
            w0 = math.ceil(util.statistics_mean(matrix1[a][0]))
            w1 = math.ceil(util.statistics_mean(matrix1[a][1]))
            # average weight
            avg = math.ceil(util.statistics_mean([w0, w1]))
            # print(f"ALT={altitude:05d} W0={w0} W1={w1} AVG={avg}")
            matrix2[a] = [w0, w1, avg]
        return math.ceil(util.statistics_mean([matrix2[a][2] for a in range(len(altitudes))]))
    pounds_per_hour = cruise(altitude_range_cruise)
    weight_fuel_flight = pounds_per_hour * (time_flight_hours + (time_flight_minutes / 60))
    weight_fuel_ground = ground(time_ground_departure) + ground(time_ground_destination)
    weight_fuel_hold = cruise(altitude_range_hold) * (time_hold_minutes / 60)
    time_fuel_intitial_hours = math.floor(weight_fuel_intitial / pounds_per_hour)
    time_fuel_intitial_minutes = ((weight_fuel_intitial / pounds_per_hour) - time_fuel_intitial_hours) * 60
    weight_fuel_total = weight_fuel_ground + weight_fuel_flight + weight_fuel_hold
    # time-fuel-intitial={time_fuel_intitial_hours:02.0f}{time_fuel_intitial_minutes:02.0f}
    print(f"weight-fuel-ground={weight_fuel_ground:.0f}LB weight-fuel-flight={weight_fuel_flight:.0f}LB weight-fuel-hold={weight_fuel_hold:.0f}LB weight-fuel-total={weight_fuel_total:.0f}LB")
# aviation_fuel_calculator3()
def aviation_fuel_calculator4():
    # update variables here...
    aircraft_type = 'C-32B'
    weight_fuel = 16513
    weight_payload = 600+0
    altitude_cruise = 36000
    altitude_hold = 3000
    speed_cruise = 470
    speed_hold = 200
    time_flight_hours = 1
    time_flight_minutes = 31
    time_hold_minutes = 30
    time_ground_departure = 15
    time_ground_destination = 15
    fuel_consumption = util.file_read_json('c:\\projects\\applications\\flightgear\\fuel-consumption.json')
    # 
    weight_fuel_initial = weight_fuel
    weight_fuel_ground = 0
    weight_fuel_flight = 0
    weight_fuel_hold = 0
    weight_capacity = fuel_consumption[aircraft_type]['Characteristics']['Weight Takeoff Maximum'] - fuel_consumption[aircraft_type]['Characteristics']['Weight Aircraft Empty']
    weight_gross = fuel_consumption[aircraft_type]['Characteristics']['Weight Aircraft Empty'] + weight_payload + weight_fuel
    weight_capacity_proportion = (weight_payload + weight_fuel) / weight_capacity
    time_flight_minutes_total = (time_flight_hours * 60) + time_flight_minutes
    # 
    def ground(minutes):
        matrix1 = []
        for entry in fuel_consumption[aircraft_type]['Ground']:
            eThrottle = int(entry['Throttle'])
            ePounds = float(entry['Pounds'])
            if eThrottle < 15:
                matrix1 += [ePounds]
        pounds_mean = util.statistics_mean(matrix1)
        return pounds_mean * minutes
    def cruise(altitude, speed, weight):
        matrixS = [[0,0],[0,0]]
        matrix1 = [[[0,0],[0,0]],[[0,0],[0,0]]]
        matrix2 = [[0,0],[0,0]]
        matrix3 = [0,0]
        altitude_range = []
        altitudes = [0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000]
        for index, altitude in enumerate(altitudes):
            if index == 0: continue
            if altitudes[index-1] <= altitude and altitude <= altitudes[index]: altitude_range = [altitudes[index-1], altitudes[index]]
        for w in range(2):
            for a in range(2):
                for entry in fuel_consumption[aircraft_type]['Cruise']:
                    if not entry['Altitude'] == altitude_range[a]: continue
                    if not entry['Weight'] == w: continue
                    s = 0 if entry['Speed'] <= speed else 1
                    matrix1[w][a][s] = entry['Pounds']
                    matrix1[w][a][s] = entry['Pounds']
                    matrixS[a][s] = entry['Speed']
        for w in range(2):
            for a in range(2):
                lowest = min(matrix1[w][a][0], matrix1[w][a][1])
                highest = max(matrix1[w][a][0], matrix1[w][a][1])
                matrix2[w][a] = lowest + (abs(matrix1[w][a][1] - matrix1[w][a][0]) * ((speed - matrixS[a][0]) / (matrixS[a][1] - matrixS[a][0])))
        for w in range(2):
            lowest = min(matrix2[w][0], matrix2[w][1])
            highest = max(matrix2[w][0], matrix2[w][1])
            matrix3[w] = lowest + (abs(matrix2[w][1] - matrix2[w][0]) * ((altitude - altitude_range[0]) / (altitude_range[1] - altitude_range[0])))
        lowest = min(matrix3[0], matrix3[1])
        highest = max(matrix3[0], matrix3[1])
        pounds_per_hour = lowest + (abs(matrix3[1] - matrix3[0]) * weight)
        pounds_per_minute = pounds_per_hour / 60
        return pounds_per_minute
    if weight_fuel > fuel_consumption[aircraft_type]['Characteristics']['Weight Fuel Maximum']:
        return print('Error: initial fuel incapatible')
    for minutes in range(time_flight_minutes_total):
        weight_fuel_per_minute = cruise(altitude_cruise, speed_cruise, weight_capacity_proportion)
        weight_fuel -= weight_fuel_per_minute
        weight_fuel_flight += weight_fuel_per_minute
        if weight_fuel < 0: return print('Error: initial fuel insufficient')
        weight_capacity_proportion = (weight_payload + weight_fuel) / weight_capacity
    for minutes in range(time_hold_minutes):
        weight_fuel_per_minute = cruise(altitude_hold, speed_hold, weight_capacity_proportion)
        weight_fuel -= weight_fuel_per_minute
        weight_fuel_hold += weight_fuel_per_minute
        if weight_fuel < 0: return print('Error: initial fuel insufficient')
        weight_capacity_proportion = (weight_payload + weight_fuel) / weight_capacity
    weight_fuel_ground = ground(time_ground_departure) + ground(time_ground_destination)
    weight_fuel_total = weight_fuel_ground + weight_fuel_flight + weight_fuel_hold
    print(f"weight-fuel-ground={weight_fuel_ground:.0f}LB weight-fuel-flight={weight_fuel_flight:.0f}LB weight-fuel-hold={weight_fuel_hold:.0f}LB weight-fuel-total={weight_fuel_total:.0f}LB")
# aviation_fuel_calculator4()
def aviation_averege_fuel_consumption_rate():
    aircraft_type = 'E-8R'
    fuel_consumption = util.file_read_json('c:\\projects\\applications\\flightgear\\fuel-consumption.json')
    altitudes = [0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000]
    matrix1 = [[[],[]] for i in range(len(altitudes))]
    matrix2 = [[] for i in range(len(altitudes))]
    for a, altitude in enumerate(altitudes):
        matrixS = [[],[]]
        for entry in (fuel_consumption[aircraft_type]['Cruise']):
            for w in range(2):
                if entry['Altitude'] == altitude and entry['Weight'] == w:
                    matrix1[a][w] += [entry['Pounds']]
                    matrixS[w] += [entry['Speed']]
        w0 = math.ceil(util.statistics_mean(matrix1[a][0]))
        w1 = math.ceil(util.statistics_mean(matrix1[a][1]))
        # average weight
        avg = math.ceil(util.statistics_mean([w0, w1]))
        print(f"ALT={altitude:05d} W0={w0:05d} W1={w1:05d} AVG={avg:05d}")
        matrix2[a] = [w0, w1, avg]
    pounds_per_hour = math.ceil(util.statistics_mean([matrix2[a][2] for a in range(len(altitudes))]))
    print(f"{aircraft_type} avg. lb/hr={pounds_per_hour}")
# aviation_averege_fuel_consumption_rate()
"""
C-32B Cruise VS1 Heavy == VS1 Light
            { "Altitude":     0, "Speed": 174, "Weight": 1, "Pounds":  4239 },
            { "Altitude":     0, "Speed": 357, "Weight": 1, "Pounds": 12158 },
            { "Altitude":  5000, "Speed": 190, "Weight": 1, "Pounds":  4301 },
            { "Altitude":  5000, "Speed": 371, "Weight": 1, "Pounds": 11806 },
            { "Altitude": 10000, "Speed": 209, "Weight": 1, "Pounds":  4369 },
            { "Altitude": 10000, "Speed": 387, "Weight": 1, "Pounds": 11416 },
            { "Altitude": 15000, "Speed": 232, "Weight": 1, "Pounds":  4482 },
            { "Altitude": 15000, "Speed": 405, "Weight": 1, "Pounds": 11025 },
            { "Altitude": 20000, "Speed": 258, "Weight": 1, "Pounds":  4621 },
            { "Altitude": 20000, "Speed": 424, "Weight": 1, "Pounds": 10652 },
            { "Altitude": 25000, "Speed": 286, "Weight": 1, "Pounds":  4801 },
            { "Altitude": 25000, "Speed": 445, "Weight": 1, "Pounds": 10302 },
            { "Altitude": 30000, "Speed": 318, "Weight": 1, "Pounds":  5013 },
            { "Altitude": 30000, "Speed": 468, "Weight": 1, "Pounds":  9984 },
            { "Altitude": 35000, "Speed": 353, "Weight": 1, "Pounds":  5266 },
            { "Altitude": 35000, "Speed": 474, "Weight": 1, "Pounds":  9153 },
            { "Altitude": 40000, "Speed": 394, "Weight": 1, "Pounds":  5662 },
            { "Altitude": 40000, "Speed": 477, "Weight": 1, "Pounds":  7809 }

C-32B Cruise VS1 Heavy == VS1 Heavy
            { "Altitude":     0, "Speed": 214, "Weight": 1, "Pounds":  4829 },
            { "Altitude":     0, "Speed": 357, "Weight": 1, "Pounds": 12158 },
            { "Altitude":  5000, "Speed": 233, "Weight": 1, "Pounds":  5005 },
            { "Altitude":  5000, "Speed": 371, "Weight": 1, "Pounds": 11806 },
            { "Altitude": 10000, "Speed": 256, "Weight": 1, "Pounds":  5240 },
            { "Altitude": 10000, "Speed": 387, "Weight": 1, "Pounds": 11416 },
            { "Altitude": 15000, "Speed": 281, "Weight": 1, "Pounds":  5483 },
            { "Altitude": 15000, "Speed": 405, "Weight": 1, "Pounds": 11025 },
            { "Altitude": 20000, "Speed": 310, "Weight": 1, "Pounds":  5743 },
            { "Altitude": 20000, "Speed": 424, "Weight": 1, "Pounds": 10652 },
            { "Altitude": 25000, "Speed": 342, "Weight": 1, "Pounds":  6071 },
            { "Altitude": 25000, "Speed": 445, "Weight": 1, "Pounds": 10302 },
            { "Altitude": 30000, "Speed": 378, "Weight": 1, "Pounds":  6435 },
            { "Altitude": 30000, "Speed": 468, "Weight": 1, "Pounds":  9984 },
            { "Altitude": 35000, "Speed": 416, "Weight": 1, "Pounds":  6818 },
            { "Altitude": 35000, "Speed": 474, "Weight": 1, "Pounds":  9153 },
            { "Altitude": 40000, "Speed": 460, "Weight": 1, "Pounds":  7299 },
            { "Altitude": 40000, "Speed": 477, "Weight": 1, "Pounds":  7809 }
"""
def aviation_descent_profile():
    a="""
    KDFW/BEREE3/HEDMN/POWND/006//
    049/120-120/210/
    060/120-130/240/
    068/130-150/270/
    075/150-170/270/
    093/200-230/290/
    113/240-300/290/
    KDFW/BOOVE7/BEONE/SNGGL/006//
    050/120-120/210/
    059/120-130/240/
    067/130-150/270/
    079/150-170/280/
    083/170-190/280/
    098/200-230/290/
    118/240-300/290/
    KDFW/SOCCK4/SOCKK/SNGGL/006//
    030/050-050/230/
    042/070-090/250/
    050/090-110/250/
    060/100-110/270/
    065/120-140/270/
    100/200-230/290/
    119/240-300/290/
    KDFW/SOCCK4/SOCKK/GUTZZ/006//
    030/050-050/230/
    042/070-090/250/
    050/090-110/250/
    060/100-110/270/
    065/120-140/270/
    100/200-230/290/
    112/240-300/290/
    KDFW/VRTRY2/POPPA/FAWNT/006//
    029/050-050/240/
    042/070-090/250/
    053/100-110/250/
    068/130-160/270/
    088/200-220/290/
    101/240-260/290/
    KDFW/VRTRY2/POPPA/TYPTN/006//
    029/050-050/240/
    042/070-090/250/
    053/100-110/250/
    064/130-160/270/
    079/170-190/290/
    101/200-230/290/
    109/240-300/290/
    KIAH/DRLLR5/SKLER/OILLL/001//
    040/060-060/210/
    053/080-100/240/
    064/110-130/XXX/
    074/130-160/250/
    085/160-190/280/
    100/200-240/XXX/
    110/220-260/XXX/
    120/240-320/280/
    KIAH/GESNR1/CASST/  AEX/001//
    012/060-060/210/
    021/070-070/240/
    032/080-100/240/
    047/100-110/250/
    058/130-160/280/
    071/170-200/280/
    091/220-270/280/
    109/240-300/XXX/
    KIAH/NNCEE2/CASST/GIRLY/001//
    012/060-060/210/
    017/060-060/240/
    032/060-060/XXX/
    037/060-070/XXX/
    051/100-120/250/
    059/120-120/XXX/
    072/120-150/XXX/
    084/170-200/280/
    102/200-290/280/
    KLAX/IRNMN2/GADDO/BURGL/001//
    015/060-060/XXX/
    018/060-060/210/
    023/070-080/210/
    028/080-090/XXX/
    034/090-120/240/
    045/120-130/250/
    052/120-160/XXX/
    059/140-170/XXX/
    066/160-200/XXX/
    075/190-230/XXX/
    081/200-240/XXX/
    088/230-270/280/
    100/260-290/XXX/
    KLAX/MDNYT2/SHIPM/HAKMN/001//
    014/070-070/210/
    021/080-100/230/
    031/100-120/XXX/
    050/100-130/XXX/
    058/130-140/XXX/
    062/XXX-150/XXX/
    068/140-170/XXX/
    082/190-230/XXX/
    097/240-290/280/
    114/270-320/XXX/
    125/290-320/XXX/
    KMCO/SNFLD3/CUBAL/LPERD/001//
    012/050-050/210/
    019/060-080/XXX/
    026/080-100/230/
    036/100-120/250/
    053/120-160/280/
    059/100-160/XXX/
    067/120-180/XXX/
    074/130-190/XXX/
    099/230-290/XXX/
    153/300-340/XXX/
    KPHX/BRUSR1/FOWLE/WOTRO/010//
    010/040-040/XXX/
    021/060-060/210/
    027/070-100/210/
    031/080-100/230/
    041/090-120/250/
    052/130-170/250/
    074/190-250/270/
    094/240-290/XXX/
    134/290-290/XXX/
    KPHX/EAGUL6/JAGAL/ZUN  /010//
    010/040-045/XXX/
    013/045-055/210/
    020/060-080/XXX/
    026/081-100/210/
    037/094-130/XXX/
    043/140-170/250/
    065/180-220/260/
    085/240-300/270/
    105/270-330/270/
    KPHX/HYDRR1/BALTE/BLH  /010//
    010/040-050/XXX/
    014/050-060/XXX/
    018/060-060/210/
    022/070-070/XXX/
    026/080-090/210/
    036/100-120/230/
    043/110-170/250/
    055/150-190/265/
    075/190-220/XXX/
    100/240-250/XXX/
    107/250-250/280/
    KPHX/PINNG1/GIPSE/DRRVR/010//
    010/040-050/XXX/
    014/050-060/XXX/
    026/080-090/210/
    036/100-120/230/
    046/130-150/250/
    064/170-190/270/
    083/220-250/280/
    093/250-280/280/
    """
    lines = [line for line in a.splitlines() if not len(line.strip(' ')) == 0]
    arrivals = []
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.endswith('//'):
            arrival = {  }
            _key_ = ''
            _index_ = 0
            arrival['airport'] = line[_index_:len(_key_)+line[_index_:].index('/')]
            _key_ = f"{arrival['airport']}/"
            _index_ = line.index(_key_)+len(_key_)
            arrival['name'] = line[_index_:len(_key_)+line[_index_:].index('/')]
            _key_ = f"{arrival['airport']}/{arrival['name']}/"
            _index_ = line.index(_key_)+len(_key_)
            arrival['waypoint-start'] = line[_index_:len(_key_)+line[_index_:].index('/')]
            _key_ = f"{arrival['airport']}/{arrival['name']}/{arrival['waypoint-start']}/"
            _index_ = line.index(_key_)+len(_key_)
            arrival['waypoint-end'] = line[_index_:len(_key_)+line[_index_:].index('/')]
            _key_ = f"{arrival['airport']}/{arrival['name']}/{arrival['waypoint-start']}/{arrival['waypoint-end']}/"
            _index_ = line.index(_key_)+len(_key_)
            arrival['elevation'] = line[_index_:len(_key_)+line[_index_:].index('/')]
            arrival['constraints'] = []
            arrivals.append(arrival)
        else:
            arrival = arrivals[-1]
            constraints: list = arrival['constraints']
            constraint = {  }
            _key_ = ''
            _index_ = 0
            constraint['distance'] = line[_index_:len(_key_)+line[_index_:].index('/')]
            _key_ = f"{constraint['distance']}/"
            _index_ = line.index(_key_)+len(_key_)
            constraint['altitude'] = line[_index_:len(_key_)+line[_index_:].index('/')]
            _key_ = f"{constraint['distance']}/{constraint['altitude']}/"
            constraint['altitude'] = constraint['altitude'].split('-')
            _index_ = line.index(_key_)+len(_key_)
            constraint['speed'] = line[_index_:len(_key_)+line[_index_:].index('/')]
            constraints.append(constraint)
        index += 1
    entries = []
    for miles in range(150, 0, -10):
        entries.append({ 'NM': miles, 'ALT': '', 'ALT-MIM': [], 'ALT-MAX': [], 'SPD': [] })
    def getEntry(distance: int) -> dict:
        for entry in entries:
            if entry['NM'] == distance:
                return entry
        return None
    for arrival in arrivals:
        constraints = arrival['constraints']
        elevation = int(arrival['elevation'])
        for constaint in constraints:
            distance = int(constaint['distance'])
            altitudeMin = constaint['altitude'][0] if constaint['altitude'][0] == 'XXX' else int(constaint['altitude'][0])
            altitudeMax = constaint['altitude'][1] if constaint['altitude'][1] == 'XXX' else int(constaint['altitude'][1])
            speed = constaint['speed'] if constaint['speed'] == 'XXX' else int(constaint['speed'])
            entry = getEntry(util.mathematics_round(distance, 2))
            entry['ALT-MIM'].append(altitudeMin)
            entry['ALT-MAX'].append(altitudeMax)
            entry['SPD'].append(speed)
    for entry in entries:
        distance = entry['NM']
        altitudeMin = [val for val in entry['ALT-MIM'] if not val == 'XXX']
        altitudeMax = [val for val in entry['ALT-MAX'] if not val == 'XXX']
        speed = [val for val in entry['SPD'] if not val == 'XXX']
        # entry['ALT-MIM-MODE'] = 0 if len(altitudeMin) == 0 else util.statistics_mode(altitudeMin)
        # entry['ALT-MIM-MEAN'] = 0 if len(altitudeMin) == 0 else int(util.statistics_mean(altitudeMin))
        # entry['ALT-MIM-MEDN'] = 0 if len(altitudeMin) == 0 else util.statistics_median(altitudeMin)
        # entry['ALT-MIM'] = int(util.statistics_mean([entry['ALT-MIM-MODE'], entry['ALT-MIM-MEAN'], entry['ALT-MIM-MEDN']]))
        # del entry['ALT-MIM-MODE'], entry['ALT-MIM-MEAN'], entry['ALT-MIM-MEDN']
        # entry['ALT-MAX-MODE'] = 0 if len(altitudeMax) == 0 else util.statistics_mode(altitudeMax)
        # entry['ALT-MAX-MEAN'] = 0 if len(altitudeMax) == 0 else int(util.statistics_mean(altitudeMax))
        # entry['ALT-MAX-MEDN'] = 0 if len(altitudeMax) == 0 else util.statistics_median(altitudeMax)
        # entry['ALT-MAX'] = int(util.statistics_mean([entry['ALT-MAX-MODE'], entry['ALT-MAX-MEAN'], entry['ALT-MAX-MEDN']]))
        # del entry['ALT-MAX-MODE'], entry['ALT-MAX-MEAN'], entry['ALT-MAX-MEDN']
        # entry['ALT'] = f"{entry['ALT-MIM']:03d}-{entry['ALT-MAX']:03d}"
        # del entry['ALT-MIM'], entry['ALT-MAX']
        # entry['SPD-MODE'] = 0 if len(speed) == 0 else util.statistics_mode(speed)
        # entry['SPD-MEAN'] = 0 if len(speed) == 0 else int(util.statistics_mean(speed))
        # entry['SPD-MEDN'] = 0 if len(speed) == 0 else util.statistics_median(speed)
        # entry['SPD'] = int(util.statistics_mean([entry['SPD-MODE'], entry['SPD-MEAN'], entry['SPD-MEDN']]))
        # del entry['SPD-MODE'], entry['SPD-MEAN'], entry['SPD-MEDN']

        entry['ALT-MIM'] = 0 if len(altitudeMin) == 0 else int(util.statistics_median(altitudeMin))
        entry['ALT-MAX'] = 0 if len(altitudeMax) == 0 else int(util.statistics_median(altitudeMax))
        entry['ALT'] = f"{entry['ALT-MIM']:03d}-{entry['ALT-MAX']:03d}"
        del entry['ALT-MIM'], entry['ALT-MAX']
        entry['SPD'] = 0 if len(speed) == 0 else int(util.statistics_median(speed))
    print(util.table_encode(entries))
# aviation_descent_profile()
def aviation_flight_path_angle():
    flight_path_angle = 4
    groundspeed = 240
    feet_per_minute = 1828
    # 
    angleA = flight_path_angle*util.DEGREES_TO_RADIANS
    sideB = 6076.115
    sideC = sideB / math.cos(angleA)
    sideA = math.sqrt(sideC**2-sideB**2)
    feet_per_nautical_mile = sideA
    feet_per_minute_calculated = feet_per_nautical_mile * (groundspeed/60)
    # 
    sideA = feet_per_minute / (groundspeed/60)
    sideB = 6076.115
    sideC = math.sqrt(sideA**2+sideB**2)
    angleA = math.asin(sideA/sideC)*util.RADIANS_TO_DEGREES
    flight_path_angle_calculated = angleA
    print(f"feet_per_nautical_mile={feet_per_nautical_mile:03.0f}\nfeet_per_minute={feet_per_minute_calculated:04.0f}\nflight_path_angle={flight_path_angle_calculated:.0f}")
# aviation_flight_path_angle()
def aviation_pressure_and_density_altitude_formula():
    barometric_pressure = 29.92 # inches of mercury (inHg)
    elevation = 567 # feet
    outide_air_temperature = 28.3 # degrees Celsius
    # 
    pressure_altitude = (29.92 - barometric_pressure) * 1000 + elevation
    standard_air_temperature = (15 - (2 / 1000 * pressure_altitude)) # degrees Celsius
    density_altitude = pressure_altitude + (120 * (outide_air_temperature - standard_air_temperature))
    print(f"perssure-altitude = {pressure_altitude:.0f}")
    print(f"density-altitude = {density_altitude:.0f}")
    return density_altitude
# aviation_pressure_and_density_altitude_formula()
def aviation_runway_approach_line():
    p1=[36.247580, -115.024166] # runway start
    p2=[36.226694, -115.046803] # runway end
    length = 15 # nm
    azimuth = util.geographic_to_azimuth(p2, p1)
    print(f"approach-course={azimuth:.1f}")
    p3=util.geographic_to_destination_point(p1, azimuth, length*1852)
    print(f"{p1[0]:.6f} {p1[1]:.6f}")
    print(f"{p3[0]:.6f} {p3[1]:.6f}")
# aviation_runway_approach_line()
def aviation_standard_terminal_arrival():
    # entry.distance = distance to runway threshold
    # entry.elevation = airport AMSL altitude
    # enter parameters here...
    altitude_correction = False # true=altitude is height above airport, False=altitude is height above mean sea level
    # 
    data: str = util.file_read_string("c:\\projects\\applications\\flightgear\\standard-terminal-arrival.txt")
    lines = [line for line in data.splitlines() if not len(line) == 0]
    index = 0
    entries = []
    while index < len(lines):
        line: str = lines[index]
        if line.endswith('//'):
            entry = {  }
            key = f""
            indexStart = line.index(key)+len(key)
            entry['airport'] = line[indexStart:len(key)+line[indexStart:].index('/')]
            key = f"{entry['airport']}/"
            indexStart = line.index(key)+len(key)
            entry['name'] = line[indexStart:len(key)+line[indexStart:].index('/')]
            key = f"{entry['airport']}/{entry['name']}/"
            indexStart = line.index(key)+len(key)
            entry['waypoint_start'] = line[indexStart:len(key)+line[indexStart:].index('/')]
            key = f"{entry['airport']}/{entry['name']}/{entry['waypoint_start']}/"
            indexStart = line.index(key)+len(key)
            entry['waypoint_end'] = line[indexStart:len(key)+line[indexStart:].index('/')]
            key = f"{entry['airport']}/{entry['name']}/{entry['waypoint_start']}/{entry['waypoint_end']}/"
            indexStart = line.index(key)+len(key)
            entry['elevation'] = line[indexStart:len(key)+line[indexStart:].index('/')]
            # 
            entry['waypoint_start'] = entry['waypoint_start'].strip(' ')
            entry['waypoint_end'] = entry['waypoint_end'].strip(' ')
            entry['elevation'] = int(entry['elevation'])
            entry['constraints'] = []
            # 
            entries += [entry]
        else:
            constraint = {  }
            key = f""
            indexStart = line.index(key)+len(key)
            constraint['distance'] = line[indexStart:len(key)+line[indexStart:].index('/')]
            key = f"{constraint['distance']}/"
            indexStart = line.index(key)+len(key)
            constraint['altitude'] = line[indexStart:len(key)+line[indexStart:].index('/')]
            key = f"{constraint['distance']}/{constraint['altitude']}/"
            indexStart = line.index(key)+len(key)
            constraint['speed'] = line[indexStart:len(key)+line[indexStart:].index('/')]
            # 
            constraint['distance'] = int(constraint['distance'])
            constraint['altitude'] = constraint['altitude'].split('-')
            constraint['altitude'] = [None if constraint['altitude'][0] == 'XXX' else int(constraint['altitude'][0]), None if constraint['altitude'][1] == 'XXX' else int(constraint['altitude'][1])]

            constraint['speed'] = None if constraint['speed'] == 'XXX' else int(constraint['speed'])
            # 
            entries[-1]['constraints'] += [constraint]
        index += 1
    def getEntryconstraintsByDistance(distance: int) -> dict:
        constraints = []
        for entry in array(entries).copy():
            for constraint in entry['constraints']:
                if util.mathematics_round(constraint['distance'], 2) == distance:
                    altitude_correction_feet = entry['elevation'] if altitude_correction else 0
                    constraint['altitude'][0] = constraint['altitude'][0] if constraint['altitude'][0] == None else constraint['altitude'][0] - altitude_correction_feet
                    constraint['altitude'][1] = constraint['altitude'][1] if constraint['altitude'][1] == None else constraint['altitude'][1] - altitude_correction_feet
                    constraints.append(constraint)
        return constraints
    table = []
    for distance in range(200, 0, -10):
        altitude_range = [[],[]]
        speed_range = []
        for constraint in getEntryconstraintsByDistance(distance):
            altitude_range[0] += [constraint['altitude'][0]]
            altitude_range[1] += [constraint['altitude'][1]]
            speed_range += [constraint['speed']]
        altitude_range[0] = [value for value in altitude_range[0] if not value == None]
        altitude_range[1] = [value for value in altitude_range[1] if not value == None]
        speed_range = [value for value in speed_range if not value == None]
        altitude = [
            'XXX' if len(altitude_range[0]) == 0 else f"{int(util.statistics_mean(altitude_range[0])):03d}",
            'XXX' if len(altitude_range[1]) == 0 else f"{int(util.statistics_mean(altitude_range[1])):03d}",
        ]
        speed = 'XXX' if len(speed_range) == 0 else f"{int(util.statistics_mode(speed_range)):03d}"
        table += [{ "DIS": f"{distance:03d}", "ALT": f"{altitude[0]}-{altitude[1]}", "SPD": speed }]
    print(util.table_encode(table))
    """
    MEAN
    NM      ALT         SPD
    200     XXX-XXX     XXX
    190     XXX-XXX     XXX
    180     XXX-XXX     XXX
    170     XXX-XXX     XXX
    160     299-339     XXX
    150     XXX-XXX     XXX
    140     239-289     280
    130     221-246     280
    120     214-262     286
    110     214-249     283
    100     186-207     282
    90      166-204     273
    80      144-185     270
    70      118-136     262
    60      115-120     258
    50      088-097     236
    40      078-110     245
    30      059-065     223
    20      047-048     211
    10      032-042     210

    # MEDIAN
    NM      ALT         SPD
    200     XXX-XXX     XXX
    190     XXX-XXX     XXX
    180     XXX-XXX     XXX
    170     XXX-XXX     XXX
    160     299-339     XXX
    150     XXX-XXX     XXX
    140     239-289     280
    130     229-269     280
    120     226-294     290
    110     231-239     285
    100     194-224     290
    90      170-212     280
    80      139-184     270
    70      116-136     270
    60      114-124     265
    50      084-104     250
    40      079-109     250
    30      059-062     230
    20      049-049     210
    10      031-044     210

    # MODE
    NM      ALT         SPD
    200     XXX-XXX     XXX
    190     XXX-XXX     XXX
    180     XXX-XXX     XXX
    170     XXX-XXX     XXX
    160     299-339     XXX
    150     XXX-XXX     XXX
    140     239-289     280
    130     239-269     280
    120     234-294     290
    110     234-294     290
    100     194-224     290
    90      194-159     290
    80      144-164     270
    70      114-144     270
    60      114-124     270
    50      059-104     250
    40      064-084     250
    30      044-044     210
    20      049-049     210
    10      029-034     210
    """
# aviation_standard_terminal_arrival()
def aviation_visual_decent_point():
    # On RNAV approach charts, a waypoint indicaed distance is nautical miles from runway start
    # provided that the VDP's distance to runway, subtract the VDP and final fix navaid distance and add to the final fix distance from runway

    # use https://www.calculator.net/right-triangle-calculator.html
    # Set angle 'a' degrees to approach  GS angle and set side 'a' to fix before VDP altitude minus MDA. Calculate side 'b': distance from VDP to fix before VDP.
    # Substract indicated distance of fix before VDP from distance calculated at website = VDP distance from runway.
    # p1 = [float(coordinate) for coordinate in util.geographic_ddm_to_ddd("N32°04.43' W110°47.00'".split(' '))]
    p1 = [ 35.606667, -117.785000 ] # 1st fix before vdp
    rwy = [ 35.675416, -117.708646 ] # rwy start centerline
    p1_to_rwy_distance_indicated = 5.6
    vdp_to_rwy_distance_indicated = 1.84
    touchdown_zone_elevation = 59
    # KNID/03 35.675416, -117.708646 
    # KNID/32 35.676469, -117.679962
    # 3.768421467
    # 
    p1_to_rwy_azimuth_calculated = util.geographic_to_azimuth(p1, rwy)
    p1_to_rwy_distance_calculated = util.geographic_to_distance(p1, rwy)
    p1_to_rwy_distance_offset = p1_to_rwy_distance_calculated - p1_to_rwy_distance_indicated*1852
    vdp_to_rwy_distance_calculated = vdp_to_rwy_distance_indicated*1852 + p1_to_rwy_distance_offset
    p1_to_vdp_distance = p1_to_rwy_distance_calculated - vdp_to_rwy_distance_calculated
    vdp1 = util.geographic_to_destination_point(p1, p1_to_rwy_azimuth_calculated, p1_to_vdp_distance)
    vdp2 = util.geographic_to_destination_point(rwy, p1_to_rwy_azimuth_calculated+180%360, vdp_to_rwy_distance_calculated)
    vdp1_vdp2_azimuth = util.geographic_to_azimuth(vdp1, vdp2)
    vdp1_vdp2_distance = util.geographic_to_distance(vdp1, vdp2)
    vdp3 = util.geographic_to_destination_point(vdp1, vdp1_vdp2_azimuth, vdp1_vdp2_distance)

    print(F"p1_to_rwy_azimuth_calculated={p1_to_rwy_azimuth_calculated:.1f}")
    print(F"p1_to_rwy_distance_offset={p1_to_rwy_distance_offset:.0f}m")
    print(f"vdp_to_rwy_distance_calculated={vdp_to_rwy_distance_calculated/1852:.2f}nm")
    print(f"margin={vdp1_vdp2_distance:.1f}m")
    # print(f"VDP: {vdp1[0]:.6f} {vdp1[1]:.6f}")
    # print(f"VDP: {vdp2[0]:.6f} {vdp2[1]:.6f}")
    print(f"VDP: {vdp3[0]:.6f} {vdp3[1]:.6f}")
# aviation_visual_decent_point()

def correlation1():
    import numpy as np
    from scipy import stats
    a = 0
    b = 0

    array1 = np.array([103,98,92,88,85])
    array2 = np.array([a, 154,147,143,123])
    x = 170

    # Assuming 'a' and 'b' can be estimated 
    # (Replace 'a' and 'b' with initial estimates for the first two values in array2) 
    array2[0] = 160  # Example initial estimate for 'a'
    # array2[1] = 42  # Example initial estimate for 'b'

    # Calculate the slope and intercept
    slope, intercept, r_value, p_value, std_err = stats.linregress(array1, array2)

    # Print the results
    print("Slope:", slope)
    print("Intercept:", intercept)

    # Use the equation to refine the estimates for 'a' and 'b'
    a_predicted = slope * x + intercept
    # b_predicted = slope * 44 + intercept

    print("Estimated value for 'a':", a_predicted)
    # print("Estimated value for 'b':", b_predicted)
# correlation1()
def predict_next_number(data):
    # Predicts the next number in a sequence using linear regression.
    import numpy as np
    if len(data) < 2:
        return None  # Insufficient data for prediction
    # Create input and output arrays
    x = np.arange(len(data))
    y = np.array(data)
    # Calculate the correlation coefficient
    corr_coef = np.corrcoef(x, y)[0, 1]
    # Check for weak correlation
    correlation_threshold = 0.7  # Adjust as needed
    if abs(corr_coef) < correlation_threshold:
        print(f"Warning: Weak correlation ({corr_coef:.2f}). Prediction may be inaccurate.")
        return None
    # Calculate the slope and intercept of the regression line
    slope, intercept = np.polyfit(x, y, 1) 
    # Predict the next number
    next_x = len(data)
    predicted_next_number = slope * next_x + intercept
    return predicted_next_number
# print(predict_next_number([180,135,101,79,73]))
def correlation3():
    # number to predict will be next in list to right
    array1 = [22796,21268,19552,18560,17320,15456,11108,8968]
    array2 = [23336,21716,20172,19116,18112,16420,12265,10259] # predicting array
    x = 7480
    # x = predict_next_number(array1)
    # array1 = [x, 0, 0 ...]
    # array2 = [a, 0, 0, ...]
    # x: The value in array1 for which to find the corresponding value in array2.
    import numpy as np
    # Calculate the correlation coefficient
    corr_coef = np.corrcoef(array1, array2)[0, 1] 
    if abs(corr_coef) < 0.5:  # Adjust threshold as needed
        print("Warning: Weak correlation between arrays. Estimation may be inaccurate.")
        return None
    # Calculate the slope and intercept of the regression line
    slope, intercept = np.polyfit(array1, array2, 1) 
    # Estimate the corresponding value in array2
    estimated_value = slope * x + intercept
    print(f"Estimated value for 'a' in array2: {estimated_value:.2f}") 
    return estimated_value
# correlation3()
def correlation4():
    array1 = [85, 88, 92, 98, 103]
    array2 = [123, 143, 147, 154, 160, None]


    import numpy as np
    # Check for sufficient data
    if len(array1) != len(array2) - 1:
        print("Error: Array lengths do not match.")
        return None
    # Calculate the correlation coefficient
    corr_coef = np.corrcoef(array1, array2[:-1])[0, 1] 
    # Check for weak correlation
    correlation_threshold = 0.7  # Adjust as needed
    if abs(corr_coef) < correlation_threshold:
        print(f"Warning: Weak correlation ({corr_coef:.2f}). Prediction may be inaccurate.")
        return None
    # Calculate the slope and intercept of the regression line
    slope, intercept = np.polyfit(array1, array2[:-1], 1) 
    # Predict the next number 
    predicted_next_number = slope * array1[-1] + intercept
    print(predicted_next_number)
    return predicted_next_number
# correlation4()

def notes_object_format():
    keyLength = 10
    data="""
    """
    # 
    output = ''
    lines = data.splitlines()
    objectPairs: list[str] = []
    for line in lines:
        if line.strip(' ') == '': continue
        objectKey, objectValue = line.split(': ', 1)
        objectPairs.append([objectKey.strip(' '), objectValue.strip(' ')])
    objectPairs.sort(key=lambda objectPair : objectPair[0].lower())
    output = array([f"{objectPair[0].ljust(keyLength, ' ')}: {objectPair[1]}" for objectPair in objectPairs]).join('\n')
    print(output)
    app.copyToClipboard(output)
# notes_object_format()

def logic_gate_truth_table():
    type = 'IMPLY'
    inputCount = 2
    print(f"Logic Gate {type.upper()}\n{array([chr(index+65) for index in range(inputCount)]).join(' ')} X")
    for decimal in range(2**inputCount):
        binary = util.dec2bin(decimal, inputCount)
        inputs = [state == '1' for state in binary]
        output = '1' if util.get(f"logic_gate_{type.lower()}", inputs) else '0'
        print(*binary + output)
# logic_gate_truth_table()


# a="33.22684462,-78.99657918 33.17177201,-79.03781246"
# p1,p2=a.split(' ')
# p1lat, p1lng = p1.split(',')
# p2lat, p2lng = p2.split(',')
# print(f"{util.geographic_to_distance([float(p1lat), float(p1lng)], [float(p2lat), float(p2lng)]):.0f}")

# find arc center from two points
# p1 = [ 27.188627,89.439138 ] # 
# p2 = [ 27.229200,89.507702 ] # 
# midpoint = util.geographic_to_midpoint(p1, p2)
# azimuth = util.geographic_to_azimuth(p1, p2)
# azimuth_perpendicular = (util.geographic_to_azimuth(p1, p2)+90)%360
# print(f"azimuth-perpendicular: {azimuth_perpendicular}")
# print(f"{midpoint[0]:.6f} {midpoint[1]:.6f}")
# p3 = util.geographic_to_destination_point(midpoint, (azimuth+90)%360, 10*1852)
# p4 = util.geographic_to_destination_point(midpoint, (azimuth-90)%360, 10*1852)
# print(f"{p3[0]:.6f} {p3[1]:.6f}")
# print(f"{p4[0]:.6f} {p4[1]:.6f}")

# geographic coordinates dme waypoint
# p1 = [36.256218, -115.088702]
# p2 = [36.586310, -115.115825]
# p1 = [float(coord) for coord in "36.244667 -115.025000".strip(' ').split(' ')]
# p2 = [float(coord) for coord in "36.259586 -115.144237".strip(' ').split(' ')]
# azimuth = util.geographic_to_azimuth(p1, p2)
# distance_meters = util.geographic_to_distance(p1,p2)
# distance_nautical_miles = distance_meters/1852
# print(f"{azimuth:03.0f}°T {distance_meters:.0f}m {distance_nautical_miles:.1f}nm D{azimuth:03.0f}{chr(round(64+distance_nautical_miles))}")

# geographic coordinates dms to ddd formated
# p1 = [float(coord) for coord in util.geographic_dms_to_ddd("385134N 0770211W".strip(' ').split(' '))]
# print(f"{p1[0]:.6f} {p1[1]:.6f}")

# geographic coordinates ddd to dms formated
# p1 = util.geographic_ddd_to_dms("36.216792 -115.062092".strip(' ').split(' '))
# print(f"{p1[0]} {p1[1]} {p1[0]}{p1[1]}")

# movrep
# azimuth = util.geographic_to_azimuth([9.134301, 123.696082], [9.095656, 123.588278])
# azimuth = util.mathematics_constrain(azimuth-90, 0, 360)
# point = util.geographic_to_destination_point([9.105936, 123.642528], azimuth, 12*1852)
# print(f"{point[0]:.6f} {point[1]:.6f}")
# point = util.geographic_to_midpoint([9.120986, 123.680120], [8.545962, 124.319321])
# point = util.geographic_to_midpoint([10.457100, 125.463228], point)
# print(f"{point[0]:.6f} {point[1]:.6f}")

# timestamp addition (time-to-wait)
# timestampZ = util.timestamp_calculator_addition(days=0, hours=7, minutes=10)
# timestampR = util.timestamp_to_zone(timestampZ, 'R')
# weekday = util.timestamp_weekday(timestampR)
# print(timestampR, weekday)

# https://www.powerstream.com/Wire_Size.htm
wireGauge_to_maximumCurrent = [[0, 150.0], [1, 119.0], [2, 94.0], [3, 75.0], [4, 60.0], [5, 47.0], [6, 37.0], [7, 30.0], [8, 24.0], [9, 19.0], [10, 15.0], [11, 12.0], [12, 9.3], [13, 7.4], [14, 5.9], [15, 4.7], [16, 3.7], [17, 2.9], [18, 2.3], [19, 1.8], [20, 1.5], [21, 1.2], [22, 0.92], [23, 0.729], [24, 0.577], [25, 0.457], [26, 0.361], [27, 0.288], [28, 0.226], [29, 0.182], [30, 0.142], [31, 0.113], [32, 0.091]]
a="""
"""
# arr = []
# axisX = []
# axisY = []
# for line in [b for b in a.splitlines() if len(b.strip(' ')) > 0]:
#     gauge = int(line[0:2])
#     resistance = float(line[3:])
#     arr.append([gauge,resistance])
#     axisX += [gauge]
#     axisY += [resistance]
# print(arr)
# import matplotlib.pyplot
# matplotlib.pyplot.xlabel('x-axis')
# matplotlib.pyplot.ylabel('y-axis')
# points = [axisX,axisY]
# matplotlib.pyplot.plot(*points, scalex=True, scaley=True, color='black', linestyle='solid', linewidth=1, marker='o', markersize=1)
# matplotlib.pyplot.grid(color = 'black', linestyle = 'solid', linewidth = 0.5)
# matplotlib.pyplot.show()


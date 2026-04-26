# Author: Corey J. Taylor
# Version: 1.0.0
# Date created: XXXX-XX-XX
# Last modified: XXXX-XX-XX

import datetime, inspect, json, math, os, re, socket, time, threading
from typing import Callable, Any, TypeVar

class address(str): pass
class binary(str): pass
class decimal(int): pass
class hexadecimal(float): pass
class octal(str): pass
# class timestamp(datetime.datetime|int|str): pass
# generic type for better type hinting
T = TypeVar('T')

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
address-ipv4-networkmask
address-ipv4-prefix-length
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
address-ipv6-unicast
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
degrees
hexadecimal
html
html-tag
identifier
number
number-decimal
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
string-number-decimal
string-number-float
string-number-integer
string-object
timestamp
timestamp-date
timestamp-time
timestamp-zone
url
--------------------------------------------------------------------------------
address-ipv4-netmask    = address-ipv4-networkmask
address-ipv4-subnetmask = address-ipv4-subnetworkmask
ip                      = internet_protocol
ipv4                    = internet_protocol_v4
ipv6                    = internet_protocol_v6
mac                     = media_access_control
--------------------------------------------------------------------------------

"""

#______________________________________________________________________________#
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

    RADIANS_TO_DEGREES = 180 / math.pi
    SPHERE_RADIUS = 6371000

    ALIGN_CENTER = "center"
    ALIGN_LEFT   = "left"
    ALIGN_RIGHT  = "right"

    FILE_TIMESTAMP_MILLISECONDS = "milliseconds"
    FILE_TIMESTAMP_SECONDS      = "seconds"

    GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_DECIMAL_LATITUDE_OPT1 = r"(?P<decimal_degrees>(-|\+)?([0-8]\d)(\.\d+)?)"
    GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_DECIMAL_LATITUDE_OPT2 = r"(?P<decimal_degrees>(-|\+)?([0-8]?\d)(\.\d+)?)(\*|°|º)"
    GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_DECIMAL_LONGITUDE_OPT1 = r"(?P<decimal_degrees>(-|\+)?(0\d\d|1[0-7]\d)(\.\d+)?)"
    GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_DECIMAL_LONGITUDE_OPT2 = r"(?P<decimal_degrees>(-|\+)?(\d\d?|0\d\d|1[0-7]\d)(\.\d+)?)(\*|°|º)"
    GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LATITUDE_OPT1 = r"(?P<degrees>[0-8]\d)"
    GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LATITUDE_OPT2 = r"(?P<degrees>[0-8]?\d)(\*|°|º)"
    GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LONGITUDE_OPT1 = r"(?P<degrees>0\d\d|1[0-7]\d)"
    GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LONGITUDE_OPT2 = r"(?P<degrees>\d\d?|0\d\d|1[0-7]\d)(\*|°|º)"
    GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LATITUDE = r"(?P<direction>N|S)"
    GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LONGITUDE = r"(?P<direction>E|W)"
    GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_DECIMAL_OPT1 = r"(?P<decimal_minutes>(0\d|[1-5]\d)\.\d\d)"
    GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_DECIMAL_OPT2 = r"(?P<decimal_minutes>(0?\d|[1-5]\d)\.\d+)('|′)"
    GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_OPT1 = r"(?P<minutes>0\d|[1-5]\d)"
    GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_OPT2 = r"(?P<minutes>0?\d|[1-5]\d)('|′)"
    GEOGRAPHIC_COORDINATES_PATTERN_SECONDS_OPT1 = r"(?P<seconds>(0\d|[1-5]\d)(\.\d+)?)"
    GEOGRAPHIC_COORDINATES_PATTERN_SECONDS_OPT2 = r"(?P<seconds>(0?\d|[1-5]\d)(\.\d+)?)(\"|″)"

    HASH_MD5    = "md5"
    HASH_SHA1   = "sha1"
    HASH_SHA224 = "sha224"
    HASH_SHA256 = "sha256"
    HASH_SHA384 = "sha384"
    HASH_SHA512 = "sha512"

    NUMBER_PLACEMENT = {
        13:  "trillions",
        12:  "hundred billions",
        11:  "ten billions",
        10:  "billions",
         9:  "hundred millions",
         8:  "ten millions",
         7:  "millions",
         6:  "hundred thousands",
         5:  "ten thousands",
         4:  "thousands",
         3:  "hundreds",
         2:  "tens",
         1:  "ones",
         0:  "",
        -1:  "tenths",
        -2:  "hundredths",
        -3:  "thousandths",
        -4:  "ten thousandths",
        -5:  "hundred thousandths",
        -6:  "millionths",
        -7:  "ten millionths",
        -8:  "hundred millionths",
        -9:  "billionths",
        -10: "ten billionths",
        -11: "hundred billionths",
        -12: "trillionths",
        -13: "ten trillionths",
        -14: "hundred trillionths"
    }

    REFERENCE_TAG_ABBREVIATIONS = "ABBREVIATIONS"
    REFERENCE_TAG_ACRONYMS      = "ACRONYMS"
    REFERENCE_TAG_DEFINITIONS   = "DEFINITIONS"
    REFERENCE_TAG_LIST          = "LIST"
    REFERENCE_TAG_NAME          = "NAME"
    REFERENCE_TAG_OBJECT        = "OBJECT"
    REFERENCE_TAG_QUESTIONS     = "QUESTIONS"
    REFERENCE_TAG_SOURCE        = "SOURCE"
    REFERENCE_TAG_SUBTITLE      = "SUBTITLE"
    REFERENCE_TAG_TABLE         = "TABLE"
    REFERENCE_TAG_TITLE         = "TITLE"

    STRING_INTERPOLATION_SYNTAX1 = r"<\w+(?:[-_]\w+)*>"
    STRING_INTERPOLATION_SYNTAX2 = r"\{\w+(?:[-_]\w+)*\}"
    STRING_INTERPOLATION_SYNTAX3 = r"%\w+(?:[-_]\w+)*%"

    TABLE_ORIENTATION_VERTICAL   = "vertical"
    TABLE_ORIENTATION_HORIZONTAL = "horizontal"

    TIME_DAYS_OF_WEEK = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    TIME_MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    TIME_QUARTERS = ["First", "Second", "Third", "Fourth"]

    TIMESTAMP_OPTION_DICTIONARY   = "dictionary"
    TIMESTAMP_OPTION_MILLISECONDS = "milliseconds"
    TIMESTAMP_OPTION_OBJECT       = "object"
    TIMESTAMP_OPTION_SECONDS      = "seconds"
    TIMESTAMP_OPTION_STRING       = "string"
    TIMESTAMP_OPTION_TEXT         = "text"

    TIMESTAMP_PATTERN_YEAR        = r"(?P<year>19[7-9][0-9]|[2-9][0-9][0-9][0-9])"
    TIMESTAMP_PATTERN_MONTH       = r"(?P<month>0[1-9]|1[0-2])"
    TIMESTAMP_PATTERN_DAY         = r"(?P<day>0[1-9]|1[0-9]|2[0-9]|3[0-2])"
    TIMESTAMP_PATTERN_HOUR        = r"(?P<hour>0[0-9]|1[0-9]|2[0-3])"
    TIMESTAMP_PATTERN_MINUTE      = r"(?P<minute>0\d|[1-5]\d)"
    TIMESTAMP_PATTERN_SECOND      = r"(?P<second>0\d|[1-5]\d)"
    TIMESTAMP_PATTERN_MILLISECOND = r"(?P<millisecond>\d\d\d)?"
    TIMESTAMP_PATTERN_ZONE        = r"(?P<zone>[A-I]|[K-Z])?"

    TIMEZONE_DESIGNATIONS = {
        'A': "Etc/GMT-1",
        'B': "Etc/GMT-2",
        'C': "Etc/GMT-3",
        'D': "Etc/GMT-4",
        'E': "Etc/GMT-5",
        'F': "Etc/GMT-6",
        'G': "Etc/GMT-7",
        'H': "Etc/GMT-8",
        'I': "Etc/GMT-9",
        'K': "Etc/GMT-10",
        'L': "Etc/GMT-11",
        'M': "Etc/GMT-12",
        'N': "Etc/GMT+1",
        'O': "Etc/GMT+2",
        'P': "Etc/GMT+3",
        'Q': "Etc/GMT+4",
        'R': "Etc/GMT+5",
        'S': "Etc/GMT+6",
        'T': "Etc/GMT+7",
        'U': "Etc/GMT+8",
        'V': "Etc/GMT+9",
        'W': "Etc/GMT+10",
        'X': "Etc/GMT+11",
        'Y': "Etc/GMT+12",
        'Z': "GMT",
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

    variables: dict[str, str] = {
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
        return bool(re.match(pattern, f"{value}"))
    def istype(value, types: str):
        def toBinary(value: str, type: str) -> str:
            if util.ispattern(value, r"^(0|1)+$"):
                return value
            elif type.startswith("address-ipv4") or type.startswith("address-internet_protocol_v4"):
                return util.address_ipv4(value)
            elif type.startswith("address-ipv6") or type.startswith("address-internet_protocol_v6"):
                return util.address_ipv6(value)
            elif type.startswith("address-mac") or type.startswith("address-media_access_control"):
                return util.address_mac(value)
        def istype(value, type: str):
            if type == "address":
                return istype(value, "address-ipv4") or istype(value, "address-ipv6") or istype(value, "address-mac")
            if type == "address-ip" or type == "address-internet_protocol":
                return istype(value, "address-ipv4") or istype(value, "address-ipv6")
            if type == "address-ip-local" or type == "address-internet_protocol-local":
                return istype(value, "address-ipv4-local") or istype(value, "address-ipv6-local")
            if type == "address-ip-local-link" or type == "address-internet_protocol-local-link":
                return istype(value, "address-ipv4-local-link") or istype(value, "address-ipv6-local-link")
            if type == "address-ip-local-unique" or type == "address-internet_protocol-local-unique":
                return istype(value, "address-ipv4-local-unique") or istype(value, "address-ipv6-local-unique")
            if type == "address-ip-loopback" or type == "address-internet_protocol-loopback":
                return istype(value, "address-ipv4-loopback") or istype(value, "address-ipv6-loopback")
            if type == "address-ip-multicast" or type == "address-internet_protocol-multicast":
                return istype(value, "address-ipv4-multicast") or istype(value, "address-ipv6-multicast")
            if type == "address-ip-unspecified" or type == "address-internet_protocol-unspecified":
                return istype(value, "address-ipv4-unspecified") or istype(value, "address-ipv6-unspecified")
            if type == "address-ipv4" or type == "address-internet_protocol_v4":
                if istype(value, "string"):
                    if istype(value, "binary"):
                        return len(value) == 32
                    else:
                        assert isinstance(value, str)
                        strings = value.split('.')
                        if len(strings) == 4:
                            for string in strings:
                                if len(string) < 0 or len(string) > 3: return False
                                if not istype(string, "string-number"): return False
                                if int(string) < 0 or int(string) > 255: return False
                            return True
            if type == "address-ipv4-benchmarking" or type == "address-internet_protocol_v4-benchmarking":
                if istype(value, "address-ipv4"):
                    value = toBinary(value, type)
                    return value[0:15] == "110001100001001"
            if type == "address-ipv4-broadcast" or type == "address-internet_protocol_v4-broadcast":
                if istype(value, "address-ipv4"):
                    value = toBinary(value, type)
                    return value == "11111111111111111111111111111111"
            if type == "address-ipv4-dummy" or type == "address-internet_protocol_v4-dummy":
                if istype(value, "address-ipv4"):
                    value = toBinary(value, type)
                    return value == "11000000000000000000000000001000"
            if type == "address-ipv4-local" or type == "address-internet_protocol_v4-local":
                return istype(value, "address-ipv4-local-link") or istype(value, "address-ipv4-local-unique")
            if type == "address-ipv4-local-link" or type == "address-internet_protocol_v4-local-link":
                if istype(value, "address-ipv4"):
                    value = toBinary(value, type)
                    return value[0:16] == "1010100111111110"
            if type == "address-ipv4-local-unique" or type == "address-internet_protocol_v4-local-unique":
                if istype(value, "address-ipv4"):
                    value = toBinary(value, type)
                    return value[0:8] == "10100000" or value[0:12] == "101011000001" or value[0:16] == "1100000010101000"
            if type == "address-ipv4-loopback" or type == "address-internet_protocol_v4-loopback":
                if istype(value, "address-ipv4"):
                    value = toBinary(value, type)
                    return value[0:8] == "01111111"
            if type == "address-ipv4-mask" or type == "address-internet_protocol_v4-mask":
                return istype(value, "address-ipv4-networkmask") or istype(value, "address-ipv4-wildcardmask")
            if type == "address-ipv4-multicast" or type == "address-internet_protocol_v4-multicast":
                if istype(value, "address-ipv4"):
                    value = toBinary(value, type)
                    return value[0:4] == "1110"
            if type == "address-ipv4-netmask" or type == "address-internet_protocol_v4-netmask":
                return istype(value, "address-ipv4-networkmask")
            if type == "address-ipv4-networkmask" or type == "address-internet_protocol_v4-networkmask":
                if istype(value, "address-ipv4"):
                    value = toBinary(value, type)
                    if "0" in value:
                        return value.find("0") > value.rfind("1")
                    else:
                        return value == "11111111111111111111111111111111"
            if type == "address-ipv4-prefix-length" or type == "address-internet_protocol_v4-prefix-length":
                if istype(value, "number") or istype(value, "string-number"):
                    return util.ispattern(value, r"^(0?[0-9]|1[0-9]|2[0-9]|3[1-2])$")
            if type == "address-ipv4-subnetmask" or type == "address-internet_protocol_v4-subnetmask":
                return istype(value, "address-ipv4-networkmask")
            if type == "address-ipv4-subnetworkmask" or type == "address-internet_protocol_v4-subnetworkmask":
                return istype(value, "address-ipv4-networkmask")
            if type == "address-ipv4-unicast" or type == "address-internet_protocol_v4-unicast":
                if istype(value, "address-ipv4"):
                    return not (istype(value, "address-ipv4-broadcast") or istype(value, "address-ipv4-multicast"))
            if type == "address-ipv4-unspecified" or type == "address-internet_protocol_v4-unspecified":
                if istype(value, "address-ipv4"):
                    value = toBinary(value, type)
                    return value == "00000000000000000000000000000000"
            if type == "address-ipv4-wildcardmask" or type == "address-internet_protocol_v4-wildcardmask":
                if istype(value, "address-ipv4"):
                    value = toBinary(value, type)
                    if "1" in value:
                        return value.find("1") > value.rfind("0")
                    else:
                        return value == "00000000000000000000000000000000"
            if type == "address-ipv6" or type == "address-internet_protocol_v6":
                if istype(value, "string"):
                    if istype(value, "binary"):
                        return len(value) == 128
                    else:
                        assert isinstance(value, str)
                        strings = value.split(':')
                        if len(strings) == 8:
                            for string in strings:
                                if len(string) < 0 or len(string) > 4: return False
                                if not istype(string, "hexadecimal"): return False
                            return True
                        elif '::' in value:
                            return util.ispattern(value, r"^(:|[0-9]|[A-F]|[a-f])+$") and len(value) <= 39
            if type == "address-ipv6-4to6" or type == "address-internet_protocol_v6-4to6":
                if istype(value, "address-ipv6"):
                    value = toBinary(value, type)
                    return value[0:96] == "000000000000000000000000000000000000000000000000000000000000000000000000000000001111111111111111"
            if type == "address-ipv6-ipv4-mapped" or type == "address-internet_protocol_v6-internet_protocol_v4-mapped":
                if istype(value, "address-ipv6"):
                    value = toBinary(value, type)
                    return value[0:96] == "000000000000000000000000000000000000000000000000000000000000000000000000000000001111111111111111"
            if type == "address-ipv6-6to4" or type == "address-internet_protocol_v6-6to4":
                if istype(value, "address-ipv6"):
                    value = toBinary(value, type)
                    return value[0:16] == "0010000000000010"
            if type == "address-ipv6-anycast" or type == "address-internet_protocol_v6-anycast":
                return istype(value, "address-ipv6-global")
            if type == "address-ipv6-benchmarking" or type == "address-internet_protocol_v6-benchmarking":
                if istype(value, "address-ipv6"):
                    value = toBinary(value, type)
                    return value[0:48] == "001000000000000100000000000000100000000000000000"
            if type == "address-ipv6-documentation" or type == "address-internet_protocol_v6-documentation":
                if istype(value, "address-ipv6"):
                    value = toBinary(value, type)
                    return value[0:32] == "00100000000000010000110110111000"
            if type == "address-ipv6-global" or type == "address-internet_protocol_v6-global":
                if istype(value, "address-ipv6"):
                    value = toBinary(value, type)
                    return value[0:3] == "001"
            if type == "address-ipv6-local" or type == "address-internet_protocol_v6-local":
                return istype(value, "address-ipv6-local-link") or istype(value, "address-ipv6-local-unique")
            if type == "address-ipv6-local-link" or type == "address-internet_protocol_v6-local-link":
                if istype(value, "address-ipv6"):
                    value = toBinary(value, type)
                    return value[0:10] == "1111111010"
            if type == "address-ipv6-local-unique" or type == "address-internet_protocol_v6-local-unique":
                if istype(value, "address-ipv6"):
                    value = toBinary(value, type)
                    return value[0:7] == "1111110"
            if type == "address-ipv6-loopback" or type == "address-internet_protocol_v6-loopback":
                if istype(value, "address-ipv6"):
                    value = toBinary(value, type)
                    return value == "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"
            if type == "address-ipv6-multicast" or type == "address-internet_protocol_v6-multicast":
                if istype(value, "address-ipv6"):
                    value = toBinary(value, type)
                    return value[0:8] == "11111111"
            if type == "address-ipv6-teredo" or type == "address-internet_protocol_v6-teredo":
                if istype(value, "address-ipv6"):
                    value = toBinary(value, type)
                    return value[0:32] == "00100000000000010000000000000000"
            if type == "address-ipv6-unicast" or type == "address-internet_protocol_v6-unicast":
                if istype(value, "address-ipv6"):
                    return istype(value, "address-ipv6-global") or istype(value, "address-ipv6-local")
            if type == "address-ipv6-unspecified" or type == "address-internet_protocol_v6-unspecified":
                if istype(value, "address-ipv6"):
                    value = toBinary(value, type)
                    return value == "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
            if type == "address-mac" or type == "address-media_access_control":
                if istype(value, "string"):
                    if istype(value, "binary"):
                        return len(value) == 48
                    else:
                        assert isinstance(value, str)
                        strings = value.split('-')
                        if len(strings) == 6:
                            for string in strings:
                                if len(string) != 2: return False
                                if not istype(string, "hexadecimal"): return False
                            return True
            if type == "address-mac-broadcast" or type == "address-media_access_control-broadcast":
                if istype(value, "address-mac"):
                    value = toBinary(value, type)
                    return value == "111111111111111111111111111111111111111111111111"
            if type == "address-mac-multicast" or type == "address-media_access_control-multicast":
                return istype(value, "address-mac-multicast-ipv4") or istype(value, "address-mac-multicast-ipv6")
            if type == "address-mac-multicast-ipv4" or type == "address-media_access_control-multicast-internet_protocol_v4":
                if istype(value, "address-mac"):
                    value = toBinary(value, type)
                    return value[0:25] == "0000000100000000010111100"
            if type == "address-mac-multicast-ipv6" or type == "address-media_access_control-multicast-internet_protocol_v6":
                if istype(value, "address-mac"):
                    value = toBinary(value, type)
                    return value[0:16] == "0011001100110011"
            if type == "address-mac-unicast" or type == "address-media_access_control-unicast":
                if istype(value, "address-mac"):
                    return not (istype(value, "address-mac-broadcast") or istype(value, "address-mac-multicast"))
            if type == "array":
                return isinstance(value, list)
            if type == "array-boolean":
                if istype(value, "array"):
                    for value_ in value:
                        if not istype(value_, "boolean"): return False
                    return True
            if type == "array-bytes":
                if istype(value, "array"):
                    for value_ in value:
                        if not istype(value_, "bytes"): return False
                    return True
            if type == "array-number":
                if istype(value, "array"):
                    for value_ in value:
                        if not istype(value_, "number"): return False
                    return True
            if type == "array-object":
                if istype(value, "array"):
                    for value_ in value:
                        if not istype(value_, "object"): return False
                    return True
            if type == "array-string":
                if istype(value, "array"):
                    for value_ in value:
                        if not istype(value_, "string"): return False
                    return True
            if type == "array-string-array":
                if istype(value, "array"):
                    for value_ in value:
                        if not istype(value_, "string-array"): return False
                    return True
            if type == "array-string-array-object":
                if istype(value, "array"):
                    for value_ in value:
                        if not istype(value_, "string-array-object"): return False
                    return True
            if type == "array-string-boolean":
                if istype(value, "array"):
                    for value_ in value:
                        if not istype(value_, "string-boolean"): return False
                    return True
            if type == "array-string-number":
                if istype(value, "array"):
                    for value_ in value:
                        if not istype(value_, "string-number"): return False
                    return True
            if type == "array-string-object":
                if istype(value, "array"):
                    for value_ in value:
                        if not istype(value_, "string-object"): return False
                    return True
            if type == "base64":
                if istype(value, "string"):
                    return util.ispattern(value, r"^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$")
            if type == "binary":
                if istype(value, "string"):
                    return util.ispattern(value, r"^(0|1)+$")
            if type == "boolean":
                return isinstance(value, bool)
            if type == "bytes":
                return isinstance(value, bytes) or isinstance(value, bytearray)
            if type == "bytes-array":
                if istype(value, "bytes"):
                    return istype(util.byt2str(value), "string-array")
            if type == "bytes-array-object":
                if istype(value, "bytes"):
                    return istype(util.byt2str(value), "string-array-object")
            if type == "bytes-object":
                if istype(value, "bytes"):
                    return istype(util.byt2str(value), "string-object")
            if type == "character":
                if istype(value, "string"):
                    return util.ispattern(value, r"^([A-Z]|[a-z])$")
            if type == "coordinates-geographic":
                return istype(value, "coordinates-geographic-ddd") or istype(value, "coordinates-geographic-ddm") or istype(value, "coordinates-geographic-dms")
            if type == "coordinates-geographic-ddd":
                if istype(value, "string"):
                    return istype(value, "coordinates-geographic-latitude-ddd") or istype(value, "coordinates-geographic-longitude-ddd")
                elif istype(value, "array-number") or istype(value, "array-string"):
                    if len(value) == 2:
                        return istype(value[0], "coordinates-geographic-latitude-ddd") and istype(value[1], "coordinates-geographic-longitude-ddd")
            if type == "coordinates-geographic-ddm":
                if istype(value, "string"):
                    return istype(value, "coordinates-geographic-latitude-ddm") or istype(value, "coordinates-geographic-longitude-ddm")
                elif istype(value, "array-string"):
                    if len(value) == 2:
                        return istype(value[0], "coordinates-geographic-latitude-ddm") and istype(value[1], "coordinates-geographic-longitude-ddm")
            if type == "coordinates-geographic-dms":
                if istype(value, "string"):
                    return istype(value, "coordinates-geographic-latitude-dms") or istype(value, "coordinates-geographic-longitude-dms")
                elif istype(value, "array-string"):
                    if len(value) == 2:
                        return istype(value[0], "coordinates-geographic-latitude-dms") and istype(value[1], "coordinates-geographic-longitude-dms")
            if type == "coordinates-geographic-latitude":
                if istype(value, "string"):
                    return istype(value, "coordinates-geographic-latitude-ddd") or istype(value, "coordinates-geographic-latitude-ddm") or istype(value, "coordinates-geographic-latitude-dms")
            if type == "coordinates-geographic-latitude-ddd":
                if istype(value, "number") or istype(value, "string-number"):
                    return 0 <= abs(float(value)) and abs(float(value)) <= 90
                if istype(value, "string"):
                    pattern = f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_DECIMAL_LATITUDE_OPT1}" if not ('*' in value or '°' in value or 'º' in value) else f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_DECIMAL_LATITUDE_OPT2}"
                    return util.ispattern(value, f"^{pattern}$")
            if type == "coordinates-geographic-latitude-ddm":
                if istype(value, "string"):
                    pattern = f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LATITUDE_OPT1}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_DECIMAL_OPT1}" if not ('*' in value or '°' in value or 'º' in value) else f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LATITUDE_OPT2}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_DECIMAL_OPT2}"
                    return util.ispattern(value, f"^{pattern}{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LATITUDE}$") or util.ispattern(value, f"^{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LATITUDE}{pattern}$")
            if type == "coordinates-geographic-latitude-dms":
                if istype(value, "string"):
                    pattern = f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LATITUDE_OPT1}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_OPT1}{util.GEOGRAPHIC_COORDINATES_PATTERN_SECONDS_OPT1}" if not ('*' in value or '°' in value or 'º' in value) else f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LATITUDE_OPT2}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_OPT2}{util.GEOGRAPHIC_COORDINATES_PATTERN_SECONDS_OPT2}"
                    return util.ispattern(value, f"^{pattern}{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LATITUDE}$") or util.ispattern(value, f"^{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LATITUDE}{pattern}$")
            if type == "coordinates-geographic-longitude":
                if istype(value, "string"):
                    return istype(value, "coordinates-geographic-longitude-ddd") or istype(value, "coordinates-geographic-longitude-ddm") or istype(value, "coordinates-geographic-longitude-dms")
            if type == "coordinates-geographic-longitude-ddd":
                if istype(value, "number") or istype(value, "string-number"):
                    return 0 <= abs(float(value)) and abs(float(value)) <= 180
                if istype(value, "string"):
                    pattern = f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_DECIMAL_LONGITUDE_OPT1}" if not ('*' in value or '°' in value or 'º' in value) else f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_DECIMAL_LONGITUDE_OPT2}"
                    return util.ispattern(value, f"^{pattern}$")
            if type == "coordinates-geographic-longitude-ddm":
                if istype(value, "string"):
                    pattern = f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LONGITUDE_OPT1}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_DECIMAL_OPT1}" if not ('*' in value or '°' in value or 'º' in value) else f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LONGITUDE_OPT2}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_DECIMAL_OPT2}"
                    return util.ispattern(value, f"^{pattern}{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LONGITUDE}$") or util.ispattern(value, f"^{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LONGITUDE}{pattern}$")
            if type == "coordinates-geographic-longitude-dms":
                if istype(value, "string"):
                    pattern = f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LONGITUDE_OPT1}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_OPT1}{util.GEOGRAPHIC_COORDINATES_PATTERN_SECONDS_OPT1}" if not ('*' in value or '°' in value or 'º' in value) else f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LONGITUDE_OPT2}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_OPT2}{util.GEOGRAPHIC_COORDINATES_PATTERN_SECONDS_OPT2}"
                    return util.ispattern(value, f"^{pattern}{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LONGITUDE}$") or util.ispattern(value, f"^{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LONGITUDE}{pattern}$")
            if type == "date":
                return isinstance(value, datetime.datetime)
            if type == "decimal":
                return istype(value, "number") or istype(value, "string-number")
            if type == "degrees":
                return util.ispattern(value, r"^(0?\d?\d|[1-2]\d\d|3[0-5]\d)(°(M|T))?$")
            if type == "hexadecimal":
                if istype(value, "string"):
                    return util.ispattern(value, r"^([0-9]|[A-F]|[a-f])+$")
            if type == "html":
                pass
            if type == "html-tag":
                if istype(value, "string"):
                    strings = '!doctype|a|abbr|address|area|article|aside|audio|b|base|bb|bdi|bdo|big|blockquote|br|button|canvas|caption|cite|code|col|colgroup|data|datalist|dd|del|details|dfn|dialog|div|dl|dt|em|embed|fieldset|figcaption|figure|footer|form|h1|h2|h3|h4|h5|h6|head|header|hr|html|i|iframe|img|input|ins|kbd|label|legend|li|link|main|map|mark|meta|meter|nav|noscript|object|ol|optgroup|option|p|param|picture|polyline|polygon|pre|progress|q|rp|rt|ruby|s|samp|script|section|select|small|source|span|strong|style|sub|summary|sup|svg|table|tbody|td|template|textarea|tfoot|th|thead|tr|track|u|ul|var|video|wbr'.split('|')
                    return value in strings
            if type == "identifier":
                if istype(value, "string"):
                    return util.ispattern(value, r"^([0-9]|[A-Z]|[a-z]|_)+$")
            if type == "number":
                return istype(value, "number-decimal") or istype(value, "number-integer")
            if type == "number-decimal" or type == "number-float":
                return isinstance(value, float)
            if type == "number-integer":
                return isinstance(value, int)
            if type == "object":
                return isinstance(value, dict)
            if type == "octal":
                if istype(value, "string"):
                    return util.ispattern(value, r"^[0-7]+$")
            if type == "port":
                if istype(value, "number") or istype(value, "string-number"):
                    return 0 <= int(value) and int(value) <= 65535
            if type == "port-ephemeral":
                if istype(value, "number") or istype(value, "string-number"):
                    return 1024 <= int(value) and int(value) <= 65535
            if type == "port-ephemeral-registered":
                if istype(value, "number") or istype(value, "string-number"):
                    return 1024 <= int(value) and int(value) <= 49151
            if type == "port-ephemeral-unregistered" or type == "port-ephemeral-dynamic" or type == "port-ephemeral-private":
                if istype(value, "number") or istype(value, "string-number"):
                    return 49152 <= int(value) and int(value) <= 65535
            if type == "port-nonephemeral" or type == "port-wellknown":
                if istype(value, "number") or istype(value, "string-number"):
                    return 0 <= int(value) and int(value) <= 1023
            if type == "string":
                return isinstance(value, str)
            if type == "string-array":
                if istype(value, "string"):
                    if len(value) >= 2:
                        return value[0] == '[' and value[-1] == ']'
            if type == "string-array-object":
                if istype(value, "string"):
                    if len(value) >= 4:
                        return value[0] == '[' and value[-1] == ']' and value[1] == '{' and value[-2] == '}'
            if type == "string-boolean":
                if istype(value, "string"):
                    assert isinstance(value, str)
                    return value.lower() == "true" or value.lower() == "false"
            if type == "string-number":
                 return istype(value, "string-number-decimal") or istype(value, "string-number-integer")
            if type == "string-number-decimal" or type == "string-number-float":
                if istype(value, "string"):
                    return util.ispattern(value, r"^(-|\+)?\d+\.\d+$")
            if type == "string-number-integer":
                if istype(value, "string"):
                    return util.ispattern(value, r"^(-|\+)?\d+$")
            if type == "string-object":
                if istype(value, "string"):
                    if len(value) >= 2:
                        return value[0] == '{' and value[-1] == '}'
            if type == "timestamp":
                if istype(value, "string"):
                    if len(value) >= 4:
                        pattern = ""
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
                        return util.ispattern(value, f"^{pattern}{util.TIMESTAMP_PATTERN_ZONE}$")
            if type == "timestamp-date":
                if istype(value, "string"):
                    if len(value) > 0:
                        if '-' in value:
                            return util.ispattern(value, f"^{util.TIMESTAMP_PATTERN_YEAR}-{util.TIMESTAMP_PATTERN_MONTH}-{util.TIMESTAMP_PATTERN_DAY}{util.TIMESTAMP_PATTERN_ZONE}$")
                        else:
                            return util.ispattern(value, f"^{util.TIMESTAMP_PATTERN_YEAR}{util.TIMESTAMP_PATTERN_MONTH}{util.TIMESTAMP_PATTERN_DAY}{util.TIMESTAMP_PATTERN_ZONE}$")
            if type == "timestamp-time":
                if istype(value, "string"):
                    if len(value) > 0:
                        if ':' in value:
                            return util.ispattern(value, f"^{util.TIMESTAMP_PATTERN_HOUR}:{util.TIMESTAMP_PATTERN_MINUTE}:{util.TIMESTAMP_PATTERN_SECOND}{util.TIMESTAMP_PATTERN_ZONE}$")
                        else:
                            return util.ispattern(value, f"^{util.TIMESTAMP_PATTERN_HOUR}{util.TIMESTAMP_PATTERN_MINUTE}{util.TIMESTAMP_PATTERN_SECOND}{util.TIMESTAMP_PATTERN_ZONE}$")
            if type == "timestamp-zone":
                if istype(value, "string"):
                    if len(value) == 1:
                        return util.ispattern(value, util.TIMESTAMP_PATTERN_ZONE)
            # 
            if type[-2:len(type)] == '[]':
                if istype(value, "array"):
                    for value_ in value:
                        if not istype(value_, type[0:-2]):
                            return False
                    return True
            return False
        if value == None: return False
        delimiters = ['&','|']
        delimiter = next((delimiter for delimiter in delimiters if delimiter in types), None)
        if all([delimiter in types for delimiter in delimiters]): raise Exception(f"ValueError: conflicting delimiters")
        if delimiter == None: return istype(value, types)
        else:
            results = [istype(value, type) for type in types.split(delimiter)]
            if delimiter == '&': return all(results)
            if delimiter == '|': return any(results)
    def importModule(name: str):
        # if util.importModule(''): import
        return not name in dir()
    def get(method: str, *arguments):
        return getattr(globals()["util"], method)(*arguments)
    # a
    def abbreviation(string: str, delimiter: str = ' ') -> str:
        specials = {
            "child-to-parent synchronization": "CSYNC",
            "domain name system security": "DNSSEC",
            "domain name system security extensions": "DNSSEC",
            "domain name system security lookaside validation": "DLV",
            "domain name system key": "DNSKEY",
            "domain name system stateful operations": "DSO",
            "high level data link control": "HDLC",
            "gateway to gateway protocol": "GGP",
            "identifier": "ID",
            "inter domain policy routing": "IDPR",
            "inter domain policy routing protocol": "IDPR",
            "inter domain routing protocol": "IDRP",
            "internet control message protocol v6": "ICMPv6",
            "internet protocol v4": "IPv4",
            "internet protocol v6": "IPv6",
            "internet protocol secure": "IPSec",
            "internet protocol secure key": "IPSECKEY",
            "internet stream protocol": "ST",
            "inverse address resolution protocol": "InARP",
            "naming authority pointer": "NAPTR",
            "netbios": "NetBIOS",
            "netbios datagram distribution server": "NBDDS",
            "netbios name server": "NBNS",
            "nimrod locator": "NIMLOC",
            "path maximum transmission unit discovery": "PMTUD",
            "resource record digital signature": "RRSIG",
            "resource reservation protocol": "RSVP",
            "secure multipurpose internet mail extensions": "SMIME",
            "secure shell": "SSH",
            "secure shell fingerprint": "SSHFP",
            "service locator": "SRV",
            "service binding": "SVCB",
            "transaction signature": "TSIG",
            "transport layer security": "TLS",
        }
        for specialBefore, specialAfter in specials.items():
            if specialBefore.lower() == string.lower() or specialBefore.replace(' ', '_').lower() == string.lower():
                return specialAfter
        nString = ''
        for substring in string.split(delimiter):
            nString += substring[0]
        return nString
    def address_binary(value: str|int) -> str:
        if util.istype(value, "address&binary"):
            return value
        if util.istype(value, "number|string-number"):
            return util.address_prefix_length_to_mask(value)
        elif util.istype(value, "address-ipv4"):
            return util.address_ipv4(value)
        elif util.istype(value, "address-ipv6"):
            return util.address_ipv6(value)
        elif util.istype(value, "address-mac"):
            return util.address_mac(value)
        else:
            raise Exception(f"TypeError: require type address or number")
    def address_decimal(value: str) -> int:
        return util.bin2dec(util.address_binary(value))
    def address_family(value: str, short: bool = False) -> str:
        if util.istype(value, "address-internet_protocol_v4"):
            return "ipv4" if short else "internet_protocol_v4"
        elif util.istype(value, "address-internet_protocol_v6"):
            return "ipv6" if short else "internet_protocol_v6"
        elif util.istype(value, "address-media_access_control"):
            return "mac" if short else "media_access_control"
        else:
            raise Exception(f"TypeError: require type address")
    def address_hexadecimal(value: str) -> str:
        return util.bin2hex(util.address_binary(value))
    def address_string(value: int|str) -> str:
        if util.istype(value, "address") and not util.istype(value, "binary"):
            return value
        elif util.istype(value, "address") and util.istype(value, "binary"):
            if util.istype(value, "address-internet_protocol_v4"):
                return util.address_ipv4(value)
            elif util.istype(value, "address-internet_protocol_v6"):
                return util.address_ipv6(value)
            elif util.istype(value, "address-media_access_control"):
                return util.address_mac(value)
        elif util.istype(value, "number|string-number"):
            return util.address_ipv4(util.address_prefix_length_to_mask(value))
        else:
            raise Exception(f"TypeError: require type address or number")
    def address_ip_to_mac_multicast(value: str) -> str:
        if util.istype(value, "address-ipv4"):
            return util.address_ipv4_to_mac_multicast(value)
        elif util.istype(value, "address-ipv6"):
            return util.address_ipv6_to_mac_multicast(value)
        else:
            raise Exception(f"TypeError: require type address-ipv4 or address-ipv6")
    def address_ipv4(value: str = None) -> str:
        def generate() -> str:
            # generate a random number and convert to 8-bit binary for each octet
            return ''.join([util.dec2bin(util.random(0, 255), 8) for i in range(4)])
        def toBinary(text: str) -> str:
            # convert each number to 8-bit binary string (octet)
            return ''.join([util.dec2bin(int(octet), 8) for octet in text.split('.')])
        def toText(binary: str) -> str:
            # convert each 8-bit binary string to number (octet)
            return '.'.join([str(util.bin2dec(binary[i:i+8])) for i in range(0, 32, 8)])
        # generate random binary
        if value == None:
            return generate()
        # text to binary
        elif '.' in value:
            if not len(value.split('.')) == 4:
                raise Exception(f"Error: invalid IPv4 address (requires 4 octets)")
            return toBinary(value)
        # binary to text
        else:
            if not len(value) == 32:
                raise Exception(f"Error: invalid IPv4 address (improper length)")
            return toText(value)
    def address_ipv4_broadcast(address: str, netmask: int|str) -> str:
        binary_address = util.address_binary(address)
        binary_netmask = util.address_binary(netmask)
        prefix_length = util.address_mask_to_prefix_length(binary_netmask)
        return binary_address[0:prefix_length].ljust(32, '1')
    def address_ipv4_network_identifier(address: str, netmask: int|str) -> str:
        binary_address = util.address_binary(address)
        binary_netmask = util.address_binary(netmask)
        prefix_length = util.address_mask_to_prefix_length(binary_netmask)
        return binary_address[0:prefix_length].ljust(32, '0')
    def address_ipv4_to_ipv6_4to6(value: str) -> str:
        binary = util.address_binary(value)
        return '000000000000000000000000000000000000000000000000000000000000000000000000000000001111111111111111' + binary
    def address_ipv4_to_ipv6_6to4(value: str) -> str:
        binary = util.address_binary(value)
        return '0010000000000010' + binary + '00000000000000000000000000000000000000000000000000000000000000000000000000000000'
    def address_ipv4_to_ipv6_mapped(value: str) -> str:
        binary = util.address_binary(value)
        return '000000000000000000000000000000000000000000000000000000000000000000000000000000001111111111111111' + binary
    def address_ipv4_to_mac_multicast(value: str) -> str:
        binary = util.address_binary(value)
        return util.hex2bin("01005E") + '0' + binary[9:32]
    def address_ipv4_to_ptr(address: str) -> str:
        text: str = util.address_string(address)
        digits = text.split('.')
        digits.reverse()
        ptr_prefix = ".".join(digits)
        return f"{ptr_prefix}.in-addr.arpa"
    def address_ipv6(value: str = None) -> str:
        def generate() -> str:
            # generate a random number and convert to 16-bit binary for each hextet
            return ''.join([util.dec2bin(util.random(0, 65535), 16) for i in range(8)])
        def toBinary(text: str) -> str:
            isCompressed = '::' in text or any(len(hextet) < 4 for hextet in text.split(':'))
            if isCompressed:
                hextets = util.address_ipv6_uncompress(text).split(':')
            else:
                hextets = text.split(':')
            # convert each 4-digit hexadecimal string to 16-bit binary string (hextet)
            binary = ''
            for hextet in hextets:
                binary += util.hex2bin(hextet)
            return binary
        def toText(binary: str) -> str:
            # convert each 16-bit binary string to 4-digit hexadecimal string (hextet)
            text = ":".join([util.bin2hex(binary[i:i+16]) for i in range(0, 128, 16)])
            return util.address_ipv6_compress(text)
        # generate random binary
        if value == None:
            return generate()
        # text to binary
        elif ':' in value:
            return toBinary(value)
        # binary to text
        else:
            if not len(value) == 128:
                raise Exception(f"Error: invalid IPv6 address (improper length)")
            return toText(value)
    def address_ipv6_compress(text: str) -> str:
        if not ':' in text:
            raise Exception(f"Error: invalid IPv6 address")
        # ensure address is fully expanded
        text = util.address_ipv6_uncompress(text)
        # remove all zero expansion block hextets and insert the double colon notation
        if text.startswith('0000:'):
            text = text.replace('0000:', '')
            text = '::' + text
        elif text.endswith(':0000'):
            text = text.replace(':0000', '')
            text = text + '::'
        elif '0000' in text:
            index = text.index('0000')
            text = text.replace('0000:', '')
            text = text[:index] + ':' + text[index:]
        # strip leading zeros in each hextet
        hextets = text.split(':')
        for index, hextet in enumerate(hextets):
            if len(hextet) == 0: continue
            hextets[index] = hex(int(hextet, 16))[2:]
        return ':'.join(hextets)
    def address_ipv6_expand(text: str) -> str:
        return util.address_ipv6_uncompress(text)
    def address_ipv6_uncompress(text: str) -> str:
        if not ':' in text:
            raise Exception(f"Error: invalid IPv6 address (missing colon)")
        if len(text.split('::')) > 2:
            raise Exception(f"Error: invalid IPv6 address (more than one '::')")
        # address is already fully expanded
        if '::' not in text:
            hextets = text.split(':')
            if len(hextets) != 8:
                raise Exception(f"Error: invalid IPv6 address (requires 8 hextets)")
            # pad hextets to 4 hexadecimal digits
            return ':'.join(hextet.zfill(4) for hextet in hextets)
        parts = text.split('::')
        # process left and right parts of the '::'
        # pad existing hextets to 4 hexadecimal digits
        hextets_lt = [hextet.zfill(4) for hextet in parts[0].split(':') if hextet]
        hextets_rt = [hextet.zfill(4) for hextet in parts[1].split(':') if hextet]
        # calculate the number of zero blocks to insert
        num_existing_hextets = len(hextets_lt) + len(hextets_rt)
        num_zeros_to_insert = 8 - num_existing_hextets
        if num_zeros_to_insert < 0:
            raise Exception(f"Error: invalid IPv6 address")
        # create the zero expansion block
        expansion_blocks = ['0000'] * num_zeros_to_insert
        hextets = hextets_lt + expansion_blocks + hextets_rt
        return ':'.join(hextets)
    def address_ipv6_local_link_to_mac(value: str) -> str:
        binary = util.address_binary(value)
        universal_local_bit = '1' if binary[70] == '0' else '0'
        return binary[64:70] + universal_local_bit + binary[71:88] + binary[104:128]
    def address_ipv6_to_ipv4(value: str) -> str:
        binary = util.address_binary(value)
        if util.istype(binary, "address-ipv6-4to6"):
            return binary[96:128]
        elif util.istype(binary, "address-ipv6-6to4"):
            return binary[16:48]
        else:
            raise Exception(f"TypeError: require type address-ipv6-4to6 or address-ipv6-6to4")
    def address_ipv6_to_mac(value: str) -> str:
        binary = util.address_binary(value)
        if util.istype(binary, "address-ipv6-local-link"):
            return util.address_ipv6_local_link_to_mac(binary)
        elif util.istype(binary, "address-ipv6-multicast"):
            return util.address_ipv6_to_mac_multicast(binary)
        else:
            raise Exception(f"TypeError: require type address-ipv6-local-link or address-ipv6-multicast")
    def address_ipv6_to_mac_multicast(value: str) -> bool:
        binary = util.address_binary(value)
        return util.hex2bin("3333") + binary[96:128]
    def address_ipv6_to_ptr(address: str) -> str:
        text_compressed = util.address_string(address)
        text_expanded: str = util.address_ipv6_uncompress(text_compressed)
        hexadecimal = text_expanded.replace(':', '')
        digits = list(hexadecimal)
        digits.reverse()
        ptr_prefix = ".".join(digits)
        return f"{ptr_prefix}.ip6.arpa"
    def address_is_ipv4_broadcast(value: str, network_identifier: str, subnetmask: str) -> bool:
        binary = util.address_binary(value)
        if binary == util.address_ipv4("255.255.255.255"):
            return True
        return binary == util.address_ipv4_broadcast(network_identifier, subnetmask)
    def address_mac(value: str) -> str:
        def generate() -> str:
            # generate a random number and convert to 8-bit binary for each octet
            return ''.join([util.dec2bin(util.random(0, 255), 8) for i in range(6)])
        def toBinary(text: str) -> str:
            # convert each 2-digit hexadecimal string to 8-bit binary string (octet)
            return ''.join([util.hex2bin(octet) for octet in text.split('-')])
        def toText(binary: str) -> str:
            # convert each 8-bit binary string to 2-digit hexadecimal string (octet)
            return '-'.join([util.bin2hex(binary[i:i+8]) for i in range(0, 48, 8)])
        # generate random binary
        if value == None:
            return generate()
        # text to binary
        elif '-' in value:
            if not len(value.split('-')) == 6:
                raise Exception(f"Error: invalid MAC address (requires 6 octets)")
            return toBinary(value)
        # binary to text
        else:
            if not len(value) == 48:
                raise Exception(f"Error: invalid MAC address (improper length)")
            return toText(value)
    def address_mac_to_ipv6_local_link(address: str, network_prefix: str) -> str:
        if len(network_prefix) != 64:
            raise Exception(f"LengthError: 'network_prefix' require 64 characters")
        binary = util.address_binary(address)
        interface_identifier = binary[0:24] + util.hex2bin("fffe") + binary[24:48]
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
    def address_mask_to_address_count(value: int|str) -> int:
        prefix_length = util.address_mask_to_prefix_length(value)
        return 2 ** (32 - prefix_length)
    def address_mask_to_prefix_length(value: str) -> str:
        binary = util.address_binary(value)
        if binary.count('1') == 32 or binary.count('0') == 32:
            return 32
        else:
            character = '1' if binary.find('0') > binary.rfind('1') else '0'
            return binary.count(character)
    def address_mask_to_wildcardmask(value: str) -> str:
        binary = util.address_binary(value)
        prefix_length = binary.count('1')
        return ''.ljust(prefix_length, '0') + ''.ljust(32 - prefix_length, '1')
    def address_prefix_length_to_mask(prefix_length: int|str) -> str:
        prefix_length = int(prefix_length)
        return ''.ljust(prefix_length, '1') + ''.ljust(32 - prefix_length, '0')
    def address_prefix_length_to_wildcardmask(prefix_length: int|str) -> str:
        prefix_length = int(prefix_length)
        return ''.ljust(prefix_length, '0') + ''.ljust(32 - prefix_length, '1')
    def address_prefix_length_to_address_count(prefix_length: int|str) -> int:
        prefix_length = int(prefix_length)
        return 2 ** (32 - prefix_length)
    def address_ptr_to_ip(address: str) -> str:
        pass
    def address_subnetting(network_identifier: str, netmask: int|str, subnets: int):
        netmask = util.address_binary(netmask)
        subnets = int(subnets)
        #
        network_identifier = util.address_ipv4_network_identifier(
            util.address_binary(network_identifier),
            netmask
        )
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
    def address_wildcardmask_to_mask(value: str) -> str:
        binary = util.address_binary(value)
        prefix_length = binary.count('0')
        return ''.ljust(prefix_length, '1') + ''.ljust(32 - prefix_length, '0')
    def address_wildcardmask_to_prefix_length(value: str) -> str:
        binary = util.address_binary(value)
        return binary.count('0')
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
        return util.algebra_factor(number)
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
    def arithmetic_least_common_multiple(numbers: list[int]) -> int:
        lcm = numbers[0]
        for i in range(len(numbers)):
            lcm = (lcm * numbers[i]) / util.arithmetic_greatest_common_denominator(lcm, numbers[i])
        return lcm
    # b
    def base64_encode(data: bytes) -> str:
        import base64
        return base64.b64encode(data).decode("utf-8")
    def base64_decode(data: str) -> bytes:
        import base64
        return base64.decodebytes(data.encode("utf-8"))
    def boolean(value: str):
        return value.lower() in ['y', 'yes', '1', 't', 'true']
    def bytes_format(value: bytes|int, fractionDigits:int = 2) -> str:
        if util.invalidateType(value, "bytes|number"): return ''
        if util.istype(value, "bytes"):
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
    def cartesian_point_in_rectangle(point: tuple[float, float], rectangle: list[tuple[float, float]]) -> bool:
        x, y = point
        xs = [corner[0] for corner in rectangle]
        yx = [corner[1] for corner in rectangle]
        xMin = min(xs)
        xMax = max(xs)
        yMin = min(yx)
        yMax = max(yx)
        return (xMin <= x and x <= xMax) and (yMin <= y and y <= yMax)
    def cartesian_polygon_centroid(points: list[tuple[float, float]]) -> tuple[float, float]:
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
    def cartesian_to_azimuth(point1: tuple[float, float], point2: tuple[float, float]) -> float:
        x1, y1 = point1
        x2, y2 = point2
        dx = x2 - x1
        dy = y2 - y1
        degrees = math.degrees(math.atan2(dy, dx))
        azimuth = (90 - degrees)
        azimuth = util.mathematics_constrain(azimuth, 0, 360)
        return azimuth
    def cartesian_to_cylindrical(point1: tuple[float, float, float], point2: tuple[float, float, float]) -> tuple[float, float, float]:
        x1, y1, z1 = point1
        x2, y2, z2 = point2
        dx = x2 - x1
        dy = y2 - y1
        dz = z2 - z1
        r = (dx**2 + dy**2 + dz**2)**0.5
        azimuth = math.degrees(math.atan2(dy, dx))
        height = math.atan2(dz, r)
        return [r, azimuth, height]
    def cartesian_to_degrees(point1: tuple[float, float], point2: tuple[float, float]) -> float:
        x1, y1 = point1[0], point1[1]
        x2, y2 = point2[0], point2[1]
        dx = x2 - x1
        dy = y2 - y1
        return math.degrees(math.atan2(dy, dx))
    def cartesian_to_distance(point1: tuple[float, float]|tuple[float, float, float], point2: tuple[float, float]|tuple[float, float, float]) -> float:
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
    def cartesian_to_elevation(point1: tuple[float, float, float], point2: tuple[float, float, float]) -> float:
        x1, y1, z1 = point1
        x2, y2, z2 = point2
        dx = x2 - x1
        dy = y2 - y1
        dz = z2 - z1
        r = (dx**2 + dy**2 + dz**2)**0.5
        phi = math.acos(dz / r)
        degrees = math.degrees(phi)
        elevation = 90 - degrees
        return elevation
    def cartesian_in(point: tuple[float, float], polygon: list[tuple[float, float]]) -> bool:
        n = len(polygon)
        inside = False
        j = n - 1
        for i in range(n):
            if (polygon[i][1] <= point[1] and polygon[j][1] >= point[1] or polygon[j][1] <= point[1] and polygon[i][1] >= point[1]):
                if (point[0] <= (polygon[j][0] - polygon[i][0]) * (point[1] - polygon[i][1]) / (polygon[j][1] - polygon[i][1]) + polygon[i][0]):
                    inside = not inside
            j = i
        return inside
    def cartesian_to_midpoint(point1: tuple[float, float]|tuple[float, float, float], point2: tuple[float, float]|tuple[float, float, float]) -> tuple[float, float]:
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
    def cartesian_to_polar(point1: tuple[float, float, float], point2: tuple[float, float, float]) -> tuple[float, float]:
        x1, y1, z1 = point1
        x2, y2, z2 = point2
        dx = x2 - x1
        dy = y2 - y1
        dz = z2 - z1
        r = (dx**2 + dy**2) ** 0.5
        theta = math.atan2(dy, dx)
        return [r, theta]
    def cartesian_to_slope(point1: tuple[float, float], point2: tuple[float, float]) -> float:
        x1, y1 = point1
        x2, y2 = point2
        dx = x2 - x1
        dy = y2 - y1
        return dy / dx
    def cartesian_to_spherical(point1: tuple[float, float, float], point2: tuple[float, float, float]) -> tuple[float, float, float]:
        x1, y1, z1 = point1
        x2, y2, z2 = point2
        dx = x2 - x1
        dy = y2 - y1
        dz = z2 - z1
        r = (dx**2 + dy**2 + dz**2)**0.5
        theta = math.atan2(dy, dx)
        phi = math.acos(dz / r)
        return [r, theta, phi]
    def cartesian_to_theta(point1: tuple[float, float], point2: tuple[float, float]) -> float:
        x1, y1 = point1[0], point1[1]
        x2, y2 = point2[0], point2[1]
        dx = x2 - x1
        dy = y2 - y1
        return math.atan2(dy, dx)
    def clone(value):
        import copy
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
        import csv
        csv_data = []
        reader = csv.reader(csv_string.splitlines())
        headers = next(reader)
        for row in reader:
            row_dict = dict(zip(headers, row))
            csv_data.append(row_dict)
        return csv_data
    def cylindrical_to_cartesian(r: float, azimuth: float, height: float) -> tuple[float, float, float]:
        x = r * math.cos(math.radians(azimuth))
        y = r * math.sin(math.radians(azimuth))
        z = height
        return [x, y, z]
    # d
    def date_to_julian_date(date: datetime.datetime) -> int:
        """
        Converts a Gregorian date to a Julian date.
        The Julian Date is the continuous count of days since the beginning of the
        Julian Period, starting from noon Universal Time on January 1, 4713 BC.
        """
        year = date.year
        month = date.month
        day = date.day
        if month <= 2:
            year -= 1
            month += 12
        # algorithm for Julian Day Number calculation
        a = year // 100
        b = a // 4
        c = 2 - a + b
        e = int(365.25 * (year + 4716))
        f = int(30.6001 * (month + 1))
        julian_day_number = c + day + e + f - 1524
        return julian_day_number

    def dump(value: dict|list, tabs: int = 0):
        def tab(count: int, size: int = 4):
            return " " * count * size
        def get(value, tabs: int = 0) -> str:
            if value == None:
                return "null"
            elif isinstance(value, str):
                return f"'{value}'"
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
        for i in range(0, len(values), 2): filters.append({ "key": values[i], "value": values[i + 1] })
        filtered = []
        for entry in entries:
            matches = 0
            for filter in filters:
                if entry[filter["key"]] == filter["value"]: matches += 1
            if matches == len(filters): filtered.append(entry)
        return filtered
    def entries_filter_or(entries: list[dict], *values) -> list[dict]:
        filters = []
        for i in range(0, len(values), 2): filters.append({ "key": values[i], "value": values[i + 1] })
        filtered = []
        for entry in entries:
            matches = 0
            for filter in filters:
                if entry[filter["key"]] == filter["value"]: matches += 1
            if matches > 0: filtered.append(entry)
        return filtered
    def entries_find(entries: list[dict], *values) -> dict|None:
        return util.entries_find_and(entries, *values)
    def entries_find_and(entries: list[dict], *values) -> dict|None:
        filters = []
        for i in range(0, len(values), 2): filters.append({ "key": values[i], "value": values[i + 1] })
        for i in range(len(entries)):
            matches = 0
            for filter in filters:
                if entries[i][filter["key"]] == filter["value"]: matches += 1
            if matches == len(filters): return { "index": i, "value": entries[i] }
        return None
    def entries_find_or(entries: list[dict], *values) -> dict|None:
        filters = []
        for i in range(0, len(values), 2): filters.append({ "key": values[i], "value": values[i + 1] })
        for i in range(len(entries)):
            matches = 0
            for filter in filters:
                if entries[i][filter["key"]] == filter["value"]: matches += 1
            if matches > 0: return { "index": i, "value": entries[i] }
        return None
    def entries_remove(entries: list[dict], values: list) -> list[dict]:
        identifierKey = ''
        if entries == []:
            return []
        identifierKey = "id" if "id" in entries[0] else "identifier"
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
        else: identifierKey = "id" if "id" in entries[0] else "identifier"
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
        elif isinstance(value, dict|list):
            value = util.json_encode(value)
            assert isinstance(value, str)
            value = value.encode()
        else:
            value = str(value).encode()
        file = open(path, "ab")
        file.write(value)
        file.close()
    def _file_append_json(path: str, value: dict|list):
        if not os.path.isfile(path):
            util.file_write(path, '[]')
        file = open(path, "rb")
        data = file.read().decode()
        file.close()
        if not util.istype(data, "string-array"):
            data = '[]'
        data = util.json_decode(data)
        assert isinstance(data, list)
        data.append(value)
        data = util.json_encode(data)
        assert isinstance(data, str)
        data = data.encode()
        file = open(path, "wb")
        file.write(data)
        file.flush()
        file.close()
    def file_append_json(path: str, value: dict|list):
        if not os.path.isfile(path):
            util.file_write(path, '[]')
        file = open(path, "rb")
        data = file.read().decode()
        file.close()
        data: list = util.json_decode(data)
        data.append(value)
        data: str = util.json_encode(data)
        data = data.encode()
        file = open(path, "wb")
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
                "isdir": 1 if os.path.isdir(path) else 0,
                "items": {},
                "name": name,
                "path": path,
                "size": util.file_size(path),
                "timestamp": util.file_timestamp(path, "milliseconds"),
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
                    items = items[name]["items"]
            for name in folders:
                if isExcludedPath(f"{path}\\{name}"): continue
                items[name] = directoryItem(name, f"{path}\\{name}")
            for name in files:
                if isExcludedPath(f"{path}\\{name}"): continue
                items[name] = directoryItem(name, f"{path}\\{name}")
        return directory
    def file_hash(path: str, mode: str = "md5") -> str:
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
            raise Exception(f"ValueError: hash mode '{mode}' unsupported")
    def __file_read(path: str, size: int = None) -> bytes:
        file = open(path, "rb")
        data = file.read(size)
        file.close()
        return data
    def file_read(path: str, content_type: str = '', size: int = None) -> bytes|dict|list|str:
        try:
            with open(path, "rb") as file:
                data: bytes = file.read(size)
            if content_type == '': return data
            if content_type == "application/json": return json.loads(data)
            if content_type == "text/plain": return data.decode()
        except FileNotFoundError:
            print(f"FileNotFoundError: file '{path}' nonexistent")
        except Exception as e:
            print(f"Error: {e}")
    def file_read_data(path: str) -> dict:
        dataTypes = {
            "list":{
                "lines": "multiple",
                "type": "object",
            },
            "name": {
                "lines": "single",
                "type": "string",
            },
            "reference": {
                "lines": "single",
                "type": "array",
            },
            "subtitle": {
                "lines": "single",
                "type": "string",
            },
            "table": {
                "lines": "multiple",
                "type": "object",
            },
            "title": {
                "lines": "single",
                "type": "string",
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
            if key == "list":
                return [(line.strip(' ')) for line in string.split('\n')]
            if key == "name":
                return string
            if key == "reference":
                return [(substring.strip(' ')) for substring in string.split(',')]
            if key == "subtitle":
                return string
            if key == "table":
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
            if key == "title":
                return string
        def decode(string: str):
            data = {}
            lines = string.replace('\r', '').split('\n')
            index = 0
            for key, dataType in dataTypes.items():
                if dataType["type"] == "array":
                    data[key] = []
                if dataType["type"] == "object":
                    data[key] = {}
                if dataType["type"] == "string":
                    data[key] = ''
            while index < len(lines):
                line = lines[index]
                for key, dataType in dataTypes.items():
                    if hasKey(key, line):
                        keyvalue = line[len(key) + 1:len(line)].strip(' ')
                        value = None
                        if dataType["lines"] == "single":
                            value = getValue(key, keyvalue)
                        if dataType["lines"] == "multiple":
                            value, index = getLines(lines, index + 1)
                            value = getValue(key, value)
                        if dataType["type"] == "array":
                            data[key].append(value)
                        if dataType["type"] == "object":
                            data[key][keyvalue] = value
                        if dataType["type"] == "string":
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
        return os.path.getsize(path) # bytes
    def file_timestamp(path: str, options: str = "milliseconds") -> int:
        # returns milliseconds
        if options == "milliseconds":
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
        changedFilename = False
        pathInfo = util.path_info(path)
        filename: str = pathInfo["filename"]
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
            value = json.dumps(value).encode()
        else:
            value = str(value).encode()
        file = open(path, "wb")
        file.write(value)
        file.close()
    def file_write_data(path: str, data: dict):
        pass
    def file_write_list(path: str, value: list):
        value = '\n'.join(value).encode()
        util.file_write(path, value)
    def fraction_to_percentage(numerator: float, denominator: float) -> float:
        return round(numerator / denominator * 100, 3)
    # g
    def geographic_ddd_to_ddm(*point) -> list[str]:
        point = point[0] if len(point) == 1 else list(point)
        if not util.istype(point, "coordinates-geographic-ddd"):
            raise Exception(f"ValueError: geographic coordinate invalid")
        point = [float(point[0]), float(point[1])]
        direction = 'N' if point[0] >= 0 else 'S'
        degrees = int(abs(point[0]))
        minutes = int((abs(point[0]) - degrees) * 60)
        seconds = int(round((abs(point[0]) - degrees - minutes / 60) * 3600, 0))
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            degrees += 1
        decimal_minutes = minutes + seconds/60
        latitude = f"{degrees:02d}{decimal_minutes:05.2f}{direction}"
        direction = 'E' if point[1] >= 0 else 'W'
        degrees = int(abs(point[1]))
        minutes = int((abs(point[1]) - degrees) * 60)
        seconds = int(round((abs(point[1]) - degrees - minutes / 60) * 3600, 0))
        if seconds == 60:
            minutes += 1
            seconds = 0
        if minutes == 60:
            degrees += 1
            minutes = 0
        decimal_minutes = minutes + seconds/60
        longitude = f"{degrees:03d}{decimal_minutes:05.2f}{direction}"
        return [latitude, longitude]
    def geographic_ddd_to_dms(*point) -> list[str]:
        point = point[0] if len(point) == 1 else list(point)
        if not util.istype(point, "coordinates-geographic-ddd"):
            raise Exception(f"ValueError: geographic coordinate invalid")
        point = [float(point[0]), float(point[1])]
        direction = 'N' if point[0] >= 0 else 'S'
        degrees = int(abs(point[0]))
        minutes = int((abs(point[0]) - degrees) * 60)
        seconds = int(round((abs(point[0]) - degrees - minutes / 60) * 3600, 0))
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            degrees += 1
        latitude = f"{degrees:02d}{minutes:02d}{seconds:02d}{direction}"
        direction = 'E' if point[1] >= 0 else 'W'
        degrees = int(abs(point[1]))
        minutes = int((abs(point[1]) - degrees) * 60)
        seconds = int(round((abs(point[1]) - degrees - minutes / 60) * 3600, 0))
        if seconds == 60:
            minutes += 1
            seconds = 0
        if minutes == 60:
            degrees += 1
            minutes = 0
        longitude = f"{degrees:03d}{minutes:02d}{seconds:02d}{direction}"
        return [latitude, longitude]
    def geographic_ddm_to_ddd(*point) -> list[str]:
        point = point[0] if len(point) == 1 else list(point)
        if not util.istype(point, "coordinates-geographic-ddm"):
            raise Exception(f"ValueError: geographic coordinate invalid")
        pattern = f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LATITUDE_OPT1}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_DECIMAL_OPT1}" if not ('*' in point[0] or '°' in point[0] or 'º' in point[0]) else f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LATITUDE_OPT2}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_DECIMAL_OPT2}"
        pattern = f"^{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LATITUDE}{pattern}$" if (point[0][0] == 'N' or point[0][0] == 'S') else f"^{pattern}{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LATITUDE}$"
        match = re.match(pattern, point[0])
        groups = match.groupdict()
        direction = groups["direction"]
        degrees = int(groups["degrees"])
        minutes = float(groups["decimal_minutes"])
        decimal_degrees = degrees + minutes/60
        decimal_degrees *= 1 if direction == 'N' else -1
        latitude = f"{decimal_degrees:.6f}"
        pattern = f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LONGITUDE_OPT1}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_DECIMAL_OPT1}" if not ('*' in point[1] or '°' in point[1] or 'º' in point[1]) else f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LONGITUDE_OPT2}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_DECIMAL_OPT2}"
        pattern = f"^{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LONGITUDE}{pattern}$" if (point[1][0] == 'E' or point[1][0] == 'W') else f"^{pattern}{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LONGITUDE}$"
        match = re.match(pattern, point[1])
        groups = match.groupdict()
        direction = groups["direction"]
        degrees = int(groups["degrees"])
        minutes = float(groups["decimal_minutes"])
        decimal_degrees = degrees + minutes/60
        decimal_degrees *= 1 if direction == 'E' else -1
        longitude = f"{decimal_degrees:.6f}"
        return [latitude, longitude]
    def geographic_ddm_to_dms(*point) -> list[str]:
        point = point[0] if len(point) == 1 else list(point)
        if not util.istype(point, "coordinates-geographic-ddm"):
            raise Exception(f"ValueError: geographic coordinate invalid")
        pattern = f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LATITUDE_OPT1}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_DECIMAL_OPT1}" if not ('*' in point[0] or '°' in point[0] or 'º' in point[0]) else f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LATITUDE_OPT2}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_DECIMAL_OPT2}"
        pattern = f"^{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LATITUDE}{pattern}$" if (point[0][0] == 'N' or point[0][0] == 'S') else f"^{pattern}{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LATITUDE}$"
        match = re.match(pattern, point[0])
        groups = match.groupdict()
        direction = groups["direction"]
        degrees = int(groups["degrees"])
        minutes = float(groups["decimal_minutes"])
        decimal_degrees = degrees + minutes/60
        decimal_degrees *= 1 if direction == 'N' else -1
        latitude = f"{decimal_degrees}"
        pattern = f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LONGITUDE_OPT1}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_DECIMAL_OPT1}" if not ('*' in point[1] or '°' in point[1] or 'º' in point[1]) else f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LONGITUDE_OPT2}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_DECIMAL_OPT2}"
        pattern = f"^{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LONGITUDE}{pattern}$" if (point[1][0] == 'E' or point[1][0] == 'W') else f"^{pattern}{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LONGITUDE}$"
        match = re.match(pattern, point[1])
        groups = match.groupdict()
        direction = groups["direction"]
        degrees = int(groups["degrees"])
        minutes = float(groups["decimal_minutes"])
        decimal_degrees = degrees + minutes/60
        decimal_degrees *= 1 if direction == 'E' else -1
        longitude = f"{decimal_degrees}"
        return util.geographic_ddd_to_dms([latitude, longitude])
    def geographic_dms_to_ddd(*point) -> list[str]:
        point = point[0] if len(point) == 1 else list(point)
        if not util.istype(point, "coordinates-geographic-dms"):
            raise Exception(f"ValueError: geographic coordinate invalid")
        pattern = f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LATITUDE_OPT1}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_OPT1}{util.GEOGRAPHIC_COORDINATES_PATTERN_SECONDS_OPT1}" if not ('*' in point[0] or '°' in point[0] or 'º' in point[0]) else f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LATITUDE_OPT2}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_OPT2}{util.GEOGRAPHIC_COORDINATES_PATTERN_SECONDS_OPT2}"
        pattern = f"^{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LATITUDE}{pattern}$" if (point[0][0] == 'N' or point[0][0] == 'S') else f"^{pattern}{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LATITUDE}$"
        match = re.match(pattern, point[0])
        groups = match.groupdict()
        direction = groups["direction"]
        degrees = int(groups["degrees"])
        minutes = int(groups["minutes"])
        seconds = float(groups["seconds"])
        decimal_degrees = degrees + minutes/60 + seconds/3600
        decimal_degrees *= 1 if direction == 'N' else -1
        latitude = f"{decimal_degrees:.6f}"
        pattern = f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LONGITUDE_OPT1}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_OPT1}{util.GEOGRAPHIC_COORDINATES_PATTERN_SECONDS_OPT1}" if not ('*' in point[1] or '°' in point[1] or 'º' in point[1]) else f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LONGITUDE_OPT2}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_OPT2}{util.GEOGRAPHIC_COORDINATES_PATTERN_SECONDS_OPT2}"
        pattern = f"^{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LONGITUDE}{pattern}$" if (point[1][0] == 'E' or point[1][0] == 'W') else f"^{pattern}{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LONGITUDE}$"
        match = re.match(pattern, point[1])
        groups = match.groupdict()
        direction = groups["direction"]
        degrees = int(groups["degrees"])
        minutes = int(groups["minutes"])
        seconds = float(groups["seconds"])
        decimal_degrees = degrees + minutes/60 + seconds/3600
        decimal_degrees *= 1 if direction == 'E' else -1
        longitude = f"{decimal_degrees:.6f}"
        return [latitude, longitude]
    def geographic_dms_to_ddm(*point) -> list[str]:
        point = point[0] if len(point) == 1 else list(point)
        if not util.istype(point, "coordinates-geographic-dms"):
            raise Exception(f"ValueError: geographic coordinate invalid")
        pattern = f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LATITUDE_OPT1}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_OPT1}{util.GEOGRAPHIC_COORDINATES_PATTERN_SECONDS_OPT1}" if not ('*' in point[0] or '°' in point[0] or 'º' in point[0]) else f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LATITUDE_OPT2}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_OPT2}{util.GEOGRAPHIC_COORDINATES_PATTERN_SECONDS_OPT2}"
        pattern = f"^{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LATITUDE}{pattern}$" if (point[0][0] == 'N' or point[0][0] == 'S') else f"^{pattern}{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LATITUDE}$"
        match = re.match(pattern, point[0])
        groups = match.groupdict()
        direction = groups["direction"]
        degrees = int(groups["degrees"])
        minutes = int(groups["minutes"])
        seconds = float(groups["seconds"])
        decimal_minutes = minutes + seconds/60
        latitude = f"{degrees:02d}{decimal_minutes:05.2f}{direction}"
        pattern = f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LONGITUDE_OPT1}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_OPT1}{util.GEOGRAPHIC_COORDINATES_PATTERN_SECONDS_OPT1}" if not ('*' in point[1] or '°' in point[1] or 'º' in point[1]) else f"{util.GEOGRAPHIC_COORDINATES_PATTERN_DEGREES_LONGITUDE_OPT2}{util.GEOGRAPHIC_COORDINATES_PATTERN_MINUTES_OPT2}{util.GEOGRAPHIC_COORDINATES_PATTERN_SECONDS_OPT2}"
        pattern = f"^{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LONGITUDE}{pattern}$" if (point[1][0] == 'E' or point[1][0] == 'W') else f"^{pattern}{util.GEOGRAPHIC_COORDINATES_PATTERN_DIRECTION_LONGITUDE}$"
        match = re.match(pattern, point[1])
        groups = match.groupdict()
        direction = groups["direction"]
        degrees = int(groups["degrees"])
        minutes = int(groups["minutes"])
        seconds = float(groups["seconds"])
        decimal_minutes = minutes + seconds/60
        longitude = f"{degrees:03d}{decimal_minutes:05.2f}{direction}"
        return [latitude, longitude]
    def geographic_to_azimuth(point1: list[float], point2: list[float]) -> float:
        latitude1 = math.radians(point1[0])
        longitude1 = math.radians(point1[1])
        latitude2 = math.radians(point2[0])
        longitude2 = math.radians(point2[1])
        differenceLatitude = latitude2 - latitude1
        differenceLongitude = longitude2 - longitude1
        y = math.sin(differenceLongitude) * math.cos(latitude2)
        x = math.cos(latitude1) * math.sin(latitude2) - math.sin(latitude1) * math.cos(latitude2) * math.cos(differenceLongitude)
        theta = math.atan2(y, x)
        theta = util.mathematics_constrain(theta, 0, math.pi * 2)
        azimuth = math.degrees(theta)
        return azimuth
    def geographic_to_azimuth_rhumb(point1: list[float], point2: list[float]) -> float:
        latitude1 = math.radians(point1[0])
        longitude1 = math.radians(point1[1])
        latitude2 = math.radians(point2[0])
        longitude2 = math.radians(point2[1])
        differenceLatitude = latitude2 - latitude1
        differenceLongitude = longitude2 - longitude1
        if abs(differenceLongitude) > math.pi:
            differenceLongitude = -(2 * math.pi - differenceLongitude) if differenceLongitude > 0 else (2 * math.pi + differenceLongitude)
        aa = math.log(math.tan(latitude2 / 2 + math.pi / 4) / math.tan(latitude1 / 2 + math.pi / 4))
        theta = math.atan2(differenceLongitude, aa)
        theta = util.mathematics_constrain(theta, 0, math.pi * 2)
        azimuth = math.degrees(theta)
        return azimuth
    def geographic_to_cartesian(latitude: float, longitude: float, altitude: float) -> list[float]:
        r = util.SPHERE_RADIUS + altitude
        theta = math.radians(longitude if longitude >= 0 else 360 + longitude)
        phi = math.radians(90 - latitude)
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
        latitude = math.radians(point[0])
        longitude = math.radians(point[1])
        theta = math.radians(azimuth)
        angularDistance = distance / util.SPHERE_RADIUS
        destinationLatitude = math.asin(math.sin(latitude) * math.cos(angularDistance) + math.cos(latitude) * math.sin(angularDistance) * math.cos(theta))
        destinationLongitude = longitude + math.atan2(math.sin(theta) * math.sin(angularDistance) * math.cos(latitude), math.cos(angularDistance) - math.sin(latitude) * math.sin(destinationLatitude))
        destinationLatitude *= (180/math.pi)
        destinationLongitude *= (180/math.pi)
        return [destinationLatitude, destinationLongitude]
    def geographic_to_distance(point1: list[float], point2: list[float]) -> float:
        # distance along the surface of the earth from source point to destination point, great circle (shortest distance)
        # haversine formula
        latitude1 = math.radians(point1[0])
        longitude1 = math.radians(point1[1])
        latitude2 = math.radians(point2[0])
        longitude2 = math.radians(point2[1])
        differenceLatitude = latitude2 - latitude1
        differenceLongitude = longitude2 - longitude1
        a = math.sin(differenceLatitude / 2) ** 2 + math.cos(latitude1) * math.cos(latitude2) * math.sin(differenceLongitude / 2) ** 2
        c = 2 * math.atan2(a ** 0.5, (1 - a) ** 0.5)
        distance = util.SPHERE_RADIUS * c
        return distance
    def geographic_to_distance_offset(point: list[float], pointStart: list[float], pointEnd: list[float]) -> float: # inaccurate
        # distance of a point from a great-circle path (sometimes called cross track error)
        angularDistance = util.geographic_to_distance(pointStart, point) / util.SPHERE_RADIUS
        deg1 = util.geographic_to_azimuth(pointStart, point)
        deg2 = util.geographic_to_azimuth(pointStart, pointEnd)
        aa = math.asin(math.sin(angularDistance) * math.sin(math.radians(deg1) - math.radians(deg2)))
        return aa * util.SPHERE_RADIUS
    def geographic_to_distance_rhumb(point1: list[float], point2: list[float]) -> float:
        # distance traveling from starting point to destination point along a rhumb line
        latitude1 = math.radians(point1[0])
        longitude1 = math.radians(point1[1])
        latitude2 = math.radians(point2[0])
        longitude2 = math.radians(point2[1])
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
        latitude1 = math.radians(point1[0])
        longitude1 = math.radians(point1[1])
        latitude2 = math.radians(point2[0])
        longitude2 = math.radians(point2[1])
        a = math.sin((1 - fractionOfDistance) * distance) / math.sin(distance)
        b = math.sin(fractionOfDistance * distance) / math.sin(distance)
        x = a * math.cos(latitude1) * math.cos(longitude1) + b * math.cos(latitude2) * math.cos(longitude2)
        y = a * math.cos(latitude1) * math.sin(longitude1) + b * math.cos(latitude2) * math.sin(longitude2)
        z = a * math.sin(latitude1) + b * math.sin(latitude2)
        latitude = math.atan2(z, (x ** 2 + y ** 2) ** 0.5) * (180/math.pi)
        longitude = math.atan2(y, x) * (180/math.pi)
        return [latitude, longitude]
    def geographic_to_intersection_point(point1: list[float], azimuth1: float, point2: list[float], azimuth2: float) -> list[float]|None:
        # point of intersection of two paths defined by point and bearing
        latitude1 = math.radians(point1[0])
        longitude1 = math.radians(point1[1])
        latitude2 = math.radians(point2[0])
        longitude2 = math.radians(point2[1])
        differenceLatitude = latitude2 - latitude1
        differenceLongitude = longitude2 - longitude1
        theta1 = math.radians(azimuth1)
        theta2 = math.radians(azimuth2)
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
        destinationLatitude *= (180/math.pi)
        destinationLongitude *= (180/math.pi)
        return [destinationLatitude, destinationLongitude]
    def _geographic_to_midpoint(point1: list[float], point2: list[float]) -> list[float]:
        latitude1 = math.radians(point1[0])
        longitude1 = math.radians(point1[1])
        latitude2 = math.radians(point2[0])
        longitude2 = math.radians(point2[1])
        differenceLatitude = latitude2 - latitude1
        differenceLongitude = longitude2 - longitude1
        bx = math.cos(latitude2) * math.cos(differenceLatitude)
        by = math.cos(latitude2) * math.sin(differenceLatitude)
        latitude = math.atan2(math.sin(latitude1) + math.sin(latitude2), ((math.cos(latitude1) + bx) ** 2 + by ** 2) ** 0.5) * (180/math.pi)
        longitude = point1[1] + (math.atan2(by, math.cos(longitude1) + bx) * (180/math.pi))
        return [latitude, longitude]
    def geographic_to_midpoint(point1: list[float], point2: list[float]) -> list[float]:
        azimuth = util.geographic_to_azimuth(point1, point2)
        distance = util.geographic_to_distance(point1, point2)
        latitude, longitude = util.geographic_to_destination_point(point1, azimuth, distance/2)
        return [latitude, longitude]
    def geographic_to_spherical(latitude: float, longitude: float, altitude: float) -> list[float]:
        r = util.SPHERE_RADIUS + altitude
        theta = math.radians(longitude if longitude >= 0 else 360 + longitude)
        phi = math.radians(90 - latitude)
        return [r, theta, phi]
    def geometry_area_circle(radius: float) -> float:
        return math.pi * radius ** 2
    def geometry_area_cone(radius: float, height: float) -> float:
        return (math.pi * radius) * (radius + (height ** 2 + radius ** 2) ** 0.5)
    def geometry_area_cube(side: float) -> float:
        return 6 * side ** 2
    def geometry_area_cuboid(length: float, width: float, height: float) -> float:
        return 2 * (length * width + width * height + length * height)
    def geometry_area_cylinder(radius: float, height: float) -> float:
        return 2 * math.pi * radius * height + 2 * math.pi * radius ** 2
    def geometry_area_octagon(side: float):
        return 2 * (1 + 2 ** 0.5) * side ** 2
    def geometry_area_parallelogram(base: float, height: float) -> float:
        return base * height
    def geometry_area_rectangle(length: float, width: float) -> float:
        return length * width
    def geometry_area_semicircle(radius: float) -> float:
        return (math.pi * radius ** 2) / 2
    def geometry_area_sphere(radius: float) -> float:
        return 4 * math.pi * radius ^ 2
    def geometry_area_square(length: float) -> float:
        return length ** 2
    def geometry_area_trapezoid(base_1, base_2, height):
        return (base_1 + base_2) / 2 * height
    def geometry_area_triangle(base: float, height: float) -> float:
        return (base * height) / 2
    def geometry_distance_formula(point1: list[float], point2: list[float]) -> float:
        return util.cartesian_to_distance(point1, point2)
    def geometry_midpoint_formula(point1: list[float], point2: list[float]) -> float:
        return util.cartesian_to_midpoint(point1, point2)
    def geometry_perimeter_circle(radius: float) -> float:
        return 2 * math.pi * radius
    def geometry_perimeter_octagon(side: float) -> float:
        return 8 * side
    def geometry_perimeter_parallelogram(side: float, base: float) -> float:
        return 2 * (side + base)
    def geometry_perimeter_rectangle(length: float, width: float) -> float:
        return 2 * (length + width)
    def geometry_perimeter_semicircle(radius: float) -> float:
        return (math.pi * radius) + 2 * radius
    def geometry_perimeter_square(side: float) -> float:
        return 4 * side
    def geometry_perimeter_triangle(sideA: float, sideB: float, sideC: float) -> float:
        return sideA + sideB + sideC
    def geometry_pythagorean_theorem(a: float = None, b: float = None, c: float = None) -> float:
        if a and b:
            return math.sqrt(a**2+b**2)
        if b and c:
            return math.sqrt(c**2-b**2)
        if c and a:
            return math.sqrt(c**2-a**2)
    def geometry_triangle_calculator(a: float = None, b: float = None, c: float = None, A: float = None, B: float = None, C: float = None) -> dict:
        def solution(side_a, side_b, side_c, angle_a, angle_b, angle_c):
            return {
                'a': side_a, 'b': side_b, 'c': side_c,
                'A': math.degrees(angle_a), 'B': math.degrees(angle_b), 'C': math.degrees(angle_c)
            }
        # input validation: parameter count
        sides_known = sum(1 for side in [a, b, c] if side is not None)
        angles_known = sum(1 for angle in [A, B, C] if angle is not None)
        if not (sides_known + angles_known) == 3:
            raise Exception("ValueError: require 3 parameters")
        # convert all known angles to radians
        rad_A = math.radians(A) if A is not None else None
        rad_B = math.radians(B) if B is not None else None
        rad_C = math.radians(C) if C is not None else None
        if sides_known == 3:
            # input validation: Triangle Inequality Theorem
            if a + b <= c or a + c <= b or b + c <= a:
                return []
            rad_A = math.acos((b**2+c**2-a**2)/(2*b*c))
            rad_B = math.acos((a**2+c**2-b**2)/(2*a*c))
            rad_C = math.pi - rad_A - rad_B
            return solution(a, b, c, rad_A, rad_B, rad_C)
        elif sides_known == 2 and angles_known == 1:
            if a and b and A:
                rad_B = math.asin((b*math.sin(rad_A))/a) # possibility 1
                # rad_B = math.pi - math.asin((b*math.sin(rad_A))/a) # possibility 2
                print('calculation produced 2 possibilities, see function')
                rad_C = math.pi - rad_A - rad_B
                c = (a*math.sin(rad_C))/math.sin(rad_A)
            elif a and b and B:
                rad_A = math.asin((a*math.sin(rad_B))/b)
                rad_C = math.pi - rad_A - rad_B
                c = (b*math.sin(rad_C))/math.sin(rad_B)
            elif a and b and C:
                c = math.sqrt(a**2+b**2-2*a*b*math.cos(rad_C))
                rad_A = math.acos((b**2+c**2-a**2)/(2*b*c))
                rad_B = math.pi - rad_A - rad_C
            elif a and c and A:
                rad_C = math.asin((c*math.sin(rad_A))/a) # possibility 1
                # rad_C = math.pi - math.asin((c*math.sin(rad_A))/a) # possibility 2
                print('calculation produced 2 possibilities, see function')
                rad_B = math.pi - rad_A - rad_C
                b = (a*math.sin(rad_B))/math.sin(rad_A)
            elif a and c and B:
                b = math.sqrt(a**2+c**2-2*a*c*math.cos(rad_B))
                rad_A = math.acos((b**2+c**2-a**2)/(2*b*c))
                rad_C = math.pi - rad_A - rad_B
            elif a and c and C:
                rad_A = math.asin((a*math.sin(rad_C))/c)
                rad_B = math.pi - rad_A - rad_C
                b = ((c*math.sin(rad_B))/math.sin(rad_C))
            elif b and c and A:
                a = math.sqrt(b**2+c**2-2*b*c*math.cos(rad_A))
                rad_B = math.acos((a**2+c**2-b**2)/(2*a*c))
                rad_C = math.pi - rad_A - rad_B
            elif b and c and B:
                rad_C = math.asin((c*math.sin(rad_B))/b)
                rad_B = math.pi - rad_A - rad_C
                a = (b*math.sin(rad_A))/math.sin(rad_B)
            elif b and c and C:
                rad_B = math.asin((b*math.sin(rad_C))/c) # possibility 1
                # rad_B = math.pi - math.asin((b*math.sin(rad_C))/c) # possibility 2
                print('calculation produced 2 possibilities, see function')
                rad_A = math.pi - rad_C - rad_B
                a = (c*math.sin(rad_A))/math.sin(rad_C)
            return solution(a, b, c, rad_A, rad_B, rad_C)
        elif sides_known == 1 and angles_known == 2:
            if A is None:
                rad_A = math.pi - rad_B - rad_C
            elif B is None:
                rad_B = math.pi - rad_A - rad_C
            elif C is None:
                rad_C = math.pi - rad_A - rad_B
            if a:
                b = a*math.sin(rad_B)/math.sin(rad_A)
                c = a*math.sin(rad_C)/math.sin(rad_A)
            elif b:
                a = b*math.sin(rad_A)/math.sin(rad_B)
                c = b*math.sin(rad_C)/math.sin(rad_B)
            elif c:
                a = c*math.sin(rad_A)/math.sin(rad_C)
                b = c*math.sin(rad_B)/math.sin(rad_C)
            return solution(a, b, c, rad_A, rad_B, rad_C)
    def geometry_volume_cone(radius: float, height: float) -> float:
        return math.pi * radius ** 2 * (height / 3)
    def geometry_volume_cube(side: float) -> float:
        return side ** 3
    def geometry_volume_cylinder(radius: float, height: float) -> float:
        return math.pi * radius ** 2 * height
    def geometry_volume_cylinder_hollow(radius_outer: float, radius_inner: float, height: float) -> float:
        return math.pi * (radius_outer ** 2 - radius_inner ** 2) * height
    def geometry_volume_rectangle(length: float, width: float, height: float) -> float:
        return length * width * height
    def geometry_volume_sphere(radius: float) -> float:
        return (4/3) * math.pi * radius ** 3
    def geometry_volume_triangular_prism(side_1: float, side_2: float, side_3: float, height) -> float:
        return 0.25 * height * (-side_1 ** 4 + 2 * (side_1 * side_2) ** 2 + 2 * (side_1 * side_3) ** 2 - side_2 ** 4 + 2 * (side_2 * side_3) ** 2 - side_3 ** 4) ** 0.5
    # h
    def hash_md5(value: bytes|str) -> str:
        import hashlib
        return hashlib.md5(value if type(value) == bytes else value.encode()).hexdigest()
    def hash_sha1(value: bytes|str) -> str:
        import hashlib
        return hashlib.sha1(value if type(value) == bytes else value.encode()).hexdigest()
    def hash_sha224(value: bytes|str) -> str:
        import hashlib
        return hashlib.sha224(value if type(value) == bytes else value.encode()).hexdigest()
    def hash_sha256(value: bytes|str) -> str:
        import hashlib
        return hashlib.sha256(value if type(value) == bytes else value.encode()).hexdigest()
    def hash_sha384(value: bytes|str) -> str:
        import hashlib
        return hashlib.sha384(value if type(value) == bytes else value.encode()).hexdigest()
    def hash_sha512(value: bytes|str) -> str:
        import hashlib
        return hashlib.sha512(value if type(value) == bytes else value.encode()).hexdigest()
    def hex_to_brightness(color: str) -> float:
        # calculate hex color perceived brightness or luma (W3C/WCAG ITU-R BT.709 - HD), not linearized
        # normalized from 0 (darkest) to 1 (lightest)
        hex_color = color.lstrip("#")
        # convert 3-digit hex to 6-digit
        if len(hex_color) == 3:
            hex_color = ''.join([char + char for char in hex_color.split('')])
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        return (r * 0.2126 + g * 0.7152 + b * 0.0722) / 255
    def hex_to_relative_luminance(color: str) -> float:
        # calculate hex color relative luminance or perceived brightness (W3C/WCAG ITU-R BT.709 - HD), linearized
        # normalized from 0 (darkest) to 1 (lightest)
        hex_color = color.lstrip("#")
        # convert 3-digit hex to 6-digit
        if len(hex_color) == 3:
            hex_color = ''.join([char + char for char in hex_color.split('')])
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        def linearize(c):
            c = c / 255.0
            if c <= 0.03928: return c / 12.92
            else: return ((c + 0.055) / 1.055) ** 2.4
        r = linearize(r)
        g = linearize(g)
        b = linearize(b)
        return (r * 0.2126 + g * 0.7152 + b * 0.0722)
    def hex_to_rgb(color: str) -> tuple[int, int, int]:
        hex_color = color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    def __hex_from_brightness(color: str, brightness_factor: float) -> str:
        # adjusts relative luminance of a hex color by using luminance factor (interpolated scaling)
        # relative luminance defined using number between 0 to 1, 0.0 = black, 0.5 = original, 1.0 = white
        # factor < 0.5: darken
        # factor > 0.5: lighten
        hex_color = color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4)) # normalize (0-1)
        # multiplier on current brightness, map 0-1 to -1-1
        adjustment = max(-1.0, min(1.0, (brightness_factor - 0.5) * 2))
        if adjustment > 0: # lighten
            r = min(255, r + (255 - r) * adjustment)
            g = min(255, g + (255 - g) * adjustment)
            b = min(255, b + (255 - b) * adjustment)
        elif adjustment < 0: # darken
            r = max(0.0, r + r * adjustment)
            g = max(0.0, g + g * adjustment)
            b = max(0.0, b + b * adjustment)
        # adding 0.5 before casting to int mimics a proper round-to-nearest operation
        return "#{:02x}{:02x}{:02x}".format(int(r + 0.5), int(g + 0.5), int(b + 0.5))
    def hex_from_brightness(color: str, brightness_factor: float) -> str:
        # adjusts relative luminance of a hex color by using luminance factor (interpolated scaling)
        # relative luminance defined using number between 0 to 1, 0.0 = black, 0.5 = original, 1.0 = white
        # factor < 0.5: darken
        # factor > 0.5: lighten
        hex_color = color.lstrip('#')
        rgb = [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]
        # multiplier on current brightness, map 0-1 to -1-1
        adjustment = max(-1.0, min(1.0, (brightness_factor - 0.5) * 2))
        new_rgb = []
        for channel in rgb:
            # adjustment > 0: lighten. adjustment < 0: darken
            target = 255 if adjustment > 0 else 0
            shifted = channel + (target - channel) * abs(adjustment)
            # adding 0.5 before casting to int mimics a proper round-to-nearest operation
            new_rgb.append(int(shifted + 0.5))
        return "#{:02x}{:02x}{:02x}".format(*new_rgb)
    def hex_from_brightness_linear(color: str, brightness_factor: float) -> str:
        # adjusts relative luminance of a hex color by using scaling factor (linear scaling)
        # relative luminance defined using number between 0 to 1
        # factor < 1: darken
        # factor > 1: lighten
        hex_color = color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        r = max(0, min(255, r * brightness_factor))
        g = max(0, min(255, g * brightness_factor))
        b = max(0, min(255, b * brightness_factor))
        return "#{:02x}{:02x}{:02x}".format(int(r), int(g), int(b))
    def html_decode(string: str) -> dict:
        pass
    def html_encode(object: dict) -> str:
        pass
    # i
    def identifier(value: str = None) -> str:
        if value:
            nString = ''
            allowedCharacters = "- 0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z _ a b c d e f g h i j k l m n o p q r s t u v w x y z".split(' ')
            notAllowedFirstCharacters = "0 1 2 3 4 5 6 7 8 9".split(' ')
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
            allowedFirstCharacters = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(' ')
            allowedCharacters = "0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z".split(' ')
            identifier = ''
            identifier += util.random(allowedFirstCharacters)
            for i in range(0, 9, 1):
                identifier += util.random(allowedCharacters)
            return identifier
    # j
    def javascript_run(path: str):
        import js2py
        # runs in only ECMAScript 5
        return js2py.eval_js(path)
    def json_encode(value: dict|list) -> str:
        try:
            return json.dumps(value)
        except:
            raise Exception(f"Error: json encoding unsuccessful")
    def json_decode(value: str) -> dict|list:
        try:
            return json.loads(value)
        except:
            raise Exception(f"Error: json decoding unsuccessful")
    # k

    # l
    def len(value, base: int = 1) -> int:
        return util.mathematics_block_count(value, base)
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
    def mathematics_block_count(value: dict|int|list, base: int = 1) -> int:
        """
        Calculates the number of full blocks (segments) of size 'base'
        that can be fit into the total length of the input 'value'.
        """
        if value == None: return 0
        return len(value) // base
    def mathematics_number_to_decimal_notation(argument) -> str:
        if isinstance(argument, float|int):
            number = argument
        elif isinstance(argument, str):
            number = eval(argument)
        else: 
            number = 0
        return f"{number:.15f}".rstrip('0').rstrip('.')
    def mathematics_number_to_scientific_notation(argument) -> str:
        number = util.mathematics_number_to_decimal_notation(argument)
        bDigits, aDigits = number.split('.') if '.' in number else [number, ""]
        # whole number
        if len(aDigits) == 0:
            significate_digits = bDigits.rstrip("0")
            precision = len(significate_digits)-1
        # decimal number (less than 1)
        elif bDigits == "0" and len(aDigits) > 0:
            significate_digits = aDigits.lstrip("0")
            precision = len(significate_digits)-1
        # decimal number (greater than 1)
        else:
            significate_digits = aDigits + bDigits
            precision = len(significate_digits)-1
        formatting = "{:." + f"{precision}" + "e}"
        return formatting.format(float(number))
    def mathematics_number_placement(argument) -> int:
        if isinstance(argument, float|int):
            number = argument
        elif isinstance(argument, str):
            number = eval(argument)
        else: 
            number = 0
        placement = 0
        while True:
            n = number * 10**placement
            # handle floating-point imprecision
            n = float(re.sub(r"\.?0{5,}[1-9]$", r"", f"{n}"))
            if (n < 1 if number >= 1 else int(n) == n): break
            placement += -1 if number >= 1 else 1
        return -placement
    def mathematics_random(*values):
        import random
        # 1. list item
        if isinstance(values[0], list):
            index = random.randint(0, len(values[0])-1)
            return values[0][index]
        # 2. number range
        number_range = [0, values[0]] if len(values) == 1 else [values[0], values[1]]
        if len(values) == 1 or len(values) == 2:
            multiple = 1
            while True:
                if all(int(n*multiple) == n*multiple for n in number_range): break
                multiple = multiple*10
            number_range = [int(number_range[0]*multiple), int(number_range[1]*multiple)]
            return random.randint(number_range[0], number_range[1])/multiple
        # 3. number range + round to nth place
        if len(values) == 3:
            if values[0] == values[1]: return values[0]
            placement = values[2]
            if placement > 0:
                random_number = random.randint(number_range[0], number_range[1])
                return util.mathematics_round(random_number, placement)
            if placement < 0:
                multiple = 10**-placement
                number_range = [int(number_range[0]*multiple), int(number_range[1]*multiple)]
                random_number = random.randint(number_range[0], number_range[1])
                return util.mathematics_round(random_number, placement) / multiple
    def mathematics_round(number: float, placement: int = 1) -> int|float:
        multiplier = 10**placement
        if placement > 0:
            number = round(number / multiplier, 1) * multiplier
            # correct floating point precision errors when handling large numbers
            number = round(number)
        elif placement < 0:
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
    def network_online(address: tuple = ("8.8.8.8", 53)) -> bool:
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
    def numerical_solver(function, initial_guess, tolerance=1e-9, direction = 1, magnitude = 1.0, magnitude_decrease = 0.1, magnitude_increase = 2.0, optimization = 50, max_iterations=10000, **kwargs) -> float:
        # linear heuristic search-based root finder (adaptive "trial and error" step-search method)
        # prevent infinite local minimum oscillations (max_iterations)
        # the function only knows the value error
        x = initial_guess
        # direction control: smaller error = maintain direction, larger error = reverse direction
        # step control: direction maintained = accelerate, direction changed = decelerate
        #   changing direction (larger error) suggest passing the correct answer
        #   maintaining direction (smaller error) suggest a movement towards the correct answer
        consecutive_steps = 0
        error = 0
        error_previous, kwargs = function(x, kwargs)
        error_previous = abs(error_previous)
        for iteration in range(1, max_iterations + 1):
            if iteration == max_iterations: print("Error: numerical solver reached maximum iteration")
            # calculate current error
            error, kwargs = function(x, kwargs)
            error = abs(error)
            if error <= tolerance:
                return x, kwargs
            # error increase (overshot): flip direction and decrease speed
            # precision: decrease step magnitude after direction change, answer fine tunning (zoom in to precise value)
            if error > error_previous:
                direction *= -1
                magnitude *= magnitude_decrease
                consecutive_steps = 0
            # error decrease: maintain direction; increase speed if direction maintained consecutively 
            # exploration: increase step magnitude after 100 consecutive steps, run-time optimization (find larger numbers faster)
            else:
                consecutive_steps += 1
                if consecutive_steps >= optimization:
                    magnitude *= magnitude_increase
                    consecutive_steps = 0
            # apply movement
            x += direction * magnitude
            error_previous = error
            # safety: magnitude approaches float precision error
            if magnitude < 1e-18:
                break
        return x, kwargs
    # o

    # p
    def pad(string: str, length: int, pad: str = ' ', type = 'l') -> str:
        return util.string_pad(string, length, type, pad)
    def pad_block(string: str, width: int, align: str = "left", fillChar: str = ' '):
        return util.string_pad_block(string, width, align, fillChar)
    def path_info(path: str, option: str = None) -> dict[str, str]|str:
        delimiter = '/' if '/' in path else '\\'
        # example: C:\\path\\filename.ext
        value = {
            # example: c:\\folder
            "dirname": path[0:path.rindex(delimiter)] if delimiter in path else None,
            # example: filename.ext
            "basename": path[path.rindex(delimiter)+1:] if delimiter in path else None,
            # example: ext
            "extension": path[path.rindex('.')+1:] if '.' in path else None,
            # example: filename
            "filename": (path[path.rindex(delimiter)+1:path.rindex('.')] if '.' in path else path[path.rindex(delimiter)+1:]) if delimiter in path else None,
        }
        # if delimiter in path:
        #     value["filename"] = path[path.rindex(delimiter) + 1:]

        return value if option == None else value[option]
    def polar_to_cartesian(r: float, theta: float) -> list[float]:
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        return [x, y]
    # q
    # r
    def random(*values):
        return util.mathematics_random(*values)
    def reference_encode(data: dict) -> str:
        pass
    def reference_decode(data: str) -> dict:
        results = {
            "ABBREVIATIONS": {},
            # key: {string: string}
            "ACRONYMS": {},
            # key: {string: string}
            "DEFINITIONS": {},
            # key: {string: string}
            "LIST": {},
            # key: [string]
            "NAME": '',
            # string
            "OBJECT": {},
            # key: {string: string}
            "QUESTIONS": {},
            # [{question: string, answers: [string], comment: string}]
            "SOURCE": [],
            # [string]
            "SUBTITLE": '',
            # string
            "TABLE": {},
            # key: [{string: string}]
            "TITLE": '',
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
            tagKey = "ABBREVIATIONS"
            if line.startswith(tagKey):
                tag = results[tagKey]
                assert isinstance(tag, dict)
                tagValue = getTagValue(tagKey, line)
                tagContentLines = getTagContent(lines, index)
                tagContent = dict([(s.lower().strip(' ') for s in line.split(':')) for line in tagContentLines])
                tag[tagValue] = tagContent
                index += len(tagContent) + 1
            tagKey = "ACRONYMS"
            if line.startswith(tagKey):
                tag = results[tagKey]
                assert isinstance(tag, dict)
                tagValue = getTagValue(tagKey, line)
                tagContentLines = getTagContent(lines, index)
                tagContent = dict([(s.strip(' ') for s in line.split(':')) for line in tagContentLines])
                tagContent = dict((sk.upper(), sv) for sk, sv in tagContent.items())
                tag[tagValue] = tagContent
                index += len(tagContent) + 1
            tagKey = "DEFINITIONS"
            if line.startswith(tagKey):
                tag = results[tagKey]
                assert isinstance(tag, dict)
                tagValue = getTagValue(tagKey, line)
                tagContentLines = getTagContent(lines, index)
                tagContent = dict([(s.strip(' ') for s in line.split(':')) for line in tagContentLines])
                tag[tagValue] = tagContent
                index += len(tagContent) + 1
            tagKey = "LIST"
            if line.startswith(tagKey):
                tag = results[tagKey]
                assert isinstance(tag, dict)
                tagValue = getTagValue(tagKey, line)
                tagContentLines = getTagContent(lines, index)
                tagContent = tagContentLines
                tag[tagValue] = tagContent
                index += len(tagContent) + 1
            tagKey = "NAME"
            if line.startswith(tagKey):
                tag = results[tagKey]
                assert isinstance(tag, str)
                tag = getTagValue(tagKey, line)
            tagKey = "OBJECT"
            if line.startswith(tagKey):
                tag = results[tagKey]
                assert isinstance(tag, dict)
                tagValue = getTagValue(tagKey, line)
                tagContentLines = getTagContent(lines, index)
                tagContent = dict([(s.strip(' ') for s in line.split(':')) for line in tagContentLines])
                tag[tagValue] = tagContent
                index += len(tagContent) + 1
            tagKey = "QUESTIONS"
            if line.startswith(tagKey):
                tag = results[tagKey]
                assert isinstance(tag, dict)
                tagValue = getTagValue(tagKey, line)
                tagContentLines = getTagContent(lines, index, "BREAK")
                tagContent = []
                i = 0
                # ignore initial empty lines
                while tagContentLines[0] == '':
                    tagContentLines.pop(0)
                while i < len(tagContentLines):
                    if tagContentLines[i] == '':
                        tagContent.append({ "question": '', "answers": [], "comment": '' })
                        j = i - 1
                        while j >= 0 and len(tagContentLines[j]) > 0:
                            if j == 0 or tagContentLines[j-1] == '':
                                tagContent[-1]["question"] = tagContentLines[j]
                            elif tagContentLines[j].startswith('###'):
                                tagContent[-1]["comment"] = tagContentLines[j]
                            else:
                                tagContent[-1]["answers"] = [tagContentLines[j]] + tagContent[-1]["answers"]
                            j -= 1
                    i += 1
                tag[tagValue] = tagContent
                index += len(tagContent) + 1
            tagKey = "SOURCE"
            if line.startswith(tagKey):
                tag = results[tagKey]
                assert isinstance(tag, list)
                tagValue = getTagValue(tagKey, line)
                tag.append(tagValue)
            tagKey = "SUBTITLE"
            if line.startswith(tagKey):
                tag = results[tagKey]
                assert isinstance(tag, str)
                tag = getTagValue(tagKey, line)
            tagKey = "TABLE"
            if line.startswith(tagKey):
                tag = results[tagKey]
                assert isinstance(tag, dict)
                tagValue = getTagValue(tagKey, line)
                tagContentLines = getTagContent(lines, index)
                tagContent = util.table_decode(tagContentLines)
                tag[tagValue] = tagContent
                index += len(tagContent) + 1
            tagKey = "TITLE"
            if line.startswith(tagKey):
                tag = results[tagKey]
                assert isinstance(tag, str)
                tag = getTagValue(tagKey, line)
        return results
    def regular_expression_match(pattern: str, value: str) -> bool:
        return util.ispattern(value, pattern)
    def round(number: float, placement: int) -> float|int:
        # round non integer numbers by nth placement
        return round(number * (10 ** placement)) / (10 ** placement)
    def rgb_to_hex(r, g, b):
        return '#{:02x}{:02x}{:02x}'.format(int(r), int(g), int(b))
    # s
    def statistics_correlation_coefficient(numbers1: list[float], numbers2: list[float]):
        if len(numbers1) != len(numbers2): raise Exception("RangeError: numbers length mismatch")
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
        return product
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
        elif util.istype(value, "array"):
            return util.json_encode(value)
        elif util.istype(value, "boolean"):
            return f"{value}"
        elif util.istype(value, "number"):
            return f"{value}"
        elif util.istype(value, "object"):
            return util.json_encode(value)
        else:
            return value
    def string_conversion_decode(value: str) -> bool|dict|int|float|list:
        if value == None:
            return value
        elif util.istype(value, "string-array"):
            return util.json_decode(value)
        elif util.istype(value, "string-boolean"):
            return value.lower() == "true"
        elif util.istype(value, "string-number-decimal"):
            return float(value)
        elif util.istype(value, "string-number-integer"):
            return int(value)
        elif util.istype(value, "string-object"):
            return util.json_decode(value)
        else:
            return value
    def string_interpolation_encode(string: str, variables: dict) -> str:
        # find & replace variable value w/ variable placeholder
        # prioritize longer variable value
        matches = [[key, value, len(value)] for key, value in variables.items() if value in string]
        matches.sort(key=lambda entry : entry[2])
        matches.reverse()
        for entry in matches:
            if not entry[1] in string: continue
            string = string.replace(entry[1], f"%{entry[0]}%")
        return string
    def string_interpolation_decode(string: str, variables: dict) -> str:
        # find & replace variable placeholder w/ variable value
        def isKey(key: str) -> bool:
            # determine whether key exist in variables set (case insensitive)
            return key.lower() in [key.lower() for key in variables.keys()]
        for match in re.findall(util.STRING_INTERPOLATION_SYNTAX1, string):
            key: str = match[1:-1]
            if not isKey(key):
                print(f"KeyError: '{key}' not found in provided variables")
                continue
            string = string.replace(match, str(variables[key.lower()]))
        for match in re.findall(util.STRING_INTERPOLATION_SYNTAX2, string):
            key: str = match[1:-1]
            if not isKey(key):
                print(f"KeyError: '{key}' not found in provided variables")
                continue
            string = string.replace(match, str(variables[key.lower()]))
        for match in re.findall(util.STRING_INTERPOLATION_SYNTAX3, string):
            key: str = match[1:-1]
            if not isKey(key):
                print(f"KeyError: '{key}' not found in provided variables")
                continue
            string = string.replace(match, str(variables[key.lower()]))
        return string
    def string_pad(string: str, width: int, align: str = "left", fillChar: str = ' ') -> str:
        if len(string) >= width: return string
        align = align.lower()
        if align == "right":
            return string.rjust(width, fillChar)
        elif align == "center":
            return string.center(width, fillChar)
        else:
            return string.ljust(width, fillChar)
    def string_pad_block(string: str, width: int, align: str = "left", fillChar: str = ' ') -> str:
        padding_length = (width - len(string) % width) % width
        if padding_length == 0: return string
        align = align.lower()
        if align == "right":
            return fillChar * padding_length + string
        elif align == "center":
            return fillChar * math.floor(padding_length / 2) + string + fillChar * math.ceil(padding_length / 2)
        else:
            return string + fillChar * padding_length
    def spherical_to_cartesian(r: float, theta: float, phi: float) -> list[float]:
        x = r * math.sin(phi) * math.cos(theta)
        y = r * math.sin(phi) * math.sin(theta)
        z = r * math.cos(phi)
        return [x, y, z]
    def spherical_to_geographic(r: float, theta: float, phi: float) -> list[float]:
        latitude = 90 - (math.degrees(phi))
        longitude = math.degrees(theta)
        longitude = longitude - 360 if longitude > 180 else longitude
        altitude = r - util.SPHERE_RADIUS
        return [latitude, longitude, altitude]
    def system_abspath(path: str):
        return os.path.dirname(os.path.abspath(path))
    def system_command(value: str):
        os.system(value)
    def system_log(path: str, line: int, *values):
        #example: util.system_log(__file__, inspect.currentframe().f_lineno, "message")
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
    def table_encode(entries: list[dict[str, int|str]], orientation = "vertical", delimiter: str = '     ') -> str:
        if entries == []: return ""
        headers = [*entries[0].keys()]
        rows = [[*entry.values()] for entry in entries]
        results = ""
        if orientation == util.TABLE_ORIENTATION_VERTICAL or orientation == 'v':
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
        if orientation == util.TABLE_ORIENTATION_HORIZONTAL or orientation == 'h':
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
    def table_decode(data: list|str, orientation = "vertical", delimiter: str = '     ') -> list[dict[str, int|str]]:
        # NOTE: each header name must be unique
        rows = [  ]
        if util.istype(data, "array-string"):
            lines = data
        if util.istype(data, "string"):
            lines = data.splitlines()
        lines = [line for line in lines if line.strip()]
        headers = [substr.strip() for substr in lines[0].split(delimiter) if substr.strip()]
        if len(headers) == 0:
            raise Exception(f"ValueError: table headers not found")
        for line in lines[1:]:
            if len(delimiter) == 1:
                # requires cell contain characters other than space
                row = [substr.strip() for substr in line.split(delimiter) if substr.strip()]
            else:
                row = [''] * len(headers)
                for j in range(len(headers)):
                    sIndex = lines[0].index(headers[j])
                    eIndex = lines[0].index(headers[j+1]) if j < len(headers)-1 else len(line)
                    row[j] = line[sIndex:eIndex].strip()
            if len(row) != len(headers):
                raise Exception(f"RangeError: table row to header column count mismatch")
            rows.append(dict(zip(headers, row)))
        return rows
    def timestamp(value: datetime.datetime|int|str = None, convert_to: str = None) -> datetime.datetime|dict|int|str:
        def convert(date: datetime.datetime, option: str) -> datetime.datetime|int|str:
            if option == None:
                return date
            if option.lower() == util.TIMESTAMP_OPTION_DICTIONARY:
                return {
                    "year"       : date.year,
                    "month"      : date.month,
                    "day"        : date.day,
                    "hour"       : date.hour,
                    "minute"     : date.minute,
                    "second"     : date.second,
                    "millisecond": int(date.microsecond / 1000) % 1000,
                    "zone"       : 'Z',
                }
            if option.lower() == util.TIMESTAMP_OPTION_MILLISECONDS:
                return round((date.timestamp()) * 1000)
            if option.lower() == util.TIMESTAMP_OPTION_OBJECT:
                return date
            if option.lower() == util.TIMESTAMP_OPTION_SECONDS:
                return round(date.timestamp())
            if option.lower() == util.TIMESTAMP_OPTION_STRING:
                return date.strftime('%Y%m%dT%H%M%S') + 'Z'
            if option.lower() == util.TIMESTAMP_OPTION_TEXT:
                return date.strftime('%Y%m%dT%H%M%S') + 'Z'
            # if len(option) == 1 and util.regular_expression_match(r"^([A-I]|[K-Z])$"):
            #     zone_utc_offset = util.TIMEZONE_DESIGNATION_OFFSETS[option]
            #     timezoneTO = datetime.timezone(datetime.timedelta(hours=zone_utc_offset))
            #     return date.astimezone(timezoneTO)
        def isOption(value: str):
            option = value.lower()
            return option == util.TIMESTAMP_OPTION_DICTIONARY or option == util.TIMESTAMP_OPTION_MILLISECONDS or option == util.TIMESTAMP_OPTION_OBJECT or option == util.TIMESTAMP_OPTION_SECONDS or option == util.TIMESTAMP_OPTION_STRING or option == util.TIMESTAMP_OPTION_TEXT
        def getString(value) -> dict:
            if '-' in value:
                # print(f"DepreciationError: legacy timestamp format \"YYYY-MM-DDTHH:MM:SS\" depreciated")
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
        timezone = datetime.timezone(datetime.timedelta(hours=0))
        if value == None:
            return convert(date, convert_to if convert_to else util.TIMESTAMP_OPTION_SECONDS)
        elif isinstance(value, datetime.datetime):
            return convert(value, convert_to)
        elif isinstance(value, int):
            date = None
            if len(str(value)) <= 10:
                date = datetime.datetime.fromtimestamp(value, tz=timezone)
            elif len(str(value)) == 13:
                date = datetime.datetime.fromtimestamp(value/1000, tz=timezone)
            else:
                raise Exception(f"ValueError: timestamp specifications inadequate")
            return convert(date, convert_to)
        elif isinstance(value, str):
            if isOption(value):
                return convert(date, value)
            elif util.istype(value, "string-number-integer") and len(value) == 10:
                date = datetime.datetime.fromtimestamp(int(value), tz=timezone)
                return convert(date, convert_to)
            elif util.istype(value, "string-number-integer") and len(value) == 13:
                date = datetime.datetime.fromtimestamp(int(value)/1000, tz=timezone)
                return convert(date, convert_to)
            elif len(value) > 0 and bool(getString(value)):
                groups = getString(value)
                year        = int(groups["year"])               if "year"        in groups else 1970
                month       = int(groups["month"])              if "month"       in groups else 1
                day         = int(groups["day"])                if "day"         in groups else 1
                hour        = int(groups["hour"])               if "hour"        in groups else 0
                minute      = int(groups["minute"])             if "minute"      in groups else 0
                second      = int(groups["second"])             if "second"      in groups else 0
                microsecond = int(groups["millisecond"]) * 1000 if "millisecond" in groups else 0
                zone        = groups["zone"]                    if groups["zone"]          else 'Z'
                zone_utc_offset = util.TIMEZONE_DESIGNATION_OFFSETS[zone]
                timezone = datetime.timezone(datetime.timedelta(hours=zone_utc_offset))
                date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second, microsecond=microsecond, tzinfo=timezone)
                date = date.astimezone(datetime.timezone.utc)
                return convert(date, convert_to)
            else:
                raise Exception(f"ValueError: timestamp specifications inadequate")
    def timestamp_calculator_addition(timestamp_start: datetime.datetime|int|str = None, years: int = 0, days: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0) -> datetime.datetime:
        timestamp_start = util.timestamp(timestamp_start, util.TIMESTAMP_OPTION_SECONDS)
        duration = 0
        duration = duration+(years*365*24*60*60)
        duration = duration+(days*24*60*60)
        duration = duration+(hours*60*60)
        duration = duration+(minutes*60)
        duration = duration+(seconds)
        timestamp_end = timestamp_start + duration
        timestamp_end = util.timestamp(timestamp_end, util.TIMESTAMP_OPTION_OBJECT)
        return timestamp_end
    def timestamp_calculator_difference(timestamp_start: datetime.datetime|int|str, timestamp_end: datetime.datetime|int|str = None) -> dict:
        timestamp_start = util.timestamp(timestamp_start, util.TIMESTAMP_OPTION_SECONDS)
        timestamp_end = util.timestamp(timestamp_end, util.TIMESTAMP_OPTION_SECONDS)
        difference = abs(timestamp_end - timestamp_start)
        years   = difference//(365*24*60*60)
        days    = (difference//(24*60*60))-((years*365))
        hours   = (difference//(60*60))-((years*365*24)+(days*24))
        minutes = (difference//(60))-((years*365*24*60)+(days*24*60)+(hours*60))
        seconds = (difference)-((years*365*24*60*60)+(days*24*60*60)+(hours*60*60)+(minutes*60))
        return {
            "years": years,
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
        }
    def timestamp_date(timestamp: datetime.datetime|int|str = None) -> str:
        timestamp = util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT)
        year = f"{timestamp.year}"
        month = f"{timestamp.month}".rjust(2, '0')
        day = f"{timestamp.day}".rjust(2, '0')
        return f"{year}-{month}-{day}"
    def timestamp_day(timestamp: datetime.datetime|int|str = None) -> str:
        timestamp = util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT)
        return f"{timestamp.day}".rjust(2, '0')
    def timestamp_day_of_year(timestamp: datetime.datetime|int|str = None) -> int:
        timestamp: datetime.datetime = util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT)
        return timestamp.timetuple().tm_yday
    def timestamp_difference(timestamp_start: datetime.datetime|int|str, timestamp_end: datetime.datetime|int|str = None, short: bool = True) -> str:
        timestamp_start = util.timestamp(timestamp_start, util.TIMESTAMP_OPTION_SECONDS)
        timestamp_end = util.timestamp(timestamp_end, util.TIMESTAMP_OPTION_SECONDS)
        difference = abs(timestamp_end - timestamp_start)
        if difference == 0: return "Now"
        if difference <= 1: return "1sec" if short else "1 second"
        if difference <= 2: return "2sec" if short else "2 seconds"
        if difference <= 3: return "3sec" if short else "3 seconds"
        if difference <= 4: return "4sec" if short else "4 seconds"
        if difference <= 5: return "5sec" if short else "5 seconds"
        if difference <= 10: return "10sec" if short else "10 seconds"
        if difference <= 20: return "20sec" if short else "20 seconds"
        if difference <= 30: return "30sec" if short else "30 seconds"
        if difference <= 60: return "1min" if short else "1 minute"
        if difference <= 120: return "2min" if short else "2 minutes"
        if difference <= 180: return "3min" if short else "3 minutes"
        if difference <= 240: return "4min" if short else "4 minutes"
        if difference <= 300: return "5min" if short else "5 minutes"
        if difference <= 600: return "10min" if short else "10 minutes"
        if difference <= 1200: return "20min" if short else "20 minutes"
        if difference <= 1800: return "30min" if short else "30 minutes"
        if difference <= 3600: return "1h" if short else "1 hour"
        if difference <= 7200: return "2h" if short else "2 hours"
        if difference <= 10800: return "3h" if short else "3 hours"
        if difference <= 14400: return "4h" if short else "4 hours"
        if difference <= 18000: return "5h" if short else "5 hours"
        if difference <= 21600: return "6h" if short else "6 hours"
        if difference <= 43200: return "12h" if short else "12 hours"
        if difference <= 86400: return "1d" if short else "1 day"
        if difference <= 172800: return "2d" if short else "2 days"
        if difference <= 259200: return "3d" if short else "3 days"
        if difference <= 345600: return "4d" if short else "4 days"
        if difference <= 432000: return "5d" if short else "5 days"
        if difference <= 864000: return "10d" if short else "10 days"
        if difference <= 1728000: return "20d" if short else "20 days"
        if difference <= 2592000: return "1mo" if short else "1 month" # 30 days
        if difference <= 5184000: return "2mo" if short else "2 months"
        if difference <= 7776000: return "3mo" if short else "3 months"
        if difference <= 10368000: return "4mo" if short else "4 months"
        if difference <= 12960000: return "5mo" if short else "5 months"
        if difference <= 15552000: return "6mo" if short else "6 months"
        if difference <= 31536000: return "1yr" if short else "1 year"
        if difference <= 63072000: return "2yr" if short else "2 years"
        if difference <= 94608000: return "3yr" if short else "3 years"
        if difference <= 126144000: return "4yr" if short else "4 years"
        if difference <= 157680000: return "5yr" if short else "5 years"
        if difference <= 315360000: return "10yr" if short else "10 years"
    def timestamp_hour(timestamp: datetime.datetime|int|str = None) -> str:
        timestamp = util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT)
        return f"{timestamp.hour}".rjust(2, '0')
    def __timestamp_julian_date(timestamp: datetime.datetime|int|str = None) -> int:
        """
        Converts a Gregorian date to a Julian date.
        The Julian Date is the continuous count of days since the beginning of the
        Julian Period, starting from noon Universal Time on January 1, 4713 BC.
        """
        timestamp: datetime.datetime = util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT)
        year = timestamp.year
        month = timestamp.month
        day = timestamp.day
        # algorithm for Julian Day Number calculation
        if month <= 2:
            year -= 1
            month += 12
        a = year // 100
        b = a // 4
        c = 2 - a + b
        e = int(365.25 * (year + 4716))
        f = int(30.6001 * (month + 1))
        julian_day_number = c + day + e + f - 1524
        return julian_day_number
    def timestamp_julian_date(timestamp: datetime.datetime|int|str = None) -> int:
        timestamp: datetime.datetime = util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT)
        # reference point for Julian Day Number: January 1, 4713 BC, 12:00 UTC (JD 0.0)
        # python datetime does not support dates before 1 CE, so we use a known reference point
        # use 1858-11-17T00:00Z as a reference, which corresponds to JD 2400000.5
        reference_date = datetime.datetime(1858, 11, 17, 0, 0, 0, tzinfo=timestamp.astimezone().tzinfo)
        julian_date_reference = 2400000.5
        # the offset from this reference to the input date will be added to the reference JD.
        # calculate the difference in days from the reference date
        difference = timestamp - reference_date
        days_since_reference = difference.total_seconds() / (24 * 3600)
        return julian_date_reference + days_since_reference
    def timestamp_julian_day(timestamp: datetime.datetime|int|str = None) -> int:
        return math.floor(util.timestamp_julian_date(timestamp))
    def timestamp_julian_day_of_year(timestamp: datetime.datetime|int|str = None) -> int:
        timestamp: datetime.datetime = util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT)
        first_day_of_year = datetime.datetime(timestamp.year, 1, 1, tzinfo=timestamp.astimezone().tzinfo)
        # calculate the difference in days and add 1 (since it's a 1-indexed day count)
        return (timestamp - first_day_of_year).days + 1
    def timestamp_millisecond(timestamp: datetime.datetime|int|str = None) -> str:
        timestamp = util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT)
        millisecond = int(timestamp.microsecond / 1000)
        if millisecond == '1000': millisecond = '0'
        return f"{millisecond}".rjust(3, '0')
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
        return f"{timestamp.second}".rjust(2, '0')
    def timestamp_summary(timestamp: datetime.datetime|int|str = None):
        timestamp = util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT)
        import calendar
        results = { }
        results["date"] = util.timestamp(timestamp, util.TIMESTAMP_OPTION_DICTIONARY)
        results["Year"] = util.timestamp_year(timestamp)
        results["Month"] = util.timestamp_month(timestamp)
        results["Day"] = util.timestamp_day(timestamp)
        results["Hour"] = util.timestamp_hour(timestamp)
        results["Minute"] = util.timestamp_minute(timestamp)
        results["Second"] = util.timestamp_second(timestamp)
        results["Millisecond"] = util.timestamp_millisecond(timestamp)
        results["Zone"] = results["date"]["zone"]
        results["Date"] = util.timestamp_date(timestamp)
        results["Time"] = util.timestamp_time(timestamp, True)
        results["Weekday"] = util.timestamp_weekday(timestamp)
        results["Quarter"] = util.timestamp_quarter(timestamp)
        results["Leap Year"] = calendar.isleap(results["date"]["year"])
        results["Timestamp Seconds"] = util.timestamp(timestamp, util.TIMESTAMP_OPTION_SECONDS)
        results["Timestamp Milliseconds"] = util.timestamp(timestamp, util.TIMESTAMP_OPTION_MILLISECONDS)
        results["Timestamp Text"] = util.timestamp(timestamp, util.TIMESTAMP_OPTION_TEXT)
        results["Julian Date"] = util.timestamp_julian_date(timestamp)
        results["Julian Day"] = util.timestamp_julian_day(timestamp)
        results["Julian Day of Year"] = util.timestamp_julian_day_of_year(timestamp)
        return results
    def timestamp_time(timestamp: datetime.datetime|int|str = None, short: bool = False) -> str:
        timestamp = util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT)
        hour = f"{timestamp.hour}".rjust(2, '0')
        minute = f"{timestamp.minute}".rjust(2, '0')
        second = f"{timestamp.second}".rjust(2, '0')
        millisecond = f"{timestamp.microsecond / 1000:.0f}".rjust(3, '0')
        # TODO: if millisecond == 1000, increase second by one
        if millisecond == "1000": millisecond = "999"
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
            "arcnet", "arp", "atm",
            "ciaddr", "chaddr",
            "dhcp", "drarp",
            "giaddr",
            "hdlc",
            "icmp", "ieee", "ip", "id",
            "mac",
            "ok",
            "rarp", "rfc",
            "siaddr", "sha", "spa",
            "tha", "tpa",
            "udp",
            "yiaddr"
        ]
        specials = [
            "ICMPv6", "InARP", "IPv4", "IPv6"
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
    def type_to_value(data_type: str|type):
        if data_type == array   or data_type == "array"         : return array()
        if data_type == bool    or data_type == "boolean"       : return False
        if data_type == complex or data_type == "complex"       : return complex()
        if data_type == dict    or data_type == "dictionary"    : return {}
        if data_type == int     or data_type == "number"        : return 0
        if data_type == int     or data_type == "number-integer": return 0
        if data_type == float   or data_type == "number-decimal": return 0.0
        if data_type == list    or data_type == "list"          : return []
        if data_type == object  or data_type == "object"        : return object()
        if data_type == str     or data_type == "string"        : return ''
    # u
    def uri_encode(object: dict) -> str:
        uriString = ''
        return uriString
    def uri_decode(relative: str, absolute: str = None):
        # example: http://username:password@hostname:9090/path?arg=value#anchor
        # relative path: relative-part [ ? query ] [ # fragment ] (cannot begin with '/')
        # absolute path: scheme ":" hierarchal-part [ "?" query ]
        uriObject = {
            "scheme": None,
            "username": None,
            "password": None,
            "authority": None,
            "host": None,
            "port": None,
            "path": None,
            "query": None,
            "fragment": None,
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
            uriObject["scheme"] = target[:target.index('://')]
            target_partial = target[target.index('://')+3:]
        if '@' in target:
            string = target_partial[:target_partial.index('@')]
            uriObject["username"], uriObject["password"] = string.split(':')
            target_partial = target_partial[target_partial.index('@')+1:]
        index = getFirstIndex(target_partial, ['/', '?', '#'])
        if index == None:
            uriObject["authority"] = target_partial
            target_partial = ''
        else:
            uriObject["authority"] = target_partial[:index]
            target_partial = target_partial[index:]
        if ':' in uriObject["authority"]:
            uriObject["host"] = uriObject["authority"][:uriObject["authority"].index(':')]
            uriObject["port"] = uriObject["authority"][uriObject["authority"].index(':')+1:]
        else:
            uriObject["host"] = uriObject["authority"]
        if len(target_partial) > 0 and '/' == target_partial[0]:
            index = getFirstIndex(target_partial, ['?', '#'])
            if index == None:
                uriObject["path"] = target_partial
                target_partial = ''
            else:
                uriObject["path"] = target_partial[:index]
                target_partial = target_partial[index:]
        else:
            uriObject["path"] = '/'
        if len(target_partial) > 0 and '?' == target_partial[0]:
            target_partial = target_partial[1:]
            index = getFirstIndex(target_partial, ['#'])
            if index == None:
                uriObject["query"] = target_partial
                target_partial = ''
            else:
                uriObject["query"] = target_partial[:index]
                target_partial = target_partial[index:]
        else:
            pass
        if len(target_partial) > 0 and '#' == target_partial[0]:
            uriObject["fragment"] = target_partial[1:]
        else:
            pass
        return uriObject
    def uri_query_encode(data: dict) -> str:
        if len(data) == 0: return ''
        return '&'.join([(f"{key}={val}") for key, val in data.items()])
    def uri_query_decode(data: str) -> str:
        if not '=' in data: return {}
        data = data[data.index('?')+1:] if '?' in data else data
        return dict(s.split('=', 1) for s in data.split('&'))
    # v
    def vector_addition(vector1: list[float], vector2: list[float]) -> list[float]:
        if not len(vector1) == len(vector2):
            raise Exception(f"RangeError: vector length mismatch")
        return [c1 + c2 for c1, c2 in zip(vector1, vector2)]
    def vector_magnitude(vector: list[float]) -> float:
        return math.sqrt(sum(component**2 for component in vector))
    def vector_multiplication(vector1: list[float], vector2: list[float]) -> list[float]:
        if not len(vector1) == len(vector2):
            raise Exception(f"RangeError: vector length mismatch")
        return [c1 * c2 for c1, c2 in zip(vector1, vector2)]
    def vector_multiplication_scalar(vector: list[float], scalar: float) -> list[float]:
        return [c * scalar for c in vector]
    def vector_subtraction(vector1: list[float], vector2: list[float]) -> list[float]:
        if not len(vector1) == len(vector2):
            raise Exception(f"RangeError: vector length mismatch")
        return [c1 - c2 for c1, c2 in zip(vector1, vector2)]
    def vector_to_component_form(magnitude: float, direction: float) -> list[float]:
        x = util.vector_to_x(magnitude, direction)
        y = util.vector_to_y(magnitude, direction)
        return [x, y]
    def vector_to_direction(x: float, y: float) -> list[float]:
        return math.degrees(math.atan2(y, x))
    def vector_to_magnitude(x: float, y: float) -> list[float]:
        return abs(math.sqrt(x**2 + y**2))
    def vector_to_magnitude_direction_form(x: float, y: float) -> list[float]:
        return [util.vector_to_magnitude(x, y), util.vector_to_direction(x, y)]
    def vector_to_x(magnitude: float, direction: float) -> list[float]:
        return magnitude * math.cos(math.radians(direction))
    def vector_to_y(magnitude: float, direction: float) -> list[float]:
        return magnitude * math.sin(math.radians(direction))
    def volume(x: float, y: float, z: float) -> float:
        return x * y * z
    # w

    # x

    # y

    # z

    # ascii functions
    # default bits per character (size) = 8
    def _dataT_(data, datatype: str):
        types = "bin byt cha dec hex oct str".split(' ')
        for type in types:
            if type == datatype: continue
            method = F"{datatype}2{type}"
            print(method, getattr(globals()["util"], method)(data))
    # binary
    def bin2byt(bin: str) -> bytes:
        if len(bin) == 0: return bytes()
        length = math.ceil(len(bin)/8)
        return util.bin2dec(bin).to_bytes(length, "big")
    def bin2cha(bin: str) -> str:
        return util.dec2cha(util.bin2dec(bin))
    def bin2dec(bin: str) -> int:
        if len(bin) == 0: return 0
        return int(bin, 2)
    def bin2hex(bin: str) -> str:
        bin = util.pad_block(bin, 4, "right", '0')
        hex = ''
        for i in range(0, len(bin), 4):
            hex += util.dec2hex(util.bin2dec(bin[i:i+4]))
        return hex
    def bin2oct(bin: str) -> str:
        return util.dec2oct(util.bin2dec(bin))
    def bin2str(bin: str, size: int = 8) -> str: # 8 bpc
        bin = util.pad_block(bin, size, "right", '0')
        str = ''
        for i in range(0, len(bin), size):
            str += util.dec2cha(util.bin2dec(bin[i:i+size]))
        return str
    def bin2bol(bin: str) -> bool:
        return bin == '1'
    def bin2decs(bin: str, size: int = 8) -> list:
        bin = util.pad_block(bin, size, "right", '0')
        decs = []
        for i in range(0, len(bin), size):
            decs.append(util.bin2dec(bin[i:i+size]))
        return decs
    def bin2hexs(bin: str) -> str:
        return "0x" + util.bin2hex(bin).upper()
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
        bin = util.pad_block(bin, size, "right", '0')
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
    def decs2bin(decs: list[int], len: int = None) -> str: # 8 size
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
        # return str.encode("utf-8").hex()
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

class array(list):
    def __init__(self, *values):
        super().__init__()
        flat_values = []
        for value in values:
            if isinstance(value, list|tuple):
                flat_values.extend(value)
            elif hasattr(value, "__iter__") and not isinstance(value, bytes|dict|str):
                flat_values.extend(list(value))
            else:
                flat_values.append(value)
        self.extend(flat_values)
    def __getitem__(self, index):
        result = super().__getitem__(index)
        if isinstance(index, slice):
            return self.__class__(*result)
        return result
    def __iadd__(self, other):
        if isinstance(other, list|tuple):
            self.extend(other)
        else:
            self.append(other)
        return self
    def __repr__(self) -> str:
        return super().__repr__()
    def __str__(self):
        return json.dumps(self)

    @staticmethod
    def fromdata(data):
        nArray = array()
        if data == None:
            return nArray
        if util.istype(data, "array"):
            nArray.append(*data)
        elif util.istype(data, "bytes-array"):
            nArray.append(*util.json_decode(util.byt2str(data)))
        elif util.istype(data, "bytes-object"):
            nArray = array.fromobject(util.json_decode(util.byt2str(data)))
        elif util.istype(data, "object"):
            nArray = array.fromobject(data)
        elif util.istype(data, "string-array"):
            nArray.append(*util.json_decode(data))
        elif util.istype(data, "string-object"):
            nArray = array.fromobject(util.json_decode(data))
        elif util.istype(data, "string"):
            nArray = array.fromstring(data)
        else:
            raise Exception(f"TypeError: type {type(data)} unsupported")
        return nArray
    @staticmethod
    def fromobject(data: dict|object, delimiter=': '):
        return array((f"{key}{delimiter}{value}") for key, value in data.items())
    @staticmethod
    def fromstring(data: str, delimiter: str = ',', remove_whitespace: bool = False):
        nArray = array()
        if data == None:
            return nArray
        for substring in data.split(delimiter):
            item = substring.strip(' ') if remove_whitespace else substring
            nArray.append(item)
        return nArray
    @staticmethod
    def __fromstring(data: str):
        nArray = array()
        if data == None:
            return nArray
        trimmed_data = data.strip(' ,:')
        hasComma = ',' in trimmed_data
        hasColon = ':' in trimmed_data
        # data = 'value,value:value,value:value:value,value...'
        if hasComma and hasColon:
            for substring in trimmed_data.split(','):
                nArray.append(array(substring.strip(' :').split(':')))
        # data = 'value,value,value...'
        if hasComma and not hasColon:
            nArray.extend(trimmed_data.split(','))
        # data = 'value:value:value...'
        if not hasComma and hasColon:
            nArray.extend(trimmed_data.split(':'))
        # data = 'value'
        if not hasComma and not hasColon:
            nArray.append(trimmed_data)
        return nArray

    @staticmethod
    def generate(*args):
        size = len(args)
        start = stop = step = 0
        if size == 1:
            stop, start, step = args[0], 0, 1
        elif size == 2:
            start, stop, step = args[0], args[1], 1
        elif size == 3:
            start, stop, step = args
        else:
            raise Exception(f"TypeError: require 1 to 3 arguments")
        yield from range(start, stop, step)

    def __callback(self, callback: Callable[..., bool|Any], value: T, index: int, self_ref: 'array') -> bool|Any:
        try:
            return callback(value, index, self_ref)
        except TypeError:
            try:
                return callback(value, index)
            except TypeError:
                try:
                    return callback(value)
                except TypeError:
                    raise Exception(f"TypeError: array callback requires 1 to 3 arguments")

    def any(self):
        return any(self)
    def append(self, *values):
        self.extend(values)
    def clear(self):
        del self[:]
    def clone(self):
        import copy
        return copy.deepcopy(self)
    def copy(self, start: int = 0, end: int = None):
        if end is None:
            end = len(self)
        return array(*self[start:end])
    def count(self, value):
        return super().count(value)
    def dump(self):
        return util.dump(self)
    def empty(self):
        return not self
    def enumerate(self):
        return enumerate(self)
    def every(self, callback: Callable[..., bool]) -> bool:
        return all(self.__callback(callback, v, i, self) for i, v in enumerate(self))
    def excludes(self, *values) -> bool:
        return all(val not in self for val in values)
    def find(self, callback: Callable[..., bool]) -> T|None:
        for i, v in enumerate(self):
            if self.__callback(callback, v, i, self):
                return v
        return None
    def findindex(self, callback: Callable[..., bool]):
        for i, v in enumerate(self):
            if self.__callback(callback, v, i, self):
                return i
        return None
    def findvalue(self, callback: Callable[..., bool]):
        return self.find(callback)
    def filter(self, callback: Callable[..., bool]):
        return self.__class__(*(v for i, v in enumerate(self) if self.__callback(callback, v, i, self)))
    def fill(self, value: Any):
        for i in range(len(self)):
            self[i] = value
        return self
    def get(self, index: int, default_value: Any = None) -> Any:
        try:
            return self[index]
        except IndexError:
            return default_value
    def getfirst(self):
        return self.get(0)
    def getlast(self):
        return self.get(-1)
    def hash(self, mode: str = util.HASH_MD5) -> str:
        data = util.json_encode(self)
        func = getattr(util, f"hash_{mode.lower()}", None)
        return func(data)
    def includes(self, *values) -> bool:
        return all(val in self for val in values)
    def index(self, value, start: int = 0) -> int:
        try:
            return super().index(value, start)
        except ValueError:
            return -1
    def insert(self, index, value):
        super().insert(index, value)
    def join(self, delimiter: str = '') -> str:
        return delimiter.join(map(str, self))
    def json(self) -> str:
        return util.json_encode(self)
    def map(self, callback: Callable[..., Any]):
        return self.__class__(*(self.__callback(callback, v, i, self) for i, v in enumerate(self)))
    def pop(self, index: int = -1) -> Any:
        return super().pop(index)
    def product(self) -> int:
        if not self: return 0
        value = 1
        for number in self:
            value *= number
        return value
    def random(self, *index_range):
        if not self: return None
        if index_range:
            start = index_range[0]
            end = index_range[1] if len(index_range) > 1 else len(self)
            nArray = self[start:end]
        else:
            nArray = self
        return util.random(nArray)
    def remove(self, condition: Callable[..., bool]):
        if callable(condition):
            nArray = [v for i, v in enumerate(self) if not self.__callback(condition, v, i, self)]
        else:
            value = condition
            nArray = [v for v in self if v != value]
        self[:] = nArray
    def removeduplicates(self):
        self[:] = list(dict.fromkeys(self))
    def removeindexes(self, *indices):
        sorted_indices = sorted(indices, reverse=True)
        for index in sorted_indices:
            if index < len(self) and index >= -len(self):
                del self[index]
    def removevalues(self, *values):
        unique_values = set(values)
        self[:] = [item for item in self if item not in unique_values]
    def replaceindex(self, index: int, value: Any):
        self[index] = value
    def replacevalue(self, oldvalue: Any, newvalue: Any):
        index = self.index(oldvalue)
        if index != -1:
            self[index] = newvalue
    def resize(self, size):
        old_size = len(self)
        if size < old_size:
            del self[size:]
        elif size > old_size:
            self.extend([None] * (size - old_size))
    def set(self, index: int, value: Any):
        self.insert(index, value)
    def shuffle(self):
        import random
        random.shuffle(self)
    def size(self):
        return len(self)
    def some(self, callback: Callable[..., bool]) -> bool:
        return any(self.__callback(callback, v, i, self) for i, v in enumerate(self))
    def sum(self):
        return sum(self)

class object(dict):
    def __init__(self, *values):
        super().__init__()
        for value in values:
            if value is None:
                pass
            elif isinstance(value, dict):
                self.update(value)
            else:
                self.update(object.fromdata(value))
    def __add__(self, other):
        return self.__class__(self, other)
    def __eq__(self, other: Any):
        return super().__eq__(other)
    def __iadd__(self, other):
        if isinstance(other, dict):
            self.update(other)
        return self
    def __radd__(self, other):
        return self.__class__(other, self)
    def __repr__(self) -> str:
        return f'{super().__repr__()}'

    @staticmethod
    def fromdata(data):
        nObject = object()
        if data == None:
            return nObject
        if util.istype(data, "array"):
            nObject = object.fromarray(data)
        elif util.istype(data, "bytes-array"):
            nObject = object.fromarray(util.json_decode(util.byt2str(data)))
        elif util.istype(data, "bytes-object"):
            nObject.update(util.json_decode(util.byt2str(data)))
        elif util.istype(data, "object"):
            nObject.update(data)
        elif util.istype(data, "string-object"):
            nObject.update(util.json_decode(data))
        elif util.istype(data, "string"):
            nObject = object.fromstring(data)
        else:
            raise Exception(f"TypeError: type {type(data)} unsupported")
        return nObject
    @staticmethod
    def fromarray(data: list):
        nObject = object()
        if data == None:
            return nObject
        # data = [['key','value'],['key','value']...]
        if all(util.istype(item, "array") and len(item) == 2 for item in data):
            for key, value in data:
                nObject[key] = value
        # data = ['key','value','key','value'...]
        elif len(data) % 2 == 0:
            for index in range(0, len(data), 2):
                nObject[data[index]] = data[index + 1]
        else:
            raise Exception(f"ValueError: array structure invalid")
        return nObject
    @staticmethod
    def fromkeys(keys: list[int|str], value: Any = None):
        return object(dict.fromkeys(keys, value))
    @staticmethod
    def fromstring(data: str, delimiterPairs: str = ',', delimiterPair: str = ':', remove_whitespace: bool = False):
        nObject = object()
        if data == None:
            return nObject
        for substring in data.split(delimiterPairs):
            parts = substring.split(delimiterPair, 1)
            # ensure there is at least a key and a value, the rest is considered part of the value
            # handle single key and single value
            if len(parts) == 2:
                key   = parts[0]
                value = parts[1]
            # handle a single key with no value
            elif len(parts) == 1 and parts[0]:
                key   = parts[0]
                value = None
            key = key.strip(' ') if remove_whitespace else key
            value = value.strip(' ') if remove_whitespace and not value == None else value
            nObject[key] = value
        return nObject

    def append(self, key: Any, value: Any):
        self[key] = value
    def clear(self):
        super().clear()
    def clone(self) -> 'object':
        return util.clone(self)
    def copy(self) -> 'object':
        return object(super().copy())
    def count(self, value: Any) -> int:
        return self.values().count(value)
    def dump(self) -> str:
        return util.dump(self)
    def empty(self) -> bool:
        return not bool(self)
    def excludes(self, *values) -> bool:
        return self.excludeskeys(*values)
    def excludeskeys(self, *values) -> bool:
        return all(value not in self for value in values)
    def excludesvalues(self, *values: Any) -> bool:
        object_values = super().values()
        return all(value not in object_values for value in values)
    # def get(key: str, defaultvalue: Any = None) -> Any: return super().get(key, defaultvalue)
    def hash(self, mode: str = util.HASH_MD5) -> str:
        data = util.json_encode(self)
        func = getattr(util, f"hash_{mode.lower()}", None)
        return func(data)
    def includes(self, *values) -> bool:
        return self.includeskeys(*values)
    def includeskeys(self, *values) -> bool:
        return all(value in self for value in values)
    def includesvalues(self, *values: Any) -> bool:
        object_values = super().values()
        return all(value in object_values for value in values)
    def iskey(self, key: str) -> bool:
        return key in self
    def istype(self, key: Any, datatype: str) -> bool:
        return util.istype(self.get(key), datatype)
    def ispattern(self, key: Any, pattern: str) -> bool:
        return util.ispattern(self.get(key), pattern)
    def isvalue(self, key: str, value: Any) -> bool:
        return self.get(key) == value
    def isvaluein(self, key: str, value: Any) -> bool:
        target = self.get(key)
        return isinstance(target, list) and value in target
    def json(self) -> str:
        return util.json_encode(self)
    def keys(self) -> array:
        return array(*super().keys())
    def lower(self):
        temp = {}
        for key, value in self.items():
            if isinstance(key, str):
                temp[key.lower()] = value
            else:
                temp[key] = value
        self.clear()
        self.update(temp)
    def order(self, *keys):
        cObject = self.copy()
        self.clear()
        for key in keys:
            if key in cObject:
                self[key] = cObject.pop(key)
        # retain unlisted keys at the end
        self.update(cObject)
    def remove(self, *values):
        return self.removekeys(*values)
    def removekeys(self, *values):
        for value in values:
            if value in self:
                del self[value]
        return self
    def removevalues(self, *values: Any):
        values_remove = set(values)
        new_data = {key: value for key, value in self.items() if value not in values_remove}
        self.clear()
        self.update(new_data)
    def replacekey(self, oldkey: Any, newkey: Any):
        if oldkey in self:
            value = self.pop(oldkey)
            self[newkey] = value
    def replacevalue(self, oldvalue: Any, newvalue: Any):
        for key, val in self.items():
            if val == oldvalue:
                self[key] = newvalue
    def set(self, key, value: Any):
        self[key] = value
    def size(self) -> int:
        return len(self)
    def sort(self):
        sorted_keys = sorted(self.keys())
        temp_data = {}
        for key in sorted_keys:
            temp_data[key] = self[key]
        self.clear()
        self.update(temp_data)
    def toitems(self, dimensions: int = 1) -> array:
        nArray = array()
        if dimensions == 1:
            # [key1,value1,key2,value2]
            for key, value in self.items():
                nArray.append(key, value)
        elif dimensions == 2:
            # [[key1,value1],[key2,value2]]
            for key, value in self.items():
                nArray.append(array(key, value))
        return nArray
    def tostring(self, delimiterPairs: str = ', ', delimiterPair: str = ': ') -> str:
        nArray = array()
        for key, value in self.items():
            nArray.append(f"{key}{delimiterPair}{value}")
        return nArray.join(delimiterPairs)
    def upper(self):
        temp = {}
        for key, value in self.items():
            if isinstance(key, str):
                temp[key.upper()] = value
            else:
                temp[key] = value
        self.clear()
        self.update(temp)
    def values(self) -> array:
        return array(*super().values())
#______________________________________________________________________________#
class app:
    """
    Application
    
    """
    STRING_INTERPOLATION_SYNTAX1 = r"<\w+(?:[-_]\w+)*>"
    STRING_INTERPOLATION_SYNTAX2 = r"\{\w+(?:[-_]\w+)*\}"
    STRING_INTERPOLATION_SYNTAX3 = r"%\w+(?:[-_]\w+)*%"
    
    def __init__(self):
        pass

    __arguments__: object|dict[str, str] = object()
    __configuration__: object|dict[str, int|str] = object()
    __variables__: object = object({
        # do not insert blank entries
    })
    
    executionTimerEntries: dict[str, list]|object = object()
    executionTimerPerformance: dict[str, list]|object = object()

    @staticmethod
    def __setArguments():
        import sys
        for index, value in enumerate(sys.argv[1:]):
            app.__arguments__.set(index, value)
    @staticmethod
    def __getConfiguration() -> object:
        # read application's configuration file
        data = util.file_read(f"{app.variables('path')}\\configuration.json", "application/json")
        data = object.fromdata(data)
        def pointer(obj: dict):
            for key, val in obj.items():
                if isinstance(val, dict):
                    pointer(val)
                elif isinstance(val, str):
                    obj[key] = util.string_interpolation_decode(val, app.__variables__)
                elif isinstance(val, list):
                    obj[key] = [util.string_interpolation_decode(item, app.__variables__) for item in val]
        pointer(data)
        return data
    @staticmethod
    def __setConfiguration() -> None:
        data = app.__configuration__.copy()
        def pointer(obj: dict):
            for key, val in obj.items():
                if isinstance(val, dict):
                    pointer(val)
                elif isinstance(val, str):
                    obj[key] = util.string_interpolation_encode(val, app.__variables__)
        pointer(data)
        util.file_write(f"{app.variables('path')}\\configuration.json", data)

    def main(path: str) -> None:
        """
        the path parameter holds the file path of application, use __file__
        """
        print(f"{app.getProcessIdentifier()}.{util.path_info(path, 'filename')}.{__name__}\n")
        app.__setArguments()
        app.__variables__.update(util.variables)
        app.variables("file", path.lower())
        app.variables("name", util.path_info(path.lower(), "filename"))
        app.variables("path", util.path_info(path.lower(), "dirname"))
        # load application's configuration file data
        if os.path.isfile(f"{app.variables('path')}\\configuration.json"):
            app.__configuration__ = app.__getConfiguration()
        else:
            print(f"FileNotFoundError: application configuration file not found")
    def confirm(message: str, onInvalidResponseMessage: str = "invalid") -> bool:
        message = message.strip("?: ")
        while True:
            value = input(f"{message}?: ")
            if value.lower() in ['y', 'yes', '1']:
                return True
            elif value.lower() in ['n', 'no', '0']:
                return False
            else:
                pass
            print(onInvalidResponseMessage)
    def copyToClipboard(text: str):
        import pyperclip
        try: pyperclip.copy(text)
        except pyperclip.PyperclipException as e: print(f"ClipboardCopyError: {e}")
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
        import sys
        sys.exit(0)
    def getCurrentWorkingDirectory() -> str:
        return os.getcwd()
    def getName() -> str:
        return app.variables("name")
    def getProcessIdentifier() -> int:
        return os.getpid()
    def hasArguments() -> bool:
        return any(app.__arguments__.values())
    def isArgument(key: str) -> bool:
        return app.__arguments__.iskey(key)
    def isOnline(address: tuple[str, int] = ("8.8.8.8", 53)) -> bool:
        try:
            socket.setdefaulttimeout(1000)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP).connect(address)
            return True
        except:
            return False
        finally:
            socket.setdefaulttimeout(None)
    def prompt(message: str, defaultValue: str = None, onVerification = None, onInvalidResponseMessage: str = "invalid") -> tuple[str, bool]:
        message = message.strip(": ")
        message = f"{message}: " if defaultValue == None else f"{message} ({defaultValue}): "
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
                        verificationValues = [verificationValue for verificationValue in onVerification.strip(' ').split('|')]
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
                    if type(onVerification).__name__ == "function":
                        if onVerification(value):
                            return value, not value == defaultValue
            print(onInvalidResponseMessage)
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
    def setTimeout(milliseconds: int, callback, *args, **kwargs) -> threading.Timer:
        timeout = threading.Timer(milliseconds / 1000, callback, args, kwargs)
        timeout.start()
        return timeout
    
    def arguments(key: str = None):
        if key == None:
            return app.__arguments__
        if not app.__arguments__.iskey(key):
            raise Exception(f"KeyError: application argument '{key}' nonexistent")
        else:
            value = app.__arguments__.get(key, None)
            value = util.string_conversion_decode(value)
            return value
    def configuration(key: str = None, value = None, write: bool = False):
        if key == None:
            return app.__configuration__
        elif value == None:
            if not app.__configuration__.iskey(key):
                raise Exception(f"KeyError: application configuration '{key}' nonexistent")
            else:
                value = app.__configuration__.get(key, None)
                value = util.string_conversion_decode(value)
            return value
        else:
            if not app.__configuration__.iskey(key):
                raise Exception(f"KeyError: application configuration '{key}' nonexistent")
            else:
                value = util.string_conversion_encode(value)
                app.__configuration__.set(key, value)
            if write: app.__setConfiguration()
            return value
    def variables(key: str = None, value = None):
        if key == None:
            return app.__variables__
        elif value == None:
            if not app.__variables__.iskey(key):
                print(f"KeyError: application variable '{key}' nonexistent")
            else:
                value = app.__variables__.get(key, None)
                value = util.string_conversion_decode(value)
            return value
        else:
            value = util.string_conversion_encode(value)
            app.__variables__.set(key, value)
            return value
    
    def setArguments(keys: list[str]) -> object:
        for index, key in enumerate(keys):
            app.__arguments__.set(key, app.__arguments__.get(index, None))
            app.__arguments__.pop(index)

    def setConfiguration(data):
        app.__configuration__ = object.fromdata(data)

class FaaS:
    """
    Function as a Service
    """
    class address:
        def _():
            return
        def address_space_registry_searcher(address: str, filter_enabled: bool = True) -> dict:
            def constructBinaryVariablePossibility(binary_variable: str, decimal: int):
                index_start = binary_variable.index('X')
                index_end = binary_variable.rindex('X') + 1
                binary = util.dec2bin(decimal, binary_variable.count('X'))
                return f"{binary_variable[:index_start]}{binary}{binary_variable[index_end:]}"
            def inBounds(address_binary: str, address_binary_range_start: str, address_binary_range_end: str) -> bool:
                # determine whether the address is within the provided address range
                # conducts the match in 8-bit partial chunks to avoid issues with converting large binary strings to integers
                for i in range(0, len(address_binary), 8):
                    # slice the current 8-bit segment from address
                    decimal_partial = util.bin2dec(address_binary[i:i+8])
                    # slice the corresponding 8-bit segment from the range start and end
                    decimal_range_partial_start = util.bin2dec(address_binary_range_start[i:i+8])
                    decimal_range_partial_end   = util.bin2dec(address_binary_range_end[i:i+8])
                    if (decimal_partial < decimal_range_partial_start or decimal_range_partial_end < decimal_partial):
                        return False
                return True
            # filter and retrieve table data where the entry's address range includes the input address
            address_space_registry: dict = util.file_read_json(f"{app.variables('repository')}\\address-space-registry.json")
            tables = { }
            address_binary: str = util.address_binary(address)
            address_family: str = util.address_family(address_binary)
            address_space_registry_family: dict[str, list[dict]] = address_space_registry[address_family]
            for tablename, entries in address_space_registry_family.items():
                tables[tablename] = [  ]
                for index, entry in enumerate(entries):
                    # address unspecified, insert all entries
                    if not filter_enabled:
                        tables[tablename] += [entry]
                        continue
                    if not address:
                        continue
                    address_binary_range: list[str] = entry["binary"]
                    address_binary_range_start = address_binary_range[0] if len(address_binary_range) != 0 else None
                    address_binary_range_end   = address_binary_range[1] if len(address_binary_range) == 2 else None
                    # case 0: size == 0
                    if len(address_binary_range) == 0:
                        continue
                    # case 1: size == 1 and variable prefix match
                    elif len(address_binary_range) == 1 and ('X' in address_binary_range_start):
                        binary_variable_length = address_binary_range_start.count('X')
                        for decimal in range(2**binary_variable_length):
                            address_binary_range_possibility_start = constructBinaryVariablePossibility(address_binary_range_start, decimal)
                            if address_binary.startswith(address_binary_range_possibility_start):
                                tables[tablename] += [entry]
                                break
                    # case 2: size == 1 and fixed prefix match
                    elif len(address_binary_range) == 1:
                        if address_binary.startswith(address_binary_range_start):
                            tables[tablename] += [entry]
                    # case 3: size == 2 and variable range match
                    elif len(address_binary_range) == 2 and ('X' in address_binary_range_start or 'X' in address_binary_range[1]):
                        binary_variable_length = address_binary_range_start.count('X')
                        for decimal in range(2**binary_variable_length):
                            address_binary_range_possibility_start = constructBinaryVariablePossibility(address_binary_range_start, decimal)
                            address_binary_range_possibility_end   = constructBinaryVariablePossibility(address_binary_range_end, decimal)
                            if inBounds(address_binary, address_binary_range_possibility_start, address_binary_range_possibility_end):
                                tables[tablename] += [entry]
                                break
                    # case 4: size == 2 and fixed range match
                    elif len(address_binary_range) == 2:
                        if inBounds(address_binary, address_binary_range_start, address_binary_range_end):
                            tables[tablename] += [entry]
            return tables
    class aviation:
        ISA_ATMOSPHERIC_PROPERTIES = [
            {"altitude": "00000", "temperature": " 15.2"},
            {"altitude": "00500", "temperature": " 14.2"},
            {"altitude": "01000", "temperature": " 13.2"},
            {"altitude": "01500", "temperature": " 12.2"},
            {"altitude": "02000", "temperature": " 11.2"},
            {"altitude": "02500", "temperature": " 10.2"},
            {"altitude": "03000", "temperature": " 09.3"},
            {"altitude": "03500", "temperature": " 08.3"},
            {"altitude": "04000", "temperature": " 07.3"},
            {"altitude": "04500", "temperature": " 06.3"},
            {"altitude": "05000", "temperature": " 05.3"},
            {"altitude": "05500", "temperature": " 04.3"},
            {"altitude": "06000", "temperature": " 03.3"},
            {"altitude": "06500", "temperature": " 02.3"},
            {"altitude": "07000", "temperature": " 01.3"},
            {"altitude": "07500", "temperature": " 00.3"},
            {"altitude": "08000", "temperature": "-00.6"},
            {"altitude": "08500", "temperature": "-01.6"},
            {"altitude": "09000", "temperature": "-02.6"},
            {"altitude": "09500", "temperature": "-03.6"},
            {"altitude": "10000", "temperature": "-04.6"}
        ]
        
        PARAMETER_PATTERN_ALTITUDE    = r"^\d{1,5}$"
        PARAMETER_PATTERN_AZIMUTH     = r"^(0?\d?\d|[1-2]\d\d|3[0-5]\d)(\.\d)?$"
        PARAMETER_PATTERN_COORDINATE  = r"^-?([0-8]?\d)(\.\d+)? -?(0?\d?\d|1[0-7]\d)(\.\d+)?$"
        PARAMETER_PATTERN_DISTANCE    = r"^\d{1,3}(\.\d)?$"
        PARAMETER_PATTERN_HOURS       = r"^\d{1,3}(\.\d)?$"
        PARAMETER_PATTERN_LATITUDE    = r"^-?([0-8]?\d)(\.\d+)?$"
        PARAMETER_PATTERN_LONGITUDE   = r"^-?(0?\d?\d|1[0-7]\d)(\.\d+)?$"
        PARAMETER_PATTERN_MINUTES     = r"^(0?\d|[1-5]\d)$"
        PARAMETER_PATTERN_PRESSURE    = r"^\d\d\.\d\d?$"
        PARAMETER_PATTERN_SPEED       = r"^\d{1,3}$"
        PARAMETER_PATTERN_TEMPERATURE = r"^-?\d\d?(\.\d)?$"
        PARAMETER_PATTERN_ZENITH      = r"^-?([0-8]?\d(\.\d\d?)?|90(\.00?)?)$"
        
        def density_altitude(altitude: float, pressure: float, temperature: float) -> str:
            pressure_altitude = (29.92 - pressure) * 1000 + altitude
            standard_air_temperature = 15.2 - 0.002 * pressure_altitude
            density_altitude = pressure_altitude + (120 * (temperature - standard_air_temperature))
            return f"{density_altitude:05.0f}"
        def distance(groundspeed: float, hours: float, minutes: float) -> str:
            time = hours + minutes/60
            distance = groundspeed * time
            return f"{distance:05.1f}"
        def feet_per_minute1(groundspeed: float, pitch_angle: float = None) -> str:
            if pitch_angle:
                feet_per_minute = (groundspeed/60*pitch_angle)*100
            else:
                feet_per_minute = groundspeed * 5
            return ('' if feet_per_minute >= 0 else '-') + f"{abs(feet_per_minute):04.0f}"
        def feet_per_minute2(groundspeed: float, flight_path_angle) -> str:
            b=6076.1154855643
            feet_per_nautical_mile = ((b/math.cos(math.radians(flight_path_angle)))**2-b**2)**0.5
            feet_per_minute = feet_per_nautical_mile * (groundspeed/60)
            return ('' if feet_per_minute >= 0 else '-') + f"{abs(feet_per_minute):04.0f}"
        def pressure_altitude(altitude: float, pressure: float) -> str:
            pressure_altitude = (29.92 - pressure) * 1000 + altitude
            return f"{pressure_altitude:05.0f}"
        def temperature_deviation(altitude: float, temperature: float) -> str:
            entries = FaaS.aviation.ISA_ATMOSPHERIC_PROPERTIES
            isa_temperature = None
            for index, entry in enumerate(entries):
                if index == 0: continue
                aAltitude = int(entries[index-1]["altitude"])
                bAltitude = int(entries[index]["altitude"])
                aTemperature = float(entries[index-1]["temperature"])
                bTemperature = float(entries[index]["temperature"])
                if aAltitude <= altitude and altitude <= bAltitude:
                    degrees_per_foot = (aTemperature - bTemperature) / (bAltitude - aAltitude)
                    b = altitude - aAltitude
                    isa_temperature = aTemperature - (degrees_per_foot * b)
                    break
            temperature_deviation = temperature - isa_temperature
            return ('' if temperature_deviation >= 0 else '-') + f"{abs(temperature_deviation):04.1f}"
        def time(distance: float, groundspeed: float) -> str:
            time = distance / groundspeed
            hours = math.floor(time)
            minutes = (time - hours) * 60
            return f"{hours:05.1f}" if hours >= 100 else f"{hours:02.0f}{minutes:02.0f}"
        def top_of_descent(altitude: float, target_altitude: float, speed: float, target_speed: float) -> str:
            # for standard 3° descent, 3 to 1 rule
            top_of_descent = (altitude-target_altitude)/1000*3 + (speed-target_speed)/10
            return f"{top_of_descent:05.1f}"
        def true_airspeed(altitude: float, indicated_airspeed: float) -> str:
            true_airspeed = indicated_airspeed * (1 + (altitude/1000*0.02))
            return f"{true_airspeed:03.0f}"
        def turn_radius(airspeed: float, bank_angle: float) -> str:
            turn_radius = (airspeed**2)/(11.26*math.tan(math.radians(bank_angle)))
            turn_radius *= 0.0001645788336933
            return f"{turn_radius:.1f}"
        def visual_descent_point1(runway_latitude: float, runway_longitude: float, final_approach_fix_latitude: float, final_approach_fix_longitude: float, final_approach_fix_distance_indicated: float, visual_decent_point_distance_indicated: float):
            runway = [runway_latitude, runway_longitude]
            final_approach_fix = [final_approach_fix_latitude, final_approach_fix_longitude]
            faf_to_rwy_azimuth = util.geographic_to_azimuth(final_approach_fix, runway)
            faf_to_rwy_distance = util.geographic_to_distance(final_approach_fix, runway)
            faf_to_rwy_distance_offset = faf_to_rwy_distance - (final_approach_fix_distance_indicated*1852)
            vdp_to_rwy_distance_calculated = (visual_decent_point_distance_indicated*1852) + faf_to_rwy_distance_offset
            faf_to_vdp_distance = faf_to_rwy_distance - vdp_to_rwy_distance_calculated
            vdp = util.geographic_to_destination_point(final_approach_fix, faf_to_rwy_azimuth, faf_to_vdp_distance)
            return f"{vdp[0]:.6f} {vdp[1]:.6f}"
        def visual_descent_point2(runway_touchdown_latitude: float, runway_touchdown_longitude: float, final_approach_fix_latitude: float, final_approach_fix_longitude: float, height_above_touchdown: float, vertical_descent_angle: float):
            touchdown_zone   = [runway_touchdown_latitude, runway_touchdown_longitude]
            final_approach_fix = [final_approach_fix_latitude, final_approach_fix_longitude]
            a = height_above_touchdown*0.3048
            vdp_to_tdz_distance = ((a/math.sin(math.radians(vertical_descent_angle)))**2-a**2)**0.5
            tdz_to_faf_azimuth = util.geographic_to_azimuth(touchdown_zone, final_approach_fix)
            vdp = util.geographic_to_destination_point(touchdown_zone, tdz_to_faf_azimuth, vdp_to_tdz_distance)
            return f"{vdp[0]:.6f} {vdp[1]:.6f}"
        def wind_correction_angle(aircraft_course: float, aircraft_true_airspeed: float, wind_direction: float, wind_speed: float):
            # the acute angle between the wind direction and your desired course
            wind_angle = math.radians(aircraft_course - (180 + wind_direction))
            wind_correction_angle = math.asin((wind_speed * math.sin(wind_angle))/aircraft_true_airspeed)
            wind_correction_angle = math.degrees(wind_correction_angle)
            return f"{wind_correction_angle:04.1f}"
        def VAPP(VREF: float, runway_direction: float, wind_direction: float, wind_speed: float, wind_gust: float = 0) -> str:
            headwind = wind_speed * math.cos(math.radians(abs(runway_direction - wind_direction)))
            correction = max(min(headwind/2 + wind_gust, 20), 5)
            VAPP = VREF + correction
            return f"{VAPP:03.0f}"
        def VLS(VS1g: float) -> str:
            VLS = 1.23 * VS1g
            return f"{VLS:03.0f}"
        def VREF(VSO: float) -> str:
            VREF = 1.3 * VSO
            return f"{VREF:03.0f}"
    class networking:
        def convert(address: str) -> dict:
            results = { "family": None, "types": [], "format": None, "associations": {} }
            def type_number(address: str):
                results["family"] = "Number"
                results["format"] = "XX"
                results["types"] += ["Classless Inter-Domain Routing"]
                results["associations"]["Network Mask"] = util.address_string(util.address_prefix_length_to_mask(address))
                results["associations"]["Wildcard Mask"] = util.address_string(util.address_prefix_length_to_wildcardmask(address))
                results["associations"]["Address Count"] = util.address_prefix_length_to_address_count(address)
            def type_pointer(address: str):
                # TODO: complete
                results["family"] = "DNS Pointer"
                results["format"] = ""
            def type_ipv4(address: str):
                results["family"] = "Internet Protocol v4"
                results["format"] = "XXX.XXX.XXX.XXX"
                if util.istype(address, "binary"):
                    results["associations"]["IPv4"] = util.address_string(address)
                if util.istype(address, "address-internet_protocol_v4-benchmarking"):
                    results["types"] += ["Benchmarking"]
                if util.istype(address, "address-internet_protocol_v4-broadcast"):
                    results["types"] += ["Broadcast"]
                if util.istype(address, "address-internet_protocol_v4-dummy"):
                    results["types"] += ["Dummy"]
                if util.istype(address, "address-internet_protocol_v4-local-link"):
                    results["types"] += ["Link Local"]
                if util.istype(address, "address-internet_protocol_v4-local-unique"):
                    results["types"] += ["Unique Local"]
                if util.istype(address, "address-internet_protocol_v4-loopback"):
                    results["types"] += ["Loopback"]
                if util.istype(address, "address-internet_protocol_v4-multicast"):
                    results["types"] += ["Multicast"]
                    results["associations"]["MAC Multicast"] = util.address_string(util.address_ipv4_to_mac_multicast(address))
                if util.istype(address, "address-internet_protocol_v4-networkmask"):
                    results["types"] += ["Network mask"]
                    results["associations"]["Prefix Length"] = f"/{util.address_mask_to_prefix_length(address)}"
                    results["associations"]["Wildcard mask"] = util.address_string(util.address_mask_to_wildcardmask(address))
                    results["associations"]["Address Count"] = util.address_prefix_length_to_address_count(util.address_mask_to_prefix_length(address))
                if util.istype(address, "address-internet_protocol_v4-wildcardmask"):
                    results["types"] += ["Wildcard mask"]
                    results["associations"]["Prefix Length"] = f"/{util.address_wildcardmask_to_prefix_length(address)}"
                    results["associations"]["Network mask"] = util.address_string(util.address_wildcardmask_to_mask(address))
                    results["associations"]["Address Count"] = util.address_prefix_length_to_address_count(util.address_wildcardmask_to_prefix_length(address))
                if util.istype(address, "address-internet_protocol_v4-unicast"):
                    results["types"] += ["Unicast"]
                    results["associations"]["IPv6 IPv4-mapped"] = util.address_string(util.address_ipv4_to_ipv6_4to6(address))
                    results["associations"]["IPv6 6to4"] = util.address_string(util.address_ipv4_to_ipv6_6to4(address))
                    results["associations"]["DNS Pointer Record Name"] = util.address_ipv4_to_ptr(address)
                if util.istype(address, "address-internet_protocol_v4-unspecified"):
                    results["types"] += ["Unspecified"]
            def type_ipv6(address: str):
                results["family"] = "Internet Protocol v6"
                results["format"] = "XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX"
                if util.istype(address, "binary"):
                    results["associations"]["IPv6"] = util.address_string(address)
                if util.istype(address, "address-internet_protocol_v6-4to6"):
                    results["types"] += ["IPv4-mapped"]
                    results["associations"]["IPv4"] = util.address_string(util.address_ipv6_to_ipv4(address))
                if util.istype(address, "address-internet_protocol_v6-6to4"):
                    results["types"] += ["IPv6 to IPv4"]
                    results["associations"]["IPv4"] = util.address_string(util.address_ipv6_to_ipv4(address))
                if util.istype(address, "address-internet_protocol_v6-anycast"):
                    results["types"] += ["Anycast"]
                if util.istype(address, "address-internet_protocol_v6-benchmarking"):
                    results["types"] += ["Benchmarking"]
                if util.istype(address, "address-internet_protocol_v6-documentation"):
                    results["types"] += ["Documentation"]
                if util.istype(address, "address-internet_protocol_v6-global"):
                    results["types"] += ["Global"]
                if util.istype(address, "address-internet_protocol_v6-local-link"):
                    results["types"] += ["Link Local"]
                    results["associations"]["MAC Unicast"] = util.address_string(util.address_ipv6_to_mac(address))
                if util.istype(address, "address-internet_protocol_v6-local-unique"):
                    results["types"] += ["Unique Local"]
                if util.istype(address, "address-internet_protocol_v6-loopback"):
                    results["types"] += ["Loopback"]
                if util.istype(address, "address-internet_protocol_v6-multicast"):
                    results["types"] += ["Multicast"]
                    results["associations"]["MAC Multicast"] = util.address_string(util.address_ipv6_to_mac_multicast(address))
                if util.istype(address, "address-internet_protocol_v6-teredo"):
                    results["types"] += ["Teredo"]
                if util.istype(address, "address-internet_protocol_v6-unicast"):
                    results["associations"]["DNS Pointer Record Name"] = util.address_ipv6_to_ptr(address)
                if util.istype(address, "address-internet_protocol_v6-unspecified"):
                    results["types"] += ["Unspecified"]
            def type_mac(address: str):
                results["family"] = "Media Access Control"
                results["format"] = "XX-XX-XX-XX-XX-XX"
                if util.istype(address, "binary"):
                    results["associations"]["MAC"] = util.address_string(address)
                if util.istype(address, "address-media_access_control-broadcast"):
                    results["types"] += ["Broadcast"]
                if util.istype(address, "address-media_access_control-multicast-ipv4"):
                    results["types"] += ["Multicast"]
                    results["associations"]["IPv4 Multicast"] = f"239.XXX.{util.bin2dec(address[32:40])}.{util.bin2dec(address[40:48])}"
                if util.istype(address, "address-media_access_control-multicast-ipv6"):
                    results["types"] += ["Multicast"]
                    results["associations"]["IPv6 Multicast"] = util.address_string(f"{util.hex2bin('ff').ljust(96, '0')}{address[16:48]}")
                if util.istype(address, "address-media_access_control-unicast"):
                    results["types"] += ["Unicast"]
                    results["associations"]["IPv6 Link Local"] = util.address_string(util.address_mac_to_ipv6_local_link(address, util.hex2bin("fe80000000000000")))
            def set_number_base(results):
                results["base02"] = util.address_binary(address)
                results["base10"] = util.address_decimal(address)
                results["base16"] = util.address_hexadecimal(address)
            if   util.istype(address, "address-internet_protocol_v4-prefix-length"):
                type_number(address)
                set_number_base(results)
            elif util.istype(address, "address-internet_protocol_v4"):
                type_ipv4(address)
                set_number_base(results)
            elif util.istype(address, "address-internet_protocol_v6"):
                type_ipv6(address)
                set_number_base(results)
            elif util.istype(address, "address-media_access_control"):
                type_mac(address)
                set_number_base(results)
            else:
                pass
            return results
        def protocols_searcher(protocol: str, filter_enabled: bool = True):
            matches = [  ]
            networking_protocols: dict = util.file_read_json(f"{app.variables('repository')}\\networking-protocols.json")
            for entry in networking_protocols:
                if not filter_enabled:
                    matches.append(entry)
                    continue
                if not protocol:
                    continue
                elif protocol == entry["Decimal"]:
                    matches.append(entry)
                elif protocol.lower() in str(entry["Protocol"]).lower():
                    matches.append(entry)
            return matches
        def services_searcher(service: str, filter_enabled: bool = True):
            matches = [  ]
            networking_protocols: dict = util.file_read_json(f"{app.variables('repository')}\\networking-services.json")
            for entry in networking_protocols:
                if not filter_enabled:
                    matches.append(entry)
                    continue
                if not service:
                    continue
                elif service == entry["Port Number"]:
                    matches.append(entry)
                elif service.lower() in str(entry["Service Name"]).lower():
                    matches.append(entry)
            return matches

class Logger(threading.Thread):
    def __init__(self, path: str = None):
        super().__init__()
        from queue import Queue
        self.queue = Queue()
        self.path = path
        self.stopped = False
        self.start()

    def run(self):
        while True:
            entry = self.queue.get()
            if entry is None:
                break
            timestamp = entry["timestamp"]
            stamp = util.timestamp_date(util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT))
            # util.file_append(f"{self.path}\\{stamp}.txt", f"{util.json_encode(entry)}\n")
            util.file_append_json(f"{self.path}\\{stamp}.json", entry)

    def print(self, entry: dict|str):
        if isinstance(entry, str):
            print(f"\n{entry}")
        if isinstance(entry, dict):
            print(f"\n{Logger.dump(entry)}")
    def put(self, entry: dict):
        timestamp = util.timestamp(util.TIMESTAMP_OPTION_OBJECT)
        timestamp = f"{util.timestamp_date(timestamp)}T{util.timestamp_time(timestamp)}"
        entry_ = { "timestamp": timestamp }
        entry_.update(entry)
        self.queue.put(entry_)
        print(f'\n{Logger.dump(entry_)}')
        return self
    def out(path: str, print_to_screen: bool, entry: dict):
        timestamp = util.timestamp(util.TIMESTAMP_OPTION_OBJECT)
        timestamp = f"{util.timestamp_date(timestamp)}T{util.timestamp_time(timestamp)}"
        entry_ = { "timestamp": timestamp }
        entry_.update(entry)
        if print_to_screen: print(f"\n{Logger.dump(entry_)}")
        if not path == None:
            stamp = util.timestamp_date(util.timestamp(timestamp, util.TIMESTAMP_OPTION_OBJECT))
            util.file_append_json(f"{path}\\{stamp}.json", entry_)
    def stop(self) -> None:
        self.queue.put(None)
    def dump(entry: dict) -> str:
        def get(value) -> str:
            if value == None:
                return "null"
            elif isinstance(value, bool):
                return str(value)
            elif isinstance(value, float|int):
                return str(value)
            elif isinstance(value, str):
                return value
            elif isinstance(value, dict):
                string = '{'
                end = [key for key in value.keys()][-1] if len(value.keys()) > 0 else None
                for key, val in value.items():
                    string += f"{get(key)}: {get(val)}" + ('' if key == end else ', ')
                string += '}'
                return string
            elif isinstance(value, list):
                string = '['
                end = value[-1]
                for val in value:
                    string += get(val) + ('' if val == end else ', ')
                string += ']'
                return string
        string = f"{entry['timestamp']}: "
        end = [key for key in entry.keys()][-1]
        for key, val in entry.items():
            if key == "timestamp": continue
            string += f"{get(key)}: {get(val)}" + ('' if key == end else ', ')
        return string

#______________________________________________________________________________#

util.variables.update(util.file_read("...variables.json", "application/json"))
for key, val in util.variables.items():
    if isinstance(val, str):
        util.variables[key] = util.string_interpolation_decode(val, util.variables)

# _____________________________________________________________________________#

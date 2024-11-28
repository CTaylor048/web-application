/**
 * @author Corey Taylor <coreyjtaylor048@gmail.com>
 * @typedef {string} address
 * @typedef {[]} array
 * @typedef {"0"|"1"} bit
 * @typedef {string} binary
 * @typedef {Int8Array|Uint8Array} bytes
 * @typedef {string} hexadecimal
 * @typedef {{}} object
 * @typedef {number} port
 * @typedef {Date|number|string} timestamp
 * 
 * 
 * Error
 * 
 * ArrayLengthError: variable-name= variable-length=${.length} length=<eq|ge|gt|le|lt>${}
 * KeyError: variable-name= key=${}
 * IndexError: variable-name= variable-length=${.length} index=${}
 * StringLengthError: variable-name= variable-length=${.length} length=<eq|ge|gt|le|lt>${}
 * TypeError: variable-name= variable-value=${} variable-type=${type()} type=
 * UnsetError: variable-name=
 * ValueError: variable-name= variable-value=${}
 * 
 * console.error(``)
 * 
 * Ctrl+Shift+P > Generate JSDoc
 */
Array.prototype.append = function (...values) {
    this.push(...values)
}
Array.prototype.clear = function (...values) {
    this.splice(0, this.length)
}
Array.prototype.copy = function (index, start = 0, stop = this.length) {
    let nArray = new array()
    for (let i = start; i < stop; i++) {
        nArray.append(this[i])
    }
    return nArray
}
Array.prototype.count = function (value) {
    let count = 0
    for (let value_ of this) {
        if (value_ == value) {
            count += 1
        }
    }
    return count
}
Array.prototype.empty = function () {
    return this.length == 0
}
Array.prototype.enumerate = function* () {
    for (let index = 0; index < this.length; index++) {
        yield [index, this[index]]
    }
}
Array.prototype.get = function (index, defaultvalue = null) {
    let value = this[index < 0 ? index + this.length : index]
    return value == null ? defaultvalue : value
}
Array.prototype.getFirst = function () {
    return this[0]
}
Array.prototype.getLast = function () {
    return this[this.length - 1]
}
Array.prototype.index = function (value, start = 0) {
    return this.indexOf(value, start)
}
Array.prototype.insert = function (index, value) {
    this.splice(index, 0, value)
}
Array.prototype.pop = function (index = -1) {
    this.splice(index, 1)
}
Array.prototype.remove = function (...values) {
    for (let value of values) {
        let index = this.indexOf(value)
        this.splice(index, 1)
    }
}
Array.prototype.set = function (index, value) {
    this.splice(index, 0, value)
}
Array.prototype.size = function () {
    return this.length
}
String.prototype.capitalize = function () {
    return this[0].toUpperCase() + this.slice(1).toLowerCase()
}
String.prototype.casefold = function () {
    return this.toLowerCase()
}
String.prototype.center = function (length, character = ' ') {
    let nString = this.toString()
    if (nString.length < length) {
        let leftCharacterCount = Math.ceil((length - nString.length) / 2)
        let rightCharacterCount = Math.floor((length - nString.length) / 2)
        nString = character.repeat(leftCharacterCount) + nString + character.repeat(rightCharacterCount)
    }
    return nString
}
String.prototype.count = function (value, start = 0, end = this.length) {
    let count = 0
    let i = start
    while (i < end) {
        if (this.slice(i, i + value.length) == value) {
            count += 1
            i += value.length
        } else {
            i += 1
        }
    }
    return count
}
String.prototype.empty = function () {
    return this.length == 0
}
String.prototype.encode = function (encoding = 'UTF-8', errors) {
    return
}
String.prototype.endswith = function (value, start = 0, end = this.length) {
    let string = this.slice(start, end)
    return string.indexOf(value) == string.length - value.length
}
String.prototype.expandtabs = function (tabsize) {
    let string = this.toString()
    return string.replaceAll('\t', ' '.repeat(tabsize))
}
String.prototype.find = function (value, start = 0, end = this.length) {
    let string = this.slice(start, end)
    let index = string.indexOf(value)
    return index == -1 ? index : index + start
}
String.prototype.format = function () {
    return
}
String.prototype.format_map = function () {
    return
}
String.prototype.identifier = function () {
    let string = this.toString()
    let nString = ''
    let allowedCharacters = '0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z _ a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
    let notAllowedFirstCharacters = '0 1 2 3 4 5 6 7 8 9'.split(' ')
    for (let i = 0; i < this.length; i++) {
        let character = string[i]
        if (i == 0 && notAllowedFirstCharacters.includes(character)) {
            nString += '_' + character
        }
        else if (!allowedCharacters.includes(character)) {
            nString += '_'
        }
        else {
            nString += character
        }
    }
    return nString.toLowerCase()
}
String.prototype.index = function (value, start = 0, end = this.length) {
    // TODO: overload function - create function that receives one or more characters returns the index of character that comes before others
    let string = this.slice(start, end)
    let index = string.indexOf(value)
    return index == -1 ? index : index + start
}
String.prototype.isalnum = function () {
    if (this.length == 0) return false
    let allowedCharacters = '0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
    for (let character of this.toString()) {
        if (!allowedCharacters.includes(character)) {
            return false
        }
    }
    return true
}
String.prototype.isalpha = function () {
    if (this.length == 0) return false
    let allowedCharacters = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
    for (let character of this.toString()) {
        if (!allowedCharacters.includes(character)) {
            return false
        }
    }
    return true
}
String.prototype.isdecimal = function () {
    if (this.length == 0) return false
    let allowedCharacters = '0 1 2 3 4 5 6 7 8 9'.split(' ')
    for (let character of this.toString()) {
        if (!allowedCharacters.includes(character)) {
            return false
        }
    }
    return true
}
String.prototype.isdigit = function () {
    if (this.length == 0) return false
    let allowedCharacters = '0 1 2 3 4 5 6 7 8 9 ² ³'.split(' ')
    for (let character of this.toString()) {
        if (!allowedCharacters.includes(character)) {
            return false
        }
    }
    return true
}
String.prototype.isidentifier = function () {
    if (this.length == 0) return false
    let allowedCharacters = '0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z _ a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
    let notAllowedFirstCharacters = '0 1 2 3 4 5 6 7 8 9'.split(' ')
    let isFirstCharacter = true
    for (let character of this.toString()) {
        if (isFirstCharacter) {
            if (notAllowedFirstCharacters.includes(character)) return false
            isFirstCharacter = false
        }
        if (!allowedCharacters.includes(character)) {
            return false
        }
    }
    return true
}
String.prototype.islower = function () {
    if (this.length == 0) return false
    let notAllowedCharacters = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split(' ')
    for (let character of this.toString()) {
        if (notAllowedCharacters.includes(character)) {
            return false
        }
    }
    return true
}
String.prototype.isnumeric = function () {
    if (this.length == 0) return false
    let allowedCharacters = '0 1 2 3 4 5 6 7 8 9 ² ³'.split(' ')
    for (let character of this.toString()) {
        if (!allowedCharacters.includes(character)) {
            return false
        }
    }
    return true
}
String.prototype.isprintable = function () {
    let notAllowedCharacters = '\n \r \t \b \f'.split(' ')
    for (let character of this.toString()) {
        if (notAllowedCharacters.includes(character)) {
            return false
        }
    }
    return true
}
String.prototype.isspace = function () {
    if (this.length == 0) return false
    for (let character of this.toString()) {
        if (character != ' ') {
            return false
        }
    }
    return true
}
String.prototype.istitle = function () {
    if (this.length == 0) return false
    let allowedCharacters = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split(' ')
    let strings = this.toString().split(' ')
    for (let string of strings) {
        string = string.trim()
        if (string.length == 0) continue
        if (!allowedCharacters.includes(string[0])) return false
    }
    return true
}
String.prototype.isupper = function () {
    if (this.length == 0) return false
    let notAllowedCharacters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
    for (let character of this.toString()) {
        if (notAllowedCharacters.includes(character)) {
            return false
        }
    }
    return true
}
String.prototype.join = function (iterable) {
    let string = ''
    for (let item of iterable) {
        string += (string.length == 0 ? '' : this.toString()) + item.toString()
    }
    return string
}
String.prototype.ljust = function (length, character = ' ') {
    let nString = this.toString()
    if (nString.length < length) {
        let characterCount = length - nString.length
        nString = nString + character.repeat(characterCount)
    }
    return nString
}
String.prototype.lower = function () {
    return this.toLowerCase()
}
String.prototype.lstrip = function (characters = ' ') {
    let nString = this.toString()
    characters = characters.split('')
    characters = characters.filter((character, index) => characters.indexOf(character) == index)
    while (true) {
        let index = 0
        let character = nString[index]
        if (characters.includes(character) && nString.length > 0) {
            nString = nString.slice(0, index) + nString.slice(index + 1, nString.length)
        }
        else {
            break
        }
    }
    return nString
}
String.prototype.maketrans = function () {
    return
}
String.prototype.remove = function (...substrings) {
    let nString = this.toString()
    for (let substring of substrings) {
        nString = nString.replaceAll(substring, '')
    }
    return nString
}
String.prototype.removeprefix = function (prefix) {
    let string = this.toString()
    if (string.indexOf(prefix) == 0) {
        string = string.slice(prefix.length, string.length)
    }
    return string
}
String.prototype.reverse = function () {
    let nString = ""
    let string = this.toString()
    for (let i = string.length - 1; i >= 0; i--) {
        nString += string[i]
    }
    return nString
}
String.prototype.rfind = function (value, start = 0, end = this.length) {
    let string = this.slice(start, end)
    let index = string.lastIndexOf(value)
    return index == -1 ? index : index + start
}
String.prototype.rindex = function (value, start = 0, end = this.length) {
    let string = this.slice(start, end)
    let index = string.lastIndexOf(value)
    return index == -1 ? index : index + start
}
String.prototype.rjust = function (length, character = ' ') {
    let nString = this.toString()
    if (nString.length < length) {
        let characterCount = length - nString.length
        nString = character.repeat(characterCount) + nString
    }
    return nString
}
String.prototype.rpartition = function (value) {
    let string = this.toString()
    let tuple = [string, '', '']
    let index = string.lastIndexOf(value)
    if (index != -1) {
        tuple[0] = string.slice(0, index)
        tuple[1] = string.slice(index, index + value.length)
        tuple[2] = string.slice(index + value.length, string.length)
    }
    return tuple
}
String.prototype.rsplit = function () {
    return
}
String.prototype.rstrip = function (characters = ' ') {
    let nString = this.toString()
    characters = characters.split('')
    characters = characters.filter((character, index) => characters.indexOf(character) == index)
    while (true) {
        let index = nString.length - 1
        let character = nString[index]
        if (characters.includes(character)) {
            nString = nString.slice(0, index) + nString.slice(index + 1, nString.length)
        }
        else {
            break
        }
    }
    return nString
}
String.prototype.size = function () {
    return this.length
}
String.prototype.splitlines = function (keeplinebreaks = false) {
    let lines = this.split(/\r?\n/)
    if (keeplinebreaks) {
        lines = lines.map((line, index) => line + (index == lines.length - 1 ? '' : '\n'))
    }
    return lines
}
String.prototype.startswith = function (value, start = 0, end = this.length) {
    let string = this.slice(start, end)
    return string.indexOf(value) == 0
}
String.prototype.strip = function (characters = ' ') {
    let nString = this.toString()
    characters = characters.split('')
    characters = characters.filter((character, index) => characters.indexOf(character) == index)
    let side = true
    while (true) {
        let index = side ? 0 : nString.length - 1
        let character = nString[index]
        if (characters.includes(character) && nString.length > 0) {
            nString = nString.slice(0, index) + nString.slice(index + 1, nString.length)
        }
        else {
            if (side) {
                side = false
            } else {
                break
            }
        }
    }
    return nString
}
String.prototype.swapcase = function () {
    let nString = ''
    let uppercaseCharacters = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split(' ')
    for (let character of this.toString()) {
        if (uppercaseCharacters.includes(character)) {
            nString += character.toLowerCase()
        } else {
            nString += character.toUpperCase()
        }
    }
    return nString
}
String.prototype.title = function () {
    let nStrings = []
    let alphaCharacters = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
    let numericCharacters = '0 1 2 3 4 5 6 7 8 9'.split(' ')
    for (let string of this.split(' ')) {
        let nString = ''
        let upperCased = false
        for (let character of string.split('')) {
            if (alphaCharacters.includes(character) && !upperCased) {
                character = character.toUpperCase()
                upperCased = true
            }
            if (numericCharacters.includes(character)) {
                upperCased = false
            }
            nString += character
        }
        nStrings.push(nString)
    }
    return nStrings.join(' ')
}
String.prototype.translate = function () {
    return
}
String.prototype.upper = function () {
    return this.toUpperCase()
}
String.prototype.zfill = function (len) {
    let nString = this.toString()
    if (nString.length < len) {
        let count = len - nString.length
        nString = '0'.repeat(count) + nString
    }
    return nString
}
//_________________________________________________________________________________________________________________________________________________//
class util {
    constructor() {
    }

    // DATE-TIME
    /** @readonly @type {string[]} */
    static DAYS_OF_WEEK = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    /** @readonly @type {string[]} */
    static MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    /** @readonly @type {string[]} */
    static QUARTERS = ['First', 'Second', 'Third', 'Fourth']

    // MATHEMATICS
    /** @readonly @type {number} */
    static DEGREES_TO_RADIANS  = Math.PI / 180
    /** @readonly @type {number} */
    static RADIANS_TO_DEGREES  = 180 / Math.PI
    /** @readonly @type {number} kilometers to mean sea level elevation */
    static SPHERE_RADIUS = 6371000

    // TABLE
    /** @readonly @type {string} */
    static TABLE_ORIENTATION_VERTICAL = 'vertical'
    /** @readonly @type {string} */
    static TABLE_ORIENTATION_HORIZONTAL = 'horizontal'

    // HTML
    /** @readonly @type {string[][]} */
    static CHARACTER_ENTITIES = [[' ', '&nbsp;'], ['!', '&excl;'], ['"', '&quot;'], ['#', '&num;'], ['$', '&dollar;'], ['%', '&percnt;'], ['&', '&amp;'], ['\'', '&apos;'], ['(', '&lpar;'], [')', '&rpar;'], ['*', '&ast;'], ['+', '&plus;'], [',', '&comma;'], ['-', '&minus;'], ['.', '&period;'], ['/', '&sol;'], [':', '&colon;'], [';', '&semi;'], ['<', '&lt;'], ['=', '&equals;'], ['>', '&gt;'], ['?', '&quest;'], ['@', '&commat;'], ['[', '&lsqb;'], ['\\', '&bsol;'], [']', '&rsqb;'], ['^', '&Hat;'], ['_', '&lowbar;'], ['`', '&grave;'], ['{', '&lcub;'], ['|', '&verbar;'], ['}', '&rcub;'], ['~', '&tilde;']]
    /** @readonly @type {string[]} */
    static TAGS = [
        '!doctype',
        'a', 'abbr', 'address', 'area', 'article', 'aside', 'audio',
        'b', 'base', 'bb', 'bdi', 'bdo', 'big', 'blockquote', 'body', 'br', 'button',
        'canvas', 'caption', 'cite', 'code', 'col', 'colgroup',
        'data', 'datalist', 'dd', 'del', 'details', 'dfn', 'dialog', 'div', 'dl', 'dt', 'em', 'embed',
        'fieldset', 'figcaption', 'figure', 'footer', 'form',
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'head', 'header', 'hr', 'html',
        'i', 'iframe', 'img', 'input', 'ins',
        'kbd',
        'label', 'legend', 'li', 'link',
        'main', 'map', 'mark', 'meta', 'meter',
        'nav', 'noscript',
        'object', 'ol', 'optgroup', 'option',
        'p', 'param', 'picture', 'polyline', 'polygon', 'pre', 'progress',
        'q',
        'rp', 'rt', 'ruby',
        's', 'samp', 'script', 'section', 'select', 'small', 'source', 'span', 'strong', 'style', 'sub', 'summary', 'sup', 'svg',
        'table', 'tbody', 'td', 'template', 'textarea', 'tfoot', 'th', 'thead', 'tr', 'track',
        'u', 'ul',
        'var', 'video',
        'wbr'
    ]

    // OTHER
    static MIME_TYPES = {'application/andrew-inset': ['ez'], 'application/applixware': ['aw'], 'application/atom+xml': ['atom'], 'application/atomcat+xml': ['atomcat'], 'application/atomsvc+xml': ['atomsvc'], 'application/ccxml+xml': ['ccxml'], 'application/cu-seeme': ['cu'], 'application/davmount+xml': ['davmount'], 'application/ecmascript': ['ecma'], 'application/emma+xml': ['emma'], 'application/epub+zip': ['epub'], 'application/font-tdpfr': ['pfr'], 'application/gzip': ['gz', 'tgz'], 'application/hyperstudio': ['stk'], 'application/java-archive': ['jar'], 'application/java-serialized-object': ['ser'], 'application/java-vm': ['class'], 'application/json': ['json'], 'application/lost+xml': ['lostxml'], 'application/mac-binhex40': ['hqx'], 'application/mac-compactpro': ['cpt'], 'application/marc': ['mrc'], 'application/mathematica': ['ma', 'mb', 'nb'], 'application/mathml+xml': ['mathml', 'mml'], 'application/mbox': ['mbox'], 'application/mediaservercontrol+xml': ['mscml'], 'application/mp4': ['mp4s'], 'application/msword': ['doc', 'dot', 'wiz'], 'application/mxf': ['mxf'], 'application/octet-stream': ['a', 'bin', 'bpk', 'deploy', 'dist', 'distz', 'dmg', 'dms', 'dump', 'elc', 'lha', 'lrf', 'lzh', 'o', 'obj', 'pkg', 'so'], 'application/oda': ['oda'], 'application/oebps-package+xml': ['opf'], 'application/ogg': ['ogx'], 'application/onenote': ['onepkg', 'onetmp', 'onetoc', 'onetoc2'], 'application/patch-ops-error+xml': ['xer'], 'application/pdf': ['pdf'], 'application/pgp-encrypted': ['pgp'], 'application/pgp-signature': ['asc', 'sig'], 'application/pics-rules': ['prf'], 'application/pkcs10': ['p10'], 'application/pkcs7-mime': ['p7c', 'p7m'], 'application/pkcs7-signature': ['p7s'], 'application/pkix-cert': ['cer'], 'application/pkix-crl': ['crl'], 'application/pkix-pkipath': ['pkipath'], 'application/pkixcmp': ['pki'], 'application/pls+xml': ['pls'], 'application/postscript': ['ai', 'eps', 'ps'], 'application/prql': ['prql'], 'application/prs.cww': ['cww'], 'application/rdf+xml': ['rdf'], 'application/reginfo+xml': ['rif'], 'application/relax-ng-compact-syntax': ['rnc'], 'application/resource-lists+xml': ['rl'], 'application/resource-lists-diff+xml': ['rld'], 'application/rls-services+xml': ['rs'], 'application/rsd+xml': ['rsd'], 'application/rss+xml': ['rss', 'xml'], 'application/rtf': ['rtf'], 'application/sbml+xml': ['sbml'], 'application/scvp-cv-request': ['scq'], 'application/scvp-cv-response': ['scs'], 'application/scvp-vp-request': ['spq'], 'application/scvp-vp-response': ['spp'], 'application/sdp': ['sdp'], 'application/set-payment-initiation': ['setpay'], 'application/set-registration-initiation': ['setreg'], 'application/shf+xml': ['shf'], 'application/smil+xml': ['smi', 'smil'], 'application/sparql-query': ['rq'], 'application/sparql-results+xml': ['srx'], 'application/srgs': ['gram'], 'application/srgs+xml': ['grxml'], 'application/ssml+xml': ['ssml'], 'application/vnd.3gpp.pic-bw-large': ['plb'], 'application/vnd.3gpp.pic-bw-small': ['psb'], 'application/vnd.3gpp.pic-bw-var': ['pvb'], 'application/vnd.3gpp2.tcap': ['tcap'], 'application/vnd.3m.post-it-notes': ['pwn'], 'application/vnd.accpac.simply.aso': ['aso'], 'application/vnd.accpac.simply.imp': ['imp'], 'application/vnd.acucobol': ['acu'], 'application/vnd.acucorp': ['acutc', 'atc'], 'application/vnd.adobe.air-application-installer-package+zip': ['air'], 'application/vnd.adobe.xdp+xml': ['xdp'], 'application/vnd.adobe.xfdf': ['xfdf'], 'application/vnd.airzip.filesecure.azf': ['azf'], 'application/vnd.airzip.filesecure.azs': ['azs'], 'application/vnd.amazon.ebook': ['azw'], 'application/vnd.americandynamics.acc': ['acc'], 'application/vnd.amiga.ami': ['ami'], 'application/vnd.android.package-archive': ['apk'], 'application/vnd.anser-web-certificate-issue-initiation': ['cii'], 'application/vnd.anser-web-funds-transfer-initiation': ['fti'], 'application/vnd.antix.game-component': ['atx'], 'application/vnd.apple.installer+xml': ['mpkg'], 'application/vnd.arastra.swi': ['swi'], 'application/vnd.audiograph': ['aep'], 'application/vnd.blueice.multipass': ['mpm'], 'application/vnd.bmi': ['bmi'], 'application/vnd.businessobjects': ['rep'], 'application/vnd.chemdraw+xml': ['cdxml'], 'application/vnd.chipnuts.karaoke-mmd': ['mmd'], 'application/vnd.cinderella': ['cdy'], 'application/vnd.claymore': ['cla'], 'application/vnd.clonk.c4group': ['c4d', 'c4f', 'c4g', 'c4p', 'c4u'], 'application/vnd.commonspace': ['csp'], 'application/vnd.contact.cmsg': ['cdbcmsg'], 'application/vnd.cosmocaller': ['cmc'], 'application/vnd.crick.clicker': ['clkx'], 'application/vnd.crick.clicker.keyboard': ['clkk'], 'application/vnd.crick.clicker.palette': ['clkp'], 'application/vnd.crick.clicker.template': ['clkt'], 'application/vnd.crick.clicker.wordbank': ['clkw'], 'application/vnd.criticaltools.wbs+xml': ['wbs'], 'application/vnd.ctc-posml': ['pml'], 'application/vnd.cups-ppd': ['ppd'], 'application/vnd.curl.car': ['car'], 'application/vnd.curl.pcurl': ['pcurl'], 'application/vnd.data-vision.rdz': ['rdz'], 'application/vnd.debian.binary-package': ['deb', 'udeb'], 'application/vnd.denovo.fcselayout-link': ['fe_launch'], 'application/vnd.dna': ['dna'], 'application/vnd.dolby.mlp': ['mlp'], 'application/vnd.dpgraph': ['dpg'], 'application/vnd.dreamfactory': ['dfac'], 'application/vnd.dynageo': ['geo'], 'application/vnd.ecowin.chart': ['mag'], 'application/vnd.enliven': ['nml'], 'application/vnd.epson.esf': ['esf'], 'application/vnd.epson.msf': ['msf'], 'application/vnd.epson.quickanime': ['qam'], 'application/vnd.epson.salt': ['slt'], 'application/vnd.epson.ssf': ['ssf'], 'application/vnd.eszigno3+xml': ['es3', 'et3'], 'application/vnd.ezpix-album': ['ez2'], 'application/vnd.ezpix-package': ['ez3'], 'application/vnd.fdf': ['fdf'], 'application/vnd.fdsn.mseed': ['mseed'], 'application/vnd.fdsn.seed': ['dataless', 'seed'], 'application/vnd.flographit': ['gph'], 'application/vnd.fluxtime.clip': ['ftc'], 'application/vnd.framemaker': ['book', 'fm', 'frame', 'maker'], 'application/vnd.frogans.fnc': ['fnc'], 'application/vnd.frogans.ltf': ['ltf'], 'application/vnd.fsc.weblaunch': ['fsc'], 'application/vnd.fujitsu.oasys': ['oas'], 'application/vnd.fujitsu.oasys2': ['oa2'], 'application/vnd.fujitsu.oasys3': ['oa3'], 'application/vnd.fujitsu.oasysgp': ['fg5'], 'application/vnd.fujitsu.oasysprs': ['bh2'], 'application/vnd.fujixerox.ddd': ['ddd'], 'application/vnd.fujixerox.docuworks': ['xdw'], 'application/vnd.fujixerox.docuworks.binder': ['xbd'], 'application/vnd.fuzzysheet': ['fzs'], 'application/vnd.genomatix.tuxedo': ['txd'], 'application/vnd.geogebra.file': ['ggb'], 'application/vnd.geogebra.tool': ['ggt'], 'application/vnd.geometry-explorer': ['gex', 'gre'], 'application/vnd.gerber': ['gbr'], 'application/vnd.gmx': ['gmx'], 'application/vnd.google-earth.kml+xml': ['kml'], 'application/vnd.google-earth.kmz': ['kmz'], 'application/vnd.grafeq': ['gqf', 'gqs'], 'application/vnd.groove-account': ['gac'], 'application/vnd.groove-help': ['ghf'], 'application/vnd.groove-identity-message': ['gim'], 'application/vnd.groove-injector': ['grv'], 'application/vnd.groove-tool-message': ['gtm'], 'application/vnd.groove-tool-template': ['tpl'], 'application/vnd.groove-vcard': ['vcg'], 'application/vnd.handheld-entertainment+xml': ['zmm'], 'application/vnd.hbci': ['hbci'], 'application/vnd.hhe.lesson-player': ['les'], 'application/vnd.hp-hpgl': ['hpgl'], 'application/vnd.hp-hpid': ['hpid'], 'application/vnd.hp-hps': ['hps'], 'application/vnd.hp-jlyt': ['jlt'], 'application/vnd.hp-pcl': ['pcl'], 'application/vnd.hp-pclxl': ['pclxl'], 'application/vnd.hydrostatix.sof-data': ['sfd-hdstx'], 'application/vnd.hzn-3d-crossword': ['x3d'], 'application/vnd.ibm.minipay': ['mpy'], 'application/vnd.ibm.modcap': ['afp', 'list3820', 'listafp'], 'application/vnd.ibm.rights-management': ['irm'], 'application/vnd.ibm.secure-container': ['sc'], 'application/vnd.iccprofile': ['icc', 'icm'], 'application/vnd.igloader': ['igl'], 'application/vnd.immervision-ivp': ['ivp'], 'application/vnd.immervision-ivu': ['ivu'], 'application/vnd.intercon.formnet': ['xpw', 'xpx'], 'application/vnd.intu.qbo': ['qbo'], 'application/vnd.intu.qfx': ['qfx'], 'application/vnd.ipunplugged.rcprofile': ['rcprofile'], 'application/vnd.irepository.package+xml': ['irp'], 'application/vnd.is-xpr': ['xpr'], 'application/vnd.jam': ['jam'], 'application/vnd.jcp.javame.midlet-rms': ['rms'], 'application/vnd.jisp': ['jisp'], 'application/vnd.joost.joda-archive': ['joda'], 'application/vnd.kahootz': ['ktr', 'ktz'], 'application/vnd.kde.karbon': ['karbon'], 'application/vnd.kde.kchart': ['chrt'], 'application/vnd.kde.kformula': ['kfo'], 'application/vnd.kde.kivio': ['flw'], 'application/vnd.kde.kontour': ['kon'], 'application/vnd.kde.kpresenter': ['kpr', 'kpt'], 'application/vnd.kde.kspread': ['ksp'], 'application/vnd.kde.kword': ['kwd', 'kwt'], 'application/vnd.kenameaapp': ['htke'], 'application/vnd.kidspiration': ['kia'], 'application/vnd.kinar': ['kne', 'knp'], 'application/vnd.koan': ['skd', 'skm', 'skp', 'skt'], 'application/vnd.kodak-descriptor': ['sse'], 'application/vnd.llamagraphics.life-balance.desktop': ['lbd'], 'application/vnd.llamagraphics.life-balance.exchange+xml': ['lbe'], 'application/vnd.lotus-1-2-3': ['123'], 'application/vnd.lotus-approach': ['apr'], 'application/vnd.lotus-freelance': ['pre'], 'application/vnd.lotus-notes': ['nsf'], 'application/vnd.lotus-organizer': ['org'], 'application/vnd.lotus-screencam': ['scm'], 'application/vnd.lotus-wordpro': ['lwp'], 'application/vnd.macports.portpkg': ['portpkg'], 'application/vnd.mcd': ['mcd'], 'application/vnd.medcalcdata': ['mc1'], 'application/vnd.mediastation.cdkey': ['cdkey'], 'application/vnd.mfer': ['mwf'], 'application/vnd.mfmp': ['mfm'], 'application/vnd.micrografx.flo': ['flo'], 'application/vnd.micrografx.igx': ['igx'], 'application/vnd.mif': ['mif'], 'application/vnd.mobius.daf': ['daf'], 'application/vnd.mobius.dis': ['dis'], 'application/vnd.mobius.mbk': ['mbk'], 'application/vnd.mobius.mqy': ['mqy'], 'application/vnd.mobius.msl': ['msl'], 'application/vnd.mobius.plc': ['plc'], 'application/vnd.mobius.txf': ['txf'], 'application/vnd.mophun.application': ['mpn'], 'application/vnd.mophun.certificate': ['mpc'], 'application/vnd.mozilla.xul+xml': ['xul'], 'application/vnd.ms-artgalry': ['cil'], 'application/vnd.ms-cab-compressed': ['cab'], 'application/vnd.ms-excel': ['xla', 'xlb', 'xlc', 'xlm', 'xls', 'xlt', 'xlw'], 'application/vnd.ms-excel.addin.macroenabled.12': ['xlam'], 'application/vnd.ms-excel.sheet.binary.macroenabled.12': ['xlsb'], 'application/vnd.ms-excel.sheet.macroenabled.12': ['xlsm'], 'application/vnd.ms-excel.template.macroenabled.12': ['xltm'], 'application/vnd.ms-fontobject': ['eot'], 'application/vnd.ms-htmlhelp': ['chm'], 'application/vnd.ms-ims': ['ims'], 'application/vnd.ms-lrm': ['lrm'], 'application/vnd.ms-pki.seccat': ['cat'], 'application/vnd.ms-pki.stl': ['stl'], 'application/vnd.ms-powerpoint': ['pot', 'ppa', 'pps', 'ppt', 'pwz'], 'application/vnd.ms-powerpoint.addin.macroenabled.12': ['ppam'], 'application/vnd.ms-powerpoint.presentation.macroenabled.12': ['pptm'], 'application/vnd.ms-powerpoint.slide.macroenabled.12': ['sldm'], 'application/vnd.ms-powerpoint.slideshow.macroenabled.12': ['ppsm'], 'application/vnd.ms-powerpoint.template.macroenabled.12': ['potm'], 'application/vnd.ms-project': ['mpp', 'mpt'], 'application/vnd.ms-word.document.macroenabled.12': ['docm'], 'application/vnd.ms-word.template.macroenabled.12': ['dotm'], 'application/vnd.ms-works': ['wcm', 'wdb', 'wks', 'wps'], 'application/vnd.ms-wpl': ['wpl'], 'application/vnd.ms-xpsdocument': ['xps'], 'application/vnd.mseq': ['mseq'], 'application/vnd.musician': ['mus'], 'application/vnd.muvee.style': ['msty'], 'application/vnd.neurolanguage.nlu': ['nlu'], 'application/vnd.noblenet-directory': ['nnd'], 'application/vnd.noblenet-sealer': ['nns'], 'application/vnd.noblenet-web': ['nnw'], 'application/vnd.nokia.n-gage.data': ['ngdat'], 'application/vnd.nokia.n-gage.symbian.install': ['n-gage'], 'application/vnd.nokia.radio-preset': ['rpst'], 'application/vnd.nokia.radio-presets': ['rpss'], 'application/vnd.novadigm.edm': ['edm'], 'application/vnd.novadigm.edx': ['edx'], 'application/vnd.novadigm.ext': ['ext'], 'application/vnd.oasis.opendocument.chart': ['odc'], 'application/vnd.oasis.opendocument.chart-template': ['otc'], 'application/vnd.oasis.opendocument.database': ['odb'], 'application/vnd.oasis.opendocument.formula': ['odf'], 'application/vnd.oasis.opendocument.formula-template': ['odft'], 'application/vnd.oasis.opendocument.graphics': ['odg'], 'application/vnd.oasis.opendocument.graphics-template': ['otg'], 'application/vnd.oasis.opendocument.image': ['odi'], 'application/vnd.oasis.opendocument.image-template': ['oti'], 'application/vnd.oasis.opendocument.presentation': ['odp'], 'application/vnd.oasis.opendocument.presentation-template': ['otp'], 'application/vnd.oasis.opendocument.spreadsheet': ['ods'], 'application/vnd.oasis.opendocument.spreadsheet-template': ['ots'], 'application/vnd.oasis.opendocument.text': ['odt'], 'application/vnd.oasis.opendocument.text-master': ['otm'], 'application/vnd.oasis.opendocument.text-template': ['ott'], 'application/vnd.oasis.opendocument.text-web': ['oth'], 'application/vnd.olpc-sugar': ['xo'], 'application/vnd.oma.dd2+xml': ['dd2'], 'application/vnd.openofficeorg.extension': ['oxt'], 'application/vnd.openxmlformats-officedocument.presentationml.presentation': ['pptx'], 'application/vnd.openxmlformats-officedocument.presentationml.slide': ['sldx'], 'application/vnd.openxmlformats-officedocument.presentationml.slideshow': ['ppsx'], 'application/vnd.openxmlformats-officedocument.presentationml.template': ['potx'], 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': ['xlsx'], 'application/vnd.openxmlformats-officedocument.spreadsheetml.template': ['xltx'], 'application/vnd.openxmlformats-officedocument.wordprocessingml.document': ['docx'], 'application/vnd.openxmlformats-officedocument.wordprocessingml.template': ['dotx'], 'application/vnd.osgi.dp': ['dp'], 'application/vnd.palm': ['oprc', 'pdb', 'pqa'], 'application/vnd.pg.format': ['str'], 'application/vnd.pg.osasli': ['ei6'], 'application/vnd.picsel': ['efif'], 'application/vnd.pocketlearn': ['plf'], 'application/vnd.powerbuilder6': ['pbd'], 'application/vnd.previewsystems.box': ['box'], 'application/vnd.proteus.magazine': ['mgz'], 'application/vnd.publishare-delta-tree': ['qps'], 'application/vnd.pvi.ptid1': ['ptid'], 'application/vnd.quark.quarkxpress': ['qwd', 'qwt', 'qxb', 'qxd', 'qxl', 'qxt'], 'application/vnd.rar': ['rar'], 'application/vnd.recordare.musicxml': ['mxl'], 'application/vnd.recordare.musicxml+xml': ['musicxml'], 'application/vnd.rim.cod': ['cod'], 'application/vnd.rn-realmedia': ['rm'], 'application/vnd.route66.link66+xml': ['link66'], 'application/vnd.seemail': ['see'], 'application/vnd.sema': ['sema'], 'application/vnd.semd': ['semd'], 'application/vnd.semf': ['semf'], 'application/vnd.shana.informed.formdata': ['ifm'], 'application/vnd.shana.informed.formtemplate': ['itp'], 'application/vnd.shana.informed.interchange': ['iif'], 'application/vnd.shana.informed.package': ['ipk'], 'application/vnd.simtech-mindmapper': ['twd', 'twds'], 'application/vnd.smaf': ['mmf'], 'application/vnd.smart.teacher': ['teacher'], 'application/vnd.solent.sdkm+xml': ['sdkd', 'sdkm'], 'application/vnd.spotfire.dxp': ['dxp'], 'application/vnd.spotfire.sfs': ['sfs'], 'application/vnd.sqlite3': ['db', 'sqlite', 'sqlite3', 'db-wal', 'sqlite-wal', 'db-shm', 'sqlite-shm'], 'application/vnd.stardivision.calc': ['sdc'], 'application/vnd.stardivision.draw': ['sda'], 'application/vnd.stardivision.impress': ['sdd'], 'application/vnd.stardivision.math': ['smf'], 'application/vnd.stardivision.writer': ['sdw', 'vor'], 'application/vnd.stardivision.writer-global': ['sgl'], 'application/vnd.sun.xml.calc': ['sxc'], 'application/vnd.sun.xml.calc.template': ['stc'], 'application/vnd.sun.xml.draw': ['sxd'], 'application/vnd.sun.xml.draw.template': ['std'], 'application/vnd.sun.xml.impress': ['sxi'], 'application/vnd.sun.xml.impress.template': ['sti'], 'application/vnd.sun.xml.math': ['sxm'], 'application/vnd.sun.xml.writer': ['sxw'], 'application/vnd.sun.xml.writer.global': ['sxg'], 'application/vnd.sun.xml.writer.template': ['stw'], 'application/vnd.sus-calendar': ['sus', 'susp'], 'application/vnd.svd': ['svd'], 'application/vnd.symbian.install': ['sis', 'sisx'], 'application/vnd.syncml+xml': ['xsm'], 'application/vnd.syncml.dm+wbxml': ['bdm'], 'application/vnd.syncml.dm+xml': ['xdm'], 'application/vnd.tao.intent-module-archive': ['tao'], 'application/vnd.tmobile-livetv': ['tmo'], 'application/vnd.trid.tpt': ['tpt'], 'application/vnd.triscape.mxs': ['mxs'], 'application/vnd.trueapp': ['tra'], 'application/vnd.ufdl': ['ufd', 'ufdl'], 'application/vnd.uiq.theme': ['utz'], 'application/vnd.umajin': ['umj'], 'application/vnd.unity': ['unityweb'], 'application/vnd.uoml+xml': ['uoml'], 'application/vnd.vcx': ['vcx'], 'application/vnd.visio': ['vsd', 'vss', 'vst', 'vsw', 'vsdx', 'vssx', 'vstx', 'vssm', 'vstm'], 'application/vnd.visionary': ['vis'], 'application/vnd.vsf': ['vsf'], 'application/vnd.wap.sic': ['sic'], 'application/vnd.wap.slc': ['slc'], 'application/vnd.wap.wbxml': ['wbxml'], 'application/vnd.wap.wmlc': ['wmlc'], 'application/vnd.wap.wmlscriptc': ['wmlsc'], 'application/vnd.webturbo': ['wtb'], 'application/vnd.wordperfect': ['wpd'], 'application/vnd.wqd': ['wqd'], 'application/vnd.wt.stf': ['stf'], 'application/vnd.xara': ['xar'], 'application/vnd.xfdl': ['xfdl'], 'application/vnd.yamaha.hv-dic': ['hvd'], 'application/vnd.yamaha.hv-script': ['hvs'], 'application/vnd.yamaha.hv-voice': ['hvp'], 'application/vnd.yamaha.openscoreformat': ['osf'], 'application/vnd.yamaha.openscoreformat.osfpvg+xml': ['osfpvg'], 'application/vnd.yamaha.smaf-audio': ['saf'], 'application/vnd.yamaha.smaf-phrase': ['spf'], 'application/vnd.yellowriver-custom-menu': ['cmp'], 'application/vnd.zul': ['zir', 'zirz'], 'application/vnd.zzazz.deck+xml': ['zaz'], 'application/voicexml+xml': ['vxml'], 'application/wasm': ['wasm'], 'application/winhlp': ['hlp'], 'application/wsdl+xml': ['wsdl'], 'application/wspolicy+xml': ['wspolicy'], 'application/x-7z-compressed': ['7z'], 'application/x-abiword': ['abw', 'zabw', 'abw.gz'], 'application/x-ace-compressed': ['ace'], 'application/x-authorware-bin': ['aab', 'u32', 'vox', 'x32'], 'application/x-authorware-map': ['aam'], 'application/x-authorware-seg': ['aas'], 'application/x-bcpio': ['bcpio'], 'application/x-bittorrent': ['torrent'], 'application/x-bzip': ['bz'], 'application/x-bzip2': ['boz', 'bz2'], 'application/x-cdlink': ['vcd'], 'application/x-chat': ['chat'], 'application/x-chess-pgn': ['pgn'], 'application/x-cpio': ['cpio'], 'application/x-csh': ['csh'], 'application/x-debian-package': ['deb', 'udeb'], 'application/x-director': ['cct', 'cst', 'cxt', 'dcr', 'dir', 'dxr', 'fgd', 'swa', 'w3d'], 'application/x-doom': ['wad'], 'application/x-dtbncx+xml': ['ncx'], 'application/x-dtbook+xml': ['dtb'], 'application/x-dtbresource+xml': ['res'], 'application/x-dvi': ['dvi'], 'application/x-font-bdf': ['bdf'], 'application/x-font-ghostscript': ['gsf'], 'application/x-font-linux-psf': ['psf'], 'application/x-font-otf': ['otf'], 'application/x-font-pcf': ['pcf'], 'application/x-font-snf': ['snf'], 'application/x-font-ttf': ['ttc', 'ttf'], 'application/x-font-type1': ['afm', 'pfa', 'pfb', 'pfm'], 'application/x-futuresplash': ['spl'], 'application/x-gnumeric': ['gnumeric'], 'application/x-gtar': ['gtar'], 'application/x-gzip': ['gz', 'tgz'], 'application/x-hdf': ['hdf'], 'application/x-iso9660-image': ['iso', 'isoimg', 'cdr'], 'application/x-java-jnlp-file': ['jnlp'], 'application/x-killustrator': ['kil'], 'application/x-krita': ['kra', 'krz'], 'application/x-latex': ['latex'], 'application/x-mobipocket-ebook': ['mobi', 'prc'], 'application/x-ms-application': ['application'], 'application/x-ms-wmd': ['wmd'], 'application/x-ms-wmz': ['wmz'], 'application/x-ms-xbap': ['xbap'], 'application/x-msaccess': ['mdb'], 'application/x-msbinder': ['obd'], 'application/x-mscardfile': ['crd'], 'application/x-msclip': ['clp'], 'application/x-msdownload': ['bat', 'com', 'dll', 'exe', 'msi'], 'application/x-msmediaview': ['m13', 'm14', 'mvb'], 'application/x-msmetafile': ['wmf'], 'application/x-msmoney': ['mny'], 'application/x-mspublisher': ['pub'], 'application/x-msschedule': ['scd'], 'application/x-msterminal': ['trm'], 'application/x-mswrite': ['wri'], 'application/x-netcdf': ['cdf', 'nc'], 'application/x-perl': ['pm', 'pl'], 'application/x-pkcs12': ['p12', 'pfx'], 'application/x-pkcs7-certificates': ['p7b', 'spc'], 'application/x-pkcs7-certreqresp': ['p7r'], 'application/x-python-code': ['pyc', 'pyo'], 'application/x-rar-compressed': ['rar'], 'application/x-redhat-package-manager': ['rpa'], 'application/x-rpm': ['rpm'], 'application/x-sh': ['sh'], 'application/x-shar': ['shar'], 'application/x-shellscript': ['sh'], 'application/x-shockwave-flash': ['swf'], 'application/x-silverlight-app': ['xap'], 'application/x-sqlite3': ['db', 'sqlite', 'sqlite3', 'db-wal', 'sqlite-wal', 'db-shm', 'sqlite-shm'], 'application/x-stuffit': ['sit'], 'application/x-stuffitx': ['sitx'], 'application/x-sv4cpio': ['sv4cpio'], 'application/x-sv4crc': ['sv4crc'], 'application/x-tar': ['tar'], 'application/x-tcl': ['tcl'], 'application/x-tex': ['tex'], 'application/x-tex-tfm': ['tfm'], 'application/x-texinfo': ['texi', 'texinfo'], 'application/x-ustar': ['ustar'], 'application/x-wais-source': ['src'], 'application/x-x509-ca-cert': ['crt', 'der'], 'application/x-xfig': ['fig'], 'application/x-xpinstall': ['xpi'], 'application/x-zip-compressed': ['zip'], 'application/xenc+xml': ['xenc'], 'application/xhtml+xml': ['xht', 'xhtml'], 'application/xml': ['xml', 'xpdl', 'xsl'], 'application/xml-dtd': ['dtd'], 'application/xop+xml': ['xop'], 'application/xslt+xml': ['xslt'], 'application/xspf+xml': ['xspf'], 'application/xv+xml': ['mxml', 'xhvml', 'xvm', 'xvml'], 'application/yaml': ['yaml', 'yml'], 'application/zip': ['zip'], 'application/zip-compressed': ['zip'], 'audio/3gpp2': ['3g2'], 'audio/aac': ['aac', 'm4a'], 'audio/aacp': ['aacp'], 'audio/adpcm': ['adp'], 'audio/aiff': ['aiff', 'aif', 'aff'], 'audio/basic': ['au', 'snd'], 'audio/flac': ['flac'], 'audio/midi': ['kar', 'mid', 'midi', 'rmi'], 'audio/mp4': ['mp4', 'm4a', 'm4b', 'm4p', 'm4r', 'm4v', 'mp4v', '3gp', '3g2', '3ga', '3gpa', '3gpp', '3gpp2', '3gp2'], 'audio/mpeg': ['m2a', 'm3a', 'mp2', 'mp2a', 'mp3', 'mpga'], 'audio/ogg': ['oga', 'ogg', 'spx'], 'audio/opus': ['opus'], 'audio/vnd.digital-winds': ['eol'], 'audio/vnd.dts': ['dts'], 'audio/vnd.dts.hd': ['dtshd'], 'audio/vnd.lucent.voice': ['lvp'], 'audio/vnd.ms-playready.media.pya': ['pya'], 'audio/vnd.nuera.ecelp4800': ['ecelp4800'], 'audio/vnd.nuera.ecelp7470': ['ecelp7470'], 'audio/vnd.nuera.ecelp9600': ['ecelp9600'], 'audio/vnd.wav': ['wav'], 'audio/webm': ['weba'], 'audio/x-matroska': ['mka'], 'audio/x-mpegurl': ['m3u'], 'audio/x-ms-wax': ['wax'], 'audio/x-ms-wma': ['wma'], 'audio/x-pn-realaudio': ['ra', 'ram'], 'audio/x-pn-realaudio-plugin': ['rmp'], 'chemical/x-cdx': ['cdx'], 'chemical/x-cif': ['cif'], 'chemical/x-cmdf': ['cmdf'], 'chemical/x-cml': ['cml'], 'chemical/x-csml': ['csml'], 'chemical/x-xyz': ['xyz'], 'font/otf': ['otf'], 'font/woff': ['woff'], 'font/woff2': ['woff2'], 'gcode': ['gcode'], 'image/avif': ['avif', 'avifs'], 'image/bmp': ['bmp'], 'image/cgm': ['cgm'], 'image/g3fax': ['g3'], 'image/gif': ['gif'], 'image/heic': ['heif', 'heic'], 'image/ief': ['ief'], 'image/jpeg': ['jpe', 'jpeg', 'jpg', 'pjpg', 'jfif', 'jfif-tbnl', 'jif'], 'image/pjpeg': ['jpe', 'jpeg', 'jpg', 'pjpg', 'jfi', 'jfif', 'jfif-tbnl', 'jif'], 'image/png': ['png'], 'image/prs.btif': ['btif'], 'image/svg+xml': ['svg', 'svgz'], 'image/tiff': ['tif', 'tiff'], 'image/vnd.adobe.photoshop': ['psd'], 'image/vnd.djvu': ['djv', 'djvu'], 'image/vnd.dwg': ['dwg'], 'image/vnd.dxf': ['dxf'], 'image/vnd.fastbidsheet': ['fbs'], 'image/vnd.fpx': ['fpx'], 'image/vnd.fst': ['fst'], 'image/vnd.fujixerox.edmics-mmr': ['mmr'], 'image/vnd.fujixerox.edmics-rlc': ['rlc'], 'image/vnd.ms-modi': ['mdi'], 'image/vnd.net-fpx': ['npx'], 'image/vnd.wap.wbmp': ['wbmp'], 'image/vnd.xiff': ['xif'], 'image/webp': ['webp'], 'image/x-adobe-dng': ['dng'], 'image/x-canon-cr2': ['cr2'], 'image/x-canon-crw': ['crw'], 'image/x-cmu-raster': ['ras'], 'image/x-cmx': ['cmx'], 'image/x-epson-erf': ['erf'], 'image/x-freehand': ['fh', 'fh4', 'fh5', 'fh7', 'fhc'], 'image/x-fuji-raf': ['raf'], 'image/x-icns': ['icns'], 'image/x-icon': ['ico'], 'image/x-kodak-dcr': ['dcr'], 'image/x-kodak-k25': ['k25'], 'image/x-kodak-kdc': ['kdc'], 'image/x-minolta-mrw': ['mrw'], 'image/x-nikon-nef': ['nef'], 'image/x-olympus-orf': ['orf'], 'image/x-panasonic-raw': ['raw', 'rw2', 'rwl'], 'image/x-pcx': ['pcx'], 'image/x-pentax-pef': ['pef', 'ptx'], 'image/x-pict': ['pct', 'pic'], 'image/x-portable-anymap': ['pnm'], 'image/x-portable-bitmap': ['pbm'], 'image/x-portable-graymap': ['pgm'], 'image/x-portable-pixmap': ['ppm'], 'image/x-rgb': ['rgb'], 'image/x-sigma-x3f': ['x3f'], 'image/x-sony-arw': ['arw'], 'image/x-sony-sr2': ['sr2'], 'image/x-sony-srf': ['srf'], 'image/x-xbitmap': ['xbm'], 'image/x-xpixmap': ['xpm'], 'image/x-xwindowdump': ['xwd'], 'message/rfc822': ['eml', 'mht', 'mhtml', 'mime', 'nws'], 'model/iges': ['iges', 'igs'], 'model/mesh': ['mesh', 'msh', 'silo'], 'model/vnd.dwf': ['dwf'], 'model/vnd.gdl': ['gdl'], 'model/vnd.gtw': ['gtw'], 'model/vnd.mts': ['mts'], 'model/vnd.vtu': ['vtu'], 'model/vrml': ['vrml', 'wrl'], 'test/mimetype': ['test'], 'text/calendar': ['ics', 'ifb'], 'text/css': ['css'], 'text/csv': ['csv'], 'text/html': ['htm', 'html'], 'text/javascript': ['js'], 'text/markdown': ['md', 'markdown', 'mdown', 'markdn'], 'text/mathml': ['mathml', 'mml'], 'text/plain': ['conf', 'def', 'diff', 'in', 'ksh', 'list', 'log', 'pl', 'text', 'txt'], 'text/prs.lines.tag': ['dsc'], 'text/richtext': ['rtx'], 'text/sgml': ['sgm', 'sgml'], 'text/tab-separated-values': ['tsv'], 'text/troff': ['man', 'me', 'ms', 'roff', 't', 'tr'], 'text/uri-list': ['uri', 'uris', 'urls'], 'text/vnd.curl': ['curl'], 'text/vnd.curl.dcurl': ['dcurl'], 'text/vnd.curl.mcurl': ['mcurl'], 'text/vnd.curl.scurl': ['scurl'], 'text/vnd.fly': ['fly'], 'text/vnd.fmi.flexstor': ['flx'], 'text/vnd.graphviz': ['gv'], 'text/vnd.in3d.3dml': ['3dml'], 'text/vnd.in3d.spot': ['spot'], 'text/vnd.sun.j2me.app-descriptor': ['jad'], 'text/vnd.wap.si': ['si'], 'text/vnd.wap.sl': ['sl'], 'text/vnd.wap.wml': ['wml'], 'text/vnd.wap.wmlscript': ['wmls'], 'text/x-asm': ['asm', 's'], 'text/x-c': ['c', 'cc', 'cpp', 'cxx', 'dic', 'h', 'hh'], 'text/x-fortran': ['f', 'f77', 'f90', 'for'], 'text/x-java-source': ['java'], 'text/x-pascal': ['p', 'pas', 'pp', 'inc'], 'text/x-python': ['py'], 'text/x-setext': ['etx'], 'text/x-uuencode': ['uu'], 'text/x-vcalendar': ['vcs'], 'text/x-vcard': ['vcf'], 'video/3gpp': ['3gp'], 'video/3gpp2': ['3g2'], 'video/h261': ['h261'], 'video/h263': ['h263'], 'video/h264': ['h264'], 'video/jpeg': ['jpgv'], 'video/jpm': ['jpgm', 'jpm'], 'video/mj2': ['mj2', 'mjp2'], 'video/mp2t': ['ts'], 'video/mp4': ['mp4', 'mp4v', 'mpg4'], 'video/mpeg': ['m1v', 'm2v', 'mpa', 'mpe', 'mpeg', 'mpg'], 'video/ogg': ['ogv'], 'video/quicktime': ['mov', 'qt'], 'video/vnd.fvt': ['fvt'], 'video/vnd.mpegurl': ['m4u', 'mxu'], 'video/vnd.ms-playready.media.pyv': ['pyv'], 'video/vnd.vivo': ['viv'], 'video/webm': ['webm'], 'video/x-f4v': ['f4v'], 'video/x-fli': ['fli'], 'video/x-flv': ['flv'], 'video/x-m4v': ['m4v'], 'video/x-matroska': ['mkv'], 'video/x-ms-asf': ['asf', 'asx'], 'video/x-ms-wm': ['wm'], 'video/x-ms-wmv': ['wmv'], 'video/x-ms-wmx': ['wmx'], 'video/x-ms-wvx': ['wvx'], 'video/x-msvideo': ['avi'], 'video/x-sgi-movie': ['movie'], 'x-conference/x-cooltalk': ['ice']}

    /**
     * COORDINATES
     * cartesian   = (x, y, z)
     * cylindrical = (r, azimuth, height)
     * geographic  = (latitude, longitude, altitude)
     * polar       = (r, theta)
     * spherical   = (r, theta, phi)
     */

    /** @param {any} value @param {string} types @returns {boolean} */
    static istype(value, types) {
        function istype(value, type) {
            function toBinary(value, type) {
                if (new RegExp("^(0|1)+$").test(value)) {
                    return value
                }
                else if (type.startswith('address-ipv4') || type.startswith('address-internet_protocol_v4')) {
                    return util.address_ipv4(value)
                }
                else if (type.startswith('address-ipv6') || type.startswith('address-internet_protocol_v6')) {
                    return util.address_ipv6(value)
                }
                else if (type.startswith('address-mac') || type.startswith('address-media_access_control')) {
                    return util.address_mac(value)
                }
            }
            if (type == 'address') {
                return istype(value, 'address-ipv4') || istype(value, 'address-ipv6') || istype(value, 'address-mac')
            }
            if (type == 'address-ip' || type == 'address-internet_protocol') {
                return istype(value, 'address-ipv4') || istype(value, 'address-ipv6')
            }
            if (type == 'address-ip-local' || type == 'address-internet_protocol-local') {
                return istype(value, 'address-ipv4-local') || istype(value, 'address-ipv6-local')
            }
            if (type == 'address-ip-local-link' || type == 'address-internet_protocol-local-link') {
                return istype(value, 'address-ipv4-local-link') || istype(value, 'address-ipv6-local-link')
            }
            if (type == 'address-ip-local-unique' || type == 'address-internet_protocol-local-unique') {
                return istype(value, 'address-ipv4-local-unique') || istype(value, 'address-ipv6-local-unique')
            }
            if (type == 'address-ip-loopback' || type == 'address-internet_protocol-loopback') {
                return istype(value, 'address-ipv4-loopback') || istype(value, 'address-ipv6-loopback')
            }
            if (type == 'address-ip-multicast' || type == 'address-internet_protocol-multicast') {
                return istype(value, 'address-ipv4-multicast') || istype(value, 'address-ipv6-multicast')
            }
            if (type == 'address-ip-unspecified' || type == 'address-internet_protocol-unspecified') {
                return istype(value, 'address-ipv4-unspecified') || istype(value, 'address-ipv6-unspecified')
            }
            if (type == 'address-ipv4' || type == 'address-internet_protocol_v4') {
                if (istype(value, 'string')) {
                    if (istype(value, 'binary')) {
                        return value.length == 32
                    } else {
                        let strings = value.split('.')
                        if (strings.length == 4) {
                            for (let string of strings) {
                                if (string.length < 0 || string.length > 3) return false
                                if (!istype(string, 'string-number')) return false
                                if (Number(string) < 0 || Number(string) > 255) return false
                            }
                            return true
                        }
                    }
                }
            }
            if (type == 'address-ipv4-benchmarking' || type == 'address-internet_protocol_v4-benchmarking') {
                if (istype(value, 'address-ipv4')) {
                    value = toBinary(value, type)
                    return value.slice(0, 15) == '110001100001001'
                }
            }
            if (type == 'address-ipv4-broadcast' || type == 'address-internet_protocol_v4-broadcast') {
                if (istype(value, 'address-ipv4')) {
                    value = toBinary(value, type)
                    return value == '11111111111111111111111111111111'
                }
            }
            if (type == 'address-ipv4-dummy' || type == 'address-internet_protocol_v4-dummy') {
                if (istype(value, 'address-ipv4')) {
                    value = toBinary(value, type)
                    return value == '11000000000000000000000000001000'
                }
            }
            if (type == 'address-ipv4-local' || type == 'address-internet_protocol_v4-local') {
                return istype(value, 'address-ipv4-local-link') || istype(value, 'address-ipv4-local-unique')
            }
            if (type == 'address-ipv4-local-link' || type == 'address-internet_protocol_v4-local-link') {
                if (istype(value, 'address-ipv4')) {
                    value = toBinary(value, type)
                    return value.slice(0, 16) == '1010100111111110'
                }
            }
            if (type == 'address-ipv4-local-unique' || type == 'address-internet_protocol_v4-local-unique') {
                if (istype(value, 'address-ipv4')) {
                    value = toBinary(value, type)
                    return value.slice(0, 8) == '10100000' | value.slice(0, 12) == '101011000001' || value.slice(0, 16) == '1100000010101000'
                }
            }
            if (type == 'address-ipv4-loopback' || type == 'address-internet_protocol_v4-loopback') {
                if (istype(value, 'address-ipv4')) {
                    value = toBinary(value, type)
                    return value.slice(0, 8) == '01111111'
                }
            }
            if (type == 'address-ipv4-mask' || type == 'address-internet_protocol_v4-mask') {
                return istype(value, 'address-ipv4-netmask') || istype(value, 'address-ipv4-subnetmask') || istype(value, 'address-ipv4-wildcardmask')
            }
            if (type == 'address-ipv4-multicast' || type == 'address-internet_protocol_v4-multicast') {
                if (istype(value, 'address-ipv4')) {
                    value = toBinary(value, type)
                    return value.slice(0, 4) == '1110'
                }
            }
            if (type == 'address-ipv4-netmask' || type == 'address-internet_protocol_v4-netmask') {
                if (istype(value, 'address-ipv4')) {
                    value = toBinary(value, type)
                    if (value.includes('0')) {
                        return value.indexOf('0') > value.lastIndexOf('1')
                    } else {
                        return value == '11111111111111111111111111111111'
                    }
                }
            }
            if (type == 'address-ipv4-networkmask' || type == 'address-internet_protocol_v4-networkmask') {
                if (istype(value, 'address-ipv4')) {
                    value = toBinary(value, type)
                    if (value.includes('0')) {
                        return value.indexOf('0') > value.lastIndexOf('1')
                    } else {
                        return value == '11111111111111111111111111111111'
                    }
                }
            }
            if (type == 'address-ipv4-subnetmask' || type == 'address-internet_protocol_v4-subnetmask') {
                if (istype(value, 'address-ipv4')) {
                    value = toBinary(value, type)
                    if (value.includes('0')) {
                        return value.indexOf('0') > value.lastIndexOf('1')
                    } else {
                        return value == '11111111111111111111111111111111'
                    }
                }
            }
            if (type == 'address-ipv4-subnetworkmask' || type == 'address-internet_protocol_v4-subnetworkmask') {
                if (istype(value, 'address-ipv4')) {
                    value = toBinary(value, type)
                    if (value.includes('0')) {
                        return value.indexOf('0') > value.lastIndexOf('1')
                    } else {
                        return value == '11111111111111111111111111111111'
                    }
                }
            }
            if (type == 'address-ipv4-unicast' || type == 'address-internet_protocol_v4-unicast') {
                if (istype(value, 'address-ipv4')) {
                    return !(istype(value, 'address-ipv4-broadcast') || istype(value, 'address-ipv4-dummy') || istype(value, 'address-ipv4-mask') || istype(value, 'address-ipv4-multicast') || istype(value, 'address-ipv4-unspecified'))
                }
            }
            if (type == 'address-ipv4-unspecified' || type == 'address-internet_protocol_v4-unspecified') {
                if (istype(value, 'address-ipv4')) {
                    value = toBinary(value, type)
                    return value == '00000000000000000000000000000000'
                }
            }
            if (type == 'address-ipv4-wildcardmask' || type == 'address-internet_protocol_v4-wildcardmask') {
                if (istype(value, 'address-ipv4')) {
                    value = toBinary(value, type)
                    if (value.includes('1')) {
                        return value.indexOf('1') > value.lastIndexOf('0')
                    } else {
                        return value == '00000000000000000000000000000000'
                    }
                }
            }
            if (type == 'address-ipv6' || type == 'address-internet_protocol_v6') {
                if (istype(value, 'string')) {
                    if (istype(value, 'binary')) {
                        return value.length == 128
                    } else {
                        let strings = value.split(':')
                        if (strings.length == 8) {
                            for (let string of strings) {
                                if (string.length < 0 || string.length > 4) return false
                                if (!istype(string, 'hexadecimal')) return false
                            }
                            return true
                        } else if (value.includes('::')) {
                            return new RegExp("^(:|[0-9]|[A-F]|[a-f])+$").test(value) && value.length <= 39
                        }
                    }
                }
            }
            if (type == 'address-ipv6-4to6' || type == 'address-internet_protocol_v6-4to6') {
                if (istype(value, 'address-ipv6')) {
                    value = toBinary(value, type)
                    return value.slice(0, 96) == '000000000000000000000000000000000000000000000000000000000000000000000000000000001111111111111111'
                }
            }
            if (type == 'address-ipv6-ipv4-mapped' || type == 'address-internet_protocol_v6-internet_protocol_v4-mapped') {
                if (istype(value, 'address-ipv6')) {
                    value = toBinary(value, type)
                    return value.slice(0, 96) == '000000000000000000000000000000000000000000000000000000000000000000000000000000001111111111111111'
                }
            }
            if (type == 'address-ipv6-6to4' || type == 'address-internet_protocol_v6-6to4') {
                if (istype(value, 'address-ipv6')) {
                    value = toBinary(value, type)
                    return value.slice(0, 16) == '0010000000000010'
                }
            }
            if (type == 'address-ipv6-anycast' || type == 'address-internet_protocol_v6-anycast') {
                return istype(value, 'address-ipv6-global')
            }
            if (type == 'address-ipv6-benchmarking' || type == 'address-internet_protocol_v6-benchmarking') {
                if (istype(value, 'address-ipv6')) {
                    value = toBinary(value, type)
                    return value.slice(0, 48) == '001000000000000100000000000000100000000000000000'
                }
            }
            if (type == 'address-ipv6-documentation' || type == 'address-internet_protocol_v6-documentation') {
                if (istype(value, 'address-ipv6')) {
                    value = toBinary(value, type)
                    return value.slice(0, 32) == '00100000000000010000110110111000'
                }
            }
            if (type == 'address-ipv6-global' || type == 'address-internet_protocol_v6-global') {
                if (istype(value, 'address-ipv6')) {
                    value = toBinary(value, type)
                    return value.slice(0, 3) == '001'
                }
            }
            if (type == 'address-ipv6-local' || type == 'address-internet_protocol_v6-local') {
                return istype(value, 'address-ipv6-local-link') || istype(value, 'address-ipv6-local-unique')
            }
            if (type == 'address-ipv6-local-link' || type == 'address-internet_protocol_v6-local-link') {
                if (istype(value, 'address-ipv6')) {
                    value = toBinary(value, type)
                    return value.slice(0, 10) == '1111111010'
                }
            }
            if (type == 'address-ipv6-local-unique' || type == 'address-internet_protocol_v6-local-unique') {
                if (istype(value, 'address-ipv6')) {
                    value = toBinary(value, type)
                    return value.slice(0, 7) == '1111110'
                }
            }
            if (type == 'address-ipv6-loopback' || type == 'address-internet_protocol_v6-loopback') {
                if (istype(value, 'address-ipv6')) {
                    value = toBinary(value, type)
                    return value == '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001'
                }
            }
            if (type == 'address-ipv6-multicast' || type == 'address-internet_protocol_v6-multicast') {
                if (istype(value, 'address-ipv6')) {
                    value = toBinary(value, type)
                    return value.slice(0, 8) == '11111111'
                }
            }
            if (type == 'address-ipv6-teredo' || type == 'address-internet_protocol_v6-teredo') {
                if (istype(value, 'address-ipv6')) {
                    value = toBinary(value, type)
                    return value.slice(0, 32) == '00100000000000010000000000000000'
                }
            }
            if (type == 'address-ipv6-unicast' || type == 'address-internet_protocol_v6-unicast') {
                if (istype(value, 'address-ipv6')) {
                    value = toBinary(value, type)
                }
            }
            if (type == 'address-ipv6-unspecified' || type == 'address-internet_protocol_v6-unspecified') {
                if (istype(value, 'address-ipv6')) {
                    value = toBinary(value, type)
                    return value == '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
                }
            }
            if (type == 'address-mac' || type == 'address-media_access_control') {
                if (istype(value, 'string')) {
                    if (istype(value, 'binary')) {
                        return value.length == 48
                    } else {
                        let strings = value.split('-')
                        if (strings.length == 6) {
                            for (let string of strings) {
                                if (string.length != 2) return false
                                if (!istype(string, 'hexadecimal')) return false
                            }
                            return true
                        }
                    }
                }
            }
            if (type == 'address-mac-broadcast' || type == 'address-media_access_control-broadcast') {
                if (istype(value, 'address-mac')) {
                    if (istype(value, 'binary')) {
                        return value == '111111111111111111111111111111111111111111111111'
                    } else {
                        return istype(util.address_mac(value), type)
                    }
                }
            }
            if (type == 'address-mac-multicast' || type == 'address-media_access_control-multicast') {
                return istype(value, 'address-mac-multicast-ipv4') || istype(value, 'address-mac-multicast-ipv6')
            }
            if (type == 'address-mac-multicast-ipv4' || type == 'address-media_access_control-multicast-internet_protocol_v4') {
                if (istype(value, 'address-mac')) {
                    value = toBinary(value, type)
                    return value.slice(0, 25) == '0000000100000000010111100'
                }
            }
            if (type == 'address-mac-multicast-ipv6' || type == 'address-media_access_control-multicast-internet_protocol_v6') {
                if (istype(value, 'address-mac')) {
                    value = toBinary(value, type)
                    return value.slice(0, 16) == '0011001100110011'
                }
            }
            if (type == 'address-mac-unicast' || type == 'address-media_access_control-unicast') {
                if (istype(value, 'address-mac')) {
                    return !(istype(value, 'address-mac-broadcast') || istype(value, 'address-mac-multicast'))
                }
            }
            if (type == 'array') {
                if (typeof value === 'object') {
                    return value instanceof Array
                }
            }
            if (type == 'array-boolean') {
                if (istype(value, 'array')) {
                    for (let value_ of value) {
                        if (!istype(value_, 'boolean')) return false
                    }
                    return true
                }
            }
            if (type == 'array-bytes') {
                if (istype(value, 'array')) {
                    for (let value_ of value) {
                        if (!istype(value_, 'bytes')) return false
                    }
                    return true
                }
            }
            if (type == 'array-number') {
                if (istype(value, 'array')) {
                    for (let value_ of value) {
                        if (!istype(value_, 'number')) return false
                    }
                    return true
                }
            }
            if (type == 'array-object') {
                if (istype(value, 'array')) {
                    for (let value_ of value) {
                        if (!istype(value_, 'object')) return false
                    }
                    return true
                }
            }
            if (type == 'array-string') {
                if (istype(value, 'array')) {
                    for (let value_ of value) {
                        if (!istype(value_, 'string')) return false
                    }
                    return true
                }
            }
            if (type == 'array-string-array') {
                if (istype(value, 'array')) {
                    for (let value_ of value) {
                        if (!istype(value_, 'string-array')) return false
                    }
                    return true
                }
            }
            if (type == 'array-string-array-object') {
                if (istype(value, 'array')) {
                    for (let value_ of value) {
                        if (!istype(value_, 'string-array-object')) return false
                    }
                    return true
                }
            }
            if (type == 'array-string-boolean') {
                if (istype(value, 'array')) {
                    for (let value_ of value) {
                        if (!istype(value_, 'string-boolean')) return false
                    }
                    return true
                }
            }
            if (type == 'array-string-number') {
                if (istype(value, 'array')) {
                    for (let value_ of value) {
                        if (!istype(value_, 'string-number')) return false
                    }
                    return true
                }
            }
            if (type == 'array-string-object') {
                if (istype(value, 'array')) {
                    for (let value_ of value) {
                        if (!istype(value_, 'string-object')) return false
                    }
                    return true
                }
            }
            if (type == 'base64') {
                if (istype(value, 'string')) {
                    return new RegExp("^(\+|/|[0-9]|=|[A-Z]|[a-z])+$").test(value)
                }
            }
            if (type == 'binary') {
                if (istype(value, 'string')) {
                    return new RegExp("^(0|1)+$").test(value)
                }
            }
            if (type == 'boolean') {
                return typeof value === 'boolean'
            }
            if (type == 'bytes') {
                return value instanceof Int8Array || value instanceof Uint8Array
            }
            if (type == 'bytes-array') {
                if (istype(value, 'bytes')) {
                    return istype(util.byt2str(value), 'string-array')
                }
            }
            if (type == 'bytes-array-object') {
                if (istype(value, 'bytes')) {
                    return istype(util.byt2str(value), 'string-array-object')
                }
            }
            if (type == 'bytes-object') {
                if (istype(value, 'bytes')) {
                    return istype(util.byt2str(value), 'string-object')
                }
            }
            if (type == 'character') {
                if (istype(value, 'string')) {
                    return new RegExp("^([A-Z]|[a-z])$").test(value)
                }
            }
            if (type == 'coordinates-geographic') {
                return istype(value, 'coordinates-geographic-ddd') || istype(value, 'coordinates-geographic-ddm') || istype(value, 'coordinates-geographic-dms')
            }
            if (type == 'coordinates-geographic-ddd') {
                if (istype(value, 'string')) {
                    return istype(value, 'coordinates-geographic-latitude-ddd') || istype(value, 'coordinates-geographic-longitude-ddd')
                }
                else if (istype(value, 'array-number') || istype(value, 'array-string')) {
                    if (value.length == 2) {
                        return istype(value[0], 'coordinates-geographic-latitude-ddd') && istype(value[1], 'coordinates-geographic-longitude-ddd')
                    }
                }
            }
            if (type == 'coordinates-geographic-ddm') {
                if (istype(value, 'string')) {
                    return istype(value, 'coordinates-geographic-latitude-ddm') || istype(value, 'coordinates-geographic-longitude-ddm')
                }
                else if (istype(value, 'array-string')) {
                    if (value.length == 2) {
                        return istype(value[0], 'coordinates-geographic-latitude-ddm') && istype(value[1], 'coordinates-geographic-longitude-ddm')
                    }
                }
            }
            if (type == 'coordinates-geographic-dms') {
                if (istype(value, 'string')) {
                    return istype(value, 'coordinates-geographic-latitude-dms') || istype(value, 'coordinates-geographic-longitude-dms')
                }
                else if (istype(value, 'array-string')) {
                    if (value.length == 2) {
                        return istype(value[0], 'coordinates-geographic-latitude-dms') && istype(value[1], 'coordinates-geographic-longitude-dms')
                    }
                }
            }
            if (type == 'coordinates-geographic-latitude') {
                if (istype(value, 'string')) {
                    return istype(value, 'coordinates-geographic-latitude-ddd') || istype(value, 'coordinates-geographic-latitude-ddm') || istype(value, 'coordinates-geographic-latitude-dms')
                }
            }
            if (type == 'coordinates-geographic-latitude-ddd') {
                if (istype(value, 'string') || istype(value, 'number')) {
                    return new RegExp(/^(-|\+)?((0)?[0-9]|[1-8][0-9])(\.[0-9]+)?$/).test(`${value}`) || new RegExp("^-?(90)(\.[0]+)?$").test(value)
                }
            }
            if (type == 'coordinates-geographic-latitude-ddm') {
                if (istype(value, 'string')) {
                    return new RegExp(/^([0-8][0-9])(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9][0-9])[NS]$/).test(value) || new RegExp("^(90)(00)\.(00)[NS]$").test(value)
                }
            }
            if (type == 'coordinates-geographic-latitude-dms') {
                if (istype(value, 'string')) {
                    return new RegExp(/^([0-8][0-9])(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])[NS]$/).test(value) || new RegExp("^(90)(00)(00)[NS]$").test(value)
                }
            }
            if (type == 'coordinates-geographic-longitude') {
                if (istype(value, 'string')) {
                    return istype(value, 'coordinates-geographic-longitude-ddd') || istype(value, 'coordinates-geographic-longitude-ddm') || istype(value, 'coordinates-geographic-longitude-dms')
                }
            }
            if (type == 'coordinates-geographic-longitude-ddd') {
                if (istype(value, 'string') || istype(value, 'number')) {
                    return new RegExp(/^(-|\+)?((00)?[0-9]|(0)?[1-9][0-9]|1[0-7][0-9])(\.[0-9]+)?$/).test(`${value}`) || new RegExp("^-?(180)(\.[0]+)?$").test(value)
                }
            }
            if (type == 'coordinates-geographic-longitude-ddm') {
                if (istype(value, 'string')) {
                    return new RegExp(/^(0[0-9][0-9]|1[0-7][0-9])(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\.([0-9][0-9])[EW]$/).test(value) || new RegExp("^(180)(00)\.(00)[EW]$").test(value)
                }
            }
            if (type == 'coordinates-geographic-longitude-dms') {
                if (istype(value, 'string')) {
                    return new RegExp(/^(0[0-9][0-9]|1[0-7][0-9])(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])[EW]$/).test(value) || new RegExp("^(180)(00)(00)[EW]$").test(value)
                }
            }
            if (type == 'date') {
                return value instanceof Date
            }
            if (type == 'decimal') {
                return istype(value, 'number')
            }
            if (type == 'element') {
                return value instanceof Element || value instanceof AppElement
            }
            if (type == 'hexadecimal') {
                if (istype(value, 'string')) {
                    return new RegExp("^([0-9]|[A-F]|[a-f])+$").test(value)
                }
            }
            if (type == 'html') {
                if (istype(value, 'string')) {
                    let document = new DOMParser().parseFromString(value, 'text/html')
                    return Array.from(document.body.childNodes).some(node => node.nodeType === 1)
                }
            }
            if (type == 'html-tag') {
                if (istype(value, 'string')) {
                    let array = '!doctype|a|abbr|address|area|article|aside|audio|b|base|bb|bdi|bdo|big|blockquote|br|button|canvas|caption|cite|code|col|colgroup|data|datalist|dd|del|details|dfn|dialog|div|dl|dt|em|embed|fieldset|figcaption|figure|footer|form|h1|h2|h3|h4|h5|h6|head|header|hr|html|i|iframe|img|input|ins|kbd|label|legend|li|link|main|map|mark|meta|meter|nav|noscript|object|ol|optgroup|option|p|param|picture|polyline|polygon|pre|progress|q|rp|rt|ruby|s|samp|script|section|select|small|source|span|strong|style|sub|summary|sup|svg|table|tbody|td|template|textarea|tfoot|th|thead|tr|track|u|ul|var|video|wbr'.split('|')
                    return array.includes(value)
                }
            }
            if (type == 'identifier') {
                if (istype(value, 'string')) {
                    return new RegExp("^([0-9]|[A-Z]|[a-z]|_)+$").test(value)
                }
            }
            if (type == 'number') {
                return typeof value === 'number'
            }
            if (type == 'object') {
                if (typeof value === 'object') {
                    return value instanceof Object && !(value instanceof Array)
                }
            }
            if (type == 'octal') {
                if (istype(value, 'string')) {
                    return new RegExp("^[0-7]+$").test(value)
                }
            }
            if (type == 'port') {
                if (istype(value, 'number') || istype(value, 'string-number')) {
                    return 0 <= Number(value) && Number(value) <= 65535
                }
            }
            if (type == 'port-ephemeral') {
                if (istype(value, 'number') || istype(value, 'string-number')) {
                    return 1024 <= Number(value) && Number(value) <= 65535
                }
            }
            if (type == 'port-ephemeral-registered') {
                if (istype(value, 'number') || istype(value, 'string-number')) {
                    return 1024 <= Number(value) && Number(value) <= 49151
                }
            }
            if (type == 'port-ephemeral-unregistered' || type == 'port-ephemeral-dynamic' || type == 'port-ephemeral-private') {
                if (istype(value, 'number') || istype(value, 'string-number')) {
                    return 49152 <= Number(value) && Number(value) <= 65535
                }
            }
            if (type == 'port-nonephemeral' || type == 'port-wellknown') {
                if (istype(value, 'number') || istype(value, 'string-number')) {
                    return 0 <= Number(value) && Number(value) <= 1023
                }
            }
            if (type == 'string') {
                return typeof value === 'string'
            }
            if (type == 'string-array') {
                if (istype(value, 'string')) {
                    if (value.length >= 2) {
                        return value.slice(0, 1) == '[' && value.slice(-1) == ']'
                    }
                }
            }
            if (type == 'string-array-object') {
                if (istype(value, 'string')) {
                    if (value.length >= 4) {
                        return value.slice(0, 1) == '[' && value.slice(-1) == ']' && value.slice(1, 2) == '{' && value.slice(-2, -1) == '}'
                    }
                }
            }
            if (type == 'string-boolean') {
                if (istype(value, 'string')) {
                    return value.toLowerCase() == 'true' || value.toLowerCase() == 'false'
                }
            }
            if (type == 'string-number') {
                if (istype(value, 'string')) {
                    if (value.length >= 1) {
                        return !isNaN(value)
                    }
                }
            }
            if (type == 'string-object') {
                if (istype(value, 'string')) {
                    if (value.length >= 2) {
                        return value.slice(0, 1) == '{' && value.slice(-1) == '}'
                    }
                }
            }
            if (type == 'url') {
                if (istype(value, 'string')) {
                    try {
                        new URL(value)
                        return true
                    } catch (error) {
                        return false
                    }
                }
            }
            if (type == 'timestamp') {
                if (istype(value, 'string')) {
                    if (value.includes('T')) {
                        return new RegExp("^(19[7-9][0-9]|[2-9][0-9][0-9][0-9])-(0[0-9]|1[0-2])-(0[0-9]|1[0-9]|2[0-9]|3[0-2])T(0[0-9]|1[0-9]|2[0-3]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])(\.[0-9][0-9][0-9]|)$").test(value)
                    } else {
                        return new RegExp("^(19[7-9][0-9]|[2-9][0-9][0-9][0-9])-(0[0-9]|1[0-2])-(0[0-9]|1[0-9]|2[0-9]|3[0-2])$").test(value)
                    }
                }
            }
            if (type.slice(-2, type.length) == '[]') {
                if (istype(value, 'array')) {
                    for (let value_ of value) {
                        if (!istype(value_, type.slice(0, -2))) {
                            return false
                        }
                    }
                    return true
                }
            }
            return false
        }
        if (value == null || value == undefined) {
            return false
        }
        // 
        let delimiter = null
        if (types.includes('|')) {
            delimiter = '|'
        }
        else if (types.includes('&')) {
            delimiter = '&'
        }
        else {

        }
        // 
        if (delimiter) {
            let results = []
            for (let type of types.split(delimiter)) {
                results.push(istype(value, type))
            }
            if (delimiter == '|') {
                return results.includes(true)
            }
            if (delimiter == '&') {
                return !results.includes(false)
            }
        } else {
            return istype(value, types)
        }
    }
    /**  @param {string} method  @param {...*} args */
    static get(method, ...args) {
        return util[method](...args)
    }
    /** @param {any} value @param {string} types @returns {boolean} */
    static invalidateType(value, types) {
        let valid = util.istype(value, types)
        if (!valid) console.error(`TypeError: variable-name: variable-type:${typeof value}`)
        return !valid
    }
    // a
    /** @param {number|string} value @returns {string} */
    static address_binary(value) {
        if (!util.istype(value, 'number|string')) return console.error(`TypeError: variable-name=value variable-value=${value} variable-type=${typeof value} type=number|string`)
        if (util.istype(value, 'address&binary')) {
            return value
        }
        if (util.istype(value, 'number|string-number')) {
            return util.address_prefix_length_to_mask(value)
        }
        else if (util.istype(value, 'address-ipv4')) {
            return util.address_ipv4(value)
        }
        else if (util.istype(value, 'address-ipv6')) {
            return util.address_ipv6(value)
        }
        else if (util.istype(value, 'address-mac')) {
            return util.address_mac(value)
        }
        else {
            return console.error(`TypeError: variable-name=value variable-value=${value} variable-type=${typeof value} type=address|number|string-number`)
        }
    }
    /** @param {string} address @param {number|string} netmask @returns {string} */
    static address_broadcast(address, netmask) {
        if (!util.istype(address, 'address-ipv4')) return console.error(`TypeError: variable-name=address variable-value=${address} variable-type=${typeof address} type=address-ipv4`)
        address = util.address_binary(address)
        if (!util.istype(netmask, 'address-ipv4-netmask|number|string-number')) return console.error(`TypeError: variable-name=netmask variable-value=${netmask} variable-type=${typeof netmask} type=address-ipv4-netmask|number|string-number`)
        netmask = util.address_binary(netmask)
        let prefix_length = util.address_mask_to_prefix_length(netmask)
        return address.slice(0, prefix_length).ljust(32, '1')
    }
    /** @param {number|string} value @returns {string} */
    static address_decimal(value) {
        return util.bin2dec(util.address_binary(value))
    }
    /** @param {any} value @returns {string|null} */
    static address_family(value) {
        if (util.istype(value, 'address-internet_protocol_v4')) {
            return 'internet_protocol_v4'
        }
        if (util.istype(value, 'address-internet_protocol_v6')) {
            return 'internet_protocol_v6'
        }
        if (util.istype(value, 'address-media_access_control')) {
            return 'media_access_control'
        }
        return console.error(`TypeError: variable-name=value variable-value=${value} variable-type=${typeof value} type=address`)
    }
    /** @param {number|string} value @returns {string} */
    static address_hexadecimal(value) {
        return util.bin2hex(util.address_binary(value))
    }
    /** @param {string} value @returns {string} */
    static address_ip_to_mac_multicast(value) {
        if (util.istype(value, 'address-ipv4')) {
            return util.address_ipv4_to_mac_multicast(value)
        }
        if (util.istype(value, 'address-ipv6')) {
            return util.address_ipv6_to_mac_multicast(value)
        }
        return console.error(`TypeError: variable-name=value variable-value=${value} variable-type=${typeof value} type=address-ip`)
    }
    /** @param {string|null} value @returns {string} */
    static address_ipv4(value = null) {
        let output = ''
        if (value == null) {
            for (let i = 0; i < 4; i++) {
                output += util.dec2bin(util.random(0, 255), 8)
            }
        } else {
            if (value.includes('.')) {
                value.split('.').forEach(octet => output += util.dec2bin(Number(octet), 8))
            } else {
                for (let i = 0; i < value.length; i += 8) {
                    output += (output.length == 0 ? '' : '.') + util.bin2dec(value.slice(i, i + 8))
                }
            }
        }
        return output
    }
    /** @param {string} address @param {number|string} netmask @returns {string} */
    static address_ipv4_broadcast(address, netmask) {
        if (!util.istype(address, 'address-ipv4')) return console.error(`TypeError: variable-name=address variable-value=${address} variable-type=${typeof address} type=address-ipv4`)
        address = util.address_binary(address)
        if (!util.istype(netmask, 'address-ipv4-netmask|number|string-number')) return console.error(`TypeError: variable-name=netmask variable-value=${netmask} variable-type=${typeof netmask} type=address-ipv4-netmask|number|string-number`)
        netmask = util.address_binary(netmask)
        let prefix_length = util.address_mask_to_prefix_length(netmask)
        return address.slice(0, prefix_length).ljust(32, '1')
    }
    /** @param {string} address @param {number|string} netmask @returns {string} */
    static address_ipv4_network_identifier(address, netmask) {
        if (!util.istype(address, 'address-ipv4')) return console.error(`TypeError: variable-name=address variable-value=${address} variable-type=${typeof address} type=address-ipv4`)
        address = util.address_binary(address)
        if (!util.istype(netmask, 'address-ipv4-netmask|number|string-number')) return console.error(`TypeError: variable-name=netmask variable-value=${netmask} variable-type=${typeof netmask} type=address-ipv4-netmask|number|string-number`)
        netmask = util.address_binary(netmask)
        let prefix_length = util.address_mask_to_prefix_length(netmask)
        return address.slice(0, prefix_length).ljust(32, '0')
    }
    /** @param {string} value @returns {string} */
    static address_ipv4_to_ipv6_4to6(value) {
        if (!util.istype(value, 'address-ipv4')) return console.error(`TypeError: variable-name=value variable-value=${value} variable-type=${typeof value} type=address-ipv4`)
        value = util.address_binary(value)
        return '000000000000000000000000000000000000000000000000000000000000000000000000000000001111111111111111' + value
    }
    /** @param {string} value @returns {string} */
    static address_ipv4_to_ipv6_6to4(value) {
        if (!util.istype(value, 'address-ipv4')) return console.error(`TypeError: variable-name=value variable-value=${value} variable-type=${typeof value} type=address-ipv4`)
        value = util.address_binary(value)
        return '0010000000000010' + value + '00000000000000000000000000000000000000000000000000000000000000000000000000000000'
    }
    /** @param {string} value @returns {string} */
    static address_ipv4_to_ipv6_mapped(value) {
        if (!util.istype(value, 'address-ipv4')) return console.error(`TypeError: variable-name=value variable-value=${value} variable-type=${typeof value} type=address-ipv4`)
        value = util.address_binary(value)
        return '000000000000000000000000000000000000000000000000000000000000000000000000000000001111111111111111' + value
    }
    /** @param {string} value @returns {string} */
    static address_ipv4_to_mac_multicast(value) {
        if (!util.istype(value, 'address-ipv4')) return console.error(`TypeError: variable-name=value variable-value=${value} variable-type=${typeof value} type=address-ipv4`)
        value = util.address_binary(value)
        return util.hex2bin('01005E') + '0' + value.slice(9, 32)
    }
    /** @param {string|null} value @returns {string} */
    static address_ipv6(value = null) {
        let output = ''
        if (value == undefined) {
            for (let i = 0; i < 8; i++) {
                output += util.dec2bin(util.random(0, 65535), 16)
            }
        } else if (value.includes(':')) {
            if (value.length == 39) {
                value.split(':').forEach(quartet => output += util.hex2bin(quartet))
            } else {
                let aArray = value.split(':').map((hex) => hex.rjust(4, '0'))
                let bArray = []
                let a = aArray.findIndex((hex) => hex == '0000')
                for (let i = 0; i < aArray.length; i++) {
                    bArray.push(util.hex2bin(aArray[i]))
                    if (i == a) for (let j = 0; j < 8 - aArray.length; j++) {
                        bArray.push(util.hex2bin('0000'))
                    }
                }
                output = bArray.join('')
            }
        } else {
            let aArray = []
            for (let i = 0; i < 128; i += 16) {
                let hex = util.bin2hex(value.slice(i, i + 16))
                for (let j = 0; j < hex.length; j++) {
                    if (hex[j] != '0' || j == 3) {
                        hex = hex.slice(j)
                        break
                    }
                }
                aArray.push(hex)
            }
            let bArray = []
            for (let i = 0; i < 8; i++) {
                if ((i == 0 && aArray[i] == '0') || i != 0 && aArray[i - 1] != '0' && aArray[i] == '0') {
                    bArray.push([i, 0])
                }
                if (aArray[i] == '0') {
                    bArray[bArray.length - 1][1] += 1
                }
            }
            bArray.sort((a, b) => b[1] - a[1])
            if (bArray.length > 0 && bArray[0][1] > 1) {
                for (let i = 0; i < 8; i++) {
                    if (i == bArray[0][0]) {
                        output += (output.slice(output.length - 1, output.length) == ':' ? '' : ':') + ':'
                        i += bArray[0][1] - 1
                    } else output += aArray[i] + (i == 7 ? '' : ':')
                }
            } else output = aArray.join(':')
        }
        return output
    }
    /** @param {string} value @returns {string} */
    static address_ipv6_local_link_to_mac(value) {
        if (!util.istype(value, 'address-ipv6-local-link')) return console.error(`TypeError: variable-name=value variable-value=${value} variable-type=${typeof value} type=address-ipv6-local-link`)
        value = util.address_binary(value)
        let universal_local_bit = value[70] == '0' ? '1' : '0'
        return value.slice(64, 70) + universal_local_bit + value.slice(71, 88) + value.slice(104, 128)
    }
    /** @param {string} value @returns {string} */
    static address_ipv6_to_ipv4(value) {
        if (!util.istype(value, 'address-ipv6')) return console.error(`TypeError: variable-name=value variable-value=${value} variable-type=${typeof value} type=address-ipv6`)
        value = util.address_binary(value)
        if (util.istype(value, 'address-ipv6-4to6')) {
            return value.slice(96, 128)
        }
        if (util.istype(value, 'address-ipv6-6to4')) {
            return value.slice(16, 48)
        }
        return console.error(`TypeError: variable-name=value variable-value=${value} variable-type=${typeof value} type=address-ipv6-4to6|address-ipv6-6to4`)
    }
    /** @param {string} value @returns {string} */
    static address_ipv6_to_mac(value) {
        if (!util.istype(value, 'address-ipv6')) return console.error(`TypeError: variable-name=value variable-value=${value} variable-type=${typeof value} type=address-ipv6`)
        value = util.address_binary(value)
        if (util.istype(value, 'address-ipv6-local-link')) {
            return util.address_ipv6_local_link_to_mac(value)
        }
        if (util.istype(value, 'address-ipv6-multicast')) {
            return util.address_ipv6_to_mac_multicast(value)
        }
    }
    /** @param {string} value @returns {string} */
    static address_ipv6_to_mac_multicast(value) {
        value = util.address_binary(value)
        return util.hex2bin('3333') + value.slice(96, 128)
    }
    /** @param {string} value @param {string} network_identifier @param {string} subnetmask @returns {string} */
    static address_is_ipv4_broadcast(value, network_identifier, subnetmask) {
        value = util.address_binary(value)
        if (value == util.address_ipv4('255.255.255.255')) return true
        return value == util.address_ipv4_broadcast(network_identifier, subnetmask)
    }
    /** @param {string|null} value @returns {string} */
    static address_mac(value = null) {
        let output = ''
        if (value == undefined) {
            for (let i = 0; i < 6; i++) {
                output += util.dec2bin(util.random(0, 255), 8)
            }
        } else {
            if (value.includes('-')) {
                value.split('-').forEach(hex => output += util.hex2bin(hex))
            } else {
                for (let i = 0; i < value.length; i += 8) {
                    output += (output.length == 0 ? '' : '-') + util.bin2hex(value.slice(i, i + 8))
                }
            }
        }
        return output
    }
    /** @param {string} address @param {string} network_prefix @returns {string} */
    static address_mac_to_ipv6_local_link(address, network_prefix) {
        if (!util.istype(address, 'address-mac')) return console.error(`TypeError: variable-name=address variable-value=${address} variable-type=${typeof address} type=address-mac`)
        if (!util.istype(network_prefix, 'binary')) return console.error(`TypeError: variable-name=network_prefix variable-value=${network_prefix} variable-type=${typeof network_prefix} type=binary`)
        if (network_prefix.length != 64) return console.error(`StringLengthError: variable-name=network_prefix variable-length=${network_prefix.length} length=eq64`)
        address = util.address_binary(address)
        let interface_identifier = address.slice(0, 24) + util.hex2bin('fffe') + address.slice(24, 48)
        let universal_local_bit = (interface_identifier[7] == '0' ? '1' : '0')
        interface_identifier = interface_identifier.slice(0, 6) + universal_local_bit + interface_identifier.slice(7, 64)
        return network_prefix + interface_identifier
    }
    /** @param {string} value @returns {number} */
    static address_mask_to_prefix_length(value) {
        // netmask|subnetmask: 11110000..., wildcardmask: 00001111...
        if (!util.istype(value, 'address-ipv4-mask')) return console.error(`TypeError: variable-name=value variable-value=${value} variable-type=${typeof value} type=address-ipv4-mask`)
        value = util.address_binary(value)
        if (value.count('1') == 32 || value.count('0') == 32) {
            return 32
        } else {
            let character = value.find('0') > value.rfind('1') ? '1' : '0'
            return value.count(character)
        }
    }
    /** @param {string} value @returns {string} */
    static address_mask_to_wildcardmask(value) {
        if (!util.istype(value, 'address-ipv4-mask')) return console.error(`TypeError: variable-name=value variable-value=${value} variable-type=${typeof value} type=address-ipv4-mask`)
        value = util.address_binary(value)
        let prefix_length = value.count('1')
        return ''.ljust(prefix_length, '0') + ''.ljust(32 - prefix_length, '1')
    }
    /** @param {string} address @param {number|string} netmask @returns {string} */
    static address_network_identifier(address, netmask) {
        if (!util.istype(address, 'address-ipv4')) return console.error(`TypeError: variable-name=address variable-value=${address} variable-type=${typeof address} type=address-ipv4`)
        address = util.address_binary(address)
        if (!util.istype(netmask, 'address-ipv4-netmask|number|string-number')) return console.error(`TypeError: variable-name=netmask variable-value=${netmask} variable-type=${typeof netmask} type=address-ipv4-netmask|number|string-number`)
        let prefix_length = util.istype(netmask, 'number') ? netmask : util.address_mask_to_prefix_length(netmask)
        return address.slice(0, prefix_length).ljust(32, '0')
    }
    /** @param {number|string} prefix_length @returns {string} */
    static address_prefix_length_to_mask(prefix_length) {
        if (!util.istype(prefix_length, 'number|string-number')) return console.error(`TypeError: variable-name=prefix_length variable-value=${prefix_length} variable-type=${typeof prefix_length} type=number|string-number`)
        prefix_length = Number(prefix_length)
        return '1'.repeat(prefix_length) + '0'.repeat(32 - prefix_length)
    }
    /** @param {number|string} prefix_length @returns {string} */
    static address_prefix_length_to_wildcardmask(prefix_length) {
        if (!util.istype(prefix_length, 'number|string-number')) return console.error(`TypeError: variable-name=prefix_length variable-value=${prefix_length} variable-type=${typeof prefix_length} type=number|string-number`)
        prefix_length = Number(prefix_length)
        return '0'.repeat(prefix_length) + '1'.repeat(32 - prefix_length)
    }
    /** @param {number|string} prefix_length @returns {number} */
    static address_prefix_length_to_address_count(prefix_length) {
        if (!util.istype(prefix_length, 'number|string-number')) return console.error(`TypeError: variable-name=prefix_length variable-value=${prefix_length} variable-type=${typeof prefix_length} type=number|string-number`)
        prefix_length = Number(prefix_length)
        return 2 ** (32 - prefix_length)
    }
    /** @param {number|string} value @returns {string} */
    static address_string(value) {
        if (!util.istype(value, 'number|string')) return console.error(`TypeError: variable-name=value variable-value=${value} variable-type=${typeof value} type=number|string`)
        if (util.istype(value, 'binary')) {
            if (util.istype(value, 'address-internet_protocol_v4')) {
                return util.address_ipv4(value)
            }
            else if (util.istype(value, 'address-internet_protocol_v6')) {
                return util.address_ipv6(value)
            }
            else if (util.istype(value, 'address-media_access_control')) {
                return util.address_mac(value)
            } else {
                return console.error(`TypeError: variable-name=value variable-value=${value} variable-type=${typeof value} type=address`)
            }
        }
        else if (util.istype(value, 'address')) {
            return value
        }
        else if (util.istype(value, 'number|string-number')) {
            return util.address_ipv4(util.address_prefix_length_to_mask(value))
        }
        else {
            return console.error(`TypeError: variable-name=value variable-value=${value} variable-type=${typeof value} type=address|number|string-number`)
        }
    }
    /** @param {string} network_identifier @param {number|string} netmask @param {number|string} subnets @returns {string[]} */
    static address_subnetting(network_identifier, netmask, subnets) {
        if (!util.istype(network_identifier, 'address-ipv4')) return console.error(`TypeError: variable-name=network_identifier variable-value=${network_identifier} variable-type=${typeof network_identifier} type=address-ipv4`)
        network_identifier = util.address_binary(network_identifier)
        if (!util.istype(netmask, 'address-ipv4-netmask|number|string-number')) return console.error(`TypeError: variable-name=netmask variable-value=${netmask} variable-type=${typeof netmask} type=address-ipv4-netmask|number|string-number`)
        netmask = util.address_binary(netmask)
        if (!util.istype(subnets, 'number|string-number')) return console.error(`TypeError: variable-name=subnets variable-value=${subnets} variable-type=${typeof subnets} type=number|string-number`)
        subnets = Number(subnets)
        // 
        network_identifier = util.address_network_identifier(network_identifier, netmask)
        // 
        let network_mask_prefix_length = netmask.indexOf('0')
        let network_extension_length = null
        if (subnets == 1) {
            return [netmask, [network_identifier]]
        }
        // subnets must be a power of 2
        for (let bit_length = 1; bit_length < 32; bit_length++) {
            if ((2 ** bit_length) >= subnets) {
                subnets = 2 ** bit_length
                network_extension_length = bit_length
                break
            }
        }
        if (network_extension_length == null) return []
        let network_identifiers = []
        let wildcardmask_prefix_length = 32 - (network_mask_prefix_length + network_extension_length)
        let subnetmask = '1'.repeat(network_mask_prefix_length) + '1'.repeat(network_extension_length) + '0'.repeat(wildcardmask_prefix_length)
        // cycle through bit combinations in network_extension
        for (let x = 0; x < (2 ** network_extension_length); x++) {
            network_identifiers.append(network_identifier.slice(0, network_mask_prefix_length) + util.dec2bin(x, network_extension_length) + '0'.repeat(wildcardmask_prefix_length))
        }
        return [subnetmask, network_identifiers]
    }
    /** @param {string} value @returns {string|null} */
    static address_type(value) {
        if (util.istype(value, 'address-ipv4')) {
            return 'ipv4'
        }
        if (util.istype(value, 'address-ipv6')) {
            return 'ipv6'
        }
        if (util.istype(value, 'address-mac')) {
            return 'mac'
        }
        return null
    }
    /** @param {string} value @returns {string} */
    static address_wildcardmask_to_mask(value) {
        value = util.address_binary(value)
        let prefix_length = value.count('0')
        return ''.ljust(prefix_length, '1') + ''.ljust(32 - prefix_length, '0')
    }
    /** @param {string} value @returns {number} */
    static address_wildcardmask_to_prefix_length(value) {
        value = util.address_binary(value)
        return value.count('0')
    }
    /** @param {number} number @returns {number} */
    static algebra_number_round(number, placement) {
        let [number_whole, number_rational] = `${Number(number)}`.split('.')
        if (placement > 0) {
            let v = number / 10**placement
            number = util.round(util.round(v, 1) * 10**placement, 1)
        }
        else if (placement < 0 && number_rational.length > -placement) {
            number = util.round(number, -placement)
            number = util.algebra_number_simplify(number)
        }
        return number
    }
    /** @param {number} number  @returns {number} */
    static algebra_number_simplify(number) {
        return `${number}`.slice(-2) == '.0' ? Math.trunc(number) : number
    }
    /** @param {number} n @param {{ index:number, result:number }} results  @returns {number} */
    static algorithm_fibonacci(n, results = {}) {
        if (n == 0 || n == 1) {
            return n
        }
        if (n in results) {
            return results[n]
        }
        let result = util.algorithm_fibonacci(n - 1, results) + util.algorithm_fibonacci(n - 2, results)
        results[n] = result
        return result
    }
    /** @returns {Generator<number, void, unknown>} */
    static *algorithm_fibonacci_generator() {
        let current = 0
        let next = 1
        while (true) {
            let reset = yield current;
            [current, next] = [next, next + current]
            if (reset) {
                current = 0
                next = 1
            }
        }
    }
    /** @param {number} n @param {{ index:number, result:number }} results  @returns {number} */
    static algorithm_tribonacci(n, results = {}) {
        if (n == 0 || n == 1) {
            return 0
        }
        if (n == 2) {
            return 1
        }
        if (n in results) {
            return results[n]
        }
        let result = util.algorithm_tribonacci(n - 1, results) + util.algorithm_tribonacci(n - 2, results) + util.algorithm_tribonacci(n - 3, results)
        results[n] = result
        return result
    }
    // b
    /** @param {string} value @returns {string} */
    static base64_encode(value) {
        if (!util.istype(value, 'string')) return console.error(`TypeError: `, value)
        return window.btoa(value)
    }
    /** @param {string} value @returns {string} */
    static base64_decode(value) {
        if (!util.istype(value, 'string')) return console.error(`TypeError: `, value)
        return window.atob(value)
    }
    /** @param {string} value @returns {boolean} */
    static boolean(value) {
        return ['y', 'yes', '1', 't', 'true'].includes(value.toLowerCase())
    }
    /** @param {bytes|number} value @param {number} fractionDigits @returns {string} */
    static bytes_format(value, fractionDigits = 2) {
        if (!util.istype(value, 'bytes|number')) return console.error(`TypeError: variable-name:value variable-type:${typeof value} type=bytes|number`)
        if (util.istype(value, 'bytes')) {
            value = util.byt2dec(value)
        }
        if (value < 1024) {
            return `${value} B`
        } else if (value < 1048576) {
            return `${(value / 1024).toFixed(fractionDigits)} KB`
        } else if (value < 1073741824) {
            return `${(value / 1048576).toFixed(fractionDigits)} MB`
        } else if (value < 1099511627776) {
            return `${(value / 1073741824).toFixed(fractionDigits)} GB`
        } else {
            return `${(value / 1099511627776).toFixed(fractionDigits)} TB`
        }
    }
    // c
    /** @param {number[]} point @param {number[][]} polygon @returns {boolean} */
    static cartesian_in(point, polygon) {
        let n = polygon.length
        let inside = false
        let j = n - 1
        for (let i = 0; i < n; i++) {
            if (polygon[i][1] <= point[1] && polygon[j][1] >= point[1] || polygon[j][1] <= point[1] && polygon[i][1] >= point[1]) {
                if (point[0] <= (polygon[j][0] - polygon[i][0]) * (point[1] - polygon[i][1]) / (polygon[j][1] - polygon[i][1]) + polygon[i][0]) {
                    inside = !inside
                }
            }
            j = i
        }
        return inside
    }
    /** @param {number[]} point1 @param {number[]} point2 @returns {number} */
    static cartesian_polygon_centroid(points) {
        // let xSum = 0;
        // let ySum = 0;
        // let area = 0;
        // // iterate through the polygon's vertices
        // for (let i = 0; i < points.length - 1; i++) {
        //     let x1 = points[i][0];
        //     let y1 = points[i][1];
        //     let x2 = points[i + 1][0];
        //     let y2 = points[i + 1][1];
        //     // calculate the signed area of the triangle formed by the current vertex, the next vertex, and the origin
        //     let a = x1 * y2 - x2 * y1;
        //     area += a;
        //     // update the sums of x and y coordinates, weighted by the triangle's area
        //     xSum += (x1 + x2) * a;
        //     ySum += (y1 + y2) * a;
        // }
        // // calculate the centroid coordinates
        // area /= 2;
        // let cx = xSum / (6 * area);
        // let cy = ySum / (6 * area);
        // return [cx, cy];

        // let xSum = 0
        // let ySum = 0
        // for (let point of points) {
        //     xSum += point[0]
        //     ySum += point[1]
        // }
        // let xAverage = xSum / points.length
        // let yAverage = ySum / points.length
        // let centroid = [xAverage, yAverage]
        // return centroid

        // initialize the centroid coordinates
        let x = 0;
        let y = 0;
        let area = 0;
        // iterate through the polygon's vertices
        for (let i = 0, j = points.length - 1; i < points.length; j = i++) {
            let xi = points[i][0];
            let yi = points[i][1];
            let xj = points[j][0];
            let yj = points[j][1];
            // calculate the cross product between two consecutive vertices.
            let crossProduct = xi * yj - xj * yi;
            area += crossProduct;
            /// update the x and y coordinates of the centroid based on the cross product and vertex coordinates.
            x += (xi + xj) * crossProduct;
            y += (yi + yj) * crossProduct;
        }
        area /= 2;
        x /= (6 * area);
        y /= (6 * area);
        return [x, y];
    }
    /** @param {number[]} point1 @param {number[]} point2 @returns {number} */
    static cartesian_to_azimuth(point1, point2) {
        let [x1, y1] = point1
        let [x2, y2] = point2
        let dx = x2 - x1
        let dy = y2 - y1
        let theta = Math.atan2(dy, dx)
        let degrees = theta * util.RADIANS_TO_DEGREES
        let azimuth = (90 - degrees) % 360
        return azimuth
    }
    /** @param {number[]} point1 @param {number[]} point2 @returns {number[]} */
    static cartesian_to_cylindrical(point1, point2) {
        let [x1, y1, z1] = point1
        let [x2, y2, z2] = point2
        let dx = x2 - x1
        let dy = y2 - y1
        let dz = z2 - z1
        let r = (dx ** 2 + dy ** 2 + dz ** 2) ** 0.5
        let azimuth = Math.atan2(dy, dx)
        let height = Math.atan2(dz, r)
        return [r, azimuth, height]
    }
    /** @param {number[]} point1 @param {number[]} point2 @returns {number} */
    static cartesian_to_distance(point1, point2) {
        let length1 = point1.length
        let length2 = point2.length
        if (length1 == 2 && length2 == 2) {
            let [x1, y1] = point1
            let [x2, y2] = point2
            let dx = x2 - x1
            let dy = y2 - y1
            let distance = (dx ** 2 + dy ** 2) ** 0.5
            return distance
        }
        if (length1 == 3 && length2 == 3) {
            let [x1, y1, z1] = point1
            let [x2, y2, z2] = point2
            let dx = x2 - x1
            let dy = y2 - y1
            let dz = z2 - z1
            let distance = (dx ** 2 + dy ** 2 + dz ** 2) ** 0.5
            return distance
        }
    }
    /** @param {number[]} point1 @param {number[]} point2 @returns {number} */
    static cartesian_to_elevation(point1, point2) {
        let [x1, y1, z1] = point1
        let [x2, y2, z2] = point2
        let dx = x2 - x1
        let dy = y2 - y1
        let dz = z2 - z1
        let r = (dx ** 2 + dy ** 2 + dz ** 2) ** 0.5
        let phi = Math.acos(dz / r)
        let degrees = phi * util.RADIANS_TO_DEGREES
        let elevation = 90 - degrees
        return elevation
    }
    /** @param {number[]} point1 @param {number[]} point2 @returns {number} */
    static cartesian_to_midpoint(point1, point2) {
        length1 = point1.length
        length2 = point2.length
        if (length1 == 2 && length2 >= 2) {
            let [x1, y1] = point1
            let [x2, y2] = point2
            midpoint = [(x1 + x2) / 2, (y1 + y2) / 2]
            return midpoint
        }
        if (length1 == 3 && length2 == 3) {
            let [x1, y1, z1] = point1
            let [x2, y2, z2] = point2
            midpoint = [(x1 + x2) / 2, (y1 + y2) / 2, (z1 + z2) / 2]
            return midpoint
        }
    }
    /** @param {number[]} point1 @param {number[]} point2 @returns {number[]} */
    static cartesian_to_polar(point1, point2) {
        // returns: radius, angle, height
        let [x1, y1, z1] = point1
        let [x2, y2, z2] = point2
        let dx = x2 - x1
        let dy = y2 - y1
        let dz = z2 - z1
        let r = (dx ** 2 + dy ** 2) ** 0.5
        let theta = Math.atan2(dy, dx)
        return [r, theta]
    }
    /** @param {number[]} point1 @param {number[]} point2 @returns {number[]} */
    static cartesian_to_slope(point1, point2) {
        // returns: radius, angle, height
        let [x1, y1] = point1
        let [x2, y2] = point2
        let dx = x2 - x1
        let dy = y2 - y1
        return dy / dx
    }
    /** @param {number[]} point1 @param {number[]} point2 @returns {number[]} */
    static cartesian_to_spherical(point1, point2) {
        // returns: radius, angle, height
        let [x1, y1, z1] = point1
        let [x2, y2, z2] = point2
        let dx = x2 - x1
        let dy = y2 - y1
        let dz = z2 - z1
        let r = (dx ** 2 + dy ** 2 + dz ** 2) ** 0.5
        let theta = Math.atan2(dy, dx)
        let phi = Math.acos(dz / r)
        return [r, theta, phi]
    }
    /** @param {number[]} point1 @param {number[]} point2 @returns {number} */
    static cartesian_to_theta(point1, point2) {
        let [x1, y1] = point1
        let [x2, y2] = point2
        let dx = x2 - x1
        let dy = y2 - y1
        let theta = Math.atan2(dy, dx)
        return theta
    }
    /** @param {any} value @returns {any} */
    static clone(value) {
        return JSON.parse(JSON.stringify(value))
    }
    /** @param {number} number @param {number} minimum @param {number} maximum @returns {number} */
    static constrain(number, minimum, maximum) {
        if (minimum <= number && number <= maximum) {
            return number
        }
        if (number > maximum) {
            return minimum + (number % maximum)
        }
        if (number < minimum) {
            return (number % maximum) + maximum
        }
    }
    /** @param {string} value @returns {number} */
    static coordinate_conversions(value) {
        if (!util.istype(value, 'string')) return console.error(`TypeError: `, value)
        let semiMajorAxis = 6378137.0
        let semiMinorAxis = 6356752.3142
        if (value == 'semiMajorAxis') return semiMajorAxis
        else if (value == 'semiMinorAxis') return semiMinorAxis
        else return console.error(`TypeError: `, value)
    }
    /** @param {any} value @returns {any} */
    static copy(value) {
        return JSON.parse(JSON.stringify(value))
    }
    /** @param {{string:string}} value @returns {string} */
    static css_encode(value) {
        let string = ''
        for (let [cssKey, cssValue] in enumerate(value)) {
            string += (string.empty() ? '' : '; ') + cssKey + ': ' + cssValue
        }
        return string
    }
    /** @param {string} string @returns {{string:string}} */
    static css_decode(value) {
        let object = {}
        for (let entry of value.strip(' ;').split(';')) {
            let [cssKey, cssValue] = entry.split(':')
            cssKey = cssKey.strip(' ')
            cssValue = cssValue.strip(' ')
            object[cssKey] = cssValue
        }
        return object
    }
    /** @param {{}[]} value @returns {string} */
    static csv_encode(value) {

    }
    /** @param {string} value @returns {{}[]} */
    static csv_decode(value) {
        if (!util.istype(value, 'string')) return console.error(`TypeError: `, value)
    }
    /** @param {number} r @param {number} azimuth @param {number} height @returns {number[]} */
    static cylindrical_to_cartesian(r, azimuth, height) {
        azimuth *= util.DEGREES_TO_RADIANS
        let x = r * math.cos(azimuth)
        let y = r * math.sin(azimuth)
        let z = height
        return [x, y, z]
    }
    // d
    /** @param {number} degrees @returns {number}  */
    static degrees_to_radians(degrees) {
        return degrees * util.DEGREES_TO_RADIANS
    }
    // e
    /** @param {{}[]} entries @param {...any} values @returns {boolean} */
    static entries_contains(entries, ...values) {
        let filters = object.fromarray(values)
        for (let entry of entries) {
            for (let [filterKey, filterValue] of enumerate(filters)) {
                if (entry[filterKey] == filterValue) {
                    return true
                }
            }
        }
        return false
    }
    /** @param {{}[]} entries @param {...any} values @returns {boolean} */
    static entries_excludes(entries, ...values) {
        let filters = object.fromarray(values)
        for (let entry of entries) {
            for (let [filterKey, filterValue] of enumerate(filters)) {
                if (entry[filterKey] == filterValue) {
                    return false
                }
            }
        }
        return true
    }
    /** @param {{}[]} entries @param {...any} values @returns {{}[]} */
    static entries_filter(entries, ...values) {
        if (!util.istype(entries, 'array')) return console.error(`TypeError: `, entries)
        return util.filter_and(entries, ...values)
    }
    /** @param {{}[]} entries @param {...any} values @returns {{}[]} */
    static entries_filter_and(entries, ...values) {
        if (!util.istype(entries, 'array')) return console.error(`TypeError: `, entries)
        let filters = []
        for (let i = 0; i < values.length; i += 2) filters.push({ 'key': values[i], 'val': values[i + 1] })
        let filtered = []
        for (let i = 0; i < entries.length; i++) {
            let matches = 0
            for (let filter of filters) {
                if (entries[i][filter['key']] == filter['val']) matches++
            }
            if (matches == filters.length) filtered.push(entries[i])
        }
        return filtered
    }
    /** @param {{}[]} entries @param {...any} values @returns {{}[]} */
    static entries_filter_or(entries, ...values) {
        if (!util.istype(entries, 'array')) return console.error(`TypeError: `, entries)
        let filters = []
        for (let i = 0; i < values.length; i += 2) filters.push({ 'key': values[i], 'val': values[i + 1] })
        let filtered = []
        for (let i = 0; i < entries.length; i++) {
            let matches = 0
            for (let filter of filters) {
                if (entries[i][filter['key']] == filter['val']) matches++
            }
            if (matches != 0) filtered.push(entries[i])
        }
        return filtered
    }
    /** @param {{}[]} entries @param {...any} values @returns {{}|null} */
    static entries_find(entries, ...values) {
        if (!util.istype(entries, 'array')) return console.error(`TypeError: `, entries)
        return util.entries_find_and(entries, ...values)
    }
    /** @param {{}[]} entries @param {...any} values @returns {{}|null} */
    static entries_find_and(entries, ...values) {
        if (!util.istype(entries, 'array')) return console.error(`TypeError: `, entries)
        let filters = []
        for (let i = 0; i < values.length; i += 2) filters.push({ 'key': values[i], 'val': values[i + 1] })
        for (let i = 0; i < entries.length; i++) {
            let matches = 0
            for (let filter of filters) {
                if (entries[i][filter['key']] == filter['val']) matches++
            }
            if (matches == filters.length) return { 'index': i, 'value': entries[i] }
        }
        return null
    }
    /** @param {{}[]} entries @param {...any} values @returns {{}|null} */
    static entries_find_or(entries, ...values) {
        if (!util.istype(entries, 'array')) return console.error(`TypeError: `, entries)
        let filters = []
        for (let i = 0; i < values.length; i += 2) filters.push({ 'key': values[i], 'val': values[i + 1] })
        for (let i = 0; i < entries.length; i++) {
            let matches = 0
            for (let filter of filters) {
                if (entries[i][filter['key']] == filter['val']) matches++
            }
            if (matches != 0) return { 'index': i, 'value': entries[i] }
        }
        return null
    }
    /** @param {{}[]} entries @param {...any} values @returns {{}[]} */
    static entries_remove(entries = [], ...values) {
        // values: array = [{ id:'' }] or [id]
        if (!util.istype(entries, 'array')) return console.error(`TypeError: `, entries)
        if (!util.istype(values, 'array')) return console.error(`TypeError: `, values)
        for (let i = 0; i < values.length; i++) {
            if (util.istype(values[i], 'object')) {
                values[i] = values[i]['id']
            }
        }
        let array = []
        for (let entry of entries) {
            if (!values.includes(entry['id'])) {
                array.push(entry)
            }
        }
        return array
    }
    /** @param {{}[]} entries @param {...any} values @returns {{}[]} */
    static entries_remove_filter(entries, ...values) {
        if (!util.istype(entries, 'array')) return console.error(`TypeError: `, entries)
        let filtered = util.entries_filter_and(entries, ...values)
        return util.remove(entries, ...filtered)
    }
    /** @param {number|string} value @returns {string} */
    static expand_exponential(value) {
        if (!util.istype(value, 'number|string')) return console.error(`TypeError: `, value)
        value = value.toString()
        return value.replace(/^([+-])?(\d+).?(\d*)[eE]([-+]?\d+)$/, (x, s, n, f, c) => {
            var l = +c < 0, i = n.length + +c, x = (l ? n : f).length,
                c = ((c = Math.abs(c)) >= x ? c - x + l : 0),
                z = (new Array(c + 1)).join("0"), r = n + f
            return (s || "") + (l ? r = z + r : r += z).slice(0, i += l ? z.length : 0) + (i < r.length ? "." + r.slice(i) : "")
        })
    }
    // f
    /** @param {string} filename @param {bytes|string} data @param {string} type @returns {void} */
    static file_create(filename, data, type = 'text/plain') {
        if (!util.istype(filename, 'string')) return console.error(`TypeError: `, filename)
        if (util.istype(data, 'string')) data = util.str2byt(data)
        if (data instanceof ArrayBuffer) data = new Uint8Array(data)
        if (!util.istype(data, 'bytes')) return console.error(`TypeError: `, data)
        if (!util.istype(type, 'string')) return console.error(`TypeError: `, type)
        let element = document.createElement('a')
        let blob = new Blob([data], { type: type })
        let urlCreator = window.URL || window.webkitURL
        let url = urlCreator.createObjectURL(blob)
        element.href = url
        element.setAttribute('download', filename)
        element.style['display'] = 'none'
        document.body.appendChild(element)
        element.click()
        document.body.removeChild(element)
    }
    /** @param {string|string[]} file_extensions @param {(FileSystemFileHandle[]) => void} callback @returns {FileSystemFileHandle[]} */
    static file_picker(file_extensions, callback) {
        // https://developer.mozilla.org/en-US/docs/Web/API/Window/showOpenFilePicker
        if (!('showOpenFilePicker' in window)) {
            return callback([])
        }
        if (util.istype(file_extensions, 'array-string')) {
            
        }
        else if (util.istype(file_extensions, 'string')) {
            file_extensions = file_extensions.strip(' ').split('|')
        } else {
            return callback([])
        }
        let options = {
            excludeAcceptAllOption: true,
            multiple: false,
            startIn: 'downloads',
            types: [],
        }
        for (let file_extension of file_extensions) {
            file_extension = file_extension[0] == '.' ? file_extension.slice(1) : file_extension
            let entries = {}
            for (let [mime_type, _file_extensions] of enumerate(util.MIME_TYPES)) {
                if (_file_extensions.includes(file_extension)) {
                    let key = mime_type.split('/')[0]
                    if (!entries[key]) {
                        entries[key] = []
                    }
                    entries[key].append(..._file_extensions)
                    break
                }
            }
            for (let [key, extensions] of enumerate(entries)) {
                let accept = {}
                accept[`${key}/*`] = extensions.map((extension) => `.${extension}`)
                let deescription = `${key.capitalize()}s`
                options.types.push({
                    accept: accept,
                    key: deescription,
                })
            }
        }
        if (file_extensions.empty()) {
            options.types.push({
                description: 'All',
                accept: {}
            })
        }
        window.showOpenFilePicker(options).then((fileSystemFileHandles) => {
            // fileSystemFileHandles:array=[FileSystemFileHandle()]
            // fileSystemFileHandle.getFile().then((file) => { file.text().then((data) => {}})
            callback(fileSystemFileHandles)
        })
    }
    /** @param {string} path @param {(ArrayBuffer) => void} callback @returns {void} */
    static file_read(path, callback) {
        if (!util.istype(path, 'string')) return console.error(`TypeError: `, path)
        fetch(path).then((response) => response.arrayBuffer()).then(data => {
            callback(data)
        }).catch((error) => {
            console.warn(error)
            callback(ArrayBuffer())
        })
    }
    /** @param {string} path @param {(Object) => void} callback @returns {void} */
    static file_read_data(path, callback) {
        let dataTypes = {
            'list': {
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
        function isBlank(line) {
            return line.trim() == ''
        }
        function hasKey(key, line) {
            return line.indexOf(key) == 0
        }
        function getLines(lines, index) {
            let value = ''
            while (index < lines.length) {
                let line = lines[index]
                if (isBlank(line)) break
                value += (value == '' ? '' : '\n') + line
                index += 1
            }
            return [value, index]
        }
        function getValue(key, string) {
            if (key == 'list') {
                return string.split('\n').map((line) => line.trim())
            }
            if (key == 'name') {
                return string
            }
            if (key == 'reference') {
                return string.split(',').map((string) => string.trim())
            }
            if (key == 'subtitle') {
                return string
            }
            if (key == 'table') {
                function getHeaders(string, delimiter = '     ') {
                    let headers = {}
                    let delimiterLength = delimiter.length
                    let stringLength = string.length
                    let sIndex = 0
                    let cIndex = 0
                    while (cIndex < string.length) {
                        if (cIndex == stringLength - 1) {
                            let header = string.slice(sIndex, cIndex + 1).trim()
                            headers[header] = [sIndex, -1]
                        }
                        if (string.slice(cIndex, cIndex + delimiterLength) == delimiter && string[cIndex + delimiterLength] != ' ') {
                            let header = string.slice(sIndex, cIndex + delimiterLength - 1).trim()
                            headers[header] = [sIndex, cIndex + delimiterLength - 1]
                            sIndex = cIndex + delimiterLength
                        }
                        cIndex += 1
                    }
                    return headers
                }
                let entries = []
                let lines = string.split('\n')
                let headers = getHeaders(lines[0])
                for (let index = 1; index < lines.length; index++) {
                    let line = lines[index]
                    entries.push({})
                    for (let header in headers) {
                        let indexes = headers[header]
                        let sIndex = indexes[0]
                        let eIndex = indexes[1] == -1 ? line.length : indexes[1]
                        entries[entries.length - 1][header] = line.slice(sIndex, eIndex).trim()
                    }
                }
                return entries
            }
            if (key == 'title') {
                return string
            }
        }
        function decode(string) {
            let data = {}
            let lines = string.replaceAll('\r', '').split('\n')
            let index = 0
            for (let key in dataTypes) {
                let dataType = dataTypes[key]
                if (dataType['type'] == 'array') {
                    data[key] = []
                }
                if (dataType['type'] == 'object') {
                    data[key] = {}
                }
                if (dataType['type'] == 'string') {
                    data[key] = ''
                }
            }
            while (index < lines.length) {
                let line = lines[index]

                for (let key in dataTypes) {
                    let dataType = dataTypes[key]
                    if (hasKey(key, line)) {
                        let keyvalue = line.slice(key.length + 1, line.length).trim()
                        let value = null
                        if (dataType['lines'] == 'single') {
                            value = getValue(key, keyvalue)
                        }
                        if (dataType['lines'] == 'multiple') {
                            [value, index] = getLines(lines, index + 1)
                            value = getValue(key, value)
                        }
                        if (dataType['type'] == 'array') {
                            data[key].push(value)
                        }
                        if (dataType['type'] == 'object') {
                            data[key][keyvalue] = value
                        }
                        if (dataType['type'] == 'string') {
                            data[key] = value
                        }
                        break
                    }
                }
                index += 1
            }
            return data
        }
        util.file_read_string(path, (data) => {
            data = decode(data)
            callback(data)
        })
    }
    /** @param {string} path @param {(Array|Object) => void} callback @returns {void} */
    static file_read_json(path, callback = (data) => { }) {
        fetch(path).then((response) => response.json()).then(data => {
            callback(data)
        }).catch((error) => {
            console.warn(error)
            callback([])
        })
    }
    /** @param {string} path @param {(string[]) => void} callback @returns {void} */
    static file_read_list(path, callback = (data) => { }) {
        if (!util.istype(path, 'string')) return console.error(`TypeError: `, path)
        fetch(path).then((response) => response.text()).then(data => {
            data = data.replaceAll('\r', '')
            data = data.split('\n').map((string) => string.trim())
            callback(data)
        }).catch((error) => {
            console.warn(error)
            callback([])
        })
    }
    /** @param {string} path @param {(string) => void} callback @returns {void} */
    static file_read_string(path, callback = (data) => { }) {
        if (!util.istype(path, 'string')) return console.error(`TypeError: `, path)
        fetch(path).then((response) => response.text()).then(data => {
            data = data.replaceAll('\r', '')
            callback(data)
        }).catch((error) => {
            console.warn(error)
            callback('')
        })
    }
    /** @param {FileSystemFileHandle} fileHandle @param {bytes} data @param {(string) => void} callback @returns {void} */
    static file_write(fileHandle, data, callback = () => { }) {
        fileHandle.createWritable().then((writable) => {
            // writable = FileSystemWritableFileStream
            writable.write(data).then((response) => {
                writable.close().then((response) => {
                    callback()
                })
            })
        })
    }
    // g

    /** @param {string[]} point @returns {string[]} */
    static geographic_ddd_to_ddm(point) {
        if (!util.istype(point, 'coordinates-geographic-ddd')) {
            throw new Error(`ValueError: variable-name=point variable-value=${point} >>> Invalid Format`)
        }
        return ''
    }
    /** @param {string[]} point @returns {string[]} */
    static geographic_ddd_to_dms(point) {
        if (!util.istype(point, 'coordinates-geographic-ddd')) {
            throw new Error(`ValueError: variable-name=point variable-value=${point} >>> Invalid Format`)
        }
        let degrees, minutes, seconds, direction
        point = [Number(point[0]), Number(point[1])]
        degrees = `${Math.floor(Math.abs(point[0]))}`
        minutes = `${Math.floor((Math.abs(point[0]) - degrees) * 60)}`
        seconds = `${Math.round((Math.abs(point[0]) - degrees - minutes / 60) * 3600)}`
        if (seconds == '60') {
            seconds = '0'
            minutes = `${Number(minutes) + 1}`
        }
        if (minutes == 60) {
            minutes = '0'
            degrees = `${Number(degrees) + 1}`
        }
        direction = point[0] >= 0 ? 'N' : 'S'
        let latitude = `${degrees.rjust(2, '0')}${minutes.rjust(2, '0')}${seconds.rjust(2, '0')}${direction}`
        degrees = `${Math.floor(Math.abs(point[1]))}`
        minutes = `${Math.floor((Math.abs(point[1]) - degrees) * 60)}`
        seconds = `${Math.round((Math.abs(point[1]) - degrees - minutes / 60) * 3600)}`
        if (seconds == '60') {
            seconds = '0'
            minutes = `${Number(minutes) + 1}`
        }
        if (minutes == 60) {
            minutes = '0'
            degrees = `${Number(degrees) + 1}`
        }
        direction = point[1] >= 0 ? 'E' : 'W'
        let longitude = `${degrees.rjust(3, '0')}${minutes.rjust(2, '0')}${seconds.rjust(2, '0')}${direction}`
        return [latitude, longitude]
    }
    /** @param {string[]} point @returns {string[]} */
    static geographic_ddm_to_ddd(point) {
        if (!util.istype(point, 'coordinates-geographic-ddm')) {
            throw new Error(`ValueError: variable-name=point variable-value=${point} >>> Invalid Format`)
        }
        return ''
    }
    /** @param {string[]} point @returns {string[]} */
    static geographic_ddm_to_dms(point) {
        if (!util.istype(point, 'coordinates-geographic-ddm')) {
            throw new Error(`ValueError: variable-name=point variable-value=${point} >>> Invalid Format`)
        }
        return ''
    }
    /** @param {string[]} point @returns {string[]} */
    static geographic_dms_to_ddd(point) {
        if (!util.istype(point, 'coordinates-geographic-dms')) {
            throw new Error(`ValueError: variable-name=point variable-value=${point} >>> Invalid Format`)
        }
        let degrees, minutes, seconds, direction
        let decimal_degrees
        degrees = Number(point[0].slice(0, 2))
        minutes = Number(point[0].slice(2, 4))
        seconds = Number(point[0].slice(4, 6))
        direction = point[0].slice(-1)
        decimal_degrees = degrees + minutes/60 + seconds/3600
        decimal_degrees *= direction == 'N' ? 1 : -1
        let latitude = `${decimal_degrees}`
        degrees = Number(point[1].slice(0, 3))
        minutes = Number(point[1].slice(3, 5))
        seconds = Number(point[1].slice(5, 7))
        direction = point[1].slice(-1)
        decimal_degrees = degrees + minutes/60 + seconds/3600
        decimal_degrees *= direction == 'E' ? 1 : -1
        let longitude = `${decimal_degrees}`
        return [latitude, longitude]
    }
    /** @param {string[]} point @returns {string[]} */
    static geographic_dms_to_ddm(point) {
        if (!util.istype(point, 'coordinates-geographic-dms')) {
            throw new Error(`ValueError: variable-name=point variable-value=${point} >>> Invalid Format`)
        }
        let degrees, minutes, seconds, direction
        let decimal_minutes
        degrees = Number(point[0].slice(0, 2))
        minutes = Number(point[0].slice(2, 4))
        seconds = Number(point[0].slice(4, 6))
        direction = point[0].slice(-1)
        decimal_minutes = minutes + seconds/60
        let latitude = `${degrees.rjust(2, '0')}${decimal_minutes.toFixed(2).rjust(5, '0')}${direction}`
        degrees = Number(point[1].slice(0, 3))
        minutes = Number(point[1].slice(3, 5))
        seconds = Number(point[1].slice(5, 7))
        direction = point[1].slice(-1)
        decimal_minutes = minutes + seconds/60
        let longitude = `${degrees.rjust(3, '0')}${decimal_minutes.toFixed(2).rjust(5, '0')}${direction}`
        return [latitude, longitude]
    }
    /** @param {number[]} point1 @param {number[]} point2 @returns {number} */
    static geographic_to_azimuth(point1, point2) {
        let latitude1 = point1[0] * util.DEGREES_TO_RADIANS
        let longitude1 = point1[1] * util.DEGREES_TO_RADIANS
        let latitude2 = point2[0] * util.DEGREES_TO_RADIANS
        let longitude2 = point2[1] * util.DEGREES_TO_RADIANS
        let differenceLatitude = latitude2 - latitude1
        let differenceLongitude = longitude2 - longitude1
        let y = Math.sin(differenceLongitude) * Math.cos(latitude2)
        let x = Math.cos(latitude1) * Math.sin(latitude2) - Math.sin(latitude1) * Math.cos(latitude2) * Math.cos(differenceLongitude)
        let theta = Math.atan2(y, x)
        theta = util.constrain(theta, 0, Math.PI * 2)
        let azimuth = theta * util.RADIANS_TO_DEGREES
        return azimuth
    }
    /** @param {number[]} point1 @param {number[]} point2 @returns {number} */
    static geographic_to_azimuth_rhumb(point1, point2) {
        let latitude1 = point1[0] * util.DEGREES_TO_RADIANS
        let longitude1 = point1[1] * util.DEGREES_TO_RADIANS
        let latitude2 = point2[0] * util.DEGREES_TO_RADIANS
        let longitude2 = point2[1] * util.DEGREES_TO_RADIANS
        let differenceLatitude = latitude2 - latitude1
        let differenceLongitude = longitude2 - longitude1
        if (Math.abs(differenceLongitude) > Math.PI) {
            differenceLongitude = differenceLongitude > 0 ? -(2 * Math.PI - differenceLongitude) : (2 * Math.PI + differenceLongitude)
        }
        let aa = Math.log(Math.tan(latitude2 / 2 + Math.PI / 4) / Math.tan(latitude1 / 2 + Math.PI / 4))
        let theta = Math.atan2(differenceLongitude, aa)
        theta = util.constrain(theta, 0, Math.PI * 2)
        let azimuth = theta * util.RADIANS_TO_DEGREES
        return azimuth
    }
    /** @param {number} latitude @param {number} longitude @param {number} altitude @returns {number[]} */
    static geographic_to_cartesian(latitude, longitude, altitude) {
        let r = util.SPHERE_RADIUS + altitude
        let theta = (longitude >= 0 ? longitude : 360 + longitude) * util.DEGREES_TO_RADIANS
        let phi = (90 - latitude) * util.DEGREES_TO_RADIANS
        let x = r * Math.sin(phi) * Math.cos(theta)
        let y = r * Math.sin(phi) * Math.sin(theta)
        let z = r * Math.cos(phi)
        return [x, y, z]
    }
    /** @param {number[]} point @param {number} azimuth @param {number} distance @returns {number[]} */
    static geographic_to_destination_point(point, azimuth, distance) {
        // destination point from start point having traveled the given distance on the given initial bearing
        let latitude = point[0] * util.DEGREES_TO_RADIANS
        let longitude = point[1] * util.DEGREES_TO_RADIANS
        let theta = azimuth * util.DEGREES_TO_RADIANS
        let angularDistance = distance / util.SPHERE_RADIUS
        let destinationLatitude = Math.asin(Math.sin(latitude) * Math.cos(angularDistance) + Math.cos(latitude) * Math.sin(angularDistance) * Math.cos(theta))
        let destinationLongitude = longitude + Math.atan2(Math.sin(theta) * Math.sin(angularDistance) * Math.cos(latitude), Math.cos(angularDistance) - Math.sin(latitude) * Math.sin(destinationLatitude))
        destinationLatitude *= util.RADIANS_TO_DEGREES
        destinationLongitude *= util.RADIANS_TO_DEGREES
        return [destinationLatitude, destinationLongitude]
    }
    /** @param {number[]} point1 @param {number[]} point2 @returns {number} */
    static geographic_to_distance(point1, point2) {
        // distance along the surface of the earth from source point to destination point, great circle (shortest distance)
        // haversine formula
        let latitude1 = point1[0] * util.DEGREES_TO_RADIANS
        let longitude1 = point1[1] * util.DEGREES_TO_RADIANS
        let latitude2 = point2[0] * util.DEGREES_TO_RADIANS
        let longitude2 = point2[1] * util.DEGREES_TO_RADIANS
        let differenceLatitude = latitude2 - latitude1
        let differenceLongitude = longitude2 - longitude1
        let a = Math.sin(differenceLatitude / 2) ** 2 + Math.cos(latitude1) * Math.cos(latitude2) * Math.sin(differenceLongitude / 2) ** 2
        let c = 2 * Math.atan2(a ** 0.5, (1 - a) ** 0.5)
        let distance = util.SPHERE_RADIUS * c
        return distance
    }
    /** @param {number[]} point @param {number[]} pointStart @param {number[]} pointEnd @returns {number} */
    static geographic_to_distance_offset(point, pointStart, pointEnd) { // inaccurate
        // distance of a point from a great-circle path (sometimes called cross track error)
        let angularDistance = util.geographic_to_distance(pointStart, point) / util.SPHERE_RADIUS
        let theta1 = util.geographic_to_azimuth(pointStart, point) * util.DEGREES_TO_RADIANS
        let theta2 = util.geographic_to_azimuth(pointStart, pointEnd) * util.DEGREES_TO_RADIANS
        let aa = Math.asin(Math.sin(angularDistance) * Math.sin(theta1 - theta2))
        return aa * util.SPHERE_RADIUS
    }
    /** @param {number[]} point1 @param {number[]} point2 @returns {number} */
    static geographic_to_distance_rhumb(point1, point2) {
        // distance traveling from starting point to destination point along a rhumb line
        let latitude1 = point1[0] * util.DEGREES_TO_RADIANS
        let longitude1 = point1[1] * util.DEGREES_TO_RADIANS
        let latitude2 = point2[0] * util.DEGREES_TO_RADIANS
        let longitude2 = point2[1] * util.DEGREES_TO_RADIANS
        let differenceLatitude = latitude2 - latitude1
        let differenceLongitude = longitude2 - longitude1
        if (Math.abs(differenceLongitude) > Math.PI) {
            differenceLongitude = differenceLongitude > 0 ? -(2 * Math.PI - differenceLongitude) : (2 * Math.PI + differenceLongitude)
        }
        let aa = Math.log(Math.tan(latitude2 / 2 + Math.PI / 4) / Math.tan(latitude1 / 2 + Math.PI / 4))
        let stretchFactor = Math.abs(aa) > 10e-12 ? differenceLatitude / aa : Math.cos(latitude1)
        let angularDistance = (differenceLatitude * differenceLatitude + stretchFactor * stretchFactor * differenceLongitude * differenceLongitude) ** 0.5
        let distance = angularDistance * util.SPHERE_RADIUS
        return distance
    }
    /** @param {number[]} point1 @param {number[]} point2 @returns {number} */
    static geographic_to_elevation(point1, point2) { // inaccurate
        let [x1, y1, z1] = util.geographic_to_cartesian(point1[0], point1[1], point1[2])
        let [x2, y2, z2] = util.geographic_to_cartesian(point2[0], point2[1], point2[2])
        let dx = x2 - x1
        let dy = y2 - y1
        let dz = z2 - z1
        let distance = (dx ** 2 + dy ** 2 + dz ** 2) ** 0.5
        let vx = dx / distance
        let vy = dy / distance
        let vz = dz / distance
        let elevation = 90.0 - (180.0 / Math.PI) * Math.acos(vx * x1 + vy * y1 + vz * z1)
        return elevation
    }
    /** @param {number[]} point1 @param {number[]} point2 @param {number} fractionOfDistance @returns {number[]} */
    static geographic_to_intermediate_point(point1, point2, fractionOfDistance = 0.5) {
        let distance = util.geographic_to_distance(point1, point2)
        let latitude1 = point1[0] * util.DEGREES_TO_RADIANS
        let longitude1 = point1[1] * util.DEGREES_TO_RADIANS
        let latitude2 = point2[0] * util.DEGREES_TO_RADIANS
        let longitude2 = point2[1] * util.DEGREES_TO_RADIANS
        let a = Math.sin((1 - fractionOfDistance) * distance) / Math.sin(distance)
        let b = Math.sin(fractionOfDistance * distance) / Math.sin(distance)
        let x = a * Math.cos(latitude1) * Math.cos(longitude1) + b * Math.cos(latitude2) * Math.cos(longitude2)
        let y = a * Math.cos(latitude1) * Math.sin(longitude1) + b * Math.cos(latitude2) * Math.sin(longitude2)
        let z = a * Math.sin(latitude1) + b * Math.sin(latitude2)
        let latitude = Math.atan2(z, (x ** 2 + y ** 2) ** 0.5) * util.RADIANS_TO_DEGREES
        let longitude = Math.atan2(y, x) * util.RADIANS_TO_DEGREES
        return [latitude, longitude]
    }
    /** @param {number[]} point1 @param {number} azimuth1 @param {number[]} point2 @param {number} azimuth2 @returns {number[]|null} */
    static geographic_to_intersection_point(point1, azimuth1, point2, azimuth2) {
        // point of intersection of two paths defined by point and bearing
        let latitude1 = point1[0] * util.DEGREES_TO_RADIANS
        let longitude1 = point1[1] * util.DEGREES_TO_RADIANS
        let latitude2 = point2[0] * util.DEGREES_TO_RADIANS
        let longitude2 = point2[1] * util.DEGREES_TO_RADIANS
        let differenceLatitude = latitude2 - latitude1
        let differenceLongitude = longitude2 - longitude1
        let theta1 = azimuth1 * util.DEGREES_TO_RADIANS
        let theta2 = azimuth2 * util.DEGREES_TO_RADIANS
        let angularDistance = 2 * Math.asin(Math.sqrt(Math.sin(differenceLatitude / 2) * Math.sin(differenceLatitude / 2) + Math.cos(latitude1) * Math.cos(latitude2) * Math.sin(differenceLongitude / 2) * Math.sin(differenceLongitude / 2)))
        if (Math.abs(angularDistance) < Number.EPSILON) {
            return [point1[0], point1[1]]
        }
        let initialAzimuth = (Math.sin(latitude2) - Math.sin(latitude1) * Math.cos(angularDistance)) / (Math.sin(angularDistance) * Math.cos(latitude1))
        let finalAzimuth = (Math.sin(latitude1) - Math.sin(latitude2) * Math.cos(angularDistance)) / (Math.sin(angularDistance) * Math.cos(latitude2))
        initialAzimuth = Math.acos(Math.min(Math.max(initialAzimuth, -1), 1))
        finalAzimuth = Math.acos(Math.min(Math.max(finalAzimuth, -1), 1))
        let initialTheta = Math.sin(longitude2 - longitude1) > 0 ? initialAzimuth : 2 * Math.PI - initialAzimuth
        let finalTheta = Math.sin(longitude2 - longitude1) > 0 ? 2 * Math.PI - finalAzimuth : finalAzimuth
        let angle1 = theta1 - initialTheta
        let angle2 = finalTheta - theta2
        if (Math.sin(angle1) == 0 && Math.sin(angle2) == 0) {
            return null
        }
        if (Math.sin(angle1) * Math.sin(angle2) < 0) {
            return null
        }
        let aa = -Math.cos(angle1) * Math.cos(angle2) + Math.sin(angle1) * Math.sin(angle2) * Math.cos(angularDistance)
        let bb = Math.atan2(Math.sin(angularDistance) * Math.sin(angle1) * Math.sin(angle2), Math.cos(angle2) + Math.cos(angle1) * aa)
        let destinationLatitude = Math.asin(Math.min(Math.max(Math.sin(latitude1) * Math.cos(bb) + Math.cos(latitude1) * Math.sin(bb) * Math.cos(theta1), -1), 1))
        let cc = Math.atan2(Math.sin(theta1) * Math.sin(bb) * Math.cos(latitude1), Math.cos(bb) - Math.sin(latitude1) * Math.sin(destinationLatitude))
        let destinationLongitude = longitude1 + cc
        destinationLatitude *= util.RADIANS_TO_DEGREES
        destinationLongitude *= util.RADIANS_TO_DEGREES
        return [destinationLatitude, destinationLongitude]
    }
    /** @param {number[]} point1 @param {number[]} point2 @returns {number[]} */
    static geographic_to_midpoint(point1, point2) {
        let latitude1 = point1[0] * util.DEGREES_TO_RADIANS
        let longitude1 = point1[1] * util.DEGREES_TO_RADIANS
        let latitude2 = point2[0] * util.DEGREES_TO_RADIANS
        let longitude2 = point2[1] * util.DEGREES_TO_RADIANS
        let differenceLatitude = latitude2 - latitude1
        let differenceLongitude = longitude2 - longitude1
        let bx = Math.cos(latitude2) * Math.cos(differenceLatitude)
        let by = Math.cos(latitude2) * Math.sin(differenceLatitude)
        let latitude = Math.atan2(Math.sin(latitude1) + Math.sin(latitude2), ((Math.cos(latitude1) + bx) ** 2 + by ** 2) ** 0.5) * util.RADIANS_TO_DEGREES
        let longitude = point1[1] + (Math.atan2(by, Math.cos(longitude1) + bx) * util.RADIANS_TO_DEGREES)
        return [latitude, longitude]
    }
    /** @param {number} latitude @param {number} longitude @param {number} altitude @returns {number[]} */
    static geographic_to_spherical(latitude, longitude, altitude) {
        let r = util.SPHERE_RADIUS + altitude
        let theta = (longitude >= 0 ? longitude : 360 + longitude) * util.DEGREES_TO_RADIANS
        let phi = (90 - latitude) * util.DEGREES_TO_RADIANS
        return [r, theta, phi]
    }
    // h
    /** @param {string} string @param {boolean} raw @returns {string} */
    static hash_md5(string, raw = false) {
        let hc = "0123456789abcdef"
        function rh(n) { let j, s = ""; for (j = 0; j <= 3; j++) s += hc.charAt((n >> (j * 8 + 4)) & 0x0F) + hc.charAt((n >> (j * 8)) & 0x0F); return s }
        function ad(x, y) { let l = (x & 0xFFFF) + (y & 0xFFFF); let m = (x >> 16) + (y >> 16) + (l >> 16); return (m << 16) | (l & 0xFFFF) }
        function rl(n, c) { return (n << c) | (n >>> (32 - c)) }
        function cm(q, a, b, x, s, t) { return ad(rl(ad(ad(a, q), ad(x, t)), s), b) }
        function ff(a, b, c, d, x, s, t) { return cm((b & c) | ((~b) & d), a, b, x, s, t) }
        function gg(a, b, c, d, x, s, t) { return cm((b & d) | (c & (~d)), a, b, x, s, t) }
        function hh(a, b, c, d, x, s, t) { return cm(b ^ c ^ d, a, b, x, s, t) }
        function ii(a, b, c, d, x, s, t) { return cm(c ^ (b | (~d)), a, b, x, s, t) }
        function sb(x) {
            let i; let nblk = ((x.length + 8) >> 6) + 1; let blks = new Array(nblk * 16); for (i = 0; i < nblk * 16; i++) blks[i] = 0
            for (i = 0; i < x.length; i++) blks[i >> 2] |= x.charCodeAt(i) << ((i % 4) * 8)
            blks[i >> 2] |= 0x80 << ((i % 4) * 8); blks[nblk * 16 - 2] = x.length * 8; return blks
        }
        let i, x = sb(string), a = 1732584193, b = -271733879, c = -1732584194, d = 271733878, olda, oldb, oldc, oldd
        for (i = 0; i < x.length; i += 16) {
            olda = a; oldb = b; oldc = c; oldd = d
            a = ff(a, b, c, d, x[i + 0], 7, -680876936); d = ff(d, a, b, c, x[i + 1], 12, -389564586); c = ff(c, d, a, b, x[i + 2], 17, 606105819)
            b = ff(b, c, d, a, x[i + 3], 22, -1044525330); a = ff(a, b, c, d, x[i + 4], 7, -176418897); d = ff(d, a, b, c, x[i + 5], 12, 1200080426)
            c = ff(c, d, a, b, x[i + 6], 17, -1473231341); b = ff(b, c, d, a, x[i + 7], 22, -45705983); a = ff(a, b, c, d, x[i + 8], 7, 1770035416)
            d = ff(d, a, b, c, x[i + 9], 12, -1958414417); c = ff(c, d, a, b, x[i + 10], 17, -42063); b = ff(b, c, d, a, x[i + 11], 22, -1990404162)
            a = ff(a, b, c, d, x[i + 12], 7, 1804603682); d = ff(d, a, b, c, x[i + 13], 12, -40341101); c = ff(c, d, a, b, x[i + 14], 17, -1502002290)
            b = ff(b, c, d, a, x[i + 15], 22, 1236535329); a = gg(a, b, c, d, x[i + 1], 5, -165796510); d = gg(d, a, b, c, x[i + 6], 9, -1069501632)
            c = gg(c, d, a, b, x[i + 11], 14, 643717713); b = gg(b, c, d, a, x[i + 0], 20, -373897302); a = gg(a, b, c, d, x[i + 5], 5, -701558691)
            d = gg(d, a, b, c, x[i + 10], 9, 38016083); c = gg(c, d, a, b, x[i + 15], 14, -660478335); b = gg(b, c, d, a, x[i + 4], 20, -405537848)
            a = gg(a, b, c, d, x[i + 9], 5, 568446438); d = gg(d, a, b, c, x[i + 14], 9, -1019803690); c = gg(c, d, a, b, x[i + 3], 14, -187363961)
            b = gg(b, c, d, a, x[i + 8], 20, 1163531501); a = gg(a, b, c, d, x[i + 13], 5, -1444681467); d = gg(d, a, b, c, x[i + 2], 9, -51403784)
            c = gg(c, d, a, b, x[i + 7], 14, 1735328473); b = gg(b, c, d, a, x[i + 12], 20, -1926607734); a = hh(a, b, c, d, x[i + 5], 4, -378558)
            d = hh(d, a, b, c, x[i + 8], 11, -2022574463); c = hh(c, d, a, b, x[i + 11], 16, 1839030562); b = hh(b, c, d, a, x[i + 14], 23, -35309556)
            a = hh(a, b, c, d, x[i + 1], 4, -1530992060); d = hh(d, a, b, c, x[i + 4], 11, 1272893353); c = hh(c, d, a, b, x[i + 7], 16, -155497632)
            b = hh(b, c, d, a, x[i + 10], 23, -1094730640); a = hh(a, b, c, d, x[i + 13], 4, 681279174); d = hh(d, a, b, c, x[i + 0], 11, -358537222)
            c = hh(c, d, a, b, x[i + 3], 16, -722521979); b = hh(b, c, d, a, x[i + 6], 23, 76029189); a = hh(a, b, c, d, x[i + 9], 4, -640364487)
            d = hh(d, a, b, c, x[i + 12], 11, -421815835); c = hh(c, d, a, b, x[i + 15], 16, 530742520); b = hh(b, c, d, a, x[i + 2], 23, -995338651)
            a = ii(a, b, c, d, x[i + 0], 6, -198630844); d = ii(d, a, b, c, x[i + 7], 10, 1126891415); c = ii(c, d, a, b, x[i + 14], 15, -1416354905)
            b = ii(b, c, d, a, x[i + 5], 21, -57434055); a = ii(a, b, c, d, x[i + 12], 6, 1700485571); d = ii(d, a, b, c, x[i + 3], 10, -1894986606)
            c = ii(c, d, a, b, x[i + 10], 15, -1051523); b = ii(b, c, d, a, x[i + 1], 21, -2054922799); a = ii(a, b, c, d, x[i + 8], 6, 1873313359)
            d = ii(d, a, b, c, x[i + 15], 10, -30611744); c = ii(c, d, a, b, x[i + 6], 15, -1560198380); b = ii(b, c, d, a, x[i + 13], 21, 1309151649)
            a = ii(a, b, c, d, x[i + 4], 6, -145523070); d = ii(d, a, b, c, x[i + 11], 10, -1120210379); c = ii(c, d, a, b, x[i + 2], 15, 718787259)
            b = ii(b, c, d, a, x[i + 9], 21, -343485551); a = ad(a, olda); b = ad(b, oldb); c = ad(c, oldc); d = ad(d, oldd)
        }
        return rh(a) + rh(b) + rh(c) + rh(d)
    }
    /** @param {string} value @returns {String} */
    static hex_to_rgb(value) {
        let start = value.includes('#') ? 1 : 0
        let rgb = []
        for (let i = start; i < start + 6; i += 2) {
            let hex = value.slice(i, i + 2)
            rgb.append(util.hex2dec(hex))
        }
        return `rgb(${rgb[0]}, ${rgb[1]}, ${rgb[2]})`
    }
    /** @param {string} value @returns {Document} */
    static html_decode(value) {
        let parser = new DOMParser()
        return parser.parseFromString(value, 'text/html')
    }
    /** @param {Document} value @returns {string} */
    static html_encode(value) {
        return `${value}`
    }
    /** @param {string} value @returns {string} */
    static html_entity_encode(value) {
        if (!util.istype(value, 'string')) return console.error(`TypeError: `, value)
        for (let [character, name] of enumerate(util.CHARACTER_ENTITIES)) {
            value = value.replaceAll(character, name)
        }
        return value
    }
    /** @param {string} value @returns {string} */
    static html_entity_decode(value) {
        if (!util.istype(value, 'string')) return console.error(`TypeError: `, value)
        for (let [character, name] of enumerate(util.CHARACTER_ENTITIES)) {
            value = value.replaceAll(name, character)
        }
        return value
    }
    // i
    /** @param {string} value @returns {string} */
    static identifier(value) {
        if (value) {
            if (!util.istype(value, 'string')) return console.error(`variable-name=value variable-value=${value} variable-type=${type(value)} type=string`)
            let nString = ''
            let allowedCharacters = '- 0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z _ a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
            let notAllowedFirstCharacters = '0 1 2 3 4 5 6 7 8 9'.split(' ')
            for (let i = 0; i < value.length; i++) {
                let character = value[i]
                if (i == 0 && notAllowedFirstCharacters.includes(character)) {
                    nString += '_' + character
                }
                else if (!allowedCharacters.includes(character)) {
                    nString += '_'
                }
                else {
                    nString += character
                }
            }
            return nString.lower()
        } else {
            // ULID: 128-bit | 16-characters
            // GUID: 128-bit util.dec2hex(util.timestamp())
            let allowedFirstCharacters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
            let allowedCharacters = '0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
            let identifier = ''
            identifier += util.random(allowedFirstCharacters)
            for (let i = 0; i < 9; i++) {
                identifier += util.random(allowedCharacters)
            }
            return identifier
        }
    }
    // j
    /** @param {object} object @returns {string} */
    static json_encode(object) {
        return JSON.stringify(object)
    }
    /** @param {string} string @returns {object} */
    static json_decode(string) {
        return JSON.parse(string)
    }
    // k
    // l
    /** @param {string} value @returns {number} */
    static len(value, base = 1) {
        return Number(value.length / base)
    }
    // m
    /** @param {number[][]} matrix1 @param {number[][]} matrix2 @returns {number[][]} */
    static matrix_addition(matrix1, matrix2) {
        if (!util.istype(matrix1, 'array')) return console.error('TypeError: ', matrix1)
        if (!util.istype(matrix2, 'array')) return console.error('TypeError: ', matrix2)
        if (matrix1.length != matrix2.length) return console.error(`ArrayLengthError: variable-name=matrix2 variable-length=${matrix2.length} length=eq${matrix1.length}`)
        let rows = matrix1.length
        let columns = matrix1[0].length
        let nMatrix = new Array(rows).fill(new Array(columns).fill(0))
        for (let i = 0; i < rows; i++) {
            for (let j = 0; j < columns; j++) {
                nMatrix[i][j] = matrix1[i][j] + matrix2[i][j]
            }
        }
        return nMatrix
    }
    /** @param {number[][]} matrix1 @param {number[][]} matrix2 @returns {number[][]} */
    static matrix_combination(matrix1, matrix2) {
        if (!util.istype(matrix1, 'array')) return console.error('TypeError: ', matrix1)
        if (!util.istype(matrix2, 'array')) return console.error('TypeError: ', matrix2)
        if (matrix1.length != matrix2.length) return console.error(`ArrayLengthError: variable-name=matrix2 variable-length=${matrix2.length} length=eq${matrix1.length}`)
        let rows = matrix1.length
        let columns = matrix1[0].length
        let nMatrix = new Array(rows).fill(new Array(columns).fill(0))
        return nMatrix
    }
    /** @param {number[][]} matrix1 @param {number[][]} matrix2 @returns {number[][]} */
    static matrix_multiplication(matrix1, matrix2) {
        if (!util.istype(matrix1, 'array')) return console.error('TypeError: ', matrix1)
        if (!util.istype(matrix2, 'array')) return console.error('TypeError: ', matrix2)
        if (matrix1.length != matrix2.length) return console.error(`ArrayLengthError: variable-name=matrix2 variable-length=${matrix2.length} length=eq${matrix1.length}`)
        let rows = matrix1.length
        let columns = matrix1[0].length
        let nMatrix = new Array(rows).fill(new Array(columns).fill(0))
        for (let i = 0; i < rows; i++) {
            let row = new Array(columns).fill(0)
            for (let j = 0; j < columns; j++) {
                for (let k = 0; k < columns; k++) {
                    row[k] += matrix1[i][j] * matrix2[j][k]
                }
            }
            nMatrix[i] = row
        }
        return nMatrix
    }
    /** @param {number[][]} matrix1 @param {number[][]} matrix2 @returns {number[][]} */
    static matrix_subtraction(matrix1, matrix2) {
        if (!util.istype(matrix1, 'array')) return console.error('TypeError: ', matrix1)
        if (!util.istype(matrix2, 'array')) return console.error('TypeError: ', matrix2)
        if (matrix1.length != matrix2.length) return console.error(`ArrayLengthError: variable-name=matrix2 variable-length=${matrix2.length} length=eq${matrix1.length}`)
        let rows = matrix1.length
        let columns = matrix1[0].length
        let nMatrix = new Array(rows).fill(new Array(columns).fill(0))
        for (let i = 0; i < rows; i++) {
            for (let j = 0; j < columns; j++) {
                nMatrix[i][j] = matrix1[i][j] - matrix2[i][j]
            }
        }
        return nMatrix
    }
    // n
    
    // o

    // p
    /** @param {string} path @param {string} option @returns {Object|string} */
    static path_info(path = null, option = null) {
        if (!path && window) {
            path = window.location.pathname
        }
        if (!util.istype(path, 'string')) return console.error(`TypeError: `, path)
        let delimiter = path.includes('/') ? '/' : '\\'
        let value = {
            'dirname': path.includes(delimiter) ? path.slice(0, path.lastIndexOf(delimiter)) : null,
            'basename': path.includes(delimiter) ? path.slice(path.lastIndexOf(delimiter) + 1) : null,
            'extension': path.includes('.') ? path.slice(path.lastIndexOf('.') + 1) : null,
            'filename': path.includes(delimiter) && path.includes('.') ? path.slice(path.lastIndexOf(delimiter) + 1, path.lastIndexOf('.')) : null
        }
        if (!option) return value
        return value[option]
    }
    /** @param {number} r @param {number} theta @returns {number[]} */
    static polar_to_cartesian(r, theta) {
        let x = r * Math.cos(theta)
        let y = r * Math.sin(theta)
        return [x, y]
    }
    // q

    // r
    /** @param {number} radians @returns {number} */
    static radians_to_degrees(radians) {
        return radians * util.RADIANS_TO_DEGREES
    }
    /** @param {...number} values @returns {number} */
    static random(...values) {
        // includes lowest and highest
        if (util.istype(values[0], 'array')) {
            return values[0][Math.floor(Math.random() * values[0].length)]
        }
        let range = values.length == 1 ? [0, values[0] + 1] : [values[0], values[1] + 1]
        let random_number = Math.floor(Math.random() * (range[1] - range[0])) + range[0]
        if (values.length == 3) {
            return Math.floor(random_number / values[2]) * values[2]
        }
        return random_number
    }
    static range(aValue, bValue, interval = 1) {
        let array = []
        let start = 0
        let end = typeof aValue === 'object' ? aValue.length : aValue
        if (bValue != undefined) {
            start = typeof aValue === 'object' ? aValue.length : aValue
            end = typeof bValue === 'object' ? bValue.length : bValue
        }
        for (let i = start; i < end; i += interval) {
            array.push(i)
        }
        return array
    }
    static reference_encode(object) {

    }
    static reference_decode(string) {
        if (!util.istype(string, 'string')) return console.error(`TypeError: `, string)
        if (string == '') return console.error(`TypeError: `, string)
        // keys
        let key_name = 'name:'
        let key_title = 'title:'
        let key_subtitle = 'subtitle:'
        let key_reference = 'reference:'
        let key_table = 'table:'
        let cell_delimiter = '     '
        // template
        let reference = {
            'name': '',
            'title': '',
            'subtitle': '',
            'references': [],
            'tables': [],
        }
        let tables = []
        let table = null
        let lines = string.replaceAll('\r', '').split('\n')
        for (let i = 0; i < lines.length; i++) {
            let line = lines[i]
            // deprecated
            if (i == 0 && line.slice(0, 2) == '//') {
                reference['title'] = line.replace('//', '').trim()
            }
            // deprecated
            if (i == 1 && line.slice(0, 2) == '//') {
                reference['references'] = line.replace('//', '').trim().split(', ')
            }
            if (line.indexOf(key_name) == 0) {
                reference['name'] = line.replace(key_name, '').trim()
            }
            if (line.indexOf(key_title) == 0) {
                reference['title'] = line.replace(key_title, '').trim()
            }
            if (line.indexOf(key_subtitle) == 0) {
                reference['subtitle'] = line.replace(key_subtitle, '').trim()
            }
            if (line.indexOf(key_reference) == 0) {
                let data = line.replace(key_reference, '').trim()
                reference['reference'] = data == '' ? [] : data.split(', ')
            }
            if (line.indexOf(key_table) == 0) {
                let header_string = lines[i + 1].trim()
                table = {
                    'name': lines[i].replace(key_table, '').trim(),
                    'headers': header_string.split(cell_delimiter).map((string) => string.trim()).filter(string => string.length > 0),
                    'rows': [],
                    'header_string': header_string
                }
                i += 1
                continue
            }
            if (table) {
                if (line == '' || i == lines.length - 1) {
                    delete table['header_string']
                    tables.push(util.clone(table))
                    table = null
                    continue
                }
                let row = new Array(table['headers'].length).fill('')
                for (let string of lines[i].split(cell_delimiter).map((string) => string.trim()).filter(string => string.length > 0)) {
                    for (let j = 0; j < table['headers'].length; j++) {
                        if (table['header_string'].indexOf(table['headers'][j]) == lines[i].indexOf(string)) {
                            row[j] = string
                        }
                    }
                }
                table['rows'].push(row)
            }

        }
        reference['tables'] = tables
        return reference
    }
    /** @param {string|RegExp} pattern @param {string} value @returns {boolean} */
    static regular_expression_match(pattern, value) {
        return new RegExp(pattern).test(value)
    }
    /** @param {string} string @returns {string} */
    static rgb2hex(value) {
        let hexadecimal = ''
        if (util.istype(value, 'array-number|array-string-number')) {
            if (value.length == 3) {
                let [red, green, blue] = value
                red = Number(red)
                hexadecimal += util.dec2hex(red, 2)
                green = Number(green)
                hexadecimal += util.dec2hex(green, 2)
                blue = Number(blue)
                hexadecimal += util.dec2hex(blue, 2)
            }
            else if (value.length == 4) {
                let [red, green, blue, alpha] = value
                red = Number(red)
                hexadecimal += util.dec2hex(red, 2)
                green = Number(green)
                hexadecimal += util.dec2hex(green, 2)
                blue = Number(blue)
                hexadecimal += util.dec2hex(blue, 2)
                alpha = Number(alpha)
                alpha *= 255
                alpha = Math.round(alpha)
                hexadecimal += util.dec2hex(alpha, 2)
            } else {
                return console.error(`StringLengthError: variable-name=value variable-length=${value.length} length=eq3|eq4`)
            }
        }
        if (util.istype(value, 'string')) {
            value = value.strip(' ')
            if (util.regular_expression_match(/^rgb\(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]), ([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]), ([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\)$/, value)) {
                let [red, green, blue] = value.split(', ')
                red = Number(red.slice(4))
                hexadecimal += util.dec2hex(red, 2)
                green = Number(green)
                hexadecimal += util.dec2hex(green, 2)
                blue = Number(blue.slice(0, -1))
                hexadecimal += util.dec2hex(blue, 2)
            }
            else if (util.regular_expression_match(/^rgba\(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]), ([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]), ([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]), (0(.\d+)?|1)\)$/, value)) {
                let [red, green, blue, alpha] = value.split(', ')
                red = Number(red.slice(5))
                hexadecimal += util.dec2hex(red, 2)
                green = Number(green)
                hexadecimal += util.dec2hex(green, 2)
                blue = Number(blue)
                hexadecimal += util.dec2hex(blue, 2)
                alpha = Number(alpha.slice(0, -1))
                alpha *= 255
                alpha = Math.round(alpha)
                hexadecimal += util.dec2hex(alpha, 2)
            }
            else {
                return console.error(`ValueError: variable-name=value variable-value=${value}`)
            }
        }
        return `#${hexadecimal}`
    }
    /** @param {number} number @param {number} nDigits @returns {number} */
    static round(number, nDigits) {
        let multiplier = Math.pow(10, nDigits)
        return Math.round(number * multiplier) / multiplier
    }
    // s
    /** @param {string} string @returns {string} */
    static slashes_add(string) {
        if (!util.istype(string, 'string')) return console.error(`TypeError: `, string)
        return string.replaceAll('\'', "\\'").replaceAll('\"', '\\"').replaceAll('null', '\\null')
    }
    /** @param {number[]} point1 @param {number[]} point2 @returns {number} */
    static spherical_to_azimuth(point1, point2 = null) {
        
    }
    /** @param {number} r @param {number} theta @param {number} phi @returns {number[]} */
    static spherical_to_cartesian(r, theta, phi) {
        let x = r * Math.sin(phi) * Math.cos(theta)
        let y = r * Math.sin(phi) * Math.sin(theta)
        let z = r * Math.cos(phi)
        return [x, y, z]
    }
    /** @param {number} r @param {number} theta @param {number} phi @returns {number[]} */
    static spherical_to_geographic(r, theta, phi) {
        let latitude = 90 - (phi * util.RADIANS_TO_DEGREES)
        let longitude = theta * util.RADIANS_TO_DEGREES
        longitude = longitude > 180 ? longitude - 360 : longitude
        let altitude = r - util.SPHERE_RADIUS
        return [latitude, longitude, altitude]
    }
    /** @param {string} string @returns {string} */
    static slashes_remove(string) {
        if (!util.istype(string, 'string')) return console.error(`TypeError: `, string)
        return string.replaceAll("\\'", '\'').replaceAll('\\"', '\"').replaceAll('\\null', 'null')
    }
    /** @param {number[]} numbers @returns {number} */
    static statistics_aggregate(numbers, operation) {
        if (operation == 'average') {
            return util.statistics_mean(numbers)
        }
        if (operation == 'count') {
            return util.statistics_count(numbers)
        }
        if (operation == 'maximum') {
            return util.statistics_maximum(numbers)
        }
        if (operation == 'median') {
            return util.statistics_median(numbers)
        }
        if (operation == 'minimum') {
            return util.statistics_minimum(numbers)
        }
        if (operation == 'mode') {
            return util.statistics_mode(numbers)
        }
        if (operation == 'range') {
            return util.statistics_range(numbers)
        }
        if (operation == 'standard deviation' || operation == 'stddev') {
            return util.statistics_standard_deviation(numbers)
        }
        if (operation == 'sum') {
            return util.statistics_sum(numbers)
        }
        if (operation == 'variation' || operation == 'var') {
            return util.statistics_variation(numbers)
        }
    }
    /** @param {number[]} numbers1 @param {number[]} numbers2 @returns {number} */
    static statistics_correlation_coefficient(numbers1, numbers2) {
        if (numbers1.length !== numbers2.length) {
            return console.error(`ArrayLengthError: variable-name=numbers2 variable-length=${numbers2.length} length=eq${numbers1.length}\nLists must have the same length.`)
        }
        let xMean = util.statisticsMean(numbers1);
        let yMean = util.statisticsMean(numbers2);
        let xStandardDeviation = util.statisticsStandardDeviation(numbers1);
        let yStandardDeviation = util.statisticsStandardDeviation(numbers2);
        if (xStandardDeviation === 0 || yStandardDeviation === 0) {
            return 0.0;
        }
        let zScores1 = numbers1.map(number => (number - xMean) / xStandardDeviation);
        let zScores2 = numbers2.map(number => (number - yMean) / yStandardDeviation);
        let zScoresProduct = zScores1.map((zScore1, index) => zScore1 * zScores2[index]);
        let zScoreSum = util.statisticsSum(zScoresProduct);
        return (1 / (numbers1.length - 1)) * zScoreSum;
    }
    /** @param {number[]} numbers @returns {number} */
    static statistics_correlation_matrix(numbers) {

    }
    /** @param {number[]} numbers @returns {number} */
    static statistics_count(numbers) {
        return numbers.length
    }
    /** @param {number[]} numbers @returns {number} */
    static statistics_maximum(numbers) {
        return Math.max(...numbers)
    }
    
    /** @param {number[]} numbers @returns {number} */
    static statistics_mean(numbers) {
        return util.statistics_sum(numbers) / numbers.length
    }
    /** @param {number[]} numbers @returns {number} */
    static statistics_median(numbers) {
        numbers = numbers.sort((a, b) => a - b)
        let n = numbers.length
        if (n % 2 == 0) {
            return (numbers[Math.floor(n / 2)] + numbers[Math.floor((n / 2) - 1)]) / 2
        }
        else {
            return numbers[Math.floor((n / 2) - .5)]
        }
    }
    /** @param {number[]} numbers @returns {number} */
    static statistics_minimum(numbers) {
        return Math.min(...numbers)
    }
    /** @param {number[]} numbers @returns {number} */
    static statistics_mode(numbers) {
        let frequencyCounts = {};
        let maxFrequency = 0;
        let modes = [];
        // count the occurrences of each number
        for (let number of numbers) {
            frequencyCounts[number] = (frequencyCounts[number] || 0) + 1;
            maxFrequency = Math.max(maxFrequency, frequencyCounts[number]);
        }
        // find the numbers with the maximum frequency
        for (let number in frequencyCounts) {
            if (frequencyCounts[number] == maxFrequency) {
                modes.append(number);
            }
        }
        // return number with greatest occurrence
        return modes[0];
    }
    /** @param {number[]} numbers @returns {number} */
    static statistics_range(numbers) {
        return Math.max(...numbers) - Math.min(...numbers)
    }
    /** @param {number[]} numbers @returns {number} */
    static statistics_standard_deviation(numbers) {
        return Math.sqrt(util.statistics_variation(numbers))
    }
    /** @param {number[]} numbers @returns {number} */
    static statistics_sum(numbers) {
        let sum = 0
        for (let number of numbers) {
            sum += number
        }
        return sum
    }
    /** @param {number[]} numbers @returns {number} */
    static statistics_variation(numbers) {
        let n = numbers.length
        let mean = util.statistics_mean(numbers)
        return util.statistics_sum(numbers.map((value) => (value - mean) ** 2)) / (n - 1)
    }
    // t
    /** @param {object[]} entries @param {string} orientation @param {string} delimiter @returns {string} */
    static table_encode(entries, orientation = 'vertical', delimiter = '     ') {
        if (entries == []) return ''
        let headers = []
        for (let key in entries[0]) {
            headers.append(`${key}`)
        }
        let rows = entries.map((entry) => new object(entry).values())
        if (orientation == 'vertical' || orientation == 'v') {
            let columnLengths = []
            for (let x = 0; x < headers.length; x++) {
                columnLengths.push(0)
                for (let y = 0; y < rows.length + 1; y++) {
                    let cell = y == 0 ? headers[x] : rows[y - 1][x]
                    cell = cell == null ? '' : `${cell}`
                    columnLengths[x] = cell.length > columnLengths[x] ? cell.length : columnLengths[x]
                }
            }
            let tableString = headers.map((header, index) => header.ljust(columnLengths[index], ' ')).join(delimiter)
            for (let row of rows) {
                tableString += '\n' + row.map((cell, index) => `${cell}`.ljust(columnLengths[index], ' ')).join(delimiter)
            }
            return tableString
        }
        if (orientation == 'horizontal' || orientation == 'h') {
            let columnLengths = []
            for (let x = 0; x < rows.length + 1; x++) {
                columnLengths.push(0)
                for (let y = 0; y < headers.length; y++) {
                    let cell = x == 0 ? headers[y] : rows[x - 1][y]
                    cell = cell == null ? '' : `${cell}`
                    columnLengths[x] = cell.length > columnLengths[x] ? cell.length : columnLengths[x]
                }
            }
            let tableString = ''
            for (let y = 0; y < headers.length; y++) {
                tableString += y > 0 ? '\n' : ''
                for (let x = 0; x < rows.length + 1; x++) {
                    let cell = x == 0 ? headers[y] : rows[x - 1][y]
                    cell = cell == null ? '' : cell
                    tableString += x > 0 ? delimiter : ''
                    tableString += cell.ljust(columnLengths[x], ' ')
                }
            }
            return tableString
        }

    }
    /** @deprecated @param {string} string @param {string} delimiter @returns {object[]} */
    static _table_decode(string, delimiter) {
        if (!util.istype(string, 'string')) return console.error(`TypeError: `, string)
        if (!util.istype(delimiter, 'string')) return console.error(`TypeError: `, delimiter)
        let entries = []
        function getHeadersData(string, delimiter) {
            let object = {}
            let sIndex = 0
            let dLength = delimiter.length
            let i = 0
            while (i < string.length) {
                if (i == string.length - 1) {
                    let value = string.slice(sIndex, i + 1).trim()
                    object[value] = [sIndex, -1]
                }
                if (string.slice(i, i + dLength) == delimiter && string[i + dLength] != ' ') {
                    let value = string.slice(sIndex, i + dLength - 1).trim()
                    object[value] = [sIndex, i + dLength - 1]
                    sIndex = i + dLength
                }
                i += 1
            }
            return object
        }
        let lines = string.split('\n')
        let headerData = getHeadersData(lines[0], delimiter)
        for (let i = 1; i < lines.length; i++) {
            let line = lines[i]
            let entry = {}
            for (let key in headerData) {
                let indexes = headerData[key]
                let sIndex = indexes[0]
                let eIndex = indexes[1] == -1 ? line.length : indexes[1]
                entry[key] = line.slice(sIndex, eIndex).strip(' ')
            }
            entries.append(entry)
        }
        return entries
    }
    /** @param {string} data @param {string} delimiter @returns {object[]} */
    static table_decode(data, delimiter) {
        // NOTE: each header name must be unique
        let rows = [  ]
        let lines
        if (util.istype(data, 'array-string')) {
            lines = data
        }
        if (util.istype(data, 'string')) {
            lines = data.split(/\r?\n/)
        }
        lines = lines.filter(line => line.trim().length > 0)
        let headers = lines[0].split(delimiter).filter(header => header.trim().length > 0)
        if (headers.length === 0) {
            throw new Error("Invalid table format: no headers found.")
        }
        for (let index = 1; index < lines.length; index++) {
            let cells = lines[index].split(delimiter).filter(cell => cell.trim().length > 0)
            if (cells.length !== headers.length) {
                throw new Error("Invalid table format: row has incorrect number of columns.")
            }
            let row = Object.fromEntries(headers.map((header, index) => [header, cells[index]]))
            rows.push(row)
        }
        return rows
    } 
    /** @param {Date|number|string} value @param {} option @returns {Date|number|string} */
    static timestamp(value = null, option = '') {
        function toString(date) {
            let year = date.getFullYear().toString()
            let month = (date.getMonth() + 1).toString().rjust(2, '0')
            let dayOfMonth = date.getDate().toString().rjust(2, '0')
            let hours = date.getHours().toString().rjust(2, '0')
            let minutes = date.getMinutes().toString().rjust(2, '0')
            let seconds = date.getSeconds().toString().rjust(2, '0')
            let milliseconds = date.getMilliseconds().toString().ljust(3, '0')
            return `${year}-${month}-${dayOfMonth}T${hours}:${minutes}:${seconds}.${milliseconds}`
        }
        let date = new Date() //new Date().toLocaleString("en-US", { timeZone: "UTC" })
        let offset = (new Date().getTimezoneOffset() * 60)
        if (value == 'seconds' || value == null) {
            return Math.round((date.getTime() + offset) / 1000)
        }
        if (value == 'milliseconds') {
            return date.getTime() + offset
        }
        if (value == 'object') {
            return util.timestamp(util.timestamp('milliseconds'))
        }
        if (value == 'string') {
            date = util.timestamp('object')
            return toString(date)
        }
        if (typeof value === 'number') { // return date by default
            if (value.toString().length <= 10) {
                date.setTime((value * 1000) + (offset * 1000))
            }
            if (value.toString().length == 13) {
                date.setTime(value + (offset * 1000))
            }
            if (option == 'seconds') return util.timestamp(date, 'seconds')
            if (option == 'milliseconds') return util.timestamp(date, 'milliseconds')
            if (option == 'object') return date
            if (option == 'string') return toString(date)
            return date
        }
        if (typeof value === 'object') { // return seconds by default
            if (option == 'seconds') return Math.round((value.getTime() + offset) / 1000)
            if (option == 'milliseconds') return value.getTime() + offset
            if (option == 'object') return value
            if (option == 'string') return toString(value)
            return Math.round((value.getTime() + offset) / 1000)
        }
        if (typeof value === 'string') { // return date by default
            let date_ = [0, 1, 0]
            let time_ = [0, 0, 0, 0]
            let values = value.split('T')
            if (value.includes('T')) {
                for (let [index, value] of enumerate(values[0].split('-'))) {
                    date_[index] = Number(value)
                }
                for (let [index, value] of enumerate(values[1].split(':'))) {
                    if (value.includes('.')) {
                        time_[2] = Number(value.slice(0, value.indexOf('.')))
                        time_[3] = Number(value.slice(value.indexOf('.')+1))
                    } else {
                        time_[index] = Number(value)
                    }
                }
            } else {
                for (let [index, value] of enumerate(values[0].split('-'))) {
                    date_[index] = Number(value)
                }
            }
            date.setFullYear(date_[0])
            date.setMonth(date_[1] - 1)
            date.setDate(date_[2])
            date.setHours(time_[0])
            date.setMinutes(time_[1])
            date.setSeconds(time_[2])
            date.setMilliseconds(time_[3])
            if (option == 'seconds') return util.timestamp(date, 'seconds')
            if (option == 'milliseconds') return util.timestamp(date, 'milliseconds')
            if (option == 'object') return date
            if (option == 'string') return util.timestamp(date, 'string')
            return date
        }
    }
    /** @param {Date|number|string} timestamp @returns {string} */
    static timestamp_date(timestamp) {
        timestamp = util.timestamp(timestamp, 'object')
        let year = timestamp.getFullYear().toString()
        let month = (timestamp.getMonth() + 1).toString().rjust(2, '0')
        let dayOfMonth = timestamp.getDate().toString().rjust(2, '0')
        return `${year}-${month}-${dayOfMonth}`
    }
    /** @param {Date|number|string} timestamp @param {boolean} short @returns {string} */
    static timestamp_datetime(timestamp = util.timestamp('object'), short = false) {
        return `${util.timestamp_date(timestamp)} ${util.timestamp_time(timestamp, short)}`
    }
    /** @param {Date|number|string} timestamp @param {boolean} short @returns {string} */
    static timestamp_dayofweek(timestamp, short = false) {
        timestamp = util.timestamp(timestamp, 'object')
        let dayOfWeek = util.DAYS_OF_WEEK[timestamp.getDay()]
        if (short) {
            return dayOfWeek.slice(0, 3)
        } else {
            return dayOfWeek
        }
    }
    /** @param {Date|number|string} timestamp1 @param {Date|number|string} timestamp2 @param {boolean} short @returns {string} */
    static timestamp_difference(timestamp1, timestamp2 = util.timestamp('seconds'), short = true) {
        timestamp1 = util.timestamp(timestamp1, 'seconds')
        timestamp2 = util.timestamp(timestamp2, 'seconds')
        let difference = Math.abs(timestamp2 - timestamp1)
        if (difference == 0) return 'Now'
        if (difference <= 1) return short ? '1sec': '1 second'
        if (difference <= 2) return short ? '2sec' : '2 seconds'
        if (difference <= 3) return short ? '3sec' : '3 seconds'
        if (difference <= 4) return short ? '4sec' : '4 seconds'
        if (difference <= 5) return short ? '5sec' : '5 seconds'
        if (difference <= 10) return short ? '10sec' : '10 seconds'
        if (difference <= 20) return short ? '20sec' : '20 seconds'
        if (difference <= 30) return short ? '30sec' : '30 seconds'
        if (difference <= 60) return short ? '1min' : '1 minute'
        if (difference <= 120) return short ? '2min' : '2 minutes'
        if (difference <= 180) return short ? '3min' : '3 minutes'
        if (difference <= 240) return short ? '4min' : '4 minutes'
        if (difference <= 300) return short ? '5min' : '5 minutes'
        if (difference <= 600) return short ? '10min' : '10 minutes'
        if (difference <= 1200) return short ? '20min' : '20 minutes'
        if (difference <= 1800) return short ? '30min' : '30 minutes'
        if (difference <= 3600) return short ? '1h' : '1 hour'
        if (difference <= 7200) return short ? '2h' : '2 hours'
        if (difference <= 10800) return short ? '3h' : '3 hours'
        if (difference <= 14400) return short ? '4h' : '4 hours'
        if (difference <= 18000) return short ? '5h' : '5 hours'
        if (difference <= 21600) return short ? '6h' : '6 hours'
        if (difference <= 43200) return short ? '12h' : '12 hours'
        if (difference <= 86400) return short ? '1d' : '1 day'
        if (difference <= 172800) return short ? '2d' : '2 days'
        if (difference <= 259200) return short ? '3d' : '3 days'
        if (difference <= 345600) return short ? '4d' : '4 days'
        if (difference <= 432000) return short ? '5d' : '5 days'
        if (difference <= 864000) return short ? '10d' : '10 days'
        if (difference <= 1728000) return short ? '20d' : '20 days'
        if (difference <= 2592000) return short ? '1mo' : '1 month' // 30 days
        if (difference <= 5184000) return short ? '2mo' : '2 months'
        if (difference <= 7776000) return short ? '3mo' : '3 months'
        if (difference <= 10368000) return short ? '4mo' : '4 months'
        if (difference <= 12960000) return short ? '5mo' : '5 months'
        if (difference <= 15552000) return short ? '6mo' : '6 months'
        if (difference <= 31536000) return short ? '1yr' : '1 year'
        if (difference <= 63072000) return short ? '2yr' : '2 years'
        if (difference <= 94608000) return short ? '3yr' : '3 years'
        if (difference <= 126144000) return short ? '4yr' : '4 years'
        if (difference <= 157680000) return short ? '5yr' : '5 years'
        if (difference <= 315360000) return short ? '10yr' : '10 years'
    }
    /** @param {Date|number|string} timestamp @returns {string} */
    static timestamp_hours(timestamp) {
        timestamp = util.timestamp(timestamp, 'object')
        return timestamp.getHours().toString().rjust(2, '0')
    }
    /** @param {Date|number|string} timestamp @returns {string} */
    static timestamp_minutes(timestamp) {
        timestamp = util.timestamp(timestamp, 'object')
        return timestamp.getMinutes().toString().rjust(2, '0')
    }
    /** @param {Date|number|string} timestamp @param {boolean} short @returns {string} */
    static timestamp_month(timestamp, short = false) {
        timestamp = util.timestamp(timestamp, 'object')
        let month = util.MONTHS[timestamp.getMonth()]
        if (short) {
            return month.slice(0, 3)
        } else {
            return month
        }
    }
    /** @param {Date|number|string} timestamp @param {boolean} short @returns {string} */
    static timestamp_quarter(timestamp, short = false) {
        timestamp = util.timestamp(timestamp, 'object')
        let quarter = Math.ceil((timestamp.getMonth() + 1) / 3)
        return short ? `Q${quarter}` : util.QUARTERS[quarter-1]
    }
    /** @param {Date|number|string} timestamp @returns {string} */
    static timestamp_seconds(timestamp) {
        timestamp = util.timestamp(timestamp, 'object')
        return timestamp.getSeconds().toString().rjust(2, '0')
    }
    /** @param {Date|number|string} timestamp @param {boolean} short @returns {string} */
    static timestamp_time(timestamp, short = false) {
        timestamp = util.timestamp(timestamp, 'object')
        let hours = timestamp.getHours().toString().rjust(2, '0')
        let minutes = timestamp.getMinutes().toString().rjust(2, '0')
        let seconds = timestamp.getSeconds().toString().rjust(2, '0')
        let milliseconds = timestamp.getMilliseconds().toString().ljust(3, '0')
        if (short) {
            return `${hours}:${minutes}:${seconds}`
        } else {
            return `${hours}:${minutes}:${seconds}.${milliseconds}`
        }
    }
    /** @param {Date|number|string} timestamp @returns {string} */
    static timestamp_year(timestamp) {
        timestamp = util.timestamp(timestamp, 'object')
        return timestamp.getFullYear().toString()
    }
    /** @param {string} string @returns {string} */
    static title(string) {
        if (!util.istype(string, 'string')) return console.error(`TypeError: `, string)
        let uppers = [
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
        let lowers = [
            'a', 'at',
            'be',
            'for',
            'in',
            'of',
            'nor',
        ]
        let specials = [
            'ICMPv6', 'InARP', 'IPv4', 'IPv6'
        ]
        function convert(string) {
            if (string == '') return string
            if (lowers.includes(string)) return string
            if (uppers.includes(string)) return string.upper()
            for (let special of specials) {
                if (special.lower() == string) {
                    return special
                }
            }
            return string.capitalize()
        }
        return string.split('_').map((substring) => convert(substring.lower())).join(' ')
    }
    // u
    /** @param {Object} value @returns {string} */
    static uri_encode(object) {
        if (!util.istype(object, 'object')) return console.error(`TypeError: `, object)
        let uriString = ''
        return uriString
    }
    /** @param {string} relative @param {string} absolute @returns {Object} */
    static uri_decode(relative, absolute = null) {
        if (!util.istype(relative, 'string')) return console.error(`TypeError: `, relative)
        if (absolute && !util.istype(absolute, 'string')) return console.error(`TypeError: `, absolute)
        // example: http://username:password@hostname:9090/path?arg=value#anchor
        // relative path: relative-part [ ? query ] [ # fragment ] (cannot begin with '/')
        // absolute path: scheme ":" hierarchal-part [ "?" query ]
        let uriObject = {
            'scheme': null,
            'username': null,
            'password': null,
            'authority': null,
            'host': null,
            'port': null,
            'path': null,
            'query': null,
            'fragment': null,
        }
        function getFirstIndex(string, characters) {
            // get index of each character in string
            let indexes = characters.map((character) => string.find(character))
            // filter numbers less than 0
            indexes = indexes.filter((index) => index > 0)
            // sort ascending
            indexes.sort((aIndex, bIndex) => aIndex - bIndex)
            // return first number or null
            return indexes.length == 0 ? null : indexes[0]
        }
        // build target uri
        let target = null
        if (absolute != null) {
            // absolute must end with '/' and relative cannot start with '/'
            target = absolute + (absolute.slice(-1) == '/' ? '' : '/') + (relative[0] == '/' ? relative.slice(1, relative.length) : relative)
        }
        else {
            target = relative
        }
        let target_partial = target
        if (target.includes('://')) {
            uriObject['scheme'] = target.slice(0, target.index('://'))
            target_partial = target.slice(target.index('://') + 3, target.length)
        }
        if (target.includes('@')) {
            string = target_partial.slice(0, target_partial.index('@'))
            let strings = string.split(':')
            uriObject['username'] = strings[0]
            uriObject['password'] = strings[1]
            target_partial = target_partial.slice(target_partial.index('@') + 1, target_partial.length)
        }
        let index = getFirstIndex(target_partial, ['/', '?', '#'])
        if (index == null) {
            uriObject['authority'] = target_partial
            target_partial = ''
        }
        else {
            uriObject['authority'] = target_partial.slice(0, index)
            target_partial = target_partial.slice(index, target_partial.length)
        }
        if (uriObject['authority'].includes(':')) {
            uriObject['host'] = uriObject['authority'].slice(0, uriObject['authority'].index(':') + 1)
            uriObject['port'] = uriObject['authority'].slice(uriObject['authority'].index(':') + 1, uriObject['authority'].length)
        }
        else {
            uriObject['host'] = uriObject['authority']
        }
        if (target_partial.length > 0 && '/' == target_partial[0]) {
            let index = getFirstIndex(target_partial, ['?', '#'])
            if (index == null) {
                uriObject['path'] = target_partial
                target_partial = ''
            }
            else {
                uriObject['path'] = target_partial.slice(0, index)
                target_partial = target_partial.slice(index, target_partial.length)
            }
        }
        else {
            uriObject['path'] = '/'
        }
        if (target_partial.length > 0 && '?' == target_partial[0]) {
            target_partial = target_partial.slice(1, target_partial.length)
            let index = getFirstIndex(target_partial, ['#'])
            if (index == null) {
                uriObject['query'] = target_partial
                target_partial = ''
            }
            else {
                uriObject['query'] = target_partial.slice(0, index)
                target_partial = target_partial.slice(index, target_partial.length)
            }
        }
        else {

        }
        if (target_partial.length > 0 && '#' == target_partial[0]) {
            uriObject['fragment'] = target_partial.slice(1, target_partial.length)
        }
        else {

        }
        return uriObject
    }
    /** @param {Object} object @returns {string} */
    static uri_query_encode(object) {
        let queries = []
        for (let [queryKey, queryValue] in enumerate(object)) {
            queries.append(`${queryKey}=${queryValue}`)
        }
        return queries.join('&')
    }
    /** @param {string} string @returns {Object} */
    static uri_query_decode(string) {
        let object = {}
        if (!string.includes('=')) return object
        string = string.includes('?') ? string.slice(string.indexOf('?') + 1, string.length) : string
        for (let pair of string.split('&')) {
            let [queryKey, queryValue] = pair.split('=')
            object[queryKey] = queryValue
        }
        return object
    }
    // v
    /** @param {number} x @param {number} y @param {number} z @returns {number} */
    static volume(x, y, z) {
        if (!util.istype(x, 'number')) return console.error(`TypeError: `, x)
        if (!util.istype(y, 'number')) return console.error(`TypeError: `, y)
        if (!util.istype(z, 'number')) return console.error(`TypeError: `, z)
        return x * y * z
    }
    // w

    // x
    /** @param {string} method @param {Object} headers @param {number|Object|string} body @param {function(XMLHttpRequest): void} oncomplete @param {function(ProgressEvent): void} onprogress @returns {void} */
    static xhr(method, url, headers = {}, body = null, oncomplete = (request) => { }, onprogress = (event) => { }) {
        if (!util.istype(method, 'string')) return console.error(`TypeError: `, method)
        if (!util.istype(url, 'string')) return console.error(`TypeError: `, url)
        if (headers != null && !util.istype(headers, 'object')) return console.error(`TypeError: `, headers)
        // https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/send
        let request = new XMLHttpRequest()
        request.onreadystatechange = (event) => {
            if (request.readyState == 4) {
                if (request.status.toString()[0] != 2) {
                    console.error(request)
                }
                oncomplete(request)
            }
        }
        request.onprogress = (event) => {
            // event=ProgressEvent
            /*if (event.lengthComputable) {
                let percent = (event.loaded / event.total) * 100
            } else {
                // Unable to compute progress information since the total size is unknown
            }*/
            onprogress(event)
        }
        request.open(method, url, true)
        if (headers) {
            for (let name in headers) {
                request.setRequestHeader(name, headers[name])
            }
        }
        if (util.istype(body, 'array|object')) {
            body = util.json_encode(body)
        }
        request.send(body)
        // NOTE: send(...) body(Document | XMLHttpRequestBodyInit | null) XMLHttpRequestBodyInit(Blob | BufferSource | FormData | URLSearchParams | string)
    }
    static xhr_headers_encode(object) {

    }
    /** @param {string|XMLHttpRequest} value @returns {Object} */
    static xhr_headers_decode(value) {
        if (value instanceof XMLHttpRequest) {
            value = value.getAllResponseHeaders()
        }
        if (!util.istype(value, 'string')) return console.error(`TypeError: `, value)
        let headers = {}
        if (value.includes('\r\n')) {
            for (let pairString of value.split('\r\n')) {
                if (pairString == '') continue
                let pairValues = pairString.split(': ')
                headers[pairValues[0]] = pairValues[1]
            }
        } else if (value.includes('\n')) {
            for (let pairString of value.split('\n')) {
                if (pairString == '') continue
                let pairValues = pairString.split(': ')
                headers[pairValues[0]] = pairValues[1]
            }
        } else if (value.includes(': ')) {
            let pairValues = value.split(': ')
            headers[pairValues[0]] = pairValues[1]
        }
        return headers
    }
    /** @param {number|XMLHttpRequest} value  @returns {boolean} */
    static xhr_successful(value) {
        if (value instanceof XMLHttpRequest) {
            return value.status.toString()[0] == 2
        }
        else if (util.istype(value, 'number')) {
            return value.toString()[0] == 2
        }
        else {
            return console.error(`TypeError: `, value)
        }
    }
    // y

    // z

    // ascii functions
    // default bits per character (bpc) (size) = 8
    static _dataT_(data, datatype) {
        let types = 'bin byt cha dec hex oct str'.split(' ')
        for (let type in types) {
            if (type == datatype) continue
            method = `${datatype}2${type}`
            print(method, util[method](data))
        }
    }
    // binary
    static __len__(data, length) {
        while (true) {
            if (data.length % length == 0) {
                break
            }
            data = '0' + data
        }
        return data
    }
    /** @param {string} bin @returns {Uint8Array} */
    static bin2byt(bin) {
        if (!util.istype(bin, 'binary')) return console.error(`TypeError: `, bin)
        if (bin.length == 0) return new Uint8Array()
        bin = util.__len__(bin, 8)
        let decs = []
        for (let i = 0; i < bin.length; i += 8) {
            decs.push(util.bin2dec(bin.slice(i, i + 8)))
        }
        return new Uint8Array(decs)
    }
    /** @param {string} bin @returns {string} */
    static bin2cha(bin) {
        if (!util.istype(bin, 'binary')) return console.error(`TypeError: `, bin)
        return util.dec2cha(util.bin2dec(bin))
    }
    /** @param {string} bin @returns {number} */
    static bin2dec(bin) {
        if (!util.istype(bin, 'binary')) return console.error(`TypeError: `, bin)
        if (bin.length == 0) return 0
        return parseInt(bin, 2)
    }
    /** @param {string} bin @returns {string} */
    static bin2hex(bin) {
        if (!util.istype(bin, 'binary')) return console.error(`TypeError: `, bin)
        bin = util.__len__(bin, 4)
        let hex = ''
        for (let i = 0; i < bin.length; i += 4) {
            hex += util.dec2hex(util.bin2dec(bin.slice(i, i + 4)))
        }
        return hex
        // return util.dec2hex(util.bin2dec(bin), bin.length / 4) does not work for large numbers (exponential)
    }
    /** @param {string} bin @returns {string} */
    static bin2oct(bin) {
        if (!util.istype(bin, 'binary')) return console.error(`TypeError: `, bin)
        return util.dec2oct(util.bin2dec(bin))
    }
    /** @param {string} bin @param {number} size @returns {string} */
    static bin2str(bin, size = 8) { // 8 bpc
        if (!util.istype(bin, 'binary')) return console.error(`TypeError: `, bin)
        bin = util.__len__(bin, size)
        let str = ''
        for (let i = 0; i < bin.length; i += size) {
            str += util.dec2cha(util.bin2dec(bin.slice(i, i + size)))
        }
        return str
    }
    /** @param {string} bin @returns {boolean} */
    static bin2bol(bin) {
        if (!util.istype(bin, 'binary') || bin.length > 1) return console.error(`TypeError: `, bin)
        return bin == '1'
    }
    /** @param {string} bin @param {number} size @returns {number[]} */
    static bin2decs(bin, size = 8) {
        if (!util.istype(bin, 'binary')) return console.error(`TypeError: `, bin)
        bin = util.__len__(bin, size)
        let decs = []
        for (let i = 0; i < bin.length; i += size) {
            decs.push(util.bin2dec(bin.slice(i, i + size)))
        }
        return decs
    }
    /** @param {string} bin @returns {string} */
    static bin2hexs(bin) {
        return '0x' + util.bin2hex(bin).upper()
    }
    // byte (Uint8Array)
    /** @param {ArrayBuffer|Uint8Array} byt @returns {string} */
    static byt2bin(byt) {
        if (byt instanceof ArrayBuffer) byt = new Uint8Array(byt)
        if (!util.istype(byt, 'bytes')) return console.error(`TypeError: `, byt)
        // Int8Array range -128 to 127
        // Uint8Array range 0 to 255
        // dec 0  127  128  129  255 256
        // byt 0  127  -128 -127 -1  0
        let bin = ''
        for (let dec of byt) {
            bin += util.dec2bin(dec, 8)
        }
        return bin
    }
    /** @param {ArrayBuffer|Uint8Array} byt @returns {number} */
    static byt2dec(byt) {
        if (byt instanceof ArrayBuffer) byt = new Uint8Array(byt)
        if (!util.istype(byt, 'bytes')) return console.error(`TypeError: `, byt)
        return util.bin2dec(util.byt2bin(byt))
    }
    /** @param {ArrayBuffer|Uint8Array} byt @returns {string} */
    static byt2cha(byt) {
        if (byt instanceof ArrayBuffer) byt = new Uint8Array(byt)
        if (!util.istype(byt, 'bytes')) return console.error(`TypeError: `, byt)
        return util.bin2cha(util.byt2bin(byt))
    }
    /** @param {ArrayBuffer|Uint8Array} byt @returns {string} */
    static byt2hex(byt) {
        if (byt instanceof ArrayBuffer) byt = new Uint8Array(byt)
        if (!util.istype(byt, 'bytes')) return console.error(`TypeError: `, byt)
        let hex = ''
        for (let dec of byt) {
            hex += util.dec2hex(dec, 2)
        }
        return hex
    }
    /** @param {ArrayBuffer|Uint8Array} byt @returns {string} */
    static byt2oct(byt) {
        if (byt instanceof ArrayBuffer) byt = new Uint8Array(byt)
        if (!util.istype(byt, 'bytes')) return console.error(`TypeError: `, byt)
        return util.bin2oct(util.byt2bin(byt))
    }
    /** @param {ArrayBuffer|Uint8Array} @param {number} size @returns {string} */
    static byt2str(byt, size = 8) { // 8 bpc
        if (byt instanceof ArrayBuffer) byt = new Uint8Array(byt)
        if (!util.istype(byt, 'bytes')) return console.error(`TypeError: `, byt)
        let bin = util.byt2bin(byt)
        bin = util.__len__(bin, size)
        let str = ''
        for (let i = 0; i < bin.length; i += size) {
            str += util.bin2cha(bin.slice(i, i + size))
        }
        return str
    }
    // character
    /** @param {string} cha @returns {string} */
    static cha2bin(cha, len = null) {
        if (!util.istype(cha, 'string')) return console.error(`TypeError: `, cha)
        return util.dec2bin(util.cha2dec(cha), len)
    }
    /** @param {string} cha @returns {Uint8Array} */
    static cha2byt(cha) {
        if (!util.istype(cha, 'string')) return console.error(`TypeError: `, cha)
        return util.dec2byt(util.cha2dec(cha))
    }
    /** @param {string} cha @returns {number} */
    static cha2dec(cha) {
        if (!util.istype(cha, 'string')) return console.error(`TypeError: `, cha)
        return cha.charCodeAt(0)
    }
    /** @param {string} cha @returns {string} */
    static cha2hex(cha) {
        if (!util.istype(cha, 'string')) return console.error(`TypeError: `, cha)
        return util.dec2hex(util.cha2dec(cha))
    }
    /** @param {string} cha @returns {string} */
    static cha2oct(cha) {
        if (!util.istype(cha, 'string')) return console.error(`TypeError: `, cha)
        return util.dec2oct(util.cha2dec(cha))
    }
    /** @param {string} cha @param {number} size @returns {string} */
    static cha2str(cha, size = 8) { // 8 bpc
        if (!util.istype(cha, 'string')) return console.error(`TypeError: `, cha)
        return util.bin2str(util.cha2bin(cha), size)
    }
    // decimal
    /** @param {number} dec @param {number} len @returns {string} */
    static dec2bin(dec, len = null) {
        if (!util.istype(dec, 'number|string-number')) return console.error(`TypeError: `, dec)
        let bin = Number(dec).toString(2)
        if (len == null || len <= bin.length) return bin
        return ('0'.repeat(len - bin.length)).concat(bin)
    }
    /** @param {number} dec @returns {Uint8Array} */
    static dec2byt(dec) {
        if (!util.istype(dec, 'number|string-number')) return console.error(`TypeError: `, dec)
        return util.bin2byt(util.dec2bin(dec))
    }
    /** @param {number} dec @returns {string} */
    static dec2cha(dec) {
        if (!util.istype(dec, 'number|string-number')) return console.error(`TypeError: `, dec)
        return String.fromCharCode(Number(dec))
    }
    /** @param {number} dec @param {number} len @returns {string} */
    static dec2hex(dec, len = null) {
        if (!util.istype(dec, 'number|string-number')) return console.error(`TypeError: `, dec)
        let hex = Number(dec).toString(16)
        if (len == null || len <= hex.length) return hex
        return ('0'.repeat(len - hex.length)).concat(hex)
    }
    /** @param {number} dec @param {number} len @returns {string} */
    static dec2oct(dec, len = null) {
        if (!util.istype(dec, 'number|string-number')) return console.error(`TypeError: `, dec)
        let oct = Number(dec).toString(8)
        if (len == null || len <= oct.length) return oct
        return ('0'.repeat(len - oct.length)).concat(oct)
    }
    /** @param {number} dec @param {number} size @returns {string} */
    static dec2str(dec, size = 8) { // 8 bpc
        if (!util.istype(dec, 'number|string-number')) return console.error(`TypeError: `, dec)
        return util.bin2str(util.dec2bin(dec), size)
    }
    /** @param {number} dec @param {number} len @returns {string} */
    static decs2bin(decs, len = null) { // 8 size
        let bin = ''
        for (let dec in decs) {
            bin += util.dec2bin(dec, len)
        }
        return bin
    }
    // hexadecimal
    /** @param {string} hex @returns {string} */
    static hex2bin(hex) {
        if (!util.istype(hex, 'hexadecimal')) return console.error(`TypeError: `, hex)
        return util.dec2bin(util.hex2dec(hex), hex.length * 4)
    }
    /** @param {string} hex @returns {Uint8Array} */
    static hex2byt(hex) {
        if (!util.istype(hex, 'hexadecimal')) return console.error(`TypeError: `, hex)
        hex = util.__len__(hex, 2)
        let decs = []
        for (let i = 0; i < hex.length; i += 2) {
            decs.push(util.hex2dec(hex.slice(i, i + 2)))
        }
        return new Uint8Array(decs)
    }
    /** @param {string} hex @returns {string} */
    static hex2cha(hex) {
        if (!util.istype(hex, 'hexadecimal')) return console.error(`TypeError: `, hex)
        return util.dec2cha(util.hex2dec(hex))
    }
    /** @param {string} hex @returns {number} */
    static hex2dec(hex) {
        if (!util.istype(hex, 'hexadecimal')) return console.error(`TypeError: `, hex)
        return parseInt(hex, 16)
    }
    /** @param {string} hex @returns {string} */
    static hex2oct(hex) {
        if (!util.istype(hex, 'hexadecimal')) return console.error(`TypeError: `, hex)
        return util.dec2oct(util.hex2dec(hex))
    }
    /** @param {string} hex @returns {string} */
    static hex2str(hex, size = 8) { // 8 bpc
        if (!util.istype(hex, 'hexadecimal')) return console.error(`TypeError: `, hex)
        return util.bin2str(util.hex2bin(hex), size)
    }
    // octal
    /** @param {string} oct @param {number} len @returns {string} */
    static oct2bin(oct, len = null) {
        if (!util.istype(oct, 'octal')) return console.error(`TypeError: `, oct)
        return util.dec2bin(util.oct2dec(oct), len)
    }
    /** @param {string} oct @returns {Uint8Array} */
    static oct2byt(oct) {
        if (!util.istype(oct, 'octal')) return console.error(`TypeError: `, oct)
        return util.bin2byt(util.oct2bin(oct))
    }
    /** @param {string} oct @returns {string} */
    static oct2cha(oct) {
        if (!util.istype(oct, 'octal')) return console.error(`TypeError: `, oct)
        return util.dec2cha(util.oct2dec(oct))
    }
    /** @param {string} oct @returns {number} */
    static oct2dec(oct) {
        if (!util.istype(oct, 'octal')) return console.error(`TypeError: `, oct)
        return parseInt(oct, 8)
    }
    /** @param {string} oct @returns {string} */
    static oct2hex(oct) {
        if (!util.istype(oct, 'octal')) return console.error(`TypeError: `, oct)
        return util.dec2hex(util.oct2dec(oct))
    }
    /** @param {string} oct @param {number} size @returns {string} */
    static oct2str(oct, size = 8) { // 8 bpc
        if (!util.istype(oct, 'octal')) return console.error(`TypeError: `, oct)
        return util.bin2str(util.oct2bin(oct), size)
    }
    // string
    /** @param {string} str @param {number} size @returns {string} */
    static str2bin(str, size = 8) { // 8 bpc
        if (!util.istype(str, 'string')) return console.error(`TypeError: `, str)
        let bin = ''
        for (let dec of util.str2decs(str)) {
            bin += util.dec2bin(dec, size)
        }
        return bin
    }
    /** @param {string} str @param {number} size @returns {Uint8Array} */
    static str2byt(str, size = 8) { // 8 bpc
        if (!util.istype(str, 'string')) return console.error(`TypeError: `, str)
        return util.bin2byt(util.str2bin(str, size))
    }
    /** @param {string} str @param {number} size @returns {string} */
    static str2cha(str, size = 8) { // 8 bpc
        if (!util.istype(str, 'string')) return console.error(`TypeError: `, str)
        return util.dec2cha(util.str2dec(str))
    }
    /** @param {string} str @param {number} size @returns {number} */
    static str2dec(str, size = 8) { // 8 bpc
        if (!util.istype(str, 'string')) return console.error(`TypeError: `, str)
        return util.bin2dec(util.str2bin(str, size))
    }
    /** @param {string} str @param {number} size @returns {string} */
    static str2hex(str, size = 8) { // 8 bpc
        if (!util.istype(str, 'string')) return console.error(`TypeError: `, str)
        let hex = ''
        for (let dec of util.str2decs(str)) {
            hex += util.dec2hex(dec, size / 4)
        }
        return hex
    }
    /** @param {string} str @param {number} size @returns {string} */
    static str2oct(str, size = 8) { // 8 bpc
        if (!util.istype(str, 'string')) return console.error(`TypeError: `, str)
        return util.dec2oct(util.str2dec(str, size))
    }
    /** @param {string} str @returns {number[]} */
    static str2decs(str) {
        if (!util.istype(str, 'string')) return console.error(`TypeError: `, str)
        let decs = []
        for (let cha of str) {
            decs.push(util.cha2dec(cha))
        }
        return decs
    }
}
//_________________________________________________________________________________________________________________________________________________//
class array extends Array {
    /** @constructor */
    constructor(...values) {
        super()
        for (let value of values) {
            if (value instanceof Array | array) {
                this.append(...value)
            }
            else if (value instanceof HTMLCollection) {
                this.append(...value)
            }
            else {
                this.append(value)
            }
        }
    }
    /** @param {any[]|bytes|{string:string}|string} data @returns {array} */
    static fromdata(data) {
        let nArray = new array()
        if (!data) {
            return nArray
        }
        if (util.istype(data, 'array')) {
            nArray.append(...data)
        }
        else if (util.istype(data, 'bytes-array')) {
            nArray.append(...util.json_decode(util.byt2str(data)))
        }
        else if (util.istype(data, 'bytes-object')) {
            nArray = array.fromobject(util.json_decode(util.byt2str(data)))
        }
        else if (util.istype(data, 'object')) {
            nArray = array.fromobject(data)
        }
        else if (util.istype(data, 'string-array')) {
            nArray.append(...util.json_decode(data))
        }
        else if (util.istype(data, 'string-object')) {
            nArray = array.fromobject(util.json_decode(data))
        }
        else if (util.istype(data, 'string')) {
            nArray = array.fromstring(data)
        }
        else {
            return console.error(`TypeError: variable-name=data variable-value=${data} variable-type=${typeof data} type=array|bytes-array|bytes-object|object|string-array|string-object|string`)
        }
        return nArray
    }
    /** @param {Object<string, boolean|number|string>} object @param {string} delimiter @returns {array} */
    static fromobject(data, delimiter = ': ') {
        let nArray = new array()
        for (let [key, value] in enumerate(data)) {
            nArray.append(`${key}${delimiter}${value}`)
        }
        return nArray
    }
    /** @param {string} data @returns {array} */
    static fromstring(data) {
        let nArray = new array()
        // data = 'value'
        if (!data.includes(',') && !data.includes(':')) {
            for (let substring of data.strip(' ,').split(',')) {
                nArray.append(substring)
            }
        }
        // data = 'value,value,value...'
        if (data.includes(',') && !data.includes(':')) {
            for (let substring of data.strip(' ,').split(',')) {
                nArray.append(substring)
            }
        }
        // data = 'value:value:value...'
        if (!data.includes(',') && data.includes(':')) {
            for (let substring of data.strip(' :').split(':')) {
                nArray.append(substring)
            }
        }
        // data = 'value,value:value,value:value:value,value...'
        if (data.includes(',') && data.includes(':')) {
            for (let substring of data.strip(' ,').split(',')) {
                nArray.append(new array(substring.strip(' :').split(':')))
            }
        }
        return nArray
    }
    /** @param {...number} args @returns {Generator<number>} */
    static *generate(...args) {
        let size = args.length
        let start = size == 1 ? 0 : args[0]
        let stop = size == 1 ? args[0] : args[1]
        let step = size == 3 ? args[2] : start < stop ? 1 : -1
        for (let index = start; start < stop ? index < stop : index > stop; index += step) {
            yield index
        }
    }
    /** @returns {boolean} */
    any() {
        for (let value of this) {
            if (value === true) {
                return true
            }
        }
        return false
    }
    /** @param {...any} values @returns {void} */
    append(...values) {
        this.push(...values)
    }
    /** @returns {void} */
    clear() {
        this.splice(0, this.length)
    }
    /** @param {number} index @param {number} start @param {number} stop */
    copy(index, start = 0, stop = this.length) {
        let nArray = new array()
        for (let i = start; i < stop; i++) {
            nArray.append(this[i])
        }
        return nArray
    }
    /** @param {any} value @returns {number} */
    count(value) {
        let count = 0
        for (let value_ of this) {
            if (value_ == value) {
                count += 1
            }
        }
        return count
    }
    /** @returns {boolean} */
    empty() {
        return this.length == 0
    }
    /** @returns {Generator<number>} */
    *enumerate() {
        for (let index = 0; index < this.length; index++) {
            yield [index, this[index]]
        }
    }
    /** @param {...any} values @returns {boolean} */
    excludes(...values) {
        for (let value of values) {
            if (super.includes(value)) {
                return false
            }
        }
        return true
    }
    /** @param {function(value, index, array)} callback @returns {number|null} */
    findindex(callback) {
        for (let [index, value] of this.enumerate()) {
            if (callback(value, index, this)) {
                return index
            }
        }
        return null
    }
    /** @param {function(value, index, array)} callback @returns {any|null} */
    findvalue(callback) {
        return this.find(callback)
    }
    /** @param {number} index @param {any} defaultvalue @returns {any|null} */
    get(index, defaultvalue = null) {
        let value = this[index < 0 ? index + this.length : index]
        if (index < 0) {
            value = this[index + this.length]
        } else if (index >= this.length) {
            value = null
        } else {
            value = this[index]
        }
        return value == null ? defaultvalue : value
    }
    /** @returns {any} */
    getFirst() {
        return this.get(0)
    }
    /** @returns {any} */
    getLast() {
        return this.get(-1)
    }
    /** @returns {string} */
    hash() {
        let string = util.json_encode(this)
        return util.hash_md5(string)
    }
    /** @param {...any} values @returns {boolean} */
    includes(...values) {
        for (let value of values) {
            if (!super.includes(value)) {
                return false
            }
        }
        return true
    }
    /** @param {any} value @param {number} start @returns {number} */
    index(value, start = 0) {
        return this.indexOf(value, start)
    }
    /** @param {number} index @param {any} value @returns {void} */
    insert(index, value) {
        this.splice(index, 0, value)
    }
    /** @param {number} index @returns {void} */
    pop(index = -1) {
        this.splice(index, 1)
    }
    /** @returns {number} */
    product() {
        if (this.length == 0) {
            return 0
        }
        let value = 1
        for (let number of this) {
            value *= number
        }
        return value
    }
    /** @param {...number} index @return {any} */
    random(...index) {
        let nArray = this.slice(...index)
        return util.random(nArray)
    }
    /** @param {...any} values @returns {void} */
    remove(...values) {
        this.removevalues(...values)
    }
    /** @returns {void} */
    removeduplicates() {
        let nArray = this.filter((item, index) => this.index(item) == index)
        this.clear()
        this.append(...nArray)
    }
    /** @param {...number} values @returns {void} */
    removeindexes(...values) {
        let positiveIndexes = values.filter(value => value >= 0)
        positiveIndexes.sort((a, b) => b - a)
        let negativeIndexes = values.filter(value => value < 0)
        negativeIndexes.sort((a, b) => a - b)
        let indexes = [...positiveIndexes, ...negativeIndexes]
        for (let index of indexes) {
            this.pop(index)
        }
    }
    /** @param {...any} values @returns {void} */
    removevalues(...values) {
        for (let value of values) {
            let index = this.index(value)
            if (index != -1) {
                this.pop(index)
            }
        }
    }
    /** @param {number} index @param {any} value @returns {void} */
    replaceindex(index, value) {
        this.splice(index, 1, value)
    }
    /** @param {any} newvalue @param {any} oldvalue @returns {void} */
    replacevalue(oldvalue, newvalue) {
        let index = this.index(oldvalue)
        if (index != -1) {
            this.splice(index, 1, newvalue)
        }
    }
    /** @param {number} newSize @returns {void} */
    resize(newSize) {
        let oldSize = this.size()
        if (oldSize > newSize) {
            this.splice(newSize, oldSize - newSize)
        }
        if (oldSize < newSize) {
            for (let i = 0; i < (newSize - oldSize); i++) {
                this.append(null)
            }
        }
    }
    /** @param {number} index @param {any} value @returns {void} */
    set(index, value) {
        this.splice(index, 0, value)
    }
    /** @returns {void} */
    shuffle() {
        let nArray = new array()
        do {
            let index = Math.floor((Math.random() * this.length))
            nArray.push(this[index])
            this.splice(index, 1)
        } while (this.length > 0)
        this.push(...nArray)
    }
    /** @returns {number} */
    size() {
        return this.length
    }
    /** @returns {number} */
    sum() {
        let value = 0
        for (let number of this) {
            value += number
        }
        return value
    }
    /** @returns {string} */
    toString() {
        return JSON.stringify(this)
    }
    
}
class binary extends String {
    /** @constructor @param {string} data  */
    constructor(data) {
        super(data)
        if (!util.istype(data, 'binary')) {
            throw new Error('TypeError: binary must be characters of the following 0, 1')
        }
    }

    /*
    def __cast(data):
        if isinstance(data, binary):
            data_ = str(data)
        elif isinstance(data, decimal):
            data_ = util.dec2bin(int(data))
        elif isinstance(data, hexadecimal):
            data_ = util.hex2bin(str(data))
        elif isinstance(data, octal):
            data_ = util.oct2bin(str(data))
        elif util.istype(data, 'binary'):
            data_ = data
        elif util.istype(data, 'decimal'):
            data_ = util.dec2bin(data)
        elif util.istype(data, 'hexadecimal'):
            data_ = util.hex2bin(data)
        elif util.istype(data, 'octal'):
            data_ = util.oct2bin(data)
        else:
            raise Exception(f"TypeError: unsupported type: '{type(data)}'")
        return data_
    */

    cast(data) {

    }

    /** @returns {bytes} */
    byt() {

    }
    /** @returns {string} */
    cha() {

    }
    /** @returns {decimal} */
    dec() {

    }
    /** @returns {hexadecimal} */
    hex() {

    }
    /** @returns {octal} */
    oct() {

    }
    /** @param {number} size @returns {string} */
    str(size = 8) {

    }
}
class bytes extends Uint8Array {
    /** @constructor @param {Int8Array|Uint8Array} data  */
    constructor(data) {
        this.data = data
        if (!util.istype(data, 'bytes')) {
            throw new Error('TypeError: bytes must be classes of the following Int8Array, Uint8Array')
        }
    }

    /** @returns {binary} */
    bin() {

    }
    /** @returns {string} */
    cha() {

    }
    /** @returns {decimal} */
    dec() {

    }
    /** @returns {hexadecimal} */
    hex() {

    }
    /** @returns {octal} */
    oct() {

    }
    /** @param {number} size @returns {string} */
    str(size = 8) {

    }
}
class decimal extends Number {
    /** @constructor @param {string} data  */
    constructor(data) {
        super(data)
        if (util.istype(data, 'string-number')) {
            data = Number(data)
        }
        if (!util.istype(data, 'decimal')) {
            throw new Error('TypeError: decimal must be characters of the following 0, 1, 2, 3, 4, 5, 6, 7, 8, 9')
        }
    }

    /** @returns {binary} */
    bin() {

    }
    /** @returns {bytes} */
    byt() {

    }
    /** @returns {string} */
    cha() {

    }
    /** @returns {decimal} */
    dec() {

    }
    /** @returns {hexadecimal} */
    hex() {

    }
    /** @returns {octal} */
    oct() {

    }
    /** @param {number} size @returns {string} */
    str(size = 8) {

    }
}
class entries {
    /** @constructor @param {Object[]} entries  */
    constructor(entries = []) {
        this.entries = new array(entries)
    }
    /** @param {...any} values @returns {boolean}  */
    excludes(...values) {
        return !this.includes(...values)
    }
    /** @param {...any} values @returns {boolean}  */
    includes(...values) {
        let filters = object.fromarray(values)
        for (let entry of this.entries) {
            for (let [filterKey, filterValue] in enumerate(filters)) {
                if (entry[filterKey] == filterValue) return true
            }
        }
        return false
    }
    /** @param {...any} values @returns {Object[]}  */
    filter(...values) {
        return this.filter_and(...values)
    }
    /** @param {...any} values @returns {Object[]}  */
    filter_and(...values) {
        let filters = object.fromarray(values)
        let filtered = new array()
        for (let entry of this.entries) {
            let matches = 0
            for (let [filterKey, filterValue] in enumerate(filters)) {
                if (entry[filterKey] == filterValue) matches += 1
            }
            if (matches == filters.count()) filtered.append(entry)
        }
        return filtered
    }
    /** @param {...any} values @returns {Object[]}  */
    filter_or(...values) {
        let filters = object.fromarray(values)
        let filtered = new array()
        for (let entry of this.entries) {
            let matches = 0
            for (let [filterKey, filterValue] in enumerate(filters)) {
                if (entry[filterKey] == filterValue) matches += 1
            }
            if (matches > 0) {
                filtered.append(entry)
            }
        }
        return filtered
    }
    /** @param {...any} values  */
    find(...values) {
        return this.find_and(...values)
    }
    /** @param {...any} values @returns {{ index: number, value: any }}  */
    find_and(...values) {
        let filters = object.fromarray(values)
        for (let [index, entry] of this.entries.enumerate()) {
            let matches = 0
            for (let [filterKey, filterValue] in enumerate(filters)) {
                if (entry[filterKey] == filterValue) matches += 1
            }
            if (matches == filters.count()) {
                return { 'index': index, 'value': entry }
            }
        }
    }
    /** @param {...any} values @returns {{ index: number, value: any }}  */
    find_or(...values) {
        let filters = object.fromarray(values)
        for (let [index, entry] of this.entries.enumerate()) {
            let matches = 0
            for (let [filterKey, filterValue] in filters.enumerate()) {
                if (entry[filterKey] == filterValue) matches += 1
            }
            if (matches > 0) return { 'index': index, 'value': entry }
        }
    }
    /** @param {...any} values @returns {null}  */
    remove(values) {
        let identifiers = []
        for (let value of values) {
            if (util.istype(value, 'string')) {
                identifiers.push(value)
            }
            if (util.istype(value, 'object')) {
                identifiers.push(value['id'])
            }
        }
        let nEntries = new array()
        for (let entry of this.entries) {
            if (!identifiers.includes(entry['id'])) nEntries.append(entry)
        }
        this.entries = nEntries
    }
    /** @param {...any} values @returns {null}  */
    remove_filter(...values) {
        let filtered = this.find(...values)
        this.remove(filtered)
    }
    /** @param {Object} entry @returns {null}  */
    update(entry) {
        for (let [index, entry_] of this.entries.enumerate()) {
            if (entry_['id'] == entry['id']) {
                this.entries[index] = entry
            }
        }
    }
}
class hexadecimal extends String {
    /** @constructor @param {string} data  */
    constructor(data) {
        super(data)
        if (!util.istype(data, 'hexadecimal')) {
            throw new Error('TypeError: hexadecimal must be characters of the following 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f, A, B, C, D, E, F')
        }
    }

    /** @returns {binary} */
    bin() {

    }
    /** @returns {bytes} */
    byt() {

    }
    /** @returns {string} */
    cha() {

    }
    /** @returns {decimal} */
    dec() {

    }
    /** @returns {octal} */
    oct() {

    }
    /** @param {number} size @returns {string} */
    str(size = 8) {

    }
}
class octal extends String {
    /** @constructor @param {string} data  */
    constructor(data) {
        super(data)
        if (!util.istype(data, 'octal')) {
            throw new Error('TypeError: octal must be characters of the following 0, 1, 2, 3, 4, 5, 6, 7')
        }
    }

    /** @returns {binary} */
    bin() {

    }
    /** @returns {bytes} */
    byt() {

    }
    /** @returns {string} */
    cha() {

    }
    /** @returns {decimal} */
    dec() {

    }
    /** @returns {hexadecimal} */
    hex() {

    }
    /** @param {number} size @returns {string} */
    str(size = 8) {

    }
}
class object extends Object {
    /** @constructor */
    constructor(...values) {
        super()
        for (let value of values) {
            if (value instanceof Object | object) {
                for (let key in value) {
                    this[key] = value[key]
                }
            }
            else {
                this.update(object.fromdata(value))
            }
        }
    }
    /** @param {any[]|bytes|{string:string}|string} data @returns {object} */
    static fromdata(data) {
        let nObject = new object()
        if (!data) {
            return nObject
        }
        if (util.istype(data, 'array')) {
            nObject = object.fromarray(data)
        }
        else if (util.istype(data, 'bytes-array')) {
            nObject = object.fromarray(util.json_decode(util.byt2str(data)))
        }
        else if (util.istype(data, 'bytes-object')) {
            nObject.update(util.json_decode(util.byt2str(data)))
        }
        else if (util.istype(data, 'object')) {
            nObject.update(data)
        }
        else if (util.istype(data, 'string-object')) {
            nObject.update(util.json_decode(data))
        }
        else if (util.istype(data, 'string')) {
            nObject = object.fromstring(data)
        }
        else {
            return console.error(`TypeError: variable-name=data variable-value=${data} variable-type=${typeof data} type=array|bytes-array|bytes-object|object|string-object|string`)
        }
        return nObject
    }
    /** @param {string[]} data @returns {object} */
    static fromarray(data) {
        let nObject = new object()
        if (!data) {
            return nObject
        }
        // data = [['key','value'],['key','value']...]
        if (data.every((item) => util.istype(item, 'array') && item.length == 2)) {
            for (let index = 0; index < data.length; index++) {
                nObject[data[index][0]] = data[index][1]
            }
        }
        // data = ['key','value','key','value'...]
        else if (data.every((item) => util.istype(item, 'number|string')) && data.length % 2 == 0) {
            for (let index = 0; index < data.length; index += 2) {
                nObject[data[index]] = data[index + 1]
            }
        } else {
            return console.error(`TypeError: variable-name=data variable-value=${data} variable-type=${typeof data} type=array`)
        }
        return nObject
    }
    /** @param {number[]|string[]} @param {any} value  keys @returns {object} */
    static fromkeys(keys, value) {
        let nObject = new object()
        for (let key of keys) {
            nObject[key] = value
        }
        return nObject
    }
    /** @param {string} data @param {string} delimiterPairs @param {string} delimiterPair @returns {object} */
    static fromstring(data, delimiterPairs = ',', delimiterPair = ':') {
        let nObject = new object()
        for (let substring of data.strip(` ${delimiterPairs}`).split(delimiterPairs)) {
            nObject.set(...substring.strip(` ${delimiterPair}`).split(delimiterPair))
        }
        return nObject
    }
    // custom dynamic
    /** @param {number|string} key @param {any} value  @returns {void} */
    append(key, value) {
        this[key] = value
    }
    /** @returns {void} */
    clear() {
        for (let key in this) {
            delete this[key]
        }
    }
    /** @returns {object} */
    copy() {
        return new object(this)
    }
    /** @returns {number} */
    count() {
        return this.keys().length
    }
    /** @returns {boolean} */
    empty() {
        return this.keys().length == 0
    }
    *enumerate() {
        for (let key in this) {
            yield [key, this[key]]
        }
    }
    /** @param {...any} values @returns {boolean} */
    excludes(...values) {
        return this.excludeskeys(...values)
    }
    /** @param {...any} values @returns {boolean} */
    excludeskeys(...values) {
        let keys = this.keys()
        for (let value of values) {
            if (keys.includes(value)) {
                return false
            }
        }
        return true
    }
    /** @param {...any} values @returns {boolean} */
    excludesvalues(...values) {
        let values_ = this.values()
        for (let value of values) {
            if (values_.includes(value)) {
                return false
            }
        }
        return true
    }
    /** @param {number|string} key @param {any} defaultvalue @returns {any} */
    get(key, defaultvalue = null) {
        return key in this ? this[key] : defaultvalue
    }
    /** @returns {string} */
    hash() {
        let string = util.json_encode(this)
        return util.hash_md5(string)
    }
    /** @param {...number|string} values @returns {boolean} */
    includes(...values) {
        return this.includeskeys(...values)
    }
    /** @param {...number|string} values @returns {boolean} */
    includeskeys(...values) {
        let keys = this.keys()
        for (let value of values) {
            if (!keys.includes(value)) {
                return false
            }
        }
        return true
    }
    /** @param {...any} values @returns {boolean} */
    includesvalues(...values) {
        let values_ = this.values()
        for (let value of values) {
            if (!values_.includes(value)) {
                return false
            }
        }
        return true
    }
    /** @param {string} key @returns {boolean} */
    iskey(key) {
        return this.keys().includes(key)
    }
    /** @param {number|string} key @param {string} datatype @returns {boolean} */
    istype(key, datatype) {
        return util.istype(this.get(key), datatype)
    }
    /** @param {string} key @param {any} value @returns {boolean} */
    isvalue(key, value) {
        return this.get(key) == value
    }
    /** @param {string} key @param {any} value @returns {boolean} */
    isvaluein(key, value) {
        return this.get(key).includes(value)
    }
    /** @returns {array} */
    keys() {
        let keys = new array()
        for (let key in this) {
            keys.append(key)
        }
        return keys
    }
    /** @returns {void} */
    lower() {
        for (let [key, value] of this.enumerate()) {
            if (util.istype(key, 'string')) {
                delete this[key]
                this[key.lower()] = value
            }
        }
    }
    /** @param {...number|string} keys @returns {void} */
    order(...keys) {
        let cObject = this.copy()
        this.clear()
        for (let key of keys) {
            if (key in cObject) {
                this[key] = cObject[key]
            }
        }
    }
    /** @returns {void} */
    sort() {
        let keys = this.keys()
        keys.sort()
        for (let key of keys) {
            let value = this[key]
            delete this[key]
            this[key] = value
        }
        return this
    }
    /** @param {number|string} key @param {any} defaultvalue @returns {any} */
    pop(key, defaultvalue = null) {
        let value = this[key]
        delete this[key]
        return value == null ? defaultvalue : value
    }
    /** @param {...number|string} values @returns {void} */
    remove(...values) {
        return this.removekeys(...values)
    }
    /** @param {...number|string} values @returns {void} */
    removekeys(...values) {
        for (let key in this) {
            if (values.includes(key)) {
                delete this[key]
            }
        }
    }
    /** @param {...any} values @returns {void} */
    removevalues(...values) {
        for (let key in this) {
            if (values.includes(this[key])) {
                delete this[key]
            }
        }
    }
    /** @param {number|string} oldkey @param {number|string} newkey @returns {void} */
    replacekey(oldkey, newkey) {
        if (oldkey in this) {
            let value = this[oldkey]
            delete this[oldkey]
            this[newkey] = value
        }
    }
    /** @param {any} value @param {any} newvalue @returns {void} */
    replacevalue(value, newvalue) {
        for (let key in this) {
            if (this[key] == value) {
                this[key] = newvalue
            }
        }
    }
    /** @param {number|string} key @param {any} value @returns {void} */
    set(key, value) {
        this[key] = value
    }
    /** @param {number|string} key @param {any} defaultvalue @returns {any} */
    setdefault(key, defaultvalue = null) {
        if (key in this) {
            return this[key]
        } else {
            this[key] = defaultvalue
            return defaultvalue
        }
    }
    /** @returns {number} */
    size() {
        return this.keys().length
    }
    /** @param {number} dimensions @returns {array} */
    toitems(dimensions = 1) {
        nArray = array()
        if (dimensions == 1) {
            for (let [key, value] of this.enumerate()) {
                nArray.append(key, value)
            }
        }
        if (dimensions == 2) {
            for (let [key, value] of this.enumerate()) {
                nArray.append(array(key, value))
            }
        }
        return nArray
    }
    /** @param {string} delimiterPairs @param {string} delimiterPair @returns {string} */
    tostring(delimiterPairs = ', ', delimiterPair = ': ') {
        nArray = array()
        for (let [key, value] of this.enumerate()) {
            nArray.append(`${key}${delimiterPair}${value}`)
        }
        return nArray.join(delimiterPairs)
    }
    /** @returns {string} */
    toString() {
        return JSON.stringify(this)
    }
    /** @param {object|Object} other  @returns {object} */
    update(other) {
        for (let key in other) {
            this[key] = other[key]
        }
        return this
    }
    /** @returns {void} */
    upper() {
        for (let [key, value] of this.enumerate()) {
            if (util.istype(key, 'string')) {
                delete this[key]
                this[key.upper()] = value
            }
        }
    }
    /** @returns {array} */
    values() {
        let values = new array()
        for (let key in this) {
            values.append(this[key])
        }
        return values
    }
}
class string extends String {
    constructor(data) {
        super(data)
    }

    /** @returns {binary} */
    bin() {

    }
    /** @returns {bytes} */
    byt() {

    }
    /** @returns {string} */
    cha() {

    }
    /** @returns {decimal} */
    dec() {

    }
    /** @returns {hexadecimal} */
    hex() {

    }
    /** @returns {octal} */
    oct() {

    }
}
//_________________________________________________________________________________________________________________________________________________//
class app {
    constructor() {

    }

    /** @readonly @type {{string:string}} */
    static CONFIGURATION = {
        'color-accent': '#aa0000',
        'color-caution': '#c8c800',
        'color-default': '#191919',
        'color-header': '#323232',
        'color-highlight': '#646464',
        'color-select': '#4b4b4b',
        'color-text': '#ffffff',
        'font-family': 'American Typewriter, serif',
        'font-size': '100%',
        'font-weight': 'normal',
    }
    /** @readonly @type {{string:string}} */
    static DIRECTORY = {
        'root': '/',
        'images': '/repository/images/',
    }

    /** @type {array} */
    static childWindows = []
    /** @type {object} */
    static eventListenerInterfaces = {}
    /** @type {string} */
    static identifier = null
    /** @type {boolean[]} */
    static mouseButtons = []
    /** @type {string} */
    static name = ''
    /** @type {object} */
    static options = new object()
    /** @type {boolean} */
    static touchable = true

    /** @readonly @type {string} */
    static DEVICE_PHONE = 'phone'
    /** @readonly @type {string} */
    static DEVICE_COMPUTER = 'computer'

    /** @readonly @type {string} */
    static COLOR_SCHEME_DARK = 'DARK'
    /** @readonly @type {string} */
    static COLOR_SCHEME_LIGHT = 'LIGHT'

    /** @readonly @type {number} */
    static MOUSE_BUTTON_LEFT = 0
    /** @readonly @type {number} */
    static MOUSE_BUTTON_WHEEL = 1
    /** @readonly @type {number} */
    static MOUSE_BUTTON_RIGHT = 2

    /** @readonly @type {string[]} */
    static PROGRESS_ACTIVE = []
    /** @readonly @type {number} */
    static PROGRESS_TIMEOUT = 3000
    /** @readonly @type {Dialog} */
    static PROGRESS_DIALOG

    /** @readonly @type {{string:string}} */
    static EVENT_INTERFACES = { "afterprint": "onAfterPrint", "afterscriptexecute": "onAfterScriptExecute", "appinstalled": "onAppInstalled", "beforeinstallprompt": "onBeforeInstallPrompt", "beforeprint": "onBeforePrint", "beforescriptexecute": "onBeforeScriptExecute", "beforeunload": "onBeforeUnload", "blur": "onBlur", "click": "onClick", "copy": "onCopy", "cut": "onCut", "devicemotion": "onDeviceMotion", "deviceorientation": "onDeviceOrientation", "error": "onError", "focus": "onFocus", "fullscreenchange": "onFullScreenChange", "fullscreenerror": "onFullScreenError", "gamepadconnected": "onGamePadConnected", "gamepaddisonnected": "onGamePadDisonnected", "hashchange": "onHashChange", "input": "onInput", "keydown": "onKeyDown", "keyup": "onKeyUp", "languagechange": "onLanguageChange", "message": "onMessage", "messageerror": "onMessageError", "mousedown": "onMouseDown", "mouseenter": "onMouseEnter", "mouseleave": "onMouseLeave", "mousemove": "onMouseMove", "mouseout": "onMouseOut", "mouseover": "onMouseOver", "mouseup": "onMouseUp", "offline": "onOffline", "online": "onOnline", "pagehide": "onPageHide", "pagereveal": "onPageReveal", "pageshow": "onPageShow", "pageswap": "onPageSwap", "paste": "onPaste", "pointercancel": "onPointerCancel", "pointerdown": "onPointerDown", "pointerlockchange": "onPointerLockChange", "pointerlockerror": "onPointerLockError", "popstate": "onPopState", "prerenderingchange": "onPrerenderingChange", "readystatechange": "onReadyStateChange", "rejectionhandled": "onRejectionHandled", "resize": "onResize", "scroll": "onScroll", "scrollend": "onScrollEnd", "securitypolicyviolation": "onSecurityPolicyViolation", "selectionchange": "onSelectionChange", "storage": "onStorage", "touchend": "onTouchEnd", "touchmove": "onTouchMove", "touchstart": "onTouchStart", "unhandledrejection": "onUnhandledRejection", "visibilitychange": "onVisibilityChange", "wheel": "onWheel" }
    /** @readonly @type {{string:string}} */
    static EVENT_INTERFACES_ = { "abort": "onAbort", "afterprint": "onAfterPrint", "animationend": "onAnimationEnd", "animationiteration": "onAnimatiOniteration", "animationstart": "onAnimationStart", "beforeprint": "onBeforePrint", "beforeunload": "onBeforeUnload", "blur": "onBlur", "canplay": "onCanPlay", "canplaythrough": "onCanPlayThrough", "change": "onChange", "click": "onClick", "contextmenu": "onContextMenu", "copy": "onCopy", "cut": "onCut", "dblclick": "onDBLClick", "drag": "onDrag", "dragend": "onDragEnd", "dragenter": "onDragEnter", "dragleave": "onDragLeave", "dragover": "onDragover", "dragstart": "onDragStart", "drop": "onDrop", "durationchange": "onDurationChange", "ended": "onEnded", "error": "onError", "focus": "onFocus", "focusin": "onFocusIn", "focusout": "onFocusOut", "fullscreenchange": "onFullscreenChange", "fullscreenerror": "onFullscreenError", "hashchange": "onHashChange", "input": "onInput", "invalid": "onInvalid", "keydown": "onKeyDown", "keyup": "onKeyUp", "load": "onLoad", "loadeddata": "onLoadedData", "loadedmetadata": "onLoadedMetadata", "loadstart": "onLoadStart", "message": "onMessage", "mousedown": "onMouseDown", "mouseenter": "onMouseEnter", "mouseleave": "onMouseLeave", "mousemove": "onMouseMove", "mouseover": "onMouseOver", "mouseout": "onMouseOut", "mouseup": "onMouseUp", "mousewheel": "onMouseWheel", "offline": "onOffline", "online": "onOnline", "open": "onOpen", "pagehide": "onPageHide", "pageshow": "onPageShow", "paste": "onPaste", "pause": "onPause", "play": "onPlay", "playing": "onPlaying", "popstate": "onPopState", "progress": "onProgress", "ratechange": "onRateChange", "resize": "onResize", "reset": "onReset", "scroll": "onScroll", "search": "onSearch", "seeked": "onSeeked", "seeking": "onSeeking", "select": "onSelect", "show": "onShow", "stalled": "onStalled", "storage": "onStorage", "submit": "onSubmit", "suspend": "onSuspend", "timeupdate": "onTimeUpdate", "toggle": "onToggle", "touchcancel": "onTouchCancel", "touchend": "onTouchEnd", "touchmove": "onTouchMove", "touchstart": "onTouchStart", "transitionend": "onTransitionEnd", "volumechange": "onVolumeChange", "waiting": "onWaiting", "wheel": "onWheel" }
    /** @readonly @type {{string:string}} */
    static LANGUAGE_CODES = { "ab": "abkhazian", "aa": "afar", "af": "afrikaans", "ak": "akan", "sq": "albanian", "am": "amharic", "ar": "arabic", "an": "aragonese", "hy": "armenian", "as": "assamese", "av": "avaric", "ae": "avestan", "ay": "aymara", "az": "azerbaijani", "bm": "bambara", "ba": "bashkir", "eu": "basque", "be": "belarusian", "bn": "bengali (bangla)", "bh": "bihari", "bi": "bislama", "bs": "bosnian", "br": "breton", "bg": "bulgarian", "my": "burmese", "ca": "catalan", "ch": "chamorro", "ce": "chechen", "ny": "chichewa, chewa, nyanja", "zh": "chinese", "zh-hans": "chinese (simplified)", "zh-hant": "chinese (traditional)", "cv": "chuvash", "kw": "cornish", "co": "corsican", "cr": "cree", "hr": "croatian", "cs": "czech", "da": "danish", "dv": "divehi, dhivehi, maldivian", "nl": "dutch", "dz": "dzongkha", "en": "english", "eo": "esperanto", "et": "estonian", "ee": "ewe", "fo": "faroese", "fj": "fijian", "fi": "finnish", "fr": "french", "ff": "fula, fulah, pulaar, pular", "gl": "galician", "gd": "gaelic (scottish)", "gv": "manx", "ka": "georgian", "de": "german", "el": "greek", "kl": "kalaallisut, greenlandic", "gn": "guarani", "gu": "gujarati", "ht": "haitian creole", "ha": "hausa", "he": "hebrew", "hz": "herero", "hi": "hindi", "ho": "hiri motu", "hu": "hungarian", "is": "icelandic", "io": "ido", "ig": "igbo", "id, in": "indonesian", "ia": "interlingua", "ie": "interlingue", "iu": "inuktitut", "ik": "inupiak", "ga": "irish", "it": "italian", "ja": "japanese", "jv": "javanese", "kn": "kannada", "kr": "kanuri", "ks": "kashmiri", "kk": "kazakh", "km": "khmer", "ki": "kikuyu", "rw": "kinyarwanda (rwanda)", "rn": "kirundi", "ky": "kyrgyz", "kv": "komi", "kg": "kongo", "ko": "korean", "ku": "kurdish", "kj": "kwanyama", "lo": "lao", "la": "latin", "lv": "latvian (lettish)", "li": "limburgish ( limburger)", "ln": "lingala", "lt": "lithuanian", "lu": "luga-katanga", "lg": "luganda, ganda", "lb": "luxembourgish", "mk": "macedonian", "mg": "malagasy", "ms": "malay", "ml": "malayalam", "mt": "maltese", "mi": "maori", "mr": "marathi", "mh": "marshallese", "mo": "moldavian", "mn": "mongolian", "na": "nauru", "nv": "navajo", "ng": "ndonga", "nd": "northern ndebele", "ne": "nepali", "no": "norwegian", "nb": "norwegian bokmål", "nn": "norwegian nynorsk", "ii": "sichuan yi", "oc": "occitan", "oj": "ojibwe", "cu": "old church slavonic, old bulgarian", "or": "oriya", "om": "oromo (afaan oromo)", "os": "ossetian", "pi": "pāli", "ps": "pashto, pushto", "fa": "persian (farsi)", "pl": "polish", "pt": "portuguese", "pa": "punjabi (eastern)", "qu": "quechua", "rm": "romansh", "ro": "romanian", "ru": "russian", "se": "sami", "sm": "samoan", "sg": "sango", "sa": "sanskrit", "sr": "serbian", "sh": "serbo-croatian", "st": "sesotho", "tn": "setswana", "sn": "shona", "sd": "sindhi", "si": "sinhalese", "ss": "swati", "sk": "slovak", "sl": "slovenian", "so": "somali", "nr": "southern ndebele", "es": "spanish", "su": "sundanese", "sw": "swahili (kiswahili)", "sv": "swedish", "tl": "tagalog", "ty": "tahitian", "tg": "tajik", "ta": "tamil", "tt": "tatar", "te": "telugu", "th": "thai", "bo": "tibetan", "ti": "tigrinya", "to": "tonga", "ts": "tsonga", "tr": "turkish", "tk": "turkmen", "tw": "twi", "ug": "uyghur", "uk": "ukrainian", "ur": "urdu", "uz": "uzbek", "ve": "venda", "vi": "vietnamese", "vo": "volapük", "wa": "wallon", "cy": "welsh", "wo": "wolof", "fy": "western frisian", "xh": "xhosa", "yi, ji": "yiddish", "yo": "yoruba", "za": "zhuang, chuang", "zu": "zulu" }
    
    /** @param {string|{string:string}} options @returns {void} */
    static start(options = null) {
        app.options = object.fromdata(options)
        app.identifier = app.options.get('identifier', util.identifier())
        app.name = app.options.get('name', util.path_info(window.location.pathname, 'filename'))
        let dialog = app.createProgressDialog()
        dialog.setStyle(DialogProgress.STYLE_SPINNER)
        app.PROGRESS_DIALOG = dialog
        // 
        app.listeners1()
        if (window.document.readyState === 'complete') {
            app.listeners2()
        }
    }
    /** @private @returns {void} */
    static listeners1() {
        /** @param {Event} event @returns {void} */
        window.onafterprint = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onAfterPrint) {
                window.onAfterPrint(event)
            }
        }
        /** @param {Event} event @returns {void} */
        window.onappinstalled = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onAppInstalled) {
                window.onAppInstalled(event)
            }
        }
        /** @param {BeforeInstallPromptEvent} event @returns {void} */
        window.onbeforeinstallprompt = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onBeforeInstallPrompt) {
                window.onBeforeInstallPrompt(event)
            }
        }
        /** @param {Event} event @returns {void} */
        window.onbeforeprint = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onBeforePrint) {
                window.onBeforePrint(event)
            }
        }
        /** @param {BeforeUnloadEvent} event @returns {void} */
        window.onbeforeunload = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onBeforeUnload) {
                window.onBeforeUnload(event)
            }
        }
        /** @param {FocusEvent} event @returns {void} */
        window.onblur = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onBlur) {
                window.onBlur(event)
            }
        }
        /** @param {ClipboardEvent} event @returns {void} */
        window.oncopy = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onCopy) {
                window.onCopy(event)
            }
        }
        /** @param {ClipboardEvent} event @returns {void} */
        window.oncut = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onCut) {
                window.onCut(event)
            }
        }
        /** @param {DeviceMotionEvent} event @returns {void} */
        window.ondevicemotion = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onDeviceMotion) {
                window.onDeviceMotion(event)
            }
        }
        /** @param {DeviceOrientationEvent} event @returns {void} */
        window.ondeviceorientation = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onDeviceOrientation) {
                window.onDeviceOrientation(event)
            }
        }
        /** @param {DeviceOrientationEvent} event @returns {void} */
        window.deviceorientationabsolute = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onDeviceOrientationAbsolute) {
                window.onDeviceOrientationAbsolute(event)
            }
        }
        /** @param {ErrorEvent} event @returns {void} */
        window.onerror = (event, source, lineno, colno, error) => {
            app.onEventListenerInterface(event.type, null)
            if (window.onError) {
                window.onError(event)
            }
        }
        /** @param {FocusEvent} event @returns {void} */
        window.onfocus = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onFocus) {
                window.onFocus(event)
            }
        }
        /** @param {Event} event @returns {void} */
        window.ongamepadconnected = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onGamePadConnected) {
                window.onGamePadConnected(event)
            }
        }
        /** @param {Event} event @returns {void} */
        window.ongamepaddisconnected = (event) => {
            if (window.onGamePadDisconnected) {
                window.onGamePadDisconnected(event)
            }
        }
        /** @param {HashChangeEvent} event @returns {void} */
        window.onhashchange = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onHashChange) {
                window.onHashChange(event)
            }
        }
        /** @param {HashChangeEvent} event @returns {void} */
        window.onlanguagechange = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onLanguageChange) {
                window.onLanguageChange(event)
            }
        }
        /** @param {Event} event @returns {void} */
        window.onload = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onLoad) {
                window.onLoad(event)
            }
        }
        /** @param {MessageEvent} event @returns {void} */
        window.onmessage = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onMessage) {
                window.onMessage(event)
            }
        }
        /** @param {MessageEvent} event @returns {void} */
        window.onmessageerror = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onMessageError) {
                window.onMessageError(event)
            }
        }
        /** @param {Event} event @returns {void} */
        window.onoffline = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onOffline) {
                window.onOffline(event)
            }
        }
        /** @param {Event} event @returns {void} */
        window.ononline = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onOnline) {
                window.onOnline(event)
            }
        }
        /** @param {PageTransitionEvent} event @returns {void} */
        window.onpagehide = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onPageHide) {
                window.onPageHide(event)
            }
        }
        /** @param {PageRevealEvent} event @returns {void} */
        window.onpagereveal = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onPageReveal) {
                window.onPageReveal(event)
            }
        }
        /** @param {PageTransitionEvent} event @returns {void} */
        window.onpageshow = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onPageShow) {
                window.onPageShow(event)
            }
        }
        /** @param {PageSwapEvent} event @returns {void} */
        window.onpageswap = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onPageSwap) {
                window.onPageSwap(event)
            }
        }
        /** @param {ClipboardEvent} event @returns {void} */
        window.onpaste = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onPaste) {
                window.onPaste(event)
            }
        }
        /** @param {PopStateEvent} event @returns {void} */
        window.onpopstate = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onPopState) {
                window.onPopState(event)
            }
        }
        /** @param {PromiseRejectionEvent} event @returns {void} */
        window.onrejectionhandled = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onRejectionHandled) {
                window.onRejectionHandled(event)
            }
        }
        /** @param {Event} event @returns {void} */
        window.onresize = (event) => {
            app.onEventListenerInterface(event.type, event)
            // refresh contents of background element
            for (let element of document.getElementsByClassName('content-background')) {
                let parentElement = app.element(element.parentElement)
                if (element.something) {
                    parentElement.setBackground(element.something)
                }
            }
            if (window.onResize) {
                window.onResize(event)
            }
        }
        /** @param {StorageEvent} event @returns {void} */
        window.onstorage = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onStorage) {
                window.onStorage(event)
            }
        }
        /** @param {PromiseRejectionEvent} event @returns {void} */
        window.onunhandledrejection = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onUnhandledRejection) {
                window.onUnhandledRejection(event)
            }
        }
        /** @param {Event} event @returns {void} */
        window.document.onreadystatechange = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onReadyStateChange) {
                window.onReadyStateChange(event)
            }
            if (window.document.readyState === 'complete') {
                app.listeners2()
            }
        }
    }
    /** @private @returns {void} */
    static listeners2() {
        if (app.options.get('input-validation', 'true') == 'true') {
            app.inputValidation()
        }
        /** @param {Event} event @returns {void} */
        window.document.onafterscriptexecute = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onAfterScriptExecute) {
                window.onAfterScriptExecute(event)
            }
        }
        /** @param {Event} event @returns {void} */
        window.document.onbeforescriptexecute = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onBeforeScriptExecute) {
                window.onBeforeScriptExecute(event)
            }
        }
        /** @param {PointerEvent} event @returns {void} */
        window.document.onclick = (event) => {
            if (app.isTouchDisabled()) return
            app.onEventListenerInterface(event.type, event)
            if (window.onClick) {
                window.onClick(event, app.element(event.target))
            }
        }
        /** @param {Event} event @returns {void} */
        window.document.onfullscreenchange = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onFullScreenChange) {
                window.onFullScreenChange(event)
            }
        }
        /** @param {Event} event @returns {void} */
        window.document.onfullscreenerror = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onFullScreenError) {
                window.onFullScreenError(event)
            }
        }
        /** @param {InputEvent} event @returns {void} */
        window.document.oninput = (event) => {
            if (app.isTouchDisabled()) return
            app.onEventListenerInterface(event.type, event)
            if (window.onInput) {
                window.onInput(event, app.element(event.target))
            }
        }
        /** @param {KeyboardEvent} event @returns {void} */
        window.document.onkeydown = (event) => {
            if (app.isTouchDisabled()) return
            app.onEventListenerInterface(event.type, event)
            if (window.onKeyDown) {
                window.onKeyDown(event)
            }
        }
        /** @param {KeyboardEvent} event @returns {void} */
        window.document.onkeyup = (event) => {
            if (app.isTouchDisabled()) return
            app.onEventListenerInterface(event.type, event)
            if (window.onKeyUp) {
                window.onKeyUp(event)
            }
        }
        /** @param {MouseEvent} event @returns {void} */
        window.document.onmousedown = (event) => {
            app.mouseButtons[event.button] = true
            if (app.isTouchDisabled()) return
            app.onEventListenerInterface(event.type, event)
            if (window.onMouseDown) {
                window.onMouseDown(event, app.element(event.target))
            }
        }
        /** @param {MouseEvent} event @returns {void} */
        window.document.onmouseenter = (event) => {
            if (app.isTouchDisabled()) return
            app.onEventListenerInterface(event.type, event)
            if (window.onMouseEnter) {
                window.onMouseEnter(event, app.element(event.target))
            }
        }
        /** @param {MouseEvent} event @returns {void} */
        window.document.onmouseleave = (event) => {
            if (app.isTouchDisabled()) return
            app.onEventListenerInterface(event.type, event)
            if (window.onMouseLeave) {
                window.onMouseLeave(event, app.element(event.target))
            }
        }
        /** @param {MouseEvent} event @returns {void} */
        window.document.onmousemove = (event) => {
            if (app.isTouchDisabled()) return
            app.onEventListenerInterface(event.type, event)
            if (window.onMouseMove) {
                window.onMouseMove(event, app.element(event.target))
            }
        }
        /** @param {MouseEvent} event @returns {void} */
        window.document.onmouseout = (event) => {
            if (app.isTouchDisabled()) return
            app.onEventListenerInterface(event.type, event)
            if (window.onMouseOut) {
                window.onMouseOut(event, app.element(event.target))
            }
        }
        /** @param {MouseEvent} event @returns {void} */
        window.document.onmouseover = (event) => {
            if (app.isTouchDisabled()) return
            app.onEventListenerInterface(event.type, event)
            if (window.onMouseOver) {
                window.onMouseOver(event, app.element(event.target))
            }
        }
        /** @param {MouseEvent} event @returns {void} */
        window.document.onmouseup = (event) => {
            app.mouseButtons[event.button] = false
            if (app.isTouchDisabled()) return
            app.onEventListenerInterface(event.type, event)
            if (window.onMouseUp) {
                window.onMouseUp(event, app.element(event.target))
            }
        }
        /** @param {PointerEvent} event @returns {void} */
        window.document.onpointercancel = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onPointerCancel) {
                window.onPointerCancel(event)
            }
        }
        /** @param {PointerEvent} event @returns {void} */
        window.document.onpointerdown = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onPointerDown) {
                window.onPointerDown(event, app.element(event.target))
            }
        }
        /** @param {PointerEvent} event @returns {void} */
        window.document.onpointerenter = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onPointerEnter) {
                window.onPointerEnter(event)
            }
        }
        /** @param {Event} event @returns {void} */
        window.document.onpointerlockchange = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onPointerLockChange) {
                window.onPointerLockChange(event)
            }
        }
        /** @param {Event} event @returns {void} */
        window.document.onpointerlockerror = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onPointerLockError) {
                window.onPointerLockError(event)
            }
        }
        /** @param {Event} event @returns {void} */
        window.document.onprerenderingchange = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onPrerenderingChange) {
                window.onPrerenderingChange(event)
            }
        }
        /** @param {Event} event @returns {void} */
        window.document.onscroll = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onScroll) {
                window.onScroll(event, app.element(event.target))
            }
        }
        /** @param {Event} event @returns {void} */
        window.document.onscrollend = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onScrollEnd) {
                window.onScrollEnd(event, app.element(event.target))
            }
        }
        /** @param {SecurityPolicyViolationEvent} event @returns {void} */
        window.document.onsecuritypolicyviolation = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onSecurityPolicyViolation) {
                window.onSecurityPolicyViolation(event)
            }
        }
        /** @param {Event} event @returns {void} */
        window.document.onselectionchange = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onSelectionChange) {
                window.onSelectionChange(event)
            }
        }
        /** @param {TouchEvent} event @returns {void} */
        window.document.ontouchend = (event) => {
            if (app.isTouchDisabled()) return
            app.onEventListenerInterface(event.type, event)
            if (window.onTouchEnd) {
                window.onTouchEnd(event, app.element(event.target))
            }
        }
        /** @param {TouchEvent} event @returns {void} */
        window.document.ontouchmove = (event) => {
            if (app.isTouchDisabled()) return
            app.onEventListenerInterface(event.type, event)
            if (window.onTouchMove) {
                window.onTouchMove(event, app.element(event.target))
            }
        }
        /** @param {TouchEvent} event @returns {void} */
        window.document.ontouchstart = (event) => {
            if (app.isTouchDisabled()) return
            app.onEventListenerInterface(event.type, event)
            if (window.onTouchStart) {
                window.onTouchStart(event, app.element(event.target))
            }
        }
        /** @param {Event} event @returns {void} */
        window.document.onvisibilitychange = (event) => {
            app.onEventListenerInterface(event.type, event)
            if (window.onVisibilityChange) {
                window.onVisibilityChange(event)
            }
        }
        /** @param {WheelEvent} event @returns {void} */
        window.document.onwheel = (event) => {
            if (app.isTouchDisabled()) return
            app.onEventListenerInterface(event.type, event)
            if (window.onWheel) {
                window.onWheel(event, app.element(event.target))
            }
        }
    }
    


    // system
    /** @param {string} types @param {View} instance @param {boolean} withinView @returns {void} */
    static addEventListenerInterface(types, instance, withinView = true) {
        for (let type of types.strip(' |').split('|')) {
            type = type.strip(' ')
            if (!app.isEventInterface(type)) {
                console.warn(`ValueError: variable-name=types variable-value=${type}`)
                continue
            }
            if (!app.eventListenerInterfaces[type]) {
                app.eventListenerInterfaces[type] = []
            }
            app.eventListenerInterfaces[type].append([instance, withinView])
        }
    }
    /** @param {Window} window_ @returns {void} */
    static addWindow(window_) {
        app.childWindows.append(window_)
    }
    /** @param {any} message @param {string} targetOrigin @param {[]} transfer @returns {void} */
    static broadcast(message, targetOrigin = "*", transfer = null) {
        window.postMessage(message, targetOrigin, transfer)
    }
    /** */
    static broadcastIntent(action, category, data, type, extras, options) {
    }
    /** @param {string} data @returns {Promise|void} */
    static copyToClipboard(data) {
        if (navigator && navigator.clipboard && navigator.clipboard.writeText) {
            return navigator.clipboard.writeText(data)
        }
        return console.error('Clipboard API is not available.')
    }
    /** @deprecated @param {string|null} key @param {any|null} value @returns {{string:string}|string} */
    static configuration(key = null, value = null) {
        if (key && value) {
            app.CONFIGURATION[key] = value
            if (window.onConfiguration) {
                window.onConfiguration(key, value)
            }
        }
        else if (key) {
            if (!key in app.CONFIGURATION) return console.error(`TypeError: `, key)
            return app.CONFIGURATION[key]
        }
        else {
            return app.CONFIGURATION
        }
    }
    /** */
    static createNotification(title, body, icon) {
    }
    /** @param {string|null} key @param {string|null} value @returns {string|void} */
    static directory(key, value = null) {
        if (value) {
            app.DIRECTORY[key] = value
        } else {
            if (excludes(key, app.DIRECTORY)) return console.error(`ValueError: variable-name=key variable-value=${key}`)
            return app.DIRECTORY[key]
        }
    }
    /** @returns {void} */
    static exit() {
        window.close()
    }
    /** @param {string} javascript @returns {void} */
    static executeScript(javascript) {
        window.eval(javascript)
    }
    /** @param {boolean} value @param {AppElement|Element|string} element @returns {void} */
    static fullscreen(value, element = document.documentElement) {
        // https://developer.mozilla.org/en-US/docs/Web/API/Window/fullScreen
        element = app.element(element).getElement()
        if (value) {
            if (element.requestFullscreen) {
                element.requestFullscreen()
            } else if (element.mozRequestFullScreen) { // Firefox
                element.mozRequestFullScreen()
            } else if (element.webkitRequestFullscreen) { // Chrome, Safari & Opera
                element.webkitRequestFullscreen()
            } else if (element.msRequestFullscreen) { // IE/Edge
                element.msRequestFullscreen()
            }
        } else {
            if (document.exitFullscreen) {
                document.exitFullscreen()
            } else if (document.mozCancelFullScreen) {
                document.mozCancelFullScreen()
            } else if (document.webkitExitFullscreen) {
                document.webkitExitFullscreen()
            } else if (document.msExitFullscreen) {
                document.msExitFullscreen()
            }
        }
    }
    /** @returns {string|null} */
    static getColorScheme() {
        if (window.matchMedia) {
            let query = window.matchMedia('(prefers-color-scheme: dark)')
            return query.matches ? app.COLOR_SCHEME_DARK : app.COLOR_SCHEME_LIGHT
        }
        return null
    }
    /** @returns {string} */
    static getIdentifier() {
        return app.identifier
    }
    /** @returns {string} */
    static getLanguage() {
        let languageCode = app.getLanguageCode()
        if (languageCode.includes('-')) {
            languageCode = languageCode.split('-').getFirst()
        }
        return app.LANGUAGE_CODES[languageCode]
    }
    /** @returns {string} */
    static getLanguageCode() {
        return window.navigator.language
    }
    /** @returns {string} */
    static getOrientation() {

    }
    /** @returns {string} */
    static getName() {
        return this.name
    }
    /** @param {string} basename @returns {string} */
    static getPathImages(basename) {
        let pathInfo = util.path_info(basename)
        if (!pathInfo['extension']) {
            basename += '.png'
        }
        if (basename.includes(app.directory('images'))) {
            return basename
        }
        return app.directory('images') + basename
    }
    /** */
    static getPermissions() {

    }
    /** @param {(state: string) => void} callback @returns {void} */
    static getPermissionStatus(permission, callback = (state) => { }) {
        window.navigator.permissions.query({ name: permission }).then((permissionStatus) => {
            callback(permissionStatus.state)
        })
    }
    /** @param {Element} element @returns {void} */
    static inputValidation(element = null) {
        let replaceable = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;'
        }
        let elements = []
        if (element) {
            elements.append(element)
        } else {
            for (let element of document.getElementsByTagName('input')) {
                if (includes(element.type, 'email|password|text|url')) {
                    elements.append(element)
                }
            }
            for (let element of document.getElementsByTagName('textarea')) {
                elements.append(element)
            }
        }
        for (let index = 0; index < elements.length; index++) {
            let element = elements[index]
            if (!element.hasAttribute('maxlength')) {
                element.setAttribute('maxlength', '100')
            }
            if (!element.hasAttribute('autocomplete')) {
                element.setAttribute('autocomplete', 'off')
            }
            element.addEventListener('input', (event) => {
                for (let key in replaceable) {
                    event.target.value = event.target.value.replace(key, '')
                }
            })
        }
    }
    /** @param {string} type @returns {boolean} */
    static isEventInterface(type) {
        for (let [interfaceType, interfaceName] of enumerate(app.EVENT_INTERFACES)) {
            if (type.lower() == interfaceType.lower() || type.lower() == interfaceName.lower()) {
                return true
            }
        }
        return false
    }
    /** @param {number} button @returns {boolean} */
    static isMouseButtonActive(button) {
        return app.mouseButtons[button]
    }
    /** @returns {boolean} */
    static isMouseLeftActive() {
        return app.mouseButtons[app.MOUSE_BUTTON_LEFT]
    }
    /** @returns {boolean} */
    static isMouseRightActive() {
        return app.mouseButtons[app.MOUSE_BUTTON_RIGHT]
    }
    /** @returns {boolean} */
    static isMouseWheelActive() {
        return app.mouseButtons[app.MOUSE_BUTTON_WHEEL]
    }
    /** @returns {boolean} */
    static isOnline() {
        return navigator.onLine
    }
    /** @returns {boolean} */
    static isTouchEnabled() {
        return app.touchable
    }
    /** @returns {boolean} */
    static isTouchDisabled() {
        return !app.touchable
    }
    /** @param {string} path @param {() => void} callback @returns {void} */
    static loadScript(path, callback = () => { }) {

    }
    /** @param {string} type @param {Event} event @returns {void} */
    static onEventListenerInterface(type, event) {
        if (event == null) return
        if (event.target == window.document) return
        let element = app.element(event.target)
        if (app.eventListenerInterfaces[type]) {
            for (let [instance, withinView] of app.eventListenerInterfaces[type]) {
                if (withinView) {
                    if (element.isEqualTo(instance.view, true)) {
                        instance.onEventListenerInterface(event, element)
                    }
                } else {
                    instance.onEventListenerInterface(event, element)
                }
            }
        }
    }
    /** @param {string|URL} url @param {string} target @param {string} features @returns {Window|null} */
    static open(url, target = null, features = null) {
        // https://developer.mozilla.org/en-US/docs/Web/API/Window/open
        if (excludes(target, 'chromeTab|chromeWindow|_blank|mozillaTab|mozillaWindow|_parent|_self|_to|_unfencedTop')) { console.error(`ValueError: variable-name=target variable-value=${target}`) }
        if (features) {
            for (let feature of features.strip(' ,').split(',')) {
                let [featureKey, featureValue] = feature.strip(' ').split('=')
                if (excludes(featureKey, 'attributionsrc|height|innerHeight|innerWidth|left|noopener|noreferrer|popup|screenX|screenY|top|width')) { console.error(`ValueError: variable-name=featureKey variable-value=${featureKey}`) }
                if (excludes(featureValue, 'yes|true|n|{string-number}')) { console.error(`ValueError: variable-name=featureValue variable-value=${featureValue}`) }            
            }
        }
        return window.open(url, target, features)
    }
    /** @param {string} identifier @returns {void} */
    static progressStart(identifier) {
        app.PROGRESS_ACTIVE.append(identifier)
        setTimeout(() => {
            if (app.PROGRESS_ACTIVE.includes(identifier)) {
                app.setTouchable(false)
                app.PROGRESS_DIALOG.setIdentifier(identifier)
                app.PROGRESS_DIALOG.show()
            }
        }, app.PROGRESS_TIMEOUT)
    }
    /** @param {string} identifier @returns {void} */
    static progressStop(identifier) {
        let index = app.PROGRESS_ACTIVE.index(identifier)
        if (index != -1) {
            app.PROGRESS_ACTIVE.pop(index)
        }
        if (app.PROGRESS_ACTIVE.empty()) {
            if (app.PROGRESS_DIALOG.isVisible()) {
                app.setTouchable(true)
                app.PROGRESS_DIALOG.dismiss()
            }
        }
    }
    /** */
    static sendIntent(packageName, className, action, category, uri, type, extras, options, callback) {
    }
    /** @param {any} message @param {string} targetOrigin @param {[]} transfer @returns {void} */
    static sendMessage(message, targetOrigin = "*", transfer = null) {
        window.postMessage(message, targetOrigin, transfer)
    }
    /** */
    static sendText(text, subject, choose) {
    }
    /** @param {number} milliseconds @param {(...args:any) => void} callback @param {...any} args @returns {number} */
    static setInterval(milliseconds, callback, ...args) {
        return setInterval(() => callback(...args), milliseconds)
    }
    /** @param {string} language @returns {void} */
    static setLanguage(language) {
    }
    /** @param {string} theme @returns {void} */
    static setTheme(theme) {
    }
    /** @param {number} milliseconds @param {(...args:any) => void} callback @param {...any} args @returns {number} */
    static setTimeout(milliseconds, callback, ...args) {
        return setTimeout(() => callback(...args), milliseconds)
    }
    /** @param {boolean} value @returns {boolean} */
    static setTouchable(value) {
        app.touchable = value
        return app.touchable
    }
    /** @returns {void} */
    static stop() {
        window.close()
    }
    /** */
    static simulateDrag() {
    }
    /** */
    static simulateKey() {
    }
    /** */
    static simulateScroll() {
    }
    /** */
    static simulateTouch() {
    }
    /** @param {app} instance @returns {void} */
    static sync(instance) {
        app.DIRECTORY = instance.directory_
        app.CONFIGURATION = instance.CONFIGURATION

    }
    /** @param {number} milliseconds @param {function(): void} callback @returns {void} */
    static wait(milliseconds, callback) {
        setTimeout(() => {
            callback()
        }, milliseconds)
    }



    // class
    /** @param {any} value @param {function(any, any): void} callback @returns {DataBinding} */
    static createBinding(value = null, callback = null) {
        return new DataBinding(value, callback)
    }
    /** @returns {void} */
    static createMediaPlayer() {
        return
    }
    /** @returns {ApplicationProgrammingInterface} */
    static createServer() {
        return new ApplicationProgrammingInterface()
    }
    /** @returns {void} */
    static createService() {
        return 
    }
    /** @param {AppElement} element @returns {void} */
    static createTextWatcher(element) {
        return 
        // let element = app.element(event.target)
        // let rows = 0
        // let fontsize = 10
        // let padding = element.style('padding-left').replace('px', '') * 2
        // let text = element.value()
        // let width = element.getWidth(false)

        // let chars_per_line = (width - (padding * 2)) / fontsize
        // text.split('\n').map((line) => {
        //     rows += Math.ceil(line.length / chars_per_line)
        // })
        // element.setProperty('rows', rows)
        // return rows
    }
    /** @returns {ApplicationProgrammingInterface} */
    static createWebConnection() {
        return new ApplicationProgrammingInterface()
    }
    /** @returns {void} */
    static createWebSocket() {
        return
    }
    /** @param {AppElement|Element|string} value @returns {AppElement} */
    static element(value) {
        return new AppElement(value)
    }



    // data
    /** @param {string} key @param {string} prefix @returns {void} */
    static clearData(key, prefix = null) {
        window.localStorage.removeItem(prefix == null ? key : `${prefix}.${key}`)
    }
    /** @param {string} key @param {string} defaultvalue @param {string} prefix @returns {number|string|{}|[]} */
    static getData(key, defaultvalue = '', prefix = null) {
        let string = window.localStorage.getItem(prefix == null ? key : `${prefix}.${key}`)
        if (string) {
            if (util.istype(string, 'string-array|string-object')) {
                return util.json_decode(string)
            }
            if (util.istype(string, 'string-number')) {
                return Number(string)
            }
            return string
        } else if (defaultvalue) {
            app.setData(key, defaultvalue, prefix)
            return defaultvalue
        }
    }
    /** @param {string} key @param {string} prefix @returns {void} */
    static removeData(key, prefix = null) {
        window.localStorage.removeItem(prefix == null ? key : `${prefix}.${key}`)
    }
    /** @param {string} key @param {string|[]|{}} value @param {string} prefix @returns {void} */
    static setData(key, value, prefix = null) {
        if (util.istype(value, 'array|object')) {
            value = util.json_encode(value)
        }
        window.localStorage.setItem(prefix == null ? key : `${prefix}.${key}`, value)
    }



    // document
    /** @param {string|{string:string}} values @returns {HTMLScriptElement} */
    static addScript(attributes) {
        attributes = object.fromdata(attributes)
        for (let key in attributes) {
            if (excludes(key, 'async|charset|defer|id|src|type')) return console.error(`ValueError: variable-name=key variable-value=${key}`)
        }
        let script = window.document.createElement('script')
        for (let [key, value] in enumerate(attributes)) {
            script[key] = value
        }
        window.document.body.appendChild(script)
        return script
    }
    // document styling
    /** @param {string} selector @param {string} propertyKey @returns {string} */
    static getStyleProperty(selector, propertyKey) {
        let element = window.document.querySelector(selector)
        let styleDeclaration = window.getComputedStyle(element)
        return styleDeclaration.getPropertyValue(propertyKey)
    }
    /** @param {string} selector @param {string} propertyKey @param {string|null} propertyValue @param {string} priority @returns {void} */
    static setStyleProperty(selector, propertyKey, propertyValue, priority = '') {
        if (excludes(priority, 'important|undefined|')) return console.error(`ValueError: variable-name=priority variable-value=${priority}`)
        let element = window.document.querySelector(selector)
        if (element) {
            /** @type {CSSStyleDeclaration} */
            let styleDeclaration = element.style
            styleDeclaration.setProperty(propertyKey, propertyValue, priority)
        } else {
            console.error(`UnsetError: variable-name=selector`)
        }
    }
    // document body
    /** @returns {AppElement} */
    static body() {
        return app.element('body')
    }
    /** @param {...AppElement|Element|string} values @returns {boolean} */
    static containsElement(...values) {
        return AppElement.hasElement(...values)
    }
    /** @returns {number} */
    static getHeight() {
        let element = app.element('body')
        return element.getHeight(true)
    }
    /** @returns {number} */
    static getWidth() {
        let element = app.element('body')
        return element.getWidth(true)
    }
    /** @returns {void} */
    static hide() {
        app.element('body').hide()
    }
    /** @returns {void} */
    static show() {
        app.element('body').show()
    }

    

    // device
    /** @returns {number} */
    static getDeviceMemory() {
        // https://developer.mozilla.org/en-US/docs/Web/API/Navigator/deviceMemory
        // returns the approximate amount of device memory in gigabytes.
        return window.navigator.deviceMemory
    }
    /** @returns {number} */
    static getDevicePixelRatio() {
        // https://developer.mozilla.org/en-US/docs/Web/API/Window/devicePixelRatio
        return window.devicePixelRatio
    }
    /** @returns {string} */
    static getDeviceType() {
        return app.getWidth() < app.getHeight() ? app.DEVICE_PHONE : app.DEVICE_COMPUTER
    }
    /** @param {function(boolean): void} callback @returns {void} */
    static isDeviceCharging(callback) {
        window.navigator.getBattery().then((batteryManager) => {
            callback(batteryManager.charging)
        })
    }
    /** @returns {boolean} */
    static isDevicePhone() {
        return app.getWidth() < app.getHeight()
    }
    /** @returns {boolean} */
    static isDeviceComputer() {
        return app.getWidth() > app.getHeight()
    }
    /** @returns {boolean} */
    static isFullscreen() {
        return window.screenTop > 0 && window.screenY > 0
    }
    /** @param {KeyboardEvent} event @param {string} value @returns {boolean} */
    static isKey(event, value) {
        if (!(event instanceof KeyboardEvent)) {
            return false
        }
        for (let key of value.strip(' |').split('|')) {
            key = key.strip(' ')
            if (key.lower() == event.code.lower() || key.lower() == event.key.lower()) {
                return true
            }
        }
        return false
    }



    // request
    /** @param {string} url @param {string} responseType  @returns {ArrayBuffer|Blob|FormData|[]|{}|string}} */
    static async getFile(url, responseType = '') {
        let response = await fetch(url)
        if (!response.ok) {
            throw new Error(`app.getFile(url=${url}): response.status=${response.status}`)
        }
        let responseValue = null
        if (responseType == '') {
            responseValue = await response.json()
        }
        if (responseType == 'arraybuffer') {
            responseValue = await response.arrayBuffer()
        }
        if (responseType == 'blob') {
            responseValue = await response.blob()
        }
        if (responseType == 'formData') {
            responseValue = await response.formData()
        }
        if (responseType == 'json') {
            responseValue = await response.json()
        }
        if (responseType == 'text') {
            responseValue = await response.text()
        }
        return responseValue
    }



    // view
    /** @param {{string:string}|string} attributes @returns {View} */
    static createButton(attributes) {
        let view = new Button(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createCalender(attributes) {
        let view = new Calender(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createCanvas(attributes) {
        let view = new Canvas(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createCheckBox(attributes) {
        let view = new Checkbox(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createDivider(attributes) {
        let view = new Divider(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createDrawer(attributes) {
        let view = new Drawer(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createImage(attributes) {
        let view = new Image(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createList(attributes) {
        let view = new List(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createMenu(attributes) {
        let view = new Menu(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createMenuBar(attributes) {
        let view = new MenuBar(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createPopup(attributes) {
        let view = new Popup(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createPopupMenu(attributes) {
        let view = new PopupMenu(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createProgressBar(attributes) {
        let view = new ProgressBar(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createRadioButton(attributes) {
        let view = new RadioButton(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createRadioGroup(attributes) {
        let view = new RadioGroup(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createScroller(attributes) {
        let view = new Scroller(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createSeekBar(attributes) {
        let view = new SeekBar(attributes)
        return view
    }
    /** @param {string|string[][]} items @returns {AppElement} */
    static createSelect(items) {
        let itemsData = array.fromdata(items)
        let view = app.element('select')
        for (let itemData of itemsData) {
            let [title, value] = itemData
            let option = app.element('option')
            option.text(title)
            option.value(value)
            view.appendChild(option)
        }
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createSelector(attributes) {
        let view = new Selector(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createSearch(attributes) {
        let view = new Search(attributes)
        return view
    }
    /** @param {string|string[][]} items @returns {AppElement} */
    static createSpinner(items) {
        return app.createSelect(items)
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createSwitch(attributes) {
        let view = new Switch(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createTab(attributes) {
        let view = new Tab(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createTabs(attributes) {
        let view = new Tabs(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createTable(attributes) {
        let view = new Table(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createToggle(attributes) {
        let view = new Toggle(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createToolbar(attributes) {
        let view = new Toolbar(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createVideo(attributes) {
        let view = new Video(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createViewSwitcher(attributes) {
        let view = new ViewSwitcher(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createWebView(attributes) {
        let view = new WebView(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createWindow(attributes) {
        let view = new Window(attributes)
        return view
    }
    // dialog
    /** @param {{string:string}|string} attributes @returns {View} */
    static createDialog(attributes) {
        let view = new Dialog(attributes)
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createConfirmDialog(attributes) {
        let view = new Dialog(attributes)
        view.setPositiveButton('OK')
        view.setNegativeButton('CANCEL')
        return view
    }
    /** @param {{string:string}|string} attributes @param {string|string[][]} items @returns {View} */
    static createListDialog(attributes, items) {
        let view = new Dialog(attributes)
        let list = app.createList(attributes)
        list.setItems(items)
        view.setBody(list.getView())
        return view
    }
    /** @param {{string:string}|string} attributes @returns {View} */
    static createProgressDialog(attributes) {
        let view = new DialogProgress(attributes)
        return view
    }
    static storage = {
        key: util.path_info(null, 'filename'),
        get: (key, value = null, use = false) => {
            let string = window.localStorage.getItem(use ? app.storage.key + '.' + key : key)
            if (string) {
                return string
            } else if (value) {
                window.localStorage.setItem(use ? app.storage.key + '.' + key : key, value)
                return value
            }
        },
        set: (key, value, use = false) => {
            window.localStorage.setItem(use ? app.storage.key + '.' + key : key, value)
            return util.storage
        },
        remove: (key, use = false) => {
            window.localStorage.removeItem(use ? app.storage.key + '.' + key : key)
            return util.storage
        },
    }
}
//_________________________________________________________________________________________________________________________________________________//
class ApplicationProgrammingInterface {
    constructor() {
        // https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest
        /** @type {function(ProgressEvent): void} */
        this.onAbortListener = ApplicationProgrammingInterface.onAbortListener
        /** @type {function(ProgressEvent): void} */
        this.onErrorListener = ApplicationProgrammingInterface.onErrorListener
        /** @type {function(ProgressEvent): void} */
        this.onLoadListener = ApplicationProgrammingInterface.onLoadListener
        /** @type {function(ProgressEvent): void} */
        this.onLoadEndListener = ApplicationProgrammingInterface.onLoadEndListener
        /** @type {function(ProgressEvent): void} */
        this.onLoadStartListener = ApplicationProgrammingInterface.onLoadStartListener
        /** @type {function(ProgressEvent): void} */
        this.onProgressListener = ApplicationProgrammingInterface.onProgressListener
        /** @type {function(Event): void} */
        this.onReadyStateChangeListener = ApplicationProgrammingInterface.onReadyStateChangeListener
        /** @type {function(any): void} */
        this.onResponseListener = ApplicationProgrammingInterface.onResponseListener
        /** @type {XMLHttpRequest} */
        this.request = null
        /** @type {boolean} */
        this.requestAsynchronous = false
        /** @type {any} */
        this.requestBody = null
        /** @type {string} */
        this.requestController = ''
        /** @type {object} */
        this.requestHeaders = new object()
        /** @type {string} */
        this.requestIdentifier = null
        /** @type {string} */
        this.requestMimeType = 'text/xml'
        /** @type {string} */
        this.requestPassword = null
        /** @type {string} */
        this.requestQuery = ''
        /** @type {string} */
        this.requestResponseValueDefault = null
        /** @type {string} */
        this.requestResponseType = null
        /** @type {string} */
        this.requestRoute = ''
        /** @type {string} */
        this.requestUsername = null
        /** @type {number} */
        this.requestTimeout = 0
        /** @type {string} */
        this.requestURL = null
        /** @type {boolean} */
        this.requestWithCredentials = false
    }

    /** @readonly @type {string} */
    static METHOD_DELETE = "DELETE"
    /** @readonly @type {string} */
    static METHOD_GET = "GET"
    /** @readonly @type {string} */
    static METHOD_HEAD = "HEAD"
    /** @readonly @type {string} */
    static METHOD_OPTIONS = "OPTIONS"
    /** @readonly @type {string} */
    static METHOD_PUT = "PUT"
    /** @readonly @type {string} */
    static METHOD_POST = "POST"
    /** @readonly @type {string} */
    static METHOD_TRACE = "TRACE"

    /** @readonly @type {number} */
    static READY_STATE_UNSET = 0
    /** @readonly @type {number} */
    static READY_STATE_OPENED = 1
    /** @readonly @type {number} */
    static READY_STATE_HEADERS_RECEIVED = 2
    /** @readonly @type {number} */
    static READY_STATE_LOADING = 3
    /** @readonly @type {number} */
    static READY_STATE_DONE = 4

    /** @readonly @type {string} */
    static RESPONSE_TYPE_DEFAULT = ""
    /** @readonly @type {string} */
    static RESPONSE_TYPE_ARRAYBUFFER = "arraybuffer"
    /** @readonly @type {string} */
    static RESPONSE_TYPE_BLOB = "blob"
    /** @readonly @type {string} */
    static RESPONSE_TYPE_DOCUMENT = "document"
    /** @readonly @type {string} */
    static RESPONSE_TYPE_JSON = "json"
    /** @readonly @type {string} */
    static RESPONSE_TYPE_TEXT = "text"

    /** @type {function(ProgressEvent): void} */
    static onAbortListener = (event) => { }
    /** @type {function(ProgressEvent): void} */
    static onErrorListener = (event) => { }
    /** @type {function(ProgressEvent): void} */
    static onLoadListener = (event) => { }
    /** @type {function(ProgressEvent): void} */
    static onLoadEndListener = (event) => { }
    /** @type {function(ProgressEvent): void} */
    static onLoadStartListener = (event) => { }
    /** @type {function(ProgressEvent): void} */
    static onProgressListener = (event) => { }
    /** @type {function(Event): void} */
    static onReadyStateChangeListener = (event) => { }
    /** @type {function(any): void} */
    static onResponseListener = (data) => { }

    /** @returns {void} */
    abort() {
        this.request.abort()
        return this
    }
    /** @param {boolean} value @returns {ApplicationProgrammingInterface} */
    asynchronous(value) {
        this.requestAsynchronous = value
        return this
    }
    /** @param {any} value @returns {ApplicationProgrammingInterface} */
    body(body) {
        if (util.istype(body, 'array|object')) {
            body = util.json_encode(body)
        }
        this.requestBody = body
        return this
    }
    /** @param {string} controller @returns {ApplicationProgrammingInterface} */
    controller(controller) {
        if (controller == '' || controller == null) {
            this.requestController = ''
        } else {
            this.requestController = controller[0] == '/' ? controller : `/${controller}`
        }
        return this
    }
    /** @param {string} route @returns {any} */
    delete(route = null) {
        this.#setRequest(ApplicationProgrammingInterface.METHOD_DELETE, route)
        this.request.send()
        return this.#getResponse()
    }
    /** @param {string} route @returns {any} */
    get(route = null) {
        this.#setRequest(ApplicationProgrammingInterface.METHOD_GET, route)
        this.request.send()
        return this.#getResponse()
    }
    /** @param {string} headerKey @param {string} headerValue @returns {ApplicationProgrammingInterface|string} */
    header(headerKey, headerValue) {
        this.requestHeaders.set(headerKey, headerValue)
        return this
    }
    /** @param {string|{string:string}} value @returns {ApplicationProgrammingInterface|string} */
    headers(value) {
        let headers = object.fromdata(value)
        this.requestHeaders.update(headers)
        return this
    }
    /** @param {string} value @returns {ApplicationProgrammingInterface} */
    mimeType(value) {
        this.requestMimeType = value
        return this
    }
    /** @param {function(ProgressEvent): void} listener @returns {ApplicationProgrammingInterface} */
    onabort(listener) {
        this.onAbortListener = listener
        return this
    }
    /** @param {function(ProgressEvent): void} listener @returns {ApplicationProgrammingInterface} */
    onerror(listener) {
        this.onErrorListener = listener
        return this
    }
    /** @param {function(ProgressEvent): void} listener @returns {ApplicationProgrammingInterface} */
    onload(listener) {
        this.onLoadListener = listener
        return this
    }
    /** @param {function(ProgressEvent): void} listener @returns {ApplicationProgrammingInterface} */
    onloadend(listener) {
        this.onLoadEndListener = listener
        return this
    }
    /** @param {function(ProgressEvent): void} listener @returns {ApplicationProgrammingInterface} */
    onloadstart(listener) {
        this.onLoadStartListener = listener
        return this
    }
    /** @param {function(ProgressEvent): void} listener @returns {ApplicationProgrammingInterface} */
    onprogress(listener) {
        this.onProgressListener = listener
        return this
    }
    /** @param {function(ProgressEvent): void} listener @returns {ApplicationProgrammingInterface} */
    onreadystatechange(listener) {
        this.onReadyStateChangeListener = listener
        return this
    }
    /** @param {function(any): void} listener @returns {ApplicationProgrammingInterface} */
    onresponse(listener) {
        this.onResponseListener = listener
        return this
    }
    /** @param {string} value @returns {ApplicationProgrammingInterface} */
    password(value) {
        this.requestPassword = value
        return this
    }
    /** @param {string} route @returns {any} */
    post(route = null) {
        this.#setRequest(ApplicationProgrammingInterface.METHOD_POST, route)
        this.request.send(this.requestBody)
        return this.#getResponse()
    }
    /** @param {string} route @returns {any} */
    put(route = null) {
        this.#setRequest(ApplicationProgrammingInterface.METHOD_PUT, route)
        this.request.send(this.requestBody)
        return this.#getResponse()
    }
    /** @param {string|{string:string}} value @returns {ApplicationProgrammingInterface} */
    query(value) {
        this.requestQuery = '?'
        let query = object.fromdata(value)
        for (let [queryKey, queryValue] of enumerate(query)) {
            this.requestQuery += `${this.requestQuery.length == 1 ? '' : '&'}${queryKey}=${queryValue}`
        }
        return this
    }
    /** @returns {any} */
    response() {
        let response = this.request.response
        if (this.responseCodeError() && response == '') {
            return this.requestResponseValueDefault ? this.requestResponseValueDefault : response
        }
        if (this.responseHeader('content-type') == 'application/json') {
            return util.json_decode(response)
        }
        if (this.responseHeader('content-type') == 'text/plain') {
            if (util.istype(response, 'string-array|string-object')) {
                return util.json_decode(response)
            }
            else if (util.istype(response, 'string-boolean')) {
                return response == 'true'
            }
            else if (util.istype(response, 'string-number')) {
                return Number(response)
            }
            else {
                return response
            }
        }
        if (this.responseHeader('content-type') == 'image/png') {

        }
        return response
    }
    /** @returns {number} */
    responseCode() {
        return this.request.status
    }
    /** @returns {boolean} */
    responseCodeError() {
        return this.responseCodeErrorClient() || this.responseCodeErrorServer()
    }
    /** @returns {boolean} */
    responseCodeErrorClient() {
        return 400 <= this.request.status && this.request.status <= 499
    }
    /** @returns {boolean} */
    responseCodeErrorServer() {
        return 500 <= this.request.status && this.request.status <= 599
    }
    /** @returns {boolean} */
    responseCodeInformational() {
        return 100 <= this.request.status && this.request.status <= 199
    }
    /** @returns {boolean} */
    responseCodeRedirection() {
        return 300 <= this.request.status && this.request.status <= 399
    }
    /** @returns {boolean} */
    responseCodeSuccessful() {
        return 200 <= this.request.status && this.request.status <= 299
    }
    /** @param {any} responseValueDefault @returns {ApplicationProgrammingInterface} */
    responseDefault(responseValueDefault) {
        this.requestResponseValueDefault = responseValueDefault
        return this
    }
    /** @param {string} header @returns {string|null} */
    responseHeader(header) {
        let headers = this.responseHeaders()
        return headers.get(header)
    }
    /** @returns {{string:string}} */
    responseHeaders() {
        let headers = new object()
        for (let header of this.request.getAllResponseHeaders().split('\r\n')) {
            headers.set(...header.split(': '))
        }
        return headers
    }
    /** @returns {number} */
    responseStatus() {
        return this.request.status
    }
    /** @returns {string} */
    responseStatusText() {
        return this.request.statusText
    }
    /** @returns {string} */
    responseText() {
        return this.request.responseText
    }
    /** @param {string} responseType @returns {ApplicationProgrammingInterface} */
    responseType(responseType) {
        this.requestResponseType = responseType
        return this
    }
    /** @returns {string} */
    responseURL() {
        return this.request.responseURL
    }
    /** @returns {Document} */
    responseXML() {
        return this.request.responseXML
    }
    /** @param {string} route @returns {ApplicationProgrammingInterface} */
    route(route) {
        this.requestRoute = route[0] == '/' ? route : `/${route}`
        return this
    }
    /** @param {function(ProgressEvent): void} listener @returns {void} */
    setOnAbortListener(listener) {
        this.onAbortListener = listener
    }
    /** @param {function(ProgressEvent): void} listener @returns {void} */
    setOnErrorListener(listener) {
        this.onErrorListener = listener
    }
    /** @param {function(ProgressEvent): void} listener @returns {void} */
    setOnLoadListener(listener) {
        this.onLoadListener = listener
    }
    /** @param {function(ProgressEvent): void} listener @returns {void} */
    setOnLoadEndListener(listener) {
        this.onLoadEndListener = listener
    }
    /** @param {function(ProgressEvent): void} listener @returns {void} */
    setOnLoadStartListener(listener) {
        this.onLoadStartListener = listener
    }
    /** @param {function(ProgressEvent): void} listener @returns {void} */
    setOnProgressListener(listener) {
        this.onProgressListener = listener
    }
    /** @param {function(ProgressEvent): void} listener @returns {void} */
    setOnReadyStateChangeListener(listener) {
        this.onReadyStateChangeListener = listener
    }
    /** @param {function(any): void} listener @returns {void} */
    setOnResponseListener(listener) {
        this.onResponseListener = listener
    }
    /** @param {number} timeout @returns {ApplicationProgrammingInterface} */
    timeout(timeout) {
        this.requestTimeout = timeout
    }
    /** @param {string} url @returns {ApplicationProgrammingInterface} */
    url(url) {
        this.requestController = ''
        this.requestRoute = ''
        this.requestQuery = ''
        this.requestURL = url
        return this
    }
    /** @param {string} value @returns {ApplicationProgrammingInterface} */
    username(value) {
        this.requestUsername = value
        return this
    }
    /** @param {boolean} value @returns {ApplicationProgrammingInterface} */
    withCredentials(value) {
        this.request.withCredentials = value
        return this
    }
    /** @returns {any} */
    #getResponse() {
        app.progressStop(this.requestIdentifier)
        return this.response()
    }
    /** @param {string} method @param {string} route @returns {void} */
    #setRequest(method, route) {
        if (route) {
            this.route(route)
        }
        let url = this.requestURL ? this.requestURL : `${this.requestController}${this.requestRoute}${this.requestQuery}`
        this.request = new XMLHttpRequest()
        if (this.requestAsynchronous && this.requestResponseType) {
            this.request.responseType = this.requestResponseType
        }
        this.request.timeout = this.requestTimeout
        this.request.onabort = this.onAbortListener
        this.request.onerror = this.onErrorListener
        this.request.onload = this.onLoadListener
        this.request.onloadend = this.onLoadEndListener
        this.request.onloadstart = this.onLoadStartListener
        this.request.onprogress = this.onProgressListener
        this.request.onreadystatechange = this.onReadyStateChangeListener
        this.request.addEventListener('loadend', (event) => {
            this.onResponseListener(this.response())
        })
        this.request.overrideMimeType(this.requestMimeType)
        this.request.open(method, url, this.requestAsynchronous, this.requestUsername, this.requestPassword)
        for (let [headerKey, headerValue] of enumerate(this.requestHeaders)) {
            this.request.setRequestHeader(headerKey, headerValue)
        }
        this.requestIdentifier = util.identifier()
        this.requestHeaders.clear()
        this.requestQuery = ''
        this.requestRoute = ''
        this.requestURL = null
        if (!this.requestAsynchronous) {
            app.progressStart(this.requestIdentifier)
        }
    }
}
class AppElement {
    /** @param {AppElement|Element|string} value  */
    constructor(value) {
        /** @type {HTMLElement} */
        this.element = null
        if (util.istype(value, 'string')) {
            if (util.istype(value, 'html-tag')) {
                this.element = document.createElement(value)
                this.element.id = util.identifier()
                if (this.getTagName() == 'INPUT' || this.getTagName() == 'TEXTAREA') {
                    app.inputValidation(this.element)
                }
            }
            // else if (AppElement.TAGS_CUSTOM.includes(value)) {
            //     if (value == 'content') {
            //         this.element = app.element('div').class('content').appendChild(
            //             app.element('svg').class('content-background'),
            //             app.element('div').class('content-foreground')
            //         ).getElement()
            //     }
            // }
            else if (util.istype(value, 'html')) {
                this.element = document.createElement('div')
                this.element.innerHTML = value
                this.element = this.element.children[0]
            }
            else {
                this.element = document.getElementById(value)
                if (!this.element) {
                    console.error(value)
                    console.trace()
                }
            }
        }
        if (value instanceof Element) {
            this.element = value
        }
        if (value instanceof AppElement) {
            this.element = value.element
        }

    }

    /** @type {string} */
    static IDENTIFIER_DELIMITER = '.'
    /** @readonly @type {string[]} */
    static TAGS = [
        '!doctype',
        'a', 'abbr', 'address', 'area', 'article', 'aside', 'audio',
        'b', 'base', 'bb', 'bdi', 'bdo', 'big', 'blockquote', 'br', 'button',
        'canvas', 'caption', 'cite', 'code', 'col', 'colgroup',
        'data', 'datalist', 'dd', 'del', 'details', 'dfn', 'dialog', 'div', 'dl', 'dt', 'em', 'embed',
        'fieldset', 'figcaption', 'figure', 'footer', 'form',
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'head', 'header', 'hr', 'html',
        'i', 'iframe', 'img', 'input', 'ins',
        'kbd',
        'label', 'legend', 'li', 'link',
        'main', 'map', 'mark', 'meta', 'meter',
        'nav', 'noscript',
        'object', 'ol', 'optgroup', 'option',
        'p', 'param', 'picture', 'polyline', 'polygon', 'pre', 'progress',
        'q',
        'rp', 'rt', 'ruby',
        's', 'samp', 'script', 'section', 'select', 'small', 'source', 'span', 'strong', 'style', 'sub', 'summary', 'sup', 'svg',
        'table', 'tbody', 'td', 'template', 'textarea', 'tfoot', 'th', 'thead', 'tr', 'track',
        'u', 'ul',
        'var', 'video',
        'wbr'
    ]
    /** @readonly @type {string[]} */
    static TAGS_CUSTOM = [
        'content'
    ]
    /** @readonly @type {string[]} */
    static LISTENERS = [
        'abort', 'afterprint', 'animationend', 'animationiteration', 'animationstart',
        'beforeprint', 'beforeunload', 'blur',
        'canplay', 'canplaythrough', 'change', 'click', 'contextmenu', 'copy', 'cut',
        'dblclick', 'drag', 'dragend', 'dragenter', 'dragleave', 'dragover', 'dragstart', 'drop', 'durationchange',
        'ended', 'error',
        'focus', 'focusin', 'focusout', 'fullscreenchange', 'fullscreenerror',
        'hashchange',
        'input', 'invalid',
        'keydown', 'keyup',
        'load', 'loadeddata', 'loadedmetadata', 'loadstart',
        'message', 'mousedown', 'mouseenter', 'mouseleave', 'mousemove', 'mouseover', 'mouseout', 'mouseup', 'mousewheel',
        'offline', 'online', 'open',
        'pagehide', 'pageshow', 'paste', 'pause', 'play', 'playing', 'popstate', 'progress',
        'ratechange', 'resize', 'reset',
        'scroll', 'search', 'seeked', 'seeking', 'select', 'show', 'stalled', 'storage', 'submit', 'suspend',
        'timeupdate', 'touchstart', 'transitionend',
        'unload',
        'volumechange',
        'waiting', 'wheel'
    ]
    /** @readonly @type {string[]} */
    static propertiesOfPixelValue = ['bottom', 'gap', 'height', 'left', 'marginBottom', 'marginLeft', 'marginRight', 'marginTop', 'max-height', 'max-width', 'paddingBottom', 'paddingLeft', 'paddingRight', 'paddingTop', 'right', 'top', 'width']
    
    /** @param {AppElement|Element|string} value @returns {Element} */
    static convertToElement(value) {
        return new AppElement(value).getElement()
    }
    /** @param {AppElement|Element|string} value @returns {AppElement} */
    static convertToAppElement(value) {
        return new AppElement(value)
    }
    /** @param {...AppElement|Element|string} values @returns {boolean} */
    static hasElement(...values) {
        /** @type {string} */
        let value = null
        if (values.length == 1) {
            if (typeof values[0] === 'string') {
                value = values[0]
            } else if (values[0] instanceof Element) {
                value = values[0].id
            } else if (values[0] instanceof AppElement) {
                value = values[0].id()
            }
        } else {
            value = values.join('.')
        }
        return document.getElementById(value) != null
    }

    accessKey(value = "hh") {
        // The accesskey attribute specifies a shortcut key to activate/focus an element. (IE=Alt+accesskey, Chrome=Alt+accesskey, Safari=Alt+accessKey, Firefox=Alt+Shift+accesskey)
        if (value == undefined) return this.element.accessKey
        else this.element.accessKey = value
        return this
    }
    /** @param {string} type @param {function(Event, AppElement)} listener @param {boolean|{capture: boolean, once: boolean, passive: boolean, signal: AbortSignal}} options @returns {AppElement} */
    addEventListener(type = null, listener = (e) => { }, options = false) {
        this.element.addEventListener(type, listener, options)
        return this
    }
    /** @param {array} keyframes @param {number|{delay: number, direction: ["normal", "reverse", "alternate", "alternate-reverse"], duration: number, easing: ["linear", "ease", "ease-in", "ease-out", "ease-in-out", "cubic-bezier()"] fill: ["none", "backward", "forward", "both"], iterations: number, pseudoElement: string, rangeEnd: string, rangeStart: string }} options @returns {Animation} */
    animate(keyframes, options) {
        // https://developer.mozilla.org/en-US/docs/Web/API/Element/animate
        return this.element.animate(keyframes, options)
    }
    /** @param {...AppElement|Element} elements @returns {AppElement} */
    appendChild(...elements) {
        for (let element of elements) {
            element = AppElement.convertToElement(element)
            this.element.appendChild(element)
        }
        return this
    }
    /** @returns {AppElement} */
    blur() {
        this.element.blur()
        return this
    }
    /** @returns {AppElement} */
    click() {
        this.element.click()
        return this
    }
    /** @param {number} index @returns {AppElement|AppElement[]} */
    children(index = null) {
        // children=collection of an element's child element (excluding text and comment nodes)
        // childNodes=collection of an element's child nodes (including text and comment nodes)
        let elements = []
        for (let i = 0; i < this.element.children.length; i++) {
            let element = app.element(this.element.children[i])
            elements.push(element)
        }
        if (index == null) return elements
        return elements[index < 0 ? index + elements.length : index]
    }
    /** @param {boolean} deep @returns {AppElement} */
    cloneNode(deep = null) {
        let element = this.element.cloneNode(deep)
        return app.element(element)
    }
    /** @param {AppElement|Element} value @returns {boolean} */
    contains(value) {
        return this.element.contains(app.element(value).getElement())
    }
    /** @param {boolean} value @returns {boolean} */
    contentEditable(value = null) {
        if (value == null) return this.element.contentEditable
        else this.element.contentEditable = value
        return this
    }
    /** @param {string} type @param {{ bubbles: boolean; cancelable: boolean; }} @returns {AppElement} */
    dispatchEvent(type, options = { bubbles: true, cancelable: true }) {
        let event = new Event(type, options)
        this.element.dispatchEvent(event)
        return this
    }
    /** @param {{ preventScroll: boolean, focusVisible: boolean }} options @returns {AppElement} */
    focus(options) {
        this.element.focus(options)
        return this
    }
    /** @param {string} key @param {string} defaultvalue @returns {string|null} */
    getAttribute(key, defaultvalue = null) {
        let value = this.element.getAttribute(key)
        return value ? value : defaultvalue
    }
    /** @param {string} key @returns {DOMRect|number} */
    getBoundingClientRect(key = null) {
        let DOMRect = this.element.getBoundingClientRect()
        return key == null ? DOMRect : DOMRect[key]
    }
    /** @param {string} classNames @returns {AppElement[]} */
    getElementsByClassName(classNames) {
        let elements = []
        for (let element of this.element.getElementsByClassName(classNames)) {
            elements.append(app.element(element))
        }
        return elements
    }
    /** @param {string} qualifedName @returns {AppElement[]} */
    getElementsByTagName(qualifedName) {
        let elements = []
        for (let element of this.element.getElementsByTagName(qualifedName)) {
            elements.append(app.element(element))
        }
        return elements
    }
    /** @param {string} namespaceURI @param {string} localName  @returns {AppElement[]} */
    getElementsByTagNameNS(namespaceURI, localName) {
        let elements = []
        for (let element of this.element.getElementsByTagNameNS(namespaceURI, localName)) {
            elements.append(app.element(element))
        }
        return elements
    }
    /** @returns {number} */
    getNodeType() {
        // 1=Element, 2=Attr, 3=Text, 4=CDATASection, 5=EntityReference, 6=Entity, 7=ProcessingInstruction, 8=Comment, 9=Document, 10=DocumentType, 11=DocumentFragment, 12=Notation
        return this.element.nodeType
    }
    /** @param {string} characterCase @returns {string} */
    getTagName(characterCase = 'upper') {
        if (characterCase == 'upper') {
            return this.element.tagName.upper()
        }
        else if (characterCase == 'lower') {
            return this.element.tagName.lower()
        }
        return this.element.tagName
    }
    /** @param {string} key @returns {boolean} */
    hasAttribute(key) {
        return this.element.hasAttribute(key)
    }
    /** @returns {boolean} */
    hasChildNodes() {
        return this.element.hasChildNodes()
    }
    /** @param {...string|...number} values @returns {AppElement|string} */
    id(...values) {
        if (values.length == 0) {
            return this.element.id
        }
        else {
            if (util.istype(values[0], 'number')) {
                let strings = this.element.id.split('.')
                return strings[values[0] < 0 ? values[0] + strings.length : values[0]]
            }
            if (util.istype(values, 'array-string')) {
                this.element.id = values.join(AppElement.IDENTIFIER_DELIMITER)
            }
        }
        // if (value == null) return this.element.id
        // this.element.id = value
        return this
    }
    /** @param {string} value @param {boolean} append @returns {AppElement|string} */
    innerHTML(value = null, append = false) {
        if (value == null) return this.element.innerHTML
        else this.element.innerHTML = append ? this.element.innerHTML + value : value
        return this
    }
    /** @param {string} [position="afterbegin"|"afterend"|"beforebegin"|"beforeend"] @param {AppElement|Element|string} value @returns {AppElement} */
    insertAdjacent(position, value) {
        if (util.istype(value, 'element')) {
            value = app.element(value)
            this.element.insertAdjacentHTML(position, value.outerHTML())
        } else {
            let tags = AppElement.TAGS.map((tag) => [`<${tag}>`, `<${tag}/>`])
            if (tags.some((tag) => value.includes(tag[0]) && value.includes(tag[1]))) {
                this.element.insertAdjacentHTML(position, value)
            } else {
                this.element.insertAdjacentText(position, value)
            }
        }
        return this
    }
    /** @param {number} position @param {AppElement|Element|string} newElement @returns {AppElement} */
    insertBefore(position, newElement) {
        newElement = app.element(newElement)
        let existingElement = null
        if (util.istype(position, 'number')) {
            existingElement = this.children(position)
        } else {
            existingElement = app.element(position)
        }
        this.element.insertBefore(newElement.getElement(), existingElement.getElement())
        return this
    }
    /** @returns {boolean} */
    isContentEditable() {
        return this.element.isContentEditable
    }
    /** @param {AppElement|Element|string} value @returns {boolean} */
    isSameNode(value) {
        let element = app.element(value).getElement()
        return this.element.isSameNode(element)
    }
    /** @param {string} value @returns {AppElement|string} */
    outerHTML(value = null) {
        if (value == null) return this.element.outerHTML
        else this.element.outerHTML = value
        return this
    }
    /** @param {number} count @returns {AppElement} */
    parentElement(count = 1) {
        let element = this.element
        for (let i = 0; i < count; i++) {
            element = element.parentElement
        }
        return app.element(element)
    }
    /** @returns {void} */
    remove() {
        this.element.remove()
        return this
    }
    /** @param {string} key @returns {AppElement} */
    removeAttribute(key) {
        this.element.removeAttribute(key)
        return this
    }
    /** @param {...AppElement|Element|string} values @returns {AppElement} */
    removeChild(...values) {
        for (let value of values) {
            let element = app.element(value).getElement()
            this.element.removeChild(element)
        }
        return this
    }
    /** @param {string} type @param {function(Event): void} callback @param {boolean|{capture: boolean}} options @returns {AppElement} */
    removeEventListener(type, callback, options) {
        this.element.removeEventListener(type, callback, options)
        return this
    }
    /** @param {AppElement|Element|string} newChild @param {AppElement|Element|string} oldChild @returns {AppElement} */
    replaceChild(newChild, oldChild) {
        newChild = app.element(newChild).getElement()
        oldChild = app.element(oldChild).getElement()
        this.element.replaceChild(newChild, oldChild)
        return this
    }
    /** @param {number} x @param {number} y @param {string} @returns {void} */
    scroll(x, y, behavior = 'smooth') {
        if (excludes(behavior, 'auto|instant|smooth')) return console.error(`ValueError: variable-name=behavior variable-value=${behavior}`)
        this.element.scroll({
            'top': y,
            'left': x,
            'behavior': behavior
        })
    }
    /** @param {number} x @param {number} y @param {string} @returns {void} */
    scrollBy(x, y, behavior = 'smooth') {
        if (excludes(behavior, 'auto|instant|smooth')) return console.error(`ValueError: variable-name=behavior variable-value=${behavior}`)
        this.element.scrollBy({
            'top': y,
            'left': x,
            'behavior': behavior
        })
    }
    /** @param {boolean|Object} options @returns {AppElement} */
    scrollIntoView(options = { 'behavior': 'smooth', 'block': 'start', 'inline': 'nearest' }) {
        if (util.istype(options, 'object')) {
            if ('behavior' in options) {
                let behavior = options['behavior']
                if (excludes(behavior, 'auto|instant|smooth')) return console.error(`ValueError: variable-name=options.behavior variable-value=${behavior}`)
            }
            if ('block' in options) {
                let block = options['block']
                if (excludes(block, 'center|end|start')) return console.error(`ValueError: variable-name=options.block variable-value=${block}`)
            }
            if ('inline' in options) {
                let inline = options['inline']
                if (excludes(inline, 'center|end|nearest|start')) return console.error(`ValueError: variable-name=options.inline variable-value=${inline}`)
            }
        }
        this.element.scrollIntoView(options)
        return this
    }
    /** @param {number} x @param {number} y @param {string} behavior @returns {void} */
    scrollTo(x, y, behavior = 'smooth') {
        if (excludes(behavior, 'auto|instant|smooth')) return console.error(`ValueError: variable-name=behavior variable-value=${behavior}`)
        this.element.scrollTo({
            'top': y,
            'left': x,
            'behavior': behavior,
        })
    }
    /** @returns {void} */
    select() {
        this.element.focus()
        this.element.select()
    }
    /** @param {string} key @param {string} value @returns {AppElement} */
    setAttribute(key, value = '') {
        this.element.setAttribute(key, value)
        return this
    }
    /** @param {any} value @returns {*|AppElement} */
    something(value = null) {
        if (value == null) return this.element.something
        else this.element.something = value
        return this
    }
    /** @param {...string} values @returns {AppElement|string} */
    src(...values) {
        if (values.length == 0) return this.element.src
        else this.element.src = values.join('/')
        return this
    }
    /** @param {...string} values @returns {AppElement|string} */
    _style(...values) {
        let set = (key, value) => {
            if (AppElement.propertiesOfPixelValue.includes(key)) {
                let append = true
                if (key == 'height' || key == 'width') {
                    append = !(value == 'auto' || value == 'inherit' || value == 'initial' || value == 'fit-content' || value == 'max-content' || value == 'min-content' || value == 'revert' || value == 'unset')
                }
                append = append && !(value.toString().includes('px') || value.toString().includes('%'))
                value += append ? 'px' : ''
            }
            this.element.style[key] = value
        }
        if (values.length == 1) {
            if (values[0].includes(':')) {
                let object = util.css_decode(values[0])
                for (let key in object) {
                    set(key, object[key])
                }
            } else {
                return this.element.style[values[0]]
            }
        } else {
            for (let i = 0; i < values.length; i += 2) {
                set(values[i], values[i + 1])
            }
        }
        return this
    }
    /** @param {string} value @param {boolean} append @returns {AppElement|string} */
    value(value, append = false) {
        if (value == null) return this.element.value
        else this.element.value = append ? this.element.value + value : value
        return this
    }
    




    /** @param {string} type @param {function(Event, AppElement)} listener @param {boolean|{capture: boolean, once: boolean, passive: boolean, signal: AbortSignal}} options @returns {AppElement} */
    addListener(type, listener, options = false) {
        if (type == 'lgclick') {
            this.element.addEventListener('touchstart', (event) => {
                this.longClickListenerTimeout = setTimeout(() => {
                    if (app.isTouchDisabled()) return
                    if (!event.target) return
                    if (!(this.element == event.target || this.element.contains(event.target))) return
                    let element = app.element(event.target)
                    listener(event, element)
                }, 2000)
            })
            this.element.addEventListener('touchmove', (event) => {
                clearTimeout(this.longClickListenerTimeout)
            })
            this.element.addEventListener('touchend', (event) => {
                clearTimeout(this.longClickListenerTimeout)
            })
            this.element.addEventListener('mousedown', (event) => {
                this.longClickListenerTimeout = setTimeout(() => {
                    if (app.isTouchDisabled()) return
                    if (!event.target) return
                    if (!(this.element == event.target || this.element.contains(event.target))) return
                    let element = app.element(event.target)
                    listener(event, element)
                }, 2000)
            })
            this.element.addEventListener('mousemove', (event) => {
                clearTimeout(this.longClickListenerTimeout)
            })
            this.element.addEventListener('mouseup', (event) => {
                clearTimeout(this.longClickListenerTimeout)
            })
        }
        this.element.addEventListener(type, (event) => {
            if (app.isTouchDisabled()) return
            if (!event.target) return
            if (!(this.element == event.target || this.element.contains(event.target))) return
            let element = app.element(event.target)
            listener(event, element)
        }, options)
        return this
    }
    /** @param {DataBinding} binding @param {function(AppElement, DataBinding): void} @returns {AppElement} */
    addDataBindingListener(binding, onchange = (binding, element) => { }) {
        binding.setOnChangeListener((newValue, oldValue) => onchange(binding, this))
        return this
    }
    /** @param {object} options @param {function(AppElement, MutationObserver, MutationRecord[]): void} listener  @returns {AppElement} */
    addMutationObserver(options = { childList: true }, listener) {
        // https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver
        let observer = new MutationObserver((mutationList, observer) => {
            listener(this, observer, mutationList)
        })
        observer.observe(this.element, { childList: true })
        return this
    }
    /** @param {...string} value @returns {AppElement} */
    addClass(...values) {
        for (let value of values) {
            this.element.classList.add(value)
        }
        return this
    }
    /** @param {string|string[]|{string:string}} value @returns {AppElement|string|null} */
    attribute(value) {
        if (util.istype(value, 'string') && value.includes(':')) {
            return this.setAttributes(value)
        }
        if (util.istype(value, 'object')) {
            return this.setAttributes(value)
        }
        if (util.istype(value, 'string') && !value.includes(':')) {
            return this.getAttribute(value)
        }
        if (util.istype(value, 'string') && value.includes(',') && !value.includes(':')) {
            return this.getAttributes(value)
        }
        if (util.istype(value, 'array-string')) {
            return this.getAttributes(value)
        }
    }
    /** @returns {number} */
    childrenLength() {
        return this.element.children.length
    }
    /** @param {string} value @returns {AppElement} */
    class(value) {
        // TODO: more functionality
        for (let _class_ of array.fromstring(value)) {
            this.element.classList.add(_class_)
        }
        return this
    }
    /** @returns {AppElement} */
    copy() {
        return new AppElement(this.element)
    }
    /** @param {boolean} value @returns {AppElement|boolean} */
    display(value = null) {
        if (value == null) return this.style('display') != 'none'
        this.style('display', value ? 'revert' : 'none')
        return this
    }
    /** @returns {boolean} */
    equals(value) {
        return this.element == AppElement.convertToElement(value)
    }
    /** @param {string|string[]} value @returns {{ string: string|null }} */
    getAttributes(value) {
        let attributes = new object()
        if (util.istype(value, 'string')) {
            for (let attributeKey of value.strip(' ,').split(',')) {
                attributeKey = attributeKey.strip(' ')
                let attributeValue = this.getAttribute(attributeKey)
                attributes.set(attributeKey, attributeValue)
            }
        }
        if (util.istype(value, 'array-string')) {
            for (let attributeKey of value) {
                let attributeValue = this.getAttribute(attributeKey)
                attributes.set(attributeKey, attributeValue)
            }
        }
        return attributes
    }
    /** @returns {Element} */
    getElement() {
        return this.element
    }
    /** @param {string} attributeKey @param {string} attributeValue @returns {AppElement|null} */
    getElementByAttribute(attributeKey, attributeValue) {
        let found = this.getElementsByAttribute(attributeKey, attributeValue)
        return found.length == 0 ? null : found[0]
    }
    /** @param {string} identifier @returns {AppElement|null} */
    getElementByIdentifier(identifier) {
        let found = this.getElementsByIdentifier(identifier)
        return found.length == 0 ? null : found[0]
    }
    /** @param {string} attributeKey @param {string} attributeValue @returns {AppElement[]} */
    getElementsByAttribute(attributeKey, attributeValue) {
        let found = []
        function find(element, found = []) {
            for (let child of element.children) {
                if (child.getAttribute(attributeKey) == attributeValue) {
                    found.append(app.element(child))
                }
                find(child, found)
            }
        }
        find(this.element, found)
        return found
    }
    /** @param {string} identifier @returns {AppElement[]}  */
    getElementsByIdentifier(identifier) {
        let found = []
        function find(element, found = []) {
            for (let child of element.children) {
                if (child.id == identifier) {
                    found.append(app.element(child))
                }
                find(child, found)
            }
        }
        find(this.element, found)
        return found
    }
    /** @param {boolean} useMargin @returns {number} */
    getHeight(useMargin = true) {
        let offsetHeight = this.element.offsetHeight
        let styles = window.getComputedStyle(this.element)
        if (useMargin) {
            let margin = parseFloat(styles['marginTop']) + parseFloat(styles['marginBottom'])
            return offsetHeight + margin
        }
        else {
            return offsetHeight
        }
    }
    /** @param {boolean} useMargin @returns {number} */
    getHeightChildren(useMargin = true) {
        let height = 0
        for (let child of this.children()) {
            height += child.getHeight(useMargin)
        }
        return height
    }
    /** @param {number} index @returns {string} */
    getIdentifier(index) {
        if (index == null) {
            return this.element.id
        } else {
            let delimiter
            if (this.element.id.includes('.')) {
                delimiter = '.'
            }
            if (this.element.id.includes('-')) {
                delimiter = '-'
            }
            let strings = this.element.id.split(delimiter)
            return strings[index < 0 ? index + strings.length : index]
        }
    }
    /** @param {string} key @param {any} defaultvalue @returns {any|null} */
    getProperty(key, defaultvalue = null) {
        if (this.isProperty(key)) {
            return this.element[key]
        } else {
            console.error(`KeyError: variable-name=this.element key=${key}`)
            return defaultvalue
        }
    }
    /** @param {string|string[]} value @returns {{ string: any|null }} */
    getProperties(value) {
        let properties = new object()
        if (util.istype(value, 'string')) {
            for (let propertyKey of value.strip(' ,').split(',')) {
                propertyKey = propertyKey.strip(' ')
                let propertyValue = this.getProperty(propertyKey)
                properties.set(propertyKey, propertyValue)
            }
        }
        if (util.istype(value, 'array-string')) {
            for (let propertyKey of value) {
                let propertyValue = this.getProperty(propertyKey)
                properties.set(propertyKey, propertyValue)
            }
        }
        return properties
    }
    /** @param {AppElement} element @returns {number[]} */
    getScrollOffset() {
        let left = ((this.getProperty('scrollLeft') / this.getWidth()) * 100)
        let top = ((this.getProperty('scrollTop') / this.getHeight()) * 100)
        return [left, top]
    }
    /** @param {string} key @param {any} defaultvalue @returns {string|null} */
    getStyleProperty(key, defaultvalue = null) {
        return this.element.style[key]
    }
    /** @param {string|string[]} value @returns {{ string: string|null }} */
    getStyleProperties(value) {
        let properties = new object()
        if (util.istype(value, 'string')) {
            for (let propertyKey of value.strip(' ,').split(',')) {
                propertyKey = propertyKey.strip(' ')
                let propertyValue = this.getStyleProperty(propertyKey)
                properties.set(propertyKey, propertyValue)
            }
        }
        if (util.istype(value, 'array-string')) {
            for (let propertyKey of value) {
                let propertyValue = this.getStyleProperty(propertyKey)
                properties.set(propertyKey, propertyValue)
            }
        }
        return properties
    }
    /** @param {string} key @returns {string} */
    getStylePropertyComputed(key) {
        let styleDeclaration = window.getComputedStyle(this.element)
        return styleDeclaration.getPropertyValue(key)
    }
    /** @param {boolean} useMargin @returns {number} */
    getWidth(useMargin = true) {
        let styles = window.getComputedStyle(this.element)
        if (useMargin) {
            let margin = parseFloat(styles['marginLeft']) + parseFloat(styles['marginRight'])
            return this.element.offsetWidth + margin
        }
        else {
            return this.element.offsetWidth
        }
    }
    /** @param {boolean} useMargin @returns {number} */
    getWidthChildren(useMargin = true) {
        let width = 0
        for (let child of this.children()) {
            width += child.getWidth(useMargin)
        }
        return width
    }
    /** @param {string} keys @returns {boolean} */
    hasAttributes(keys) {
        for (let attributeKey of keys.strip(' ,').split(',')) {
            attributeKey = attributeKey.strip(' ')
            if (!this.hasAttribute(attributeKey)) {
                return false
            }
        }
        return true
    }
    /** @returns {AppElement} */
    hide() {
        let styles = getComputedStyle(this.element)
        this.element.style.display = 'none'
        return this
    }
    highlight(oncomplete = (element) => { }, milliseconds = 500) {
        let original = this.style('background-color')
        this.style('background-color', app.getStyleProperty(':root', '--color-highlight'), 'transition', `${milliseconds}ms`)
        setTimeout(() => {
            this.style('background-color', original)
            setTimeout(() => oncomplete(this), milliseconds)
        }, milliseconds)
        return this
    }
    /** @param {number|string} value @returns {AppElement|string} */
    identifier(value = null) {
        if (value == null) {
            return this.getIdentifier()
        }
        if (util.istype(value, 'number')) {
            return this.getIdentifier(value)
        }
        if (util.istype(value, 'string')) {
            this.setIdentifier(value)
        }
        return this
    }
    /** @param {string} key @param {string} value @returns {boolean} */
    isAttribute(key, value = null) {
        if (value) {
            return this.getAttribute(key) == value
        } else {
            return this.getAttribute(key) != null
        }
    }
    /** @param {string} keys @returns {boolean} */
    isAttributes(keys) {
        for (let attributeKey of keys.strip(' ,').split(',')) {
            attributeKey = attributeKey.strip(' ')
            if (!this.hasAttribute(attributeKey)) {
                return false
            }
        }
        return true
    }
    /** @param {AppElement|Element|string} parentElement @returns {boolean} */
    isChildOf(parentElement) {
        parentElement = app.element(parentElement)
        if (this.element == parentElement.getElement()) {
            return false
        }
        let element = this.element
        while (element != null && element != app.body().getElement()) {
            if (element == parentElement.getElement()) {
                return true
            }
            element = element.parentElement
        }
        return false
    }
    /** @param {AppElement|Element} element @param {boolean} includeChildren  @returns {boolean} */
    isEqualTo(element, includeChildren = true) {
        // child.isEqualTo(parent)
        element = app.element(element)
        if (includeChildren) {
            return this.element == element.getElement() || element.contains(this.element)
        } else {
            return this.element == element.getElement()
        }
    }
    /** @param {string} identifiers @returns {boolean} */
    isIdentifier(identifiers) {
        for (let identifier of identifiers.strip(' |').split('|')) {
            if (this.element.id == identifier.strip(' ')) {
                return true
            }
        }
        return false
    }
    /** @param {string} key @param {any} value @returns {boolean} */
    isProperty(key, value = null) {
        if (value) {
            return this.getProperty(key) == value
        } else {
            let keys = []
            for (let key in this.element) {
                keys.append(key)
            }
            return keys.includes(key)
        }
    }
    /** @param {string} key @param {any} value @returns {boolean} */
    isStyleProperty(key, value = null) {
        if (value) {
            return this.getStyle(key) == value
        } else {
            let keys = []
            for (let key in this.element.style) {
                keys.append(key)
            }
            return keys.includes(key)
        }
    }
    /** @param {string} tagName @returns {boolean} */
    isTagName(tagName) {
        return this.element.tagName.upper() == tagName.upper()
    }
    /** @returns {boolean} */
    isVisible() {
        return this.getStylePropertyComputed('display') != 'none'
    }
    /** @param {string|string[]|{ string: any }} value @returns {AppElement|any} */
    property(value) {
        if (util.istype(value, 'string') && value.includes(':')) {
            return this.setProperties(value)
        }
        if (util.istype(value, 'object')) {
            return this.setProperties(value)
        }
        if (util.istype(value, 'string') && !value.includes(':')) {
            return this.getProperty(value)
        }
        if (util.istype(value, 'string') && value.includes(',') && !value.includes(':')) {
            return this.getProperties(value)
        }
        if (util.istype(value, 'array-string')) {
            return this.getProperties(value)
        }
    }
    /** @param {string} key @returns {DOMRect|number} */
    rect(key = null) {
        let DOMRect = this.getBoundingClientRect()
        return key == null ? DOMRect : DOMRect[key]
    }
    /** @param {string} keys @returns {AppElement} */
    removeAttributes(keys) {
        for (let attributeKey of keys.strip(' ,').split(',')) {
            attributeKey = attributeKey.strip(' ')
            this.removeAttribute(attributeKey)
        }
        return this
    }
    /** @param {number} index @returns {AppElement} */
    removeChildAt(index) {
        let element = this.children(index)
        this.removeChild(element)
        return this
    }
    /** @param {AppElement[]|Element[]|string[]} children @returns {AppElement} */
    removeChildern(children) {
        for (let child of children) {
            let element = app.element(child).getElement()
            this.element.removeChild(element)
        }
        return this
    }
    /** @param {...string} value @returns {AppElement} */
    removeClass(...values) {
        for (let value of values) {
            this.element.classList.remove(value)
        }
        return this
    }
    /** @param {string} type @param {function(Event): void} callback @param {boolean|{capture: boolean}} options @returns {AppElement} */
    removeListener(type, callback, options) {
        this.element.removeEventListener(type, callback, options)
        return this
    }
    /** @param {number} index @param {AppElement|Element|string} newChild @returns {AppElement} */
    replaceChildAt(index, newChild) {
        newChild = app.element(newChild).getElement()
        let oldChild = this.element.children[index]
        this.element.replaceChild(newChild, oldChild)
        return this
    }
    /** @returns {AppElement} */
    scrollDown() {
        this.element.scrollTop = this.element.scrollHeight - this.element.offsetHeight
        return this
    }
    /** @returns {AppElement} */
    scrollLeft() {
        this.element.scrollLeft = 0
        return this
    }
    /** @returns {AppElement} */
    scrollRight() {
        this.element.scrollLeft = this.element.scrollWidth
        return this
        // this.element.scrollLeft = this.element.scrollWidth - this.element.offsetWidth
    }
    /** @returns {AppElement} */
    scrollUp() {
        this.element.scrollTop = 0
        return this
    }
    /** @param {function(AppElement): void} callback @returns {AppElement} */
    self(callback) {
        callback(this)
        return this
    }
    /** @param {string|{string:string}} value @returns {AppElement} */
    setAttributes(value) {
        if (util.istype(value, 'string')) {
            for (let entry of value.strip(' ;').split(';')) {
                let attribute = entry.split(':')
                let attributeKey = attribute.getFirst().strip(' ')
                let attributeValue = attribute.getLast().strip(' ')
                this.setAttribute(attributeKey, attributeValue)
            }
        }
        if (util.istype(value, 'object')) {
            for (let [attributeKey, attributeValue] of enumerate(value)) {
                this.setAttribute(attributeKey, attributeValue)
            }
        }
        return this
    }
    /** @param {string} contentOriginal @param {string} contentResults @returns {AppElement} */
    setBackground(contentOriginal = null, contentResults = '') {
        // contentOriginal default
        if (!contentOriginal) {
            contentOriginal = this.children(0).something()
        }
        if (!contentOriginal) {
            return console.error(`UnsetError: variable-name=contentOriginal`)
        }
        if (this.childrenLength() >= 1) {
            if (this.children(0).hasAttribute('class')) {
                if (!this.children(0).getAttribute('class').includes('content-background')) {
                    return console.error(`MissingElementError: `, this.element)
                }
            } else return console.error(`MissingElementError: `, this.element)
        } else return console.error(`MissingElementError: `, this.element)
        // 
        contentResults = contentOriginal
        let element = this
        if (!this.getHeight()) {
            console.warn(`ValueError: function-name=this.getHeight()`, this.element)
        }
        if (!this.getWidth()) {
            console.warn(`ValueError: function-name=this.getWidth()`, this.element)
        }
        /** @param {string} content @param {number} index @param {number} variable @param {string} oldContent @param {string} newContent @returns {[number, string, string]} */
        function convertContents(content, index, variable = 0, oldContent = '$', newContent = '') {
            if (content.slice(index, index + 'color-accent'.length) == 'color-accent') {
                oldContent += 'color-accent'
                newContent = app.configuration('color-accent')
            }
            if (content.slice(index, index + 'color-header'.length) == 'color-header') {
                oldContent += 'color-header'
                newContent = app.configuration('color-header')
            }
            if (content[index] == '0') {
                oldContent += content[index]
                variable = 2
                newContent = variable.toString()
            }
            if (content[index] == 'h') {
                oldContent += content[index]
                variable = element.getProperty('offsetHeight') - 1
                newContent = variable.toString()
            }
            if (content[index] == 'w') {
                oldContent += content[index]
                variable = element.getProperty('offsetWidth') - 1
                newContent = variable.toString()
            }
            let operator = content[index + 1]
            if (operator == '-' || operator == '+' || operator == '/' || operator == '*' || operator == '%') {
                oldContent += operator
                let number = ''
                if (content[index + 2] == '$') {
                    let results = convertContents(content, index + 3)
                    number = results[0]
                    oldContent += results[1]
                } else {
                    for (let i = index + 2; i < content.length; i++) {
                        let character = content[i]
                        if (!character.isdecimal()) {
                            number = content.slice(index + 2, i)
                            break
                        }
                    }
                    oldContent += number
                }
                if (operator == '-') {
                    variable -= Number(number)
                }
                if (operator == '+') {
                    variable += Number(number)
                }
                if (operator == '*') {
                    variable *= Number(number)
                }
                if (operator == '/') {
                    variable /= Number(number)
                }
                if (operator == '%') {
                    variable *= (Number(number) / 100)
                }
                newContent = variable.toString()
            }
            return [variable, oldContent, newContent]
        }
        for (let i = 0; i < contentResults.length; i++) {
            if (contentResults[i] == '$') {
                let [variable, oldContent, newContent] = convertContents(contentResults, i + 1)
                contentResults = contentResults.replace(oldContent, newContent)
            }
        }
        this.element.children[0].something = contentOriginal
        this.element.children[0].innerHTML = contentResults
        return this
    }
    /** @param {string} content @returns {AppElement} */
    setBackgroundContent(content = null) {
        content = content == null ? this.getStyleProperty('background-image') : content
        if (!content) {
            return console.error(`UnsetError: variable-name=content`)
        }
        if (!content.includes('xmlns')) {
            content = content.replace('<svg', '<svg xmlns="http://www.w3.org/2000/svg"')
        }
        // 
        let element = this
        if (!this.getHeight()) {
            console.warn(`ValueError: function-name=this.getHeight()`, this.element)
        }
        if (!this.getWidth()) {
            console.warn(`ValueError: function-name=this.getWidth()`, this.element)
        }
        let height = this.getHeight()
        let width = this.getWidth()
        /** @param {string} match @param {string} operandLeft @param {string} operator @param {string} operandRight @param {number} offset @param {string} string @param {{string:string}} groups @returns {string} */
        function replacer1(match, operandLeft, operator, operandRight, offset, string, groups) {
            /** @type {string} */
            let variableName = operandLeft
            /** @type {number|string} */
            let variableValue
            if (variableName == 'height') {
                variableValue = height
            }
            if (variableName == 'width') {
                variableValue = width
            }
            if (operator) {
                if (operator == '+') variableValue += Number(operandRight)
                if (operator == '/') variableValue /= Number(operandRight)
                if (operator == '*') variableValue *= Number(operandRight)
                if (operator == '%') variableValue *= (Number(operandRight) / 100)
                if (operator == '-') variableValue -= Number(operandRight)
            }
            return variableValue
        }
        content = content.replaceAll(/\$(height|width)([+/*%-]|)(\d+|)/g, replacer1)
        /** @param {string} match @param {string} propertyKey @param {number} offset @param {string} string @param {{string:string}} groups @returns {string} */
        function replacer2(match, propertyKey, p2, offset, string, groups) {
            return app.getStyleProperty(':root', propertyKey)
        }
        content = content.replaceAll(/var\((--\w+(-\w+)*)\)/g, replacer2)
        let backgroundImage = `url(data:image/svg+xml;base64,${util.base64_encode(content)})`
        this.setStyleProperty('background-image', backgroundImage)
        return this
    }
    /** @param {string} value @returns {AppElement} */
    setForeground(value) {
        if (this.childrenLength() >= 2) {
            if (this.children(1).hasAttribute('class')) {
                if (!this.children(1).getAttribute('class').includes('content-foreground')) {
                    return console.error('no foreground element')
                }
            } else return console.error('no foreground element')
        } else return console.error('no foreground element')
        if (util.istype(value, 'element')) {
            value = app.element(value)
            this.children(1).appendChild(value)
        }
        if (util.istype(value, 'string')) {
            // TODO: decode variables
            this.children(1).innerHTML(value)
        }
        return this
    }
    /** @param {...string} values @returns {AppElement} */
    setIdentifier(...values) {
        this.element.id = values.join(AppElement.IDENTIFIER_DELIMITER)
        return this
    }
    /** @param {string} key @param {any} value @returns {AppElement} */
    setProperty(key, value) {
        if (this.isProperty(key)) {
            this.element[key] = value
        } else {
            console.error(`KeyError: variable-name=this.element key=${key}`)
        }
        return this
    }
    /** @param {string|{string:string}} value @returns {AppElement} */
    setProperties(value) {
        if (util.istype(value, 'string')) {
            for (let entry of value.strip(' ;').split(';')) {
                let property = entry.split(':')
                let propertyKey = property.getFirst().strip(' ')
                let propertyValue = property.getLast().strip(' ')
                this.setProperty(propertyKey, propertyValue)
            }
        }
        if (util.istype(value, 'object')) {
            for (let [propertyKey, propertyValue] of enumerate(value)) {
                this.setProperty(propertyKey, propertyValue)
            }
        }
        return this
    }
    /** @param {string} key @param {number|string} value @returns {AppElement} */
    setStyleProperty(key, value) {
        this.element.style[key] = AppElement.#convertValue(key, value)
        return this
    }
    /** @param {string|{string:string}} value @returns {AppElement} */
    setStyleProperties(value) {
        if (util.istype(value, 'string')) {
            for (let entry of value.strip(' ;').split(';')) {
                let property = entry.split(':')
                let propertyKey = property.getFirst().strip(' ')
                let propertyValue = property.getLast().strip(' ')
                this.setStyleProperty(propertyKey, propertyValue)
            }
        }
        if (util.istype(value, 'object')) {
            for (let [propertyKey, propertyValue] of enumerate(value)) {
                this.setStyleProperty(propertyKey, propertyValue)
            }
        }
        return this
    }
    /** @returns {AppElement} */
    show() {
        let style = getComputedStyle(this.element)
        this.element.style.display = ''
        if (style.display == 'none' || style.display == '') {
            this.element.style.display = 'revert'
        }
        return this
    }
    /** @param {...string|string[]|{string:string}} value @returns {AppElement|string|null} */
    style(...value) {
        if (value.length == 1) {
            value = value[0]
            if (util.istype(value, 'string') && value.includes(':')) {
                return this.setStyleProperties(value)
            }
            if (util.istype(value, 'object')) {
                return this.setStyleProperties(value)
            }
            if (util.istype(value, 'string') && !value.includes(':')) {
                return this.getStyleProperty(value)
            }
            if (util.istype(value, 'string') && value.includes(',') && !value.includes(':')) {
                return this.getStyleProperties(value)
            }
            if (util.istype(value, 'array-string')) {
                return this.getStyleProperties(value)
            }
        } else {
            for (let i = 0; i < value.length; i += 2) {
                this.setStyleProperty(value[i], value[i + 1])
            }
        }
        return this
    }
    /** @param {string} value @param {boolean} append @returns {AppElement|string} */
    text(value = null, append = false) {
        let tagName = this.getTagName('upper')
        if (tagName == 'INPUT' || tagName == 'SELECT') {
            return this.value(value, append)
        } else {
            return this.innerHTML(value, append)
        }
    }
    /** @param {function(AppElement): void} callback @param {number} milliseconds @returns {AppElement} */
    timeout(callback, milliseconds) {
        setTimeout(() => callback(this), milliseconds)
        return this
    }
    /** @returns {AppElement} */
    toBack() {
        return this.style('z-index', 0)
    }
    /** @returns {AppElement} */
    toFront() {
        return this.style('z-index', 100)
    }
    /** @param {string} value @returns {AppElement|string} */
    view(value = null) {
        if (value == null) return this.element.getAttribute('view')
        else this.element.setAttribute('view', value)
        return this
    }
    /** @param {function(AppElement): void} callback @param {number} milliseconds @returns {AppElement} */
    wait(callback, milliseconds) {
        setTimeout(() => callback(this), milliseconds)
        return this
    }
    /** @param {function(AppElement): void} callback @returns {AppElement} */
    with(callback) {
        callback(this)
        return this
    }
    /** @param {string} key  @param {string} value @returns {string} */
    static #convertAttributeValue(key, value) {
        let dynamicValues = 'auto|inherit|initial|fit-content|max-content|min-content|revert|unset'
        if (AppElement.propertiesOfPixelValue.includes(key)) {
            let append = true
            if (key == 'height' || key == 'width') {
                append = !dynamicValues.includes(value)
            }
            append = append && !(`${value}`.includes('px') || `${value}`.includes('%'))
            value += append ? 'px' : ''
        }
        return value
    }
    /** @param {string} key  @param {string} value @returns {string} */
    static #convertValue(key, value) {
        if (AppElement.propertiesOfPixelValue.includes(key) && util.istype(value, 'string-number|number') && !(`${value}`.includes('px') || `${value}`.includes('%'))) {
            value += 'px'
        }
        return value
    }
}
class Cards {
    constructor(obj = null) {
        this.attr = { backgroundColor: '#0000ff', height: 155.55, id: 'card', left: '', select: 'translateY(-20px)', side: 'front', top: '', transform: '', transition: '500ms', width: 100, }
        this.count = 1
        this.cards = []
        this.discarded = []
        this.deck = []
        this.suits = ['D', 'C', 'H', 'S']
        this.symbols = ['&#9830;', '&#9827;', '&#9829;', '&#9824;']
        this.table = []
        this.trumps = 'ace_high'
        if (obj) this.setAttributes(obj)
    }

    setAttributes(obj) {
        for (let key in obj) if (key in this.attr) this.attr[key] = obj[key]
        if ('backgroundColor' in obj) this.cards.filter((crd) => this.side(crd) == 'back').map((crd) => crd.style.backgroundColor = this.attr.backgroundColor)
        if ('transition' in obj) this.cards.map((crd) => crd.style.transition = this.attr.transition)
        if ('width' in obj) this.cards.map((crd) => { crd.style.width = this.attr.width + 'px', crd.style.height = (3.5 / 2.25) * this.attr.width + 'px' })
    }
    content(crd) {
        let arr = this.get('e', crd)
        let fs = [this.attr.width / 5, this.attr.width + (this.attr.width / 3)]
        return `<b style=\"color: ${arr['color']}; font-size: ${fs[0]}px\">${arr['face']}</b>` +
            `<div style=\"color:${arr['color']}; font-size: ${fs[1]}px; margin-top: -27.5px; text-align: center;\">${arr['symbol']}</div>` +
            `<b style=\"color: ${arr['color']}; float:right; font-size: ${fs[0]}px; margin-top:-26px;\">${arr['face']}</b>`
    }
    create() {
        this.cards = [], this.deck = [], this.discarded = [], this.table = []
        let map = null
        if (this.trumps == 'ace_high') map = { 'D2': 'D2', 'C2': 'C2', 'H2': 'H2', 'S2': 'S2' }
        if (this.trumps == 'ace_low') map = { 'C14': 'C1', 'D14': 'D1', 'H14': 'H1', 'S14': 'S1' }
        if (this.trumps == 'jokers_deuces') map = { 'D2': 'S16', 'C2': 'S17', 'H2': 'S18', 'S2': 'S15' }
        for (let i = 0; i < this.count * 52; i++) {
            let crd = this.suits[Math.floor(i / 13) % 4] + ((i % 13) + 2)
            crd = crd in map ? map[crd] : crd
            this.cards.push(this.element(crd))
        }
        this.deck = this.cards.map((crd) => crd)
        for (let i of [1, 2, 3]) {
            this.discarded = this.deck
            this.deck = []
            this.shuffle()
        }
        return this.deck
    }
    discard(...arr) {
        if (arr.length > 0) {
            arr.forEach(crd => {
                let a = this.deck.findIndex((elt) => elt == crd)
                let b = this.table.findIndex((elt) => elt == crd)
                this[a == -1 ? 'table' : 'deck'].splice(a == -1 ? b : a, 1).forEach(crd => this.discarded.push(crd))
            })
        } else {
            this.table.forEach(crd => this.discarded.push(crd))
            this.table = []
        }
    }
    element(crd) {
        let elt = document.createElement('div')
        elt.id = this.attr.id
        elt.style.backgroundColor = this.attr.side == 'back' ? this.attr.backgroundColor : 'white'
        elt.style.border = '1px solid black'
        elt.style.borderRadius = '5px'
        elt.style.boxSizing = 'border-box'
        elt.style.fontSize = '15px'
        elt.style.height = this.attr.height + 'px'
        elt.style.left = this.attr.left
        elt.style.opacity = '1'
        elt.style.padding = '5px'
        elt.style.position = 'absolute'
        elt.style.textAlign = 'left'
        elt.style.top = this.attr.top
        elt.style.transform = this.attr.transform
        elt.style.transition = this.attr.transition
        elt.style.width = this.attr.width + 'px'
        elt.style.zIndex = 0
        elt.something = crd
        elt.innerHTML = this.attr.side == 'back' ? '' : this.content(elt)
        return elt
    }
    flip(crd, side = null) {
        let front = side == null ? crd.style.backgroundColor == 'white' : side == 'back'
        crd.style.backgroundColor = front ? this.attr.backgroundColor : 'white'
        crd.innerHTML = front ? '' : this.content(crd.something)
    }
    get(arg, crd) {
        crd = crd instanceof Element ? crd.something : crd
        let v = Number(crd.substring(1))
        switch (arg.toLowerCase()) {
            case 'c':
            case 'card':
                return crd
            case 's':
            case 'suit':
                return crd[0]
            case 'sv':
            case 'suit_value':
                return this.suits.indexOf(crd[0])
            case 'v':
            case 'value':
                return v
            case 'fv':
            case 'face_value':
                return v <= 10 ? v : (11 <= v && v <= 13) ? 10 : 11
            case 'f':
            case 'face':
                let map = { 1: 'A', 11: 'J', 12: 'Q', 13: 'K', 14: 'A', 15: '2', 16: '2', 17: 'Jo', 18: 'Jo' }
                return v in map ? map[v] : v
            case 'y':
            case 'symbol':
                return this.symbols[this.suits.indexOf(crd == 'S16' ? 'D' : crd[0])]
            case 'e':
            case 'element':
                return { face: this.get('f', crd), symbol: this.get('y', crd), color: crd[0] == 'D' || crd[0] == 'H' || crd == 'S16' || crd == 'S18' ? 'red' : 'black' }
            case 'd':
            case 'data':
                return { suit: this.get('s', crd), value: this.get('v', crd) }
        }
    }
    hasSuit(sut, hnd) {
        return hnd.some((crd) => this.get('s', crd) == sut)
    }
    index() {
        this.deck.map((crd, i, arr) => crd.style.zIndex = (arr.length - i))
    }
    position(crd, pos, rand = [random(-5, 5), random(-5, 5), random(-5, 5)]) {
        crd.style.left = rand[0] + pos[0] + '%'
        crd.style.top = rand[1] + pos[1] + '%'
        crd.style.transform = pos[2] + ' rotate(' + rand[2] + 'deg)'
        return this
    }
    pull(to = 'table') {
        if (this.deck.length == 0) {
            this.shuffle()
            return this.pull(to)
        }
        let crd = this.deck[0]
        this.deck.shift()
        this[to].push(crd)
        return crd
    }
    side(crd) {
        return crd.style.backgroundColor == 'white' ? 'front' : 'back'
    }
    sort(arg, hnd) {
        if (arg == 's' || arg == 'suit' || true) {
            let arr = [[], [], [], []].map((v) => new Array(19))
            hnd.forEach(crd => arr[this.get('sv', crd.something)][this.get('v', crd.something)] = crd)
            for (let i = 0, c = 0; i < 76; i++) {
                if (arr[Math.floor(i / 19)][i % 19]) {
                    hnd[c] = arr[Math.floor(i / 19)][i % 19]
                    c += 1
                }
            }
        }
        if (arg == 'v' || arg == 'value') {
            hnd.sort((a, b) => this.get('v', a.something) - this.get('v', b.something))
        }
        return hnd
    }
    shuffle() {
        do {
            let idx = Math.floor(Math.random() * this.discarded.length)
            this.deck.push(this.discarded[idx])
            this.discarded.splice(idx, 1)
        } while (this.discarded.length > 0)
    }
    select(crd, hnd = []) {
        hnd.map((crd) => crd.style.transform = crd.style.transform.replace(` ${this.attr.select}`, ''))
        crd.style.transform += ` ${this.attr.select}`
    }
    value(elt, crd) {
        elt.something = crd
        elt.innerHTML = this.content(crd)
        return elt
    }
}
class Color {
    #values
    constructor(r, g, b, a = 1) {
        this.#values = [r, g, b, a]
    }
    get alpha() {
        return this.#values[3]
    }
    set alpha(value) {
        if (value < 0 || value > 1) {
            throw new RangeError("Alpha value must be between 0 and 1")
        }
        this.#values[3] = value
    }
}
class Colors {
    static transparent = '#00000000'
    static overlayLight = '#33000000'
    static overlayMedium = '#66000000'
    static overlayDark = '#99000000'
}
class DataBinding {
    /*
    Data binding is the process that couples two data sources together and synchronizes them. With data binding, a change to an element in a data set automatically updates in the bound data set.
    
    TYpes
    One-way: binding is a relatively simple type of data binding. Changes to the data provider update automatically in the data consumer data set, but not the other way around.
    Two-way: binding is where changes to either the data provider or the data consumer automatically updates the other.
    One-way-to-source: binding is the reverse of one-way binding. Changes to the data consumer automatically update the data provider but not the other way around.
    One-time: binding is where changes to the data provider do not automatically update the data consumer. This approach is useful when only a snapshot of the data is needed, and the data is static.
    */
    /** @param {any} value @param {function(any, any): void} listener @returns {void} */
    constructor(value, listener = null) {
        /** @type {any} */
        this.value_ = value
        /** @type {onChangeListener[]} */
        this.onChangeListeners = []
        if (listener) {
            this.setOnChangeListener(listener)
        }
    }

    /** @typedef {function(any, any): void} onChangeListener */
    static onChangeListener = (newValue, oldValue) => { }

    /** @param {...any} values @returns {any} */
    append(...values) {
        return this.#onSet(() => this.value_.append(...values))
    }
    /** @returns {any} */
    clear() {
        return this.#onSet(() => this.value_.clear())
    }
    /** @returns {number} */
    index(value) {
        return this.value_.index(value)
    }
    /** @param {number} index @param {any} value @returns {any} */
    insert(index, value) {
        return this.#onSet(() => this.splice(index, 0, value))
    }
    /** @param {number} index @returns {any} */
    pop(index = -1) {
        return this.#onSet(() => this.value_.splice(index, 1))
    }
    /** @param {...any} values @returns {any} */
    remove(...values) {
        return this.#onSet(() => this.value_.remove(...values))
    }
    /** @param {any} value @returns {any} */
    set(value) {
        return this.#onSet(() => this.value_ = value)
    }
    /** @param {onChangeListener} listener  */
    setOnChangeListener(listener) {
        this.onChangeListeners.push(listener)
    }
    /** @param {any} condition @param {any} value @returns {boolean} */
    setEQ(condition, value) {
        return this.#onCondition(this.value_ == condition, value)
    }
    /** @param {any} condition @param {any} value @returns {boolean} */
    setGE(condition, value) {
        return this.#onCondition(this.value_ <= condition, value)
    }
    /** @param {any} condition @param {any} value @returns {boolean} */
    setGT(condition, value) {
        return this.#onCondition(this.value_ < condition, value)
    }
    /** @param {any} condition @param {any} value @returns {boolean} */
    setLE(condition, value) {
        return this.#onCondition(this.value_ >= condition, value)
    }
    /** @param {any} condition @param {any} value @returns {boolean} */
    setLT(condition, value) {
        return this.#onCondition(this.value_ > condition, value)
    }
    slice(...values) {
        return this.#onSet(() => this.value_ = this.value_.slice(...values))
    }
    /** @returns {number} */
    size() {
        return this.value_.length
    }
    /** @returns {any} */
    toggle() {
        this.#onSet(() => this.value_ = !this.value_)
        return this.value_
    }
    /** @returns {any} */
    value() {
        return this.value_
    }
    /** @param {boolean} results @param {any} value @returns {boolean} */
    #onCondition(results, value) {
        if (results) {
            this.set(value)
        }
        return results
    }
    /** @param {function(): void} assignment @returns {any} */
    #onSet(assignment) {
        let oldValue = util.clone(this.value_)
        assignment()
        let newValue = this.value_
        for (let listener of this.onChangeListeners) {
            listener(newValue, oldValue)
        }
        return newValue
    }
}
class Timestamp {
    constructor() {

    }

    static MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    static DAYS_OF_WEEK = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    /** @param {Date|number|string} date1 @param {Date|number|string} date2 @returns {boolean} */
    static isSameDay(date1, date2 = util.timestamp('object')) {
        date1 = util.timestamp(date1, 'object')
        date2 = util.timestamp(date2, 'object')
        return date1.getFullYear() == date2.getFullYear() && date1.getMonth() == date2.getMonth() && date1.getDate() == date2.getDate()
    }

    /** @param {Date|number|string} date @returns {string} */
    static getDate(date = util.timestamp('object')) {
        date = util.timestamp(date, 'object')
        let year = date.getFullYear().toString()
        let month = (date.getMonth() + 1).toString().rjust(2, '0')
        let dayOfMonth = date.getDate().toString().rjust(2, '0')
        return `${year}-${month}-${dayOfMonth}`
    }
    /** @param {Date|number|string} date @param {boolean} short @returns {string} */
    static getDateTime(date = util.timestamp('object'), short = false) {
        return `${Timestamp.getDate(date)} ${Timestamp.getTime(date, short)}`
    }
    /** @param {Date|number|string} date @param {boolean} short @returns {string} */
    static getDayOfWeek(date = util.timestamp('object'), short = false) {
        date = util.timestamp(date, 'object')
        let dayOfWeek = Timestamp.DAYS_OF_WEEK[date.getDay()]
        if (short) {
            return dayOfWeek.slice(0, 3)
        } else {
            return dayOfWeek
        }
    }
    /** @param {Date|number|string} timestamp1 @param {Date|number|string} timestamp2 @param {boolean} short @returns {string} */
    static getDifference(timestamp1, timestamp2 = util.timestamp('seconds'), short = true) {
        timestamp1 = util.timestamp(timestamp1, 'seconds')
        timestamp2 = util.timestamp(timestamp2, 'seconds')
        let difference = Math.abs(timestamp2 - timestamp1)
        if (difference == 0) return 'Now'
        if (difference <= 1) return short ? '1sec': '1 second'
        if (difference <= 2) return short ? '2sec' : '2 seconds'
        if (difference <= 3) return short ? '3sec' : '3 seconds'
        if (difference <= 4) return short ? '4sec' : '4 seconds'
        if (difference <= 5) return short ? '5sec' : '5 seconds'
        if (difference <= 10) return short ? '10sec' : '10 seconds'
        if (difference <= 20) return short ? '20sec' : '20 seconds'
        if (difference <= 30) return short ? '30sec' : '30 seconds'
        if (difference <= 60) return short ? '1min' : '1 minute'
        if (difference <= 120) return short ? '2min' : '2 minutes'
        if (difference <= 180) return short ? '3min' : '3 minutes'
        if (difference <= 240) return short ? '4min' : '4 minutes'
        if (difference <= 300) return short ? '5min' : '5 minutes'
        if (difference <= 600) return short ? '10min' : '10 minutes'
        if (difference <= 1200) return short ? '20min' : '20 minutes'
        if (difference <= 1800) return short ? '30min' : '30 minutes'
        if (difference <= 3600) return short ? '1h' : '1 hour'
        if (difference <= 7200) return short ? '2h' : '2 hours'
        if (difference <= 10800) return short ? '3h' : '3 hours'
        if (difference <= 14400) return short ? '4h' : '4 hours'
        if (difference <= 18000) return short ? '5h' : '5 hours'
        if (difference <= 21600) return short ? '6h' : '6 hours'
        if (difference <= 43200) return short ? '12h' : '12 hours'
        if (difference <= 86400) return short ? '1d' : '1 day'
        if (difference <= 172800) return short ? '2d' : '2 days'
        if (difference <= 259200) return short ? '3d' : '3 days'
        if (difference <= 345600) return short ? '4d' : '4 days'
        if (difference <= 432000) return short ? '5d' : '5 days'
        if (difference <= 864000) return short ? '10d' : '10 days'
        if (difference <= 1728000) return short ? '20d' : '20 days'
        if (difference <= 2592000) return short ? '1mo' : '1 month' // 30 days
        if (difference <= 5184000) return short ? '2mo' : '2 months'
        if (difference <= 7776000) return short ? '3mo' : '3 months'
        if (difference <= 10368000) return short ? '4mo' : '4 months'
        if (difference <= 12960000) return short ? '5mo' : '5 months'
        if (difference <= 15552000) return short ? '6mo' : '6 months'
        if (difference <= 31536000) return short ? '1yr' : '1 year'
        if (difference <= 63072000) return short ? '2yr' : '2 years'
        if (difference <= 94608000) return short ? '3yr' : '3 years'
        if (difference <= 126144000) return short ? '4yr' : '4 years'
        if (difference <= 157680000) return short ? '5yr' : '5 years'
        if (difference <= 315360000) return short ? '10yr' : '10 years'
    }
    /** @param {Date|number|string} date @returns {string} */
    static getHours(date = util.timestamp('object')) {
        date = util.timestamp(date, 'object')
        return date.getHours().toString().rjust(2, '0')
    }
    /** @param {Date|number|string} date @returns {string} */
    static getMinutes(date = util.timestamp('object')) {
        date = util.timestamp(date, 'object')
        return date.getMinutes().toString().rjust(2, '0')
    }
    /** @param {Date|number|string} date @param {boolean} short @returns {string} */
    static getMonth(date = util.timestamp('object'), short = false) {
        date = util.timestamp(date, 'object')
        let month = Timestamp.MONTHS[date.getMonth()]
        if (short) {
            return month.slice(0, 3)
        } else {
            return month
        }
    }
    /** @param {Date|number|string} date @returns {string} */
    static getSeconds(date = util.timestamp('object')) {
        date = util.timestamp(date, 'object')
        return date.getSeconds().toString().rjust(2, '0')
    }
    /** @param {Date|number|string} date @param {boolean} short @returns {string} */
    static getTime(date = util.timestamp('object'), short = false) {
        date = util.timestamp(date, 'object')
        let hours = date.getHours().toString().rjust(2, '0')
        let minutes = date.getMinutes().toString().rjust(2, '0')
        let seconds = date.getSeconds().toString().rjust(2, '0')
        let milliseconds = date.getMilliseconds().toString().ljust(3, '0')
        if (short) {
            return `${hours}:${minutes}:${seconds}`
        } else {
            return `${hours}:${minutes}:${seconds}.${milliseconds}`
        }
    }
    /** @param {Date|number|string} date @returns {string} */
    static getYear(date = util.timestamp('object')) {
        date = util.timestamp(date, 'object')
        return date.getFullYear().toString()
    }
}
class Viewer {
    constructor() {
        /** @type {string} */
        this.classname = null
        /** @type {array} */
        this.views = new array()
        /** @type {AppElement} */
        this.viewSelector = null
        /** @type {AppElement} */
        this.title = null
        /** @type {number} */
        this.previousIndex = null
        this.onLoad()
    }

    /** @param {Event} event @returns {void} */
    onLoad(event) {
        app.directory('images', 'file:///c:/projects/.repository/images/')
        this.viewSelector = app.element('viewSelector').style('position: relative; left: 50%; padding: 10px 0; transform: translateX(-50%);')
        this.title = app.element('title').style('font-size: 150%; padding: 10px 0; text-align: center; width: 100%;')
    }
    /**  @param {InputEvent} event @param {AppElement} element @returns {void} */
    onInput(event, element) {
        if (element.getIdentifier() == this.viewSelector.getIdentifier()) {
            let currentIndex = this.viewSelector.value()
            if (this.previousIndex) {
                app.body().removeChild(this.views[this.previousIndex].getView())
            }
            app.body().appendChild(this.views[currentIndex].getView())
            this.previousIndex = currentIndex
        }
    }
    /** @param {AppElement} view @returns {void} */
    addView(view) {
        if (!this.classname) {
            this.classname = view.constructor.name
            this.title.text(this.classname)
            window.document.title = this.classname
        }
        this.views.append(view)
        let size = this.views.size()
        this.viewSelector.innerHTML(`<option value="${size-1}">${this.classname}.${size}</option>`, true)
        if (size == 1) {
            this.viewSelector.value(size - 1).dispatchEvent('input')
        }
        view.setIdentifier(`${this.classname.lower()}${size}`)
    }
    /** @param {number} index @returns {void} */
    setView(index) {
        this.viewSelector.value(index).dispatchEvent('input')
    }
}
//_________________________________________________________________________________________________________________________________________________//
class View {
    /** @constructor */
    constructor() {
        /** @protected @type {AppElement} */
        this.view = app.element('div')
        /** @type {string} */
        this.tag = ''
    }

    /** @typedef {function(View): null} Listener */
    static onListener = (view) => { }

    /** @param {AppElement} element @returns {number[]} */
    static getScrollOffset(element) {
        let left = ((element.getProperty('scrollLeft') / element.getWidth()) * 100)
        let top = ((element.getProperty('scrollTop') / element.getHeight()) * 100)
        return [left, top]
    }
    /** @param {AppElement} element @returns {number[]} */
    static getScrollDistance(element) {
        let left = element.getProperty('scrollLeft') - element.getWidth()
        let top = element.getProperty('scrollTop') - element.getHeight()
        return [left, top]
    }
    /** @returns {View} */
    copy() {
        let className = this.constructor.name
        let view = new window[className]()
        // TODO: pass other class property values to new class
        return view
    }
    /** @returns {string} */
    getClassName() {
        return this.constructor.name.lower()
    }
    /** @returns {AppElement} */
    getElementByIdentifier(identifier) {
        return this.view.getElementByIdentifier(identifier)
    }
    /** @returns {string} */
    getId(index) {
        if (index) {
            return this.view.id(index)
        }
        else {
            return this.view.id()
        }
    }
    /** @param {number} index @returns {string} */
    getIdentifier(index = null) {
        return this.view.getIdentifier(index)
    }
    /** @returns {string} */
    getTag() {
        return this.tag
    }
    /** @returns {AppElement} */
    getView() {
        return this.view
    }
    /** @param {string} identifier @returns {boolean} */
    isIdentifier(identifier) {
        return this.getIdentifier() == identifier
    }
    /** @param {string} tag @returns {boolean} */
    isTag(tag) {
        return this.tag == tag
    }
    /** @returns {boolean} */
    isVisible() {
        return app.containsElement(this.view.getIdentifier()) && this.view.isVisible()
    }
    /** @param {{string:string}|string} attributes */
    setAttributes(attributes) {
        attributes = object.fromdata(attributes)
        for (let [key, value] in enumerate(attributes)) {
            console.log(`View.setAttributes(attributes=${attributes}) > key=${key}`, this[key])
            // if (this[key]) {
            //     if (util.istype(value, 'string-array')) {
            //         this[key] = util.json_decode(value)
            //     }
            //     if (util.istype(value, 'string-boolean')) {
            //         this[key] = value == 'true'
            //     }
            //     if (util.istype(value, 'string-number')) {
            //         this[key] = Number(value)
            //     }
            //     if (util.istype(value, 'string-object')) {
            //         this[key] = util.json_decode(value)
            //     }
            // }
        }
    }
    /** @param {string} id @returns {void} */
    setId(id) {
        this.view.id(id)
    }
    /** @param {string} identifier @returns {void} */
    setIdentifier(identifier) {
        this.view.setIdentifier(identifier)
    }
    /** @param {AppElement} element @param {AppElement|string} value @param {boolean} wait @returns {AppElement} */
    setImage(element, value, wait = false) {
        if (util.istype(value, 'string')) {
            if (wait) {
                let data = app.createWebConnection().headers('Accept: text/base64').get(app.getPathImages(value))
                element.src(`data:image/png;base64,${data}`)
            } else {
                element.src(app.getPathImages(value))
            }
        }
        if (util.istype(value, 'element')) {
            element.outerHTML(app.element(value).outerHTML())
        }
        return element
    }
    /** @param {string} tag @returns {void} */
    setTag(tag) {
        this.tag = tag
    }
    /** @param {AppElement} element @param {AppElement|number|string} value @returns {AppElement} */
    setText(element, value) {
        if (value == null) {
            element.hide()
            return element
        }
        if (util.istype(value, 'number|string') || value == '') {
            element.innerHTML(value)
        }
        if (util.istype(value, 'element')) {
            // element.outerHTML(app.element(value).outerHTML())
            element.appendChild(...app.element(value).children())
        }
        if (!element.isVisible()) {
            element.show()
        }
        return element
    }
    /** @param {AppElement} view */
    setView(view) {
        if (view.attribute('view') == this.getClassName() && view.childrenLength() == 0) {
            let instance = new this.constructor()
            view.appendChild(...instance.view.children())
            if (view.getIdentifier() == '') {
                view.setIdentifier(instance.getIdentifier())
            }
            this.view = view
        } else {
            this.view = view
        }
    }
}
class Button extends View {
    constructor(attributes = {}) {
        super()
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }
}
class Dialog extends View {
    constructor(attributes = {}) {
        super()
        /** @type {boolean} */
        this.cancelable = true
        /** @type {boolean} */
        this.canceledOnTouchOutside = false
        /** @type {string[]} */
        this.instances = []
        /** @type {function(Dialog): void } */
        this.onCancelListener = Dialog.onCancelListener
        /** @type {function(Dialog): void } */
        this.onDismissListener = Dialog.onDismissListener
        /** @type {function(Dialog, AppElement): void } */
        this.onInputListener = Dialog.onInputListener
        /** @type {function(Dialog, number, boolean): void } */
        this.onItemSelectedListener = Dialog.onItemSelectedListener
        /** @type {function(Dialog, Event): void } */
        this.onKeyListener = Dialog.onKeyListener
        /** @type {function(Dialog): void } */
        this.onNegativeButtonClickListener = Dialog.onButtonClickListener
        /** @type {function(Dialog): void } */
        this.onNeutralButtonClickListener = Dialog.onButtonClickListener
        /** @type {function(Dialog): void } */
        this.onPositiveButtonClickListener = Dialog.onButtonClickListener
        /** @type {function(Dialog): void } */
        this.onShowListener = Dialog.onShowListener
        /** @type {string} */
        this.style = Dialog.STYLE_DEFAULT
        // 
        super.view = app.element('div').view('dialog').appendChild(
            app.element('div').appendChild(
                app.element('img').class('icon'),
                app.element('div')
            ),
            app.element('div'),
            app.element('div'),
            app.element('div').appendChild(
                app.element('button'),
                app.element('button'),
                app.element('button')
            ),
        )
        app.addEventListenerInterface('click|keydown', this, false)
        app.addEventListenerInterface('input', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @readonly @type {string} */
    static STYLE_DEFAULT = ''
    /** @readonly @type {string} */
    static STYLE_MULTICHOICE = 'multichoice'
    /** @readonly @type {string} */
    static STYLE_SINGLECHOICE = 'singlechoice'

    /** @readonly @type {number} */
    static BUTTON_NEUTRAL = 0
    /** @readonly @type {number} */
    static BUTTON_NEGATIVE = 1
    /** @readonly @type {number} */
    static BUTTON_POSITIVE = 2

    /** @readonly @type {string} */
    static BUTTON_TEXT_NEUTRAL = 'DONE'
    /** @readonly @type {string} */
    static BUTTON_TEXT_NEGATIVE = 'CANCEL'
    /** @readonly @type {string} */
    static BUTTON_TEXT_POSITIVE = 'OK'

    /** @type {function(Dialog): void } */
    static onButtonClickListener = (dialog) => { }
    /** @type {function(Dialog): void } */
    static onCancelListener = (dialog) => { }
    /** @type {function(Dialog): void } */
    static onDismissListener = (dialog) => { }
    /** @type {function(Dialog, AppElement): void } */
    static onInputListener = (dialog, eleemnt) => { }
    /** @type {function(Dialog, number, boolean): void } */
    static onItemSelectedListener = (dialog, position, isChecked) => { }
    /** @type {function(Dialog, KeyboardEvent): void } */
    static onKeyListener = (dialog, event) => { }
    /** @type {function(Dialog): void } */
    static onShowListener = (dialog) => { }


    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
        if (event.type == 'click') {
            if (this.isVisible() && this.canceledOnTouchOutside && !element.isEqualTo(this.view)) {
                this.dismiss()
            }
            if (element.isEqualTo(this.#getButtonNeutral())) {
                this.onNeutralButtonClickListener(this)
                this.dismiss()
            }
            if (element.isEqualTo(this.#getButtonNegative())) {
                this.onNegativeButtonClickListener(this)
                this.onCancelListener(this)
                this.dismiss()
            }
            if (element.isEqualTo(this.#getButtonPositive())) {
                this.onPositiveButtonClickListener(this)
                this.dismiss()
            }
        }
        if (event.type == 'input') {
            if (this.style == Dialog.STYLE_DEFAULT) {
                this.onInputListener(this, element)
            }
            if (this.style == Dialog.STYLE_MULTICHOICE || this.style == Dialog.STYLE_SINGLECHOICE) {
                for (let [position, item] of enumerate(this.#getBody().children())) {
                    let input = item.children(0)
                    if (input.isEqualTo(element)) {
                        this.onItemSelectedListener(this, position, input.getProperty('checked'))
                    }
                }
            }
        }
        if (event.type == 'keydown') {
            this.onKeyListener(this, event)
        }
    }

    /** @returns {void} */
    cancel() {
        if (this.isVisible()) {
            app.body().removeChild(this.view)
            this.onCancelListener(this)
            this.dismiss()
        }
    }
    /** @returns {void} */
    dismiss() {
        if (this.isVisible()) {
            app.body().removeChild(this.view)
            this.onDismissListener(this)
        }
    }
    /** @returns {AppElement} */
    getBody() {
        return this.#getBody()
    }
    /** @returns {AppElement[]} */
    getItems() {
        return this.#getBody().children()
    }
    /** @param {number} position @returns {AppElement} */
    getItemAt(position) {
        return this.getItems().get(position)
    }
    /** @returns {number} */
    getItemCount() {
        return this.getItems().size()
    }
    /** @returns {string[]} */
    getSelectedMultiChoiceItems() {
        let values = new array()
        for (let item of this.getItems()) {
            let input = item.children(0)
            if (input.getProperty('checked')) {
                values.append(input.getAttribute('value'))
            }
        }
        return values
    }
    /** @returns {string} */
    getSelectedSingleChoiceItem() {
        for (let item of this.getItems()) {
            let input = item.children(0)
            if (input.getProperty('checked')) {
                return input.getAttribute('value')
            }
        }
    }
    /** @param {number} timeout @param {string} identifier @returns {void} */
    prepare(timeout = 3000, identifier = util.identifier()) {
        this.instances.push(identifier)
        setTimeout(() => {
            if (this.instances.includes(identifier)) {
                this.show()
            }
        }, timeout)
        return identifier
    }
    /** @returns {void} */
    removeAllItems() {
        this.#getBody().innerHTML('')
    }
    /** @param {string} value @returns {AppElement} */
    removeItem(value) {
        for (let [position, item] of enumerate(this.getItems())) {
            let input = item.children(0)
            if (input.getAttribute('value') == value) {
                return this.removeItemAt(position)
            }
        }
        return null
    }
    /** @param {number} position @returns {AppElement} */
    removeItemAt(position) {
        let item = this.getItemAt(position)
        if (item) {
            this.#getBody().removeChildAt(position)
        }
        return item
    }
    /** @param {AppElement|number|string} body @returns {void} */
    setBody(body) {
        super.setText(this.#getBody(), body)
    }
    /** @returns {void} */
    setCancelable(cancelable) {
        this.cancelable = cancelable
    }
    /** @returns {void} */
    setCanceledOnTouchOutside(canceledOnTouchOutside) {
        this.canceledOnTouchOutside = canceledOnTouchOutside
        if (this.canceledOnTouchOutside) {
            this.cancelable = true
        }
    }
    /** @param {number|string} height @param {number|string} width @returns {void} */
    setGeometry(height, width) {
        this.setWidth(width)
        this.setHeight(height)
    }
    /** @param {number|string} height @returns {void} */
    setHeight(height) {
        let viewport = app.body()
        height = `${height}`
        if (height.endswith('%')) {
            let percentage = Number(height.slice(0, -1)) / 100
            height = viewport.getHeight() * percentage
        }
        else if (height.endswith('px')) {
            let pixels = Number(height.slice(0, -2))
            height = pixels
        }
        else {
            height = Number(height)
        }
        if (height >= viewport.getHeight()) {
            height = viewport.getHeight() - 10
        }
        this.height = height
        this.view.style('height', height)
    }
    /** @param {AppElement|number|string} icon @returns {void} */
    setIcon(icon) {
        super.setImage(this.#getIcon(), icon).show()
    }
    /** @param {AppElement|number|string} message @returns {void} */
    setMessage(message) {
        super.setText(this.#getMessage(), message)
    }
    /** @param {string|string[][]} items @param {string} checkedItems @returns {void} */
    setMultiChoiceItems(items, checkedItems = []) {
        this.style = Dialog.STYLE_MULTICHOICE
        this.view.attribute(`style: ${this.style}`)
        // items: array = [[title,value],[title,value],...] | string = title:value,title:value,...
        // checkedItems: array = [value,value] | string = value,value...
        items = array.fromdata(items)
        checkedItems = util.istype(checkedItems, 'string') ? checkedItems.split(',') : checkedItems
        for (let itemData of items) {
            let [title, value] = itemData
            let item = app.element('div').appendChild(
                app.element('input').view('checkbox').attribute(`type: checkbox; value: ${value};`),
                app.element('div').text(title)
            )
            if (value != null && checkedItems.includes(value)) {
                item.children(0).attribute('checked: ')
            }
            this.#getBody().appendChild(item)
        }
    }
    /** @param {string} text @param {Listener} listener @returns {void} */
    setNegativeButton(text, listener = null) {
        return this.#setButton(Dialog.BUTTON_NEGATIVE, text, listener)
    }
    /** @param {string} text @param {Listener} listener @returns {void} */
    setNeutralButton(text, listener = null) {
        return this.#setButton(Dialog.BUTTON_NEUTRAL, text, listener)
    }
    /** @param {Listener} listener @returns {void} */
    setOnCancelListener(listener) {
        this.onCancelListener = listener
    }
    /** @param {Listener} listener @returns {void} */
    setOnDismissListener(listener) {
        this.onDismissListener = listener
    }
    /** @param {Listener} listener @returns {void} */
    setOnInputListener(listener) {
        this.onInputListener = listener
    }
    /** @param {Listener} listener @returns {void} */
    setOnItemSelectedListener(listener) {
        this.onItemSelectedListener = listener
    }
    /** @param {Listener} listener @returns {void} */
    setOnKeyListener(listener) {
        this.onKeyListener = listener
    }
    /** @param {Listener} listener @returns {void} */
    setOnShowListener(listener) {
        this.onShowListener = listener
    }
    /** @param {string} text @param {Listener} listener @returns {void} */
    setPositiveButton(text, listener = null) {
        return this.#setButton(Dialog.BUTTON_POSITIVE, text, listener)
    }
    /** @param {string} value @returns {void} */
    selectItem(value) {
        for (let item of this.getItems()) {
            let input = item.children(0)
            if (input.getAttribute('value') == value) {
                input.attribute('checked: ')
                break
            }
        }
    }
    /** @param {number} position @returns {void} */
    selectItemAt(position) {
        for (let [index, item] of enumerate(this.getItems())) {
            let input = item.children(0)
            if (index == position) {
                input.attribute('checked: ')
                break
            }
        }
    }
    /** @param {string|string[][]} items @param {string} checkedItem @returns {void} */
    setSingleChoiceItems(items, checkedItem = null) {
        this.style = Dialog.STYLE_SINGLECHOICE
        this.view.attribute(`style: ${this.style}`)
        // items: string[][] = [[title,value],[title,value],...]
        // items: string = title:value,title:value,...
        // checkedItem: string = value
        for (let itemData of array.fromdata(items)) {
            let [title, value] = itemData
            let item = app.element('div').appendChild(
                app.element('input').attribute(`name: single-choice; type: radio; value: ${value}`),
                app.element('div').text(title)
            )
            if (value != null && value == checkedItem) {
                item.children(0).attribute('checked: ')
            }
            this.#getBody().appendChild(item)
        }
    }
    /** @param {AppElement|number|string} title @returns {void} */
    setTitle(title) {
        super.setText(this.#getTitle(), title)
    }
    /** @param {number|string} width @returns {void} */
    setWidth(width) {
        let viewport = app.body()
        width = `${width}`
        if (width.endswith('%')) {
            let percentage = Number(width.slice(0, -1)) / 100
            width = viewport.getWidth() * percentage
        }
        else if (width.endswith('px')) {
            let pixels = Number(width.slice(0, -2))
            width = pixels
        }
        else {
            width = Number(width)
        }
        this.view.style('width', width)
    }
    /** @param {number} delay @returns {void} */
    show(delay = 10) {
        if (!this.isVisible()) {
            // NOTE: prevent immediate dismissisal after calling show() provided that canceledOnTouchOutside=true and dialog.show() is gui activated
            app.body().appendChild(this.view)
            this.#getBody().setStyleProperty('max-height', this.view.getHeight(false) * 0.8)
            this.onShowListener(this)
            // setTimeout(() => {
            // }, delay)
        }
    }
    // 
    /** @returns {AppElement} */
    #getBody() {
        return this.view.children(2)
    }
    /** @returns {AppElement[]} */
    #getButtons() {
        return this.view.children(3).children()
    }
    /** @returns {AppElement} */
    #getButtonNeutral() {
        return this.view.children(3).children(0)
    }
    /** @returns {AppElement} */
    #getButtonNegative() {
        return this.view.children(3).children(1)
    }
    /** @returns {AppElement} */
    #getButtonPositive() {
        return this.view.children(3).children(2)
    }
    /** @returns {AppElement} */
    #getIcon() {
        return this.view.children(0).children(0)
    }
    /** @returns {AppElement} */
    #getMessage() {
        return this.view.children(1)
    }
    /** @returns {AppElement} */
    #getTitle() {
        return this.view.children(0).children(1)
    }
    /** @param {number} position @param {string} text @param {Listener|null} listener */
    #setButton(position, text, listener = null) {
        let buttons = this.view.children(3).style('display: flex')
        let button = buttons.children(position).text(text).show()
        if (listener) {
            if (position == 0) {
                this.onNeutralButtonClickListener = listener
            }
            if (position == 1) {
                this.onNegativeButtonClickListener = listener
            }
            if (position == 2) {
                this.onPositiveButtonClickListener = listener
            }
        }
        return button
    }
}
class DialogProgress extends Dialog {
    constructor(attributes = {}) {
        super()
        /** @type {number} */
        this.maximum = 100
        /** @type {number} */
        this.progress = 0
        /** @type {string} */
        this.style = DialogProgress.STYLE_HORIZONTAL
        // 
        super.setAttributes(attributes)
        // 
        this.setCancelable(false)
        this.setCanceledOnTouchOutside(false)
        this.setTitle('Please Wait...')
        this.setStyle(DialogProgress.STYLE_HORIZONTAL)
    }
    /** @readonly @type {string} */    
    static STYLE_HORIZONTAL = 'horizontal'
    /** @readonly @type {string} */        
    static STYLE_SPINNER = 'spinner'

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
        super.onEventListenerInterface(event, element)
    }

    /** @returns {number} */
    getMaximum() {
        return this.maximum
    }
    /** @returns {number} */
    getProgress() {
        return this.progres
    }
    /** @returns {string} */
    getProgressStyle() {
        return this.style
    }
    /** @returns {boolean} */
    isFinish() {
        return this.progress == this.maximum
    }
    /** @param {number} increment @returns {number} */
    incrementProgressBy(increment) {
        if (this.style == DialogProgress.STYLE_HORIZONTAL) {
            this.setProgress(this.progress + increment)
        }
    }
    /** @param {number} maximum @returns {void} */
    setMaximum(maximum) {
        if (this.style == DialogProgress.STYLE_HORIZONTAL) {
            this.maximum = maximum
            this.#getProgress().attribute(`max:${this.maximum}`)
        }
    }
    /** @param {number} progress @returns {void} */
    setProgress(progress) {
        if (this.style == DialogProgress.STYLE_HORIZONTAL) {
            this.progress = Math.min(this.maximum, progress)
            this.#getProgress().attribute(`value:${this.progress}`)
            let percentage = Math.round(this.progress * this.maximum) / this.maximum
            this.#getProgressPercentage().text(`${percentage}%`)
            let fractionNumerator = this.progress.toFixed(0)
            let fractionDenominator = this.maximum
            this.#getProgressFraction().text(`${fractionNumerator}/${fractionDenominator}`)
        }
    }
    /** @param {string} style @returns {void} */
    setStyle(style) {
        this.style = style
        this.view.attribute(`style:progress-${this.style}`)
        if (this.style == DialogProgress.STYLE_HORIZONTAL) {
            this.setBody(app.element('div').appendChild(
                app.element('progress').attribute(`max:${this.maximum};value:0`),
                app.element('div').appendChild(
                    app.element('div').text('0%'),
                    app.element('div').text('0/0')
                )
            ))
        }
        if (this.style == DialogProgress.STYLE_SPINNER) {
            this.setBody(app.element('div').appendChild(
                app.element('div')
            ))
        }
    }
    // 
    /** @returns {AppElement} */
    #getProgress() {
        return this.getBody().children(0)
    }
    /** @returns {AppElement} */
    #getProgressFraction() {
        return this.getBody().children(1).children(1)
    }
    /** @returns {AppElement} */
    #getProgressPercentage() {
        return this.getBody().children(1).children(0)
    }
}
class Divider extends View {
    constructor(attributes = {}) {
        super()
        /** @type {string} */
        this.color = app.getStyleProperty(':root', '--color-accent')
        /** @type {string} */
        this.style = Divider.STYLE_SOLID
        // 
        super.view = app.element('div').view(super.getClassName()).attribute(`stlye: ${this.style}`)
        super.setAttributes(attributes)
        // 
    }

    /** @readonly @type {string} */
    static STYLE_SOLID = 'solid'
    /** @readonly @type {string} */
    static STYLE_LINEAR_GRADIENT = 'linear-gradient'

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }

    /** @returns {string} */
    getColor() {
        return this.color
    }
    /** @returns {string} */
    getStyle() {
        return this.style
    }
    /** @param {string} style @returns {void} */
    setColor(color) {
        this.color = color
        if (this.style == Divider.STYLE_SOLID) {
            this.view.style(`background-color: ${this.color}`)
        }
        if (this.style == Divider.STYLE_LINEAR_GRADIENT) {
            this.view.style(`background-color: linear-gradient(to right, transparent, ${this.color}, ${this.color}, transparent)`)
        }
    }
    /** @param {string} style @returns {void} */
    setStyle(style) {
        this.style = style
        this.view.attribute(`stlye: ${this.style}`)
    }
}
class Drawer extends View {
    constructor(attributes = {}) {
        super()
        /** @type {string} */
        this.lock_mode = Drawer.LOCK_MODE_UNLOCKED
        /** @type {string} */
        this.side = Drawer.SIDE_LEFT
        /** @type {string} */
        this.state = Drawer.STATE_CLOSED
        // 
        this.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('click', this, false)
        super.setAttributes(attributes)
    }

    /** @readonly @type {string} */
    static LOCK_MODE_LOCKED_OPEN = 'LOCKED_OPEN'
    /** @readonly @type {string} */
    static LOCK_MODE_LOCKED_CLOSED = 'LOCKED_CLOSED'
    /** @readonly @type {string} */
    static LOCK_MODE_UNLOCKED = 'UNLOCKED'

    /** @readonly @type {string} */
    static SIDE_LEFT = 'LEFT'
    /** @readonly @type {string} */
    static SIDE_RIGHT = 'RIGHT'

    /** @readonly @type {string} */
    static STATE_CLOSED = 'CLOSED'
    /** @readonly @type {string} */
    static STATE_DRAGGING = 'DRAGGING'
    /** @readonly @type {string} */
    static STATE_IDLE = 'IDLE'
    /** @readonly @type {string} */
    static STATE_OPEN = 'OPEN'
    /** @readonly @type {string} */
    static STATE_SETTLING = 'SETTLING'

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
        if (element.isEqualTo(this.view)) {

        } else {

        }
    }

    /** @returns {boolean} */
    isClosed() {
        return this.state == Drawer.STATE_CLOSED
    }
    /** @returns {boolean} */
    isLocked() {
        return this.lock_mode == Drawer.LOCK_MODE_LOCKED_OPEN || this.lock_mode == Drawer.LOCK_MODE_LOCKED_CLOSED
    }
    /** @returns {boolean} */
    isOpen() {
        return this.state == Drawer.STATE_OPEN
    }
    /** @returns {boolean} */
    isUnlocked() {
        return this.lock_mode == Drawer.LOCK_MODE_UNLOCKED
    }
    /** @returns {boolean} */
    isVisible() {
        // TODO: 
        return
    }
    /** @returns {void} */
    lock() {
        if (this.state == Drawer.STATE_OPEN) {
            this.lock_mode = Drawer.LOCK_MODE_LOCKED_OPEN
        }
        if (this.state == Drawer.STATE_CLOSED) {
            this.lock_mode = Drawer.LOCK_MODE_LOCKED_CLOSED
        }
        // TODO: account other states
    }
    /** @returns {string} */
    getSide() {
        return this.side
    }
    /** @returns {string} */
    getLockMode() {
        return this.lock_mode
    }
    /** @param {string} lock_mode @returns {void} */
    setLockMode(lock_mode) {
        this.lock_mode = lock_mode
        // TODO: 
    }
    /** @param {string} side @returns {void} */
    setSide(side) {
        this.side = side
        // TODO: 
    }
    /** @param {string} state @returns {void} */
    setState(state) {
        this.state = state
        // TODO: 
    }
    /** @returns {void} */
    unlock() {
        this.lock_mode = Drawer.LOCK_MODE_UNLOCKED
    }
}
class Calender extends View {
    constructor(attributes = {}) {
        super()
        /** @type {Date} */
        this.date = util.timestamp('object')
        /** @type {number} */
        this.firstDayOfWeek = Calender.DAY_OF_WEEK_SUNDAY
        /** @type {Date} */
        this.selectedDate = util.timestamp('object')
        /** @type {string} */
        this.selectedDateColor = app.configuration('color-accent')
        /** @type {string} */
        this.selectedWeekColor = 'transparent'
        /** @type {Date} */
        this.maxDate = null
        /** @type {Date} */
        this.minDate = null
        /** @type {function(Calender, Date)} */
        this.onDateChangeListener = Calender.onDateChangeListener
        /** @type {function(Calender, AppElement)} */
        this.onSetupDateListener = Calender.onSetDate
        // 
        super.view = app.element('div').view(super.getClassName()).appendChild(
            app.element('div').appendChild(
                app.element('div'),
                app.element('div').innerHTML('Month'),
                app.element('div').innerHTML('Year'),
                app.element('div')
            ),
            app.element('div'),
            app.element('div')
        )
        for (let i = 0; i < 7; i++) {
            this.view.children(1).appendChild(app.element('div'))
        }
        for (let i = 0; i < 35; i++) {
            this.view.children(2).appendChild(app.element('div'))
        }
        app.addEventListenerInterface('click', this, true)
        super.setAttributes(attributes)
        // 
        this.setFirstDayOfWeek(this.firstDayOfWeek)
    }

    /** @readonly @type {number} */
    static DAY_OF_WEEK_SUNDAY = 0
    /** @readonly @type {number} */
    static DAY_OF_WEEK_MONDAY = 1
    /** @readonly @type {number} */
    static DAY_OF_WEEK_TUESDAY = 2
    /** @readonly @type {number} */
    static DAY_OF_WEEK_WEDNESDAY = 3
    /** @readonly @type {number} */
    static DAY_OF_WEEK_THURSDAY = 4
    /** @readonly @type {number} */
    static DAY_OF_WEEK_FRIDAY = 5
    /** @readonly @type {number} */
    static DAY_OF_WEEK_SATURDAY = 6
    /** @readonly @type {number} */
    static MONTH_JANUARY = 0
    /** @readonly @type {number} */
    static MONTH_FEBRUARY = 1
    /** @readonly @type {number} */
    static MONTH_MARCH = 2
    /** @readonly @type {number} */
    static MONTH_APRIL = 3
    /** @readonly @type {number} */
    static MONTH_MAY = 4
    /** @readonly @type {number} */
    static MONTH_JUNE = 5
    /** @readonly @type {number} */
    static MONTH_JULY = 6
    /** @readonly @type {number} */
    static MONTH_AUGUST = 7
    /** @readonly @type {number} */
    static MONTH_SEPTEMBER = 8
    /** @readonly @type {number} */
    static MONTH_OCTOBER = 9
    /** @readonly @type {number} */
    static MONTH_NOVEMBER = 10
    /** @readonly @type {number} */
    static MONTH_DECEMBER = 11

    /** @readonly @type {string[]} */
    static DAYS_OF_WEEK = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    /** @readonly @type {string[]} */
    static MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    /** @type {function(Calender, Date): void} */
    static onDateChangeListener = (calender, date) => { }
    /** @type {function(Calender, AppElement): void} */
    static onSetDate = (calender, element) => { }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
        if (element.id() == this.#getMonthBackward().id()) {
            this.date.setMonth(this.date.getMonth() - 1)
            return this.#setDates()
        }
        if (element.id() == this.#getMonthForward().id()) {
            this.date.setMonth(this.date.getMonth() + 1)
            return this.#setDates()
        }
        for (let date of this.#getDates().children()) {
            date.children(0).style('border-color', '')
            if (date.id() == element.id() || element.isChildOf(date)) {
                this.selectedDate = date.something()
                date.children(0).style('border-color', this.selectedDateColor)
                this.onDateChangeListener(this, date.something())
            }
        }
    }

    /** @param {Date|number|string} date1 @param {Date|number|string} date2 @returns {boolean} */
    static isSameDay(date1, date2 = util.timestamp('object')) {
        date1 = util.timestamp(date1, 'object')
        date2 = util.timestamp(date2, 'object')
        return date1.getFullYear() == date2.getFullYear() && date1.getMonth() == date2.getMonth() && date1.getDate() == date2.getDate()
    }

    /** @returns {Date} */
    getDate() {
        return this.date
    }
    /** @returns {number} */
    getFirstDayOfWeek() {
        return this.firstDayOfWeek
    }
    /** @returns {Date} */
    getSelectedDate() {
        return this.selectedDate
    }
    /** @returns {string} */
    getSelectedDateColor() {
        return this.selectedDateColor
    }
    /** @returns {string} */
    getSelectedWeekColor() {
        return this.selectedWeekColor
    }
    /** @returns {Date} */
    getMaxDate() {
        return this.maxDate
    }
    /** @returns {Date} */
    getMinDate() {
        return this.minDate
    }
    /** @param {...number|Date} values */
    setDate(...values) {
        if (util.istype(values[0], 'date') && values.length == 1) {
            this.date = values[0]
        }
        if (util.istype(values[0], 'number') && values.length == 1) {
            this.date = util.timestamp(values[0])
        }
        if (values.every((value) => util.istype(value, 'number')) && values.length >= 3) {
            this.date = new Date(...values)
        }
        this.#setDates()
    }
    setFirstDayOfWeek(firstDayOfWeek) {
        if (util.istype(firstDayOfWeek, 'string')) {
            firstDayOfWeek = firstDayOfWeek.capitalize()
            firstDayOfWeek = Calender.DAYS_OF_WEEK.index(firstDayOfWeek)
        }
        if (firstDayOfWeek < 0 || 6 < firstDayOfWeek) {
            return
        }
        this.firstDayOfWeek = firstDayOfWeek
        for (let i = 0, index = this.firstDayOfWeek; i < 7; i++) {
            let dayOfWeek = Calender.DAYS_OF_WEEK[index]
            this.#getDaysOfWeek().children(i).innerHTML(dayOfWeek[0])
            index = (index + 1) % 7
        }
        this.#setDates()
    }
    /** @param {Date} selectedDate */
    setSelectedDate(selectedDate) {
        this.selectedDate = selectedDate
        this.#setDates()
    }
    /** @param {string} selectedDateColor */
    setSelectedDateColor(selectedDateColor) {
        this.selectedDateColor = selectedDateColor
        this.#setDates()
    }
    /** @param {string} selectedWeekColor */
    setSelectedWeekColor(selectedWeekColor) {
        this.selectedWeekColor = selectedWeekColor
        this.#setDates()
    }
    /** @param {Listener} listener */
    setOnDateChangeListener(listener) {
        this.onDateChangeListener = listener
    }
    /** @param {Listener} listener */
    setOnSetupDateListener(listener) {
        this.onSetupDateListener = listener
    }
    /** @param {number|string} month */
    setMonth(month) {
        if (util.istype(month, 'string')) {
            month = month.capitalize()
            month = Calender.MONTHS.index(month)
        }
        if (month < 0 || 11 < month) {
            return
        }
        this.date.setMonth(month)
        this.#setDates()
    }
    /** @param {number} year */
    setYear(year) {
        this.date.setFullYear(year)
        this.#setDates()
    }
    #getDaysOfWeek() {
        return this.view.children(1)
    }
    /** @returns {AppElement} */
    #getMonth() {
        return this.view.children(0).children(1)
    }
    /** @returns {AppElement} */
    #getMonthBackward() {
        return this.view.children(0).children(0)
    }
    /** @returns {AppElement} */
    #getMonthForward() {
        return this.view.children(0).children(3)
    }
    /** @returns {AppElement} */
    #getYear() {
        return this.view.children(0).children(2)
    }
    /** @returns {AppElement} */
    #getDates() {
        return this.view.children(2)
    }
    #setDates() {
        let firstDayOfMonth = new Date(this.date)
        firstDayOfMonth.setHours(0, 0, 0, 0)
        firstDayOfMonth.setDate(1)
        let month = Calender.MONTHS[firstDayOfMonth.getMonth()]
        super.setText(this.#getMonth(), month)
        let year = firstDayOfMonth.getFullYear()
        super.setText(this.#getYear(), year)
        let firstDayOfPeriod = new Date(firstDayOfMonth)
        while (firstDayOfPeriod.getDay() != this.firstDayOfWeek) {
            firstDayOfPeriod.setHours(firstDayOfPeriod.getHours() - 24)
        }
        let todayDate = util.timestamp('object')
        let date = new Date(firstDayOfPeriod)
        for (let i = 0; i < 35; i++) {
            if (i == 0) {
                this.minDate = date
            }
            if (i == 34) {
                this.maxDate = date
            }
            let element = this.#getDates().children(i)
            let inMonth = date.getMonth() == firstDayOfMonth.getMonth()
            let isTodayDate = Calender.isSameDay(date, todayDate)
            let isSelectDate = Calender.isSameDay(date, this.selectedDate)
            element.style('opacity', inMonth ? 1 : 0.5)
            element.something(new Date(date))
            element.innerHTML(
                app.element('div').
                    style('background-color', isTodayDate ? this.selectedDateColor : '').style('border-color', isSelectDate ? this.selectedDateColor : '').
                    innerHTML(date.getDate()).
                    outerHTML()
            )
            this.onSetupDateListener(element)
            date.setHours(date.getHours() + 24)
        }
    }
}
class Canvas extends View {
    constructor(attributes = {}) {
        super()
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }
}
class Checkbox extends View {
    constructor(attributes = {}) {
        super()
        /** @type {function(Checkbox, boolean): void } */
        this.onCheckChangeListener = Checkbox.onCheckChangeListener
        // 
        super.view = app.element('div').view(super.getClassName()).appendChild(
            app.element('div').appendChild(),
            app.element('input').view('checkbox').attribute('type: checkbox')
        )
        app.addEventListenerInterface('click', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @type {function(Checkbox, boolean): void } */
    static onCheckChangeListener = (checkbox, checked) => { }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
        if (element.id() == this.#getInput().id()) {
            this.onCheckChangeListener(this, this.isChecked())
        }
    }
    /** @returns {string} */
    getText() {
        return this.#getText().innerHTML()
    }
    /** @returns {string} */
    getTitle() {
        return this.#getTitle().innerHTML()
    }
    /** @returns {boolean} */
    isChecked() {
        return this.#getInput().getProperty('checked')
    }
    /** @returns {boolean} */
    isEnabled() {
        return !this.#getInput().getProperty('disabled')
    }
    /** @param {boolean} checked @returns {void} */
    setChecked(checked) {
        this.#getInput().setProperty('checked', checked)
    }
    /** @param {boolean} enabled @returns {void} */
    setEnabled(enabled) {
        this.#getInput().setProperty('disabled', !enabled)
    }
    /** @param {Listener} listener @returns {void} */
    setOnCheckChangeListener(listener) {
        this.onCheckChangeListener = listener
    }
    /** @param {string} text @returns {void} */
    setText(text) {
        super.setText(this.#getText(), text)
    }
    /** @param {string} title @returns {void} */
    setTitle(title) {
        super.setText(this.#getTitle(), title)
    }
    /** @returns {AppElement} */
    #getInput() {
        return this.view.children(1)
    }
    /** @returns {AppElement} */
    #getText() {
        return this.view.children(0)
    }
    /** @returns {AppElement} */
    #getTitle() {
        return this.view.children(0)
    }
}
class Item extends View {
    constructor(attributes = {}) {
        super()
        /** @type {boolean} */
        this.enabled = true
        /** @type {PopupMenu} */
        this.menu = null
        // 
        super.view = app.element('div').view(super.getClassName()).appendChild(
            app.element('div').appendChild(
                app.element('img').view('icon'),
                app.element('div')
            ),
            app.element('div')
        )
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }

    /** @returns {PopupMenu} */
    getMenu() {
        return this.menu
    }
    /** @returns {number} */
    getOrder() {
    }
    /** @returns {number|null} */
    getPosition() {
        let parent = this.view.parentElement()
        let children = new array(parent.children())
        for (let [position, element] of children.enumerate()) {
            if (element.isEqualTo(this.getView())) {
                return position
            }
        }
        return null
    }
    /** @returns {string} */
    getTitle() {
        return this.#getTitle().innerHTML()
    }
    /** @returns {boolean} */
    hasMenu() {
        return this.menu != null
    }
    /** @returns {boolean} */
    isEnabled() {
        return this.enabled
    }
    /** @returns {boolean} */
    isChecked() {
        let icon = this.#getIcon()
        return icon.getProperty('checked')
    }
    /** @returns {boolean} */
    isCheckable() {
        let icon = this.#getIcon()
        return icon.getTagName() == 'INPUT'
    }
    /** @param {string} title  @returns {boolean} */
    isTitle(title) {
        return this.getTitle() == title
    }
    /** @override */
    isVisible() {
        return this.view.style('visibility') != 'hidden'
    }
    setBody(body) {
        super.setText(this.#getBody(), body)
    }
    /** @param {boolean} checked @returns {void} */
    setChecked(checked) {
        if (!this.isCheckable()) {
            this.setCheckable(true)
        }
        let icon = this.#getIcon()
        icon.setProperty('checked', checked)
    }
    /** @param {boolean} checkable @returns {void} */
    setCheckable(checkable) {
        if (checkable) {
            let view = app.element('input').view('checkbox').attribute('type: checkbox')
            super.setImage(this.#getIcon(), view)
        } else {
            super.setImage(this.#getIcon(), '').hide()
        }
    }
    /** @param {boolean} enabled @returns {void} */
    setEnabled(enabled) {
        this.enabled = enabled
        this.#getIcon().setProperty('disabled', !enabled)
    }
    /** @param {string} icon @returns {void} */
    setIcon(icon) {
        if (icon instanceof Checkbox) {
            super.setImage(this.#getIcon(), icon.getView()).show()
        }
        else {
            super.setImage(this.#getIcon(), icon).show()
        }
    }
    /** @param {PopupMenu} menu @returns {void} */
    setMenu(menu) {
        this.menu = menu
        this.menu.setAnchor(this.getView())
        this.menu.setTitle(this.getTitle())
    }
    /** @param {string} title @returns {void} */
    setTitle(title) {
        super.setText(this.#getTitle(), title)
    }
    /** @param {boolean} visible */
    setVisible(visible) {
        this.view.style('visibility', visible ? 'visible' : 'hidden')
    }
    /** @returns {AppElement} */
    #getBody() {
        return this.view.children(1)
    }
    /** @returns {AppElement} */
    #getIcon() {
        return this.view.children(0).children(0)
    }
    /** @returns {AppElement} */
    #getTitle() {
        return this.view.children(0).children(1)
    }
}
class Label extends View {
    constructor(attributes = {}) {
        super()
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }
}
class Link extends View {
    constructor(attributes = {}) {
        super()
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }
}
class List extends View {
    constructor(attributes = {}) {
        super()
        /** @type {Item[]} */
        this.items = new array()
        /** @type {function(List, Item): void} */
        this.onItemClickListener = List.onItemClickListener
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('click', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @type {function(List, Item): void} */
    static onItemClickListener = (list, item) => { }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
        for (let [position, item] of this.getItems().enumerate()) {
            if (element.isEqualTo(item.getView(), true)) {
                if (!item.isEnabled()) continue
                if (item.isCheckable()) {
                    item.setChecked(!item.isChecked())
                }
                this.onItemClickListener(this, item)
            }
        }
    }

    /** @param {string[]|string} data @returns {Item} */
    addItem(data) {
        let [title, body, icon] = array.fromdata(data)
        let item = new Item()
        item.setTitle(title)
        item.setTag(util.identifier(title))
        if (body) {
            item.setBody(body)
        }
        if (icon) {
            if (icon.startswith('checkbox')) {
                item.setChecked(icon.endswith('true'))
            } else {
                item.setIcon(icon)
            }
        }
        this.items.append(item)
        this.view.appendChild(item.getView())
        return item
    }
    /** @param {string|string[][]} data @returns {void} */
    addItems(data) {
        data = array.fromdata(data)
        for (let itemData of data) {
            this.addItem(itemData)
        }
    }
    /** @returns {Item[]} */
    getItems() {
        return this.items
    }
    /** @param {number} position @returns {Item} */
    getItemAt(position) {
        return this.getItems().get(position)
    }
    /** @returns {number} */
    getItemCount() {
        return this.getItems().size()
    }
    /** @returns {void} */
    removeAllItems() {
        this.items.clear()
        this.view.innerHTML('')
    }
    /** @param {Item} item @returns {Item} */
    removeItem(item) {
        this.items.remove(item)
        this.view.removeChild(item.getView())
        return item
    }
    /** @param {number} position @returns {Item} */
    removeItemAt(position) {
        let item = this.getItemAt(position)
        if (item) this.removeItem(item)
        return item
    }
    /** @param {string|string[][]} data @returns {void} */
    setItems(data) {
        this.removeAllItems()
        this.addItems(data)
    }
    /** @param {Listener} listener */
    setOnItemClickListener(listener) {
        this.onItemClickListener = listener
    }
    /** @returns {number} */
    size() {
        return this.getItemCount()
    }
}
class Menu extends List {
    constructor(attributes = {}) {
        super()
        /** @type {string} */
        this.colorSelect = app.configuration('color-select')
        /** @type {boolean} */
        this.groupDividerEnabled = true
        /** @type {function(Menu, Item): void} */
        this.onMenuItemClickListener = Menu.onMenuItemClickListener
        // 
        // 
    }

    /** @type {function(Menu, Item): void} */
    static onMenuItemClickListener = (menu, item) => { }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
        super.onEventListenerInterface(event, element)
    }

    /**@param {string} groupIdentifier @param {string} itemIdentifier @param {number} order @param {string} title @returns {void} */
    add(groupIdentifier, itemIdentifier, order, title) {

    }
    /** @param {string} groupIdentifier @param {string} itemIdentifier @param {number} order @param {string} title @returns {void} */
    addSubMenu(groupIdentifier, itemIdentifier, order, title) {

    }
    /** @returns {boolean} */
    hasVisibleItems() {
        for (let item of this.getItems()) {
            if (item.isVisible()) {
                return true
            }
        }
        return false
    }
    /** @returns {boolean} */
    isGroupDividerEnabled() {
        return this.groupDividerEnabled
    }
    /** @param {string} groupIdentifier @returns {void} */
    removeGroup(groupIdentifier) {

    }
    /** @param {Item} item @returns {void} */
    selectItem(item) {
        item.getView().dispatchEvent('click')
    }
    /** @param {number} position @returns {void} */
    selectItemAt(position) {
        let item = this.getItemAt(position)
        this.selectItem(item)
    }
    /** @param {boolean} groupDividerEnabled  @returns {void} */
    setGroupDividerEnabled(groupDividerEnabled) {
        this.groupDividerEnabled = groupDividerEnabled
    }
    /** @param {string} groupIdentifier @param {boolean} enabled @returns {void} */
    setGroupEnabled(groupIdentifier, enabled) {

    }
    /** @param {string} groupIdentifier @param {boolean} visible @returns {void} */
    setGroupVisible(groupIdentifier, visible) {

    }
    /** @param {Listener} listener @returns {void} */
    setOnMenuItemClickListener(listener) {
        this.setOnItemClickListener(listener)
    }
}
class MenuBar extends List {
    constructor(attributes = {}) {
        super()
        /** @type {boolean} */
        this.groupDividerEnabled = true
        /** @type {function(MenuBar, Item): void} */
        this.onMenuItemClickListener = MenuBar.onMenuItemClickListener
        // 
        super.view = app.element('div').view(super.getClassName())
        super.setAttributes(attributes)
        // 
    }

    /** @type {function(MenuBar, Item): void} */
    static onMenuItemClickListener = (menuBar, item) => { }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
        super.onEventListenerInterface(event, element)
    }

    /** @returns {boolean} */
    hasVisibleItems() {
        for (let item of this.getItems()) {
            if (item.isVisible()) {
                return true
            }
        }
        return false
    }
    /** @returns {boolean} */
    isGroupDividerEnabled() {
        return this.groupDividerEnabled
    }
    /** @param {Item} item @returns {void} */
    selectItem(item) {
        item.getView().dispatchEvent('click')
    }
    /** @param {number} position @returns {void} */
    selectItemAt(position) {
        let item = this.getItemAt(position)
        this.selectItem(item)
    }
    /** @param {boolean} groupDividerEnabled  @returns {void} */
    setGroupDividerEnabled(groupDividerEnabled) {
        this.groupDividerEnabled = groupDividerEnabled
    }
    /** @param {Listener} listener @returns {void} */
    setOnMenuItemClickListener(listener) {
        this.setOnItemClickListener(listener)
    }
}
class NavigationLink extends View {
    constructor(attributes = {}) {
        super()
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }
}
class Navigation extends View {
    constructor(attributes = {}) {
        super()
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }
}
class Picker extends View {
    constructor(attributes = {}) {
        super()
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }
}
class Popup extends View {
    constructor(attributes = {}) {
        super()
        /** @type {AppElement} */
        this.anchor = null
        /** @type {boolean} */
        this.autoDismiss = true
        /** @type {boolean} */
        this.dismissOnTouchOutside = false
        /** @type {number} */
        this.dismissTimeout = 2000
        /** @type {function(Popup): void} */
        this.onDismissListener = Popup.onDismissListener
        /** @type {function(Popup): void} */
        this.onShowListener = Popup.onShowListener
        /** @type {number} */
        this.positionX = 0
        /** @type {number} */
        this.positionY = 0
        /** @type {string} */
        this.side = Popup.SIDE_RIGHT
        /** @type {number} */
        this.timeoutID = null
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('click', this, false)
        super.setAttributes(attributes)
        // 
    }

    /** @readonly @type {string} */
    static SIDE_LEFT = 'LEFT'
    /** @readonly @type {string} */
    static SIDE_RIGHT = 'RIGHT'

    /** @type {function(Popup): void} */
    static onDismissListener = (popup) => { }
    /** @type {function(Popup): void} */
    static onShowListener = (popup) => { }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
        if (this.isVisible()) {
            if (element.isEqualTo(this.view)) {
                clearTimeout(this.timeoutID)
                this.dismiss()
            } else {
                if (this.dismissOnTouchOutside) {
                    this.dismiss()
                }
            }
        }
        if (!this.isVisible() && this.isAnchor()) {
            if (element.isEqualTo(this.anchor)) {
                this.showOn()
            }
        }
    }

    /** @returns {void} */
    dismiss() {
        // NOTE: anchor non-existent provided that anchor is an popup menu item
        // timeout maintains anchor's existence during operations in Popup.showOn()
        setTimeout(() => {
            if (this.isVisible()) {
                clearTimeout(this.timeoutID)
                app.body().removeChild(this.view)
                this.onDismissListener(this)
            }
        }, 10)
    }
    /** @returns {AppElement} */
    getAnchor() {
        return this.anchor
    }
    /** @returns {number} */
    getDismissTimeout() {
        return this.dismissTimeout
    }
    /** @returns {boolean} */
    isAnchor() {
        return this.anchor != null
    }
    /** @returns {boolean} */
    isAutoDismiss() {
        return this.autoDismiss
    }
    /** @returns {boolean} */
    isDismissOnTouchOutside() {
        return this.dismissOnTouchOutside
    }
    /** @param {AppElement|Element|string} anchor @returns {void} */
    setAnchor(anchor) {
        this.anchor = app.element(anchor)
    }
    /** @param {boolean} autoDismiss @returns {void} */
    setAutoDismiss(autoDismiss) {
        this.autoDismiss = autoDismiss
    }
    /** @param {AppElement|string} body @returns {void} */
    setBody(body) {
        super.setText(this.#getBody(), body)
    }
    /** @param {number} dismissTimeout @returns {void} */
    setDismissTimeout(dismissTimeout) {
        this.dismissTimeout = dismissTimeout
    }
    /** @param {boolean} dismissOnTouchOutside @returns {void} */
    setDismissOnTouchOutside(dismissOnTouchOutside) {
        this.dismissOnTouchOutside = dismissOnTouchOutside
    }
    /** @param {Listener} listener @returns {void} */
    setOnDismissListener(listener) {
        this.onDismissListener = listener
    }
    /** @param {Listener} listener @returns {void} */
    setOnShowListener(listener) {
        this.onShowListener = listener
    }
    /** @param {number} x @param {number} y @returns {void} */
    setPosition(x, y) {
        this.positionX = x
        this.positionY = y
    }
    /** @returns {void} */
    show() {
        if (!this.isVisible()) {
            app.body().appendChild(this.view)
            this.onShowListener(this)
        }
    }
    /** @param {number} x @param {number} y @returns {void} */
    showAt(x = this.positionX, y = this.positionY) {
        this.show()
        let viewWidth = this.view.getWidth()
        let viewHeight = this.view.getHeight()
        let viewportWidth = app.body().getWidth()
        let viewportHeight = app.body().getHeight()
        let left = x + viewWidth > viewportWidth ? x - viewWidth - 10 : x
        let top = y + viewHeight > viewportHeight ? y - viewHeight - 10 : y
        left = left < 0 ? 10 : left
        top = top < 0 ? 10 : top
        this.view.style('left', left).style('top', top)
        clearTimeout(this.timeoutID)
        if (this.autoDismiss) {
            this.timeoutID = setTimeout(() => this.dismiss(), this.dismissTimeout)
        }
        this.show()
    }
    /** @param {AppElement|Element|string} anchor @param {string} side @returns {void} */
    showOn(anchor = this.anchor, side = Popup.SIDE_RIGHT) {
        this.setAnchor(anchor)
        let rect = anchor.getBoundingClientRect()
        let x
        let y
        if (side == Popup.SIDE_LEFT) {
            x = rect.x
            y = rect.y
        }
        if (side == Popup.SIDE_RIGHT) {
            x = rect.x + rect.width
            y = rect.y
        }
        let element = this.anchor
        do {
            element = element.parentElement()
            if (element.isTagName('BODY')) break
            x += element.getProperty('scrollLeft')
            y += element.getProperty('scrollTop')
            // print(`lengthX=${element.getProperty('offsetWidth')}, lengthY=${element.getProperty('offsetHeight')}, scrollX=${element.getProperty('scrollLeft')}, scrollY=${element.getProperty('scrollTop')}`)
            // print(`x=${x}, y=${y}`)
        } while (true)
        x = x == 0 ? 10 : x
        y = y == 0 ? 10 : y
        this.showAt(x, y)
    }
    /** @returns {AppElement} */
    #getBody() {
        return this.view
    }
}
class PopupMenu extends Popup {
    constructor(attributes = {}) {
        super()
        /** @type {Menu} */
        this.menu = new Menu()
        /** @type {number} */
        this.onMenuItemClickDismissTimeout = 300
        /** @type {function(PopupMenu, Item): void} */
        this.onMenuItemClickListener = PopupMenu.onMenuItemClickListener
        // 
        super.view = app.element('div').view(super.getClassName()).appendChild(
            app.element('div'),
            this.menu.getView()
        )
        super.setAttributes(attributes)
        // 
        this.setDismissOnTouchOutside(true)
    }

    /** @type {function(PopupMenu, Item): void} */
    static onMenuItemClickListener = (popupMenu, item) => { }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
        super.onEventListenerInterface(event, element)
    }

    /** @param {string[]|string} data @returns {Item} */
    addItem(data) {
        return this.menu.addItem(data)
    }
    /** @param {string|string[][]} data @returns {void} */
    addItems(data) {
        return this.menu.addItems(data)
    }
    /** @param {string} identifier @returns {Item|null} */
    findItem(identifier) {
        return this.menu.findItem(identifier)
    }
    /** @param {number} position @returns {Item} */
    getItemAt(position) {
        return this.menu.getItemAt(position)
    }
    /** @returns {number} */
    getItemCount() {
        return this.menu.getItemCount()
    }
    /** @returns {Item[]} */
    getItems() {
        return this.menu.getItems()
    }
    /** @returns {Menu} */
    getMenu() {
        return this.menu
    }
    /** @returns {string} */
    getTitle() {
        return this.#getTitle().text()
    }
    /** @returns {boolean} */
    hasVisibleItems() {
        return this.menu.hasVisibleItems()
    }
    /** @returns {void} */
    removeAllItems() {
        this.menu.removeAllItems()
    }
    /** @param {Item} item @returns {Item} */
    removeItem(item) {
        return this.menu.removeItem(item)
    }
    /** @param {number} position @returns {Item} */
    removeItemAt(position) {
        return this.menu.removeItemAt(position)
    }
    /** @param {Item} item @returns {void} */
    selectItem(item) {
        this.menu.selectItem(item)
    }
    /** @param {number} position @returns {void} */
    selectItemAt(position) {
        this.menu.selectItemAt(position)
    }
    /** @param {string|string[][]} data @returns {void} */
    setItems(data) {
        return this.menu.setItems(data)
    }
    /** @param {Menu} menu @returns {void} */
    setMenu(menu) {
        this.menu = menu
        this.view.removeChildAt(1)
        this.view.appendChild(this.menu.getView())
    }
    /** @param {Listener} listener @returns {void} */
    setOnMenuItemClickListener(listener) {
        this.menu.setOnItemClickListener((menu, item) => {
            listener(this, item)
        })
    }
    /** @param {string} title @returns {void} */
    setTitle(title) {
        super.setText(this.#getTitle(), title).show()
    }
    /** @returns {number} */
    size() {
        return this.menu.size()
    }
    /** @returns {AppElement} */
    #getBody() {
        return this.view.children(1)
    }
    /** @returns {AppElement} */
    #getTitle() {
        return this.view.children(0)
    }
}
class Progress extends View {
    constructor(attributes = {}) {
        super()
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }
}
class ProgressBar extends View {
    constructor(attributes = {}) {
        super()
        /** @type {string} */
        this.indeterminate = false
        /** @type {number} */
        this.indeterminateBehavior = ProgressBar.INDETERMINATE_BEHAVIOR_CYCLE
        /** @type {number} */
        this.indeterminateDuration = 100
        /** @type {string} */
        this.indeterminateColor = app.configuration('color-accent')
        /** @type {number} */
        this.max = 100
        /** @type {number} */
        this.min = 0
        /** @type {number} */
        this.progress = 0
        // 
        super.view = app.element('div').view(super.getClassName())
        super.setAttributes(attributes)
        // 
    }

    /** @readonly @type {string} */
    static INDETERMINATE_BEHAVIOR_CYCLE = 'CYCLE'
    /** @readonly @type {string} */
    static INDETERMINATE_BEHAVIOR_REPEAT = 'REPEAT'

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }
}
class RadioButton extends View {
    constructor(attributes = {}) {
        super()
        // 
        super.view = app.element('div').view(super.getClassName())
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }
}
class RadioGroup extends View {
    constructor(attributes = {}) {
        super()
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('click', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }
}
class SeekBar extends View {
    constructor() {
        super()
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }

}
class Scroller extends View {
    constructor(attributes = {}) {
        super()
        /** @type {function(Scroller, Event): void} */
        this.onTouchEvent = Scroller.onTouchEvent
        // 
        super.view = app.element('div').view(super.getClassName())
        super.setAttributes(attributes)
        // 
    }

    /** @type {function(Scroller, Event): void} */
    static onTouchEvent = (scroller, event) => { }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }

    static computeScrollOffset() {

    }

    extendDuration(extent) {

    }
    getCurrX() {
    }
    getCurrY() {
    }
    getCurrVelocity() {

    }
    getDuration() {
    }
    getFinalX() {
    }
    getFinalY() {
    }
    getStartX() {
    }
    getStartY() {
    }
    fling(startX, startY, velocityX, velocityY, minX, minY, mxX, maxY) {

    }
    forceFinish(finish) {

    }
    isFinished() {
    }
    isSmoothScrollingEnabled() {
        return
    }
    pageScroll() {

    }
    scrollTo(scrollTo) {

    }
    setFinalX(x) {
    }
    setFinalY(c) {
    }
    setFriction(friction) {

    }
    setOnTouchEvent(onTouchEvent) {
        this.onTouchEvent = onTouchEvent
    }
    smoothSCrollTo(scrollTo) {

    }
    smoothScrollBy(scrollBy) {

    }
    startScroll() {
    }
    timePassed() {
        return
    }
}
class Search extends View {
    constructor(attributes = {}) {
        super()
        /** @type {function(Search): void} */
        this.onCloseListener = Search.onCloseListener
        /** @type {function(Search, Event): void} */
        this.onKeyListener = Search.onKeyListener
        /** @type {function(Search): void} */
        this.onOpenListener = Search.onOpenListener
        /** @type {function(Search): void} */
        this.onQueryTextListener = Search.onQueryTextListener
        /** @type {function(Search): void} */
        this.onSearchClickListener = Search.onSearchClickListener
        /** @type {number|string} */
        this.maxWidth = '100%'
        /** @type {string[]} */
        this.suggestions = []
        let suggestionsListId = util.identifier()
        // 
        super.view = app.element('div').view(super.getClassName()).appendChild(
            app.element('input').attribute(`list: ${suggestionsListId}; type: search`).style('visibility: hidden'),
            app.element('img').view('icon'),
            app.element('datalist').identifier(suggestionsListId)
        )
        app.addEventListenerInterface('click|input', this, true)
        super.setAttributes(attributes)
        // 
        this.setIcon('search')
        this.setQueryHint('Search...')
    }

    /** @type {function(Search): void} */
    static onCloseListener = (search) => { }
    /** @type {function(Search, Event): void} */
    static onKeyListener = (search, event) => { }
    /** @type {function(Search): void} */
    static onOpenListener = (search) => { }
    /** @type {function(Search, string): void} */
    static onQueryTextListener = (search, text) => { }
    /** @type {function(Search): void} */
    static onSearchClickListener = (search,) => { }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
        if (event.type == 'click' && element.equals(this.#getIcon())) {
            let input = this.#getInput()
            if (input.style('visibility') == 'visible') {
                this.close()
            } else {
                this.open()
            }
        }
        if (event.type == 'input' && element.equals(this.#getInput())) {
            let text = this.#getInput().value()
            this.onQueryTextListener(this, text)
        }
    }

    /** @returns {void} */
    close() {
        this.#getInput().style('visibility: hidden; width: 0%;')
        setTimeout(() => this.#getIcon().style('margin: unset;'), 500)
        this.onCloseListener(this)
    }
    /** @returns {string} */
    getInputType(inputType) {
        return this.#getInput().getAttribute('type')
    }
    /** @returns {number|string} */
    getMaxWidth() {
        return this.maxWidth
    }
    /** @returns {string} */
    getQuery() {
        return this.#getInput().value()
    }
    /** @returns {string} */
    getQueryHint() {
        return this.#getInput().getAttribute('placeholder')
    }
    /** @returns {string[]} */
    getSuggestions() {
        return this.suggestions
    }
    /** @returns {boolean} */
    isIconified() {
        return this.#getIcon().display()
    }
    /** @returns {void} */
    open() {
        this.#getIcon().style('margin: 0 0 0 10px;')
        this.#getInput().style(`visibility: visible; width: ${this.maxWidth};`)
        this.onOpenListener(this)
    }
    /** @param {AppElement|string} icon @returns {void} */
    setIcon(icon) {
        super.setImage(this.#getIcon(), icon)
    }
    /** @param {boolean} iconified @returns {void} */
    setIconified(iconified) {
        this.#getIcon().display(iconified)
    }
    /** @param {string} inputType @returns {void} */
    setInputType(inputType) {
        if (excludes(inputType, 'color|date|datetime|local|email|month|number|range|tel|text|time|url|week')) console.error(`ValueError: variable-name=inputType variable-value=${inputType}`)
        this.#getInput().setAttribute('type', inputType)
    }
    /** @param {number|string} maxWidth @returns {void} */
    setMaxWidth(maxWidth) {
        this.maxWidth = maxWidth
    }
    /** @param {Listener} listener @returns {void} */
    setOnCloseListener(listener) {
        this.onCloseListener = listener
    }
    /** @param {Listener} listener @returns {void} */
    setOnKeyListener(listener) {
        this.onKeyListener = listener
    }
    /** @param {Listener} listener @returns {void} */
    setOnOpenListener(listener) {
        this.onOpenListener = listener
    }
    /** @param {Listener} listener @returns {void} */
    setOnQueryTextListener(listener) {
        // onQueryTextChange
        this.onQueryTextListener = listener
    }
    /** @param {Listener} listener @returns {void} */
    setOnSearchClickListener(listener) {
        this.onSearchClickListener = listener
    }
    /** @param {string} query @param {boolean} submit  @returns {void} */
    setQuery(query, submit = false) {
        this.#getInput().value(query)
        if (submit) {
            this.#getInput().dispatchEvent('input')
        }
    }
    /** @param {string} query @returns {void} */
    setQueryHint(queryHint) {
        this.#getInput().attribute(`placeholder: ${queryHint}`)
    }
    /** @param {string|string[]} suggestions @returns {void} */
    setSuggestions(suggestions) {
        suggestions = array.fromdata(suggestions, false)
        let innerHTML = suggestions.map((suggestion) => `<option>${suggestion}</option>`).join('')
        this.#getSuggestions().innerHTML(innerHTML)
    }
    #getSuggestions() {
        return this.view.children(2)
    }
    /** @returns {AppElement} */
    #getIcon() {
        return this.view.children(1)
    }
    /** @returns {AppElement} */
    #getInput() {
        return this.view.children(0)
    }
}
class Selector extends View {
    constructor(attributes = {}) {
        super()
        /** @type {function(Selector, number, string): void } */
        this.onItemClickListener = Selector.onItemClickListener
        // 
        super.view = app.element('div').view(super.getClassName()).appendChild(
            app.element('div'),
            app.element('select')
        )
        app.addEventListenerInterface('input', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @type {function(Selector, number, string): void } */
    static onItemClickListener = (selector, position, value) => { }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
        if (element.isEqualTo(this.#getSelect())) {
            for (let [position, item] of enumerate(this.getItems())) {
                let value = item.value()
                if (this.getSelectedItem() == value) {
                    this.onItemClickListener(this, position, value)
                }
            }
        }
    }

    /** @param {string[]|string} data @returns {AppElement} */
    addItem(data) {
        data = array.fromdata(data)
        let [title, value] = data
        let item = app.element('option').innerHTML(title).value(value)
        this.#getSelect().appendChild(item)
        return item
    }
    /** @param {string|string[][]} data @returns {void} */
    addItems(data) {
        data = array.fromdata(data)
        for (let itemData of data) {
            this.addItem(itemData)
        }
    }
    /** @returns {AppElement[]} */
    getItems() {
        return new array(this.#getSelect().children())
    }
    /** @param {number} position @returns {AppElement} */
    getItemAt(position) {
        return this.getItems().get(position)
    }
    /** @returns {number} */
    getItemCount() {
        return this.getItems().size()
    }
    /** @returns {string} */
    getSelectedItem() {
        return this.#getSelect().value()
    }
    /** @param {string} value @returns {boolean} */
    isItem(value) {
        for (let item of this.getItems()) {
            if (item.value() == `${value}`) {
                return true
            }
        }
        return false
    }
    /** @param {string} value @returns {boolean} */
    isSelectedItem(value) {
        return this.#getSelect().value() == value
    }
    /** @returns {void} */
    removeAllItems() {
        this.#getSelect().innerHTML('')
    }
    /** @param {string} value @returns {AppElement} */
    removeItem(value) {
        for (let [position, item] of this.getItems().enumerate()) {
            if (item.value() == value) {
                return this.removeItemAt(position)
            }
        }
        return null
    }
    /** @param {number} position @returns {AppElement} */
    removeItemAt(position) {
        let item = this.getItemAt(position)
        if (item) this.#getSelect().removeChildAt(position)
        return item
    }
    /** @param {string} value @returns {void} */
    selectItem(value) {
        if (this.isItem(value)) {
            this.#getSelect().value(value)
        }
    }
    /** @param {number} position @returns {void} */
    selectItemAt(position) {
        let value = this.getItemAt(position).value()
        this.selectItem(value)
    }
    /** @param {string|string[][]} data @returns {void} */
    setItems(data) {
        this.removeAllItems()
        this.addItems(data)
    }
    /** @param {Listener} listener */
    setOnItemClickListener(listener) {
        this.onItemClickListener = listener
    }
    /** @param {AppElement|number|string|null} title @returns {void} */
    setTitle(title) {
        super.setText(this.#getTitle(), title)
    }
    /** @returns {number} */
    size() {
        return this.getItemCount()
    }
    /** @returns {AppElement} */
    #getTitle() {
        return this.view.children(0)
    }
    /** @returns {AppElement} */
    #getSelect() {
        return this.view.children(1)
    }
}
class Slider extends View {
    constructor(attributes = {}) {
        super()
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }
}
class Stepper extends View {
    constructor(attributes = {}) {
        super()
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }
}
class Switch extends View {
    constructor(attributes = {}) {
        super()
        /** @type {boolean} */
        this.showText = true
        /** @type {string} */
        this.backgroundColor = app.configuration('color-accent')
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('click', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }

    getShowText() {
        return this.showText
    }
    isChecked() {
        return
    }
    setChecked(checked) {

    }
    setShowText(showText) {
        this.showText = showText
    }

    #getText() {

    }
    #getThumb() {

    }
}
class Tab extends View {
    constructor(attributes = {}) {
        super()
        /** @type {boolean} */
        this.selected = false
        // 
        super.view = app.element('div').view(super.getClassName()).appendChild(
            app.element('div').appendChild(
                app.element('img').class('icon'),
                app.element('div').class('single-line')
            )
        )
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }

    /** @returns {number} */
    getPosition() {
        let tabs = this.view.parentElement().children()
        for (let [position, tab] of enumerate(tabs)) {
            if (tab.isEqualTo(this.view)) {
                return position
            }
        }
        return -1
    }
    /** @returns {boolean} */
    isSelected() {
        return this.selected
    }
    /** @returns {void} */
    select() {
        this.selected = true
        let color = app.getStyleProperty(':root', '--color-accent')
        this.view.scrollIntoView()
        this.view.setStyleProperty('border-bottom-color', color)
    }
    /** @param {AppElement|string} icon @returns {void} */
    setIcon(icon) {
        super.setImage(this.#getIcon(), icon).show()
    }
    /** @param {AppElement|string} text @returns {void} */
    setText(text) {
        super.setText(this.#getText(), text)
        return this
    }
    /** @returns {void} */
    unselect() {
        if (this.selected) {
            this.selected = false
            let color = 'transparent'
            this.view.setStyleProperty('border-bottom-color', color)
        }
    }
    /** @returns {AppElement} */
    #getIcon() {
        return this.view.children(0).children(0)
    }
    /** @returns {AppElement} */
    #getText() {
        return this.view.children(0).children(1)
    }
}
class Tabs extends View {
    constructor(attributes = {}) {
        super()
        /** @type {boolean} */
        this.locked = false
        /** @type {function(Tabs, Tab): void} */
        this.onTabSelectedListener = Tabs.onTabSelectedListener
        /** @type {Tab[]} */
        this.tabs = new array()
        /** @type {string} */
        this.tabMode = Tabs.TAB_MODE_AUTO
        /** @type {ViewSwitcher} */
        this.viewSwitcher = new ViewSwitcher()
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('click', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @readonly @type {string} */
    static TAB_MODE_AUTO = 'AUTO'
    /** @readonly @type {string} */
    static TAB_MODE_FIXED = 'FIXED'
    /** @readonly @type {string} */
    static TAB_MODE_SCROLLABLE = 'SCROLLABLE'

    /** @readonly @type {string} */
    static TAB_LABEL_VISIBILITY_LABELED = 'LABELED'
    /** @readonly @type {string} */
    static TAB_LABEL_VISIBILITY_UNLABELED = 'UNLABELED'

    /** @type {function(Tabs, Tab): void} */
    static onTabSelectedListener = (tabs, tab) => { }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
        if (!this.locked) {
            for (let [position, tab] of enumerate(this.tabs)) {
                if (element.isEqualTo(tab.getView())) {
                    this.tabs.map((tab) => tab.unselect())
                    tab.select()
                    this.onTabSelectedListener(this, tab)
                    this.viewSwitcher.showViewAt(position)
                    break
                }
            }
        }
    }

    /** @param {string[]|string} data @param {boolean} selected @returns {Tab} */
    addTab(data, selected = false) {
        let [title, body, icon] = array.fromdata(data)
        let tab = new Tab()
        tab.setText(title)
        tab.setTag(util.identifier(title))
        if (icon) {
            tab.setIcon(icon)
        }
        this.tabs.append(tab)
        this.view.appendChild(tab.getView())
        if (selected || this.getTabCount() == 1) {
            tab.getView().dispatchEvent('click')
        }
        this.#setTabs()
        return tab
    }
    /** @returns {Tab|null} */
    getSelectedTab() {
        for (let [position, tab] of enumerate(this.getTabs())) {
            if (tab.isSelected()) {
                return tab
            }
        }
        return null
    }
    /** @returns {number} */
    getSelectedTabPosition() {
        for (let [position, tab] of enumerate(this.getTabs())) {
            if (tab.isSelected()) {
                return position
            }
        }
        return -1
    }
    /** @param {number} position @returns {Tab} */
    getTabAt(position) {
        return this.getTabs().get(position)
    }
    /** @returns {number} */
    getTabCount() {
        return this.getTabs().size()
    }
    /** @returns {string} */
    getTabMode() {
        return this.tabMode
    }
    /** @returns {Tab[]} */
    getTabs() {
        return this.tabs
    }
    /** @returns {boolean} */
    isLocked() {
        return this.locked
    }
    /** @returns {void} */
    lock() {
        this.setLocked(true)
    }
    /** @returns {void} */
    removeAllTabs() {
        this.tabs.clear()
        this.view.innerHTML('')
    }
    /** @param {Tab} tab @returns {void} */
    removeTab(tab) {
        this.tabs.remove(tab)
        this.view.removeChild(tab.getView())
        this.#setTabs()
    }
    /** @param {number} position @returns {void} */
    removeTabAt(position) {
        let tab = this.getTabAt(position)
        if (tab) {
            this.removeTab(tab)
        }
    }
    /** @param {Tab} tab @returns {void} */
    selectTab(tab) {
        tab.getView().dispatchEvent('click')
    }
    /** @param {number} position @returns {void} */
    selectTabAt(position) {
        let tab = this.getTabAt(position)
        this.selectTab(tab)
    }
    /** @param {boolean} locked @returns {void} */
    setLocked(locked) {
        this.locked = locked
        let transparency = locked ? '80' : 'ff'
        let color = `${app.getStyleProperty(':root', '--color-accent')}${transparency}`
        this.getSelectedTab().getView().setStyleProperty('border-bottom-color', color)
    }
    /** @param {Listener} listener @returns {void} */
    setOnTabSelectedListener(listener) {
        this.onTabSelectedListener = listener
    }
    /** @param {string} tabMode @returns {void} */
    setTabMode(tabMode) {
        this.tabMode = tabMode
        this.#setTabs()
    }
    /** @returns {void} */
    setupWithViewSwitcher(viewSwitcher) {
        this.viewSwitcher = viewSwitcher
    }
    /** @returns {void} */
    unlock() {
        this.setLocked(false)
    }
    // 
    #setTabs() {
        if (this.tabMode == Tabs.TAB_MODE_AUTO) {
            let width = 100 / this.getTabCount()
            for (let tab of this.getTabs()) {
                tab.getView().style(`width: ${width}%`)
            }
        }
        if (this.tabMode == Tabs.TAB_MODE_FIXED) {
            let width = 100 / this.getTabCount()
            for (let tab of this.getTabs()) {
                tab.getView().style(`width: ${width}%`)
            }
        }
        if (this.tabMode == Tabs.TAB_MODE_SCROLLABLE) {
            for (let tab of this.getTabs()) {
                tab.getView().style(`width: fit-content`)
            }
        }
    }
}
class Table extends View {
    constructor(attributes = {}) {
        super()
        /** @type {boolean} */
        this.actionButtonsEnalbed = true
        /** @type {[]} */
        this.headers = []
        /** @type {function(Table, AppElement): void } */
        this.onActionButtonClickListener = Table.onActionButtonClickListener
        /** @type {function(Table, AppElement): void} */
        this.onRowSelectedListener = Table.onRowSelectedListener
        /** @type {number} */
        this.selectionType = Table.SELECTION_TYPE_SINGLE
        // 
        super.view = app.element('div').view(super.getClassName()).appendChild(
            app.element('div'),
            app.element('div'),
            app.element('div').appendChild(
                app.element('button').identifier('insert'),
                app.element('button').identifier('delete'),
                app.element('button').identifier('update')
            )

        )
        app.addEventListenerInterface('click', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @readonly @type {string} */
    static ACTION_BUTTON_INSERT = 'insert'
    /** @readonly @type {string} */
    static ACTION_BUTTON_DELETE = 'delete'
    /** @readonly @type {string} */
    static ACTION_BUTTON_UPDATE = 'update'

    /** @readonly @type {string} */
    static CELL_TYPE_TEXT = 'text'
    /** @readonly @type {string} */
    static CELL_TYPE_INPUT = 'input'
    /** @readonly @type {string} */
    static CELL_TYPE_SELECTOR = 'selector'

    /** @readonly @type {string} */
    static SELECTION_TYPE_SINGLE = 'SINGLE'
    /** @readonly @type {string} */
    static SELECTION_TYPE_MULTIPLE = 'MULTIPLE'

    /** @type {function(Table, AppElement): void } */
    static onActionButtonClickListener = (table, button) => { }
    /** @type {function(Table, AppElement): void} */
    static onRowSelectedListener = (table, row) => { }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
        for (let row of this.getRows()) {
            if (element.isEqualTo(row)) {
                if (this.selectionType == Table.SELECTION_TYPE_SINGLE) {
                    this.unselectAll()
                    this.selectRow(row)
                }
                if (this.selectionType == Table.SELECTION_TYPE_MULTIPLE) {
                    if (this.isRowSelected(row)) {
                        this.unselectRow(row)
                    } else {
                        this.selectRow(row)
                    }
                }
                this.onRowSelectedListener(this, row)
            }
        }
        for (let [position, button] of enumerate(this.#getActionButtons())) {
            if (element.isEqualTo(button)) {
                this.#getActionButtonDelete().hide()
                this.#getActionButtonUpdate().hide()
                this.onActionButtonClickListener(this, element)
                break
            }
        }
    }

    /** @param {AppElement} row @param {string|{items:string|string[],type:string,text:string}} data @returns {AppElement} */
    addCell(row, data) {
        data = object.fromdata(data)
        /** @type {AppElement} */
        let header = null
        /** @type {AppElement} */
        let cell = null
        if (data.get('type') == Table.CELL_TYPE_TEXT) {
            cell = app.element('div').attribute(`cell-type: ${Table.CELL_TYPE_TEXT}`)
            cell.text(data.get('text', ''))
        }
        if (data.get('type') == Table.CELL_TYPE_INPUT) {
            cell = app.element('input').attribute(`cell-type: ${Table.CELL_TYPE_INPUT}`)
            cell.attribute('type: text; autocomplete: off').value(data.get('text', ''))
        }
        if (data.get('type') == Table.CELL_TYPE_SELECTOR) {
            cell = app.element('select').attribute(`cell-type: ${Table.CELL_TYPE_SELECTOR}`)
            for (let item of array.fromdata(data.get('items', []))) {
                let [title, value] = item
                let option = app.element('option').innerHTML(title).value(value)
                cell.appendChild(option)
            }
            cell.value(data.get('value', ''))
        }
        header = this.getHeaderAt(this.getCellCount() % this.getHeaderCount())
        // row = this.getRowAt(Math.floor(this.getCellCount() / this.getHeaderCount()))
        cell.setStyleProperty('width', header.getStyleProperty('width'))
        row.appendChild(cell)
        return cell
    }
    /** @returns {AppElement} */
    addRow() {
        let row = app.element('div')
        this.#getBody().appendChild(row)
        return row
    }
    /** @param {AppElement} row @param {number} position @returns {AppElement} */
    getCellAt(row, position) {
        return row.children(position)
    }
    /** @returns {number} */
    getCellCount() {
        let count = 0
        for (let row of this.getRows()) {
            count += row.childrenLength()
        }
        return count
    }
    /** @returns {AppElement[]} */
    getCells(row) {
        let cells = []
        for (let row of this.getRows()) {
            cells.append(...row.children())
        }
        return cells
    }
    /** @returns {AppElement} */
    getFooter() {
        return this.#getFooter()
    }
    /** @param {number} position @returns {AppElement} */
    getHeaderAt(position) {
        return this.#getHeader().children(position)
    }
    /** @returns {number} */
    getHeaderCount() {
        return this.getHeaders().size()
    }
    /** @returns {AppElement[]} */
    getHeaders() {
        return this.#getHeader().children()
    }
    /** @param {number} position @returns {AppElement} */
    getRowAt(position) {
        return this.getRows().get(position)
    }
    /** @returns {number} */
    getRowCount() {
        return this.getRows().size()
    }
    /** @returns {AppElement[]} */
    getRows() {
        return this.#getBody().children()
    }
    /** @param {AppElement} row @returns {{string: string}} */
    getRowValues(row) {
        let values = new object()
        values.set('identifier', row.getIdentifier())
        for (let [position, cell] of enumerate(row.children())) {
            let rowKey = this.#getHeader().children(position).text()
            let rowValue
            if (cell.getAttribute('cell-type') == Table.CELL_TYPE_TEXT) {
                rowValue = cell.text()
            }
            if (cell.getAttribute('cell-type') == Table.CELL_TYPE_INPUT) {
                rowValue = cell.value()
            }
            if (cell.getAttribute('cell-type') == Table.CELL_TYPE_SELECTOR) {
                rowValue = cell.value()
            }
            values.set(rowKey, rowValue)
        }
        values.lower()
        return values
    }
    /** @returns {AppElement|null} */
    getSelectedRow() {
        let rows = this.getSelectedRows()
        return rows.get(0)
    }
    /** @returns {AppElement[]} */
    getSelectedRows() {
        let rows = []
        for (let row of this.getRows()) {
            if (this.isRowSelected(row)) {
                rows.append(row)
            }
        }
        return rows
    }
    /** @returns {AppElement[]} */
    getUnselectedRows() {
        let rows = []
        for (let row of this.getRows()) {
            if (!this.isRowSelected(row)) {
                rows.append(row)
            }
        }
        return rows
    }
    /** @returns {boolean} */
    isActionButtonsEnabled() {
        return this.actionButtonsEnalbed
    }
    /** @param {AppElement} row @returns {boolean} */
    isRowSelected(row) {
        return row.hasAttribute('selected')
    }
    /** @returns {void} */
    removeAllRows() {
        this.#getBody().innerHTML('')
    }
    /** @param {AppElement} row @returns {void} */
    removeRow(row) {
        this.#getBody().removeChild(row)
    }
    /** @param {number} position @returns {void} */
    removeRowAt(position) {
        let row = this.getRowAt(position)
        this.removeRow(row)
    }
    /** @returns {void} */
    removeSelectedRows() {
        for (let row of this.getSelectedRows()) {
            this.removeRow(row)
        }
    }
    /** @returns {void} */
    removeUnselectedRows() {
        for (let row of this.getUnselectedRows()) {
            this.removeRow(row)
        }
    }
    /** @param {AppElement} row @returns {void} */
    selectRow(row) {
        if (!this.isRowSelected(row)) {
            row.attribute('selected: ').style(`background-color: ${app.getStyleProperty(':root', '--color-select')}`)
        }
        this.#getActionButtonDelete().show()
        this.#getActionButtonUpdate().show()
    }
    /** @param {number} position @returns {void} */
    selectRowAt(position) {
        let row = this.getRowAt(position)
        this.selectRow(row)
    }
    /** @returns {void} */
    selectAll() {
        for (let row of this.getRows()) {
            this.selectRow(row)
        }
    }
    /** @param {boolean} enabled @returns {void} */
    setActionButtonsEnabled(enabled) {
        this.actionButtonsEnalbed = enabled
        this.#getFooter().display(enabled)
    }
    /** @param {string|string[]} headers @returns {void} */
    setHeaders(headers) {
        this.headers = array.fromdata(headers)
        this.#getHeader().innerHTML('')
        let total = 0
        for (let header of this.headers) {
            let [title, width] = header
            total += Number(width)
            let cell = app.element('div').style(`width: ${width}%`).text(title)
            this.#getHeader().appendChild(cell)
        }
        if (total != 100) {
            console.warn(`ValueError: improper header, width=${total}`)
        }
    }
    /** @returns {AppElement|Element|number|string} */
    setFooter(footer) {
        return super.setText(this.#getFooter(), footer)
    }
    /** @param {Listener} listener @returns {void} */
    setOnActionButtonClickListener(listener) {
        this.onActionButtonClickListener = listener
    }
    /** @param {Listener} listener @returns {void} */
    setOnRowSelectedListener(listener) {
        this.onRowSelectedListener = listener
    }
    /** @param {number} selectionType @returns {void} */
    setSelectionType(selectionType) {
        this.selectionType = selectionType
        this.unselectAll()
    }
    /** @param {AppElement} row @returns {void} */
    unselectRow(row) {
        row.removeAttribute('selected').style('background-color: ')
    }
    /** @param {number} position @returns {void} */
    unselectRowAt(position) {
        let row = this.getRowAt(position)
        this.unselectRow(row)
    }
    /** @returns {void} */
    unselectAll() {
        for (let row of this.getRows()) {
            this.unselectRow(row)
        }
    }
    /** @returns {AppElement[]} */
    #getActionButtons() {
        return this.view.children(2).children()
    }
    /** @returns {AppElement} */
    #getActionButtonInsert() {
        return this.view.children(2).children(0)
    }
    /** @returns {AppElement} */
    #getActionButtonDelete() {
        return this.view.children(2).children(1)
    }
    /** @returns {AppElement} */
    #getActionButtonUpdate() {
        return this.view.children(2).children(2)
    }
    /** @returns {AppElement} */
    #getBody() {
        return this.view.children(1)
    }
    /** @returns {AppElement} */
    #getFooter() {
        return this.view.children(2)
    }
    /** @returns {AppElement} */
    #getHeader() {
        return this.view.children(0)
    }
}
class TableRow extends View {
    constructor(attributes = {}) {
        super()
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }
}
class Text extends View {
    constructor(attributes = {}) {
        super()
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }
    /** @returns {string} */
    getText() {
    }
    /** @param {string} text @returns {void} */
    setText(text) {
    }
}
class TextEditor extends View {
    constructor(attributes = {}) {
        super()
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }
}
class TextField extends View {
    constructor(attributes = {}) {
        super()
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }
}
class Toggle extends View {
    constructor(attributes = {}) {
        super()
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }
}
class Toolbar extends View {
    constructor(attributes = {}) {
        super()
        // 
        super.view = app.element('div').view(super.getClassName())
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }

    setNavigatorIcon(navigatorIcon) {

    }
    setSubtitle(subtitle) {

    }
    setTitle(title) {
    }

    #setNavigatorIcon() {

    }
    #getSubtitle() {

    }
    #getTitle() {
    }
}
class Video extends View {
    constructor(attributes = {}) {
        super()
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }
}
class ViewPager extends View {
    constructor(attributes = {}) {
        super()
        // place properties here ...
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('', this, true)
        super.setAttributes(attributes)
        // 
        // place methods here ...
    }

    /** @type {function(Tabs, Tab): void} */
    static onPageChangeListener = () => {}

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }

    /** @returns {*} */
    get() {
        return null
    }
    /** @param {*} parameter @returns {void} */
    set(parameter) {
        
    }
    /** @param {Listener} listener @returns {void} */
    setOPageChangeListener(listener) {
        // necessary calls back to the provided TabLayout so that the tab position is kept in sync. 
    }

}
class ViewSwitcher extends View {
    constructor(attributes = {}) {
        super()
        /** @type {boolean} */
        this.scrollHorizontally = false
        /** @type {function(ViewSwitcher, AppElement): void} */
        this.onViewChangeListener = ViewSwitcher.onViewChangeListener
        /** @type {number} */
        this.viewPosition = 0
        // 
        super.view = app.element('div').view(super.getClassName())
        super.setAttributes(attributes)
        // 
    }

    /** @type {function(ViewSwitcher, AppElement): void} */
    static onViewChangeListener = (viewSwitcher, view) => {}

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {

    }

    /** @param {AppElement} view @returns {AppElement} */
    addView(view) {
        this.view.appendChild(view)
    }
    /** @returns {AppElement} */
    getCurrentView() {
        return this.getViews().get(this.viewPosition)

    }
    /** @returns {AppElement} */
    getNextView() {
        let position = this.viewPosition + 1 % this.getViewCount()
        return this.getViews().get(position)
    }
    /** @returns {AppElement} */
    getPreviousView() {
        let position = this.viewPosition == 0 ? this.getViewCount() - 1 : this.viewPosition - 1
        return this.getViews().get(position)
    }
    /** @param {number} position @returns {AppElement} */
    getViewAt(position) {
        return this.getViews().get(position)
    }
    /** @returns {number} */
    getViewCount() {
        return this.getViews().size()
    }
    /** @returns {Views[]} */
    getViews() {
        return new array(this.view.children())
    }
    /** @returns {boolean} */
    isScrollHorizontally() {
        return this.scrollHorizontally
    }
    /** @returns {void} */
    removeAllViews() {
        this.view.innerHTML('')
        this.viewPosition = 0
    }
    /** @param {AppElement} view @returns {void} */
    removeView(view) {
        if (view.isEqualTo(this.getCurrentView())) {
            view.remove()
            this.viewPosition = 0
            this.showViewAt(0)
        } else {
            view.remove()
        }
    }
    /** @param {number} position @returns {void} */
    removeViewAt(position) {
        this.view.removeChildAt(position)
        if (position == this.viewPosition) {
            this.viewPosition = 0
            this.showViewAt(0)
        }
    }
    /** @param {number} start @param {number} count @returns {void} */
    removeViews(start, count) {
        // TODO: 
    }
    /** @param {Listener} listener @returns {void} */
    setOnViewChangeListener(listener) {
        this.onViewChangeListener = listener
    }
    /** @param {boolean} scrollHorizontally @returns {void} */
    setScrollHorizontally(scrollHorizontally) {
        this.scrollHorizontally = scrollHorizontally
    }
    /** @returns {void} */
    showNextView() {
        if (this.getViewCount() > 0) {
            let viewPrevious = this.getCurrentView()
            let viewCurrent = this.getNextView()
            viewPrevious.hide()
            viewCurrent.show()
            this.viewPosition = this.viewPosition + 1 % this.getViewCount()
            this.onViewChangeListener(this, viewCurrent)
        }
    }
    /** @returns {void} */
    showPreviousView() {
        if (this.getViewCount() > 0) {
            let viewPrevious = this.getCurrentView()
            let viewCurrent = this.getPreviousView()
            viewPrevious.hide()
            viewCurrent.show()
            this.viewPosition = this.viewPosition == 0 ? this.getViewCount() - 1 : this.viewPosition - 1
            this.onViewChangeListener(this, viewCurrent)
        }
    }
    /** @param {number} position @returns {void} */
    showViewAt(position) {
        if (this.getViewCount() > 0) {
            let viewPrevious = this.getCurrentView()
            let viewCurrent = this.getViewAt(position)
            viewPrevious.hide()
            viewCurrent.show()
            this.viewPosition = position
            this.onViewChangeListener(this, viewCurrent)
        }
    }
}
class WebView extends View {
    constructor(attributes = {}) {
        super()
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('', this, true)
        super.setAttributes(attributes)
        // 
    }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }
}
class Window extends View {
    constructor(attributes = {}) {
        super()
        /** @type {boolean} */
        this.closeable = true
        /** @type {number} */
        this.height = 0
        /** @type {MenuBar} */
        this.menubar = new MenuBar()
        /** @type {boolean} */
        this.moving = false
        /** @type {function(Window): void} */
        this.onCloseListener = Window.onCloseListener
        /** @type {function(Window): void} */
        this.onOpenListener = Window.onOpenListener
        /** @type {number} */
        this.positionX = 0
        /** @type {number} */
        this.positionY = 0
        /** @type {string} */
        this.size = Window.SIZE_MAXIMIZE
        /** @type {number} */
        this.width = 0
        // 
        super.view = app.element('div').view(super.getClassName()).appendChild(
            app.element('div').appendChild(
                app.element('img').view('icon'),
                app.element('div'),
                app.element('img').view('icon'),
                app.element('img').view('icon'),
            ),
            this.menubar.getView(),
            app.element('div'),
            app.element('div')
        )
        app.addEventListenerInterface('click|mousedown', this, true)
        app.addEventListenerInterface('mousemove|mouseup', this, false)
        super.setAttributes(attributes)
        // 
        super.setImage(this.#getSizer(), 'minimize')
        super.setImage(this.#getCloser(), 'close')
        this.setGeometry(Window.POSITION_CENTER, Window.POSITION_CENTER, '75%', '75%')
    }

    /** @readonly @type {string} */
    static POSITION_CENTER = 'CENTER'
    /** @readonly @type {string} */
    static POSITION_END = 'END'
    /** @readonly @type {string} */
    static POSITION_START = 'START'

    /** @readonly @type {string} */
    static SIZE_MAXIMIZE = 'MAXIMIZE'
    /** @readonly @type {string} */
    static SIZE_MINIMIZE = 'MINIMIZE'

    /** @type {function(Window): void} */
    static onCloseListener = (window) => { }
    /** @type {function(MenuBar, Item): void} */
    static onMenuItemClickListener = (menuBar, item) => { }
    /** @type {function(Window): void} */
    static onOpenListener = (window) => { }

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
        if (event.type == 'click') {
            if (element.isEqualTo(this.#getSizer())) {
                if (this.isMaximized()) {
                    this.minimize()
                }
                else {
                    this.maximize()
                }
            }
            if (element.isEqualTo(this.#getCloser())) {
                this.close()
            }
        }
        // TODO: determine when mouse leaves header while movement is activated
        if (event.type == 'mousedown') {
            this.sendForward()
            this.moving = element.isEqualTo(this.#getHeader())
        }
        if (event.type == 'mousemove') {
            let DOMRect = this.#getHeader().getBoundingClientRect()
            if (this.moving) {
                if (event.x <= DOMRect.x || event.y <= DOMRect.y || event.x >= DOMRect.x + DOMRect.width || event.y >= DOMRect.y + DOMRect.height) {
                    this.moving = false
                }
            }
            if (this.moving) {
                this.setPositionX(this.positionX + event.movementX)
                this.setPositionY(this.positionY + event.movementY)
            }
        }
        if (event.type == 'mouseup') {
            this.moving = false
        }
    }

    /** @returns {void} */
    close() {
        if (this.isVisible() && this.isCloseable()) {
            app.body().removeChild(this.getView())
            this.onCloseListener(this)
        }
    }
    /** @returns {AppElement} */
    getBody() {
        return this.#getBody()
    }
    /** @returns {number} */
    getHeight() {
        return this.height
    }
    /** @returns {AppElement} */
    getFooter() {
        return this.#getFooter()
    }
    /** @returns {number} */
    getPositionX() {
        return this.positionX
    }
    /** @returns {number} */
    getPositionY() {
        return this.positionY
    }
    /** @returns {MenuBar} */
    getMenuBar() {
        return this.menubar
    }
    /** @returns {number} */
    getWidth() {
        return this.width
    }
    /** @returns {string} */
    getTitle() {
        return this.#getTitle().text()
    }
    /** @returns {boolean} */
    isCloseable() {
        return this.closeable
    }
    /** @returns {boolean} */
    isMaximized() {
        return this.size == Window.SIZE_MAXIMIZE
    }
    /** @returns {boolean} */
    isMinimized() {
        return this.size == Window.SIZE_MINIMIZE
    }
    /** @returns {void} */
    maximize() {
        this.size = Window.SIZE_MAXIMIZE
        super.setImage(this.#getSizer(), 'minimize', true)
        this.#getMenuBar().show()
        this.#getBody().show()
        this.#getFooter().show()
        this.view.style('height', this.getHeight())
        this.view.style('width', this.getWidth())
    }
    /** @returns {void} */
    minimize() {
        this.size = Window.SIZE_MINIMIZE
        super.setImage(this.#getSizer(), 'maximize', true)
        this.#getMenuBar().hide()
        this.#getBody().hide()
        this.#getFooter().hide()
        this.view.style('height', this.#getHeader().getHeight())
        this.view.style('width', 200)
    }
    /** @returns {void} */
    open() {
        if (!this.isVisible()) {
            app.body().appendChild(this.getView())
            this.sendForward()
            this.onOpenListener(this)
            // NOtE: set view|view.body style property max-height to provide y-axis scrollbar provided that the body's content exceeds max-height
            let percentageView = this.getView().getStylePropertyComputed('max-height')
            let heightView = app.getHeight() * (percentageView.remove('%') / 100)
            this.getView().setStyleProperty('max-height', heightView)
            let percentageBody = this.getBody().getStylePropertyComputed('max-height')
            let heightBody = heightView * (percentageBody.remove('%') / 100)
            this.getBody().setStyleProperty('max-height', heightBody)
        }
    }
    /** @returns {void} */
    sendBack() {
        this.view.style('z-index: 0')
    }
    /** @returns {void} */
    sendForward() {
        for (let element of app.body().getElementsByAttribute('view', 'window')) {
            element.style('z-index: 0')
        }
        this.view.style('z-index: 1')
    }
    /** @param {boolean} closeable @returns {void} */
    setCloseable(closeable) {
        this.closeable = closeable
    }
    /** @param {AppElement|Element|string} body @returns {void} */
    setBody(body) {
        super.setText(this.#getBody(), body)
    }
    /** @param {AppElement|Element|string} footer @returns {void} */
    setFooter(footer) {
        super.setText(this.#getFooter(), footer)
    }
    /** @param {number} positionX @param {number} positionY @param {number} width @param {number} height @returns {void} */
    setGeometry(positionX = this.positionX, positionY = this.positionY, width = this.width, height = this.height) {
        this.setWidth(width)
        this.setHeight(height)
        this.setPositionX(positionX)
        this.setPositionY(positionY)
    }
    /** @param {number|string} height @returns {void} */
    setHeight(height) {
        let viewport = app.body()
        height = `${height}`
        if (height.endswith('%')) {
            let percentage = Number(height.slice(0, -1)) / 100
            height = viewport.getHeight() * percentage
        }
        else if (height.endswith('px')) {
            let pixels = Number(height.slice(0, -2))
            height = pixels
        }
        else if (height == 'fit-content') {
            // height = 'fit-content'
        }
        else {
            height = Number(height)
        }
        if (height >= viewport.getHeight()) {
            height = viewport.getHeight() - 10
        }
        this.height = height
        this.view.style('height', height)
    }
    /** @param {AppElement|string} icon @returns {void} */
    setIcon(icon) {
        super.setImage(this.#getIcon(), icon).show()
    }
    /** @param {MenuBar} menubar @returns {void} */
    setMenuBar(menubar) {
        this.menubar = menubar
    }
    /** @param {Listener} listener @returns {void} */
    setOnCloseListener(listener) {
        this.onCloseListener = listener
    }
    /** @param {Listener} listener @returns {void} */
    setOnMenuItemClickListener(listener) {
        this.menubar.setOnMenuItemClickListener(listener)
    }
    /** @param {Listener} listener @returns {void} */
    setOnOpenListener(listener) {
        this.onOpenListener = listener
    }
    /** @param {number|string} positionX @param {number|string} positionY @returns {void} */
    setPosition(positionX, positionY) {
        this.setPositionX(positionX)
        this.setPositionY(positionY)
    }
    /** @param {number|string} positionX @returns {void} */
    setPositionX(positionX) {
        let viewport = app.body()
        if (positionX == Window.POSITION_CENTER) {
            positionX = (viewport.getWidth() - this.getWidth()) / 2
        }
        else if (positionX == Window.POSITION_END) {
            positionX = viewport.getWidth() - 10
        }
        else if (positionX == Window.POSITION_START) {
            positionX = 10
        }
        else {
            positionX = Number(positionX)
        }
        this.positionX = positionX
        this.view.style('left', positionX)
    }
    /** @param {number|string} positionY @returns {void} */
    setPositionY(positionY) {
        let viewport = app.body()
        if (positionY == Window.POSITION_CENTER) {
            positionY = (viewport.getHeight() - this.getHeight()) / 2
        }
        else if (positionY == Window.POSITION_END) {
            positionY = viewport.getHeight() - 10
        }
        else if (positionY == Window.POSITION_START) {
            positionY = 10
        }
        else {
            positionY = Number(positionY)
        }
        this.positionY = positionY
        this.view.style('top', positionY)
    }
    /** @param {string} title @returns {void} */
    setTitle(title) {
        super.setText(this.#getTitle(), title)
    }
    /** @param {number|string} width @returns {void} */
    setWidth(width) {
        let viewport = app.body()
        width = `${width}`
        if (width.endswith('%')) {
            let percentage = Number(width.slice(0, -1)) / 100
            width = viewport.getWidth() * percentage
        }
        else if (width.endswith('px')) {
            let pixels = Number(width.slice(0, -2))
            width = pixels
        }
        else if (width == 'fit-content') {
            let menuBarWidth = this.#getMenuBar().getWidthChildren(true)
            if (menuBarWidth == 0) {
                width = this.#getBody().getWidth(true)
            } else {
                width = this.#getMenuBar().getWidthChildren(true) + 5
            }
        }
        else {
            width = Number(width)
        }
        this.width = width
        this.view.style('width', width)
    }
    /** @returns {AppElement} */
    #getBody() {
        return this.view.children(2)
    }
    /** @returns {AppElement} */
    #getCloser() {
        return this.view.children(0).children(3)
    }
    /** @returns {AppElement} */
    #getFooter() {
        return this.view.children(3)
    }
    /** @returns {AppElement} */
    #getHeader() {
        return this.view.children(0)
    }
    /** @returns {AppElement} */
    #getIcon() {
        return this.view.children(0).children(0)
    }
    /** @returns {AppElement} */
    #getMenuBar() {
        return this.view.children(1)
    }
    /** @returns {AppElement} */
    #getSizer() {
        return this.view.children(0).children(2)
    }
    /** @returns {AppElement} */
    #getTitle() {
        return this.view.children(0).children(1)
    }
}
class _ extends View {
    constructor(attributes = {}) {
        super()
        // place properties here ...
        // 
        super.view = app.element('div').view(super.getClassName())
        app.addEventListenerInterface('', this, true)
        super.setAttributes(attributes)
        // 
        // place methods here ...
    }

    // place constants here ...

    // place interfaces here ...

    /** @param {Event} event @param {AppElement} element @returns {void} */
    onEventListenerInterface(event, element) {
    }

    /** @returns {*} */
    get() {
        return null
    }
    /** @param {*} parameter @returns {void} */
    set(parameter) {

    }
}
//_________________________________________________________________________________________________________________________________________________//
/** @param {boolean[]|string[]|{}} iterable @returns {boolean} */
window.any = function any(iterable) {
    if (util.istype(iterable, 'array-boolean')) {
        for (let value of iterable) {
            if (value === true) {
                return true
            }
        }
    }
    else if (util.istype(iterable, 'array-string')) {
        for (let value of iterable) {
            if (value.length != 0) {
                return true
            }
        }
    }
    else if (util.istype(iterable, 'object')) {
        for (let key in iterable) {
            return true
        }
    }
    return false
}
/** @param {any[]|{}} iterable */
window.enumerate = function* enumerate(iterable) {
    if (util.istype(iterable, 'array')) {
        for (let index = 0; index < iterable.length; index++) {
            yield [index, iterable[index]]
        }
    }
    else if (util.istype(iterable, 'object')) {
        for (let key in iterable) {
            yield [key, iterable[key]]
        }
    }
    else if (util.istype(iterable, 'string')) {
        for (let index = 0; index < iterable.length; index++) {
            yield [index, iterable[index]]
        }
    }
}
/** @param {string} key @param {string|string[]|{string:string}} iterable @returns {boolean} */
window.excludes = function excludes(key, iterable) {
    // iterable:string='value|{type}|value|{type}|value'
    function istype(value) {
        if (value.startswith('{') && value.endswith('}')) {
            if (util.istype(key, value.strip('{}'))) {
                return true
            }
        }
        return false
    }
    if (!key) {
        return false
    }
    if (util.istype(iterable, 'array')) {
        for (let value of iterable) {
            if (istype(value)) {
                return false
            }
            if (value == key) {
                return false
            }
        }
        return true
    }
    if (util.istype(iterable, 'object')) {
        for (let value in iterable) {
            if (istype(value)) {
                return false
            }
            if (value == key) {
                return false
            }
        }
        return true
    }
    if (util.istype(iterable, 'string')) {
        for (let value of iterable.split('|')) {
            if (istype(value)) {
                return false
            }
            if (value == key) {
                return false
            }
        }
        return true
    }
}
/** @param {string} key @param {string|string[]|{string:string}} iterable @returns {boolean} */
window.includes = function includes(key, iterable) {
    // iterable:string='value|{type}|value|{type}|value'
    function istype(value) {
        if (value.startswith('{') && value.endswith('}')) {
            if (util.istype(key, value.strip('{}'))) {
                return true
            }
        }
        return false
    }
    if (!key) {
        return false
    }
    if (util.istype(iterable, 'array')) {
        for (let value of iterable) {
            if (istype(value)) {
                return true
            }
            if (value == key) {
                return true
            }
        }
        return false
    }
    if (util.istype(iterable, 'object')) {
        for (let [iterableKey, value = iterable[iterableKey]] in iterable) {
            if (istype(value)) {
                return true
            }
            if (value == key) {
                return true
            }
        }
        return false
    }
    if (util.istype(iterable, 'string')) {
        for (let value of iterable.split('|')) {
            if (istype(value)) {
                return true
            }
            if (value == key) {
                return true
            }
        }
        return false
    }
}
/** @param {any} value @param {string} types @returns {boolean} */
window.istype = function istype(value, types) {
    return util.istype(value, types)
}
/** @param {number} number @param {number} nDigits @returns {number} */
window.round = function round(number, nDigits) {
    let multiplier = Math.pow(10, nDigits)
    return Math.round(number * multiplier) / multiplier
}
/** @param {any} value @returns {boolean} */
window.type = function type(value) {
    return typeof value
}

/** @returns {void} */
window.print = console.log

// TESTING


/** */
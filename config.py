priority_lists = {
    "NORTH": [
        "ADQ", "AKN", "ANI", "BET", "BRW", "CDB", "DLG", "DUT", "GAL", "MCG",
        "OME", "OTZ", "SCC", "UNK"
    ],
    "SOUTH": [
        "AFE", "AKW", "ANC", "CDV", "GST", "HNS", "JNU", "KTN", "MDO", "ORT",
        "PSG", "SIT", "SWD", "YAK"
    ],
    "ATOP": ["ADK", "SYA"],
    "HIGH": []  # Replace with real station codes
}
airport_data = [{
    'City': 'Kotlik',
    'ICAO ID': 'PFKO',
    'NAS ID': '2A9',
    'Area': 'NORTH'
}, {
    'City': 'Shaktoolik',
    'ICAO ID': 'PFSH',
    'NAS ID': '2C7',
    'Area': 'NORTH'
}, {
    'City': 'Nondalton',
    'ICAO ID': 'PANO',
    'NAS ID': '5NN',
    'Area': 'SOUTH'
}, {
    'City': 'Allakaket',
    'ICAO ID': 'PFAL',
    'NAS ID': '6A8',
    'Area': 'NORTH'
}, {
    'City': 'Akutan',
    'ICAO ID': 'PAUT',
    'NAS ID': '7AK',
    'Area': 'NORTH'
}, {
    'City': 'Tatitlek',
    'ICAO ID': 'PAKA',
    'NAS ID': '7KA',
    'Area': 'SOUTH'
}, {
    'City': 'Chuathbaluk',
    'ICAO ID': 'PACH',
    'NAS ID': '9A3',
    'Area': 'NORTH'
}, {
    'City': 'Adak',
    'ICAO ID': 'PADK',
    'NAS ID': 'ADK',
    'Area': 'ATOP'
}, {
    'City': 'Kodiak',
    'ICAO ID': 'PADQ',
    'NAS ID': 'ADQ',
    'Area': 'NORTH'
}, {
    'City': 'Kake',
    'ICAO ID': 'PAFE',
    'NAS ID': 'AFE',
    'Area': 'SOUTH'
}, {
    'City': 'Ambler',
    'ICAO ID': 'PAFM',
    'NAS ID': 'AFM',
    'Area': 'NORTH'
}, {
    'City': 'Badami',
    'ICAO ID': 'PABP',
    'NAS ID': 'AK78',
    'Area': 'NORTH'
}, {
    'City': 'Atka',
    'ICAO ID': 'PAAK',
    'NAS ID': 'AKA',
    'Area': 'ATOP'
}, {
    'City': 'Akiak',
    'ICAO ID': 'PFAK',
    'NAS ID': 'AKI',
    'Area': 'NORTH'
}, {
    'City': 'Akhiok',
    'ICAO ID': 'PAKH',
    'NAS ID': 'AKK',
    'Area': 'NORTH'
}, {
    'City': 'King Salmon',
    'ICAO ID': 'PAKN',
    'NAS ID': 'AKN',
    'Area': 'NORTH'
}, {
    'City': 'Anaktuvuk Pass',
    'ICAO ID': 'PAKP',
    'NAS ID': 'AKP',
    'Area': 'NORTH'
}, {
    'City': 'Klawock',
    'ICAO ID': 'PAKW',
    'NAS ID': 'AKW',
    'Area': 'SOUTH'
}, {
    'City': 'Ted Stevens Anchorage Intl',
    'ICAO ID': 'PANC',
    'NAS ID': 'ANC',
    'Area': 'SOUTH'
}, {
    'City': 'Aniak',
    'ICAO ID': 'PANI',
    'NAS ID': 'ANI',
    'Area': 'NORTH'
}, {
    'City': 'Anvik',
    'ICAO ID': 'PANV',
    'NAS ID': 'ANV',
    'Area': 'NORTH'
}, {
    'City': 'Quinhagak',
    'ICAO ID': 'PAQH',
    'NAS ID': 'AQH',
    'Area': 'NORTH'
}, {
    'City': 'Nuiqsut',
    'ICAO ID': 'PAQT',
    'NAS ID': 'AQT',
    'Area': 'NORTH'
}, {
    'City': 'Arctic Village',
    'ICAO ID': 'PARC',
    'NAS ID': 'ARC',
    'Area': 'NORTH'
}, {
    'City': 'Atqasuk Edward Burnell Sr Meml',
    'ICAO ID': 'PATQ',
    'NAS ID': 'ATK',
    'Area': 'NORTH'
}, {
    'City': 'Wainwright',
    'ICAO ID': 'PAWI',
    'NAS ID': 'AWI',
    'Area': 'NORTH'
}, {
    'City': 'Bethel',
    'ICAO ID': 'PABE',
    'NAS ID': 'BET',
    'Area': 'NORTH'
}, {
    'City': 'Big Lake',
    'ICAO ID': 'PAGQ',
    'NAS ID': 'BGQ',
    'Area': 'SOUTH'
}, {
    'City': 'Allen AAF',
    'ICAO ID': 'PABI',
    'NAS ID': 'BIG',
    'Area': 'NORTH'
}, {
    'City': 'Wiley Post-Will Rogers Meml',
    'ICAO ID': 'PABR',
    'NAS ID': 'BRW',
    'Area': 'NORTH'
}, {
    'City': 'Barter Island',
    'ICAO ID': 'PABA',
    'NAS ID': 'BTI',
    'Area': 'NORTH'
}, {
    'City': 'Bettles',
    'ICAO ID': 'PABT',
    'NAS ID': 'BTT',
    'Area': 'NORTH'
}, {
    'City': 'Buckland',
    'ICAO ID': 'PABL',
    'NAS ID': 'BVK',
    'Area': 'NORTH'
}, {
    'City': 'Cold Bay',
    'ICAO ID': 'PACD',
    'NAS ID': 'CDB',
    'Area': 'NORTH'
}, {
    'City': 'Merle K (Mudhole) Smith',
    'ICAO ID': 'PACV',
    'NAS ID': 'CDV',
    'Area': 'SOUTH'
}, {
    'City': 'Central',
    'ICAO ID': 'PACE',
    'NAS ID': 'CEM',
    'Area': 'NORTH'
}, {
    'City': 'Chalkyitsik',
    'ICAO ID': 'PACI',
    'NAS ID': 'CIK',
    'Area': 'NORTH'
}, {
    'City': 'Crooked Creek',
    'ICAO ID': 'PACJ',
    'NAS ID': 'CJX',
    'Area': 'NORTH'
}, {
    'City': 'Clarks Point',
    'ICAO ID': 'PFCL',
    'NAS ID': 'CLP',
    'Area': 'NORTH'
}, {
    'City': 'Coldfoot',
    'ICAO ID': 'PACX',
    'NAS ID': 'CXF',
    'Area': 'NORTH'
}, {
    'City': 'Cape Romanzof LRRS',
    'ICAO ID': 'PACZ',
    'NAS ID': 'CZF',
    'Area': 'NORTH'
}, {
    'City': 'Robert/Bob/Curtis Meml',
    'ICAO ID': 'PFNO',
    'NAS ID': 'D76',
    'Area': 'NORTH'
}, {
    'City': 'Deering',
    'ICAO ID': 'PADE',
    'NAS ID': 'DEE',
    'Area': 'NORTH'
}, {
    'City': 'Dillingham',
    'ICAO ID': 'PADL',
    'NAS ID': 'DLG',
    'Area': 'NORTH'
}, {
    'City': 'Unalaska',
    'ICAO ID': 'PADU',
    'NAS ID': 'DUT',
    'Area': 'NORTH'
}, {
    'City': 'Eagle',
    'ICAO ID': 'PAEG',
    'NAS ID': 'EAA',
    'Area': 'NORTH'
}, {
    'City': 'Elmendorf AFB',
    'ICAO ID': 'PAED',
    'NAS ID': 'EDF',
    'Area': 'SOUTH'
}, {
    'City': 'Eek',
    'ICAO ID': 'PAEE',
    'NAS ID': 'EEK',
    'Area': 'NORTH'
}, {
    'City': 'Cape Newenham LRRS',
    'ICAO ID': 'PAEH',
    'NAS ID': 'EHM',
    'Area': 'NORTH'
}, {
    'City': 'Egegik',
    'ICAO ID': 'PAII',
    'NAS ID': 'EII',
    'Area': 'NORTH'
}, {
    'City': 'EIELSON AFB',
    'ICAO ID': 'PAEI',
    'NAS ID': 'EIL',
    'Area': 'NORTH'
}, {
    'City': 'KENAI MUNI',
    'ICAO ID': 'PAEN',
    'NAS ID': 'ENA',
    'Area': 'SOUTH'
}, {
    'City': 'EMMONAK',
    'ICAO ID': 'PAEM',
    'NAS ID': 'ENM',
    'Area': 'NORTH'
}, {
    'City': 'NENANA MUNI',
    'ICAO ID': 'PANN',
    'NAS ID': 'ENN',
    'Area': 'NORTH'
}, {
    'City': 'FAIRBANKS INTL',
    'ICAO ID': 'PAFA',
    'NAS ID': 'FAI',
    'Area': 'NORTH'
}, {
    'City': 'LADD AAF',
    'ICAO ID': 'PAFB',
    'NAS ID': 'FBK',
    'Area': 'NORTH'
}, {
    'City': 'NIKOLAI',
    'ICAO ID': 'PAFS',
    'NAS ID': 'FSP',
    'Area': 'NORTH'
}, {
    'City': 'FORT YUKON',
    'ICAO ID': 'PFYU',
    'NAS ID': 'FYU',
    'Area': 'NORTH'
}, {
    'City': 'EDWARD G PITKA SR',
    'ICAO ID': 'PAGA',
    'NAS ID': 'GAL',
    'Area': 'NORTH'
}, {
    'City': 'GAMBELL',
    'ICAO ID': 'PAGM',
    'NAS ID': 'GAM',
    'Area': 'NORTH'
}, {
    'City': 'GULKANA',
    'ICAO ID': 'PAGK',
    'NAS ID': 'GKN',
    'Area': 'SOUTH'
}, {
    'City': 'GOLOVIN',
    'ICAO ID': 'PAGL',
    'NAS ID': 'GLV',
    'Area': 'NORTH'
}, {
    'City': 'GUSTAVUS',
    'ICAO ID': 'PAGS',
    'NAS ID': 'GST',
    'Area': 'SOUTH'
}, {
    'City': 'HOLY CROSS',
    'ICAO ID': 'PAHC',
    'NAS ID': 'HCA',
    'Area': 'NORTH'
}, {
    'City': 'HUSLIA',
    'ICAO ID': 'PAHL',
    'NAS ID': 'HLA',
    'Area': 'NORTH'
}, {
    'City': 'HAINES',
    'ICAO ID': 'PAHN',
    'NAS ID': 'HNS',
    'Area': 'SOUTH'
}, {
    'City': 'HOMER',
    'ICAO ID': 'PAHO',
    'NAS ID': 'HOM',
    'Area': 'SOUTH'
}, {
    'City': 'HOOPER BAY',
    'ICAO ID': 'PAHP',
    'NAS ID': 'HPB',
    'Area': 'NORTH'
}, {
    'City': 'HEALY RIVER',
    'ICAO ID': 'PAHV',
    'NAS ID': 'HRR',
    'Area': 'NORTH'
}, {
    'City': 'HUGHES',
    'ICAO ID': 'PAHU',
    'NAS ID': 'HUS',
    'Area': 'NORTH'
}, {
    'City': 'BOB BAKER MEML',
    'ICAO ID': 'PAIK',
    'NAS ID': 'IAN',
    'Area': 'NORTH'
}, {
    'City': 'IGIUGIG',
    'ICAO ID': 'PAIG',
    'NAS ID': 'IGG',
    'Area': 'NORTH'
}, {
    'City': 'KIPNUK',
    'ICAO ID': 'PAKI',
    'NAS ID': 'IIK',
    'Area': 'NORTH'
}, {
    'City': 'ILIAMNA',
    'ICAO ID': 'PAIL',
    'NAS ID': 'ILI',
    'Area': 'SOUTH'
}, {
    'City': 'WALES',
    'ICAO ID': 'PAIW',
    'NAS ID': 'IWK',
    'Area': 'NORTH'
}, {
    'City': 'WASILLA',
    'ICAO ID': 'PAWS',
    'NAS ID': 'IYS',
    'Area': 'SOUTH'
}, {
    'City': 'JUNEAU INTL',
    'ICAO ID': 'PAJN',
    'NAS ID': 'JNU',
    'Area': 'SOUTH'
}, {
    'City': 'KOLIGANEK',
    'ICAO ID': 'PAJZ',
    'NAS ID': 'JZZ',
    'Area': 'NORTH'
}, {
    'City': 'KALTAG',
    'ICAO ID': 'PAKV',
    'NAS ID': 'KAL',
    'Area': 'NORTH'
}, {
    'City': 'GRAYLING',
    'ICAO ID': 'PAGX',
    'NAS ID': 'KGX',
    'Area': 'NORTH'
}, {
    'City': 'KOYUK ALFRED ADAMS',
    'ICAO ID': 'PAKK',
    'NAS ID': 'KKA',
    'Area': 'NORTH'
}, {
    'City': 'KALSKAG',
    'ICAO ID': 'PALG',
    'NAS ID': 'KLG',
    'Area': 'NORTH'
}, {
    'City': 'NEW STUYAHOK',
    'ICAO ID': 'PANW',
    'NAS ID': 'KNW',
    'Area': 'NORTH'
}, {
    'City': 'ST MARY\'S',
    'ICAO ID': 'PASM',
    'NAS ID': 'KSM',
    'Area': 'NORTH'
}, {
    'City': 'KETCHIKAN INTL',
    'ICAO ID': 'PAKT',
    'NAS ID': 'KTN',
    'Area': 'SOUTH'
}, {
    'City': 'BREVIG MISSION',
    'ICAO ID': 'PFKT',
    'NAS ID': 'KTS',
    'Area': 'NORTH'
}, {
    'City': 'KING COVE',
    'ICAO ID': 'PAVC',
    'NAS ID': 'KVC',
    'Area': 'NORTH'
}, {
    'City': 'KIVALINA',
    'ICAO ID': 'PAVL',
    'NAS ID': 'KVL',
    'Area': 'NORTH'
}, {
    'City': 'KWETHLUK',
    'ICAO ID': 'PFKW',
    'NAS ID': 'KWT',
    'Area': 'NORTH'
}, {
    'City': 'KOYUKUK',
    'ICAO ID': 'PFKU',
    'NAS ID': 'KYU',
    'Area': 'NORTH'
}, {
    'City': 'CAPE LISBURNE LRRS',
    'ICAO ID': 'PALU',
    'NAS ID': 'LUR',
    'Area': 'NORTH'
}, {
    'City': 'MANOKOTAK',
    'ICAO ID': 'PAMB',
    'NAS ID': 'MBA',
    'Area': 'NORTH'
}, {
    'City': 'MC GRATH',
    'ICAO ID': 'PAMC',
    'NAS ID': 'MCG',
    'Area': 'NORTH'
}, {
    'City': 'MARSHALL DON HUNTER SR',
    'ICAO ID': 'PADM',
    'NAS ID': 'MDM',
    'Area': 'NORTH'
}, {
    'City': 'MIDDLETON ISLAND',
    'ICAO ID': 'PAMD',
    'NAS ID': 'MDO',
    'Area': 'SOUTH'
}, {
    'City': 'MINCHUMINA',
    'ICAO ID': 'PAMH',
    'NAS ID': 'MHM',
    'Area': 'NORTH'
}, {
    'City': 'MANLEY HOT SPRINGS',
    'ICAO ID': 'PAML',
    'NAS ID': 'MLY',
    'Area': 'NORTH'
}, {
    'City': 'MOUNTAIN VILLAGE',
    'ICAO ID': 'PAMO',
    'NAS ID': 'MOU',
    'Area': 'NORTH'
}, {
    'City': 'MERRILL FLD',
    'ICAO ID': 'PAMR',
    'NAS ID': 'MRI',
    'Area': 'SOUTH'
}, {
    'City': 'MEKORYUK',
    'ICAO ID': 'PAMY',
    'NAS ID': 'MYU',
    'Area': 'NORTH'
}, {
    'City': 'NULATO',
    'ICAO ID': 'PANU',
    'NAS ID': 'NUL',
    'Area': 'NORTH'
}, {
    'City': 'KOBUK',
    'ICAO ID': 'PAOB',
    'NAS ID': 'OBU',
    'Area': 'NORTH'
}, {
    'City': 'NOME',
    'ICAO ID': 'PAOM',
    'NAS ID': 'OME',
    'Area': 'NORTH'
}, {
    'City': 'TOKSOOK BAY',
    'ICAO ID': 'PAOO',
    'NAS ID': 'OOK',
    'Area': 'NORTH'
}, {
    'City': 'NORTHWAY',
    'ICAO ID': 'PAOR',
    'NAS ID': 'ORT',
    'Area': 'SOUTH'
}, {
    'City': 'RALPH WIEN MEML',
    'ICAO ID': 'PAOT',
    'NAS ID': 'OTZ',
    'Area': 'NORTH'
}, {
    'City': 'NELSON LAGOON',
    'ICAO ID': 'PAOU',
    'NAS ID': 'OUL',
    'Area': 'NORTH'
}, {
    'City': 'WARREN "BUD" WOODS PALMER MUNI',
    'ICAO ID': 'PAAQ',
    'NAS ID': 'PAQ',
    'Area': 'SOUTH'
}, {
    'City': 'ST GEORGE',
    'ICAO ID': 'PAPB',
    'NAS ID': 'PBV',
    'Area': 'ATOP'
}, {
    'City': 'PERRYVILLE',
    'ICAO ID': 'PAPE',
    'NAS ID': 'PEV',
    'Area': 'NORTH'
}, {
    'City': 'POINT HOPE',
    'ICAO ID': 'PAPO',
    'NAS ID': 'PHO',
    'Area': 'NORTH'
}, {
    'City': 'POINT LAY LRRS',
    'ICAO ID': 'PPIZ',
    'NAS ID': 'PIZ',
    'Area': 'NORTH'
}, {
    'City': 'NAPASKIAK',
    'ICAO ID': 'PAPK',
    'NAS ID': 'PKA',
    'Area': 'NORTH'
}, {
    'City': 'PILOT POINT',
    'ICAO ID': 'PAPN',
    'NAS ID': 'PNP',
    'Area': 'NORTH'
}, {
    'City': 'PETERSBURG JAMES A JOHNSON',
    'ICAO ID': 'PAPG',
    'NAS ID': 'PSG',
    'Area': 'SOUTH'
}, {
    'City': 'PORT HEIDEN',
    'ICAO ID': 'PAPH',
    'NAS ID': 'PTH',
    'Area': 'NORTH'
}, {
    'City': 'PLATINUM',
    'ICAO ID': 'PAPM',
    'NAS ID': 'PTU',
    'Area': 'NORTH'
}, {
    'City': 'RUBY',
    'ICAO ID': 'PARY',
    'NAS ID': 'RBY',
    'Area': 'NORTH'
}, {
    'City': 'RUSSIAN MISSION',
    'ICAO ID': 'PARS',
    'NAS ID': 'RSH',
    'Area': 'NORTH'
}, {
    'City': 'DEADHORSE',
    'ICAO ID': 'PASC',
    'NAS ID': 'SCC',
    'Area': 'NORTH'
}, {
    'City': 'SCAMMON BAY',
    'ICAO ID': 'PACM',
    'NAS ID': 'SCM',
    'Area': 'NORTH'
}, {
    'City': 'SAND POINT',
    'ICAO ID': 'PASD',
    'NAS ID': 'SDP',
    'Area': 'NORTH'
}, {
    'City': 'SHUNGNAK',
    'ICAO ID': 'PAGH',
    'NAS ID': 'SHG',
    'Area': 'NORTH'
}, {
    'City': 'SHISHMAREF',
    'ICAO ID': 'PASH',
    'NAS ID': 'SHH',
    'Area': 'NORTH'
}, {
    'City': 'SHAGELUK',
    'ICAO ID': 'PAHX',
    'NAS ID': 'SHX',
    'Area': 'NORTH'
}, {
    'City': 'SITKA ROCKY GUTIERREZ',
    'ICAO ID': 'PASI',
    'NAS ID': 'SIT',
    'Area': 'SOUTH'
}, {
    'City': 'SLEETMUTE',
    'ICAO ID': 'PASL',
    'NAS ID': 'SLQ',
    'Area': 'NORTH'
}, {
    'City': 'ST MICHAEL',
    'ICAO ID': 'PAMK',
    'NAS ID': 'SMK',
    'Area': 'NORTH'
}, {
    'City': 'ST PAUL ISLAND',
    'ICAO ID': 'PASN',
    'NAS ID': 'SNP',
    'Area': 'ATOP'
}, {
    'City': 'SAVOONGA',
    'ICAO ID': 'PASA',
    'NAS ID': 'SVA',
    'Area': 'NORTH'
}, {
    'City': 'SPARREVOHN LRRS',
    'ICAO ID': 'PASV',
    'NAS ID': 'SVW',
    'Area': 'SOUTH'
}, {
    'City': 'SEWARD',
    'ICAO ID': 'PAWD',
    'NAS ID': 'SWD',
    'Area': 'SOUTH'
}, {
    'City': 'SOLDOTNA',
    'ICAO ID': 'PASX',
    'NAS ID': 'SXQ',
    'Area': 'SOUTH'
}, {
    'City': 'EARECKSON AS',
    'ICAO ID': 'PASY',
    'NAS ID': 'SYA',
    'Area': 'ATOP'
}, {
    'City': 'RALPH M CALHOUN MEML',
    'ICAO ID': 'PATA',
    'NAS ID': 'TAL',
    'Area': 'NORTH'
}, {
    'City': 'TELLER',
    'ICAO ID': 'PATE',
    'NAS ID': 'TER',
    'Area': 'NORTH'
}, {
    'City': 'TALKEETNA',
    'ICAO ID': 'PATK',
    'NAS ID': 'TKA',
    'Area': 'SOUTH'
}, {
    'City': 'TATALINA LRRS',
    'ICAO ID': 'PATL',
    'NAS ID': 'TLJ',
    'Area': 'NORTH'
}, {
    'City': 'TIN CITY LRRS',
    'ICAO ID': 'PATC',
    'NAS ID': 'TNC',
    'Area': 'NORTH'
}, {
    'City': 'TOGIAK',
    'ICAO ID': 'PATG',
    'NAS ID': 'TOG',
    'Area': 'NORTH'
}, {
    'City': 'UGNU-KUPARUK',
    'ICAO ID': 'PAKU',
    'NAS ID': 'UBW',
    'Area': 'NORTH'
}, {
    'City': 'UNALAKLEET',
    'ICAO ID': 'PAUN',
    'NAS ID': 'UNK',
    'Area': 'NORTH'
}, {
    'City': 'INDIAN MOUNTAIN LRRS',
    'ICAO ID': 'PAIM',
    'NAS ID': 'UTO',
    'Area': 'NORTH'
}, {
    'City': 'CHEVAK',
    'ICAO ID': 'PAVA',
    'NAS ID': 'VAK',
    'Area': 'NORTH'
}, {
    'City': 'VALDEZ PIONEER FLD',
    'ICAO ID': 'PAVD',
    'NAS ID': 'VDZ',
    'Area': 'SOUTH'
}, {
    'City': 'VENETIE',
    'ICAO ID': 'PAVE',
    'NAS ID': 'VEE',
    'Area': 'NORTH'
}, {
    'City': 'BEAVER',
    'ICAO ID': 'PAWB',
    'NAS ID': 'WBQ',
    'Area': 'NORTH'
}, {
    'City': 'SELAWIK',
    'ICAO ID': 'PASK',
    'NAS ID': 'WLK',
    'Area': 'NORTH'
}, {
    'City': 'WHITE MOUNTAIN',
    'ICAO ID': 'PAWM',
    'NAS ID': 'WMO',
    'Area': 'NORTH'
}, {
    'City': 'NAPAKIAK',
    'ICAO ID': 'PANA',
    'NAS ID': 'WNA',
    'Area': 'NORTH'
}, {
    'City': 'WRANGELL',
    'ICAO ID': 'PAWG',
    'NAS ID': 'WRG',
    'Area': 'SOUTH'
}, {
    'City': 'SOUTH NAKNEK NR 2',
    'ICAO ID': 'PFWS',
    'NAS ID': 'WSN',
    'Area': 'NORTH'
}, {
    'City': 'NOATAK',
    'ICAO ID': 'PAWN',
    'NAS ID': 'WTK',
    'Area': 'NORTH'
}, {
    'City': 'YAKUTAT',
    'ICAO ID': 'PAYA',
    'NAS ID': 'YAK',
    'Area': 'SOUTH'
}]

pirep_config = {
    "MinLat": 50,
    "MaxLat": 72,
    "MinLon": -179,
    "MaxLon": -130,
    "hoursBeforeNow": 1.5,
    "url_template": "https://aviationweather.gov/api/data/dataserver?requestType=retrieve&dataSource=aircraftreports&hoursBeforeNow={hours}&format=csv&boundingBox={minlat},{minlon},{maxlat},{maxlon}"
}
def get_pirep_url():
    return pirep_config["url_template"].format(
        hours=pirep_config["hoursBeforeNow"],
        minlat=pirep_config["MinLat"],
        maxlat=pirep_config["MaxLat"],
        minlon=pirep_config["MinLon"],
        maxlon=pirep_config["MaxLon"]
    )

pasy_url = "https://aviationweather.gov/api/data/dataserver?requestType=retrieve&dataSource=aircraftreports&hoursBeforeNow=1&format=csv&boundingBox=45%2C%20159%2C%2055%2C%20179"

areas = {
    "NORTH": {
        "sectors": {
            3: [
                (66.120, -157.000),
                (66.000, -163.000),
                (66.630, -164.830),
                (66.450, -168.970),
                (65.000, -168.970),
                (64.050, -172.200),
                (62.960, -174.580),
                (62.670, -170.750),
                (60.590, -168.360),
                (61.870, -166.440),
                (62.450, -163.250),
                (61.620, -158.230),
                (61.390, -156.460),
                (61.380, -156.420),
                (61.390, -156.000),
                (61.420, -153.500),
                (63.000, -153.080),
                (63.170, -152.720),
                (64.730, -154.330),
                (65.680, -154.110)
            ],
            4: [
                (67.34,	-141.09),
                (72.01,	-141.09),
                (72.07,	-157.96),
                (68.03,	-169.00),
                (66.45,	-168.97),
                (66.64,	-164.83),
                (65.99,	-163.01),
                (66.12,	-156.98),
                (65.69,	-154.11),
                (66.14,	-153.97),

            ],
            9:[
                (59.162, -152.291),
                (59.500, -155.333),
                (59.900, -156.417),
                (59.500, -158.000),
                (59.133, -159.500),
                (56.967, -162.500),
                (56.967, -165.000),
                (55.000, -167.000),
                (54.217, -167.744),
                (53.465, -167.337),
                (52.600, -163.679),
                (53.500, -160.000),
                (56.000, -153.000),
                (56.762, -151.750),
                (57.464, -150.531),
                (59.183, -150.000)
            ],
            13:[
                (61.621, -158.233),
                (62.450, -163.250),
                (61.870, -166.440),
                (60.588, -168.364),
                (59.331, -167.914),
                (58.740, -167.713),
                (56.967, -165.000),
                (56.967, -162.500),
                (59.133, -159.500),
                (59.500, -158.000),
                (59.900, -156.417),
                (61.390, -156.462)
                
            ],
            15:[
                (62.96,	-148.57),
                (63.96,	-148.00),
                (64.38,	-147.96),
                (64.43,	-147.86),
                (64.75,	-147.63),
                (65.00,	-147.29),
                (65.25,	-147.19),
                (65.67,	-146.29),
                (66.00,	-145.85),
                (66.00,	-145.25),
                (66.67,	-144.50),
                (66.67,	-141.00),
                (67.34,	-141.00),
                (66.12,	-154.00),
                (64.73,	-154.33),
                (63.17,	-152.71)
            ],
            16:[
                (63.33,	-141.00),
                (66.67,	-141.00),
                (66.67,	-144.50),
                (66.00,	-145.25),
                (66.00,	-145.85),
                (65.67,	-146.29),
                (65.25,	-147.19),
                (65.00,	-147.29),
                (64.75,	-147.63),
                (64.43,	-147.86),
                (64.38,	-147.96),
                (63.96,	-148.00),
                (62.96,	-148.57),
                (62.84,	-146.58)
            ]
            # Add other sectors (9, 13, 15, 16) and their polygons
        }
    },
    "SOUTH": {
        "sectors": {
            5:[
                (59.19,	-150.00),
                (60.50,	-150.00),
                (60.88,	-150.17),
                (61.09,	-151.08),
                (61.09,	-151.77),
                (61.24,	-152.11),
                (61.24,	-152.78),
                (61.42,	-152.81),
                (61.87,	-156.48),
                (59.90,	-156.41),
                (59.50,	-155.34),
                (59.16,	-152.30),

            ],
            6:[
                (60.87,	-150.14),
                (61.47,	-149.07),
                (61.74,	-147.41),
                (62.84,	-146.58),
                (63.17,	-152.72),
                (63.00,	-153.09),
                (62.42,	-153.50),
                (61.72,	-155.21),
                (61.42,	-152.80),
                (61.24,	-152.79),
                (61.23,	-152.12),
                (61.09,	-151.76),
                (61.09,	-151.07)
            ],
            7: [
                (59.20,	-150.00),
                (59.02,	-146.00),
                (59.50,	-141.12),
                (60.54,	-141.32),
                (60.35,	-139.20),
                (62.00,	-141.02),
                (63.35,	-141.02),
                (62.85,	-146.58),
                (61.75,	-147.42),
                (61.47,	-149.08),
                (60.88,	-150.16),
                (60.52,	-150.00)

            ],
            8: [
                (59.48,	-142.11),
                (57.97,	-137.76),
                (54.45,	-133.27),
                (54.59,	-132.80),
                (54.48,	-131.79),
                (55.29,	-130.01),
                (56.14,	-130.13),
                (57.22,	-132.24),
                (59.81,	-135.50),
                (58.94,	-137.46),
                (60.07,	-139.18),
                (60.35,	-139.18),
                (60.53,	-141.35),

            ]
        },
    },
    "HIGH": {
        "sectors":{
            63: [
                (65.682, -154.108),
                (66.117, -157.000),
                (66.000, -163.000),
                (66.633, -164.833),
                (66.450, -168.973),
                (65.000, -168.973),
                (64.050, -172.200),
                (62.958, -174.583),
                (62.670, -170.753),
                (60.588, -168.364),
                (59.331, -167.914),
                (59.787, -164.683),
                (60.250, -160.613),
                (60.588, -156.437),
                (61.869, -156.477),
                (61.725, -155.216),
                (62.417, -153.500),
                (63.000, -153.083),
                (63.167, -152.717),
                (64.733, -154.333)

            ],
            68: [
                (56.76, -151.79),
                (53.39, -137.02),
                (54.72, -130.63),
                (56.12, -130.11),
                (57.03, -132.07),
                (56.64, -133.06),
                (56.95, -135.00),
                (58.01, -137.85),
                (59.50, -142.12),
                (59.01, -146.00),
                (59.19, -150.01),
                (57.48, -150.52)

            ],
            69: [
                (59.183, -150.000),
                (59.162, -152.291),
                (59.500, -155.333),
                (59.900, -156.417),
                (60.588, -156.437),
                (60.250, -160.613),
                (59.787, -164.683),
                (59.331, -167.914),
                (58.740, -167.713),
                (58.247, -166.925),
                (58.061, -163.394),
                (57.833, -160.436),
                (57.789, -159.949),
                (57.313, -155.602),
                (56.762, -151.750),
                (57.464, -150.531)
            ]
        }
    },
    "ATOP": {
        "sectors": {
            10:[
                (45.72, -197.10),
                (49.71, -179.95),
                (50.13, -176.62),
                (51.44, -167.88),
                (53.50, -160.09),
                (56.76, -151.74),
                (58.24, -166.90),
                (58.75, -167.71),
                (58.61, -174.88),
                (58.83, -182.37),
                (54.61, -190.01),
                (50.07, -201.02)

            ],
            11:[
                (58.83, -182.37),
                (58.61, -174.88),
                (58.75, -167.71),
                (59.35, -167.90),
                (60.57, -168.37),
                (62.67, -170.75),
                (62.98, -174.56)

            ]
            
        }
    },
    # Define other areas like ATOP, HIGH
}


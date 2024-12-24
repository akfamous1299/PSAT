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
        'City': 'KOTLIK',
        'ICAO ID': 'PFKO',
        'NAS ID': '2A9',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'SHAKTOOLIK',
        'ICAO ID': 'PFSH',
        'NAS ID': '2C7',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'NONDALTON',
        'ICAO ID': 'PANO',
        'NAS ID': '5NN',
        'Area': 'SOUTH',
        'Sector': 5
    },
    {
        'City': 'ALLAKAKET',
        'ICAO ID': 'PFAL',
        'NAS ID': '6A8',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'AKUTAN',
        'ICAO ID': 'PAUT',
        'NAS ID': '7AK',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'TATITLEK',
        'ICAO ID': 'PAKA',
        'NAS ID': '7KA',
        'Area': 'SOUTH',
        'Sector': 7
    },
    {
        'City': 'CHUATHBALUK',
        'ICAO ID': 'PACH',
        'NAS ID': '9A3',
        'Area': 'NORTH',
        'Sector': 13
    },
    {
        'City': 'ADAK',
        'ICAO ID': 'PADK',
        'NAS ID': 'ADK',
        'Area': 'ATOP',
        'Sector': 11
    },
    {
        'City': 'KODIAK',
        'ICAO ID': 'PADQ',
        'NAS ID': 'ADQ',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'KAKE',
        'ICAO ID': 'PAFE',
        'NAS ID': 'AFE',
        'Area': 'SOUTH',
        'Sector': 8
    },
    {
        'City': 'AMBLER',
        'ICAO ID': 'PAFM',
        'NAS ID': 'AFM',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'BADAMI',
        'ICAO ID': 'PABP',
        'NAS ID': 'AK78',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'ATKA',
        'ICAO ID': 'PAAK',
        'NAS ID': 'AKA',
        'Area': 'ATOP',
        'Sector': 11
    },
    {
        'City': 'AKIAK',
        'ICAO ID': 'PFAK',
        'NAS ID': 'AKI',
        'Area': 'NORTH',
        'Sector': 13
    },
    {
        'City': 'AKHIOK',
        'ICAO ID': 'PAKH',
        'NAS ID': 'AKK',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'KING SALMON',
        'ICAO ID': 'PAKN',
        'NAS ID': 'AKN',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'ANAKTUVUK PASS',
        'ICAO ID': 'PAKP',
        'NAS ID': 'AKP',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'KLAWOCK',
        'ICAO ID': 'PAKW',
        'NAS ID': 'AKW',
        'Area': 'SOUTH',
        'Sector': 8
    },
    {
        'City': 'TED STEVENS ANCHORAGE INTL',
        'ICAO ID': 'PANC',
        'NAS ID': 'ANC',
        'Area': 'SOUTH',
        'Sector': 6
    },
    {
        'City': 'ANIAK',
        'ICAO ID': 'PANI',
        'NAS ID': 'ANI',
        'Area': 'NORTH',
        'Sector': 13
    },
    {
        'City': 'ANVIK',
        'ICAO ID': 'PANV',
        'NAS ID': 'ANV',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'QUINHAGAK',
        'ICAO ID': 'PAQH',
        'NAS ID': 'ENM',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'NUIQSUT',
        'ICAO ID': 'PAQT',
        'NAS ID': 'AQT',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'ARCTIC VILLAGE',
        'ICAO ID': 'PARC',
        'NAS ID': 'ARC',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'ATQASUK EDWARD BURNELL SR MEML',
        'ICAO ID': 'PATQ',
        'NAS ID': 'ATK',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'WAINWRIGHT',
        'ICAO ID': 'PAWI',
        'NAS ID': 'AWI',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'BETHEL',
        'ICAO ID': 'PABE',
        'NAS ID': 'BET',
        'Area': 'NORTH',
        'Sector': 13
    },
    {
        'City': 'BIG LAKE',
        'ICAO ID': 'PAGQ',
        'NAS ID': 'BGQ',
        'Area': 'SOUTH',
        'Sector': 6
    },
    {
        'City': 'ALLEN AAF',
        'ICAO ID': 'PABI',
        'NAS ID': 'BIG',
        'Area': 'NORTH',
        'Sector': 16
    },
    {
        'City': 'WILEY POST-WILL ROGERS MEML',
        'ICAO ID': 'PABR',
        'NAS ID': 'BRW',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'BARTER ISLAND',
        'ICAO ID': 'PABA',
        'NAS ID': 'BTI',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'BETTLES',
        'ICAO ID': 'PABT',
        'NAS ID': 'BTT',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'BUCKLAND',
        'ICAO ID': 'PABL',
        'NAS ID': 'BVK',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'COLD BAY',
        'ICAO ID': 'PACD',
        'NAS ID': 'CDB',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'MERLE K (MUDHOLE) SMITH',
        'ICAO ID': 'PACV',
        'NAS ID': 'CDV',
        'Area': 'SOUTH',
        'Sector': 7
    },
    {
        'City': 'CENTRAL',
        'ICAO ID': 'PACE',
        'NAS ID': 'CEM',
        'Area': 'NORTH',
        'Sector': 16
    },
    {
        'City': 'CHALKYITSIK',
        'ICAO ID': 'PACI',
        'NAS ID': 'CIK',
        'Area': 'NORTH',
        'Sector': 16
    },
    {
        'City': 'CROOKED CREEK',
        'ICAO ID': 'PACJ',
        'NAS ID': 'CJX',
        'Area': 'NORTH',
        'Sector': 13
    },
    {
        'City': 'CLARKS POINT',
        'ICAO ID': 'PFCL',
        'NAS ID': 'CLP',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'COLDFOOT',
        'ICAO ID': 'PACX',
        'NAS ID': 'CXF',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'CAPE ROMANZOF LRRS',
        'ICAO ID': 'PACZ',
        'NAS ID': 'CZF',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'ROBERT/BOB/CURTIS MEML',
        'ICAO ID': 'PFNO',
        'NAS ID': 'D76',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'DEERING',
        'ICAO ID': 'PADE',
        'NAS ID': 'DEE',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'DILLINGHAM',
        'ICAO ID': 'PADL',
        'NAS ID': 'DLG',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'UNALASKA',
        'ICAO ID': 'PADU',
        'NAS ID': 'DUT',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'EAGLE',
        'ICAO ID': 'PAEG',
        'NAS ID': 'EAA',
        'Area': 'NORTH',
        'Sector': 16
    },
    {
        'City': 'ELMENDORF AFB',
        'ICAO ID': 'PAED',
        'NAS ID': 'EDF',
        'Area': 'SOUTH',
        'Sector': 6
    },
    {
        'City': 'EEK',
        'ICAO ID': 'PAEE',
        'NAS ID': 'EEK',
        'Area': 'NORTH',
        'Sector': 13
    },
    {
        'City': 'CAPE NEWENHAM LRRS',
        'ICAO ID': 'PAEH',
        'NAS ID': 'EHM',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'EGEGIK',
        'ICAO ID': 'PAII',
        'NAS ID': 'EII',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'EIELSON AFB',
        'ICAO ID': 'PAEI',
        'NAS ID': 'EIL',
        'Area': 'NORTH',
        'Sector': 16
    },
    {
        'City': 'KENAI MUNI',
        'ICAO ID': 'PAEN',
        'NAS ID': 'ENA',
        'Area': 'SOUTH',
        'Sector': 5
    },
    {
        'City': 'EMMONAK',
        'ICAO ID': 'PAEM',
        'NAS ID': 'ENM',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'NENANA MUNI',
        'ICAO ID': 'PANN',
        'NAS ID': 'ENN',
        'Area': 'NORTH',
        'Sector': 15
    },
    {
        'City': 'FAIRBANKS INTL',
        'ICAO ID': 'PAFA',
        'NAS ID': 'FAI',
        'Area': 'NORTH',
        'Sector': 15
    },
    {
        'City': 'LADD AAF',
        'ICAO ID': 'PAFB',
        'NAS ID': 'FBK',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'NIKOLAI',
        'ICAO ID': 'PAFS',
        'NAS ID': 'FSP',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'FORT YUKON',
        'ICAO ID': 'PFYU',
        'NAS ID': 'FYU',
        'Area': 'NORTH',
        'Sector': 15
    },
    {
        'City': 'EDWARD G PITKA SR',
        'ICAO ID': 'PAGA',
        'NAS ID': 'GAL',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'GAMBELL',
        'ICAO ID': 'PAGM',
        'NAS ID': 'GAM',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'GULKANA',
        'ICAO ID': 'PAGK',
        'NAS ID': 'GKN',
        'Area': 'SOUTH',
        'Sector': 7
    },
    {
        'City': 'GOLOVIN',
        'ICAO ID': 'PAGL',
        'NAS ID': 'GLV',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'GUSTAVUS',
        'ICAO ID': 'PAGS',
        'NAS ID': 'GST',
        'Area': 'SOUTH',
        'Sector': 8
    },
    {
        'City': 'HOLY CROSS',
        'ICAO ID': 'PAHC',
        'NAS ID': 'HCA',
        'Area': 'NORTH',
        'Sector': 13
    },
    {
        'City': 'HUSLIA',
        'ICAO ID': 'PAHL',
        'NAS ID': 'HLA',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'HAINES',
        'ICAO ID': 'PAHN',
        'NAS ID': 'HNS',
        'Area': 'SOUTH',
        'Sector': 8
    },
    {
        'City': 'HOMER',
        'ICAO ID': 'PAHO',
        'NAS ID': 'HOM',
        'Area': 'SOUTH',
        'Sector': 5
    },
    {
        'City': 'HOOPER BAY',
        'ICAO ID': 'PAHP',
        'NAS ID': 'HPB',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'HEALY RIVER',
        'ICAO ID': 'PAHV',
        'NAS ID': 'HRR',
        'Area': 'NORTH',
        'Sector': 15
    },
    {
        'City': 'HUGHES',
        'ICAO ID': 'PAHU',
        'NAS ID': 'HUS',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'BOB BAKER MEML',
        'ICAO ID': 'PAIK',
        'NAS ID': 'IAN',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'IGIUGIG',
        'ICAO ID': 'PAIG',
        'NAS ID': 'IGG',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'KIPNUK',
        'ICAO ID': 'PAKI',
        'NAS ID': 'IIK',
        'Area': 'NORTH',
        'Sector': 13
    },
    {
        'City': 'ILIAMNA',
        'ICAO ID': 'PAIL',
        'NAS ID': 'ILI',
        'Area': 'SOUTH',
        'Sector': 5
    },
    {
        'City': 'WALES',
        'ICAO ID': 'PAIW',
        'NAS ID': 'IWK',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'WASILLA',
        'ICAO ID': 'PAWS',
        'NAS ID': 'IYS',
        'Area': 'SOUTH',
        'Sector': 6
    },
    {
        'City': 'JUNEAU INTL',
        'ICAO ID': 'PAJN',
        'NAS ID': 'JNU',
        'Area': 'SOUTH',
        'Sector': 8
    },
    {
        'City': 'KOLIGANEK',
        'ICAO ID': 'PAJZ',
        'NAS ID': 'JZZ',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'KALTAG',
        'ICAO ID': 'PAKV',
        'NAS ID': 'KAL',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'GRAYLING',
        'ICAO ID': 'PAGX',
        'NAS ID': 'KGX',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'KOYUK ALFRED ADAMS',
        'ICAO ID': 'PAKK',
        'NAS ID': 'KKA',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'KALSKAG',
        'ICAO ID': 'PALG',
        'NAS ID': 'KLG',
        'Area': 'NORTH',
        'Sector': 13
    },
    {
        'City': 'NEW STUYAHOK',
        'ICAO ID': 'PANW',
        'NAS ID': 'KNW',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'ST MARYS',
        'ICAO ID': 'PASM',
        'NAS ID': 'KSM',
        'Area': 'NORTH',
        'Sector': 13
    },
    {
        'City': 'KETCHIKAN INTL',
        'ICAO ID': 'PAKT',
        'NAS ID': 'KTN',
        'Area': 'SOUTH',
        'Sector': 8
    },
    {
        'City': 'BREVIG MISSION',
        'ICAO ID': 'PFKT',
        'NAS ID': 'KTS',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'KING COVE',
        'ICAO ID': 'PAVC',
        'NAS ID': 'KVC',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'KIVALINA',
        'ICAO ID': 'PAVL',
        'NAS ID': 'KVL',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'KWETHLUK',
        'ICAO ID': 'PFKW',
        'NAS ID': 'KWT',
        'Area': 'NORTH',
        'Sector': 13
    },
    {
        'City': 'KOYUKUK',
        'ICAO ID': 'PFKU',
        'NAS ID': 'KYU',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'CAPE LISBURNE LRRS',
        'ICAO ID': 'PALU',
        'NAS ID': 'LUR',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'MANOKOTAK',
        'ICAO ID': 'PAMB',
        'NAS ID': 'MBA',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'MC GRATH',
        'ICAO ID': 'PAMC',
        'NAS ID': 'MCG',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'MARSHALL DON HUNTER SR',
        'ICAO ID': 'PAMD',
        'NAS ID': 'MDM',
        'Area': 'NORTH',
        'Sector': 13
    },
    {
        'City': 'MIDDLETON ISLAND',
        'ICAO ID': 'PAMD',
        'NAS ID': 'MDO',
        'Area': 'SOUTH',
        'Sector': 7
    },
    {
        'City': 'MINCHUMINA',
        'ICAO ID': 'PAMH',
        'NAS ID': 'MHM',
        'Area': 'NORTH',
        'Sector': 15
    },
    {
        'City': 'MANLEY HOT SPRINGS',
        'ICAO ID': 'PAML',
        'NAS ID': 'MLY',
        'Area': 'NORTH',
        'Sector': 15
    },
    {
        'City': 'MOUNTAIN VILLAGE',
        'ICAO ID': 'PAMO',
        'NAS ID': 'MOU',
        'Area': 'NORTH',
        'Sector': 13
    },
    {
        'City': 'MERRILL FLD',
        'ICAO ID': 'PAMR',
        'NAS ID': 'MRI',
        'Area': 'SOUTH',
        'Sector': 6
    },
    {
        'City': 'MEKORYUK',
        'ICAO ID': 'PAMY',
        'NAS ID': 'MYU',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'NULATO',
        'ICAO ID': 'PANU',
        'NAS ID': 'NUL',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'KOBUK',
        'ICAO ID': 'PAOB',
        'NAS ID': 'OBU',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'NOME',
        'ICAO ID': 'PAOM',
        'NAS ID': 'OME',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'TOKSOOK BAY',
        'ICAO ID': 'PAOO',
        'NAS ID': 'OOK',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'NORTHWAY',
        'ICAO ID': 'PAOR',
        'NAS ID': 'ORT',
        'Area': 'SOUTH',
        'Sector': 7
    },
    {
        'City': 'RALPH WIEN MEML',
        'ICAO ID': 'PAOT',
        'NAS ID': 'OTZ',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'NELSON LAGOON',
        'ICAO ID': 'PAOU',
        'NAS ID': 'OUL',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'PALMER',
        'ICAO ID': 'PAAQ',
        'NAS ID': 'PAQ',
        'Area': 'SOUTH',
        'Sector': 6
    },
    {
        'City': 'ST GEORGE',
        'ICAO ID': 'PAPB',
        'NAS ID': 'PBV',
        'Area': 'ATOP',
        'Sector': 11
    },
    {
        'City': 'PERRYVILLE',
        'ICAO ID': 'PAPE',
        'NAS ID': 'PEV',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'POINT HOPE',
        'ICAO ID': 'PAPO',
        'NAS ID': 'PHO',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'POINT LAY LRRS',
        'ICAO ID': 'PPIZ',
        'NAS ID': 'PIZ',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'NAPASKIAK',
        'ICAO ID': 'PAPK',
        'NAS ID': 'PKA',
        'Area': 'NORTH',
        'Sector': 13
    },
    {
        'City': 'PILOT POINT',
        'ICAO ID': 'PAPN',
        'NAS ID': 'PNP',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'PETERSBURG JAMES A JOHNSON',
        'ICAO ID': 'PAPG',
        'NAS ID': 'PSG',
        'Area': 'SOUTH',
        'Sector': 8
    },
    {
        'City': 'PORT HEIDEN',
        'ICAO ID': 'PAPH',
        'NAS ID': 'PTH',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'PLATINUM',
        'ICAO ID': 'PAPM',
        'NAS ID': 'PTU',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'RUBY',
        'ICAO ID': 'PARY',
        'NAS ID': 'RBY',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'RUSSIAN MISSION',
        'ICAO ID': 'PARS',
        'NAS ID': 'RSH',
        'Area': 'NORTH',
        'Sector': 13
    },
    {
        'City': 'DEADHORSE',
        'ICAO ID': 'PASC',
        'NAS ID': 'SCC',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'SCAMMON BAY',
        'ICAO ID': 'PACM',
        'NAS ID': 'SCM',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'SAND POINT',
        'ICAO ID': 'PASD',
        'NAS ID': 'SDP',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'SHUNGNAK',
        'ICAO ID': 'PAGH',
        'NAS ID': 'SHG',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'SHISHMAREF',
        'ICAO ID': 'PASH',
        'NAS ID': 'SHH',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'SHAGELUK',
        'ICAO ID': 'PAHX',
        'NAS ID': 'SHX',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'SITKA ROCKY GUTIERREZ',
        'ICAO ID': 'PASI',
        'NAS ID': 'SIT',
        'Area': 'SOUTH',
        'Sector': 8
    },
    {
        'City': 'SLEETMUTE',
        'ICAO ID': 'PASL',
        'NAS ID': 'SLQ',
        'Area': 'NORTH',
        'Sector': 13
    },
    {
        'City': 'ST MICHAEL',
        'ICAO ID': 'PAMK',
        'NAS ID': 'SMK',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'ST PAUL ISLAND',
        'ICAO ID': 'PASN',
        'NAS ID': 'SNP',
        'Area': 'ATOP',
        'Sector': 11
    },
    {
        'City': 'SAVOONGA',
        'ICAO ID': 'PASA',
        'NAS ID': 'SVA',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'SPARREVOHN LRRS',
        'ICAO ID': 'PASV',
        'NAS ID': 'SVW',
        'Area': 'SOUTH',
        'Sector': 5
    },
    {
        'City': 'SEWARD',
        'ICAO ID': 'PAWD',
        'NAS ID': 'SWD',
        'Area': 'SOUTH',
        'Sector': 7
    },
    {
        'City': 'SOLDOTNA',
        'ICAO ID': 'PASX',
        'NAS ID': 'SXQ',
        'Area': 'SOUTH',
        'Sector': 5
    },
    {
        'City': 'EARECKSON AS',
        'ICAO ID': 'PASY',
        'NAS ID': 'SYA',
        'Area': 'ATOP',
        'Sector': 11
    },
    {
        'City': 'RALPH M CALHOUN MEML',
        'ICAO ID': 'PATA',
        'NAS ID': 'TAL',
        'Area': 'NORTH',
        'Sector': 15
    },
    {
        'City': 'TELLER',
        'ICAO ID': 'PATE',
        'NAS ID': 'TER',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'TALKEETNA',
        'ICAO ID': 'PATK',
        'NAS ID': 'TKA',
        'Area': 'SOUTH',
        'Sector': 6
    },
    {
        'City': 'TATALINA',
        'ICAO ID': 'PATL',
        'NAS ID': 'TLJ',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'TIN CITY LRRS',
        'ICAO ID': 'PATC',
        'NAS ID': 'TNC',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'TOGIAK',
        'ICAO ID': 'PATG',
        'NAS ID': 'TOG',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'UGNU-KUPARUK',
        'ICAO ID': 'PAKU',
        'NAS ID': 'UBW',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'UNALAKLEET',
        'ICAO ID': 'PAUN',
        'NAS ID': 'UNK',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'INDIAN MOUNTAIN LRRS',
        'ICAO ID': 'PAIM',
        'NAS ID': 'UTO',
        'Area': 'NORTH',
        'Sector': 15
    },
    {
        'City': 'CHEVAK',
        'ICAO ID': 'PAVA',
        'NAS ID': 'VAK',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'VALDEZ PIONEER FLD',
        'ICAO ID': 'PAVD',
        'NAS ID': 'VDZ',
        'Area': 'SOUTH',
        'Sector': 7
    },
    {
        'City': 'VENETIE',
        'ICAO ID': 'PAVE',
        'NAS ID': 'VEE',
        'Area': 'NORTH',
        'Sector': 4
    }, {
        'City': 'BEAVER',
        'ICAO ID': 'PAWB',
        'NAS ID': 'WBQ',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'WHITTIER',
        'ICAO ID': 'PAWR',
        'NAS ID': 'WTR',
        'Area': 'SOUTH',
        'Sector': 6
    },
    {
        'City': 'SELAWIK',
        'ICAO ID': 'PASK',
        'NAS ID': 'WLK',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'WHITE MOUNTAIN',
        'ICAO ID': 'PAWM',
        'NAS ID': 'WMO',
        'Area': 'NORTH',
        'Sector': 3
    },
    {
        'City': 'NAPAKIAK',
        'ICAO ID': 'PANA',
        'NAS ID': 'WNA',
        'Area': 'NORTH',
        'Sector': 13
    },
    {
        'City': 'WRANGELL',
        'ICAO ID': 'PAWG',
        'NAS ID': 'WRG',
        'Area': 'SOUTH',
        'Sector': 8
    },
    {
        'City': 'SOUTH NAKNEK NR 2',
        'ICAO ID': 'PFWS',
        'NAS ID': 'WSN',
        'Area': 'NORTH',
        'Sector': 9
    },
    {
        'City': 'NOATAK',
        'ICAO ID': 'PAWN',
        'NAS ID': 'WTK',
        'Area': 'NORTH',
        'Sector': 4
    },
    {
        'City': 'YAKUTAT',
        'ICAO ID': 'PAYA',
        'NAS ID': 'YAK',
        'Area': 'SOUTH',
        'Sector': 8
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


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
airport_data = [
#    {
#        'City': 'KOTLIK',
#        'ICAO ID': 'PFKO',
#        'NAS ID': '2A9',
#        'Area': 'NORTH',
#        'Sector': 3
#    },
#    {
#        'City': 'SHAKTOOLIK',
#        'ICAO ID': 'PFSH',
#        'NAS ID': '2C7',
#        'Area': 'NORTH',
#        'Sector': 3
#    },
#    {
#        'City': 'NONDALTON',
#        'ICAO ID': 'PANO',
#        'NAS ID': '5NN',
#        'Area': 'SOUTH',
#        'Sector': 5
#   },
#    {
#        'City': 'ALLAKAKET',
#        'ICAO ID': 'PFAL',
#        'NAS ID': '6A8',
#        'Area': 'NORTH',
#        'Sector': 4
#    },
#    {
#        'City': 'AKUTAN',
#        'ICAO ID': 'PAUT',
#        'NAS ID': '7AK',
#        'Area': 'NORTH',
#        'Sector': 9
#    },
#    {
#        'City': 'TATITLEK',
#        'ICAO ID': 'PAKA',
#        'NAS ID': '7KA',
#        'Area': 'SOUTH',
#        'Sector': 7
#    },
#    {
#        'City': 'CHUATHBALUK',
#        'ICAO ID': 'PACH',
#        'NAS ID': '9A3',
#        'Area': 'NORTH',
#        'Sector': 13
#    },
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
#    {
#        'City': 'BADAMI',
#        'ICAO ID': 'PABP',
#        'NAS ID': 'AK78',
#        'Area': 'NORTH',
#        'Sector': 4
#    },
#    {
#        'City': 'ATKA',
#        'ICAO ID': 'PAAK',
#        'NAS ID': 'AKA',
#        'Area': 'ATOP',
#        'Sector': 11
#    },
#    {
#        'City': 'AKIAK',
#        'ICAO ID': 'PFAK',
#        'NAS ID': 'AKI',
#        'Area': 'NORTH',
#        'Sector': 13
#    },
#    {
#        'City': 'AKHIOK',
#        'ICAO ID': 'PAKH',
#        'NAS ID': 'AKK',
#        'Area': 'NORTH',
#        'Sector': 9
#    },
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
#    {
#        'City': 'TED STEVENS ANCHORAGE INTL',
#        'ICAO ID': 'PANC',
#        'NAS ID': 'ANC',
#        'Area': 'SOUTH',
#        'Sector': 6
#    },
    {
        'City': 'ANIAK',
        'ICAO ID': 'PANI',
        'NAS ID': 'ANI',
        'Area': 'NORTH',
        'Sector': 13
    },
#    {
#        'City': 'ANVIK',
#        'ICAO ID': 'PANV',
#        'NAS ID': 'ANV',
#        'Area': 'NORTH',
#        'Sector': 3
#    },
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
#    {
#        'City': 'ARCTIC VILLAGE',
#        'ICAO ID': 'PARC',
#        'NAS ID': 'ARC',
#        'Area': 'NORTH',
#        'Sector': 4
#    },
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
#    {
#        'City': 'BIG LAKE',
#        'ICAO ID': 'PAGQ',
#        'NAS ID': 'BGQ',
#        'Area': 'SOUTH',
#        'Sector': 6
#    },
#    {
#        'City': 'ALLEN AAF',
#        'ICAO ID': 'PABI',
#        'NAS ID': 'BIG',
#        'Area': 'NORTH',
#        'Sector': 16
#    },
    {
        'City': 'WILEY POST-WILL ROGERS MEML',
        'ICAO ID': 'PABR',
        'NAS ID': 'BRW',
        'Area': 'NORTH',
        'Sector': 4
    },
#    {
#        'City': 'BARTER ISLAND',
#        'ICAO ID': 'PABA',
#        'NAS ID': 'BTI',
#        'Area': 'NORTH',
#        'Sector': 4
#    },
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
#    {
#        'City': 'CENTRAL',
#        'ICAO ID': 'PACE',
#        'NAS ID': 'CEM',
#        'Area': 'NORTH',
#        'Sector': 16
#    },
#    {
#        'City': 'CHALKYITSIK',
#        'ICAO ID': 'PACI',
#        'NAS ID': 'CIK',
#        'Area': 'NORTH',
#        'Sector': 16
#    },
#    {
#        'City': 'CROOKED CREEK',
#        'ICAO ID': 'PACJ',
#        'NAS ID': 'CJX',
#        'Area': 'NORTH',
#        'Sector': 13
#    },
#    {
#        'City': 'CLARKS POINT',
#        'ICAO ID': 'PFCL',
#        'NAS ID': 'CLP',
#        'Area': 'NORTH',
#        'Sector': 9
#    },
#    {
#        'City': 'COLDFOOT',
#        'ICAO ID': 'PACX',
#        'NAS ID': 'CXF',
#        'Area': 'NORTH',
#        'Sector': 4
#    },
    {
        'City': 'CAPE ROMANZOF LRRS',
        'ICAO ID': 'PACZ',
        'NAS ID': 'CZF',
        'Area': 'NORTH',
        'Sector': 3
    },
#    {
#        'City': 'ROBERT/BOB/CURTIS MEML',
#        'ICAO ID': 'PFNO',
#        'NAS ID': 'D76',
#        'Area': 'NORTH',
#        'Sector': 4
#    },
#    {
#        'City': 'DEERING',
#        'ICAO ID': 'PADE',
#        'NAS ID': 'DEE',
#        'Area': 'NORTH',
#        'Sector': 4
#    },
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
#    {
#        'City': 'EAGLE',
#        'ICAO ID': 'PAEG',
#        'NAS ID': 'EAA',
#        'Area': 'NORTH',
#        'Sector': 16
#    },
#    {
#        'City': 'ELMENDORF AFB',
#        'ICAO ID': 'PAED',
#        'NAS ID': 'EDF',
#        'Area': 'SOUTH',
#        'Sector': 6
#    },
#    {
#        'City': 'EEK',
#        'ICAO ID': 'PAEE',
#        'NAS ID': 'EEK',
#        'Area': 'NORTH',
#        'Sector': 13
#    },
#    {
#        'City': 'CAPE NEWENHAM LRRS',
#        'ICAO ID': 'PAEH',
#        'NAS ID': 'EHM',
#        'Area': 'NORTH',
#        'Sector': 9
#    },
#    {
#        'City': 'EGEGIK',
#        'ICAO ID': 'PAII',
#        'NAS ID': 'EII',
#        'Area': 'NORTH',
#        'Sector': 9
#    },
#    {
#        'City': 'EIELSON AFB',
#        'ICAO ID': 'PAEI',
#        'NAS ID': 'EIL',
#        'Area': 'NORTH',
#        'Sector': 16
#    },
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
#    {
#        'City': 'NENANA MUNI',
#        'ICAO ID': 'PANN',
#        'NAS ID': 'ENN',
#        'Area': 'NORTH',
#        'Sector': 15
#    },
#    {
#        'City': 'FAIRBANKS INTL',
#        'ICAO ID': 'PAFA',
#        'NAS ID': 'FAI',
#        'Area': 'NORTH',
#        'Sector': 15
#    },
#    {
##        'City': 'LADD AAF',
#        'ICAO ID': 'PAFB',
#        'NAS ID': 'FBK',
#        'Area': 'NORTH',
#        'Sector': 4
#    },
#    {
#        'City': 'NIKOLAI',
#        'ICAO ID': 'PAFS',
#        'NAS ID': 'FSP',
#        'Area': 'NORTH',
#        'Sector': 3
#    },
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
#    {
#        'City': 'GOLOVIN',
#        'ICAO ID': 'PAGL',
#        'NAS ID': 'GLV',
#        'Area': 'NORTH',
#        'Sector': 3
#    },
    {
        'City': 'GUSTAVUS',
        'ICAO ID': 'PAGS',
        'NAS ID': 'GST',
        'Area': 'SOUTH',
        'Sector': 8
    },
#    {
#        'City': 'HOLY CROSS',
#        'ICAO ID': 'PAHC',
#        'NAS ID': 'HCA',
#        'Area': 'NORTH',
#        'Sector': 13
#    },
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
#    {
#        'City': 'HEALY RIVER',
#        'ICAO ID': 'PAHV',
#        'NAS ID': 'HRR',
#        'Area': 'NORTH',
#        'Sector': 15
#    },
#    {
#        'City': 'HUGHES',
#        'ICAO ID': 'PAHU',
#        'NAS ID': 'HUS',
#        'Area': 'NORTH',
#        'Sector': 4
#    },
#    {
#        'City': 'BOB BAKER MEML',
#        'ICAO ID': 'PAIK',
#        'NAS ID': 'IAN',
#        'Area': 'NORTH',
#        'Sector': 4
#    },
#    {
#        'City': 'IGIUGIG',
#        'ICAO ID': 'PAIG',
#        'NAS ID': 'IGG',
#        'Area': 'NORTH',
#        'Sector': 9
#    },
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
#    {
#        'City': 'WALES',
#        'ICAO ID': 'PAIW',
#        'NAS ID': 'IWK',
#        'Area': 'NORTH',
#        'Sector': 3
#    },
#    {
#        'City': 'WASILLA',
#        'ICAO ID': 'PAWS',
#        'NAS ID': 'IYS',
#        'Area': 'SOUTH',
#        'Sector': 6
#    },
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
#    {
#        'City': 'KALTAG',
#        'ICAO ID': 'PAKV',
#        'NAS ID': 'KAL',
#        'Area': 'NORTH',
#        'Sector': 3
#    },
#    {
#        'City': 'GRAYLING',
#        'ICAO ID': 'PAGX',
#        'NAS ID': 'KGX',
#        'Area': 'NORTH',
#        'Sector': 3
#    },
#    {
#        'City': 'KOYUK ALFRED ADAMS',
#        'ICAO ID': 'PAKK',
#        'NAS ID': 'KKA',
#        'Area': 'NORTH',
#        'Sector': 3
#    },
#    {
#        'City': 'KALSKAG',
#        'ICAO ID': 'PALG',
#        'NAS ID': 'KLG',
#        'Area': 'NORTH',
#        'Sector': 13
#    },
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
#    {
#        'City': 'KING COVE',
#        'ICAO ID': 'PAVC',
#        'NAS ID': 'KVC',
#        'Area': 'NORTH',
#        'Sector': 9
#    },
#    {
#        'City': 'KIVALINA',
#        'ICAO ID': 'PAVL',
#        'NAS ID': 'KVL',
#        'Area': 'NORTH',
#        'Sector': 4
#    },
#    {
#        'City': 'KWETHLUK',
#        'ICAO ID': 'PFKW',
#        'NAS ID': 'KWT',
#        'Area': 'NORTH',
#        'Sector': 13
#    },
#    {
#        'City': 'KOYUKUK',
#        'ICAO ID': 'PFKU',
#        'NAS ID': 'KYU',
#        'Area': 'NORTH',
#        'Sector': 4
#    },
#    {
#        'City': 'CAPE LISBURNE LRRS',
#        'ICAO ID': 'PALU',
#        'NAS ID': 'LUR',
#        'Area': 'NORTH',
#        'Sector': 4
#    },
#    {
#        'City': 'MANOKOTAK',
#        'ICAO ID': 'PAMB',
#        'NAS ID': 'MBA',
#        'Area': 'NORTH',
#        'Sector': 9
#    },
    {
        'City': 'MC GRATH',
        'ICAO ID': 'PAMC',
        'NAS ID': 'MCG',
        'Area': 'NORTH',
        'Sector': 3
    },
#    {
#        'City': 'MARSHALL DON HUNTER SR',
#        'ICAO ID': 'PAMD',
#        'NAS ID': 'MDM',
#        'Area': 'NORTH',
#        'Sector': 13
#    },
    {
        'City': 'MIDDLETON ISLAND',
        'ICAO ID': 'PAMD',
        'NAS ID': 'MDO',
        'Area': 'SOUTH',
        'Sector': 7
    },
#    {
#        'City': 'MINCHUMINA',
#        'ICAO ID': 'PAMH',
#        'NAS ID': 'MHM',
#        'Area': 'NORTH',
#        'Sector': 15
#    },
#    {
#        'City': 'MANLEY HOT SPRINGS',
#        'ICAO ID': 'PAML',
#        'NAS ID': 'MLY',
#        'Area': 'NORTH',
#        'Sector': 15
#    },
#    {
#        'City': 'MOUNTAIN VILLAGE',
#        'ICAO ID': 'PAMO',
#        'NAS ID': 'MOU',
#        'Area': 'NORTH',
#        'Sector': 13
#    },
#    {
#        'City': 'MERRILL FLD',
#        'ICAO ID': 'PAMR',
#        'NAS ID': 'MRI',
#        'Area': 'SOUTH',
#        'Sector': 6
#    },
#    {
#        'City': 'MEKORYUK',
#        'ICAO ID': 'PAMY',
#        'NAS ID': 'MYU',
#        'Area': 'NORTH',
#        'Sector': 3
#    },
#    {
#        'City': 'NULATO',
#        'ICAO ID': 'PANU',
#        'NAS ID': 'NUL',
#        'Area': 'NORTH',
#        'Sector': 3
#    },
#    {
#        'City': 'KOBUK',
#        'ICAO ID': 'PAOB',
#        'NAS ID': 'OBU',
#        'Area': 'NORTH',
#        'Sector': 4
#    },
    {
        'City': 'NOME',
        'ICAO ID': 'PAOM',
        'NAS ID': 'OME',
        'Area': 'NORTH',
        'Sector': 3
    },
#    {
#        'City': 'TOKSOOK BAY',
#        'ICAO ID': 'PAOO',
#        'NAS ID': 'OOK',
#        'Area': 'NORTH',
#        'Sector': 3
#    },
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
#    {
#        'City': 'NELSON LAGOON',
#        'ICAO ID': 'PAOU',
#        'NAS ID': 'OUL',
#        'Area': 'NORTH',
#        'Sector': 9
#    },
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
#    {
#        'City': 'PERRYVILLE',
#        'ICAO ID': 'PAPE',
#        'NAS ID': 'PEV',
#        'Area': 'NORTH',
#        'Sector': 9
#    },
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
#    {
#        'City': 'NAPASKIAK',
#        'ICAO ID': 'PAPK',
#        'NAS ID': 'PKA',
#        'Area': 'NORTH',
#        'Sector': 13
#    },
#    {
#        'City': 'PILOT POINT',
#        'ICAO ID': 'PAPN',
#        'NAS ID': 'PNP',
#        'Area': 'NORTH',
#        'Sector': 9
#    },
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
#    {
#        'City': 'PLATINUM',
#        'ICAO ID': 'PAPM',
#        'NAS ID': 'PTU',
#        'Area': 'NORTH',
#        'Sector': 9
#    },
    {
        'City': 'RUBY',
        'ICAO ID': 'PARY',
        'NAS ID': 'RBY',
        'Area': 'NORTH',
        'Sector': 3
    },
#    {
#        'City': 'RUSSIAN MISSION',
#        'ICAO ID': 'PARS',
#        'NAS ID': 'RSH',
#        'Area': 'NORTH',
#        'Sector': 13
#    },
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
#    {
#        'City': 'SHUNGNAK',
#        'ICAO ID': 'PAGH',
#        'NAS ID': 'SHG',
#        'Area': 'NORTH',
#        'Sector': 4
#    },
    {
        'City': 'SHISHMAREF',
        'ICAO ID': 'PASH',
        'NAS ID': 'SHH',
        'Area': 'NORTH',
        'Sector': 3
    },
#    {
#        'City': 'SHAGELUK',
#        'ICAO ID': 'PAHX',
#        'NAS ID': 'SHX',
#        'Area': 'NORTH',
#        'Sector': 3
#    },
    {
        'City': 'SITKA ROCKY GUTIERREZ',
        'ICAO ID': 'PASI',
        'NAS ID': 'SIT',
        'Area': 'SOUTH',
        'Sector': 8
    },
#    {
#        'City': 'SLEETMUTE',
#        'ICAO ID': 'PASL',
#        'NAS ID': 'SLQ',
#        'Area': 'NORTH',
#        'Sector': 13
#    },
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
#    {
#        'City': 'RALPH M CALHOUN MEML',
#        'ICAO ID': 'PATA',
#        'NAS ID': 'TAL',
#        'Area': 'NORTH',
#        'Sector': 15
#    },
#    {
#        'City': 'TELLER',
#        'ICAO ID': 'PATE',
#        'NAS ID': 'TER',
#        'Area': 'NORTH',
#        'Sector': 3
#    },
    {
        'City': 'TALKEETNA',
        'ICAO ID': 'PATK',
        'NAS ID': 'TKA',
        'Area': 'SOUTH',
        'Sector': 6
    },
#    {
#        'City': 'TATALINA',
#        'ICAO ID': 'PATL',
#        'NAS ID': 'TLJ',
#        'Area': 'NORTH',
#        'Sector': 3
#    },
#    {
#        'City': 'TIN CITY LRRS',
#        'ICAO ID': 'PATC',
#        'NAS ID': 'TNC',
#        'Area': 'NORTH',
#        'Sector': 3
#    },
#    {
#        'City': 'TOGIAK',
#        'ICAO ID': 'PATG',
#        'NAS ID': 'TOG',
#        'Area': 'NORTH',
#        'Sector': 9
#    },
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
#    {
#        'City': 'INDIAN MOUNTAIN LRRS',
#        'ICAO ID': 'PAIM',
#        'NAS ID': 'UTO',
#        'Area': 'NORTH',
#        'Sector': 15
#    },
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
#    {
#        'City': 'VENETIE',
#        'ICAO ID': 'PAVE',
#        'NAS ID': 'VEE',
#        'Area': 'NORTH',
#        'Sector': 4
#    }, {
#        'City': 'BEAVER',
#        'ICAO ID': 'PAWB',
#        'NAS ID': 'WBQ',
#        'Area': 'NORTH',
#        'Sector': 4
#    },
#    {
#        'City': 'WHITTIER',
#        'ICAO ID': 'PAWR',
#        'NAS ID': 'WTR',
#        'Area': 'SOUTH',
#        'Sector': 6
#    },
#    {
#        'City': 'SELAWIK',
#        'ICAO ID': 'PASK',
#        'NAS ID': 'WLK',
#        'Area': 'NORTH',
#        'Sector': 4
#    },
#    {
#        'City': 'WHITE MOUNTAIN',
#        'ICAO ID': 'PAWM',
#        'NAS ID': 'WMO',
#        'Area': 'NORTH',
#        'Sector': 3
#    },
#    {
#        'City': 'NAPAKIAK',
#        'ICAO ID': 'PANA',
#        'NAS ID': 'WNA',
#        'Area': 'NORTH',
#        'Sector': 13
#    },
    {
        'City': 'WRANGELL',
        'ICAO ID': 'PAWG',
        'NAS ID': 'WRG',
        'Area': 'SOUTH',
        'Sector': 8
    },
#    {
#        'City': 'SOUTH NAKNEK NR 2',
#        'ICAO ID': 'PFWS',
#        'NAS ID': 'WSN',
#        'Area': 'NORTH',
#        'Sector': 9
#    },
#    {
#        'City': 'NOATAK',
#        'ICAO ID': 'PAWN',
#        'NAS ID': 'WTK',
#        'Area': 'NORTH',
#        'Sector': 4
#    },
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
    "url_template": "https://aviationweather.gov/api/data/dataserver?requestType=retrieve&dataSource=aircraftreports&hoursBeforeNow={hours}&format=xml&boundingBox={minlat},{minlon},{maxlat},{maxlon}"
}
def get_pirep_url():
    return pirep_config["url_template"].format(
        hours=pirep_config["hoursBeforeNow"],
        minlat=pirep_config["MinLat"],
        maxlat=pirep_config["MaxLat"],
        minlon=pirep_config["MinLon"],
        maxlon=pirep_config["MaxLon"]
    )

pasy_url = "https://aviationweather.gov/api/data/dataserver?requestType=retrieve&dataSource=aircraftreports&hoursBeforeNow=1&format=xml&boundingBox=45%2C%20159%2C%2055%2C%20179"

areas = {
    "NORTH": {
        "sectors": {
            3: [
                (66.45, -168.973),(66.6172, -165.3277),
                (65.6277, -163.3261),(65.6686, -160.8152),
                (66.1102, -158.4),(66.1166, -157),
                (65.6819, -154.1083),(64.7333, -154.3333),
                (63.1536, -152.3463),(63, -153.0833),
                (62.4166, -153.5),(61.725, -155.2158),
                (63.113, -159.5669),(62.98, -161.1641),
                (63.353, -163.4313),(62.3305, -170.3369),
                (62.67, -170.7525),(62.9583, -174.5825),
                (64.05, -172.2),(65, -168.973)
            ],
            4: [
                (73.4013, -150.2491),(73.4019, -159.7072),
                (73, -168.973),(66.45, -168.973),
                (66.6172, -165.3277),(65.6277, -163.3261),
                (65.6686, -160.8152),(66.1102, -158.4),
                (66.1166, -157),(65.6819, -154.1083),
                (66.1166, -154),(67.3333, -141),(73, -141)

            ],
            9:[
                (59.3311, -167.9138),(59.6652, -165.6119),
                (59.3633, -161.4152),(60.5883, -156.4369),
                (59.9, -156.4166),(59.5, -155.3333),
                (59.1619, -152.2913),(59.1833, -150),
                (57.4638, -150.5308),(56.7616, -151.75),
                (56, -153),(53.5, -160),(52.5997, -163.6791),
                (53.4652, -167.3372),(54.2172, -167.7441),
                (55, -167),(56.9666, -165),
                (58.2469, -166.9247),(58.7394, -167.713)
            ],
            13:[
                (62.3305, -170.3369),(63.353, -163.4313),
                (62.98, -161.1641),(63.113, -159.5669),
                (61.725, -155.2158),(61.4908, -156.4647),
                (60.5883, -156.4369),(59.3633, -161.4152),
                (59.6652, -165.6119),(59.3311, -167.9138),
                (60.5875, -168.3636)
            ],
            15:[
                (67.333, -141.0002),(66.1163, -154),
                (65.6816, -154.1083),(64.733, -154.3333),
                (63.1536, -152.3463),(62.9677, -148.5719),
                (63.9663, -148),(64.3747, -147.9666),
                (64.4352, -147.8544),(64.753, -147.6305),
                (64.8383, -147.4875),(65.0044, -147.2858),
                (65.2541, -147.1925),(65.6663, -146.2833),
                (65.9997, -145.8425),(65.9997, -145.2569),
                (66.6663, -144.5002),(66.6663, -141.0002)
            ],
            16:[
                (63.3333, -141),(64.9502, -141),
                (66.6666, -141),(66.6666, -144.5),
                (66, -145.2569),(65.9997, -145.8422),
                (65.6666, -146.2833),(65.2544, -147.1922),
                (65.0044, -147.285),(64.8386, -147.4875),
                (64.7533, -147.6305),(64.4352, -147.8541),
                (64.375, -147.9666),(63.9666, -148),
                (62.9677, -148.5716),(62.8333, -146.5833)
            ]
            # Add other sectors (9, 13, 15, 16) and their polygons
        }
    },
    "SOUTH": {
        "sectors": {
            5:[
                (61.725, -155.2158),(61.4166, -152.8),
                (61.2333, -152.7833),(61.2333, -152.1166),
                (61.0833, -151.75),(61.0833, -151.0738),
                (60.8755, -150.1597),(60.5, -150),
                (59.1833, -150),(59.1619, -152.2913),
                (59.5, -155.3333),(59.9, -156.4166),
                (60.5883, -156.4369),(61.4908, -156.4647)

            ],
            6:[
                (63, -153.0833),(62.4166, -153.5),
                (61.725, -155.2158),(61.4166, -152.8),
                (61.2333, -152.7833),(61.2333, -152.1166),
                (61.0833, -151.75),(61.0833, -151.0738),
                (60.8755, -150.1597),(61.4716, -149.0666),
                (61.75, -147.4166),(62.8333, -146.5833),
                (62.9677, -148.5716),(63.1536, -152.3463)


            ],
            7: [
                (63.3333, -141),(62, -141),
                (60.35, -139.1833),(60.5333, -141.3333),
                (59.4838, -142.1233),(59, -146),
                (59.1833, -150),(60.5, -150),
                (60.8755, -150.1597),(61.4716, -149.0666),
                (61.75, -147.4166),(62.8333, -146.5833)

            ],
            8: [
                (58, -137.8333),(59.0019, -140.2911),(59.4838, -142.1233),
                (60.5333, -141.3333),(60.35, -139.1833),(60.3527, -139.0727),
                (60.3197, -139.0702),(60.0886, -139.1969),(59.995, -139.0516),
                (59.9247, -138.7966),(59.9063, -138.7052),(59.8455, -138.6775),
                (59.8097, -138.6666),(59.7688, -138.6241),(59.5244, -136.2366),
                (59.3872, -134.9877),(59.3466, -135.0286),(59.2811, -134.958),
                (59.2491, -134.6988),(59.1925, -134.6772),(59.1313, -134.5636),
                (59.1316, -134.4813),(59.0894, -134.4452),(59.0388, -134.38),
                (58.9794, -134.4052),(58.9622, -134.3116),(58.9236, -134.3344),
                (58.9013, -134.3063),(58.8611, -134.2561),(58.7675, -133.9705),
                (58.7297, -133.8386),(58.6125, -133.7052),(58.593, -133.6727),
                (58.585, -133.6591),(58.5797, -133.65),(58.5794, -133.65),
                (58.5516, -133.603),(58.5233, -133.5558),(58.4308, -133.3752),
                (58.3877, -133.4597),(58.2763, -133.3436),(58.2272, -133.268),
                (58.1902, -133.2188),(58.1816, -133.2075),(58.1747, -133.198),
                (58.1538, -133.1702),(58.0005, -133.068),(57.8397, -132.8675),
                (57.6961, -132.7491),(57.6169, -132.6588),(57.4966, -132.5516),
                (57.35, -132.3677),(57.2113, -132.2458),(57.0916, -132.3669),
                (57.0452, -132.0433),(56.9997, -132.0641),(56.8738, -132.1216),
                (56.8061, -131.8711),(56.7538, -131.8991),(56.703, -131.8588),
                (56.6711, -131.8508),(56.6619, -131.8488),(56.6511, -131.8461),
                (56.633, -131.8416),(56.5994, -131.8336),(56.6011, -131.8),
                (56.603, -131.7616),(56.6036, -131.7494),(56.6044, -131.7361),
                (56.6061, -131.7041),(56.6083, -131.6572),(56.6097, -131.6308),
                (56.6125, -131.5791),(56.5527, -131.47),(56.5002, -131.3177),
                (56.4972, -131.3091),(56.4925, -131.2952),(56.4919, -131.2933),
                (56.4497, -131.1713),(56.4061, -131.0852),(56.3905, -130.9638),
                (56.3875, -130.94),(56.385, -130.9208),(56.3841, -130.9127),
                (56.3797, -130.8775),(56.3769, -130.8577),(56.3669, -130.78),
                (56.3516, -130.7558),(56.3436, -130.743),(56.3386, -130.7347),
                (56.3347, -130.7291),(56.328, -130.7183),(56.3216, -130.708),
                (56.3066, -130.6841),(56.295, -130.6655),(56.2822, -130.6455),
                (56.2811, -130.6436),(56.2691, -130.6247),(56.2669, -130.6213),
                (56.2652, -130.6133),(56.2575, -130.5802),(56.2547, -130.5688),
                (56.2475, -130.5386),(56.243, -130.4658),(56.2152, -130.4541),
                (56.2033, -130.4494),(56.1986, -130.4475),(56.1747, -130.4375),
                (56.1416, -130.4238),(56.1286, -130.348),(56.0966, -130.2441),
                (56.0994, -130.228),(56.1227, -130.1019),(56.0991, -130.0808),
                (56.0783, -130.0627),(56.0713, -130.0566),(56.07, -130.0555),
                (56.0663, -130.0522),(56.0463, -130.0347),(56.0441, -130.0327),
                (56.0175, -130.0094),(56.008, -130.0013),(56.0013, -130.0019),
                (56.0011, -130.0019),(55.993, -130.0033),(55.9469, -130.0102),
                (55.93, -130.013),(55.9186, -130.0147),(55.9122, -130.0155),
                (55.9119, -130.0155),(55.9119, -130.0144),(55.9119, -130.0016),
                (55.9075, -130.0016),(55.8219, -130.0813),(55.8058, -130.1227),
                (55.7663, -130.1505),(55.7266, -130.1525),(55.683, -130.1097),
                (55.5811, -130.1258),(55.498, -130.0877),(55.4519, -130.0391),
                (55.338, -130.0191),(55.3005, -129.9747),(55.2819, -129.9722),
                (55.1927, -130.1011),(55.143, -130.1441),(55.1247, -130.1505),
                (55.0913, -130.1791),(55.063, -130.1858),(54.9741, -130.2713),
                (54.9177, -130.3441),(54.8736, -130.4208),(54.8513, -130.4525),
                (54.8369, -130.4783),(54.7922, -130.5663),(54.7827, -130.6269),
                (54.7633, -130.6572),(54.7383, -130.6238),(54.725, -130.6269),
                (54.7166, -130.6166),(54.4916, -131.8),(54.5833, -132.8333),
                (54.4083, -133.2738)

            ]
        },
    },
    "HIGH": {
        "sectors":{
            63: [
                (66.45, -168.973),(66.6172, -165.3277),
                (65.6277, -163.3261),(65.6686, -160.8152),
                (66.1102, -158.4),(66.1166, -157),
                (65.6819, -154.1083),(64.7333, -154.3333),
                (63.1536, -152.3463),(63, -153.0833),
                (62.4166, -153.5),(61.725, -155.2158),
                (61.4908, -156.4647),(60.5883, -156.4369),
                (59.6652, -165.6119),(59.3311, -167.9138),
                (60.5875, -168.3636),(62.3305, -170.3369),
                (62.67, -170.7525),(62.9583, -174.5825),
                (64.05, -172.2),(65, -168.973),
                (66.45, -168.973)
            ],
            64: [
                (75.6817, -141),(75, -141),
                (73.4428, -141),(72.9986, -141),
                (73.402, -159.7074),(72.9986, -168.9725),
                (72.9986, -168.973),(74.9404, -168.973),
                (90, -141),(75.6817, -141)
            ],
            
            68: [
                (54.1166, -134),(54.1083, -135.45),(54, -136),
                (53.3674, -137),(54.6875, -141.6464),(55.8239, -146.5707),
                (56.7616, -151.75),(57.4641, -150.5309),(59.1833, -150),
                (59, -146),(59.4839, -142.1235),(59.0021, -140.2913),
                (58, -137.8333),(56.9513, -134.9983),(56.6388, -133.0675),
                (56.9997, -132.0641),(56.8738, -132.1216),(56.8061, -131.8711),
                (56.7538, -131.8991),(56.703, -131.8588),(56.6711, -131.8508),
                (56.6619, -131.8488),(56.6511, -131.8461),(56.633, -131.8416),
                (56.5994, -131.8336),(56.6011, -131.8),(56.603, -131.7616),
                (56.6036, -131.7494),(56.6044, -131.7361),(56.6061, -131.7041),
                (56.6083, -131.6572),(56.6097, -131.6308),(56.6125, -131.5791),
                (56.5527, -131.47),(56.5002, -131.3177),(56.4972, -131.3091),
                (56.4925, -131.2952),(56.4919, -131.2933),(56.4497, -131.1713),
                (56.4061, -131.0852),(56.3905, -130.9638),(56.3875, -130.94),
                (56.385, -130.9208),(56.3841, -130.9127),(56.3797, -130.8775),
                (56.3769, -130.8577),(56.3669, -130.78),(56.3516, -130.7558),
                (56.3436, -130.743),(56.3386, -130.7347),(56.3347, -130.7291),
                (56.328, -130.7183),(56.3216, -130.708),(56.3066, -130.6841),
                (56.295, -130.6655),(56.2822, -130.6455),(56.2811, -130.6436),
                (56.2691, -130.6247),(56.2669, -130.6213),(56.2652, -130.6133),
                (56.2575, -130.5802),(56.2547, -130.5688),(56.2475, -130.5386),
                (56.243, -130.4658),(56.2152, -130.4541),(56.2033, -130.4494),
                (56.1986, -130.4475),(56.1747, -130.4375),(56.1416, -130.4238),
                (56.1286, -130.348),(56.0966, -130.2441),(56.0994, -130.228),
                (56.1227, -130.1019),(56.0991, -130.0808),(56.0783, -130.0627),
                (56.0713, -130.0566),(56.07, -130.0555),(56.0663, -130.0522),
                (56.0463, -130.0347),(56.0441, -130.0327),(56.0175, -130.0094),
                (56.008, -130.0013),(56.0013, -130.0019),(56.0011, -130.0019),
                (55.993, -130.0033),(55.9469, -130.0102),(55.93, -130.013),
                (55.9186, -130.0147),(55.9122, -130.0155),(55.9119, -130.0155),
                (55.9119, -130.0144),(55.9119, -130.0016),(55.9075, -130.0016),
                (55.8219, -130.0813),(55.8058, -130.1227),(55.7663, -130.1505),
                (55.7266, -130.1525),(55.683, -130.1097),(55.5811, -130.1258),
                (55.498, -130.0877),(55.4519, -130.0391),(55.338, -130.0191),
                (55.3005, -129.9747),(55.2819, -129.9722),(55.1927, -130.1011),
                (55.143, -130.1441),(55.1247, -130.1505),(55.0913, -130.1791),
                (55.063, -130.1858),(54.9741, -130.2713),(54.9177, -130.3441),
                (54.8736, -130.4208),(54.8513, -130.4525),(54.8369, -130.4783),
                (54.7922, -130.5663),(54.7827, -130.6269),(54.7633, -130.6572),
                (54.7383, -130.6238),(54.725, -130.6269),(54.7166, -130.6166),
                (54.4916, -131.8),(54.5833, -132.8333),(54.4083, -133.2738)

            ],
            69: [
                (59.1833, -150),(57.4641, -150.5309),
                (56.7616, -151.75),(57.3133, -155.6023),
                (57.7887, -159.9487),(57.8327, -160.4357),
                (58.0606, -163.394),(58.2469, -166.9247),
                (58.7396, -167.7133),(59.3312, -167.9141),
                (59.7872, -164.6833),(60.2501, -160.6125),
                (60.5883, -156.4369),(59.9, -156.4166),
                (59.5, -155.3333),(59.1619, -152.2913),
                (59.1833, -150)
            ]
        }
    },
    "ATOP": {
        "sectors": {
            10:[
                (62.9585, -174.5826),(62.67, -170.7525),
                (60.5875, -168.3638),(59.3312, -167.9141),
                (58.7396, -167.7133),(58.6236, -171.3611),
                (58.4132, -174.9778),(57.067, -180.2347),
                (55.93, -183.8357),(49.3632, -200.2986),
                (50.0833, -201),(54, -191),
                (57.3632, -185.481),(58.1704, -183.9288),(60, -180)

            ],
            11:[
                (58.2469, -166.9247),(58.0606, -163.394),
                (57.8327, -160.4357),(57.7887, -159.9487),
                (57.3133, -155.6023),(56.7616, -151.75),
                (56.7616, -151.75),(56, -153),
                (54.7993, -156.6037),(53.5, -160),
                (52.5999, -163.6791),(51.4, -167.8166),
                (51.1207, -170.25),(50.8498, -172.2516),
                (50.1333, -176.5666),(49.8756, -178.7223),
                (45.7, -197.0833),(49.3632, -200.2986),
                (53.3751, -190.4334),(55.93, -183.9357),
                (57.067, -180.2347),(58.4132, -174.9778),
                (58.6236, -171.3611),(58.7396, -167.7133)
            ]
            
        }
    },
    # Define other areas like ATOP, HIGH
}


#!/usr/bin/env ruby

world_code_map = {
    'ALGERIA'=>'DZ',
    'ARGENTINA'=>'AR',
    'AUSTRALIA'=>'AU',
    'AUSTRIA'=>'AT',
    'BELGIUM'=>'BE',
    'BRAZIL'=>'BR',
    'CANADA'=>'CA',
    'CHILE'=>'CL',
    'CHINA'=>'CN',
    'COLOMBIA'=>'CO',
    'CYPRUS'=>'CY',
    'CZECHIA'=>'CZ',
    'DENMARK'=>'DK',
    'EGYPT'=>'EG',
    'ESWATINI'=>'ES',
    'FINLAND'=>'FI',
    'FRANCE'=>'FR',
    'GEORGIA'=>'GE',
    'GERMANY'=>'DE',
    'GREECE'=>'GR',
    'GUERNSEY'=>'GU',
    'HONG KONG'=>'HK',
    'HUNGARY'=>'HU',
    'ICELAND'=>'IC',
    'INDIA'=>'IN',
    'HONG KONG'=>'HK',
    'HUNGARY'=>'HU',
    'ICELAND'=>'IC',
    'INDIA'=>'IN',
    'INDONESIA'=>'ID',
    'IRELAND'=>'IR',
    'ISRAEL'=>'IS',
    'ITALY'=>'IT',
    'JAPAN'=>'JP',
    'KAZAKHSTAN'=>'KA',
    'LEBANON'=>'LE',
    'LIECHTENSTEIN'=>'LI',
    'MACAO'=>'MA',
    'MALAYSIA'=>'MY',
    'MEXICO'=>'ME',
    'MONACO'=>'MO',
    'NEPAL'=>'NP',
    'NETHERLANDS'=>'NE',
    'NEW ZEALAND'=>'NZ',
    'NIGERIA'=>'NI',
    'NORWAY'=>'NO',
    'OMAN'=>'OM',
    'PERU'=>'PE',
    'PHILIPPINES'=>'PH',
    'POLAND'=>'PO',
    'PORTUGAL'=>'PR',
    'QATAR'=>'QA',
    'ROMANIA'=>'RO',
    'RUSSIA'=>'RU',
    'SINGAPORE'=>'SI',
    'SLOVAKIA'=>'SL',
    'SOUTH AFRICA'=>'SA',
    'SOUTH KOREA'=>'SK',
    'SPAIN'=>'SP',
    'ST. KITTS AND NEVIS'=>'KN',
    'SWEDEN'=>'SW',
    'SWITZERLAND'=>'SU',
    'TAIWAN'=>'TW',
    'TANZANIA'=>'TZ',
    'THAILAND'=>'TH',
    'TURKEY'=>'TU',
    'UKRAINE'=>'UK',
    'UNITED ARAB EMIRATES'=>'UA',
    'UNITED KINGDOM'=>'UK',
    'UNITED STATES'=>'US',
    'VENEZUELA'=>'VZ',
    'VIETNAM'=>'VI',
    'ZIMBABWE'=>'ZI',

}

File.open(ARGV[0], 'r') { |file|
  file.each_line { |line|
    new_line = line
    line =~ /"name":"([\w\s]+)"/
    if ($1)
      country_name = $1.upcase()
      world_code = world_code_map[country_name]
      new_line = line.sub(/"name":"#{$1}"/, %{"name":"#{world_code}"})
    end

    puts new_line
  }
}
def clean_manufact(df):
    mf = df['manufacturing_places'].astype(str)
    mf = mf.str.lower()
    mf[mf.str.contains('france|francaise|française|francia|franche comté|franche comté|31016|yéo frais|framce|rankfreich|occitane|fromagère|asqu|rancia')] = "France"
    # Still have to remove 'uk'
    mf[mf.str.contains('united-kingdom|united kingdom|oyaume|ingdom|londo|ngleterre|made in uk|cotla|UK|cosse|engl|schotland')] = "United kingdom"
    # Still have to remove 'CH '
    mf[mf.str.contains('witzerland|uisse|chweiz|vizzera')] = "Switzerland"
    mf[mf.str.contains('ermany|llemagne|eutschland|lemania|berlin|amburg|Munich|erlin|uitsland|lemanha|germania')] = "Germany"
    mf[mf.str.contains('taly|tali|ita|rome')] = "Italy"
    mf[mf.str.contains('pain|spaña|spana|spanha|spagne|span|espa|spagna|arcel|adrid|spagna')] = "Spain"
    mf[mf.str.contains('ortugal|lisb|potugal')] = "Portugal"
    mf[mf.str.contains('enmark|yskland|danemark|dänemark')] = "Denmark"
    mf[mf.str.contains('elgium|elgi|elguim|élgica')] = "Belgium"
    mf[mf.str.contains('usa|nited states|tates|eta|tats|État unis|état-unis|stados u|stados u|estado')] = "United states"
    mf[mf.str.contains('exi|éxi')] = "Mexico"
    mf[mf.str.contains('rasil|brazil')] = "Brasil"
    mf[mf.str.contains('hina|chine')] = "China"
    mf[mf.str.contains('ustra')] = "Australia"
    mf[mf.str.contains('austria|sterr|utriche')] = "Austria"
    mf[mf.str.contains('weden|suede|verig|uède')] = "Sweden"
    mf[mf.str.contains('orway|norv')] = "Norway"
    mf[mf.str.contains('hail|haï|tail')] = "Thailand"
    mf[mf.str.contains('ederla|olland|ays b|pays|pays-bas|ether|ethelands')] = "Netherland"
    mf[mf.str.contains('anada|uébec|canad|toro')] = "Canada"
    mf[mf.str.contains('inland|uomi')] = "Finland"
    mf[mf.str.contains('reland|rlande')] = "Ireland"
    mf[mf.str.contains('poland|olsk|polo|polen')] = "Poland"
    mf[mf.str.contains('aiwan|aïwan|taiwán')] = "Taiwan"
    mf[mf.str.contains('ndonesia|indonasia')] = "Indonesia"
    mf[mf.str.contains('ambod')] = "Cambodia"
    mf[mf.str.contains('ietnam')] = "Vietnam"
    mf[mf.str.contains('ussia|ussie')] = "Russia"
    mf[mf.str.contains('etto|atvi')] = "Latvia"
    mf[mf.str.contains('japon|japan|japan')] = "Japan"
    mf[mf.str.contains('argentine|argentina|argentina')] = "Argentina"
    mf[mf.str.contains('hilip|hillip')] = "Philippines"
    mf[mf.str.contains('hile|chili')] = "Chile"
    mf[mf.str.contains('uxemb')] = "Luxembourg"
    mf[mf.str.contains('slova')] = "Slovakia"
    mf[mf.str.contains('croat')] = "Croatia"
    mf[mf.str.contains('cz|tchèque')] = "Czech republic"
    mf[mf.str.contains('romania|romă|ouman')] = "Romania"
    mf[mf.str.contains('indi')] = "India"
    mf[mf.str.contains('srael|israël')] = "Israel"
    mf[mf.str.contains('ingap')] = "Singapour"
    mf[mf.str.contains('tunis')] = "Tunisia"
    mf[mf.str.contains('morocco|maroc')] = "Morocco"
    mf[mf.str.contains('reec|rèce|riech')] = "Greece"
    mf[mf.str.contains('gyp')] = "Egypt"
    mf[mf.str.contains('celand|slande')] = "Iceland"
    mf[mf.str.contains('peru|érou')] = "Peru"
    mf[mf.str.contains('lanka')] = "Sri lanka"
    mf[mf.str.contains('trinité et tobago')] = "Trinidad and tobago"
    mf[mf.str.contains('kong')] = "Hong kong"
    mf[mf.str.contains('malaysia|malaisie')] = "Malaysia"
    mf[mf.str.contains('serbi')] = "Serbia"
    mf[mf.str.contains('urug')] = "Uruguay"
    mf[mf.str.contains('south africa|afrique du sud|süd|cape town|sydafrika')] = "South africa"
    mf[mf.str.contains('domin')] = "Dominican republic"
    mf[mf.str.contains('turk|turcia|turq')] = "Turkey"
    mf[mf.str.contains('kore|corea|coré')] = "South korea"
    mf[mf.str.contains('indo')] = "Indonesia"
    mf[mf.str.contains('hongrie|hung')] = "Hungary"
    mf[mf.str.contains('colomb')] = "Colombia"
    mf[mf.str.contains('zea|élande|elande|zeland')] = "New zealand"
    mf[mf.str.contains('albani')] = "Albania"
    mf[mf.str.contains('alger')] = "Algeria"
    mf[mf.str.contains('armenien')] = "Armenia"
    mf[mf.str.contains('azerbaijan')] = "Azerbaijan"
    mf[mf.str.contains('bangladesh')] = "Bangladesh"
    mf[mf.str.contains('belize')] = "Belize"
    mf[mf.str.contains('boli')] = "Bolivia"
    mf[mf.str.contains('bosni')] = "Bosnia and herzegovina"
    mf[mf.str.contains('bulga')] = "Bulgaria"
    mf[mf.str.contains('burk')] = "Burkina faso"
    mf[mf.str.contains('camer')] = "Cameroon"
    mf[mf.str.contains('congo')] = "Democratic republic of the congo"
    mf[mf.str.contains('costa r')] = "Costa rica"
    mf[mf.str.contains('ivoi')] = "Cote d ivoire"
    mf[mf.str.contains('cuba')] = "Cuba"
    mf[mf.str.contains('cyprus|chypre')] = "Cyprus"
    mf[mf.str.contains('ecua|equat')] = "Ecuador"
    mf[mf.str.contains('esto')] = "Estonia"
    mf[mf.str.contains('ethi')] = "Ethiopia"
    mf[mf.str.contains('georgia|géorgie')] = "Georgia"
    mf[mf.str.contains('grenada')] = "Grenada"
    mf[mf.str.contains('guat')] = "Guatemala"
    mf[mf.str.contains('guya')] = "Guyana"
    mf[mf.str.contains('iraq')] = "Iraq"
    mf[mf.str.contains('jord')] = "Jordan"
    mf[mf.str.contains('keny')] = "Kenya"
    mf[mf.str.contains('kosovo')] = "Kosovo"
    mf[mf.str.contains('kuwait')] = "Kuwait"
    mf[mf.str.contains('leba|liban')] = "Lebanon"
    mf[mf.str.contains('lichte')] = "Lichtenstein"
    mf[mf.str.contains('lithu|litu')] = "Lithuania"
    mf[mf.str.contains('maca')] = "Macao"
    mf[mf.str.contains('mace|macé')] = "Republic of macedonia"
    mf[mf.str.contains('madaga')] = "Madagascar"
    mf[mf == 'mali'] = 'Mali'
    mf[mf.str.contains('malta')] = "Malta"
    mf[mf.str.contains('martini')] = "Martinique"
    mf[mf.str.contains('martini|maurice')] = "Mauritius"
    mf[mf.str.contains('mold')] = "Moldova"
    mf[mf.str.contains('monaco')] = "Monaco"
    mf[mf.str.contains('mongol')] = "Mongolia"
    mf[mf.str.contains('montenegro')] = "Montenegro"
    mf[mf.str.contains('mya')] = "Myanmar"
    mf[mf.str.contains('nami')] = "Namibia"
    mf[mf.str.contains('nigeria')] = "Nigeria"
    mf[mf == 'oman'] = 'Oman'
    mf[mf.str.contains('pakistan')] = 'Pakistan'
    mf[mf.str.contains('papua')] = 'Papua new guinea'
    mf[mf.str.contains('rwanda')] = 'Rwanda'
    mf[mf.str.contains('senegal')] = 'Senegal'
    mf[mf.str.contains('seychelles')] = 'Seychelles'
    mf[mf.str.contains('sloveni|slovéni')] = 'Slovenia'
    mf[mf.str.contains('swaziland')] = 'Swaziland'
    mf[mf.str.contains('syr')] = 'Syria'
    mf[mf.str.contains('tanzani')] = 'Tanzania'
    mf[mf.str.contains('togo')] = 'Togo'
    mf[mf.str.contains('ukraine')] = 'Ukraine'
    mf[mf.str.contains('venezuela')] = 'Venezuela'
    mf[mf.str.contains('viet nam')] = 'Vietnam'
    # American states plus usa variants
    usa_cleaning = 'calif|calfor|pleasanton|corona|cincinnati|é. - u.a.|hyannis|tex|norwalk|état unis|north carolina|wisco|alaska|massac|chicago|é-u.a|u\.s\.a.|é.-u.a.|e\.u.a.|eua|ee.uu.|e\. u. a|u\.s.a|oregon|minneapolis|plano tx|victoria|stockton'
    mf[mf.str.contains(usa_cleaning)] = "United states"
    mf[mf.str.contains('ontario|montréal|quebec|north york|ottaw')] = "Canada"
    
    
    return mf

def clean_coutries_tags(df):
    ct = df['countries_tags'].astype(str)
    ct[ct.str.contain('Albania,sq')] = 'Albania'
    ct[ct.str.contain('Algerie')] = 'Algeria'
    ct[ct.str.contain('Belgie|Belgique')] = 'Belgium'
    ct[ct.str.contain('Comercial mexicana')] = 'Comercial mexicana'
    ct[ct.str.contain('England|Scotland|U k')] = 'United kingdom'
    ct[ct.str.contain('Franca|France,be|France,ca|France,es|Frankrijk|Franța')] = 'France'
    ct[ct.str.contain('Germany,zu')] = 'Germany'
    ct[ct.str.contain('Hungary,hu')] = 'Hungary'
    ct[ct.str.contain('Mexico,es')] = 'Mexico'
    ct[ct.str.contain('Hungary,hu')] = 'Hungary'
    ct[ct.str.contain('Nerderland')] = 'Netherlands'
    ct[ct.str.contain('Spain,es')] = 'Spain'
    ct[ct.str.contain('Portugal,es')] = 'Portugal'
    ct[ct.str.contain('Danemark')] = 'Denmark'
    
    
    
    return ct


def clean_origins_tags(df):
    ot = current_data['origins_tags'].astype(str)
    ot[ot.str.contains('algeri')] = "Algeria"
    ot[ot.str.contains('armeni')] = "Armenia"
    ot[ot.str.contains('australi')] = "Australia"
    ot[ot.str.contains('austri|autric')] = "Austria"
    ot[ot.str.contains('azer')] = "Azerbaijan"
    ot[ot.str.contains('bangladesh')] = "Bangladesh"
    ot[ot == 'bielorrusia'] = "Belarus"
    ot[ot.str.contains('belgi')] = "Belgium"
    ot[ot.str.contains('belize')] = "Belize"
    ot[ot.str.contains('benin')] = "Benin"
    ot[ot.str.contains('bolivi')] = "Bolivia"
    ot[ot.str.contains('bosni')] = "Bosnia and herzegovina"
    ot[ot.str.contains('brazil|brasil')] = "Brazil"
    ot[ot.str.contains('bulgar')] = "Bulgaria"
    ot[ot.str.contains('burkina')] = "Burkina faso"
    ot[ot.str.contains('burund')] = "Burundi"
    ot[ot.str.contains('cambodg')] = "Cambodia"
    ot[ot.str.contains('camer')] = "Cameroon"
    ot[ot.str.contains('canada|kanada|quebec')] = "Canada"
    ot[ot.str.contains('canad')] = "Cambodia"
    ot[ot.str.contains('chile|chili')] = "Chile"
    ot[ot.str.contains('china|chine')] = "China"
    ot[ot.str.contains('colombi')] = "Columbia"
    ot[ot.str.contains('republique-democratique-du-congo')] = "Democratic republic of the congo"
    ot[ot.str.contains('congo')] = "Republic of the congo"
    ot[ot.str.contains('costa')] = "Costa rica"
    ot[ot.str.contains('ivoir')] = "Cote d ivoire"
    ot[ot.str.contains('croati')] = "Croatia"
    ot[ot.str.contains('cuba')] = "Cuba"
    ot[ot.str.contains('cyprus')] = "Cyprus"
    ot[ot.str.contains('czech')] = "Czech republic"
    ot[ot.str.contains('dominica')] = "Dominican republic"
    ot[ot.str.contains('czech')] = "Czech republic"
    ot[ot.str.contains('ecua')] = "Ecudaor"
    ot[ot.str.contains('egy')] = "Egypt"
    ot[ot.str.contains('england|scotland')] = "United kingdom"
    ot[ot.str.contains('eston')] = "Estonia"
    ot[ot.str.contains('ethiop')] = "Ethiopia"
    ot[ot.str.contains('fidj')] = "Fiji"
    ot[ot.str.contains('finland')] = "Finland"
    ot[ot.str.contains('franc')] = "France"
    ot[ot.str.contains('georgia')] = "Georgia"
    ot[ot.str.contains('germa|allema')] = "Germany"
    ot[ot.str.contains('ghana')] = "Ghana"
    ot[ot.str.contains('gree|grece|grèce|grieche')] = "Greece"
    ot[ot.str.contains('ghana')] = "Ghana"
    ot[ot.str.contains('guatemala')] = "Guatemala"
    ot[ot.str.contains('guyan')] = "Guyana"
    ot[ot.str.contains('hait')] = "Haiti"
    ot[ot.str.contains('honduras')] = "Honduras"
    ot[ot.str.contains('hong-kong')] = "Hong kong"
    ot[ot.str.contains('hunga|hongr')] = "Hungary"
    ot[ot.str.contains('iceland|island')] = "Iceland"
    ot[ot.str.contains('india')] = "India"
    ot[ot.str.contains('indonesi')] = "Indonesia"
    ot[ot == 'iran'] = "Iran"
    ot[ot.str.contains('iraq')] = "Iraq"
    ot[ot.str.contains('ireland')] = "Ireland"
    ot[ot.str.contains('israel')] = "Israel"
    ot[ot.str.contains('italie|italy|italia')] = "Italy"
    ot[ot.str.contains('jamai')] = "Jamaica"
    ot[ot.str.contains('japon|japan')] = "Japan"
    ot[ot.str.contains('jordan')] = "Jordan"
    ot[ot.str.contains('jordan')] = "Jordan"
    ot[ot.str.contains('kazak')] = "Kazakhstan"
    ot[ot.str.contains('keny')] = "Kenya"
    ot[ot.str.contains('laos')] = "Laos"
    ot[ot.str.contains('latvia')] = "Latvia"
    ot[ot.str.contains('lebanon|liban')] = "Lebanon"
    ot[ot.str.contains('lithuania')] = "Lithuania"
    ot[ot.str.contains('luxem')] = "Luxembourg"
    ot[ot.str.contains('madagas')] = "Madagascar"
    ot[ot.str.contains('malawi')] = "Malawi"
    ot[ot.str.contains('malays|malaisie')] = "Malaysia"
    ot[ot.str.contains('maldives')] = "Maldives"
    ot[ot.str.contains('mali')] = "Mali"
    ot[ot.str.contains('gozo')] = "Malta"
    ot[ot.str.contains('mauritius')] = "Mauritius"
    ot[ot.str.contains('mexico|mexique')] = "Mexico"
    ot[ot.str.contains('moldavi')] = "Moldova"
    ot[ot.str.contains('monaco')] = "Monaco"
    ot[ot.str.contains('mongoli')] = "Mongolia"
    ot[ot.str.contains('monteneg')] = "Montenegro"
    ot[ot.str.contains('maroc|morocco')] = "Morocco"
    ot[ot.str.contains('mozambique')] = "Mozambique"
    ot[ot.str.contains('myanmar')] = "Myanmar"
    ot[ot.str.contains('nepal')] = "Nepal"
    ot[ot.str.contains('mozambique')] = "Mozambique"
    ot[ot.str.contains('netherland|pays-bas|holland|pays bas|niederla')] = "Netherlands"
    ot[ot.str.contains('zealand|zeland')] = "New zealand"
    ot[ot.str.contains('nicaragua')] = "Nicaragua"
    ot[ot == 'niger'] = "Niger"
    ot[ot.str.contains('nigeria')] = "Nigeria"
    ot[ot.str.contains('norway|norge|norvege|norvège')] = "Norway"
    ot[ot.str.contains('pakistan')] = "Pakistan"
    ot[ot.str.contains('palestine')] = "Palestinian territories"
    ot[ot.str.contains('panama')] = "Panama"
    ot[ot.str.contains('paraguay')] = "Paraguay"
    ot[ot.str.contains('peru|perou')] = "Peru"
    ot[ot.str.contains('philip')] = "Philippines"
    ot[ot.str.contains('poland|pologn|polen')] = "Poland"
    ot[ot.str.contains('portugal')] = "Portugal"
    ot[ot.str.contains('puerto-rico')] = "Puerto rico"
    ot[ot.str.contains('macedo')] = "Republic of macedonia"
    ot[ot.str.contains('romania|rouman')] = "Romania"
    ot[ot.str.contains('russia|russie|russland')] = "Russia"
    ot[ot.str.contains('rwanda')] = "Rwanda"
    ot[ot.str.contains('arabia')] = "Saudi arabia"
    ot[ot.str.contains('schweiz|switzer|suisse|svizz')] = "Switzerland"
    ot[ot.str.contains('senegal')] = "Senegal"
    ot[ot.str.contains('serbi')] = "Serbia"
    ot[ot.str.contains('singa')] = "Singapore"
    ot[ot.str.contains('slovakia|slovaq')] = "Slovakia"
    ot[ot.str.contains('slove')] = "Slovenia"
    ot[ot.str.contains('south-af|afrique du sud|afrique-du-sud')] = "South africa"
    ot[ot.str.contains('espa|spain')] = "Spain"
    ot[ot.str.contains('lanka')] = "Sri lanka"
    ot[ot.str.contains('sweden|suede|sverg')] = "Sweden"
    ot[ot.str.contains('syrie|syria')] = "Syria"
    ot[ot.str.contains('taiwan')] = "Taiwan"
    ot[ot.str.contains('tanza')] = "Tanzania"
    ot[ot.str.contains('thail|tail')] = "Thailand"
    ot[ot.str.contains('togo')] = "Togo"
    ot[ot.str.contains('tobago')] = "Trinidad and tobago"
    ot[ot.str.contains('tunis')] = "Tunisia"
    ot[ot.str.contains('turk|turq|turc')] = "Turkey"
    ot[ot.str.contains('kingdom')] = "United kingdom"
    ot[ot.str.contains('ukra')] = "Ukraine"
    ot[ot.str.contains('states|usa')] = "United states"
    ot[ot.str.contains('uruguay')] = "Uruguay"
    ot[ot.str.contains('venez|venes')] = "Venezuela"
    ot[ot.str.contains('viet')] = "Vietnam"
    return ot
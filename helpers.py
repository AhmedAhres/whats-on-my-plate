def clean_coutries_tags(df):
    ct = df['countries_tags'].astype(str)
    
    ct = ct.str.split(':').str.get(1)

    # We capitalize the first letter
    ct = ct.str.capitalize()

    # Some results are United-states, we remove the "-" for better readability
    ct = ct.str.replace("-", " ")
    ct = ct.str.replace(",en", "")
    ct = ct.str.replace(",fr", "")
    ct = ct.str.replace(",de", "")
    ct = ct.str.replace(",ch", "")
    ct = ct.str.replace(",it", "")
    ct = ct.str.replace(",sq", "")
    ct = ct.str.replace(",es", "")

    # We also replace the values representing the same country to the country that is represented
    ct = ct.str.replace("Suisse", "Switzerland")

    ct = ct.str.replace("French polynesia", "France")
    ct = ct.str.replace("French guiana", "France")
    ct = ct.str.replace("Martinique", "France")
    ct = ct.str.replace("Guadeloupe", "France")
    ct = ct.str.replace("New caledonia", "France")
    ct = ct.str.replace("Reunion", "France")
    ct = ct.str.replace("Frankreich", "France")
    ct = ct.str.replace("Frankrike", "France")

    ct = ct.str.replace("Deutschland", "Germany")
    ct = ct.str.replace("Allemagne", "Germany")
    ct = ct.astype(str)
    
    ct[ct.str.contains('Albania,sq')] = 'Albania'
    ct[ct.str.contains('Algerie')] = 'Algeria'
    ct[ct.str.contains('Belgie|Belgique')] = 'Belgium'
    ct[ct.str.contains('Comercial mexicana')] = 'Comercial mexicana'
    ct[ct.str.contains('England|Scotland|U k')] = 'United kingdom'
    ct[ct.str.contains('Franca|France,be|France,ca|France,es|Frankrijk|Franța')] = 'France'
    ct[ct.str.contains('Germany,zu')] = 'Germany'
    ct[ct.str.contains('Hungary,hu')] = 'Hungary'
    ct[ct.str.contains('Mexico,es')] = 'Mexico'
    ct[ct.str.contains('Hungary,hu')] = 'Hungary'
    ct[ct.str.contains('Nerderland')] = 'Netherlands'
    ct[ct.str.contains('Spain,es')] = 'Spain'
    ct[ct.str.contains('Portugal,es')] = 'Portugal'
    ct[ct.str.contains('Danemark')] = 'Denmark'
    
    
    
    return ct


def clean_origins_tags(df):
    ot = df['origins_tags'].astype(str)
    ot[ot.str.contains('algeri')] = "Algeria"
    ot[ot.str.contains('armeni')] = "Armenia"
    ot[ot.str.contains('argenti')] = "Argentina"
    ot[ot.str.contains('australi|australa')] = "Australia"
    ot[ot.str.contains('austri|autric|osterreich')] = "Austria"
    ot[ot.str.contains('azer')] = "Azerbaijan"
    ot[ot.str.contains('bangladesh')] = "Bangladesh"
    ot[ot == 'bielorrusia'] = "Belarus"
    ot[ot.str.contains('belgi')] = "Belgium"
    ot[ot.str.contains('belize')] = "Belize"
    ot[ot.str.contains('benin')] = "Benin"
    ot[ot.str.contains('bolivi')] = "Bolivia"
    ot[ot.str.contains('bosni')] = "Bosnia and herzegovina"
    ot[ot.str.contains('brazil|brasil|bresil')] = "Brazil"
    ot[ot.str.contains('bulgar')] = "Bulgaria"
    ot[ot.str.contains('burkina')] = "Burkina faso"
    ot[ot.str.contains('burund')] = "Burundi"
    ot[ot.str.contains('cambodg')] = "Cambodia"
    ot[ot.str.contains('camer')] = "Cameroon"
    ot[ot.str.contains('canada|kanada|quebec|montreal')] = "Canada"
    ot[ot.str.contains('canad')] = "Cambodia"
    ot[ot.str.contains('chile|chili')] = "Chile"
    ot[ot.str.contains('china|chine')] = "China"
    ot[ot.str.contains('colombi')] = "Columbia"
    ot[ot.str.contains('kore|corea|coré')] = "South korea"
    ot[ot.str.contains('republique-democratique-du-congo')] = "Democratic republic of the congo"
    ot[ot.str.contains('congo')] = "Republic of the congo"
    ot[ot.str.contains('costa')] = "Costa rica"
    ot[ot.str.contains('ivoir')] = "Cote d ivoire"
    ot[ot.str.contains('croati')] = "Croatia"
    ot[ot.str.contains('cuba')] = "Cuba"
    ot[ot.str.contains('cyprus')] = "Cyprus"
    ot[ot.str.contains('czech|repubblica-ceca|česko')] = "Czech republic"
    ot[ot.str.contains('dominica')] = "Dominican republic"
    ot[ot.str.contains('denmar|danemar|dinamarca|danmark')] = "Denmark"
    ot[ot.str.contains('czech|cehia')] = "Czech republic"
    ot[ot.str.contains('ecua|equateur')] = "Ecudaor"
    ot[ot.str.contains('egy|egipto')] = "Egypt"
    ot[ot.str.contains('england|scotland')] = "United kingdom"
    ot[ot.str.contains('eston')] = "Estonia"
    ot[ot.str.contains('ethiop')] = "Ethiopia"
    ot[ot.str.contains('equateur')] = "Equador"
    ot[ot.str.contains('fidj')] = "Fiji"
    ot[ot.str.contains('finland')] = "Finland"
    ot[ot.str.contains('franc|frankreich|martinique|frankrijk')] = "France"
    ot[ot.str.contains('georgia')] = "Georgia"
    ot[ot.str.contains('germa|allema|deutschland|bayern|alemania|eutschland')] = "Germany"
    ot[ot.str.contains('ghana')] = "Ghana"
    ot[ot.str.contains('gree|grece|grèce|grieche|grecia')] = "Greece"
    ot[ot.str.contains('ghana')] = "Ghana"
    ot[ot.str.contains('guatemala')] = "Guatemala"
    ot[ot.str.contains('guyan')] = "Guyana"
    ot[ot.str.contains('hait')] = "Haiti"
    ot[ot.str.contains('honduras')] = "Honduras"
    ot[ot.str.contains('hong-kong')] = "Hong kong"
    ot[ot.str.contains('hunga|hongr|ungaria|hungria')] = "Hungary"
    ot[ot.str.contains('iceland|island')] = "Iceland"
    ot[ot.str.contains('india')] = "India"
    ot[ot == 'inde'] = "India"
    ot[ot.str.contains('indonesi')] = "Indonesia"
    ot[ot == 'iran'] = "Iran"
    ot[ot.str.contains('iraq')] = "Iraq"
    ot[ot.str.contains('ireland|irland')] = "Ireland"
    ot[ot.str.contains('israel')] = "Israel"
    ot[ot.str.contains('italie|italy|italia')] = "Italy"
    ot[ot.str.contains('jamai')] = "Jamaica"
    ot[ot.str.contains('japon|japan')] = "Japan"
    ot[ot.str.contains('jordan')] = "Jordan"
    ot[ot.str.contains('jordan')] = "Jordan"
    ot[ot.str.contains('kazak')] = "Kazakhstan"
    ot[ot.str.contains('keny|kenia')] = "Kenya"
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
    ot[ot.str.contains('mexico|mexique|nuevo-leon')] = "Mexico"
    ot[ot.str.contains('moldavi')] = "Moldova"
    ot[ot.str.contains('monaco')] = "Monaco"
    ot[ot.str.contains('mongoli')] = "Mongolia"
    ot[ot.str.contains('monteneg')] = "Montenegro"
    ot[ot.str.contains('maroc|morocco')] = "Morocco"
    ot[ot.str.contains('mozambique')] = "Mozambique"
    ot[ot.str.contains('myanmar')] = "Myanmar"
    ot[ot.str.contains('nepal')] = "Nepal"
    ot[ot.str.contains('mozambique')] = "Mozambique"
    ot[ot.str.contains('netherland|pays-bas|holland|pays bas|niederla|nederland|holanda')] = "Netherlands"
    ot[ot.str.contains('zealand|zeland')] = "New zealand"
    ot[ot.str.contains('nicaragua')] = "Nicaragua"
    ot[ot == 'niger'] = "Niger"
    ot[ot.str.contains('nigeria')] = "Nigeria"
    ot[ot.str.contains('norway|norge|norvege|norvège|norwegen|norvegia')] = "Norway"
    ot[ot.str.contains('pakistan')] = "Pakistan"
    ot[ot.str.contains('palestine')] = "Palestinian territories"
    ot[ot.str.contains('panama')] = "Panama"
    ot[ot.str.contains('paraguay')] = "Paraguay"
    ot[ot.str.contains('peru|perou')] = "Peru"
    ot[ot.str.contains('philip|filipinas')] = "Philippines"
    ot[ot.str.contains('poland|pologn|polen|polonia')] = "Poland"
    ot[ot.str.contains('portugal')] = "Portugal"
    ot[ot.str.contains('puerto-rico')] = "Puerto rico"
    ot[ot.str.contains('macedo')] = "Republic of macedonia"
    ot[ot.str.contains('romania|rouman')] = "Romania"
    ot[ot.str.contains('russia|russie|russland')] = "Russia"
    ot[ot.str.contains('rwanda')] = "Rwanda"
    ot[ot.str.contains('arabia')] = "Saudi arabia"
    ot[ot.str.contains('schweiz|switzer|suisse|svizz|suiza')] = "Switzerland"
    ot[ot.str.contains('senegal')] = "Senegal"
    ot[ot.str.contains('serbi')] = "Serbia"
    ot[ot.str.contains('singa')] = "Singapore"
    ot[ot.str.contains('slovakia|slovaq|slovacia')] = "Slovakia"
    ot[ot.str.contains('slove')] = "Slovenia"
    ot[ot.str.contains('south-af|afrique du sud|afrique-du-sud|sudafrica|sudafrika')] = "South africa"
    ot[ot.str.contains('espa|spain|spanien|spagna')] = "Spain"
    ot[ot.str.contains('lanka')] = "Sri lanka"
    ot[ot.str.contains('sweden|suede|sverg')] = "Sweden"
    ot[ot.str.contains('syrie|syria')] = "Syria"
    ot[ot.str.contains('taiwan')] = "Taiwan"
    ot[ot.str.contains('tanza')] = "Tanzania"
    ot[ot.str.contains('thail|tail|thajsko')] = "Thailand"
    ot[ot.str.contains('togo')] = "Togo"
    ot[ot.str.contains('tobago')] = "Trinidad and tobago"
    ot[ot.str.contains('tunis')] = "Tunisia"
    ot[ot.str.contains('turk|turq|turc')] = "Turkey"
    ot[ot.str.contains('kingdom|ecosse|great-britain|royaume-uni')] = "United kingdom"
    ot[ot == 'uk'] = "United kingdom"
    ot[ot.str.contains('ukra|ucraina')] = "Ukraine"
    ot[ot.str.contains('states|usa|estados-unidos|e-u-a|etats-unis|eua|estado-unidos|schottland')] = "United states"
    ot[ot.str.contains('uruguay')] = "Uruguay"
    ot[ot.str.contains('uganda')] = "Uganda"
    ot[ot.str.contains('venez|venes')] = "Venezuela"
    ot[ot.str.contains('viet')] = "Vietnam"
    ot[ot.str.contains('unione-europea|agricultura|agriculture|union-europea|europe')] = "European union"
    ot[ot == 'eu'] = "European union"
    ot[ot == 'ue'] = "European union"
    ot[ot == 'union-europeenne'] = "European union"
    ot[ot == 'eu-landwirtschaft'] = "European union"
    return ot
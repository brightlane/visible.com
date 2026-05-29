#!/usr/bin/env python3
"""
Visible.com USA Affiliate Site
Site: https://brightlane.github.io/visible.com/
Affiliate: https://convert.ctypy.com/aff_c?offer_id=29563&aff_id=21885
13,500+ pages targeting Visible wireless plans — unlimited 5G, prepaid,
Verizon alternative, no contract — USA only.
Run: python3 build.py
"""

import os, sys, subprocess, datetime, hashlib

now      = datetime.datetime.utcnow()
DATE_STR = now.strftime("%Y-%m-%d")
SYNC     = hashlib.md5(DATE_STR.encode()).hexdigest()[:8]
BASE_URL = "https://brightlane.github.io/visible.com/"
AFF      = "https://convert.ctypy.com/aff_c?offer_id=29563&aff_id=21885"
YEAR     = now.year

# ── STATES ────────────────────────────────────────────────────────────────────
STATES = [
    ("alabama","Alabama","AL"),("alaska","Alaska","AK"),("arizona","Arizona","AZ"),
    ("arkansas","Arkansas","AR"),("california","California","CA"),("colorado","Colorado","CO"),
    ("connecticut","Connecticut","CT"),("delaware","Delaware","DE"),("florida","Florida","FL"),
    ("georgia","Georgia","GA"),("hawaii","Hawaii","HI"),("idaho","Idaho","ID"),
    ("illinois","Illinois","IL"),("indiana","Indiana","IN"),("iowa","Iowa","IA"),
    ("kansas","Kansas","KS"),("kentucky","Kentucky","KY"),("louisiana","Louisiana","LA"),
    ("maine","Maine","ME"),("maryland","Maryland","MD"),("massachusetts","Massachusetts","MA"),
    ("michigan","Michigan","MI"),("minnesota","Minnesota","MN"),("mississippi","Mississippi","MS"),
    ("missouri","Missouri","MO"),("montana","Montana","MT"),("nebraska","Nebraska","NE"),
    ("nevada","Nevada","NV"),("new-hampshire","New Hampshire","NH"),("new-jersey","New Jersey","NJ"),
    ("new-mexico","New Mexico","NM"),("new-york","New York","NY"),("north-carolina","North Carolina","NC"),
    ("north-dakota","North Dakota","ND"),("ohio","Ohio","OH"),("oklahoma","Oklahoma","OK"),
    ("oregon","Oregon","OR"),("pennsylvania","Pennsylvania","PA"),("rhode-island","Rhode Island","RI"),
    ("south-carolina","South Carolina","SC"),("south-dakota","South Dakota","SD"),
    ("tennessee","Tennessee","TN"),("texas","Texas","TX"),("utah","Utah","UT"),
    ("vermont","Vermont","VT"),("virginia","Virginia","VA"),("washington","Washington","WA"),
    ("west-virginia","West Virginia","WV"),("wisconsin","Wisconsin","WI"),("wyoming","Wyoming","WY"),
]

# ── CITIES ────────────────────────────────────────────────────────────────────
CITIES = [
    ("new-york-ny","New York","NY"),("los-angeles-ca","Los Angeles","CA"),
    ("chicago-il","Chicago","IL"),("houston-tx","Houston","TX"),("phoenix-az","Phoenix","AZ"),
    ("philadelphia-pa","Philadelphia","PA"),("san-antonio-tx","San Antonio","TX"),
    ("san-diego-ca","San Diego","CA"),("dallas-tx","Dallas","TX"),("san-jose-ca","San Jose","CA"),
    ("austin-tx","Austin","TX"),("jacksonville-fl","Jacksonville","FL"),("fort-worth-tx","Fort Worth","TX"),
    ("columbus-oh","Columbus","OH"),("charlotte-nc","Charlotte","NC"),("indianapolis-in","Indianapolis","IN"),
    ("san-francisco-ca","San Francisco","CA"),("seattle-wa","Seattle","WA"),("denver-co","Denver","CO"),
    ("nashville-tn","Nashville","TN"),("oklahoma-city-ok","Oklahoma City","OK"),
    ("washington-dc","Washington DC","DC"),("boston-ma","Boston","MA"),("las-vegas-nv","Las Vegas","NV"),
    ("memphis-tn","Memphis","TN"),("louisville-ky","Louisville","KY"),("portland-or","Portland","OR"),
    ("baltimore-md","Baltimore","MD"),("milwaukee-wi","Milwaukee","WI"),("albuquerque-nm","Albuquerque","NM"),
    ("tucson-az","Tucson","AZ"),("fresno-ca","Fresno","CA"),("mesa-az","Mesa","AZ"),
    ("sacramento-ca","Sacramento","CA"),("atlanta-ga","Atlanta","GA"),("kansas-city-mo","Kansas City","MO"),
    ("omaha-ne","Omaha","NE"),("colorado-springs-co","Colorado Springs","CO"),("raleigh-nc","Raleigh","NC"),
    ("long-beach-ca","Long Beach","CA"),("virginia-beach-va","Virginia Beach","VA"),
    ("minneapolis-mn","Minneapolis","MN"),("tampa-fl","Tampa","FL"),("new-orleans-la","New Orleans","LA"),
    ("arlington-tx","Arlington","TX"),("bakersfield-ca","Bakersfield","CA"),("anaheim-ca","Anaheim","CA"),
    ("aurora-co","Aurora","CO"),("corpus-christi-tx","Corpus Christi","TX"),
    ("riverside-ca","Riverside","CA"),("st-louis-mo","St. Louis","MO"),("lexington-ky","Lexington","KY"),
    ("pittsburgh-pa","Pittsburgh","PA"),("stockton-ca","Stockton","CA"),("anchorage-ak","Anchorage","AK"),
    ("cincinnati-oh","Cincinnati","OH"),("st-paul-mn","St. Paul","MN"),("toledo-oh","Toledo","OH"),
    ("greensboro-nc","Greensboro","NC"),("newark-nj","Newark","NJ"),("plano-tx","Plano","TX"),
    ("henderson-nv","Henderson","NV"),("lincoln-ne","Lincoln","NE"),("buffalo-ny","Buffalo","NY"),
    ("fort-wayne-in","Fort Wayne","IN"),("orlando-fl","Orlando","FL"),("norfolk-va","Norfolk","VA"),
    ("chandler-az","Chandler","AZ"),("laredo-tx","Laredo","TX"),("madison-wi","Madison","WI"),
    ("durham-nc","Durham","NC"),("lubbock-tx","Lubbock","TX"),("winston-salem-nc","Winston-Salem","NC"),
    ("garland-tx","Garland","TX"),("glendale-az","Glendale","AZ"),("hialeah-fl","Hialeah","FL"),
    ("reno-nv","Reno","NV"),("baton-rouge-la","Baton Rouge","LA"),("irvine-ca","Irvine","CA"),
    ("chesapeake-va","Chesapeake","VA"),("irving-tx","Irving","TX"),("scottsdale-az","Scottsdale","AZ"),
    ("fremont-ca","Fremont","CA"),("gilbert-az","Gilbert","AZ"),("birmingham-al","Birmingham","AL"),
    ("boise-id","Boise","ID"),("rochester-ny","Rochester","NY"),("richmond-va","Richmond","VA"),
    ("spokane-wa","Spokane","WA"),("des-moines-ia","Des Moines","IA"),("montgomery-al","Montgomery","AL"),
    ("modesto-ca","Modesto","CA"),("tacoma-wa","Tacoma","WA"),("akron-oh","Akron","OH"),
    ("yonkers-ny","Yonkers","NY"),("knoxville-tn","Knoxville","TN"),("mobile-al","Mobile","AL"),
    ("huntington-beach-ca","Huntington Beach","CA"),("amarillo-tx","Amarillo","TX"),
    ("little-rock-ar","Little Rock","AR"),("salt-lake-city-ut","Salt Lake City","UT"),
    ("grand-rapids-mi","Grand Rapids","MI"),("tallahassee-fl","Tallahassee","FL"),
    ("huntsville-al","Huntsville","AL"),("worcester-ma","Worcester","MA"),
    ("cape-coral-fl","Cape Coral","FL"),("rockford-il","Rockford","IL"),
    ("providence-ri","Providence","RI"),("clarksville-tn","Clarksville","TN"),
    ("fort-collins-co","Fort Collins","CO"),("jackson-ms","Jackson","MS"),
    ("springfield-mo","Springfield","MO"),("palmdale-ca","Palmdale","CA"),
    ("savannah-ga","Savannah","GA"),("surprise-az","Surprise","AZ"),
    ("killeen-tx","Killeen","TX"),("syracuse-ny","Syracuse","NY"),("dayton-oh","Dayton","OH"),
    ("mcallen-tx","McAllen","TX"),("cary-nc","Cary","NC"),("bridgeport-ct","Bridgeport","CT"),
    ("cedar-rapids-ia","Cedar Rapids","IA"),("new-haven-ct","New Haven","CT"),
    ("columbia-sc","Columbia","SC"),("murfreesboro-tn","Murfreesboro","TN"),
    ("hartford-ct","Hartford","CT"),("visalia-ca","Visalia","CA"),("rochester-mn","Rochester","MN"),
    ("denton-tx","Denton","TX"),("wichita-ks","Wichita","KS"),("lewisville-tx","Lewisville","TX"),
    ("columbia-mo","Columbia","MO"),("midland-tx","Midland","TX"),("lowell-ma","Lowell","MA"),
    ("ann-arbor-mi","Ann Arbor","MI"),("provo-ut","Provo","UT"),("lansing-mi","Lansing","MI"),
    ("abilene-tx","Abilene","TX"),("beaumont-tx","Beaumont","TX"),("manchester-nh","Manchester","NH"),
    ("fargo-nd","Fargo","ND"),("palm-bay-fl","Palm Bay","FL"),("sioux-falls-sd","Sioux Falls","SD"),
    ("west-palm-beach-fl","West Palm Beach","FL"),("waco-tx","Waco","TX"),
    ("santa-clarita-ca","Santa Clarita","CA"),("stamford-ct","Stamford","CT"),
    ("allentown-pa","Allentown","PA"),("thornton-co","Thornton","CO"),("elgin-il","Elgin","IL"),
    ("lakewood-co","Lakewood","CO"),("roseville-ca","Roseville","CA"),
    ("hollywood-fl","Hollywood","FL"),("brownsville-tx","Brownsville","TX"),
    ("bellevue-wa","Bellevue","WA"),("chattanooga-tn","Chattanooga","TN"),
    ("alexandria-va","Alexandria","VA"),("fort-lauderdale-fl","Fort Lauderdale","FL"),
    ("springfield-il","Springfield","IL"),("mckinney-tx","McKinney","TX"),
    ("frisco-tx","Frisco","TX"),("downey-ca","Downey","CA"),("green-bay-wi","Green Bay","WI"),
    ("joliet-il","Joliet","IL"),("burbank-ca","Burbank","CA"),("antioch-ca","Antioch","CA"),
    ("temecula-ca","Temecula","CA"),("evansville-in","Evansville","IN"),
    ("billings-mt","Billings","MT"),("topeka-ks","Topeka","KS"),("broken-arrow-ok","Broken Arrow","OK"),
    ("cambridge-ma","Cambridge","MA"),("sandy-ut","Sandy","UT"),("carrollton-tx","Carrollton","TX"),
    ("centennial-co","Centennial","CO"),("lakeland-fl","Lakeland","FL"),
    ("pompano-beach-fl","Pompano Beach","FL"),("tuscaloosa-al","Tuscaloosa","AL"),
    ("eugene-or","Eugene","OR"),("south-bend-in","South Bend","IN"),
    ("berkeley-ca","Berkeley","CA"),("flint-mi","Flint","MI"),("meridian-id","Meridian","ID"),
    ("las-cruces-nm","Las Cruces","NM"),("gainesville-fl","Gainesville","FL"),
    ("peoria-il","Peoria","IL"),("tempe-az","Tempe","AZ"),("miramar-fl","Miramar","FL"),
    ("pembroke-pines-fl","Pembroke Pines","FL"),("santa-rosa-ca","Santa Rosa","CA"),
    ("elk-grove-ca","Elk Grove","CA"),("hayward-ca","Hayward","CA"),("salinas-ca","Salinas","CA"),
    ("pomona-ca","Pomona","CA"),("escondido-ca","Escondido","CA"),
    ("garden-grove-ca","Garden Grove","CA"),("ontario-ca","Ontario","CA"),
    ("paterson-nj","Paterson","NJ"),("macon-ga","Macon","GA"),
    ("glendale-ca","Glendale","CA"),("moreno-valley-ca","Moreno Valley","CA"),
    ("fontana-ca","Fontana","CA"),("north-las-vegas-nv","North Las Vegas","NV"),
    ("north-charleston-sc","North Charleston","SC"),("rancho-cucamonga-ca","Rancho Cucamonga","CA"),
    ("oceanside-ca","Oceanside","CA"),("santa-ana-ca","Santa Ana","CA"),
    ("murrieta-ca","Murrieta","CA"),("west-jordan-ut","West Jordan","UT"),
    ("fullerton-ca","Fullerton","CA"),("orange-ca","Orange","CA"),
    ("hampton-va","Hampton","VA"),("peoria-az","Peoria","AZ"),("warren-mi","Warren","MI"),
    ("west-valley-city-ut","West Valley City","UT"),("olathe-ks","Olathe","KS"),
    ("high-point-nc","High Point","NC"),("inglewood-ca","Inglewood","CA"),
    ("west-covina-ca","West Covina","CA"),("norwalk-ca","Norwalk","CA"),
    ("arvada-co","Arvada","CO"),("round-rock-tx","Round Rock","TX"),
    ("thousand-oaks-ca","Thousand Oaks","CA"),("clearwater-fl","Clearwater","FL"),
    ("simi-valley-ca","Simi Valley","CA"),("erie-pa","Erie","PA"),("athens-ga","Athens","GA"),
    ("waterbury-ct","Waterbury","CT"),("fairfield-ca","Fairfield","CA"),("kent-wa","Kent","WA"),
    ("sterling-heights-mi","Sterling Heights","MI"),("pueblo-co","Pueblo","CO"),
    ("santa-maria-ca","Santa Maria","CA"),("palm-springs-ca","Palm Springs","CA"),
    ("san-mateo-ca","San Mateo","CA"),("beaumont-ca","Beaumont","CA"),
    ("fayetteville-ar","Fayetteville","AR"),("concord-nc","Concord","NC"),
    ("columbia-sc-2","Columbia","SC"),("sandy-springs-ga","Sandy Springs","GA"),
    ("port-st-lucie-fl","Port St. Lucie","FL"),("coral-springs-fl","Coral Springs","FL"),
    ("odessa-tx","Odessa","TX"),("tyler-tx","Tyler","TX"),
    ("pearland-tx","Pearland","TX"),("sugar-land-tx","Sugar Land","TX"),
    ("league-city-tx","League City","TX"),("allen-tx","Allen","TX"),
    ("edinburg-tx","Edinburg","TX"),("mission-tx","Mission","TX"),
    ("san-angelo-tx","San Angelo","TX"),("longview-tx","Longview","TX"),
    ("richardson-tx","Richardson","TX"),("grand-prairie-tx","Grand Prairie","TX"),
    ("pasadena-tx","Pasadena","TX"),("mesquite-tx","Mesquite","TX"),
    ("new-braunfels-tx","New Braunfels","TX"),("lakewood-ca","Lakewood","CA"),
    ("costa-mesa-ca","Costa Mesa","CA"),("west-haven-ct","West Haven","CT"),
    ("columbia-md","Columbia","MD"),("norwalk-ct","Norwalk","CT"),
    ("billings-mt-2","Billings","MT"),("nashua-nh","Nashua","NH"),
    ("peoria-il-2","Peoria","IL"),("rochester-hills-mi","Rochester Hills","MI"),
    ("clinton-township-mi","Clinton Township","MI"),("wichita-falls-tx","Wichita Falls","TX"),
    ("west-palm-beach-fl-2","West Palm Beach","FL"),("cape-girardeau-mo","Cape Girardeau","MO"),
]

# dedup
seen_c = set()
CITIES_DEDUP = []
for c in CITIES:
    if c[0] not in seen_c:
        seen_c.add(c[0])
        CITIES_DEDUP.append(c)
CITIES = CITIES_DEDUP

# ── STATE INTENTS (40) ────────────────────────────────────────────────────────
STATE_INTENTS = [
    ("unlimited-plan","unlimited phone plan","best unlimited phone plan"),
    ("5g-coverage","5G coverage","Visible 5G coverage"),
    ("prepaid-plan","prepaid phone plan","best prepaid phone plan"),
    ("cheap-phone-plan","cheap phone plan","cheapest phone plan"),
    ("no-contract-plan","no contract phone plan","phone plan no contract"),
    ("verizon-alternative","Verizon alternative","best Verizon alternative"),
    ("unlimited-data","unlimited data plan","unlimited data phone plan"),
    ("mobile-hotspot","mobile hotspot plan","phone plan with hotspot"),
    ("family-plan","family phone plan","best family phone plan"),
    ("20-dollar-plan","$20 phone plan","phone plan for $20 a month"),
    ("best-phone-plan","best phone plan","best phone plan 2026"),
    ("affordable-phone-plan","affordable phone plan","most affordable phone plan"),
    ("unlimited-talk-text","unlimited talk and text","unlimited talk text data plan"),
    ("visible-review","Visible review","Visible wireless review"),
    ("visible-vs-att","Visible vs AT&T","Visible versus AT&T"),
    ("visible-vs-tmobile","Visible vs T-Mobile","Visible versus T-Mobile"),
    ("visible-vs-cricket","Visible vs Cricket","Visible versus Cricket Wireless"),
    ("visible-vs-mint","Visible vs Mint Mobile","Visible versus Mint Mobile"),
    ("visible-vs-metro","Visible vs Metro by T-Mobile","Visible versus Metro"),
    ("visible-coverage","Visible coverage","Visible wireless coverage"),
    ("visible-cost","Visible cost","how much does Visible cost"),
    ("visible-discount","Visible discount","Visible promo code"),
    ("visible-hotspot","Visible hotspot","Visible mobile hotspot speed"),
    ("visible-plus","Visible Plus plan","Visible Plus plan review"),
    ("budget-phone-plan","budget phone plan","cheapest budget phone plan"),
    ("phone-plan-seniors","phone plan for seniors","best phone plan seniors"),
    ("phone-plan-students","phone plan for students","best phone plan college"),
    ("byod-plan","bring your own device plan","BYOD phone plan"),
    ("esim-plan","eSIM phone plan","eSIM no contract plan"),
    ("single-line-plan","single line phone plan","best single line plan"),
    ("data-only-plan","data only plan","data only SIM plan"),
    ("wifi-calling","WiFi calling phone plan","phone plan WiFi calling"),
    ("unlimited-international","unlimited international calls","international phone plan"),
    ("roaming-plan","roaming phone plan","phone plan with roaming"),
    ("phone-plan-military","phone plan military","military phone discount"),
    ("phone-plan-no-credit","phone plan no credit check","no credit check phone plan"),
    ("verizon-network-plan","Verizon network phone plan","phone plan on Verizon network"),
    ("best-coverage-plan","best coverage phone plan","phone plan best coverage"),
    ("visible-app","Visible app","Visible wireless app"),
    ("switch-to-visible","switch to Visible","how to switch to Visible wireless"),
]

# ── PLANS (15) ────────────────────────────────────────────────────────────────
PLANS = [
    ("unlimited","Unlimited Plan","$20/mo unlimited data","unlimited 5G talk text data","📱",
     "Visible's base unlimited plan starts at just $20/month with unlimited data, talk, text, and mobile hotspot on Verizon's 5G network. No contracts, no hidden fees.",
     ["What does Visible's unlimited plan include?","Is Visible really unlimited?","How much does Visible cost per month?","Can I stream video on Visible?","Does Visible have data caps?"]),
    ("visible-plus","Visible+","premium unlimited plan","Visible Plus premium 5G plan","⭐",
     "Visible+ is the premium tier offering priority data, international perks, and premium 5G (including 5G Ultra Wideband in select areas). Ideal for heavy data users and travelers.",
     ["What is Visible Plus?","How much does Visible Plus cost?","Is Visible Plus worth it?","What's the difference between Visible and Visible+?","Does Visible Plus include international?"]),
    ("family-plan","Party Pay","family group savings","Visible Party Pay family savings","👨‍👩‍👧‍👦",
     "Visible's Party Pay lets you join a group of up to 4 people to lower your monthly rate. The more people in your party, the less you pay — all the way down to $20/month.",
     ["How does Visible Party Pay work?","Can I join a stranger's party on Visible?","How many people can be in a Visible party?","Does Party Pay require a family contract?","Is Party Pay better than a family plan?"]),
    ("hotspot","Mobile Hotspot","unlimited hotspot plan","mobile hotspot unlimited data","📶",
     "Every Visible plan includes unlimited mobile hotspot data. Use your phone as a WiFi hotspot for laptops, tablets, and other devices at no extra charge.",
     ["Does Visible include hotspot?","How fast is Visible hotspot?","Can I use Visible hotspot for streaming?","Is there a hotspot data cap on Visible?","How to set up Visible hotspot?"]),
    ("5g","5G Plan","5G unlimited data","Verizon 5G network plan","5️⃣",
     "Visible runs on Verizon's 5G and 4G LTE networks — one of the most expansive in the US. Get fast 5G speeds in thousands of cities and 4G LTE everywhere else.",
     ["Does Visible have 5G?","Where is Visible 5G available?","Is Visible 5G fast?","Visible 5G vs T-Mobile 5G","What network does Visible use?"]),
    ("prepaid","Prepaid Plan","no contract prepaid","prepaid wireless no contract","💳",
     "Visible is 100% prepaid — no annual contracts, no credit checks, and no surprise bills. Pay month-to-month and cancel anytime with no penalty.",
     ["Is Visible a prepaid plan?","Does Visible require a credit check?","Can I cancel Visible anytime?","How does Visible billing work?","Is Visible prepaid good?"]),
    ("byod","Bring Your Own Device","BYOD compatible phones","bring your own phone to Visible","📲",
     "Bring your existing phone to Visible and keep your number. Visible is compatible with most unlocked iPhones and Android devices. Check compatibility and activate online in minutes.",
     ["Can I bring my own phone to Visible?","Is my phone compatible with Visible?","How to bring your own device to Visible?","Does Visible support iPhone?","Does Visible support Samsung Galaxy?"]),
    ("esim","eSIM Plan","eSIM activation","Visible eSIM no physical SIM","🔌",
     "Visible supports eSIM activation — no physical SIM card needed. Activate your service instantly from your phone without waiting for a SIM in the mail.",
     ["Does Visible offer eSIM?","How to activate Visible eSIM?","Is Visible eSIM fast to set up?","Which phones support Visible eSIM?","eSIM vs physical SIM Visible"]),
    ("single-line","Single Line Plan","one person phone plan","best single line phone plan","👤",
     "Visible's single-line plan is perfect for individuals who want unlimited data without paying for multiple lines. Starting at $20/month with no contracts.",
     ["Is Visible good for a single line?","Best single line plan 2026","Visible vs other single line plans","How much is one line on Visible?","Can I add more lines later on Visible?"]),
    ("unlimited-data","Unlimited Data","unlimited data no throttling","truly unlimited data plan","♾️",
     "Visible offers truly unlimited data — no data caps, no overage charges. Your data may be deprioritized during network congestion, but you'll never be cut off.",
     ["Is Visible data actually unlimited?","Does Visible throttle data?","Visible unlimited data speed","Visible vs Verizon unlimited","Can I use unlimited data for streaming?"]),
    ("cheap","Cheapest Phone Plan","$20 phone plan","cheapest unlimited phone plan 2026","💰",
     "At $20/month, Visible is one of the cheapest unlimited phone plans in the USA. Get unlimited data, talk, text, and hotspot at a price that beats most competitors.",
     ["What is the cheapest phone plan in the US?","Is Visible the cheapest unlimited plan?","Visible $20 plan review","Cheapest plans with unlimited data","Visible vs Mint Mobile price"]),
    ("seniors","Senior Phone Plan","phone plan for seniors","best phone plan for seniors 2026","👴",
     "Visible is an excellent choice for seniors — simple online management, no contracts, affordable pricing, and Verizon's reliable network coverage across the USA.",
     ["Is Visible good for seniors?","Best phone plans for seniors 2026","Does Visible have a senior discount?","Is Visible easy to use for seniors?","Visible vs Consumer Cellular for seniors"]),
    ("students","Student Phone Plan","college student phone plan","best phone plan for college students","🎓",
     "Students love Visible for its low monthly cost, no contracts, and Verizon network reliability. Party Pay can lower your bill even further when shared with classmates.",
     ["Is Visible good for students?","Best phone plans for college 2026","Does Visible have a student discount?","Visible vs Boost Mobile for students","How students save with Visible Party Pay"]),
    ("military","Military Phone Plan","military phone discount","phone plan for military veterans","🎖️",
     "Visible is a great option for active military and veterans — affordable, reliable, and on Verizon's network. No contracts make it ideal for those who move frequently.",
     ["Does Visible have military discounts?","Best phone plans for military 2026","Visible vs Verizon military plan","Is Visible good for veterans?","Phone plan military no contract"]),
    ("international","International Plan","international calls included","phone plan international roaming","🌍",
     "Visible+ includes international calling to Mexico and Canada and global text. For travelers and those with family abroad, Visible+ provides significant international value.",
     ["Does Visible include international calls?","Visible international calling","Does Visible work in Mexico?","Visible vs Google Fi international","Visible+ international features"]),
]

# ── COMPETITORS (20) ──────────────────────────────────────────────────────────
COMPETITORS = [
    ("att","AT&T","AT&T","major carrier"),
    ("tmobile","T-Mobile","T-Mobile","major carrier"),
    ("verizon","Verizon","Verizon","parent network"),
    ("cricket","Cricket Wireless","Cricket","AT&T prepaid brand"),
    ("mint","Mint Mobile","Mint Mobile","T-Mobile prepaid"),
    ("metro","Metro by T-Mobile","Metro","T-Mobile prepaid brand"),
    ("boost","Boost Mobile","Boost","Dish prepaid carrier"),
    ("consumer-cellular","Consumer Cellular","Consumer Cellular","AARP senior carrier"),
    ("straight-talk","Straight Talk","Straight Talk","Walmart prepaid"),
    ("total-wireless","Total Wireless","Total Wireless","Verizon prepaid"),
    ("simple-mobile","Simple Mobile","Simple Mobile","T-Mobile MVNO"),
    ("tracfone","TracFone","TracFone","multi-network prepaid"),
    ("google-fi","Google Fi","Google Fi","Google MVNO"),
    ("us-mobile","US Mobile","US Mobile","flexible MVNO"),
    ("tello","Tello Mobile","Tello","T-Mobile MVNO"),
    ("republic-wireless","Republic Wireless","Republic Wireless","WiFi-first carrier"),
    ("ting","Ting","Ting","pay-per-use MVNO"),
    ("xfinity-mobile","Xfinity Mobile","Xfinity Mobile","Comcast MVNO Verizon"),
    ("spectrum-mobile","Spectrum Mobile","Spectrum Mobile","Charter MVNO Verizon"),
    ("tmobile-prepaid","T-Mobile Prepaid","T-Mobile Prepaid","T-Mobile owned prepaid"),
]

# ── COMP INTENTS (12) ─────────────────────────────────────────────────────────
COMP_INTENTS = [
    ("vs","vs","which is better"),
    ("price","price comparison","which costs less"),
    ("coverage","coverage comparison","which has better coverage"),
    ("unlimited","unlimited plan","unlimited data comparison"),
    ("hotspot","hotspot","hotspot speed comparison"),
    ("review","review comparison","honest comparison review"),
    ("switch","switch","should I switch"),
    ("5g","5G","5G network comparison"),
    ("family","family plan","family plan comparison"),
    ("seniors","seniors","best for seniors"),
    ("rural","rural coverage","rural coverage comparison"),
    ("data-speed","data speed","data speed comparison"),
]

# ── LONG TAIL (250) ───────────────────────────────────────────────────────────
LONG_TAILS = [
    # Visible specific
    ("does-visible-work","Does Visible Work","does visible wireless work well"),
    ("visible-review-2026","Visible Review 2026","visible wireless review 2026"),
    ("visible-pros-cons","Visible Pros and Cons","visible wireless pros and cons"),
    ("visible-coverage-map","Visible Coverage Map","visible wireless coverage map 2026"),
    ("visible-speed","Visible Data Speed","visible wireless data speed test"),
    ("visible-activation","How to Activate Visible","how to activate visible wireless"),
    ("visible-porting","Port Number to Visible","transfer number to visible"),
    ("visible-cancel","How to Cancel Visible","how to cancel visible wireless"),
    ("visible-customer-service","Visible Customer Service","visible wireless customer service"),
    ("visible-hotspot-speed","Visible Hotspot Speed","visible mobile hotspot speed 2026"),
    ("visible-throttling","Does Visible Throttle","does visible throttle data"),
    ("visible-deprioritization","Visible Data Deprioritization","visible data slowing down"),
    ("visible-network","Visible Network","what network does visible use"),
    ("visible-verizon","Visible Verizon Connection","is visible on verizon network"),
    ("visible-vs-boost","Visible vs Boost Mobile","visible versus boost mobile"),
    ("visible-vs-straight-talk","Visible vs Straight Talk","visible versus straight talk"),
    ("visible-vs-consumer-cellular","Visible vs Consumer Cellular","visible versus consumer cellular"),
    ("visible-vs-google-fi","Visible vs Google Fi","visible versus google fi"),
    ("visible-vs-us-mobile","Visible vs US Mobile","visible versus us mobile"),
    ("visible-vs-xfinity-mobile","Visible vs Xfinity Mobile","visible versus xfinity mobile"),
    ("visible-vs-spectrum-mobile","Visible vs Spectrum Mobile","visible versus spectrum mobile"),
    ("visible-iphone-compatible","Visible iPhone Compatible","is my iphone compatible with visible"),
    ("visible-samsung-compatible","Visible Samsung Compatible","does visible work with samsung"),
    ("visible-pixel-compatible","Visible Google Pixel","does visible work with google pixel"),
    ("visible-android-compatible","Visible Android Compatible","visible wireless android compatible phones"),
    # Cheap plans
    ("cheapest-phone-plan-usa","Cheapest Phone Plan USA","cheapest phone plan in america 2026"),
    ("cheapest-unlimited-plan","Cheapest Unlimited Plan","cheapest unlimited data plan 2026"),
    ("best-cheap-phone-plan","Best Cheap Phone Plan","best cheap phone plan 2026"),
    ("20-dollar-phone-plan","$20 Phone Plan","best 20 dollar phone plan"),
    ("25-dollar-phone-plan","$25 Phone Plan","best 25 dollar phone plan"),
    ("30-dollar-phone-plan","$30 Phone Plan","best 30 dollar phone plan"),
    ("phone-plan-under-30","Phone Plan Under $30","best phone plan under 30 dollars"),
    ("phone-plan-under-20","Phone Plan Under $20","cheapest phone plan under 20"),
    ("no-contract-phone-plan","No Contract Phone Plan","best no contract phone plan 2026"),
    ("prepaid-unlimited-plan","Prepaid Unlimited Plan","best prepaid unlimited plan 2026"),
    # Coverage
    ("5g-phone-plan","5G Phone Plan","best 5g phone plan 2026"),
    ("best-5g-coverage","Best 5G Coverage","best 5g network coverage usa"),
    ("verizon-network-mvno","Verizon Network MVNO","best mvno on verizon network"),
    ("verizon-alternative-cheap","Cheap Verizon Alternative","cheapest verizon alternative"),
    ("verizon-prepaid-alternative","Verizon Prepaid Alternative","verizon prepaid vs visible"),
    ("rural-phone-plan","Rural Phone Plan","best phone plan for rural areas"),
    ("best-rural-coverage","Best Rural Coverage","best phone coverage rural usa"),
    ("nationwide-coverage-plan","Nationwide Coverage Plan","phone plan nationwide coverage"),
    ("reliable-phone-plan","Reliable Phone Plan","most reliable phone plan usa"),
    ("phone-plan-dead-zones","Phone Plan Dead Zones","best coverage no dead zones"),
    # Unlimited specific
    ("truly-unlimited-plan","Truly Unlimited Plan","truly unlimited no throttle phone plan"),
    ("unlimited-hotspot-plan","Unlimited Hotspot Plan","phone plan unlimited hotspot"),
    ("unlimited-data-no-throttle","Unlimited Data No Throttle","unlimited data that isnt throttled"),
    ("streaming-phone-plan","Phone Plan for Streaming","best phone plan for streaming video"),
    ("gaming-phone-plan","Phone Plan for Gaming","best phone plan for mobile gaming"),
    ("work-from-home-plan","Phone Plan Work from Home","best phone plan work from home"),
    ("heavy-data-user","Phone Plan Heavy Data User","best phone plan if you use a lot of data"),
    ("unlimited-video-streaming","Unlimited Video Streaming","phone plan unlimited video streaming"),
    ("netflix-phone-plan","Netflix Phone Plan","phone plan with netflix included"),
    ("disney-phone-plan","Disney Plus Phone Plan","phone plan with disney plus"),
    # Family
    ("family-phone-plan","Family Phone Plan","best family phone plan 2026"),
    ("couple-phone-plan","Phone Plan for Couples","best phone plan for 2 people"),
    ("2-line-phone-plan","2 Line Phone Plan","best 2 line phone plan"),
    ("3-line-phone-plan","3 Line Phone Plan","best 3 line phone plan"),
    ("4-line-phone-plan","4 Line Phone Plan","best 4 line phone plan"),
    ("kids-phone-plan","Kids Phone Plan","best phone plan for kids"),
    ("family-unlimited-plan","Family Unlimited Plan","best family unlimited data plan"),
    ("cheapest-family-plan","Cheapest Family Plan","cheapest family phone plan 2026"),
    ("no-contract-family-plan","No Contract Family Plan","family phone plan no contract"),
    ("party-pay","Visible Party Pay","visible party pay how it works"),
    # BYOD and devices
    ("bring-your-own-phone","Bring Your Own Phone Plan","bring your own phone no contract plan"),
    ("unlock-phone-carrier","Unlock Phone New Carrier","how to switch carriers keep phone"),
    ("keep-number-switch","Keep Number Switch Carriers","keep phone number switch carriers"),
    ("iphone-cheap-plan","Cheap iPhone Plan","cheapest plan for iphone 2026"),
    ("samsung-cheap-plan","Cheap Samsung Plan","cheapest plan for samsung 2026"),
    ("android-cheap-plan","Cheap Android Plan","cheapest android phone plan"),
    ("esim-plan","eSIM Phone Plan","best esim phone plan 2026"),
    ("esim-activation","eSIM Activation","how to activate esim phone"),
    ("compatible-phones-visible","Compatible Phones Visible","what phones work with visible"),
    ("phone-upgrade-plan","Phone Upgrade Plan","phone plan with phone upgrade"),
    # Seniors
    ("senior-phone-plan","Senior Phone Plan 2026","best phone plan for seniors 2026"),
    ("phone-plan-over-60","Phone Plan Over 60","best phone plan for people over 60"),
    ("phone-plan-over-65","Phone Plan Over 65","best phone plan seniors 65"),
    ("phone-plan-over-70","Phone Plan Over 70","best senior phone plan over 70"),
    ("aarp-phone-plan","AARP Phone Plan","best phone plan aarp members"),
    ("consumer-cellular-alternative","Consumer Cellular Alternative","better than consumer cellular"),
    ("easy-phone-plan-seniors","Easy Phone Plan Seniors","simplest phone plan for seniors"),
    ("affordable-senior-phone","Affordable Senior Phone Plan","affordable phone plan for elderly"),
    ("senior-unlimited-data","Senior Unlimited Data","unlimited data plan for seniors"),
    ("flip-phone-plan","Flip Phone Plan","best phone plan for flip phones"),
    # Students
    ("student-phone-plan","Student Phone Plan 2026","best phone plan for students 2026"),
    ("college-phone-plan","College Phone Plan","best phone plan for college students"),
    ("phone-plan-no-credit","Phone Plan No Credit Check","phone plan without credit check"),
    ("student-discount-phone","Student Discount Phone Plan","phone plan student discount"),
    ("dorm-phone-plan","Dorm Phone Plan","phone plan for college dorm"),
    ("cheap-college-plan","Cheap College Phone Plan","cheapest phone plan for college"),
    ("back-to-school-phone","Back to School Phone Plan","phone plan back to school"),
    ("first-phone-plan","First Phone Plan","best first phone plan young adult"),
    ("phone-plan-no-ssn","Phone Plan No SSN","phone plan without social security number"),
    ("phone-plan-immigrants","Phone Plan Immigrants","phone plan for new immigrants usa"),
    # Military
    ("military-phone-plan","Military Phone Plan","best phone plan military 2026"),
    ("veteran-phone-plan","Veteran Phone Plan","best phone plan for veterans"),
    ("military-discount-phone","Military Discount Phone Plan","phone plan military discount"),
    ("active-duty-phone-plan","Active Duty Phone Plan","phone plan active military"),
    ("deployed-phone-plan","Deployed Military Phone Plan","phone plan while deployed"),
    ("military-family-plan","Military Family Phone Plan","family phone plan military"),
    ("government-phone-plan","Government Employee Phone Plan","phone plan government employee"),
    ("lifeline-phone-plan","Lifeline Phone Plan","lifeline program phone plan"),
    ("acp-phone-plan","ACP Phone Plan","affordable connectivity program phone"),
    ("free-phone-plan-low-income","Free Phone Plan Low Income","free government phone plan"),
    # Switching
    ("switch-from-att","Switch from AT&T","switch from att to cheaper plan"),
    ("switch-from-tmobile","Switch from T-Mobile","switch from tmobile save money"),
    ("switch-from-verizon","Switch from Verizon","switch from verizon save money"),
    ("switch-from-cricket","Switch from Cricket","switch from cricket wireless"),
    ("save-on-phone-bill","Save on Phone Bill","how to save money on phone bill"),
    ("lower-phone-bill","Lower Phone Bill","how to lower monthly phone bill"),
    ("phone-bill-too-high","Phone Bill Too High","why is my phone bill so high"),
    ("cancel-att","Cancel AT&T","how to cancel att and switch"),
    ("cancel-verizon","Cancel Verizon","how to cancel verizon wireless"),
    ("cancel-tmobile","Cancel T-Mobile","how to cancel tmobile"),
    # International
    ("international-phone-plan","International Phone Plan","best international phone plan usa"),
    ("calling-mexico-plan","Calling Mexico Phone Plan","phone plan unlimited calls mexico"),
    ("calling-canada-plan","Calling Canada Phone Plan","phone plan unlimited calls canada"),
    ("travel-phone-plan","Travel Phone Plan","best phone plan for international travel"),
    ("roaming-free-plan","Roaming Free Plan","phone plan no roaming charges"),
    ("visible-mexico","Visible in Mexico","does visible work in mexico"),
    ("visible-canada","Visible in Canada","does visible work in canada"),
    ("visible-international","Visible International","visible international calling"),
    ("global-phone-plan","Global Phone Plan","global phone plan usa 2026"),
    ("worldwide-coverage-plan","Worldwide Coverage Plan","phone plan worldwide coverage"),
    # Tech and features
    ("wifi-calling-plan","WiFi Calling Phone Plan","best phone plan with wifi calling"),
    ("volte-plan","VoLTE Phone Plan","phone plan with VoLTE calling"),
    ("5g-hotspot-plan","5G Hotspot Plan","phone plan 5g mobile hotspot"),
    ("unlimited-text-plan","Unlimited Text Plan","unlimited texting phone plan"),
    ("voicemail-plan","Voicemail Phone Plan","phone plan with visual voicemail"),
    ("hd-calling-plan","HD Calling Plan","phone plan HD voice calling"),
    ("data-rollover","Data Rollover Plan","phone plan with data rollover"),
    ("pause-plan","Pause Phone Plan","can you pause your phone plan"),
    ("multi-month-plan","Multi Month Phone Plan","phone plan pay multiple months"),
    ("annual-phone-plan","Annual Phone Plan","phone plan annual discount"),
    # General comparison
    ("best-phone-plan-2026","Best Phone Plan 2026","best cell phone plan 2026"),
    ("best-prepaid-plan-2026","Best Prepaid Plan 2026","best prepaid phone plan 2026"),
    ("best-mvno-2026","Best MVNO 2026","best mvno carrier 2026"),
    ("mvno-comparison","MVNO Comparison","mvno carrier comparison 2026"),
    ("carrier-comparison","Carrier Comparison","cell carrier comparison 2026"),
    ("phone-plan-comparison","Phone Plan Comparison","compare phone plans 2026"),
    ("unlimited-plan-comparison","Unlimited Plan Comparison","compare unlimited phone plans"),
    ("prepaid-vs-postpaid","Prepaid vs Postpaid","prepaid vs postpaid phone plan"),
    ("mvno-vs-carrier","MVNO vs Major Carrier","mvno versus major carrier"),
    ("best-value-phone-plan","Best Value Phone Plan","best value phone plan 2026"),
    # More specific
    ("visible-data-cap","Visible Data Cap","does visible have a data cap"),
    ("visible-contract","Visible Contract","does visible require a contract"),
    ("visible-credit-check","Visible Credit Check","does visible do a credit check"),
    ("visible-port-number","Visible Port Number","how to port number to visible"),
    ("visible-sim-card","Visible SIM Card","how to get visible sim card"),
    ("visible-esim","Visible eSIM Setup","how to set up visible esim"),
    ("visible-app-setup","Visible App Setup","how to set up visible app"),
    ("visible-billing","Visible Billing","how does visible billing work"),
    ("visible-autopay","Visible Autopay","visible wireless autopay"),
    ("visible-referral","Visible Referral Code","visible referral code discount"),
    # Coverage specific
    ("visible-rural-coverage","Visible Rural Coverage","does visible work in rural areas"),
    ("visible-building-coverage","Visible Indoor Coverage","does visible work inside buildings"),
    ("visible-travel-usa","Visible Travel USA","does visible work across usa"),
    ("visible-dead-zones","Visible Dead Zones","visible wireless dead zones"),
    ("visible-4g-lte","Visible 4G LTE","visible 4g lte coverage"),
    ("visible-5g-speed","Visible 5G Speed","how fast is visible 5g"),
    ("visible-speed-test","Visible Speed Test","visible wireless speed test results"),
    ("visible-latency","Visible Latency","visible wireless latency ping"),
    ("visible-reliability","Visible Reliability","is visible wireless reliable"),
    ("visible-outage","Visible Outage","visible wireless outage problems"),
    # New 2026 topics
    ("visible-2026","Visible Wireless 2026","visible wireless review 2026"),
    ("visible-changes-2026","Visible Plan Changes 2026","visible plan changes updates 2026"),
    ("best-plan-2026","Best Wireless Plan 2026","best wireless plan america 2026"),
    ("visible-new-customers","Visible New Customer Deal","visible new customer discount 2026"),
    ("visible-loyalty","Visible Loyalty Discount","visible loyalty reward discount"),
    ("visible-referral-2026","Visible Referral 2026","visible referral program 2026"),
    ("visible-black-friday","Visible Black Friday Deal","visible black friday phone deal"),
    ("visible-cyber-monday","Visible Cyber Monday","visible cyber monday deal"),
    ("visible-holiday-deal","Visible Holiday Deal","visible holiday phone plan deal"),
    ("cell-plan-inflation","Cell Plan Inflation","how to save on phone plan inflation"),
    # More plan types
    ("pay-as-you-go","Pay As You Go Plan","pay as you go phone plan usa"),
    ("monthly-phone-plan","Monthly Phone Plan","best month to month phone plan"),
    ("phone-plan-no-annual","Phone Plan No Annual","phone plan no annual contract"),
    ("short-term-phone-plan","Short Term Phone Plan","short term phone plan month to month"),
    ("temporary-phone-plan","Temporary Phone Plan","temporary phone plan usa"),
    ("phone-plan-moving","Phone Plan When Moving","best phone plan when relocating"),
    ("phone-plan-new-usa","Phone Plan New to USA","best phone plan new to america"),
    ("sim-only-plan","SIM Only Plan","best sim only plan usa 2026"),
    ("data-sim-plan","Data SIM Plan","best data sim plan usa"),
    ("unlocked-phone-plan","Unlocked Phone Plan","best phone plan unlocked phone"),
    # More Visible
    ("visible-glitches","Visible Glitches","visible wireless problems glitches"),
    ("visible-streaming","Visible Streaming","streaming quality on visible"),
    ("visible-zoom","Visible Zoom Calls","does visible work for zoom calls"),
    ("visible-video-quality","Visible Video Quality","video streaming quality visible"),
    ("visible-international-travel","Visible International Travel","using visible while traveling abroad"),
    ("visible-hotspot-laptop","Visible Hotspot Laptop","using visible hotspot for laptop"),
    ("visible-home-internet","Visible Home Internet","can visible replace home internet"),
    ("visible-tablet","Visible Tablet","can I use visible on a tablet"),
    ("visible-smartwatch","Visible Smartwatch","does visible support smartwatch"),
    ("visible-second-phone","Visible Second Phone","visible wireless for second phone"),
]

# ── CSS ────────────────────────────────────────────────────────────────────────
CSS = """
:root{
  --blue:#1565c0;--blue-light:#1e88e5;--blue-pale:#e3f2fd;
  --bg:#f5f9ff;--white:#ffffff;--card:#ffffff;
  --text:#1a2332;--muted:#546e7a;--border:#dce6f0;
  --green:#2e7d32;--font:'Plus Jakarta Sans',sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--text);font-family:var(--font);line-height:1.6}
a{text-decoration:none;color:inherit}

.site-header{background:var(--white);box-shadow:0 2px 12px rgba(21,101,192,0.1);position:sticky;top:0;z-index:100}
.nav-inner{max-width:1200px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;padding:14px 24px}
.logo{font-weight:800;font-size:20px;color:var(--blue);display:flex;align-items:center;gap:8px}
.header-cta{background:var(--blue-light);color:#fff;font-weight:700;font-size:13px;padding:10px 22px;border-radius:8px;transition:background .2s,transform .2s}
.header-cta:hover{background:var(--blue);transform:translateY(-1px)}

.promo-bar{background:var(--green);color:#fff;text-align:center;padding:10px;font-size:13px;font-weight:700;letter-spacing:.04em}

.hero{background:linear-gradient(135deg,var(--blue) 0%,var(--blue-light) 60%,#42a5f5 100%);color:#fff;padding:72px 24px 56px;text-align:center}
.hero-badge{display:inline-block;background:rgba(255,255,255,0.15);border:1px solid rgba(255,255,255,0.3);border-radius:999px;padding:6px 18px;font-size:12px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:20px;font-weight:700}
.hero h1{font-size:clamp(24px,5vw,50px);font-weight:800;line-height:1.15;margin-bottom:14px}
.hero p{font-size:17px;opacity:.92;max-width:620px;margin:0 auto 28px}
.cta-group{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
.btn-white{background:#fff;color:var(--blue);font-weight:800;font-size:15px;padding:14px 30px;border-radius:8px;box-shadow:0 4px 20px rgba(0,0,0,0.15);transition:transform .2s,box-shadow .2s}
.btn-white:hover{transform:translateY(-2px);box-shadow:0 8px 28px rgba(0,0,0,0.2)}
.btn-outline-white{border:2px solid rgba(255,255,255,0.5);color:#fff;font-size:15px;padding:12px 24px;border-radius:8px;transition:border-color .2s}
.btn-outline-white:hover{border-color:#fff}

.price-badge{background:var(--blue-pale);border:2px solid var(--blue-light);border-radius:12px;padding:20px;text-align:center;max-width:300px;margin:0 auto 28px}
.price-amount{font-size:48px;font-weight:800;color:var(--blue);line-height:1}
.price-period{font-size:14px;color:var(--muted);margin-top:4px}
.price-note{font-size:12px;color:var(--green);font-weight:600;margin-top:6px}

.trust-bar{background:var(--white);border-bottom:1px solid var(--border);display:flex;justify-content:center;gap:40px;flex-wrap:wrap;padding:16px 24px}
.trust-item{display:flex;align-items:center;gap:8px;font-size:13px;font-weight:600;color:var(--muted)}
.trust-item span{font-size:18px}

.features{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;padding:52px 24px;max-width:1200px;margin:0 auto}
.feat{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:22px;box-shadow:0 2px 8px rgba(21,101,192,0.05);transition:box-shadow .2s,transform .2s,border-color .2s}
.feat:hover{box-shadow:0 8px 24px rgba(21,101,192,0.12);transform:translateY(-3px);border-color:var(--blue-light)}
.feat-icon{font-size:28px;margin-bottom:10px}
.feat h3{font-size:15px;font-weight:700;color:var(--blue);margin-bottom:6px}
.feat p{font-size:13px;color:var(--muted);line-height:1.6}

.faq-section{max-width:800px;margin:0 auto;padding:0 24px 52px}
.faq-title{font-size:20px;font-weight:800;color:var(--blue);margin-bottom:20px;padding-bottom:12px;border-bottom:2px solid var(--border)}
.faq-item{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:18px;margin-bottom:10px}
.faq-q{font-weight:700;font-size:14px;color:var(--text);margin-bottom:6px}
.faq-a{font-size:13px;color:var(--muted);line-height:1.6}

.related{max-width:1200px;margin:0 auto;padding:0 24px 52px}
.sec-title{font-size:18px;font-weight:800;color:var(--blue);margin-bottom:14px;padding-bottom:10px;border-bottom:2px solid var(--border)}
.rel-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:10px}
.rel-card{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:12px 14px;font-size:13px;font-weight:600;color:var(--text);transition:border-color .2s,box-shadow .2s}
.rel-card:hover{border-color:var(--blue-light);box-shadow:0 4px 12px rgba(21,101,192,0.1)}

.cta-band{background:linear-gradient(135deg,var(--blue),var(--blue-light));color:#fff;padding:52px 24px;text-align:center}
.cta-band h2{font-size:clamp(22px,4vw,36px);font-weight:800;margin-bottom:10px}
.cta-band p{opacity:.9;margin-bottom:24px;font-size:17px}

.sticky-cta{position:fixed;bottom:20px;right:20px;background:var(--blue-light);color:#fff;font-weight:800;font-size:13px;padding:13px 20px;border-radius:8px;box-shadow:0 4px 20px rgba(21,101,192,0.4);z-index:999;transition:background .2s}
.sticky-cta:hover{background:var(--blue)}

footer{background:var(--white);border-top:1px solid var(--border);padding:24px;text-align:center;font-size:12px;color:var(--muted)}
footer a{color:var(--blue-light)}

@media(max-width:600px){.nav-inner{padding:12px 14px}.hero{padding:48px 14px 36px}.trust-bar{gap:16px}}
"""
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"/><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>'

# ── PAGE BUILDER ──────────────────────────────────────────────────────────────
def make_page(slug, title, desc, h1, badge, features_html, faq_html, related_html, cta_h2, cta_p, show_price=True):
    canonical = f"{BASE_URL}{slug}"
    price_html = """<div class="price-badge">
  <div class="price-amount">$20</div>
  <div class="price-period">per month</div>
  <div class="price-note">✓ Unlimited Data · No Contract · 5G</div>
</div>""" if show_price else ""
    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<meta name="google-site-verification" content="eWVDN3vbam9nnaZQu7wAQKyfmJJdM7zjI80l4DGeUrQ"/>
<meta name="msvalidate.01" content="574044E39556B8B8DAAF1D1F233C87B0"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<meta name="robots" content="index,follow"/>
<link rel="canonical" href="{canonical}"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:type" content="website"/>
<meta property="og:url" content="{canonical}"/>
{FONTS}
<style>{CSS}</style>
<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"WebPage",
  "name":"{title}",
  "description":"{desc}",
  "url":"{canonical}"
}}
</script>
</head>
<body>
<div class="promo-bar">🎉 Limited Time: Go Unlimited for $20/mo — Visible Wireless</div>
<header class="site-header">
  <div class="nav-inner">
    <div class="logo">📱 Visible</div>
    <a class="header-cta" href="{AFF}" target="_blank" rel="nofollow sponsored">Get Started →</a>
  </div>
</header>
<section class="hero">
  <div class="hero-badge">{badge}</div>
  <h1>{h1}</h1>
  {price_html}
  <p>{desc}</p>
  <div class="cta-group">
    <a class="btn-white" href="{AFF}" target="_blank" rel="nofollow sponsored">Get $20/mo Unlimited →</a>
    <a class="btn-outline-white" href="index.html">← All Plans</a>
  </div>
</section>
<div class="trust-bar">
  <div class="trust-item"><span>📶</span> Verizon 5G Network</div>
  <div class="trust-item"><span>♾️</span> Truly Unlimited</div>
  <div class="trust-item"><span>🚫</span> No Contracts</div>
  <div class="trust-item"><span>💰</span> From $20/mo</div>
</div>
<div class="features">{features_html}</div>
{faq_html}
<div class="related">
  <div class="sec-title">Related Plans & Coverage</div>
  <div class="rel-grid">{related_html}</div>
</div>
<section class="cta-band">
  <h2>{cta_h2}</h2>
  <p>{cta_p}</p>
  <a class="btn-white" href="{AFF}" target="_blank" rel="nofollow sponsored">Get $20/mo Unlimited →</a>
</section>
<a class="sticky-cta" href="{AFF}" target="_blank" rel="nofollow sponsored">📱 $20/mo Unlimited</a>
<footer>
  © {YEAR} Visible Affiliate Guide · <a href="index.html">Home</a> · Affiliate links used · Prices subject to change
</footer>
</body>
</html>"""

def make_faq(faqs):
    if not faqs: return ""
    items = "".join(
        f'<div class="faq-item"><div class="faq-q">❓ {q}</div><div class="faq-a">Visible offers one of the best values in wireless — unlimited data on Verizon\'s 5G network starting at $20/month with no contracts. Visit Visible to check your eligibility and get started.</div></div>'
        for q in faqs
    )
    return f'<div class="faq-section"><div class="faq-title">Frequently Asked Questions</div>{items}</div>'

# ── STATE PAGES ───────────────────────────────────────────────────────────────
def make_state_page(st_slug, st_name, st_abbr, i_slug, i_name, i_kw):
    slug  = f"visible-{st_slug}-{i_slug}.html"
    title = f"Visible {i_name} in {st_name} {YEAR} | $20/mo Unlimited 5G"
    desc  = f"Get {i_kw} in {st_name}. Visible wireless — $20/month unlimited data on Verizon's 5G network. No contracts, no hidden fees. Ships to all {st_name} zip codes."
    h1    = f"📱 Visible {i_name} in {st_name}"
    badge = f"📍 {st_abbr} · $20/mo · {YEAR}"
    features_html = f"""
<div class="feat"><div class="feat-icon">📍</div><h3>Visible in {st_name}</h3><p>Visible covers {st_name} ({st_abbr}) on Verizon's 5G and 4G LTE network — one of the most reliable networks in {st_name}.</p></div>
<div class="feat"><div class="feat-icon">💰</div><h3>$20/mo in {st_name}</h3><p>Get unlimited data in {st_name} for just $20/month. No contracts, no credit checks, no hidden fees.</p></div>
<div class="feat"><div class="feat-icon">📶</div><h3>5G Coverage {st_abbr}</h3><p>Enjoy Verizon 5G speeds across {st_name}. Check coverage for your specific {st_name} zip code on Visible's coverage map.</p></div>
<div class="feat"><div class="feat-icon">🚀</div><h3>Activate Online</h3><p>Sign up for Visible in {st_name} entirely online. Order your SIM or activate eSIM — no store visit required.</p></div>"""
    faqs = [f"Does Visible have coverage in {st_name}?", f"How much is Visible in {st_name}?", f"Is Visible available in all of {st_name}?", "Can I keep my number when switching to Visible?"]
    related_html = "".join(
        f'<a href="visible-{s2}-{i_slug}.html" class="rel-card">📍 Visible {sn2} ({sa2})</a>'
        for s2, sn2, sa2 in STATES[:10] if s2 != st_slug
    )
    return slug, make_page(slug, title, desc, h1, badge, features_html, make_faq(faqs), related_html,
        f"Get Visible in {st_name} for $20/mo",
        f"Unlimited 5G on Verizon's network in {st_name}. No contract, no hidden fees.")

# ── CITY PAGES ────────────────────────────────────────────────────────────────
def make_city_page(c_slug, c_name, c_state, i_slug, i_name, i_kw):
    slug  = f"visible-{c_slug}-{i_slug}.html"
    title = f"Visible {i_name} {c_name}, {c_state} {YEAR} | $20/mo 5G"
    desc  = f"Get {i_kw} in {c_name}, {c_state}. Visible — $20/month unlimited 5G on Verizon's network. No contracts, no hidden fees, activate online today."
    h1    = f"📱 Visible {i_name} — {c_name}, {c_state}"
    badge = f"📍 {c_name}, {c_state} · $20/mo · {YEAR}"
    features_html = f"""
<div class="feat"><div class="feat-icon">🏙️</div><h3>Visible in {c_name}</h3><p>Visible covers {c_name}, {c_state} on Verizon's 5G network. Get unlimited data in {c_name} for just $20/month.</p></div>
<div class="feat"><div class="feat-icon">📶</div><h3>5G in {c_name}</h3><p>Enjoy fast 5G speeds throughout {c_name}, {c_state}. Powered by Verizon — one of America's most reliable networks.</p></div>
<div class="feat"><div class="feat-icon">💰</div><h3>$20/mo in {c_name}</h3><p>Unlimited data, talk, text, and hotspot in {c_name} for just $20/month. No contracts, no credit checks.</p></div>
<div class="feat"><div class="feat-icon">🚀</div><h3>Instant Activation</h3><p>Activate Visible in {c_name} instantly with eSIM or order a physical SIM delivered to your {c_name} address.</p></div>"""
    faqs = [f"Does Visible have 5G in {c_name}?", f"Is Visible available in {c_name}, {c_state}?", "How fast is Visible in cities?", "Can I switch to Visible and keep my number?"]
    related_html = "".join(
        f'<a href="visible-{st_slug}-{i_slug}.html" class="rel-card">📍 Visible {st_name}</a>'
        for st_slug, st_name, st_abbr in STATES[:10]
    )
    return slug, make_page(slug, title, desc, h1, badge, features_html, make_faq(faqs), related_html,
        f"Get Visible in {c_name} for $20/mo",
        f"Unlimited 5G in {c_name}, {c_state}. No contract, no hidden fees, activate today.")

# ── PLAN OVERVIEW ─────────────────────────────────────────────────────────────
def make_plan_overview(ps, pn, pt, pk, pi, pd, pf):
    slug  = f"visible-{ps}-overview.html"
    title = f"Visible {pn} {YEAR} | {pt}"
    desc  = f"Complete guide to Visible's {pn.lower()}. {pd[:120]}... $20/month, no contracts, Verizon 5G network."
    h1    = f"{pi} Visible {pn} — Complete Guide {YEAR}"
    badge = f"✅ {pn} · $20/mo · {YEAR}"
    features_html = f"""
<div class="feat"><div class="feat-icon">{pi}</div><h3>{pn}</h3><p>{pd}</p></div>
<div class="feat"><div class="feat-icon">💰</div><h3>Starting at $20/mo</h3><p>Visible's {pn.lower()} starts at just $20/month. Includes unlimited data, talk, text, and mobile hotspot. No contracts.</p></div>
<div class="feat"><div class="feat-icon">📶</div><h3>Verizon 5G Network</h3><p>Visible runs on Verizon's nationwide 5G and 4G LTE network — one of America's most reliable and expansive networks.</p></div>
<div class="feat"><div class="feat-icon">🚀</div><h3>Easy Activation</h3><p>Sign up online in minutes. Use eSIM for instant activation or order a SIM card shipped to your door. No store visit needed.</p></div>"""
    related_html = "".join(
        f'<a href="visible-{ps2}-overview.html" class="rel-card">{pi2} {pn2}</a>'
        for ps2, pn2, pt2, pk2, pi2, pd2, pf2 in PLANS if ps2 != ps
    )
    return slug, make_page(slug, title, desc, h1, badge, features_html, make_faq(pf), related_html,
        f"Get Visible's {pn} for $20/mo",
        f"Unlimited 5G on Verizon's network. No contract, no hidden fees. Start today.")

# ── PLAN INTENT PAGES ─────────────────────────────────────────────────────────
def make_plan_page(ps, pn, pt, pk, pi, pd, pf, i_slug, i_name):
    slug  = f"visible-{ps}-{i_slug}.html"
    title = f"Visible {pn} — {i_name} {YEAR} | $20/mo Unlimited"
    desc  = f"Get {pk} with Visible. {pd[:100]}... $20/month on Verizon's 5G network, no contracts."
    h1    = f"{pi} Visible {pn}: {i_name}"
    badge = f"✅ {pn} · {YEAR}"
    features_html = f"""
<div class="feat"><div class="feat-icon">{pi}</div><h3>{pn}</h3><p>{pd}</p></div>
<div class="feat"><div class="feat-icon">💰</div><h3>$20/mo Unlimited</h3><p>Visible's {pn.lower()} is available from just $20/month with unlimited data, talk, text, and hotspot.</p></div>
<div class="feat"><div class="feat-icon">📶</div><h3>Verizon's Network</h3><p>Powered by Verizon's 5G — America's most reliable network with nationwide coverage.</p></div>
<div class="feat"><div class="feat-icon">🚫</div><h3>No Contracts</h3><p>Visible is 100% no contract. Switch anytime, cancel anytime — no penalties, no fees.</p></div>"""
    related_html = "".join(
        f'<a href="visible-{ps2}-overview.html" class="rel-card">{pi2} {pn2}</a>'
        for ps2, pn2, pt2, pk2, pi2, pd2, pf2 in PLANS if ps2 != ps
    )
    return slug, make_page(slug, title, desc, h1, badge, features_html, make_faq(pf), related_html,
        f"Get Visible {pn} for $20/mo",
        f"Unlimited 5G, no contracts, no hidden fees. Start with Visible today.")

# ── COMPETITOR PAGES ──────────────────────────────────────────────────────────
def make_competitor_page(c_slug, c_name, c_short, c_type, i_slug, i_name, i_kw):
    slug  = f"visible-vs-{c_slug}-{i_slug}.html"
    title = f"Visible vs {c_name} {YEAR} — {i_name} | Which is Cheaper?"
    desc  = f"Compare Visible vs {c_name} for {i_kw}. See pricing, coverage, speeds, and features. Find out which is the better phone plan in {YEAR}."
    h1    = f"⚖️ Visible vs {c_name}: {i_name}"
    badge = f"🔍 Comparison · {YEAR}"
    features_html = f"""
<div class="feat"><div class="feat-icon">💰</div><h3>Price: Visible Wins</h3><p>Visible starts at $20/month for unlimited data. {c_name} is a {c_type} — compare their pricing and features to see how much you could save.</p></div>
<div class="feat"><div class="feat-icon">📶</div><h3>Network: Verizon 5G</h3><p>Visible runs on Verizon's 5G network. {c_name} runs on a different network. Compare {i_kw} between the two carriers.</p></div>
<div class="feat"><div class="feat-icon">🚫</div><h3>No Contract vs {c_short}</h3><p>Visible requires no contract — switch or cancel anytime. Compare this flexibility with {c_name}'s {i_kw}.</p></div>
<div class="feat"><div class="feat-icon">⭐</div><h3>Why Switch to Visible</h3><p>Millions have switched from {c_name} to Visible for lower bills, no contracts, and reliable Verizon coverage. Is it right for you?</p></div>"""
    faqs = [f"Is Visible better than {c_name}?", f"How does Visible compare to {c_name} in price?", f"Does Visible have better coverage than {c_name}?", f"Should I switch from {c_name} to Visible?"]
    related_html = "".join(
        f'<a href="visible-vs-{cs2}-{i_slug}.html" class="rel-card">Visible vs {cn2}</a>'
        for cs2, cn2, csh2, ct2 in COMPETITORS if cs2 != c_slug
    )
    return slug, make_page(slug, title, desc, h1, badge, features_html, make_faq(faqs), related_html,
        f"Switch from {c_name} to Visible",
        f"Save money with Visible — $20/mo unlimited on Verizon's 5G. No contract, no hassle.", show_price=False)

# ── LONG TAIL PAGES ───────────────────────────────────────────────────────────
def make_longtail_page(lt_slug, lt_name, lt_kw):
    slug  = f"{lt_slug}.html"
    title = f"{lt_name} | Visible Wireless {YEAR}"
    desc  = f"Complete guide to {lt_kw}. Visible offers $20/month unlimited 5G on Verizon's network — no contracts, no hidden fees. Compare and decide today."
    h1    = f"🔍 {lt_name}"
    badge = f"⭐ {lt_kw.title()} · {YEAR}"
    features_html = f"""
<div class="feat"><div class="feat-icon">🔬</div><h3>Expert Guide</h3><p>Everything you need to know about {lt_kw} — expert analysis to help you find the best phone plan in {YEAR}.</p></div>
<div class="feat"><div class="feat-icon">💰</div><h3>Visible: $20/mo</h3><p>Visible is one of the best answers to {lt_kw} — unlimited data on Verizon's 5G network for just $20/month.</p></div>
<div class="feat"><div class="feat-icon">📶</div><h3>Verizon 5G Network</h3><p>Visible runs on Verizon's nationwide 5G — reliable, fast, and available in thousands of US cities and towns.</p></div>
<div class="feat"><div class="feat-icon">🚫</div><h3>No Contracts</h3><p>100% no contract. Switch, cancel, or change plans anytime — no early termination fees, ever.</p></div>"""
    faqs = [f"What is the best option for {lt_kw}?", "Is Visible a good choice?", "How does Visible compare to other options?", "How do I sign up for Visible?"]
    related_html = "".join(
        f'<a href="{ls2}.html" class="rel-card">{ln2}</a>'
        for ls2, ln2, lk2 in LONG_TAILS[:12] if ls2 != lt_slug
    )
    return slug, make_page(slug, title, desc, h1, badge, features_html, make_faq(faqs), related_html,
        f"Get $20/mo Unlimited with Visible",
        f"The best answer to {lt_kw} — unlimited 5G on Verizon for $20/month. No contract.")

# ── STATE × PLAN ──────────────────────────────────────────────────────────────
def make_state_plan_page(st_slug, st_name, st_abbr, ps, pn, pi, pk):
    slug  = f"visible-{st_slug}-{ps}.html"
    title = f"Visible {pn} in {st_name} {YEAR} | $20/mo Unlimited"
    desc  = f"Get Visible's {pn.lower()} in {st_name}. {pk} — $20/month on Verizon's 5G network. No contracts, no hidden fees."
    h1    = f"{pi} Visible {pn} in {st_name}"
    badge = f"📍 {st_abbr} · {pn} · {YEAR}"
    features_html = f"""
<div class="feat"><div class="feat-icon">📍</div><h3>{pn} in {st_name}</h3><p>Visible's {pn.lower()} covers {st_name} ({st_abbr}) on Verizon's 5G network. Get {pk} for $20/month.</p></div>
<div class="feat"><div class="feat-icon">💰</div><h3>$20/mo in {st_name}</h3><p>Just $20/month for unlimited data in {st_name}. No contracts, no credit checks, no hidden fees.</p></div>
<div class="feat"><div class="feat-icon">📶</div><h3>5G Coverage {st_abbr}</h3><p>Verizon's 5G network covers {st_name} extensively — check the coverage map for your specific area.</p></div>
<div class="feat"><div class="feat-icon">🚀</div><h3>Activate in {st_name}</h3><p>Sign up online and activate instantly with eSIM — or get a SIM shipped to your {st_name} address.</p></div>"""
    faqs = [f"Is Visible {pn.lower()} available in {st_name}?", f"How much is Visible in {st_name}?", f"Does Visible cover all of {st_name}?", "Can I switch to Visible and keep my number?"]
    related_html = "".join(
        f'<a href="visible-{s2}-{ps}.html" class="rel-card">Visible {sn2} {pn}</a>'
        for s2, sn2, sa2 in STATES[:10] if s2 != st_slug
    )
    return slug, make_page(slug, title, desc, h1, badge, features_html, make_faq(faqs), related_html,
        f"Get Visible {pn} in {st_name}",
        f"$20/month unlimited on Verizon's 5G in {st_name}. No contract, activate today.")

# ── INDEX ─────────────────────────────────────────────────────────────────────
def make_index():
    plan_cards = "".join(
        f'<a href="visible-{ps}-overview.html" class="feat" style="cursor:pointer"><div class="feat-icon">{pi}</div><h3>{pn}</h3><p>{pd[:80]}...</p></a>'
        for ps, pn, pt, pk, pi, pd, pf in PLANS
    )
    state_cards = "".join(
        f'<a href="visible-{s}-unlimited-plan.html" class="rel-card">📍 {sn} ({sa})</a>'
        for s, sn, sa in STATES
    )
    comp_cards = "".join(
        f'<a href="visible-vs-{cs}-vs.html" class="rel-card">Visible vs {cn}</a>'
        for cs, cn, csh, ct in COMPETITORS
    )
    lt_cards = "".join(
        f'<a href="{ls}.html" class="rel-card">{ln}</a>'
        for ls, ln, lk in LONG_TAILS[:24]
    )
    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<meta name="google-site-verification" content="eWVDN3vbam9nnaZQu7wAQKyfmJJdM7zjI80l4DGeUrQ"/>
<meta name="msvalidate.01" content="574044E39556B8B8DAAF1D1F233C87B0"/>
<title>Visible Wireless {YEAR} | $20/mo Unlimited 5G — Best Prepaid Phone Plan USA</title>
<meta name="description" content="Visible wireless — $20/month unlimited 5G on Verizon's network. No contracts, no hidden fees, no credit checks. The best cheap phone plan in the USA {YEAR}."/>
<meta name="robots" content="index,follow"/>
<link rel="canonical" href="{BASE_URL}"/>
{FONTS}
<style>{CSS}
.section{{max-width:1200px;margin:0 auto;padding:52px 24px}}
.section-title{{font-size:22px;font-weight:800;color:var(--blue);margin-bottom:20px;padding-bottom:12px;border-bottom:2px solid var(--border)}}
.plan-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}}
.hero-price{{font-size:64px;font-weight:800;color:#fff;line-height:1}}
.hero-price-sub{{font-size:20px;opacity:.85;margin-bottom:8px}}
.hero-perks{{display:flex;gap:20px;justify-content:center;flex-wrap:wrap;margin:16px 0 24px;font-size:14px;opacity:.9}}
.hero-perks span{{background:rgba(255,255,255,0.15);padding:6px 14px;border-radius:999px}}
</style>
</head>
<body>
<div class="promo-bar">🎉 Limited Time: Go Unlimited for $20/mo — Visible Wireless</div>
<header class="site-header">
  <div class="nav-inner">
    <div class="logo">📱 Visible</div>
    <a class="header-cta" href="{AFF}" target="_blank" rel="nofollow sponsored">Get $20/mo →</a>
  </div>
</header>
<section class="hero">
  <div class="hero-badge">🇺🇸 Verizon 5G Network · No Contract · {YEAR}</div>
  <h1>Unlimited 5G for</h1>
  <div class="hero-price">$20<span style="font-size:28px">/mo</span></div>
  <div class="hero-price-sub">Unlimited data, talk, text & hotspot</div>
  <div class="hero-perks">
    <span>✓ No Contracts</span>
    <span>✓ No Hidden Fees</span>
    <span>✓ No Credit Check</span>
    <span>✓ Verizon 5G</span>
  </div>
  <div class="cta-group">
    <a class="btn-white" href="{AFF}" target="_blank" rel="nofollow sponsored">Get Started for $20/mo →</a>
  </div>
</section>
<div class="trust-bar">
  <div class="trust-item"><span>📶</span> Verizon 5G Network</div>
  <div class="trust-item"><span>♾️</span> Truly Unlimited</div>
  <div class="trust-item"><span>🚫</span> No Contracts</div>
  <div class="trust-item"><span>💰</span> From $20/mo</div>
  <div class="trust-item"><span>📱</span> Any Unlocked Phone</div>
</div>
<div class="section">
  <div class="section-title">📱 Our Plans</div>
  <div class="plan-grid">{plan_cards}</div>
</div>
<div class="section" style="padding-top:0">
  <div class="section-title">📍 Coverage by State</div>
  <div class="rel-grid">{state_cards}</div>
</div>
<div class="section" style="padding-top:0">
  <div class="section-title">⚖️ Visible vs Competitors</div>
  <div class="rel-grid">{comp_cards}</div>
</div>
<div class="section" style="padding-top:0">
  <div class="section-title">🔍 Research Topics</div>
  <div class="rel-grid">{lt_cards}</div>
</div>
<section class="cta-band">
  <h2>America's Best Deal in Wireless</h2>
  <p>$20/month unlimited 5G on Verizon's network. No contracts, no hidden fees.</p>
  <a class="btn-white" href="{AFF}" target="_blank" rel="nofollow sponsored">Get $20/mo Unlimited →</a>
</section>
<a class="sticky-cta" href="{AFF}" target="_blank" rel="nofollow sponsored">📱 $20/mo Unlimited</a>
<footer>© {YEAR} Visible Affiliate Guide · Affiliate links used · Prices subject to change · <a href="index.html">Home</a></footer>
</body>
</html>"""

# ── SITEMAP / ROBOTS ──────────────────────────────────────────────────────────
def make_sitemap(urls):
    iso = now.strftime("%Y-%m-%d")
    sm  = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sm += f'  <url><loc>{BASE_URL}</loc><changefreq>daily</changefreq><priority>1.0</priority><lastmod>{iso}</lastmod></url>\n'
    for url in urls:
        sm += f'  <url><loc>{url}</loc><changefreq>weekly</changefreq><priority>0.7</priority><lastmod>{iso}</lastmod></url>\n'
    sm += '</urlset>\n'
    return sm

def make_robots():
    return f"User-agent: *\nAllow: /\nDisallow: /build.py\nDisallow: /.github/\nCrawl-delay: 1\nSitemap: {BASE_URL}sitemap.xml\n"

def make_llms():
    return f"# Visible Wireless USA Affiliate\n> Updated: {DATE_STR}\n> Affiliate links present\n\n## About\n13,500+ page USA affiliate site for Visible wireless.\nCovers all 50 states, 240 cities, 15 plans, 20 competitors, 250 long-tail keywords.\nKey offer: $20/month unlimited 5G on Verizon's network, no contracts.\n\n## Site: {BASE_URL}\n"

# ── MAIN ──────────────────────────────────────────────────────────────────────
def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.stdout.strip(): print(r.stdout.strip())
    return r.returncode

if __name__ == "__main__":
    state_p = len(STATES) * len(STATE_INTENTS)
    city_p  = len(CITIES) * len(STATE_INTENTS)
    plan_p  = len(PLANS) * 20 + len(PLANS)
    comp_p  = len(COMPETITORS) * len(COMP_INTENTS)
    lt_p    = len(LONG_TAILS)
    sp_p    = len(STATES) * len(PLANS)
    total   = state_p + city_p + plan_p + comp_p + lt_p + sp_p

    print(f"📱  Visible Build — {DATE_STR}  sync={SYNC}")
    print(f"   State pages:      {state_p:,}")
    print(f"   City pages:       {city_p:,}")
    print(f"   Plan pages:       {plan_p:,}")
    print(f"   Competitor pages: {comp_p:,}")
    print(f"   Long-tail pages:  {lt_p:,}")
    print(f"   State × Plan:     {sp_p:,}")
    print(f"   Total: {total:,} pages")

    with open("index.html","w",encoding="utf-8") as f: f.write(make_index())
    with open("robots.txt","w",encoding="utf-8") as f: f.write(make_robots())
    with open("llms.txt","w",encoding="utf-8") as f: f.write(make_llms())
    with open(".nojekyll","w") as f: f.write("")
    print("✅ index.html  robots.txt  llms.txt  .nojekyll")

    sitemap_urls = []
    count = 0

    print("   Generating state pages...")
    for st_slug, st_name, st_abbr in STATES:
        for i_slug, i_name, i_kw in STATE_INTENTS:
            slug, html = make_state_page(st_slug, st_name, st_abbr, i_slug, i_name, i_kw)
            with open(slug,"w",encoding="utf-8") as f: f.write(html)
            sitemap_urls.append(f"{BASE_URL}{slug}")
            count += 1

    print("   Generating city pages...")
    for c_slug, c_name, c_state in CITIES:
        for i_slug, i_name, i_kw in STATE_INTENTS:
            slug, html = make_city_page(c_slug, c_name, c_state, i_slug, i_name, i_kw)
            with open(slug,"w",encoding="utf-8") as f: f.write(html)
            sitemap_urls.append(f"{BASE_URL}{slug}")
            count += 1
            if count % 5000 == 0: print(f"   {count:,}/{total:,}...")

    print("   Generating plan pages...")
    for plan in PLANS:
        ps, pn, pt, pk, pi, pd, pf = plan
        slug, html = make_plan_overview(ps, pn, pt, pk, pi, pd, pf)
        with open(slug,"w",encoding="utf-8") as f: f.write(html)
        sitemap_urls.append(f"{BASE_URL}{slug}")
        count += 1
        for i_slug, i_name, i_kw in STATE_INTENTS[:20]:
            slug, html = make_plan_page(ps, pn, pt, pk, pi, pd, pf, i_slug, i_name)
            with open(slug,"w",encoding="utf-8") as f: f.write(html)
            sitemap_urls.append(f"{BASE_URL}{slug}")
            count += 1

    print("   Generating competitor pages...")
    for c_slug, c_name, c_short, c_type in COMPETITORS:
        for i_slug, i_name, i_kw in COMP_INTENTS:
            slug, html = make_competitor_page(c_slug, c_name, c_short, c_type, i_slug, i_name, i_kw)
            with open(slug,"w",encoding="utf-8") as f: f.write(html)
            sitemap_urls.append(f"{BASE_URL}{slug}")
            count += 1

    print("   Generating long-tail pages...")
    for lt in LONG_TAILS:
        slug, html = make_longtail_page(*lt)
        with open(slug,"w",encoding="utf-8") as f: f.write(html)
        sitemap_urls.append(f"{BASE_URL}{slug}")
        count += 1

    print("   Generating state × plan pages...")
    for st_slug, st_name, st_abbr in STATES:
        for ps, pn, pt, pk, pi, pd, pf in PLANS:
            slug, html = make_state_plan_page(st_slug, st_name, st_abbr, ps, pn, pi, pk)
            with open(slug,"w",encoding="utf-8") as f: f.write(html)
            sitemap_urls.append(f"{BASE_URL}{slug}")
            count += 1

    print(f"✅ {count:,} pages written")
    with open("sitemap.xml","w",encoding="utf-8") as f: f.write(make_sitemap(sitemap_urls))
    print(f"✅ sitemap.xml — {len(sitemap_urls)+1:,} URLs")

    print("\n── Git ──")
    run("git add -A")
    n = int(subprocess.run("git diff --cached --name-only | wc -l",
        shell=True,capture_output=True,text=True).stdout.strip())
    print(f"Staged: {n:,} files")
    if n == 0:
        print("Nothing to commit"); sys.exit(0)
    run(f'git commit -m "visible sync {SYNC}"')
    import time
    for i in range(1,6):
        print(f"Push attempt {i}...")
        run("git fetch origin main")
        if run("git rebase origin/main") != 0:
            run("git rebase --abort"); time.sleep(5); continue
        if run("git push origin HEAD:main") == 0:
            print("✅ Pushed"); break
        time.sleep(5)
    else:
        print("❌ Push failed"); sys.exit(1)

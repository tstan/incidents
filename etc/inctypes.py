# callsign: (category, more info),
types = {
    "DEL": ("Other", "Delay Response"),
    "FAA": ("Fire", "Aircraft"),
    "FAAL": ("Fire", "Aircraft - Large"),
    "FAAS": ("Fire", "Aircraft - Small"),
    "FCS": ("Fire", "Smoke Check"),
    "FFA": ("Fire", "False Alarm"),
    "FFAS": ("Fire", "False Alarm Smoke"),
    "FOA": ("Fire", "Assist"),
    "FOAI": ("Fire", "Assist-Instant Aid"),
    "FOAM": ("Fire", "Assist-Mutual Aid"),
    "FOAS": ("Fire", "Mutual-Aid Struct"),
    "FOAV": ("Fire", "Vehicle Assist"),
    "FOAW": ("Fire", "Wildland Assist"),
    "FOD": ("Fire", "Debris"),
    "FODCB": ("Fire", "Check Control Burn"),
    "FODI": ("Fire", "Debris Illegal"),
    "FODR": ("Fire", "Debris - Roadside"),
    "FOI": ("Fire", "Improvement"),
    "FOO": ("Fire", "Other"),
    "FOOA": ("Fire", "Agriculture"),
    "FOOAH": ("Fire", "Almond Hulls"),
    "FOOCM": ("Fire", "Cotton Module"),
    "FOOD": ("Fire", "Dumpster"),
    "FOOHS": ("Fire", "Haystack"),
    "FOOP": ("Fire", "Pole"),
    "FSC": ("Fire", "Commercial"),
    "FSCA": ("Fire", "Commercial Alarm"),
    "FSCM": ("Fire", "STR Marina and Boat"),
    "FSCR": ("Fire", "3rd Alarm into RDN"),
    "FSCW": ("Fire", "Com Struct Wildland"),
    "FSM": ("Fire", "Multi Family"),
    "FSMA": ("Fire", "Multi Family Alarm"),
    "FSO": ("Fire", "Structure Other"),
    "FSOF": ("Fire", "Structure Flue"),
    "FSOP": ("Fire", "Structure Pier"),
    "FSOU": ("Fire", "Type Unknown"),
    "FSR": ("Fire", "Residential"),
    "FSRA": ("Fire", "Residential Alarm"),
    "FSRC": ("Fire", "Chimney"),
    "FSRO": ("Fire", "Oven"),
    "FSRW": ("Fire", "Res Struct Wildland"),
    "FVC": ("Fire", "Veh Commercial"),
    "FVCL": ("Fire", "Large Vehicle"),
    "FVCLW": ("Fire", "Large Vehicle Wildland"),
    "FVCT": ("Fire", "Train"),
    "FVCTW": ("Fire", "Train Threat Veg"),
    "FVCW": ("Fire", "Veh Com Wildland"),
    "FVP": ("Fire", "Veh Passenger"),
    "FVPB": ("Fire", "Boat"),
    "FVPBL": ("Fire", "Boat Large"),
    "FVPSC": ("Fire", "Veh Pas Thr Com Str"),
    "FVPSR": ("Fire", "Veh Pas Thr Res Str"),
    "FVPW": ("Fire", "Veh Pass Wildland"),
    "FWL": ("Fire", "Wildland"),
    "FWLCD": ("Fire", "Center Div/Vac Lot"),
    "FWLG": ("Fire", "Grass-LRA"),
    "FWLH": ("Fire", "Wildland High"),
    "FWLL": ("Fire", "Wildland Low"),
    "FWLM": ("Fire", "Wildland Med"),
    "FWLMTZ": ("Fire", "Wildland City MTZ"),
    "FWLT": ("Fire", "Wildland Lightning"),
    "FWLZ": ("Fire", "Wildland T Zone"),
    "HAS": ("Hazard", "Haz, Aircraft"),
    "HAS1": ("Hazard", "Hazard, Aircraft, Alert 1"),
    "HAS2": ("Hazard", "Hazard, Aircraft, Alert 2"),
    "HAS3": ("Hazard", "Hazard, Aircraft, Alert 3"),
    "HFS": ("Hazard", "Haz, Fire Menace Standby"),
    "HFSEQ": ("Hazard", "Haz, Earthquake"),
    "HFSFW": ("Hazard", "Haz, Fireworks Complaint"),
    "HFSP": ("Hazard", "Haz, Petro Spill - SM"),
    "HOA": ("Hazard", "Haz, Assist"),
    "HOAB": ("Hazard", "Haz, Assist BINTF"),
    "HOAT": ("Hazard", "Haz, Assist BINTF"),
    "HOAW": ("Hazard", "Haz, Tree"),
    "HSB": ("Hazard", "Haz, Bomb Threat"),
    "HSBC": ("Hazard", "Bomb Threat - Commercial"),
    "HSBR": ("Hazard", "Bomb Threat - Residential"),
    "HSBT": ("Hazard", "Bomb Threat - Other"),
    "HSBTC": ("Hazard", "Bomb Threat, Com / MFD"),
    "HSBTS": ("Hazard", "Bomb Threat - Residential"),
    "HSBTV": ("Hazard", "Bomb Threat, Vehicle"),
    "HSE": ("Hazard", "Haz, Electrical"),
    "HSG": ("Hazard", "Haz, Gas"),
    "HSGC": ("Hazard", "Haz, Gas - Commercial STR"),
    "HSGR": ("Hazard", "Haz, Gas - Res STR"),
    "HTT": ("Hazard", "Haz, Terrorist Threat"),
    "HZM": ("Hazard", "Hazmat"),
    "HZM1": ("Hazard", "Hazmat, Level 1"),
    "HZM2": ("Hazard", "Hazmat, Level 2"),
    "HZM3": ("Hazard", "Hazmat, Level 3"),
    "HZM3M": ("Hazard", "Hazmat, L3, Mass Casualty"),
    "HZMCMA": ("Hazard", "Car Mon Alarm Sounding"),
    "HZMDL": ("Hazard", "Hazmat, Drug Lab"),
    "HZMEX": ("Hazard", "Explosion"),
    "HZMF": ("Hazard", "Haz, Flam. Liquid"),
    "HZMMC": ("Hazard", "Hazmat, Mass Casualty"),
    "LEB": ("Law Enforcement", "LE, Arson Bomb"),
    "LEBK": ("Law Enforcement", "LE, Arson Bomb, K9"),
    "LEI": ("Law Enforcement", "LE, Investigation"),
    "LEIJ": ("Law Enforcement", "LE, Investigation, JDSF"),
    "LEO": ("Law Enforcement", "LE, Other"),
    "LEOAOA": ("Law Enforcement", "LE, Assist Other Agency"),
    "LEOCE": ("Law Enforcement", "LE, Code Enforcement"),
    "LEOF": ("Law Enforcement", "LE, Fireworks Complaint"),
    "LEOJ": ("Law Enforcement", "LE, JDSF"),
    "LEOMON": ("Law Enforcement", "LE, Monitoring/Transport"),
    "MED": ("Medical", "Medical"),
    "MED01": ("Medical", "PRO QA, Reserved"),
    "MED01A": ("Medical", "MEDICAL - C2 - ABD Pain"),
    "MED02": ("Medical", "PRO QA, Reserved"),
    "MED03": ("Medical", "PRO QA, Reserved"),
    "MED03A": ("Medical", "MEDICAL - C2 - Animal Bite"),
    "MED04": ("Medical", "PRO QA, Reserved"),
    "MED05": ("Medical", "PRO QA, Reserved"),
    "MED05A": ("Medical", "MEDICAL - C2 - Back Pain"),
    "MED06": ("Medical", "PRO QA, Reserved"),
    "MED07": ("Medical", "PRO QA, Reserved"),
    "MED08": ("Medical", "PRO QA, Reserved"),
    "MED09": ("Medical", "PRO QA, Reserved"),
    "MED1": ("Medical", "Medical, Priority 1"),
    "MED10": ("Medical", "PRO QA, Reserved"),
    "MED11": ("Medical", "PRO QA, Reserved"),
    "MED12": ("Medical", "PRO QA, Reserved"),
    "MED12A": ("Medical", "MEDICAL - C2 - Seizures"),
    "MED13": ("Medical", "PRO QA, Reserved"),
    "MED13A": ("Medical", "MEDICAL - C2 - Diabetic"),
    "MED14": ("Medical", "PRO QA, Reserved"),
    "MED15": ("Medical", "PRO QA, Reserved"),
    "MED16": ("Medical", "PRO QA, Reserved"),
    "MED17": ("Medical", "PRO QA, Reserved"),
    "MED17A": ("Medical", "MEDICAL - C2 - FALLS"),
    "MED18": ("Medical", "PRO QA, Reserved"),
    "MED19": ("Medical", "PRO QA, Reserved"),
    "MED2": ("Medical", "Medical, Priority 2"),
    "MED20": ("Medical", "PRO QA, Reserved"),
    "MED20A": ("Medical", "MEDICAL - C2 - Exposure"),
    "MED21": ("Medical", "PRO QA, Reserved"),
    "MED21A": ("Medical", "MEDICAL - C2 - Hemorrhage"),
    "MED22": ("Medical", "PRO QA, Reserved"),
    "MED23": ("Medical", "PRO QA, Reserved"),
    "MED24": ("Medical", "PRO QA, Reserved"),
    "MED25": ("Medical", "PRO QA, Reserved"),
    "MED26": ("Medical", "PRO QA, Reserved"),
    "MED26A": ("Medical", "MEDICAL - C2 - Sick Person"),
    "MED27": ("Medical", "PRO QA, Reserved"),
    "MED28": ("Medical", "PRO QA, Reserved"),
    "MED29": ("Medical", "PRO QA, Reserved"),
    "MED3": ("Medical", "Medical, Priority 3"),
    "MED30": ("Medical", "PRO QA, Reserved"),
    "MED30A": ("Medical", "MEDICAL - C2 - Traumatic"),
    "MED31": ("Medical", "PRO QA, Reserved"),
    "MED31A": ("Medical", "MEDICAL - C2 - Unconscious"),
    "MED32": ("Medical", "PRO QA, Reserved"),
    "MED33": ("Medical", "PRO QA, Reserved"),
    "MED34": ("Medical", "PRO QA, Reserved"),
    "MED35": ("Medical", "PRO QA, Reserved"),
    "MED36": ("Medical", "PRO QA, Reserved"),
    "MED37": ("Medical", "PRO QA, Reserved"),
    "MED38": ("Medical", "PRO QA, Reserved"),
    "MED39": ("Medical", "PRO QA, Reserved"),
    "MED4": ("Medical", "Medical, Priority 4"),
    "MED40": ("Medical", "PRO QA, Reserved"),
    "MED41": ("Medical", "PRO QA, Reserved"),
    "MED42": ("Medical", "PRO QA, Reserved"),
    "MED43": ("Medical", "PRO QA, Reserved"),
    "MED44": ("Medical", "PRO QA, Reserved"),
    "MED45": ("Medical", "PRO QA, Reserved"),
    "MED46": ("Medical", "PRO QA, Reserved"),
    "MED47": ("Medical", "PRO QA, Reserved"),
    "MED48": ("Medical", "PRO QA, Reserved"),
    "MED49": ("Medical", "PRO QA, Reserved"),
    "MED5": ("Medical", "Medical, Priority 5"),
    "MED50": ("Medical", "PRO QA, Reserved"),
    "MED51": ("Medical", "PRO QA, Reserved"),
    "MED515": ("Medical", "5150"),
    "MED52": ("Medical", "PRO QA, Reserved"),
    "MED53": ("Medical", "PRO QA, Reserved"),
    "MED54": ("Medical", "PRO QA, Reserved"),
    "MED55": ("Medical", "PRO QA, Reserved"),
    "MED56": ("Medical", "PRO QA, Reserved"),
    "MED57": ("Medical", "PRO QA, Reserved"),
    "MED58": ("Medical", "PRO QA, Reserved"),
    "MED59": ("Medical", "PRO QA, Reserved"),
    "MED6": ("Medical", "Medical, Priority 6"),
    "MED60": ("Medical", "PRO QA, Reserved"),
    "MED61": ("Medical", "PRO QA, Reserved"),
    "MED62": ("Medical", "PRO QA, Reserved"),
    "MED63": ("Medical", "PRO QA, Reserved"),
    "MED64": ("Medical", "PRO QA, Reserved"),
    "MED65": ("Medical", "PRO QA, Reserved"),
    "MED66": ("Medical", "PRO QA, Reserved"),
    "MED67": ("Medical", "PRO QA, Reserved"),
    "MED68": ("Medical", "PRO QA, Reserved"),
    "MED69": ("Medical", "PRO QA, Reserved"),
    "MED7": ("Medical", "Medical, Priority 7"),
    "MED70": ("Medical", "PRO QA, Reserved"),
    "MED71": ("Medical", "PRO QA, Reserved"),
    "MED72": ("Medical", "PRO QA, Reserved"),
    "MED73": ("Medical", "PRO QA, Reserved"),
    "MED74": ("Medical", "PRO QA, Reserved"),
    "MED75": ("Medical", "PRO QA, Reserved"),
    "MED76": ("Medical", "PRO QA, Reserved"),
    "MED77": ("Medical", "PRO QA, Reserved"),
    "MED78": ("Medical", "PRO QA, Reserved"),
    "MED79": ("Medical", "PRO QA, Reserved"),
    "MED80": ("Medical", "PRO QA, Reserved"),
    "MED81": ("Medical", "PRO QA, Reserved"),
    "MED82": ("Medical", "PRO QA, Reserved"),
    "MED83": ("Medical", "PRO QA, Reserved"),
    "MED84": ("Medical", "PRO QA, Reserved"),
    "MED85": ("Medical", "PRO QA, Reserved"),
    "MED86": ("Medical", "PRO QA, Reserved"),
    "MED87": ("Medical", "PRO QA, Reserved"),
    "MED88": ("Medical", "PRO QA, Reserved"),
    "MED89": ("Medical", "PRO QA, Reserved"),
    "MED90": ("Medical", "PRO QA, Reserved"),
    "MED91": ("Medical", "PRO QA, Reserved"),
    "MED92": ("Medical", "PRO QA, Reserved"),
    "MED93": ("Medical", "PRO QA, Reserved"),
    "MED94": ("Medical", "PRO QA, Reserved"),
    "MED95": ("Medical", "PRO QA, Reserved"),
    "MED96": ("Medical", "PRO QA, Reserved"),
    "MED97": ("Medical", "PRO QA, Reserved"),
    "MED98": ("Medical", "PRO QA, Reserved"),
    "MED99": ("Medical", "PRO QA, Reserved"),
    "MEDA": ("Medical", "Medical, Alpha"),
    "MEDABD": ("Medical", "Medical, Abdominal Pain"),
    "MEDAD": ("Medical", "Aircraft Down"),
    "MEDAL": ("Medical", "Aircraft Down, Large"),
    "MEDAM": ("Medical", "Ambulance Request"),
    "MEDAS": ("Medical", "Aircraft Down, Small"),
    "MEDASL": ("Medical", "Assault"),
    "MEDAVL": ("Medical", "Avalanche"),
    "MEDB": ("Medical", "Medical, Bravo"),
    "MEDBIR": ("Medical", "Child Birth"),
    "MEDBIT": ("Medical", "Bites or Stings"),
    "MEDBLD": ("Medical", "Bleeding"),
    "MEDBP": ("Medical", "Blood Pressure"),
    "MEDBRN": ("Medical", "Burns"),
    "MEDC": ("Medical", "Charlie"),
    "MEDC2": ("Medical", "Code 2"),
    "MEDC3": ("Medical", "Code 3"),
    "MEDCD": ("Medical", "Child Down"),
    "MEDCHK": ("Medical", "Choking"),
    "MEDCM": ("Medical", "Carbon Monoxide"),
    "MEDCO": ("Medical", "Coastal"),
    "MEDCOS": ("Medical", "Comp of Surgery"),
    "MEDCP": ("Medical", "Chest Pains"),
    "MEDCT1": ("Medical", "Aircraft Category 1"),
    "MEDCT2": ("Medical", "Aircraft Category 2"),
    "MEDCT3": ("Medical", "Aircraft Category 3"),
    "MEDCT4": ("Medical", "Aircrft SNGL Offsite"),
    "MEDCT5": ("Medical", "Aircrft MULT Offsite"),
    "MEDD": ("Medical", "Medical, Delta"),
    "MEDDB": ("Medical", "Difficulty Breathing"),
    "MEDDIA": ("Medical", "Diabetic"),
    "MEDDRW": ("Medical", "Drowning"),
    "MEDE": ("Medical", "Medical Echo"),
    "MEDELT": ("Medical", "Electrocution"),
    "MEDEYE": ("Medical", "Eye Injury"),
    "MEDF": ("Medical", "Flight"),
    "MEDFAL": ("Medical", "Fall"),
    "MEDFF": ("Medical", "Flight Following"),
    "MEDFM": ("Medical", "Flight Missed"),
    "MEDFNT": ("Medical", "Fainted / Passed Out"),
    "MEDFSI": ("Medical", "SSV Inquiry"),
    "MEDFSM": ("Medical", "SSV Missed Flight"),
    "MEDFSS": ("Medical", "SSV Scene Flight"),
    "MEDH": ("Medical", "Heart Attack, Stroke"),
    "MEDHET": ("Medical", "Heat Related"),
    "MEDI": ("Medical", "Industrial Accident"),
    "MEDINQ": ("Medical", "Inquiry"),
    "MEDINT": ("Medical", "Interfacility"),
    "MEDL": ("Medical", "Life Threatening"),
    "MEDLG": ("Medical", "Lifeguard"),
    "MEDLOC": ("Medical", "Level of Consciousness"),
    "MEDM": ("Medical", "Mass-Casualty"),
    "MEDN": ("Medical", "Non-Life Threatening"),
    "MEDO": ("Medical", "Medical, Omega"),
    "MEDOD": ("Medical", "Overdose"),
    "MEDOTS": ("Medical", "TC Over the Side"),
    "MEDPD": ("Medical", "Person Down"),
    "MEDPRG": ("Medical", "Comp of Pregnancy"),
    "MEDR": ("Medical", "EMS Relay"),
    "MEDRA": ("Medical", "Ringing Alarm"),
    "MEDRI": ("Medical", "Ambulance Ride In"),
    "MEDS": ("Medical", "Standby"),
    "MEDSOW": ("Medical", "Slumped Over Wheel"),
    "MEDSTG": ("Medical", "Staging (Non-violent)"),
    "MEDSU": ("Medical", "Medical - Suicide"),
    "MEDSZ": ("Medical", "Seizures"),
    "MEDT": ("Medical", "Medical Transfer"),
    "MEDTRA": ("Medical", "Trauma"),
    "MEDU": ("Medical", "Medical, Unresponsive"),
    "MEDUNR": ("Medical", "Unresp / Breathing"),
    "MEDUU": ("Medical", "Uncon / Unresp"),
    "MISC": ("Miscellaneous", "Disp. Discretion"),
    "MOA": ("Medical", "Medical Assist"),
    "MOAEMD": ("Medical", "Other Assist E M D"),
    "MOAT": ("Medical", "Assist T/C"),
    "MRE": ("Medical", "Medical Rescue"),
    "MREBC": ("Medical", "Building Collapse"),
    "MRECLF": ("Medical", "Cliff Rescue"),
    "MRECS": ("Medical", "Conf Space/Trench"),
    "MREI": ("Medical", "Med Res, Industrial"),
    "MRELG": ("Medical", "Lifeguard SRF Rescue"),
    "MREM": ("Medical", "Med Res, Mine"),
    "MREO": ("Medical", "Med Res, Ocean"),
    "MREOTS": ("Medical", "Med Res, Over the Side"),
    "MRERA": ("Medical", "Med Res, Remote Area"),
    "MRESH": ("Medical", "Med - Res - Short Haul"),
    "MRESRF": ("Medical", "Surf Rescue"),
    "MRESW": ("Medical", "Med Res, Static Water"),
    "MRESWF": ("Medical", "Med Res, Swift Water"),
    "MREUSR": ("Medical", "USAR"),
    "MREW": ("Medical", "Water Rescue"),
    "MTC": ("Medical", "Traffic Collision"),
    "MTCA": ("Medical", "T/C - Amb Ride-In"),
    "MTCF": ("Medical", "T/C With Fire"),
    "MTCFW": ("Medical", "T/C Freeway"),
    "MTCH": ("Medical", "T/C High Speed"),
    "MTCL": ("Medical", "T/C Low Speed"),
    "MTCM": ("Medical", "T/C Multi-Casualty"),
    "MTCMV": ("Medical", "T/C Multi-Vehicle"),
    "MTCOTS": ("Medical", "T/C Over the Side"),
    "MTCPED": ("Medical", "T/C Auto vs. Pedestrian"),
    "MTCS": ("Medical", "T/C into Structure"),
    "MTCU": ("Medical", "T/C Unknown Injuries"),
    "MTCW": ("Medical", "T/C with Injuries"),
    "MTX": ("Medical", "With Extrication"),
    "MTXA": ("Medical", "T/X - Amb Ride-In"),
    "MVI": ("Medical", "Violence Involved"),
    "MVIM": ("Medical", "MVI, Mass Casualty"),
    "MVIS": ("Medical", "Stabbing - Shooting"),
    "MVISTG": ("Medical", "Staging Required"),
    "OAC": ("Other", "Cover"),
    "OACA": ("Other", "Cover Ambulance"),
    "OACE": ("Other", "Cover Engine"),
    "OACM": ("Other", "Medical Cover"),
    "OAF": ("Other", "Flight Following"),
    "OAFC": ("Other", "Flight Follow, CO-OP"),
    "OAFM": ("Other", "Flight Follow, Med"),
    "OAFMHA": ("Other", "Med Copter Activity"),
    "OAM": ("Other", "Miscellaneous"),
    "OAMAD": ("Other", "Agency Death"),
    "OAMADM": ("Other", "Other, Administrative"),
    "OAMAI": ("Other", "Agency Injury"),
    "OAMCAD": ("Other", "CAD Down"),
    "OAMCSM": ("Other", "CISD"),
    "OAMD": ("Other", "Display"),
    "OAMDE": ("Other", "Damage to Equip/Fac"),
    "OAMI": ("Other", "MISC Investigation"),
    "OAMPHN": ("Other", "Phone System Down"),
    "OAMRAD": ("Other", "Radio Repair"),
    "OAMRO": ("Other", "Resource Order"),
    "OAMSO": ("Other", "SO/Medcom Incident"),
    "OAMT": ("Other", "Misc. Training"),
    "OAMT1": ("Other", "Training (w-Inc #)"),
    "OAMTE": ("Other", "Theft of Equip"),
    "OAMTEC": ("Other", "Theft of Equip, CDF"),
    "OAMTEL": ("Other", "Theft of Equip, Lcl"),
    "OAMVA": ("Other", "CDF Vehicle Accident"),
    "OAP": ("Other", "Staffing Pattern"),
    "OAR": ("Other", "Referral"),
    "OARN": ("Other", "Referral to NAVDG"),
    "OASP": ("Other", "Staffing Pattern"),
    "OAT": ("Other", "Transfer"),
    "OAV": ("Other", "Veg Mgmt"),
    "OES": ("Other", "Services"),
    "OESA": ("Other", "Alarm Test"),
    "OESK": ("Other", "Knox Box"),
    "OESL": ("Other", "Local Request"),
    "OESL1": ("Other", "Local Request(W/Inc#),"),
    "OEST": ("Other", "TRNG Announcement"),
    "OOA": ("Other", "Assist"),
    "OOABP": ("Other", "Burn Permit"),
    "OOACB": ("Other", "Control Burn"),
    "OOAFC": ("Other", "Fire Crews"),
    "OOAHT": ("Other", "Helitack Training"),
    "OOAME": ("Other", "Media"),
    "OOAOFS": ("Other", "OFS"),
    "OOASH": ("Other", "Shorthaul Training"),
    "OOU": ("Other", "Out of Unit"),
    "OOUA": ("Other", "Out of Unit, Aircrft"),
    "OOUC": ("Other", "Out of Unit, Crews"),
    "OOUE": ("Other", "Out of Unit, Equip"),
    "OOUED": ("Other", "Out of Unit, Eq Doz"),
    "OOUEE": ("Other", "Out of Unit, Eq Eng"),
    "OOUM": ("Other", "Out of Unit, MISC"),
    "OOUO": ("Other", "Out of Unit, Ovrhead"),
    "OOUOES": ("Other", "Out of Unit OES"),
    "OUT": ("Other", "Out of Service"),
    "PAA": ("Public Assist", "Agency"),
    "PAD": ("Public Assist", "Demo"),
    "PAF": ("Public Assist", "Flooding"),
    "PAO": ("Public Assist", "Other"),
    "PAO1": ("Public Assist", "Other - Engine Only"),
    "PAO2": ("Public Assist", "Other - Eng and Comp"),
    "PAOAN": ("Public Assist", "Animal"),
    "PAOC": ("Public Assist", "Civil Disturb"),
    "PAOLG": ("Public Assist", "Lifeguard"),
    "PAOS": ("Public Assist", "Salvage"),
    "PAOT": ("Public Assist", "Traffic Hazard"),
    "PAP": ("Public Assist", "Person"),
    "PSR": ("Public Assist", "Search & Rescue")
}

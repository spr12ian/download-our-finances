from sqlalchemy import Column, Float, MetaData, Table, Text
from sqlalchemy.orm.base import Mapped

metadata = MetaData()


t__ahalif = Table(
    '_ahalif', metadata,
    Column('Date', Text),
    Column('Description (10255868) AHALIF', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__asanta = Table(
    '_asanta', metadata,
    Column('Date', Text),
    Column('Description (12589975) ASANTA', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bchase = Table(
    '_bchase', metadata,
    Column('Date', Text),
    Column('Description (81107449) BCHASE', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bchrnd = Table(
    '_bchrnd', metadata,
    Column('Date', Text),
    Column('Description () BCHRND', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bchsav = Table(
    '_bchsav', metadata,
    Column('Date', Text),
    Column('Description () BCHSAV', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bcoisa = Table(
    '_bcoisa', metadata,
    Column('Date', Text),
    Column('Description (91246782) BCOISA', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bcoloy = Table(
    '_bcoloy', metadata,
    Column('Date', Text),
    Column('Description (34826286) BCOLOY', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bcyner = Table(
    '_bcyner', metadata,
    Column('Date', Text),
    Column('Description (24721201) BCYNER', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bfamil = Table(
    '_bfamil', metadata,
    Column('Date', Text),
    Column('Description (21397400) BFAMIL', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bgoldm = Table(
    '_bgoldm', metadata,
    Column('Date', Text),
    Column('Description (90168800) BGOLDM', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bhasav = Table(
    '_bhasav', metadata,
    Column('Date', Text),
    Column('Description (00699174) BHASAV', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bhault = Table(
    '_bhault', metadata,
    Column('Date', Text),
    Column('Description (00624545) BHAULT', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bmetro = Table(
    '_bmetro', metadata,
    Column('Date', Text),
    Column('Description (11220495) BMETRO', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bmocha = Table(
    '_bmocha', metadata,
    Column('Date', Text),
    Column('Description', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bmofwn = Table(
    '_bmofwn', metadata,
    Column('Date', Text),
    Column('Description', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bmokid = Table(
    '_bmokid', metadata,
    Column('Date', Text),
    Column('Description (Kids pot) BMOKID', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bmonzo = Table(
    '_bmonzo', metadata,
    Column('Date', Text),
    Column('Description (39488204) BMONZO', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bmopar = Table(
    '_bmopar', metadata,
    Column('Date', Text),
    Column('Description () BMOPAR', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bmosav = Table(
    '_bmosav', metadata,
    Column('Date', Text),
    Column('Description () BMOSAV', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bnspbz = Table(
    '_bnspbz', metadata,
    Column('Date', Text),
    Column('Description () BNSPBZ', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__boaisa = Table(
    '_boaisa', metadata,
    Column('Date', Text),
    Column('Description (23111536) BOAISA', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__boakno = Table(
    '_boakno', metadata,
    Column('Date', Text),
    Column('Description (20629212) BOAKNO', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__boxbur = Table(
    '_boxbur', metadata,
    Column('Date', Text),
    Column('Description (62009202) BOXBUR', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bpaypa = Table(
    '_bpaypa', metadata,
    Column('Date', Text),
    Column('Description () BPAYPA', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bposto = Table(
    '_bposto', metadata,
    Column('Date', Text),
    Column('Description (22546266)', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bsaisa = Table(
    '_bsaisa', metadata,
    Column('Date', Text),
    Column('Description (36519614) BSAISA', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bsanta = Table(
    '_bsanta', metadata,
    Column('Date', Text),
    Column('Description (36517881) BSANTA', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bsasa2 = Table(
    '_bsasa2', metadata,
    Column('Date', Text),
    Column('Description (19050556) BSASA2', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bsasa3 = Table(
    '_bsasa3', metadata,
    Column('Date', Text),
    Column('Description () BSASA3', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bsasav = Table(
    '_bsasav', metadata,
    Column('Date', Text),
    Column('Description', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bsatax = Table(
    '_bsatax', metadata,
    Column('Date', Text),
    Column('Description (39563359) BSATAX', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__btes01 = Table(
    '_btes01', metadata,
    Column('Date', Text),
    Column('Description (5186 5250 0916 6233)', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__btesco = Table(
    '_btesco', metadata,
    Column('Date', Text),
    Column('Description (5186 5289 6842 5509) BTESCO', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__btrisa = Table(
    '_btrisa', metadata,
    Column('Date', Text),
    Column('Description (34655017) BTRISA', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bvanga = Table(
    '_bvanga', metadata,
    Column('Date', Text),
    Column('Description (VG0640344) BVANGA', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float),
    Column('Cash balance', Text),
    Column('Investment date', Text),
    Column('Quantity', Text),
    Column('Price', Text),
    Column('Cost', Text),
    Column('Amount tallies?', Text),
    Column('Total cost', Text),
    Column('Total quantity', Text)
)


t__bvmisa = Table(
    '_bvmisa', metadata,
    Column('Date', Text),
    Column('Description (75378384) BVMISA', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bvmsav = Table(
    '_bvmsav', metadata,
    Column('Date', Text),
    Column('Description (73308643) BVMSAV', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__bwalle = Table(
    '_bwalle', metadata,
    Column('Date', Text),
    Column('Description () BWALLE', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__clloyd = Table(
    '_clloyd', metadata,
    Column('Date', Text),
    Column('Description (46555963) CLLOYD', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__cmetro = Table(
    '_cmetro', metadata,
    Column('Date', Text),
    Column('Description (21865014) CMETRO', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__cvitra = Table(
    '_cvitra', metadata,
    Column('Date', Text),
    Column('Description (Loan Charlie) CVITRA', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__jfixes = Table(
    '_jfixes', metadata,
    Column('Date', Text),
    Column('Description (Hack) JFIXES', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__jsanta = Table(
    '_jsanta', metadata,
    Column('Date', Text),
    Column('Description (10518955) JSANTA', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__jwaleu = Table(
    '_jwaleu', metadata,
    Column('Date', Text),
    Column('Description', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float),
    Column('Exchange rate (GBP/EUR)', Text),
    Column('Credit (EUR)', Text),
    Column('Debit (EUR)', Text),
    Column('Balance (EUR)', Text)
)


t__samazo = Table(
    '_samazo', metadata,
    Column('Date', Text),
    Column('Description', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float),
    Column('Actual note', Text),
    Column('Payment type', Text),
    Column('Order', Text),
    Column('Order link', Text)
)


t__schase = Table(
    '_schase', metadata,
    Column('Date', Text),
    Column('Description (81192958) SCHASE', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__schbst = Table(
    '_schbst', metadata,
    Column('Date', Text),
    Column('Description () SCHBST', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__schrnd = Table(
    '_schrnd', metadata,
    Column('Date', Text),
    Column('Description () SCHRND', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__schsav = Table(
    '_schsav', metadata,
    Column('Date', Text),
    Column('Description (40493478) SCHSAV', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__scois2 = Table(
    '_scois2', metadata,
    Column('Date', Text),
    Column('Description (76987257) SCOIS2', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__scoisa = Table(
    '_scoisa', metadata,
    Column('Date', Text),
    Column('Description (91230051) SCOISA', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__scoloy = Table(
    '_scoloy', metadata,
    Column('Date', Text),
    Column('Description (34803313) SCOLOY', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__sfamil = Table(
    '_sfamil', metadata,
    Column('Date', Text),
    Column('Description (2006034051) SFAMIL', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__sgoldm = Table(
    '_sgoldm', metadata,
    Column('Date', Text),
    Column('Description (70520307) SGOLDM', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__sjl3bh = Table(
    '_sjl3bh', metadata,
    Column('Date', Text),
    Column('Description () SJL3BH', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float),
    Column('Date from', Text),
    Column('Date to', Text)
)


t__ski3bh = Table(
    '_ski3bh', metadata,
    Column('Date', Text),
    Column('Description () SKI3BH', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float),
    Column('Date from', Text),
    Column('Date to', Text)
)


t__skrooo = Table(
    '_skrooo', metadata,
    Column('Date', Text),
    Column('Description (00097740) SKROOO', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__smetro = Table(
    '_smetro', metadata,
    Column('Date', Text),
    Column('Description (11172814) SMETRO', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__smonz1 = Table(
    '_smonz1', metadata,
    Column('Date', Text),
    Column('Description', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__smonzo = Table(
    '_smonzo', metadata,
    Column('Date', Text),
    Column('Description (46416566) SMONZO', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__snspbz = Table(
    '_snspbz', metadata,
    Column('Date', Text),
    Column('Description (3062311218)', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float),
    Column('Bond numbers', Text)
)


t__soaisa = Table(
    '_soaisa', metadata,
    Column('Date', Text),
    Column('Description (23110731) SOAISA', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__soakno = Table(
    '_soakno', metadata,
    Column('Date', Text),
    Column('Description (20629199) SOAKNO', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__soxbur = Table(
    '_soxbur', metadata,
    Column('Date', Text),
    Column('Description (16009814) SOXBUR', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__spaypa = Table(
    '_spaypa', metadata,
    Column('Date', Text),
    Column('Description () SPAYPA', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__sposto = Table(
    '_sposto', metadata,
    Column('Date', Text),
    Column('Description (22517182) SPOSTO', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__srevol = Table(
    '_srevol', metadata,
    Column('Date', Text),
    Column('Description (37193872) SREVOL', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float),
    Column('Exchange rate', Text),
    Column('Euro credit', Text),
    Column('Euro debit', Text),
    Column('Euro balance', Text)
)


t__ssacr1 = Table(
    '_ssacr1', metadata,
    Column('Date', Text),
    Column('Description (5229 4865 2531 5748) SSACR1', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__ssacrd = Table(
    '_ssacrd', metadata,
    Column('Date', Text),
    Column('Description (5229 4890 4592 9253 / 4695 5562) SSACRD', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('#REF!', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float),
    Column('Card', Text),
    Column('Actual Note', Text)
)


t__ssaisa = Table(
    '_ssaisa', metadata,
    Column('Date', Text),
    Column('Description (84123081) SSAISA', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__ssant1 = Table(
    '_ssant1', metadata,
    Column('Date', Text),
    Column('Description (04898686) SSANT1', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__ssanta = Table(
    '_ssanta', metadata,
    Column('Date', Text),
    Column('Description (04898686) SSANTA', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__ssaprm = Table(
    '_ssaprm', metadata,
    Column('Date', Text),
    Column('Description (18227933) SSAPRM', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__ssaz01 = Table(
    '_ssaz01', metadata,
    Column('Date', Text),
    Column('Description (24027843) SSAZ01', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__ssaz02 = Table(
    '_ssaz02', metadata,
    Column('Date', Text),
    Column('Description (40470306) SSAZ02', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__ssaz03 = Table(
    '_ssaz03', metadata,
    Column('Date', Text),
    Column('Description (R26745278) SSAZ03', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__sstarb = Table(
    '_sstarb', metadata,
    Column('Date', Text),
    Column('Description', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__sstarl = Table(
    '_sstarl', metadata,
    Column('Date', Text),
    Column('Description (53686763) SSTARL', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__stafix = Table(
    '_stafix', metadata,
    Column('Date', Text),
    Column('Description', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__stasav = Table(
    '_stasav', metadata,
    Column('Date', Text),
    Column('Description (43722665) STASAV', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__stes01 = Table(
    '_stes01', metadata,
    Column('Date', Text),
    Column('Description (4305 6713 8320 8057)', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__stes02 = Table(
    '_stes02', metadata,
    Column('Date', Text),
    Column('Description (5521 8885 0217 8426)', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__stes03 = Table(
    '_stes03', metadata,
    Column('Date', Text),
    Column('Description (5521 8889 7866 6243) STES03', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__stesco = Table(
    '_stesco', metadata,
    Column('Date', Text),
    Column('Description (5521 8889 8404 4278) STESCO', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__strisa = Table(
    '_strisa', metadata,
    Column('Date', Text),
    Column('Description (34566437) STRISA', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__svanga = Table(
    '_svanga', metadata,
    Column('Date', Text),
    Column('Description (VG0640058) SVANGA', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float),
    Column('Cash balance', Text),
    Column('Investment date', Text),
    Column('Quantity', Text),
    Column('Price', Text),
    Column('Cost', Text),
    Column('Amount tallies?', Text),
    Column('Total cost', Text),
    Column('Total quantity', Text)
)


t__svi2tj = Table(
    '_svi2tj', metadata,
    Column('Date', Text),
    Column('Description (Virtual SW11 2TJ HMRC record) SVI2TJ', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float),
    Column('Range', Text),
    Column('Query', Text)
)


t__svi3bh = Table(
    '_svi3bh', metadata,
    Column('Date', Text),
    Column('Description () SVI3BH', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float),
    Column('Date from', Text),
    Column('Date to', Text)
)


t__svigb2 = Table(
    '_svigb2', metadata,
    Column('Date', Text),
    Column('Description (Glenburnie Renovation Loan) SVIGB2', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float),
    Column('Account', Text),
    Column('Date2', Text),
    Column('Description2', Text),
    Column('Credit2', Text),
    Column('Debit2', Text),
    Column('Note2', Text),
    Column('CPTY2', Text),
    Column('CPTY Date2', Text),
    Column('Balance2', Text)
)


t__svigbl = Table(
    '_svigbl', metadata,
    Column('Date', Text),
    Column('Description (Glenburnie Investment Loan) SVIGBL', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float),
    Column('Account', Text),
    Column('Date2', Text),
    Column('Description2', Text),
    Column('Credit2', Text),
    Column('Debit2', Text),
    Column('Note2', Text),
    Column('CPTY2', Text),
    Column('CPTY Date2', Text),
    Column('Balance2', Text)
)


t__sviirf = Table(
    '_sviirf', metadata,
    Column('Date', Text),
    Column('Description () SVIIRF', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float),
    Column('Key', Text),
    Column('Date2', Text),
    Column('Description2', Text),
    Column('Credit2', Text),
    Column('Debit2', Text),
    Column('Note2', Text),
    Column('Key2', Text),
    Column('a', Text),
    Column('Key3', Text)
)


t__svmisa = Table(
    '_svmisa', metadata,
    Column('Date', Text),
    Column('Description (75393286) SVMISA', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__svmsav = Table(
    '_svmsav', metadata,
    Column('Date', Text),
    Column('Description', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__swalle = Table(
    '_swalle', metadata,
    Column('Date', Text),
    Column('Description () SWALLE', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t__szopa1 = Table(
    '_szopa1', metadata,
    Column('Date', Text),
    Column('Description () SZOPA1', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t_account_balances = Table(
    'account_balances', metadata,
    Column('Key', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Balance', Float)
)


t_assets = Table(
    'assets', metadata,
    Column('Asset', Text),
    Column('Asset value', Float),
    Column('isLiquid', Text),
    Column('Notes', Text)
)


t_balance_sheet = Table(
    'balance_sheet', metadata,
    Column('Item', Text),
    Column('Asset value', Float)
)


t_bank_accounts = Table(
    'bank_accounts', metadata,
    Column('Key', Text),
    Column('Full account name', Text),
    Column('Owner code', Text),
    Column('Owner', Text),
    Column('Institution code', Text),
    Column('Institution', Text),
    Column('Account code', Text),
    Column('Account name', Text),
    Column('Account purpose', Text),
    Column('Date opened', Text),
    Column('Date closed', Text),
    Column('Check balance frequency', Text),
    Column('Balance', Float),
    Column('Account minimum', Float),
    Column('Debits due', Float),
    Column('Shortfall', Float),
    Column('Account maximum', Float),
    Column('Excess', Float),
    Column('Last updated', Text),
    Column('Sort code', Text),
    Column('Account number', Text),
    Column('Interest rate', Float),
    Column('Interest taxable?', Text),
    Column('Taxable interest', Float),
    Column('Interest payable (A or M)', Text),
    Column('Interest due date', Text),
    Column('Annual interest (AER)', Float),
    Column('Monthly interest', Float),
    Column('Change required', Float),
    Column('Fixed until date', Text),
    Column('Review date', Text),
    Column('Minimum today', Float),
    Column('Account type', Text),
    Column('Taxable transactions', Text),
    Column('IBAN', Text),
    Column('BIC', Text),
    Column('Data import', Text),
    Column('Our money', Text),
    Column('Records from', Text),
    Column('Records to', Text),
    Column('Credits due', Float),
    Column('Short label', Text),
    Column('Description', Text)
)


t_bank_cards = Table(
    'bank_cards', metadata,
    Column('Last 4 digits', Text),
    Column('Account', Text),
    Column('Valid from', Text),
    Column('Expiry date', Text),
    Column('CVC', Text),
    Column('Name on card', Text),
    Column('Location', Text),
    Column('Account key', Text),
    Column('Card number', Text),
    Column('Active', Text),
    Column('Issue number', Text),
    Column('Card type', Text),
    Column('Card network', Text),
    Column('Virtual card number', Text),
    Column('Clubcard number', Text)
)


t_bank_credits_due = Table(
    'bank_credits_due', metadata,
    Column('Key', Text),
    Column('Amount', Float),
    Column('Blank', Text),
    Column('Headers', Text),
    Column('Range', Text),
    Column('Description', Text),
    Column('Query', Text)
)


t_bank_debits_due = Table(
    'bank_debits_due', metadata,
    Column('Key', Text),
    Column('Amount', Float),
    Column('Blank', Text),
    Column('Headers', Text),
    Column('Range', Text),
    Column('Description', Text),
    Column('Query', Text)
)


t_bank_interest = Table(
    'bank_interest', metadata,
    Column('Owner', Text),
    Column('Interest', Float),
    Column('Taxable interest', Float)
)


t_budget = Table(
    'budget', metadata,
    Column('Section', Text),
    Column('Annual', Float),
    Column('Monthly', Float),
    Column('Weekly', Float),
    Column('Daily', Float),
    Column('Type', Text),
    Column('Description', Text),
    Column('2023 to 2024', Text)
)


t_budget_annual_change = Table(
    'budget_annual_change', metadata,
    Column('Date', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Nett', Float)
)


t_budget_annual_transactions = Table(
    'budget_annual_transactions', metadata,
    Column('Date', Text),
    Column('Description', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Account', Text),
    Column('Payment type', Text),
    Column('Category', Text),
    Column('Subcategory', Text),
    Column('Frequency (years)', Text),
    Column('Day', Text),
    Column('Month', Text),
    Column('Payment Method', Text),
    Column('Day of week', Text),
    Column('Key', Text)
)


t_budget_breakdown = Table(
    'budget_breakdown', metadata,
    Column('Tax year', Text),
    Column('Category group', Text),
    Column('Category', Text),
    Column('Total credit', Float),
    Column('Total debit', Float),
    Column('Nett', Float)
)


t_budget_daily = Table(
    'budget_daily', metadata,
    Column('Date', Text),
    Column('Description', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('Key', Text),
    Column('Balance', Float),
    Column('Blank', Text),
    Column('Section', Text),
    Column('Where', Text),
    Column('Select', Text),
    Column('Label', Text),
    Column('Range', Text),
    Column('Query', Text),
    Column('Construct', Text)
)


t_budget_four_weekly_change = Table(
    'budget_four_weekly_change', metadata,
    Column('Next due date', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Nett', Float)
)


t_budget_four_weekly_transactions = Table(
    'budget_four_weekly_transactions', metadata,
    Column('Next due date', Text),
    Column('Description', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('Key', Text),
    Column('Day of week', Text),
    Column('Account', Text),
    Column('Frequency', Text),
    Column('Category', Text),
    Column('Subcategory', Text),
    Column('Annual', Float),
    Column('Monthly', Float),
    Column('Day', Text),
    Column('Payment type', Text)
)


t_budget_monthly_change = Table(
    'budget_monthly_change', metadata,
    Column('Day', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Nett', Float)
)


t_budget_monthly_transactions = Table(
    'budget_monthly_transactions', metadata,
    Column('Date', Text),
    Column('Description', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('Key', Text),
    Column('Day of month', Text),
    Column('Account', Text),
    Column('Payment method', Text)
)


t_budget_predicted_spend = Table(
    'budget_predicted_spend', metadata,
    Column('Day', Text),
    Column('Date', Text),
    Column('Balance', Float),
    Column('Change', Float),
    Column('Weekly', Float),
    Column('Four weekly', Float),
    Column('Monthly', Float),
    Column('Annual', Float),
    Column('Sporadic', Float)
)


t_budget_sporadic_change = Table(
    'budget_sporadic_change', metadata,
    Column('Date', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Nett', Float)
)


t_budget_sporadic_transactions = Table(
    'budget_sporadic_transactions', metadata,
    Column('Date', Text),
    Column('Description', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('Key', Text),
    Column('Payment type', Text)
)


t_budget_weekly_change = Table(
    'budget_weekly_change', metadata,
    Column('Day of week', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Nett', Float)
)


t_budget_weekly_transactions = Table(
    'budget_weekly_transactions', metadata,
    Column('Next due date', Text),
    Column('Description', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('Key', Text),
    Column('Day of week', Text),
    Column('Account', Text),
    Column('Frequency', Text),
    Column('Category', Text),
    Column('Subcategory', Text),
    Column('Annual', Float),
    Column('Monthly', Float),
    Column('Day', Text),
    Column('Payment type', Text)
)


t_categories = Table(
    'categories', metadata,
    Column('Category', Text),
    Column('How many', Text),
    Column('HMRC page', Text),
    Column('HMRC box', Text),
    Column('Description', Text),
    Column('Category group', Text)
)


t_category_clash = Table(
    'category_clash', metadata,
    Column('Key', Text),
    Column('Description and note', Text),
    Column('Category', Text),
    Column('Combined', Text),
    Column('Category 2', Text),
    Column('Match', Text),
    Column('Filter', Text),
    Column('Category 3', Text),
    Column('M2', Text)
)


t_category_clash_data = Table(
    'category_clash_data', metadata,
    Column('COMBINED', Text),
    Column('CATEGORY', Text),
    Column('MATCH', Text)
)


t_category_groups = Table(
    'category_groups', metadata,
    Column('Category group', Text),
    Column('Category group type', Text),
    Column('Blank', Text),
    Column('Sorted by type', Text),
    Column('Type', Text)
)


t_check_fixed_amounts = Table(
    'check_fixed_amounts', metadata,
    Column('Tax year', Text),
    Column('Category', Text),
    Column('Fixed amount', Float),
    Column('Dynamic amount', Float),
    Column('Tolerance', Float),
    Column('Mismatch', Text),
    Column('Note', Text)
)


t_config = Table(
    'config', metadata,
    Column('Key', Text),
    Column('Value', Text),
    Column('Ian B', Text),
    Column('Ian S', Text),
    Column('URL', Text)
)


t_dependencies = Table(
    'dependencies', metadata,
    Column('Sheet ID', Text),
    Column('Derived sheet name', Text),
    Column('Used by', Text)
)


t_description_replacements = Table(
    'description_replacements', metadata,
    Column('Description', Text),
    Column('Replacement', Text)
)


t_gift_recipients = Table(
    'gift_recipients', metadata,
    Column('Name', Text),
    Column('Birth day', Text),
    Column('Birth month', Text),
    Column('Birth year', Text),
    Column('Tier', Text),
    Column('Amount', Float),
    Column('Connection', Text)
)


t_gift_tiers = Table(
    'gift_tiers', metadata,
    Column('Tier', Text),
    Column('Amount', Float),
    Column('Recipients', Text)
)


t_hmrc_b = Table(
    'hmrc_b', metadata,
    Column('Tax Year', Text),
    Column('2023 to 2024', Text),
    Column('2022 to 2023', Text),
    Column('a', Text),
    Column('b', Text),
    Column('c', Text),
    Column('d', Text),
    Column('Date', Text),
    Column('Description', Text),
    Column('Fownes St Rent', Text),
    Column('FS Reclaimable', Text),
    Column('FS Profit', Text)
)


t_hmrc_businesses = Table(
    'hmrc_businesses', metadata,
    Column('Business name', Text),
    Column('Business description', Text),
    Column('Start date', Text),
    Column('End date', Text)
)


t_hmrc_categories = Table(
    'hmrc_categories', metadata,
    Column('Category', Text)
)


t_hmrc_constants = Table(
    'hmrc_constants', metadata,
    Column('Tax Year', Text),
    Column('2024 to 2025', Text),
    Column('2023 to 2024', Text),
    Column('2022 to 2023', Text),
    Column('2021 to 2022', Text)
)


t_hmrc_fields = Table(
    'hmrc_fields', metadata,
    Column('Section', Text),
    Column('Order', Text),
    Column('Subsection', Text),
    Column('HMRC', Text),
    Column('Field', Text)
)


t_hmrc_income_stream_types = Table(
    'hmrc_income_stream_types', metadata,
    Column('Key', Text),
    Column('Type', Text)
)


t_hmrc_income_streams = Table(
    'hmrc_income_streams', metadata,
    Column('Key', Text),
    Column('Stream type', Text),
    Column('Income stream', Text)
)


t_hmrc_l1_3bh = Table(
    'hmrc_l1_3bh', metadata,
    Column('Tax Year', Text),
    Column('Rent Income', Text),
    Column('Management Fee', Text),
    Column('Replacement Costs', Text),
    Column('Service charges', Text),
    Column('Description', Text),
    Column('Total Expenses', Text),
    Column('Rent, rates, insurance, ground rents etc', Text),
    Column('Cost of replacing domestic items', Text),
    Column('Legal, management and other professional fees', Text),
    Column('Taxable profit', Text)
)


t_hmrc_pensions = Table(
    'hmrc_pensions', metadata,
    Column('Owner', Text),
    Column('Who', Text),
    Column('Base year', Text),
    Column('Tax Year', Text),
    Column('Personal contribution', Text),
    Column('Tax relief', Text),
    Column('Full contribution', Text),
    Column('Blank', Text),
    Column('Query', Text),
    Column('Data', Text)
)


t_hmrc_people_details = Table(
    'hmrc_people_details', metadata,
    Column('Code', Text),
    Column('When', Text),
    Column('UTR', Text),
    Column('UTR check digit', Text),
    Column('NINO', Text),
    Column('Address correct?', Text),
    Column('Taxpayer residency', Text),
    Column('Marital status', Text),
    Column('Blind?', Text),
    Column('Student Loan?', Text),
    Column('Spouse code', Text),
    Column('Marriage date', Text)
)


t_hmrc_queries = Table(
    'hmrc_queries', metadata,
    Column('Query ID', Text),
    Column('Description', Text),
    Column('Select', Text),
    Column('From', Text),
    Column('Where', Text),
    Column('Group by', Text),
    Column('Label', Text),
    Column('Query', Text),
    Column('Columns', Text)
)


t_hmrc_questions = Table(
    'hmrc_questions', metadata,
    Column('Question', Text),
    Column('String length', Text),
    Column('Max string length', Text),
    Column('54', Text)
)


t_hmrc_questions_by_year = Table(
    'hmrc_questions_by_year', metadata,
    Column('Question', Text),
    Column('Order', Text),
    Column('Page label', Text),
    Column('Header', Text),
    Column('Box', Text),
    Column('2023 to 2024', Text)
)


t_hmrc_s = Table(
    'hmrc_s', metadata,
    Column('Question', Text),
    Column('Category', Text),
    Column('2024 to 2025', Text),
    Column('2023 to 2024', Text),
    Column('2022 to 2023', Text),
    Column('2021 to 2022', Text),
    Column('2020 to 2021', Text),
    Column('2019 to 2020', Text),
    Column('2018 to 2019', Text),
    Column('2017 to 2018', Text)
)


t_hmrc_self_assessment = Table(
    'hmrc_self-assessment', metadata,
    Column('Section', Text),
    Column('Question', Text),
    Column('Ian Leonard Bernard Answer 2023 to 2024', Text),
    Column('Ian Muir Sweeney Answer 2023 to 2024', Text)
)


t_hmrc_self_employment = Table(
    'hmrc_self-employment', metadata,
    Column('Owner', Text),
    Column('Who', Text),
    Column('Base year', Text),
    Column('Tax year', Text),
    Column('Income source', Text),
    Column('Income', Text),
    Column('Expense', Text),
    Column('Trading allowance', Text),
    Column('Traditional nett', Text),
    Column('TA nett', Text),
    Column('Income query', Text),
    Column('Expense query', Text),
    Column('Data', Text)
)


t_hmrc_tax_years = Table(
    'hmrc_tax_years', metadata,
    Column('Tax year', Text)
)


t_hmrc_totals_by_bank = Table(
    'hmrc_totals_by_bank', metadata,
    Column('Tax year', Text),
    Column('Category', Text),
    Column('Bank', Text),
    Column('Total', Text)
)


t_hmrc_totals_by_tax_year_and_category = Table(
    'hmrc_totals_by_tax_year_and_category', metadata,
    Column('Tax year', Text),
    Column('Category', Text),
    Column('Total', Text)
)


t_hmrc_transactions = Table(
    'hmrc_transactions', metadata,
    Column('Tax year', Text),
    Column('Category', Text),
    Column('Bank', Text),
    Column('Date', Text),
    Column('Description', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text)
)


t_imported_data = Table(
    'imported_data', metadata,
    Column('Key', Text),
    Column('Name', Text),
    Column('URL', Text),
    Column('Used by', Text)
)


t_income_interest = Table(
    'income_interest', metadata,
    Column('Source', Text),
    Column('Taxable?', Text),
    Column('Annual', Float),
    Column('Monthly', Float),
    Column('Weekly', Float),
    Column('Daily', Float)
)


t_income_planning = Table(
    'income_planning', metadata,
    Column('Income for', Text),
    Column('Income sources', Text),
    Column('Income type', Text),
    Column('Income amount', Text),
    Column('Taxable amount', Text)
)


t_income_property = Table(
    'income_property', metadata,
    Column('Who', Text),
    Column('Source', Text),
    Column('Annual', Float),
    Column('Monthly', Float),
    Column('Weekly', Float),
    Column('Daily', Float),
    Column('a', Text),
    Column('Total Annual Property Income', Text)
)


t_income_self_employment = Table(
    'income_self-employment', metadata,
    Column('Who', Text),
    Column('Source', Text),
    Column('Annual', Float),
    Column('Monthly', Float),
    Column('Weekly', Float),
    Column('Daily', Float),
    Column('a', Text),
    Column('Total Annual Self Employment Income', Text)
)


t_institutions = Table(
    'institutions', metadata,
    Column('Code', Text),
    Column('Institution', Text),
    Column('Note', Text),
    Column('Group', Text)
)


t_irf_xfer_check = Table(
    'irf_xfer_check', metadata,
    Column('Date', Text),
    Column('Description (10255868) AHALIF', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Counterparty date', Text),
    Column('-Nett', Text),
    Column('WHERE', Text),
    Column('a', Text),
    Column('b', Text),
    Column('c', Text),
    Column('d', Text),
    Column('e', Text),
    Column('f', Text),
    Column('g', Text),
    Column('h', Text),
    Column('i', Text),
    Column('j', Text),
    Column('k', Text),
    Column('l', Text),
    Column('m', Text),
    Column('n', Text),
    Column('o', Text),
    Column('p', Text),
    Column('q', Text),
    Column('r', Text)
)


t_liabilities = Table(
    'liabilities', metadata,
    Column('Liability', Text),
    Column('Value', Text)
)


t_loan_adam_perry = Table(
    'loan_adam_perry', metadata,
    Column('Date', Text),
    Column('Description', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t_loan_charlie_bernard = Table(
    'loan_charlie_bernard', metadata,
    Column('Date', Text),
    Column('Description', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t_loan_glenburnie = Table(
    'loan_glenburnie', metadata,
    Column('Date', Text),
    Column('Description', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('Balance', Float),
    Column('Key', Text)
)


t_loan_linda_hayman = Table(
    'loan_linda_hayman', metadata,
    Column('Date', Text),
    Column('Description', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Balance', Float)
)


t_loans = Table(
    'loans', metadata,
    Column('Key', Text),
    Column('Date', Text),
    Column('Description', Text),
    Column('Description + Note', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Who', Text),
    Column('Amount Owed To Us', Text)
)


t_money_owed_by_us = Table(
    'money_owed_by_us', metadata,
    Column('Owed To', Text),
    Column('Amount', Float)
)


t_money_owed_to_us = Table(
    'money_owed_to_us', metadata,
    Column('Owed By', Text),
    Column('Amount', Float)
)


t_my_formulas = Table(
    'my_formulas', metadata,
    Column('Description', Text),
    Column('Formula (follow the link for an example)', Text),
    Column('a', Text),
    Column('b', Text),
    Column('c', Text),
    Column('d', Text),
    Column('e', Text),
    Column('f', Text)
)


t_my_formulas_examples = Table(
    'my_formulas_examples', metadata,
    Column('Formula Description', Text),
    Column('Result', Text),
    Column('Parameter Name', Text),
    Column('Parameter Value', Text)
)


t_not_in_transaction_categories = Table(
    'not_in_transaction_categories', metadata,
    Column('Account + Description + Note', Text),
    Column('How Many?', Text)
)


t_our_money = Table(
    'our_money', metadata,
    Column('Balance as at', Text),
    Column('Account name', Text),
    Column('Balance', Float),
    Column('Fixed until date', Text),
    Column('Sort code', Text),
    Column('Account number', Text)
)


t_our_money_history = Table(
    'our_money_history', metadata,
    Column('Balance as at', Text),
    Column('Date 45614', Text),
    Column('Date 45538', Text),
    Column('Date 45478', Text),
    Column('Date 45473', Text),
    Column('Date 45447', Text)
)


t_pension_uk_gov = Table(
    'pension_uk_gov', metadata,
    Column('Account Owner', Text),
    Column('Ian S', Text),
    Column('Ian B', Text),
    Column('Combined', Text)
)


t_pension_vanguard = Table(
    'pension_vanguard', metadata,
    Column('Account owner', Text),
    Column('Ian B', Text),
    Column('Ian S', Text),
    Column('Combined', Text)
)


t_pension_zurich = Table(
    'pension_zurich', metadata,
    Column('Account owner', Text),
    Column('Ian S', Text)
)


t_pensions = Table(
    'pensions', metadata,
    Column('Account', Text),
    Column('Ian S Vanguard', Text),
    Column('Ian S Zurich', Text),
    Column('Ian S UK Gov', Text),
    Column('Ian B UK Gov', Text),
    Column('Ian B Vanguard', Text),
    Column('Combined TOTAL', Text)
)


t_people = Table(
    'people', metadata,
    Column('Code', Text),
    Column('First name', Text),
    Column('Middle name', Text),
    Column('Surname', Text),
    Column('Date of birth', Text),
    Column('Phone number', Text),
    Column('Address line 1', Text),
    Column('Address line 2', Text),
    Column('City', Text),
    Column('Postcode', Text),
    Column('Person', Text),
    Column('Full name', Text),
    Column('Address', Text)
)


t_property = Table(
    'property', metadata,
    Column('Property', Text),
    Column('Valuation type', Text),
    Column('Amount', Float),
    Column('Last Updated', Text),
    Column('Annual income', Text),
    Column('Annual expense', Text)
)


t_property_l1_3bh = Table(
    'property_l1_3bh', metadata,
    Column('Label', Text),
    Column('Description', Text),
    Column('Monthly income', Text),
    Column('Annual income', Text),
    Column('Monthly expense', Text),
    Column('Annual expense', Text),
    Column('Monthly profit/loss', Text),
    Column('Annual profit/loss', Text),
    Column('Paid to', Text),
    Column('How paid', Text)
)


t_property_sw11_2tj = Table(
    'property_sw11_2tj', metadata,
    Column('Label', Text),
    Column('Description', Text),
    Column('Monthly income', Text),
    Column('Annual income', Text),
    Column('Monthly expense', Text),
    Column('Annual expense', Text),
    Column('Monthly profit/loss', Text),
    Column('Annual profit/loss', Text),
    Column('Paid to', Text),
    Column('How paid', Text)
)


t_property_sw17_0sr = Table(
    'property_sw17_0sr', metadata,
    Column('Address', Text),
    Column('Note', Text),
    Column('Monthly', Float),
    Column('Annual', Float),
    Column('URL', Text)
)


t_property_sw18_3pt = Table(
    'property_sw18_3pt', metadata,
    Column('Address', Text),
    Column('5 Leckford Road', Text),
    Column('Share', Text),
    Column('URL', Text)
)


t_queries = Table(
    'queries', metadata,
    Column('Query ID', Text),
    Column('Description', Text),
    Column('Select', Text),
    Column('From', Text),
    Column('Where', Text),
    Column('Group by', Text),
    Column('Label', Text),
    Column('Query', Text),
    Column('Construct', Text),
    Column('Columns', Text)
)


t_query_lookup = Table(
    'query_lookup', metadata,
    Column('Labels', Text),
    Column('Values', Text),
    Column('Column 1', Text),
    Column('a1', Text),
    Column('a2', Text),
    Column('a3', Text),
    Column('a4', Text),
    Column('a5', Text),
    Column('a6', Text),
    Column('a7', Text),
    Column('a8', Text),
    Column('a9', Text),
    Column('a10', Text),
    Column('a11', Text),
    Column('a12', Text),
    Column('a13', Text),
    Column('a14', Text),
    Column('a15', Text),
    Column('a16', Text),
    Column('a17', Text),
    Column('a18', Text),
    Column('a19', Text),
    Column('a20', Text),
    Column('a21', Text),
    Column('a22', Text),
    Column('a23', Text)
)


t_receipts = Table(
    'receipts', metadata,
    Column('Date', Text),
    Column('Payee', Text),
    Column('Description', Text),
    Column('Amount', Float),
    Column('Account', Text),
    Column('Image', Text),
    Column('Payment Method', Text),
    Column('Payment Method X', Text)
)


t_shares = Table(
    'shares', metadata,
    Column('Shares', Text),
    Column('Institution', Text),
    Column('Account name', Text),
    Column('How many', Text),
    Column('Price per item', Text),
    Column('Value', Text),
    Column('Estimated cost of selling', Text),
    Column('Nett value', Text),
    Column('As at', Text),
    Column('Account balance', Text),
    Column('Last updated', Text),
    Column('Account number', Text),
    Column('Type', Text)
)


t_spreadsheet_summary = Table(
    'spreadsheet_summary', metadata,
    Column('Sheet name', Text),
    Column('Last row', Text),
    Column('Last column', Text),
    Column('Max rows', Text),
    Column('Max columns', Text),
    Column('Account?', Text),
    Column('Budget?', Text)
)


t_summary = Table(
    'summary', metadata,
    Column('Full account name', Text),
    Column('Balance', Float),
    Column('Interest rate', Float),
    Column('Annual interest (AER)', Float),
    Column('Fixed until date', Text)
)


t_transactions = Table(
    'transactions', metadata,
    Column('Key', Text),
    Column('Date', Text),
    Column('Description', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Nett', Float),
    Column('Tax year', Text),
    Column('Description + Note', Text),
    Column('Account + Description + Note', Text),
    Column('Category', Text),
    Column('Category group', Text),
    Column('Available', Text),
    Column('Xfer', Text),
    Column('Reverse', Text),
    Column('Xfer date', Text),
    Column('Account type', Text),
    Column("Helper for 'Check fixed amounts'", Text)
)


t_transactions_builder = Table(
    'transactions_builder', metadata,
    Column('116', Text),
    Column('rows on this sheet', Text),
    Column('a1', Text),
    Column('a2', Text),
    Column('a3', Text),
    Column('a4', Text),
    Column('a5', Text)
)


t_transactions_by_category = Table(
    'transactions_by_category', metadata,
    Column('Tax year', Text),
    Column('Category', Text),
    Column('Total credit', Float),
    Column('Total debit', Float),
    Column('Nett', Float)
)


t_transactions_by_category_group = Table(
    'transactions_by_category_group', metadata,
    Column('Tax year', Text),
    Column('Category group', Text),
    Column('Total credit', Float),
    Column('Total debit', Float),
    Column('Nett', Float)
)


t_transactions_by_date = Table(
    'transactions_by_date', metadata,
    Column('Key', Text),
    Column('Date', Text),
    Column('Description', Text),
    Column('Credit', Float),
    Column('Debit', Float),
    Column('Note', Text),
    Column('CPTY', Text),
    Column('CPTY Date', Text),
    Column('Nett', Float),
    Column('Tax year', Text),
    Column('Description + Note', Text),
    Column('Account + Description + Note', Text),
    Column('Category', Text),
    Column('Category group', Text),
    Column('Available', Text),
    Column('Xfer', Text),
    Column('Reverse', Text),
    Column('Xfer date', Text),
    Column('Account type', Text),
    Column("Helper for 'Check fixed amounts'", Text)
)


t_transactions_categories = Table(
    'transactions_categories', metadata,
    Column('Transaction Descriptions', Text),
    Column('How Many', Text),
    Column('Category', Text),
    Column('XLOOKUP category', Text)
)


t_uncategorised_by_amount = Table(
    'uncategorised_by_amount', metadata,
    Column('Tax year', Text),
    Column('Description + Note', Text),
    Column('Nett', Float)
)


t_uncategorised_by_date = Table(
    'uncategorised_by_date', metadata,
    Column('05/04/2022', Text),
    Column('Uncategorised OR unreconciled transactions after 05/04/2022', Text),
    Column('a', Text),
    Column('b', Text)
)


t_unreconciled = Table(
    'unreconciled', metadata,
    Column('Transactions!A1:O', Text),
    Column("WHERE M= 'Unreconciled'  ORDER BY B", Text),
    Column('a1', Text),
    Column('a2', Text),
    Column('a3', Text),
    Column('a4', Text),
    Column('a5', Text),
    Column('a6', Text),
    Column('a7', Text),
    Column('a8', Text),
    Column('a9', Text),
    Column('a10', Text),
    Column('a11', Text),
    Column('a12', Text),
    Column('a13', Text)
)


t_weekday = Table(
    'weekday', metadata,
    Column('Sunday', Text),
    Column('1', Text)
)


t_xfers_check = Table(
    'xfers_check', metadata,
    Column('Date', Text),
    Column('Full description', Text),
    Column('CPTY date', Text),
    Column('Date 2', Text),
    Column('Full description 2', Text),
    Column('CPTY date 2', Text)
)


t_xfers_mismatch = Table(
    'xfers_mismatch', metadata,
    Column('Date', Text),
    Column('Xfer', Text),
    Column('Mismatch', Text),
    Column('a', Text),
    Column('b', Text),
    Column('c', Text),
    Column('d', Text),
    Column('e', Text),
    Column('f', Text),
    Column('g', Text),
    Column('h', Text)
)


t_xfers_totals = Table(
    'xfers_totals', metadata,
    Column('Xfer', Text),
    Column('Total Nett', Text),
    Column('Reverse', Text),
    Column('Nett', Float),
    Column('Difference', Text)
)


t_xfers_totals_by_year = Table(
    'xfers_totals_by_year', metadata,
    Column('Tax year', Text),
    Column('Xfer', Text),
    Column('Total Nett', Text)
)

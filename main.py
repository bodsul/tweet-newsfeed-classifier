from API import API

#list labels
labels = {1: 'science, tech and health', 2:'business, economy and finance', 3: 'politics', 4: 'sports', 5:'religion/religious teachings', 6: 'entertainment', 7: 'jobs and careers', 8:'weather', 9:'other'}

#other represents 'event or news', 'fact or information sharing', 'personal' and random hard to classify tweets

sources={}

#list science and tech sources
sources['1'] = ['techreview', 'TechCrunch','ScienceTip', 'ScienceNews', 'sciam', 'ForbesTech', 'Techmeme', 'bbchealth','NatGeo', 'WomensHealthMag', 'MensHealthMag','guardianscience']

#list financial, business and economic sources
sources['2'] = ['FinancialTimes', 'RiskMagazine', 'StockTwits', 'Vanguard_Group', 'dealbook','hedge_funds', 'BloombergNews' , 'WSJbusiness', ]

#list political sources
sources['3']= ['_politicalworld', 'BBCPolitics', 'PoliticalTicker', 'ForeignPolicy', 'HuffPostPol', 'nprpolitics', 'CNNPolitics', 'AP_Politics']

#list sports sources
sources['4'] = ['espn', 'BBC Sport', 'Soccernet', 'GolfChannel','HBOboxing', 'NHL', 'NFL', 'MLB', 'Olympics', 'NBA']

#list religious sources
sources['5'] = ['news_va_en', 'Buddhism_Now', 'HinduismToday', 'Pearlsofprophet', 'YourJudaism', 'HuffPostRelig', 'RNS']

#list entertainment sources
sources['6'] = ['MTV', 'Rock Music', 'TheGRAMMYs', 'TheAcademy', 'bbcentertain',  'EntMagazine', 'EW', 'mashentertain', 'CBSShowbiz']

#job and careers sources
sources['7'] = ['GuardianCareers', 'CareerBuilder', 'LinkedIn', 'indeed', 'TweetMyJobs', 'USNewsCareers', 'UCSBcareer', 'BI_Careers']

#weather sources
sources['8'] = ['weatherchannel', 'bbcweather','wunderground', 'weathernetwork', 'capitalweather', 'CNNweather']

#random/other sources
sources['9'] = ['Seldomaniac', 'Callamasta', 'jwharris', 'don_brown', 'lou1derful', 'ChrisPawelski']

api = API(sources)
api.gettweets()
api.cleantweets()
api.tokenizetweets()
api.writetofile()
top = api.gettop()
api.getfeatures()
print top
print api.train()






import requests
from datetime import datetime
from twilio.rest import Client

MY_LAT = 30.268772
MY_LONG = 31.526516

account_sid = 'yours'
auth_token = 'yours'
client = Client(account_sid, auth_token)

INTEL_STOCK = "INTC"
intel = "Intel"

api_key_stock_api = "yours"
api_key_news_api = "yours"
api_key_currencylayer_api = "yours"
api_key_openweathermap_api = "yours"
api_key_metalpriceapi_api = "yours"

api_end_point_stock_api = "https://www.alphavantage.co/query"
api_end_point_news_api = "https://newsapi.org/v2/top-headlines"
api_end_point_openweathermap_api = "https://api.openweathermap.org/data/2.5/forecast"
api_end_point_metalpriceapi_api = "https://api.metalpriceapi.com/v1/latest"

parameters_for_stock_api = {
    "function": "TIME_SERIES_DAILY",
    "symbol":INTEL_STOCK,
    "apikey":api_key_stock_api}
parameters_for_news_api = {
    "apiKey": api_key_news_api,
    "q":intel,
    "country":"us",
    "category":"technology"}
parameters_for_openweathermap_api = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key_openweathermap_api,
    "cnt": 5}
parameters_for_metalpriceapi_api = {
    "api_key":api_key_metalpriceapi_api,
    "base":"EGP",
    "currencies":"USD,XAU,SAR"}

stock_api_response = requests.get(url=api_end_point_stock_api, params=parameters_for_stock_api)
stock_api_response.raise_for_status()
stock_api_data = stock_api_response.json()

news_api_response = requests.get(url=api_end_point_news_api, params=parameters_for_news_api)
news_api_response.raise_for_status()
news_api_data = news_api_response.json()

openweathermap_api_response = requests.get(url=api_end_point_openweathermap_api, params=parameters_for_openweathermap_api)
openweathermap_api_response.raise_for_status()
openweathermap_api_data = openweathermap_api_response.json()

metalpriceapi_api_response = requests.get(url=api_end_point_metalpriceapi_api, params=parameters_for_metalpriceapi_api)
metalpriceapi_api_response.raise_for_status()
metalpriceapi_api_data = metalpriceapi_api_response.json()

days = list(stock_api_data["Time Series (Daily)"])
the_current_day = stock_api_data["Time Series (Daily)"][days[0]]["4. close"]
the_previous_day = stock_api_data["Time Series (Daily)"][days[1]]["4. close"]
the_difference_in_tesla_stock = (float(the_current_day) - float(the_previous_day)) / float(the_current_day) * 100

will_rain_in_day = 0
for i in range(5):
    weather_id = openweathermap_api_data["list"][i]["weather"][0]["id"]
    if weather_id < 700:
        will_rain_in_day = 1
        break

temperatures = []
for item in openweathermap_api_data["list"]:
    time_str = item["dt_txt"]
    time_hour = int(time_str[11:13])

    if 9 <= time_hour <= 15:
        temperature_celsius = item["main"]["temp"] - 273.15
        temperatures.append(temperature_celsius)
noon_temperature = sum(temperatures) / len(temperatures) if temperatures else None

start_time_24 = openweathermap_api_data["list"][0]["dt_txt"]
start_time_12 = datetime.strptime(start_time_24, "%Y-%m-%d %H:%M:%S").strftime("%I:%M %p")

m0 = "اللهم صل على محمد، وعلى آل محمد، كما صليت على آل إبراهيم، وبارك على محمد، وعلى آل محمد، كما باركت على آل إبراهيم في العالمين إنك حميد مجيد"
client.messages.create(
    body=m0,
    from_='whatsapp:+14155238886',
    to='whatsapp:+201020965984'
)

m1 = '''قال جلَّ وعلا: {يا أيها الذين آمنوا اذكروا الله ذكرا كثيرا * وسبحوه بكرة وأصيلا}، وقال سبحانه: {فسبحان الله حين تمسون وحين تصبحون * وله الحمد في السماوات والأرض وعشيا وحين تظهرون}.

أذكار الصباح

*آية الكرسي: {الله لا إله إلا هو الحي القيوم لا تأخذه سنة ولا نوم له ما في السماوات وما في الأرض من ذا الذي يشفع عنده إلا بإذنه يعلم ما بين أيديهم وما خلفهم ولا يحيطون بشيء من علمه إلا بما شاء وسع كرسيه السماوات والأرض ولا يؤده حفظهما وهو العلي العظيم}

* أصبحنا على فطرة الإسلام وكلِمة الإخلاص، ودين نبينا محمد صلى الله عليه وسلم، ومِلَّةِ أبينا إبراهيم، حنيفاً مسلماً، وما كان من المشركين.

* رضيت بالله ربا، وبالإسلام دينا، وبمحمد صلى الله عليه وسلم نبياً.

* اللهم إني أسألك علماً نافعاً، ورزقاً طيباً، وعملاً متقبلاً.

* اللهم بك أصبحنا، وبك أمسينا، وبك نحيا، وبك نموت، وإليك النشور.

* لا إله إلا الله وحده، لا شريك له، له الملك، وله الحمد، وهو على كل شيء قدير.

* يا حيُّ يا قيوم برحمتك أستغيثُ، أصلح لي شأني كله، ولا تَكلني إلى نفسي طَرْفَةَ عين أبدًا.

* اللهم أنت ربي، لا إله إلا أنت، خلقتني وأنا عبدُك, وأنا على عهدِك ووعدِك ما استطعتُ، أعوذ بك من شر ما صنعتُ، أبوءُ لَكَ بنعمتكَ عَلَيَّ، وأبوء بذنبي، فاغفر لي، فإنه لا يغفرُ الذنوب إلا أنت.

* اللهم فاطر السموات والأرض، عالم الغيب والشهادة، رب كل شيء ومليكه، أشهد أن لا إله إلا أنت, أعوذ بك من شرّ نفسي، ومن شرّ الشيطان وشركه، وأن أقترف على نفسي سوءا، أو أجره إلى مسلم. .'''
client.messages.create(
    body=m1,
    from_='whatsapp:+14155238886',
    to='whatsapp:+201020965984'
)
m2 = '''* أصبحنا وأصبح الملك لله، والحمد لله ولا إله إلا الله وحده لا شريك له، له الملك وله الحمد، وهو على كل شيء قدير، أسألك خير ما في هذا اليوم، وخير ما بعده، وأعوذ بك من شر هذا اليوم، وشر ما بعده، وأعوذ بك من الكسل وسوء الكبر، وأعوذ بك من عذاب النار وعذاب القبر.

* اللهم إني أسألك العفو والعافية في الدنيا والآخرة، اللهم أسألك العفو والعافية في ديني ودنياي وأهلي ومالي، اللهم استر عوراتي، وآمن روعاتي، واحفظني من بين يدي، ومن خلفي، وعن يميني، وعن شمالي، ومن فوقي، وأعوذ بك أن أغتال من تحتي.

* بسم الله الذي لا يضر مع اسمه شيء في الأرض ولا في السماء، وهو السميع العليم. (ثلاث مرات).

* سبحان الله عدد خلقه، سبحان الله رضا نفسه، سبحان الله زنة عرشه، سبحان الله مداد كلماته. (ثلاث مرات).

* اللهم عافني في بدني، اللهم عافني في سمعي، اللهم عافني في بصري، لا إله إلا أنت، اللهم إني أعوذ بك من الكفر والفقر، اللهم إني أعوذ بك من عذاب القبر، لا إله إلا أنت. (ثلاث مرات).

* قراءة سور: الإخلاص، والفلق، والناس. ثلاث مرّات.

* {حسبي الله لا إله إلا هو عليه توكلت وهو رب العرش العظيم} (التوبة:129). (سبع مرات).

* اللهم إني أصبحت، أُشهدك وأُشهد حملة عرشك وملائكتك وجميع خلقك أنك أنت الله، وحدك لا شريك لك وأن محمداً عبدك ورسولك. (أربع مرات).

* لا إله إلا الله وحده، لا شريك له، له الملك، وله الحمد، يحيي ويميت، وهو على كل شيء قدير. (عشر مرات).

* سبحان الله وبحمده. أو: سبحان الله العظيم وبحمده. (مائة مرة أو أكثر).

* أستغفر الله. (مائة مرة).

* سبحان الله، والحمد لله، والله أكبر, لا إله إلا الله وحده، لا شريك له، له الملك، وله الحمد، وهو على كل شيء قدير. (مائة مرّةٍ أو أكثر).'''
client.messages.create(
    body=m2,
    from_='whatsapp:+14155238886',
    to='whatsapp:+201020965984'
)

the_difference_in_tesla_stock = 2.3
if abs(the_difference_in_tesla_stock) > 2:
    m3 = "Intel: "
    if the_difference_in_tesla_stock > 0:
        m3 += f"🔺{int(the_difference_in_tesla_stock)}%"
    else:
        m3 += f"🔻{int(the_difference_in_tesla_stock)}%\n"
    for i in range(3):
        title = news_api_data["articles"][i]["title"]
        description = news_api_data["articles"][i]["description"]
        m3 += f"{title}\n{description}\n\n"

    message = client.messages.create(
        body=m3,
        from_='whatsapp:+14155238886',
        to='whatsapp:+201020965984'
    )

m4 = (f"UDS : {round(metalpriceapi_api_data["rates"]["EGPUSD"], 2)}\n"
      f"SAR : {round(metalpriceapi_api_data["rates"]["EGPSAR"], 2)}\n"
      f"GOLD : {int(metalpriceapi_api_data["rates"]["EGPXAU"]/31.1)}"
      f"\n\nstart time {start_time_12}\n")
if will_rain_in_day:
    m4 += f"it might rain today 🌧️☔\n"
m4 += f"noon temperature : {round(noon_temperature, 1)}c°\n_______________________________________"
client.messages.create(
    body=m4,
    from_='whatsapp:+14155238886',
    to='whatsapp:+201020965984'
)


















from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt


def get_YG_games(year, genre):
    cnt = 1
    for j in parsed_data.iterrows():
        if j[1].Year == year and j[1].Genre == genre:
            cnt += 1
    return cnt


url = 'https://raw.githubusercontent.com/Newbilius/Old-Games_DOS_Game_Gauntlet/master/GAMES.csv'

pd.set_option('display.max_rows', None)
parsed_data = pd.read_csv(url, delimiter=';', names=[
                          'Title', 'Genre', 'URL', "Year"])
# ----------------------------------------------
plt.figure(figsize=(15, 7))
ax1 = plt.subplot(211)
years = {x: 0 for x in parsed_data["Year"]}
years.pop("не издана", None)
for i in parsed_data['Year']:
    if i != "не издана":
        years[i] += 1
ax1.bar(years.keys(), years.values())
ax1.set_title("Most active years")
# ----------------------------------------------

# ----------------------------------------------
genre_labels = set(parsed_data['Genre'])
ax1 = plt.subplot(212)
year_80 = {x: 0 for x in genre_labels}
year_90 = {x: 0 for x in genre_labels}
year_00 = {x: 0 for x in genre_labels}
for i in parsed_data.iterrows():
    if i[1].Year != 'не издана':
        if 1980 < int(i[1].Year) <= 1990:
            year_80[i[1].Genre] += 1
        elif 1990 < int(i[1].Year) <= 2000:
            year_90[i[1].Genre] += 1
        elif 2000 < int(i[1].Year) <= 2010:
            year_00[i[1].Genre] += 1
ax1.plot(year_80.keys(), year_80.values())
ax1.plot(year_90.keys(),  year_90.values())
ax1.plot(year_00.keys(), year_00.values())
ax1.legend(labels=('1980', '1990', '2000'))
ax1.set_title("Most popular genres")
plt.show()

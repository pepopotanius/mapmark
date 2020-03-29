#googlemap_memo_
# グーグルマップに緯度経度でポイント登録
# jupyterで実行するとウィンドウ内にマップが表示される→サンプルｈｔｍｌを生成するように末尾に加えた。
# これをｇドライブに入れて、IPADで「アプリで開く」で、Documentで開くとマップが表示される。尚、クロームは開かない。

import folium
import pandas as pd # pandasをpdと呼んで呼び出せる様にインポート
from pandas import Series,DataFrame

test_map = folium.Map(
    location=[35.681733 , 139.767074], #マップの中心位置を示す
    zoom_start=12)
test_map

folium.Marker([35.681733 , 139.767074], #マーカーを設置。tokyo駅の緯度と経度を入れます。[緯度,経度]
              icon=folium.Icon(color="darkblue", icon = "flag")).add_to(test_map)

test_map.save('googlemap_memo2.html') # test.map(jupyterにマップを表示　test_map.sabe(マップを呼べるhtmlを生成))
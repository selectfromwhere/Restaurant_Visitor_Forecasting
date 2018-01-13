# 提供されているデータについて
## air_reserve.csv [Airリザーブの予約データ]
- air_store_id - AirリザーブのレストランID
- visit_datetime - 予約時刻
- reserve_datetime - 予約が行われた時刻
- reserve_visitors - その予約の訪問者数
```
air_store_id,visit_datetime,reserve_datetime,reserve_visitors
air_877f79706adbfb06,2016-01-01 19:00:00,2016-01-01 16:00:00,1
```

## air_store_info.csv [Airリザーブのレストラン情報]
- air_store_id - AirリザーブのレストランID
- air_genre_name - ジャンル
- air_area_name - エリア
- latitude - 緯度
- longitude - 経度
!!! 緯度と経度は、店舗が属する地域の緯度と経度
```
air_store_id,air_genre_name,air_area_name,latitude,longitude
air_0f0cdeee6c9bf3d7,Italian/French,Hyōgo-ken Kōbe-shi Kumoidōri,34.6951242,135.1978525
```

## air_visit_data.csv [Airリザーブの訪問データ]
```
air_store_id,visit_date,visitors
air_ba937bf13d40fb24,2016-01-13,25
```

## hpg_reserve.csv [ホットペッパーグルメの予約データ]
- hpg_store_id - ホットペッパーグルメのレストランのID
- visit_datetime - 予約時刻
- reserve_datetime - 予約が行われた時刻
- reserve_visitors - その予約の訪問者数
```
hpg_store_id,visit_datetime,reserve_datetime,reserve_visitors
hpg_c63f6f42e088e50f,2016-01-01 11:00:00,2016-01-01 09:00:00,1
```

## hpg_store_info.csv [ホットペッパーグルメのレストラン情報]
- hpg_store_id - ホットペッパーグルメのレストランのID
- hpg_genre_name - ジャンル
- hpg_area_name - エリア
- latitude - 緯度
- longitude - 経度
!!! 緯度と経度は、店舗が属する地域の緯度と経度
```
hpg_store_id,hpg_genre_name,hpg_area_name,latitude,longitude
hpg_6622b62385aec8bf,Japanese style,Tōkyō-to Setagaya-ku Taishidō,35.6436746642265,139.668220854814
```

# date_info.csv [カレンダー]
- calendar_date - 年月日
- day_of_week - 曜日
- holiday_flg - 日本の祝日
```
calendar_date,day_of_week,holiday_flg
2016-01-01,Friday,1
```

# store_id_relation.csv [id横断データ]
- hpg_store_id
- air_store_id
```
air_store_id,hpg_store_id
air_63b13c56b7201bd9,hpg_4bc649e72e2a239a
```

# sample_submission.csv [Submitサンプル]
```
id,visitors
air_00a91d42b08b08d9_2017-04-23,0
air_00a91d42b08b08d9_2017-04-24,0
air_00a91d42b08b08d9_2017-04-25,0
```

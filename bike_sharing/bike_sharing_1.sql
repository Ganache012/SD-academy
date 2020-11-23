-- SELECT * FROM hour WHERE dteday='2011-01-01';

/* SELECT hr as "시간", weathersit as "날씨", windspeed as "풍속", cnt as "자전거 대여수" 
FROM hour WHERE dteday='2011-01-01';*/

SELECT hr as "시간", weathersit as "날씨", round(windspeed,2) as "풍속", cnt as "자전거 대여수" 
FROM hour WHERE dteday='2011-01-01';
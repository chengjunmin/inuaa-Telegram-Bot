```
 ╔═╗      ╔═╗ ╔═╗ ╔═╗ ╔╦╗      ╦ ╦ ╔╗╔ ╦ ╦  ╦ ╔═╗ ╦═╗ ╔═╗ ╦ ╔╦╗ ╦ ╦      ╦ ╦ ╔═╗ ╔═╗      ╔╗╔ ╔═╗      ╦ ╦ ╔═╗ ╦   ╦   ╔═╗
 ╠═╣      ║ ╦ ║ ║ ║ ║  ║║      ║ ║ ║║║ ║ ╚╗╔╝ ║╣  ╠╦╝ ╚═╗ ║  ║  ╚╦╝      ╠═╣ ╠═╣ ╚═╗      ║║║ ║ ║      ║║║ ╠═╣ ║   ║   ╚═╗
 ╩ ╩      ╚═╝ ╚═╝ ╚═╝ ═╩╝      ╚═╝ ╝╚╝ ╩  ╚╝  ╚═╝ ╩╚═ ╚═╝ ╩  ╩   ╩       ╩ ╩ ╩ ╩ ╚═╝      ╝╚╝ ╚═╝      ╚╩╝ ╩ ╩ ╩═╝ ╩═╝ ╚═╝
```

# telegram bot NUAA i南航 自动打卡机器人

好的大学没有围墙！

使用机器人，在 telegram 搜索 @yym68686bot

轻量级数据库，不考虑性能，直接用Notion的Database做了数据库

- main 分支 HeroKu 部署实例
- vercel 分支 vercel 部署实例

# 上手指南

https://yym68686.top/TelegramBot

# 自动申请出校

自助申请，自己审批，摆脱辅导员！

好的大学没有围墙！

TODO：

两个 POST 对比：

[From UNIX Timestamp, 4 more - CyberChef (gchq.github.io)](https://gchq.github.io/CyberChef/#recipe=From_UNIX_Timestamp('Seconds%20(s)'/disabled)To_UNIX_Timestamp('Seconds%20(s)',true,true/disabled)URL_Decode()Diff('%5C%5Cn%5C%5Cn','Character',true,true,false,false)JSON_Beautify('%20%20%20%20',false,true/disabled)&input=JTdCJTIyX1ZBUl9FWEVDVVRFX0lOREVQX09SR0FOSVpFX05hbWUlMjIlM0ElMjIlRTUlQkMlQTAlRTQlQjglODklRTUlQUQlQTYlRTklOTklQTIlMjIlMkMlMjJfVkFSX0FDVElPTl9JTkRFUF9PUkdBTklaRVNfQ29kZXMlMjIlM0ElMjJ7Nn0lMjIlMkMlMjJfVkFSX0FDVElPTl9SRUFMTkFNRSUyMiUzQSUyMiVFNSVCQyVBMCVFNCVCOCU4OSVFNCVCOCU4OSUyMiUyQyUyMl9WQVJfQUNUSU9OX09SR0FOSVpFJTIyJTNBJTIyezZ9JTIyJTJDJTIyX1ZBUl9FWEVDVVRFX09SR0FOSVpFJTIyJTNBJTIyezZ9JTIyJTJDJTIyX1ZBUl9BQ1RJT05fSU5ERVBfT1JHQU5JWkUlMjIlM0ElMjJ7Nn0lMjIlMkMlMjJfVkFSX0FDVElPTl9JTkRFUF9PUkdBTklaRV9OYW1lJTIyJTNBJTIyJUU1JUJDJUEwJUU0JUI4JTg5JUU1JUFEJUE2JUU5JTk5JUEyJTIyJTJDJTIyX1ZBUl9BQ1RJT05fT1JHQU5JWkVfTmFtZSUyMiUzQSUyMiVFNSVCQyVBMCVFNCVCOCU4OSVFNSVBRCVBNiVFOSU5OSVBMiUyMiUyQyUyMl9WQVJfRVhFQ1VURV9PUkdBTklaRVNfTmFtZXMlMjIlM0ElMjIlRTUlQkMlQTAlRTQlQjglODklRTUlQUQlQTYlRTklOTklQTIlMjIlMkMlMjJfVkFSX09XTkVSX09SR0FOSVpFU19Db2RlcyUyMiUzQSUyMns2fSUyMiUyQyUyMl9WQVJfQUREUiUyMiUzQSUyMjEwLjEwMC4xMTcuMjAlMjIlMkMlMjJfVkFSX09XTkVSX09SR0FOSVpFU19OYW1lcyUyMiUzQSUyMiVFNSVCQyVBMCVFNCVCOCU4OSVFNSVBRCVBNiVFOSU5OSVBMiUyMiUyQyUyMl9WQVJfVVJMJTIyJTNBJTIyaHR0cHMlM0ElMkYlMkZlaGFsbC5udWFhLmVkdS5jbiUyRmluZm9wbHVzJTJGZm9ybSUyRnswfSUyRnJlbmRlciUzRnRoZW1lJTNEbnVhYV9uZXclMjIlMkMlMjJfVkFSX0VYRUNVVEVfT1JHQU5JWkVfTmFtZSUyMiUzQSUyMiVFNSVCQyVBMCVFNCVCOCU4OSVFNSVBRCVBNiVFOSU5OSVBMiUyMiUyQyUyMl9WQVJfUkVMRUFTRSUyMiUzQSUyMnRydWUlMjIlMkMlMjJfVkFSX1RPREFZJTIyJTNBJTIyezV9JTIyJTJDJTIyX1ZBUl9OT1dfTU9OVEglMjIlM0ElMjI5JTIyJTJDJTIyX1ZBUl9BQ1RJT05fVVNFUkNPREVTJTIyJTNBJTIyMTYyMDEwMjE5JTIyJTJDJTIyX1ZBUl9BQ1RJT05fQUNDT1VOVCUyMiUzQSUyMjE2MjAxMDIxOSUyMiUyQyUyMl9WQVJfQUNUSU9OX0lOREVQX09SR0FOSVpFU19OYW1lcyUyMiUzQSUyMiVFNSVCQyVBMCVFNCVCOCU4OSVFNSVBRCVBNiVFOSU5OSVBMiUyMiUyQyUyMl9WQVJfT1dORVJfQUNDT1VOVCUyMiUzQSUyMjE2MjAxMDIxOSUyMiUyQyUyMl9WQVJfQUNUSU9OX09SR0FOSVpFU19OYW1lcyUyMiUzQSUyMiVFNSVCQyVBMCVFNCVCOCU4OSVFNSVBRCVBNiVFOSU5OSVBMiUyMiUyQyUyMl9WQVJfU1RFUF9DT0RFJTIyJTNBJTIyU1FSJTIyJTJDJTIyX1ZBUl9PV05FUl9QSE9ORSUyMiUzQSUyMjEyMzQ1Njc4OTQ1JTIyJTJDJTIyX1ZBUl9PV05FUl9VU0VSQ09ERVMlMjIlM0ElMjIxNjIwMTAyMTklMjIlMkMlMjJfVkFSX0VYRUNVVEVfT1JHQU5JWkVTX0NvZGVzJTIyJTNBJTIyezZ9JTIyJTJDJTIyX1ZBUl9OT1dfREFZJTIyJTNBJTIyMSUyMiUyQyUyMl9WQVJfT1dORVJfUkVBTE5BTUUlMjIlM0ElMjIlRTUlQkMlQTAlRTQlQjglODklRTQlQjglODklMjIlMkMlMjJfVkFSX0VOVFJZX1RBR1MlMjIlM0ElMjIwMS0lRTclOTYlQUIlRTYlODMlODUlRTklOTglQjIlRTYlOEUlQTclRTYlOUMlOEQlRTUlOEElQTElMkMlRTclQTclQkIlRTUlOEElQTglRTclQUIlQUYlMjIlMkMlMjJfVkFSX05PVyUyMiUzQSUyMjE2NjIwMzg4NTclMjIlMkMlMjJfVkFSX1VSTF9BdHRyJTIyJTNBJTIyJTdCJTVDJTIydGhlbWUlNUMlMjIlM0ElNUMlMjJudWFhX25ldyU1QyUyMiU3RCUyMiUyQyUyMl9WQVJfRU5UUllfTlVNQkVSJTIyJTNBJTIyMTMzNTczOTclMjIlMkMlMjJfVkFSX0VYRUNVVEVfSU5ERVBfT1JHQU5JWkVTX05hbWVzJTIyJTNBJTIyJUU1JUJDJUEwJUU0JUI4JTg5JUU1JUFEJUE2JUU5JTk5JUEyJTIyJTJDJTIyX1ZBUl9FTlRSWV9OQU1FJTIyJTNBJTIyXyVFNyU5NiVBQiVFNiU4MyU4NSVFOSU5OCVCMiVFNiU4RSVBNyVFNiU5QyU5RiVFNSVBRCVBNiVFNyU5NCU5RiVFOSU5QiVCNiVFNiU5OCU5RiVFOCVCRiU5QiVFNSU4NyVCQSVFNiVBMCVBMSVFNyU5NCVCMyVFOCVBRiVCNyUyMiUyQyUyMl9WQVJfU1RFUF9OVU1CRVIlMjIlM0ElMjJ7MH0lMjIlMkMlMjJfVkFSX1BPU0lUSU9OUyUyMiUzQSUyMns2fSUzQTExJTNBMTYyMDEwMjE5JTIyJTJDJTIyX1ZBUl9BQ1RJT05fUEhPTkUlMjIlM0ElMjIxMjM0NTY3ODk0NSUyMiUyQyUyMl9WQVJfRVhFQ1VURV9JTkRFUF9PUkdBTklaRVNfQ29kZXMlMjIlM0ElMjJ7Nn0lMjIlMkMlMjJfVkFSX0VYRUNVVEVfUE9TSVRJT05TJTIyJTNBJTIyezZ9JTNBMTElM0ExNjIwMTAyMTklMjIlMkMlMjJfVkFSX0FDVElPTl9PUkdBTklaRVNfQ29kZXMlMjIlM0ElMjJ7Nn0lMjIlMkMlMjJfVkFSX0VYRUNVVEVfSU5ERVBfT1JHQU5JWkUlMjIlM0ElMjJ7Nn0lMjIlMkMlMjJfVkFSX05PV19ZRUFSJTIyJTNBJTIyMjAyMiUyMiUyQyUyMmdyb3VwUVdERExpc3QlMjIlM0ElNUIwJTVEJTJDJTIyZmllbGRITURGWiUyMiUzQSUyMjIlMjIlMkMlMjJmaWVsZFhTU0YlMjIlM0ElMjIlRTYlOUMlQUMlRTclQTclOTElRTclOTQlOUYlMjIlMkMlMjJmaWVsZFNRU0olMjIlM0ExNjYyMDM4ODU3JTJDJTIyZmllbGRBeG0lMjIlM0ElMjIxNjIwMTAyMTklMjIlMkMlMjJmaWVsZEF4bV9OYW1lJTIyJTNBJTIyJUU1JUJDJUEwJUU0JUI4JTg5JUU0JUI4JTg5JTIyJTJDJTIyZmllbGRBeHklMjIlM0ElMjJ7Nn0lMjIlMkMlMjJmaWVsZEF4eV9OYW1lJTIyJTNBJTIyJUU1JUJDJUEwJUU0JUI4JTg5JUU1JUFEJUE2JUU5JTk5JUEyJTIyJTJDJTIyZmllbGRBeGglMjIlM0ElMjIxNjIwMTAyMTklMjIlMkMlMjJmaWVsZEFseGRoJTIyJTNBJTIyMTIzNDU2Nzg5NDUlMjIlMkMlMjJmaWVsZEFmZHklMjIlM0ElMjJ7MX0lMjIlMkMlMjJmaWVsZEFmZHlfTmFtZSUyMiUzQSUyMiVFNSVCQyVBMCVFNCVCOCU4OSVFNCVCOCU4OSUyMiUyQyUyMmZpZWxkRFMlMjIlM0ElMjIlMjIlMkMlMjJmaWVsZERTX05hbWUlMjIlM0ElMjIlMjIlMkMlMjJmaWVsZEFTRlpITSUyMiUzQSUyMjEyMzQ1Njc4OTQ1NjEyMzQ1NiUyMiUyQyUyMmZpZWxkQVNaWFElMjIlM0ElMjIyJTIyJTJDJTIyZmllbGRBU1pYUV9OYW1lJTIyJTNBJTIyJUU1JUIwJTg2JUU1JTg2JTlCJUU4JUI3JUFGJUU2JUEwJUExJUU1JThDJUJBJTIyJTJDJTIyZmllbGRYU0xYJTIyJTNBJTIyJUU0JUJEJThGJUU2JUEwJUExJTIyJTJDJTIyZmllbGRYU0xYX05hbWUlMjIlM0ElMjIlRTQlQkQlOEYlRTYlQTAlQTElMjIlMkMlMjJmaWVsZFNGWUdMUyUyMiUzQSUyMiUyMiUyQyUyMmZpZWxkVFpTRkpLJTIyJTNBJTIyJTIyJTJDJTIyZmllbGRTS00lMjIlM0ElMjIlN0IlNUMlMjJpZCU1QyUyMiUzQSU1QyUyMjE3N2IwOTgzLTlkN2ItNGUwZi1iOWUwLTBkMTVkNjk4NDg4MSU1QyUyMiUyQyU1QyUyMm5hbWUlNUMlMjIlM0ElNUMlMjIxLnBuZyU1QyUyMiUyQyU1QyUyMnNpemUlNUMlMjIlM0ExJTJDJTVDJTIydXJpJTVDJTIyJTNBJTVDJTIyaHR0cHMlM0ElMkYlMkZlaGFsbC5udWFhLmVkdS5jbiUyRmZpbGUlMkYxNzdiMDk4My05ZDdiLTRlMGYtYjllMC0wZDE1ZDY5ODQ4ODElNUMlMjIlMkMlNUMlMjJtaW1lJTVDJTIyJTNBJTVDJTIyaW1hZ2UlMkZwbmclNUMlMjIlN0QlMjIlMkMlMjJmaWVsZFhDTSUyMiUzQSUyMiU3QiU1QyUyMmlkJTVDJTIyJTNBJTVDJTIyNzcyMDQzOGMtY2E5Ni00ZDg0LTgxOGUtZWE0OWE2NWU1NGI2JTVDJTIyJTJDJTVDJTIybmFtZSU1QyUyMiUzQSU1QyUyMjEucG5nJTVDJTIyJTJDJTVDJTIyc2l6ZSU1QyUyMiUzQTElMkMlNUMlMjJ1cmklNUMlMjIlM0ElNUMlMjJodHRwcyUzQSUyRiUyRmVoYWxsLm51YWEuZWR1LmNuJTJGZmlsZSUyRjc3MjA0MzhjLWNhOTYtNGQ4NC04MThlLWVhNDlhNjVlNTRiNiU1QyUyMiUyQyU1QyUyMm1pbWUlNUMlMjIlM0ElNUMlMjJpbWFnZSUyRnBuZyU1QyUyMiU3RCUyMiUyQyUyMmZpZWxkSFNCRyUyMiUzQSUyMiU3QiU1QyUyMmlkJTVDJTIyJTNBJTVDJTIyNjQwMjM1YTItMTYyZS00ZmU1LWExNTYtNWM5YmZjNzg3OGI3JTVDJTIyJTJDJTVDJTIybmFtZSU1QyUyMiUzQSU1QyUyMjEucG5nJTVDJTIyJTJDJTVDJTIyc2l6ZSU1QyUyMiUzQTElMkMlNUMlMjJ1cmklNUMlMjIlM0ElNUMlMjJodHRwcyUzQSUyRiUyRmVoYWxsLm51YWEuZWR1LmNuJTJGZmlsZSUyRjY0MDIzNWEyLTE2MmUtNGZlNS1hMTU2LTVjOWJmYzc4NzhiNyU1QyUyMiUyQyU1QyUyMm1pbWUlNUMlMjIlM0ElNUMlMjJpbWFnZSUyRnBuZyU1QyUyMiU3RCUyMiUyQyUyMmZpZWxkQkxIVFMlMjIlM0ElMjIlMjIlMkMlMjJmaWVsZENYUlElMjIlM0F7NX0lMkMlMjJmaWVsZEpTU0olMjIlM0F7NX0lMkMlMjJmaWVsZENYU0pGUk9NJTIyJTNBMCUyQyUyMmZpZWxkQ1hTSlRPJTIyJTNBMCUyQyUyMmZpZWxkQ1hTWSUyMiUzQSUyMi4uLiUyMiUyQyUyMmZpZWxkQ1hMQiUyMiUzQSUyMjElMjIlMkMlMjJmaWVsZEFjeHhjJTIyJTNBJTIyMiUyMiUyQyUyMmZpZWxkQWRzJTIyJTNBJTIyMSUyMiUyQyUyMmZpZWxkQXNoZW5ncyUyMiUzQSU1QiUyMiUyMiU1RCUyQyUyMmZpZWxkQXNoZW5nc19OYW1lJTIyJTNBJTVCJTIyJTIyJTVEJTJDJTIyZmllbGRBc2hpcyUyMiUzQSU1QiUyMiUyMiU1RCUyQyUyMmZpZWxkQXNoaXNfTmFtZSUyMiUzQSU1QiUyMiUyMiU1RCUyQyUyMmZpZWxkQXNoaXNfQXR0ciUyMiUzQSU1QiUyMiU3QiU1QyUyMl9wYXJlbnQlNUMlMjIlM0ElNUMlMjIlNUMlMjIlN0QlMjIlNUQlMkMlMjJmaWVsZEFqdGRkJTIyJTNBJTVCJTIyJTIyJTVEJTJDJTIyZmllbGRDTiUyMiUzQXRydWUlMkMlMjJmaWVsZEFoaWRkZW4lMjIlM0ElMjIlMjIlMkMlMjJmaWVsZEN5ajMlMjIlM0ElMjIlMjIlMkMlMjJmaWVsZENzaHIzJTIyJTNBJTIyJTIyJTJDJTIyZmllbGRDc2hyM19OYW1lJTIyJTNBJTIyJTIyJTJDJTIyZmllbGRDc2hkYXRlMyUyMiUzQSUyMiUyMiUyQyUyMmZpZWxkRllaU0glMjIlM0ElMjIlMjIlMkMlMjJmaWVsZEZZWlNIUiUyMiUzQSUyMiUyMiUyQyUyMmZpZWxkRllaU0hSX05hbWUlMjIlM0ElMjIlMjIlMkMlMjJmaWVsZEZZWlNIUlElMjIlM0ElMjIlMjIlMkMlMjJmaWVsZEN5ajQlMjIlM0ElMjIlMjIlMkMlMjJmaWVsZENzaHI0JTIyJTNBJTIyJTIyJTJDJTIyZmllbGRDc2hyNF9OYW1lJTIyJTNBJTIyJTIyJTJDJTIyZmllbGRDc2hkYXRlNCUyMiUzQSUyMiUyMiUyQyUyMmZpZWxkQ3lqNSUyMiUzQSUyMiUyMiUyQyUyMmZpZWxkQ3NocjUlMjIlM0ElMjIlMjIlMkMlMjJmaWVsZENzaHI1X05hbWUlMjIlM0ElMjIlMjIlMkMlMjJmaWVsZENzaHNqNSUyMiUzQSUyMiUyMiUyQyUyMmZpZWxkVE9LRU4lMjIlM0ElMjIlMjIlMkMlMjJmaWVsZENYUlFTVFIlMjIlM0ElMjIlMjIlMkMlMjJmaWVsZENYUlFGcm9tJTIyJTNBMTY2MjAzODg1NyUyQyUyMmZpZWxkRlpaRCUyMiUzQSUyMiUyMiU3RCZyZW1hcms9JnJhbmQ9ODUyLjQ4OTc5MDQ5NjcxOCZuZXh0VXNlcnM9JTdCJTIyMiUyQyUyMiUzQSUyMjgzNmM4MjAxLWM5NWUtMTFlOS05MTI3LTAwNTA1NjhhMjgxZiUyMiU3RCZzdGVwSWQ9ezB9JnRpbWVzdGFtcD17Mn0mYm91bmRGaWVsZHM9ZmllbGRDWFNKVE8lMkNmaWVsZEFTWlhRJTJDZmllbGRDWFJRJTJDZmllbGRBc2hlbmdzJTJDZmllbGRBY3h4YyUyQ2ZpZWxkQXhoJTJDZmllbGRGWlpEJTJDZmllbGRDWFJRU1RSJTJDZmllbGRTS00lMkNmaWVsZEF4bSUyQ2ZpZWxkQWx4ZGglMkNmaWVsZENYUlFGcm9tJTJDZmllbGREUyUyQ2ZpZWxkWENNJTJDZmllbGRUT0tFTiUyQ2ZpZWxkWFNMWCUyQ2ZpZWxkU0ZZR0xTJTJDZmllbGRITURGWiUyQ2ZpZWxkQkxIVFMlMkNmaWVsZEFoaWRkZW4lMkNmaWVsZEZZWlNIJTJDZmllbGRKU1NKJTJDZmllbGRDWExCJTJDZmllbGRTUVNKJTJDZmllbGRDc2hyMyUyQ2ZpZWxkVFpTRkpLJTJDZmllbGRBU0ZaSE0lMkNmaWVsZENOJTJDZmllbGRGWVpTSFJRJTJDZmllbGRDWFNKRlJPTSUyQ2ZpZWxkRllaU0hSJTJDZmllbGRDc2hkYXRlMyUyQ2ZpZWxkWFNTRiUyQ2ZpZWxkQ3Noc2o1JTJDZmllbGRBanRkZCUyQ2ZpZWxkQXh5JTJDZmllbGRIU0JHJTJDZmllbGRDc2hkYXRlNCUyQ2ZpZWxkQWZkeSUyQ2ZpZWxkQ1hTWSUyQ2ZpZWxkQWRzJTJDZmllbGRDc2hyNCUyQ2ZpZWxkQ3NocjUlMkNmaWVsZEN5ajMlMkNmaWVsZEN5ajUlMkNmaWVsZEN5ajQlMkNmaWVsZEFzaGlzJmNzcmZUb2tlbj17NH0mbGFuZz16aAoKCiU3QiUyMl9WQVJfRVhFQ1VURV9JTkRFUF9PUkdBTklaRV9OYW1lJTIyJTNBJTIyJUU1JUJDJUEwJUU0JUI4JTg5JUU1JUFEJUE2JUU5JTk5JUEyJTIyJTJDJTIyX1ZBUl9BQ1RJT05fSU5ERVBfT1JHQU5JWkVTX0NvZGVzJTIyJTNBJTIyezZ9JTIyJTJDJTIyX1ZBUl9BQ1RJT05fUkVBTE5BTUUlMjIlM0ElMjIlRTUlQkMlQTAlRTQlQjglODklRTQlQjglODklMjIlMkMlMjJfVkFSX0FDVElPTl9PUkdBTklaRSUyMiUzQSUyMns2fSUyMiUyQyUyMl9WQVJfRVhFQ1VURV9PUkdBTklaRSUyMiUzQSUyMns2fSUyMiUyQyUyMl9WQVJfQUNUSU9OX0lOREVQX09SR0FOSVpFJTIyJTNBJTIyezZ9JTIyJTJDJTIyX1ZBUl9BQ1RJT05fSU5ERVBfT1JHQU5JWkVfTmFtZSUyMiUzQSUyMiVFNSVCQyVBMCVFNCVCOCU4OSVFNSVBRCVBNiVFOSU5OSVBMiUyMiUyQyUyMl9WQVJfQUNUSU9OX09SR0FOSVpFX05hbWUlMjIlM0ElMjIlRTUlQkMlQTAlRTQlQjglODklRTUlQUQlQTYlRTklOTklQTIlMjIlMkMlMjJfVkFSX0VYRUNVVEVfT1JHQU5JWkVTX05hbWVzJTIyJTNBJTIyJUU1JUJDJUEwJUU0JUI4JTg5JUU1JUFEJUE2JUU5JTk5JUEyJTIyJTJDJTIyX1ZBUl9PV05FUl9PUkdBTklaRVNfQ29kZXMlMjIlM0ElMjJ7Nn0lMjIlMkMlMjJfVkFSX0FERFIlMjIlM0ElMjIxMC4xMDAuMTE3LjIwJTIyJTJDJTIyX1ZBUl9MQVNUX0FDVElPTiUyMiUzQSUyMlN1Ym1pdCUyMiUyQyUyMl9WQVJfT1dORVJfT1JHQU5JWkVTX05hbWVzJTIyJTNBJTIyJUU1JUJDJUEwJUU0JUI4JTg5JUU1JUFEJUE2JUU5JTk5JUEyJTIyJTJDJTIyX1ZBUl9VUkwlMjIlM0ElMjJodHRwcyUzQSUyRiUyRmVoYWxsLm51YWEuZWR1LmNuJTJGaW5mb3BsdXMlMkZmb3JtJTJGezB9JTJGcmVuZGVyJTNGdGhlbWUlM0RudWFhX25ldyUyMiUyQyUyMl9WQVJfRVhFQ1VURV9PUkdBTklaRV9OYW1lJTIyJTNBJTIyJUU1JUJDJUEwJUU0JUI4JTg5JUU1JUFEJUE2JUU5JTk5JUEyJTIyJTJDJTIyX1ZBUl9SRUxFQVNFJTIyJTNBJTIydHJ1ZSUyMiUyQyUyMl9WQVJfVE9EQVklMjIlM0ElMjJ7NX0lMjIlMkMlMjJfVkFSX05PV19NT05USCUyMiUzQSUyMjklMjIlMkMlMjJfVkFSX0FDVElPTl9VU0VSQ09ERVMlMjIlM0ElMjIxNjIwMTAyMTklMjIlMkMlMjJfVkFSX0FDVElPTl9BQ0NPVU5UJTIyJTNBJTIyMTYyMDEwMjE5JTIyJTJDJTIyX1ZBUl9BQ1RJT05fSU5ERVBfT1JHQU5JWkVTX05hbWVzJTIyJTNBJTIyJUU1JUJDJUEwJUU0JUI4JTg5JUU1JUFEJUE2JUU5JTk5JUEyJTIyJTJDJTIyX1ZBUl9PV05FUl9BQ0NPVU5UJTIyJTNBJTIyMTYyMDEwMjE5JTIyJTJDJTIyX1ZBUl9BQ1RJT05fT1JHQU5JWkVTX05hbWVzJTIyJTNBJTIyJUU1JUJDJUEwJUU0JUI4JTg5JUU1JUFEJUE2JUU5JTk5JUEyJTIyJTJDJTIyX1ZBUl9TVEVQX0NPREUlMjIlM0ElMjJTUVIlMjIlMkMlMjJfVkFSX09XTkVSX1BIT05FJTIyJTNBJTIyMTIzNDU2Nzg5NDUlMjIlMkMlMjJfVkFSX09XTkVSX1VTRVJDT0RFUyUyMiUzQSUyMjE2MjAxMDIxOSUyMiUyQyUyMl9WQVJfRVhFQ1VURV9PUkdBTklaRVNfQ29kZXMlMjIlM0ElMjJ7Nn0lMjIlMkMlMjJfVkFSX05PV19EQVklMjIlM0ElMjIxJTIyJTJDJTIyX1ZBUl9PV05FUl9SRUFMTkFNRSUyMiUzQSUyMiVFNSVCQyVBMCVFNCVCOCU4OSVFNCVCOCU4OSUyMiUyQyUyMl9WQVJfRU5UUllfVEFHUyUyMiUzQSUyMjAxLSVFNyU5NiVBQiVFNiU4MyU4NSVFOSU5OCVCMiVFNiU4RSVBNyVFNiU5QyU4RCVFNSU4QSVBMSUyQyVFNyVBNyVCQiVFNSU4QSVBOCVFNyVBQiVBRiUyMiUyQyUyMl9WQVJfTk9XJTIyJTNBJTIyMTY2MjAzMzAwOCUyMiUyQyUyMl9WQVJfUEFSVElDSVBBTlRTJTIyJTNBJTIyJTJDMTYyMDEwMjE5JTJDJTIyJTJDJTIyX1ZBUl9VUkxfQXR0ciUyMiUzQSUyMiU3QiU1QyUyMnRoZW1lJTVDJTIyJTNBJTVDJTIybnVhYV9uZXclNUMlMjIlN0QlMjIlMkMlMjJfVkFSX0VOVFJZX05VTUJFUiUyMiUzQSUyMjEzMzU3Mzk3JTIyJTJDJTIyX1ZBUl9FWEVDVVRFX0lOREVQX09SR0FOSVpFU19OYW1lcyUyMiUzQSUyMiVFNSVCQyVBMCVFNCVCOCU4OSVFNSVBRCVBNiVFOSU5OSVBMiUyMiUyQyUyMl9WQVJfRU5UUllfTkFNRSUyMiUzQSUyMiVFNSVCQyVBMCVFNCVCOCU4OSVFNCVCOCU4OV8lRTclOTYlQUIlRTYlODMlODUlRTklOTglQjIlRTYlOEUlQTclRTYlOUMlOUYlRTUlQUQlQTYlRTclOTQlOUYlRTklOUIlQjYlRTYlOTglOUYlRTglQkYlOUIlRTUlODclQkElRTYlQTAlQTElRTclOTQlQjMlRTglQUYlQjclMjIlMkMlMjJfVkFSX1NURVBfTlVNQkVSJTIyJTNBJTIyezB9JTIyJTJDJTIyX1ZBUl9QT1NJVElPTlMlMjIlM0ElMjJ7Nn0lM0ExMSUzQTE2MjAxMDIxOSUyMiUyQyUyMl9WQVJfQUNUSU9OX1BIT05FJTIyJTNBJTIyMTIzNDU2Nzg5NDUlMjIlMkMlMjJfVkFSX0VYRUNVVEVfSU5ERVBfT1JHQU5JWkVTX0NvZGVzJTIyJTNBJTIyezZ9JTIyJTJDJTIyX1ZBUl9FWEVDVVRFX1BPU0lUSU9OUyUyMiUzQSUyMns2fSUzQTExJTNBMTYyMDEwMjE5JTIyJTJDJTIyX1ZBUl9BQ1RJT05fT1JHQU5JWkVTX0NvZGVzJTIyJTNBJTIyezZ9JTIyJTJDJTIyX1ZBUl9FWEVDVVRFX0lOREVQX09SR0FOSVpFJTIyJTNBJTIyezZ9JTIyJTJDJTIyX1ZBUl9OT1dfWUVBUiUyMiUzQSUyMjIwMjIlMjIlMkMlMjJncm91cFFXRERMaXN0JTIyJTNBJTVCMCU1RCUyQyUyMmZpZWxkSE1ERlolMjIlM0ElMjIyJTIyJTJDJTIyZmllbGRYU1NGJTIyJTNBJTIyJUU2JTlDJUFDJUU3JUE3JTkxJUU3JTk0JTlGJTIyJTJDJTIyZmllbGRTUVNKJTIyJTNBMTY2MjAzMzAwOCUyQyUyMmZpZWxkQXhtJTIyJTNBJTIyMTYyMDEwMjE5JTIyJTJDJTIyZmllbGRBeG1fTmFtZSUyMiUzQSUyMiVFNSVCQyVBMCVFNCVCOCU4OSVFNCVCOCU4OSUyMiUyQyUyMmZpZWxkQXh5JTIyJTNBJTIyezZ9JTIyJTJDJTIyZmllbGRBeHlfTmFtZSUyMiUzQSUyMiVFNSVCQyVBMCVFNCVCOCU4OSVFNSVBRCVBNiVFOSU5OSVBMiUyMiUyQyUyMmZpZWxkQXhoJTIyJTNBJTIyMTYyMDEwMjE5JTIyJTJDJTIyZmllbGRBbHhkaCUyMiUzQSUyMjEyMzQ1Njc4OTQ1JTIyJTJDJTIyZmllbGRBZmR5JTIyJTNBJTIyezF9JTIyJTJDJTIyZmllbGRBZmR5X05hbWUlMjIlM0ElMjIlRTUlQkMlQTAlRTQlQjglODklRTQlQjglODklMjIlMkMlMjJmaWVsZERTJTIyJTNBJTIyJTIyJTJDJTIyZmllbGREU19OYW1lJTIyJTNBJTIyJTIyJTJDJTIyZmllbGRBU0ZaSE0lMjIlM0ElMjIxMjM0NTY3ODk0NTYxMjM0NTYlMjIlMkMlMjJmaWVsZEFTWlhRJTIyJTNBJTIyMiUyMiUyQyUyMmZpZWxkQVNaWFFfTmFtZSUyMiUzQSUyMiVFNSVCMCU4NiVFNSU4NiU5QiVFOCVCNyVBRiVFNiVBMCVBMSVFNSU4QyVCQSUyMiUyQyUyMmZpZWxkWFNMWCUyMiUzQSUyMiVFNCVCRCU4RiVFNiVBMCVBMSUyMiUyQyUyMmZpZWxkWFNMWF9OYW1lJTIyJTNBJTIyJUU0JUJEJThGJUU2JUEwJUExJTIyJTJDJTIyZmllbGRTRllHTFMlMjIlM0ElMjIlMjIlMkMlMjJmaWVsZFRaU0ZKSyUyMiUzQSUyMiUyMiUyQyUyMmZpZWxkU0tNJTIyJTNBJTIyJTdCJTVDJTIyaWQlNUMlMjIlM0ElNUMlMjIxZmE5ODRlNy04YTQyLTQwOTktOTAzYy0xMDFmNjVkMzI5ZjQlNUMlMjIlMkMlNUMlMjJuYW1lJTVDJTIyJTNBJTVDJTIyMS5wbmclNUMlMjIlMkMlNUMlMjJzaXplJTVDJTIyJTNBMSUyQyU1QyUyMnVyaSU1QyUyMiUzQSU1QyUyMmh0dHBzJTNBJTJGJTJGZWhhbGwubnVhYS5lZHUuY24lMkZmaWxlJTJGMWZhOTg0ZTctOGE0Mi00MDk5LTkwM2MtMTAxZjY1ZDMyOWY0JTVDJTIyJTJDJTVDJTIybWltZSU1QyUyMiUzQSU1QyUyMmltYWdlJTJGcG5nJTVDJTIyJTdEJTIyJTJDJTIyZmllbGRYQ00lMjIlM0ElMjIlN0IlNUMlMjJpZCU1QyUyMiUzQSU1QyUyMmI1OTBmMWRmLTA1MGItNDMyYi05OWVjLThkNjYzNTY2MDdkZiU1QyUyMiUyQyU1QyUyMm5hbWUlNUMlMjIlM0ElNUMlMjIxLnBuZyU1QyUyMiUyQyU1QyUyMnNpemUlNUMlMjIlM0ExJTJDJTVDJTIydXJpJTVDJTIyJTNBJTVDJTIyaHR0cHMlM0ElMkYlMkZlaGFsbC5udWFhLmVkdS5jbiUyRmZpbGUlMkZiNTkwZjFkZi0wNTBiLTQzMmItOTllYy04ZDY2MzU2NjA3ZGYlNUMlMjIlMkMlNUMlMjJtaW1lJTVDJTIyJTNBJTVDJTIyaW1hZ2UlMkZwbmclNUMlMjIlN0QlMjIlMkMlMjJmaWVsZEhTQkclMjIlM0ElMjIlN0IlNUMlMjJpZCU1QyUyMiUzQSU1QyUyMjI2ODQ2MDUyLWNiNTktNGNhZC1iMzlhLThjYjA0ZjlhNTcyZCU1QyUyMiUyQyU1QyUyMm5hbWUlNUMlMjIlM0ElNUMlMjIxLnBuZyU1QyUyMiUyQyU1QyUyMnNpemUlNUMlMjIlM0ExJTJDJTVDJTIydXJpJTVDJTIyJTNBJTVDJTIyaHR0cHMlM0ElMkYlMkZlaGFsbC5udWFhLmVkdS5jbiUyRmZpbGUlMkYyNjg0NjA1Mi1jYjU5LTRjYWQtYjM5YS04Y2IwNGY5YTU3MmQlNUMlMjIlMkMlNUMlMjJtaW1lJTVDJTIyJTNBJTVDJTIyaW1hZ2UlMkZwbmclNUMlMjIlN0QlMjIlMkMlMjJmaWVsZEJMSFRTJTIyJTNBJTIyJTIyJTJDJTIyZmllbGRDWFJRJTIyJTNBezV9JTJDJTIyZmllbGRKU1NKJTIyJTNBezV9JTJDJTIyZmllbGRDWFNKRlJPTSUyMiUzQTAlMkMlMjJmaWVsZENYU0pUTyUyMiUzQTMwMCUyQyUyMmZpZWxkQ1hTWSUyMiUzQSUyMi4uLiUyMiUyQyUyMmZpZWxkQ1hMQiUyMiUzQSUyMjElMjIlMkMlMjJmaWVsZEFjeHhjJTIyJTNBJTIyMiUyMiUyQyUyMmZpZWxkQWRzJTIyJTNBJTIyMSUyMiUyQyUyMmZpZWxkQXNoZW5ncyUyMiUzQSU1QiUyMiUyMiU1RCUyQyUyMmZpZWxkQXNoZW5nc19OYW1lJTIyJTNBJTVCJTIyJTIyJTVEJTJDJTIyZmllbGRBc2hpcyUyMiUzQSU1QiUyMiUyMiU1RCUyQyUyMmZpZWxkQXNoaXNfTmFtZSUyMiUzQSU1QiUyMiUyMiU1RCUyQyUyMmZpZWxkQXNoaXNfQXR0ciUyMiUzQSU1QiUyMiU3QiU1QyUyMl9wYXJlbnQlNUMlMjIlM0ElNUMlMjIlNUMlMjIlN0QlMjIlNUQlMkMlMjJmaWVsZEFqdGRkJTIyJTNBJTVCJTIyJTIyJTVEJTJDJTIyZmllbGRDTiUyMiUzQXRydWUlMkMlMjJmaWVsZEFoaWRkZW4lMjIlM0ElMjIlMjIlMkMlMjJmaWVsZEN5ajMlMjIlM0ElMjIlMjIlMkMlMjJmaWVsZENzaHIzJTIyJTNBJTIyJTIyJTJDJTIyZmllbGRDc2hyM19OYW1lJTIyJTNBJTIyJTIyJTJDJTIyZmllbGRDc2hkYXRlMyUyMiUzQSUyMiUyMiUyQyUyMmZpZWxkRllaU0glMjIlM0ElMjIlMjIlMkMlMjJmaWVsZEZZWlNIUiUyMiUzQSUyMiUyMiUyQyUyMmZpZWxkRllaU0hSX05hbWUlMjIlM0ElMjIlMjIlMkMlMjJmaWVsZEZZWlNIUlElMjIlM0ElMjIlMjIlMkMlMjJmaWVsZEN5ajQlMjIlM0ElMjIlMjIlMkMlMjJmaWVsZENzaHI0JTIyJTNBJTIyJTIyJTJDJTIyZmllbGRDc2hyNF9OYW1lJTIyJTNBJTIyJTIyJTJDJTIyZmllbGRDc2hkYXRlNCUyMiUzQSUyMiUyMiUyQyUyMmZpZWxkQ3lqNSUyMiUzQSUyMiUyMiUyQyUyMmZpZWxkQ3NocjUlMjIlM0ElMjIlMjIlMkMlMjJmaWVsZENzaHI1X05hbWUlMjIlM0ElMjIlMjIlMkMlMjJmaWVsZENzaHNqNSUyMiUzQSUyMiUyMiUyQyUyMmZpZWxkVE9LRU4lMjIlM0ElMjIlMjIlMkMlMjJmaWVsZENYUlFTVFIlMjIlM0ElMjIlMjIlMkMlMjJmaWVsZENYUlFGcm9tJTIyJTNBezV9JTJDJTIyZmllbGRGWlpEJTIyJTNBJTIyJTIyJTdEJnJlbWFyaz0mcmFuZD0zNjUuNzAyNzA5MDU5ODM1OTcmbmV4dFVzZXJzPSU3QiUyMjIlMkMlMjIlM0ElMjI3Yzk0YzBjMy1jOTVlLTExZTktOTEyNy0wMDUwNTY4YTI4MWYlMjIlN0Qmc3RlcElkPXswfSZ0aW1lc3RhbXA9ezJ9JmJvdW5kRmllbGRzPWZpZWxkQ1hTSlRPJTJDZmllbGRBU1pYUSUyQ2ZpZWxkQ1hSUSUyQ2ZpZWxkQXNoZW5ncyUyQ2ZpZWxkQWN4eGMlMkNmaWVsZEF4aCUyQ2ZpZWxkRlpaRCUyQ2ZpZWxkQ1hSUVNUUiUyQ2ZpZWxkU0tNJTJDZmllbGRBeG0lMkNmaWVsZEFseGRoJTJDZmllbGRDWFJRRnJvbSUyQ2ZpZWxkRFMlMkNmaWVsZFhDTSUyQ2ZpZWxkVE9LRU4lMkNmaWVsZFhTTFglMkNmaWVsZFNGWUdMUyUyQ2ZpZWxkSE1ERlolMkNmaWVsZEJMSFRTJTJDZmllbGRBaGlkZGVuJTJDZmllbGRGWVpTSCUyQ2ZpZWxkSlNTSiUyQ2ZpZWxkQ1hMQiUyQ2ZpZWxkU1FTSiUyQ2ZpZWxkQ3NocjMlMkNmaWVsZFRaU0ZKSyUyQ2ZpZWxkQVNGWkhNJTJDZmllbGRDTiUyQ2ZpZWxkRllaU0hSUSUyQ2ZpZWxkQ1hTSkZST00lMkNmaWVsZEZZWlNIUiUyQ2ZpZWxkQ3NoZGF0ZTMlMkNmaWVsZFhTU0YlMkNmaWVsZENzaHNqNSUyQ2ZpZWxkQWp0ZGQlMkNmaWVsZEF4eSUyQ2ZpZWxkSFNCRyUyQ2ZpZWxkQ3NoZGF0ZTQlMkNmaWVsZEFmZHklMkNmaWVsZENYU1klMkNmaWVsZEFkcyUyQ2ZpZWxkQ3NocjQlMkNmaWVsZENzaHI1JTJDZmllbGRDeWozJTJDZmllbGRDeWo1JTJDZmllbGRDeWo0JTJDZmllbGRBc2hpcyZjc3JmVG9rZW49ezR9Jmxhbmc9emg)

解决 pyppeteer Browser closed unexpectedly

[https://stackoverflow.com/a/70074296](https://stackoverflow.com/a/70074296)

[jontewks/heroku-buildpack-puppeteer-firefox (github.com)](https://github.com/jontewks/heroku-buildpack-puppeteer-firefox)

[https://github.com/heroku/heroku-buildpack-google-chrome](https://github.com/heroku/heroku-buildpack-google-chrome)

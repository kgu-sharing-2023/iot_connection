# iot_connection
this is connection with R pi and sharing-server

#pycam > h264 recording 

#websocket.js > nodegpio 

need to setting nginx reverse proxy or any other enviroment. 

VPN >> nginx 에서 할당 > 접속 이런 독특한 방식으로 작동함 

openvpn 서버 설정 파일이나 그런 것들은 전부 개인 관련 파일이므로, 직접 설정+조작 필요 

pycam의 경우 외부 접속 가능하게 webdav를 선택했으나, 성능상 문제가 커서 변경 필요 아니면 별도 스크립트로 복사 해야함 

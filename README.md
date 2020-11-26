# Open CCTV(졸업 작품)
 CCTV를 누구나 쉽게 설치할 수 있도록 간단하게 만들어
 저렴한 디바이스 패키지 구축 및 실시간 스트리밍이 가능한 웹사이트.
 
## Prerequisites
 Open CCTV를 만들기 위해선 다음과 같은 환경을 구성해야합니다.
 
 * **Raspberry Pi**  
 
   Raspberry Pi와 카메라 모듈을 이용해 영상 촬영하기 위해 사용
 
 * **Linux**   
   
   Linux 가상환경 구현(이 프로젝트에선 AWS를 통하여 가상환경 셋팅)
   Linux webserver는 웹 어플리케이션 구동을 위해 사용

 * **Flask + Nginx + uWSGI**  
  
   Python3을 활용한 웹 서버 구현을 위해 요구됨 
   
 * **OpenCV**  
  
   얼굴인식 프로그램 구동을 위해 필요함
    

## Installation   
   Open CCTV 는 python3 환경에서 이용가능합니다.
  
 * python3 환경 구성
     
       $ sudo apt-get install python3 python3-venv
       $ sudo apt-get install python3-pip

 * Flask 설치
    
       $ pip3 install Flask
 
 * uWSGI 설치
 
       $ apt-get install uwsgi 
       
 * python과 uWSGI를 연결하는 플러그인

       $ apt-get install uwsgi-plugin-python3
       
 * 추가 예정

 ## URL
 http://18.212.183.253/
  
 * 추가 예정

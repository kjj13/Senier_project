var result = {{resultData|tojson}}; //감사합니다. ㅜㅠㅜㅠㅜ 배열값 넘겨받아서 새로운 배열에 대입.-> 사용하기 쉽게할려고
var container = document.getElementById('map');

var options = {
    center: new kakao.maps.LatLng(36.628788427953396, 127.45624699710056),
    level: 3
};
var map = new kakao.maps.Map(container, options);

var imageSrc = "{{ url_for('static', filename='images/camera.png') }}", // 마커이미지의 주소입니다    
    imageSize = new kakao.maps.Size(64, 69), // 마커이미지의 크기입니다
    imageOption = {
        offset: new kakao.maps.Point(27, 69)
    }; // 마커이미지의 옵션입니다. 마커의 좌표와 일치시킬 이미지 안에서의 좌표를 설정합니다.

// 마커의 이미지정보를 가지고 있는 마커이미지를 생성합니다********************************
var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption);

var markerPosition = new Array();
var iwContent = new Array();


for (var i in result) {
    markerPosition[i] = new kakao.maps.LatLng(result[i][1], result[i][2]); // 마커가 표시될 위치입니다

    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
        position: markerPosition[i],
        image: markerImage,
        map: map,
        clickable: true // 마커를 클릭했을 때 지도의 클릭 이벤트가 발생하도록 설정합니다
    });

    // *************************마커를 클릭했을 때 마커 위에 표시할 인포윈도우를 생성합니다 ***********************************************
    var url = result[i][3];

    //건든거
    iwContent[i] = '<div id="test" name="test_iframe"><iframe name="iframe_test" scrolling="no" frameborder="0" id="ifrm" src="' + url + '" marginwidth="0" marginheight="0"></iframe></div>', // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
        iwRemoveable = true; // removeable 속성을 ture 로 설정하면 인포윈도우를 닫을 수 있는 x버튼이 표시됩니다
    //iwContent[i] = '<div style="text-color:black">텃밭</div>';  //인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
    //document.write(iwContent[i]);

    var infowindow = new kakao.maps.InfoWindow({
        content: iwContent[i], // 인포윈도우에 표시할 내용
        position: markerPosition[i],
        removable: iwRemoveable
    });
    // 마커에 이벤트를 등록하는 함수 만들고 즉시 호출하여 클로저를 만듭니다
    // 클로저를 만들어 주지 않으면 마지막 마커에만 이벤트가 등록됩니다'

    (function (marker, infowindow) {
        // 마커에 mouseover 이벤트를 등록하고 마우스 오버 시 인포윈도우를 표시합니다 
        kakao.maps.event.addListener(marker, 'click', function () {
            infowindow.open(map, marker);
        });
    })(marker, infowindow);

}
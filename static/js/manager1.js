var result1 = {{resultData1 | tojson}};
var num = 1;

for (var i in result1) {
    url1 = result1[i][3];

    document.write('<form>');

    document.write('<tr>');
    //document.write('<td>hi</td>');
    document.write('<td>' + num + '</td>');
    document.write('<td><input type = "text" name = "mem_id" value = "' + result1[i][0] + '" readonly></td>');
    document.write('<td><input type = "text" name = "cctv_name" value = "' + result1[i][1] + '" readonly></td>');
    document.write('<td><input type = "text" name = "cctv_check" value = "' + result1[i][2] + '" readonly></td>');
    //document.write('<td><button onclick="location.href="'+result1[i][3]+'"">영상보기</button></td>')
    document.write('<td><a href="' + url1 + '" target = "_blank">영상 확인</a></td>')
    document.write('<td><button type="submit" formaction="/Authorization" formmethod="POST">권한주기</button></td>');
    document.write('</tr>');

    document.write('</form>');
    num++;
}
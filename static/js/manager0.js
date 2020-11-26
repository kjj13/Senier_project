var result0 = {{resultData0 | tojson}};
var num = 1;

for (var i in result0) {
    url0 = result0[i][3];

    document.write('<form>');

    document.write('<tr>');
    //document.write('<td>hi</td>');
    document.write('<td>' + num + '</td>');
    document.write('<td><input type = "text" name = "mem_id" value = "' + result0[i][0] + '" readonly></td>');
    document.write('<td><input type = "text" name = "cctv_name" value = "' + result0[i][1] + '" readonly></td>');
    document.write('<td><input type = "text" name = "cctv_check" value = "' + result0[i][2] + '" readonly></td>');
    //document.write('<td><button onclick="location.href="'+result1[i][3]+'"">영상보기</button></td>')
    document.write('<td><a href="' + url0 + '" target = "_blank">영상 확인</a></td>')
    document.write('<td><button type="submit" formaction="/Authorization" formmethod="POST">권한주기</button></td>');
    document.write('</tr>');

    document.write('</form>');
    num++;
}
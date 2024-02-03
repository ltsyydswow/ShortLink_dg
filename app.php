<?php
function abc() {
    if (isset($_GET['url'])) {
        $abc = $_GET['url'];
        $def = curl_init();
        curl_setopt($def, CURLOPT_URL, "https://2phx5m-7000.csb.app/?web=" . urlencode($abc));
        curl_setopt($def, CURLOPT_HEADER, 0);
        curl_setopt($def, CURLOPT_RETURNTRANSFER, true);
        $ghi = curl_exec($def);
        if(curl_errno($def)) {
            echo '错误啦: ' . curl_error($def);
        } else {
            echo $ghi;
        }
        curl_close($def);
    } else {
        echo "好家伙，你在抓接口吧.";
    }
}

abc();
?>

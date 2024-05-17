# CoursePowerReader
中部大学が使用している授業管理ツール「Course Power」にて自動でCSVファイルにするプログラム<br>
CPR.exeを起動すると動きます．<br>
<s>お使いのChromeのバージョンにあったchromedriverを同じディレクトリに入れる必要があります<br>
各自でダウンロードしてください<br>
<a href="https://chromedriver.chromium.org/downloads">https://chromedriver.chromium.org/downloads</a><br>
もとから入っているのは105です</s>

# option.txt
オプションを指定できます<br>
<br>USER,PASS<br>
tora-net と同じ　<b>※パスワードが平文で保存されるため取り扱い注意</b><br>
<br>OUTPUT<br>
csvファイルの出力先を指定します<br>
わからなければ「./CPR.csv」でOK<br>
<br>BROWSER<br>
chromedriver.exe のパスを指定します<br>
<br>LOGCOUNT<br>
ログの最大保存回数<br>
回数を超えると古いものから消えていきます<br>
<br>HIDE<br>
ウィンドウが見えるかどうかを指定します<br>
false で非表示<br>
<br>CLOSED<br>
公開終了の取得<br>
false で取得しない<br>
<br>INDEFINITE<br>
期限なしの取得<br>
false で取得しない<br>
<br>STATUS<br>
提出状況の条件<br>
ALL ですべて取得<br>
, で区切る<br>
（例）未提出,未評価,未確認<br>
<br>TEACHIG<br>
教材の条件<br>
ALL ですべて取得<br>

# 使用技術
Python<br>
pyInstaller<br>
Selenium<br>
ChromeDriver<br>

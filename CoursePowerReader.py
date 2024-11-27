from datetime import datetime
from Driver import Browser

USER = ''
PASS = ''
TARGET_CATEGORYS = []
TARGET_STATUS = []
CSV_PATH = ''

def writeCSV(path:str, lines):
    with open(path, 'w', encoding='sjis')as f:
        f.write(f'{datetime.now().strftime("%Y/%m/%d %H:%m")}\n')
        if type(lines) == list:
            for line in lines[:-1]:
                if type(line) == list:
                    for l in line[:-1]:
                        f.write(f'{l},')
                    f.write(f'{line[-1]}\n')
            for l in lines[-1][:-1]:
                f.write(f'{l},')
            f.write(f'{lines[-1][-1]}')

def optionRead(path:str):
    global USER, PASS, TARGET_CATEGORYS, TARGET_STATUS, CSV_PATH
    with open(path, 'r', encoding='sjis') as f:
        USER = f.readline().strip('\n')
        PASS = f.readline().strip('\n')
        TARGET_CATEGORYS = f.readline().strip('\n').split(',')
        TARGET_STATUS = f.readline().strip('\n').split(',')
        CSV_PATH = f.readline().strip('\n')

def main():
    print('optionRead...', end=' ')
    optionRead('option.txt')
    print('OK')
    # ドライバー起動
    print('wakeup Chrome ...', end=' ')
    d = Browser(True, True)
    print('OK')
    # ログイン
    print('login...',end=' ')
    d.jumpURL("https://lms.sti.chubu.ac.jp/lmsv2/lginLgir/#")
    d.sendXPath('//*[@id="loginForm"]/div[1]/div[1]/div[1]/div[2]/input', USER)
    d.sendXPath('//*[@id="loginForm"]/div[1]/div[1]/div[2]/div[2]/input', PASS)
    d.selectList('//*[@id="langList"]', 'ja')
    d.clickXPath('//*[@id="loginForm"]/div[2]/button')
    # ログインチェック
    if(d.getXPath('//*[@id="form-id"]/div/ul/li[4]/a') == None):
        del(d)
        return
    print('OK')

    # データ吸い上げ
    d.clickXPath('//*[@id="homehomlInfo"]/div[2]/span/a') # 学習実績
    lines = []
    for classLine in range(2, len(d.getXPath('//*[@id="list_block"]/table/tbody/tr'))):
        d.clickXPath(f'//*[@id="list_block"]/table/tbody/tr[{classLine}]/td[3]/a') # 科目クリック
        d.clickXPath('//*[@id="M0028"]/a') # 実施
        d.clickXPath('//*[@id="cs_tab_area"]/ul/li[2]/a') # 教材別
        className = d.getXPathText('/html/body/div[7]/div[1]/div[3]/div[1]')
        print(className, end=' ')
        for materialNum in range(1, len(d.getXPath('//*[@id="cs_tab_area2"]/ul/li'))+1):
            material = d.getXPathText(f'//*[@id="cs_tab_area2"]/ul/li[{materialNum}]')
            if material not in TARGET_CATEGORYS and TARGET_CATEGORYS != ['ALL']:
                continue # ターゲットでない教材 continue
            d.clickXPath(f'//*[@id="cs_tab_area2"]/ul/li[{materialNum}]')
            for i in range(2, len(d.getXPath('//*[@id="cs_rightTabinVox"]/div/div/table/tbody/tr')) + 1):
                line = [className, material]
                line += d.getXPathText(f'//*[@id="cs_rightTabinVox"]/div/div/table/tbody/tr[{i}]/td')[1:]
                if line[4] not in TARGET_STATUS and TARGET_STATUS != ['ALL']:
                    continue # ターゲットでない状態 continue
                line[2] = line[2].replace('\n', '/')
                line[3] = line[3].replace('24:00', '23:59')
                lines.append(line)
        print('OK')
        d.clickXPath('/html/body/div[7]/div[1]/div[2]/ul/li[1]/a') # home
        d.clickXPath('//*[@id="homehomlInfo"]/div[2]/span/a') # 学習実績

    print('writing result ...', end=' ')
    writeCSV(CSV_PATH, lines)
    print('OK')

    print('Chrome Quit ...', end=' ')
    d.quit()
    print('OK')

    print('Compleate!!')

if __name__ == '__main__':
    main()

import datetime
import time
import FinanceDataReader as fdr
import pandas as pd
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import pyperclip
import os
import random

def Autoposting(title,contents,title_2,contents_2):
    try:
        path = chromedriver_autoinstaller.install()
        driver = webdriver.Chrome(path)
        time.sleep(2)

        driver.get("https://www.tistory.com/auth/login")
        # 계정 로그인 버튼 클릭
        driver.find_element(By.XPATH,'//*[@id="cMain"]/div/div/div/a[2]').click()
        time.sleep(2)
        # 로그인
        username=driver.find_element(By.XPATH,'//*[@id="loginKey--1"]')
        username.send_keys('') #ID

        password=driver.find_element(By.XPATH,'//*[@id="password--2"]')
        password.send_keys('') #PW
    

        driver.find_element(By.XPATH,'//*[@id="mainContent"]/div/div/form/div[4]/button[1]').click()
        time.sleep(2)

        # 글 작성 페이지 이동
        # driver.find_element(By.XPATH,'//*[@id="kakaoHead"]/div/div[3]/div/a[2]').click()
        # driver.find_element(By.XPATH,'//*[@id="kakaoHead"]/div/div[3]/div/div/div/div[2]/div/div/a[2]').click()
        # time.sleep(2)
        driver.get("https://hiisk.tistory.com/manage")
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="mFeature"]/div[2]/a[1]').click()
        time.sleep(2)

        # 임시 저장글 피하기
        pyautogui.press('right')
        pyautogui.press('enter')
        time.sleep(2)

        # 카테고리 선택
        driver.find_element(By.XPATH,'//*[@id="editorContainer"]/div/div[1]/div').click()
        driver.find_element(By.XPATH,'//*[@id="category-item-1080614"]').click()
        time.sleep(2)

        #HTML 변경
        driver.find_element(By.XPATH,'//*[@id="editor-mode-layer-btn"]').click()
        driver.find_element(By.XPATH,'//*[@id="editor-mode-html-text"]').click()
        time.sleep(2)
        
        # 제목 입력
        title_area=driver.find_element(By.XPATH,'//*[@id="post-title-inp"]')
        title_area.send_keys(title)
        time.sleep(5)
        

        # 내용 입력
        # tiny_area=driver.find_element(By.XPATH,'//*[@id="tinymce"]/p')
        # tiny_area.send_keys(contents)
        pyautogui.press('tab',presses=2)
        pyperclip.copy(contents)
        pyautogui.hotkey('ctrl', 'v') # 붙여넣기
        time.sleep(5)


        # 완료 버튼 클릭
        driver.find_element(By.XPATH,'//*[@id="publish-layer-btn"]').click()
        time.sleep(5)

        # 공개 발행 - 끝
        driver.find_element(By.XPATH,'//*[@id="publish-btn"]').click()
        print("포스팅 완료")
        time.sleep(10)
        AutoLike()


        #===========================================================================================
        # 두번째 글
        driver.find_element(By.XPATH,'//*[@id="mFeature"]/div[2]/a[1]').click()
        time.sleep(2)
        
        # 임시 저장글 피하기
        pyautogui.press('right')
        pyautogui.press('enter')
        time.sleep(2)
        
        # 카테고리 선택
        driver.find_element(By.XPATH,'//*[@id="editorContainer"]/div/div[1]/div').click()
        driver.find_element(By.XPATH,'//*[@id="category-item-1080614"]').click()
        time.sleep(2)

        #HTML 변경
        driver.find_element(By.XPATH,'//*[@id="editor-mode-layer-btn"]').click()
        driver.find_element(By.XPATH,'//*[@id="editor-mode-html-text"]').click()
        time.sleep(2)
        
        # 제목 입력
        title_area=driver.find_element(By.XPATH,'//*[@id="post-title-inp"]')
        title_area.send_keys(title_2)
        time.sleep(5)
        
        # 내용 입력
        # tiny_area=driver.find_element(By.XPATH,'//*[@id="tinymce"]/p')
        # tiny_area.send_keys(contents)
        pyautogui.press('tab',presses=2)
        pyperclip.copy(contents_2)
        pyautogui.hotkey('ctrl', 'v') # 붙여넣기
        time.sleep(10)

        # 완료 버튼 클릭
        driver.find_element(By.XPATH,'//*[@id="publish-layer-btn"]').click()
        time.sleep(5)

        # 공개 발행 - 끝
        driver.find_element(By.XPATH,'//*[@id="publish-btn"]').click()
        print("포스팅 완료")
        time.sleep(10)
        AutoLike()

    except FileNotFoundError as err:
        print("크롬 브라우저를 찾을 수 없습니다. 오류")

def AutoLike():
    path = chromedriver_autoinstaller.install()
    option = webdriver.ChromeOptions()
    option.add_argument('--incognito')
    driver = webdriver.Chrome(path, options = option)
    driver.get("https://hiisk.tistory.com/")
    time.sleep(2)
    link_list = driver.find_elements(By.CSS_SELECTOR, ".link-article")
    for i in link_list:
        link = i.get_attribute('href')
        break
    for i in range(random.randint(5,10)):
        time.sleep(2)
        driver = webdriver.Chrome(path, options = option)
        driver.get(link)
        like = driver.find_element(By.CLASS_NAME,'wrap_btn')
        id = like.get_attribute('id')
        driver.find_element(By.XPATH,f'//*[@id="{id}"]/button').send_keys(Keys.ENTER)
    print("좋아요 완료")

current = datetime.datetime.now() 
# 주말이고 컴퓨터를 사용하지 않을 때 종료
if current.weekday() in (5,6) and time.monotonic() < 600: 
    os.system("shutdown /s")

# if 0 <= datetime.datetime.today().weekday() <= 5 and datetime.datetime.now().hour <= 18:
types = ['KRX'] #'ETF/KR'
title = (f'{current.year}년 {current.month}월 {current.day}일 국내시장 종가기준 주가전망 급등주 분석 TOP100')
title_2 = (f'{current.year}년 {current.month}월 {current.day}일 국내시장 종가기준 모든상장종목 주가분석')
# elif 1 <= datetime.datetime.today().weekday() <= 5 and datetime.datetime.now().hour >= 8:
#     types = ['NASDAQ','AMEX','NYSE']
#     current -= datetime.timedelta(days=1)
#     title = (f'미국시장 종가를 이용한 주가 전망 분석 TOP 100 [{current.year}년 {current.month}월 {current.day}일]')

df = pd.DataFrame()
df.insert(0, "주가", "")
df.insert(1, "전일 주가", "")
df.insert(2, "등락률", "")
df.insert(3, "5일 수익률", "")
df.insert(4, "20일 수익률", "")
df.insert(5, "60일 수익률", "")
df.insert(6, "120일 수익률", "")
df.insert(7, "5일 전 주가", "")
df.insert(8, "20일 전 주가", "")
df.insert(9, "60일 전 주가", "")
df.insert(10, "120일 전 주가", "")

#개장 확인용 함수
stock_open = True

for type in types:
    stocks = fdr.StockListing(type)
    cnt = 0
    if not stock_open:
        break

    # 한국은 fdr에서 정보가져오지만, 해외는 불가
    if type == 'KRX': 
        st_data = pd.DataFrame(fdr.DataReader('005930', datetime.datetime.now().date() - datetime.timedelta(days=10))) #값 불러오기
        valdation = (st_data.tail(1).T.columns == str(datetime.datetime.now().date()))  #오늘자 데이터 있는지 확인
        if not valdation: # 상장 폐지, 첫날일 경우 & 오늘자 데이터 없을 경우 제외 삼전으로 확인
            stock_open = False
            break
        for stock, name in zip(stocks["Code"], stocks["Name"]):
            cnt+=1
            print(f'{type}: {cnt}/{len(stocks)} 진행률:{round(cnt/len(stocks)*100,2)}% 코드: {stock} 주식: {name}')
            st_data = pd.DataFrame(fdr.DataReader(stock)) #값 불러오기
            len_st_data = len(st_data)
            if len_st_data < 2:
                continue
            # 5일 이동평균선
            if len_st_data >= 5:
                day_5 = round((st_data['Close'][-1]-st_data['Close'][-5])/st_data['Close'][-5]*100,2)
                day_5_price = st_data['Close'][-5]
            else:
                day_5 = -100
                day_5_price = 0
            # 20일 이동평균선
            if len_st_data >= 20:
                day_20 = round((st_data['Close'][-1]-st_data['Close'][-20])/st_data['Close'][-20]*100,2)
                day_20_price = st_data['Close'][-20]
            else:
                day_20 = -100
                day_20_price = 0
            # 60일 이동평균선
            if len_st_data >= 60:
                day_60 = round((st_data['Close'][-1]-st_data['Close'][-60])/st_data['Close'][-60]*100,2)
                day_60_price = st_data['Close'][-60]
            else:
                day_60 = -100
                day_60_price = 0
            # 120일 이동평균선
            if len_st_data >= 120:
                day_120 = round((st_data['Close'][-1]-st_data['Close'][-120])/st_data['Close'][-120]*100,2)
                day_120_price = st_data['Close'][-120]
            else:
                day_120 = -100
                day_120_price = 0
            df.loc[name] = ["%g" %(st_data['Close'][-1]),st_data['Close'][-2],round((st_data['Close'][-1]-st_data['Close'][-2])/st_data['Close'][-2]*100,2),day_5,day_20,day_60,day_120,day_5_price,day_20_price,day_60_price,day_120_price]
    elif type == 'ETF/KR': 
        st_data = pd.DataFrame(fdr.DataReader('005930', datetime.datetime.now().date() - datetime.timedelta(days=10))) #값 불러오기
        valdation = (st_data.tail(1).T.columns == str(datetime.datetime.now().date()))  #오늘자 데이터 있는지 확인
        if not valdation: # 상장 폐지, 첫날일 경우 & 오늘자 데이터 없을 경우 제외 삼전으로 확인
            stock_open = False
            break
        for stock, name in zip(stocks["Symbol"], stocks["Name"]):
            cnt+=1
            print(f'{type}: {cnt}/{len(stocks)} 진행률:{round(cnt/len(stocks)*100,2)}% 코드: {stock} 주식: {name}')
            st_data = pd.DataFrame(fdr.DataReader(stock)) #값 불러오기
            len_st_data = len(st_data)
            if len_st_data < 2:
                continue
            # 5일 이동평균선
            if len_st_data >= 5:
                day_5 = round((st_data['Close'][-1]-st_data['Close'][-5])/st_data['Close'][-5]*100,2)
                day_5_price = st_data['Close'][-5]
            else:
                day_5 = -100
                day_5_price = 0
            # 20일 이동평균선
            if len_st_data >= 20:
                day_20 = round((st_data['Close'][-1]-st_data['Close'][-20])/st_data['Close'][-20]*100,2)
                day_20_price = st_data['Close'][-20]
            else:
                day_20 = -100
                day_20_price = 0
            # 60일 이동평균선
            if len_st_data >= 60:
                day_60 = round((st_data['Close'][-1]-st_data['Close'][-60])/st_data['Close'][-60]*100,2)
                day_60_price = st_data['Close'][-60]
            else:
                day_60 = -100
                day_60_price = 0
            # 120일 이동평균선
            if len_st_data >= 120:
                day_120 = round((st_data['Close'][-1]-st_data['Close'][-120])/st_data['Close'][-120]*100,2)
                day_120_price = st_data['Close'][-120]
            else:
                day_120 = -100
                day_120_price = 0
            df.loc[name] = ["%g" %(st_data['Close'][-1]),st_data['Close'][-2],round((st_data['Close'][-1]-st_data['Close'][-2])/st_data['Close'][-2]*100,2),day_5,day_20,day_60,day_120,day_5_price,day_20_price,day_60_price,day_120_price]
    else: # 'NASDAQ','AMEX','NYSE'
        for stock, name in zip(stocks["Symbol"], stocks["Name"]):
            cnt+=1
            print(f'{type}: {cnt}/{len(stocks)} 진행률:{round(cnt/len(stocks)*100,2)}% 코드: {stock} 주식: {name}')
            st_data = pd.DataFrame(fdr.DataReader(stock)) #값 불러오기
            len_st_data = len(st_data)
            if len_st_data < 2:
                continue
            # 5일 이동평균선
            if len_st_data >= 5:
                day_5 = round((st_data['Adj Close'][-1]-st_data['Adj Close'][-5])/st_data['Adj Close'][-5]*100,2)
                day_5_price = round(st_data['Adj Close'][-5],2)
            else:
                day_5 = -100
                day_5_price = 0
            # 20일 이동평균선
            if len_st_data >= 20:
                day_20 = round((st_data['Adj Close'][-1]-st_data['Adj Close'][-20])/st_data['Adj Close'][-20]*100,2)
                day_20_price = round(st_data['Adj Close'][-20],2)
            else:
                day_20 = -100
                day_20_price = 0
            # 60일 이동평균선
            if len_st_data >= 60:
                day_60 = round((st_data['Adj Close'][-1]-st_data['Adj Close'][-60])/st_data['Adj Close'][-60]*100,2)
                day_60_price = round(st_data['Adj Close'][-60],2)
            else:
                day_60 = -100
                day_60_price = 0
            # 120일 이동평균선
            if len_st_data >= 120:
                day_120 = round((st_data['Adj Close'][-1]-st_data['Adj Close'][-120])/st_data['Adj Close'][-120]*100,2)
                day_120_price = round(st_data['Adj Close'][-120],2)
            else:
                day_120 = -100
                day_120_price = 0
            df.loc[name] = [round(st_data['Adj Close'][-1],2),round(st_data['Adj Close'][-2],2),round((st_data['Adj Close'][-1]-st_data['Adj Close'][-2])/st_data['Adj Close'][-2]*100,2),day_5,day_20,day_60,day_120,day_5_price,day_20_price,day_60_price,day_120_price]
            if cnt > 50 and len(df) < 1: # 50개까지 확인 시 1개도 없을 경우 탈출
                stock_open = False
                break
if stock_open:
    #등락률
    df_high = df.sort_values(by='등락률' ,ascending=False)
    df_high = df_high.head(100)
    df_high = df_high.reset_index()
    df_high.index = df_high.index+1
    df_high = df_high.rename(columns={'index':'종목'})
    df_high['등락률'] = df_high['등락률'].astype(str) + "%"

    #5일
    df_5day = df.sort_values(by='5일 수익률' ,ascending=False)
    df_5day = df_5day.head(100)
    df_5day = df_5day.reset_index()
    df_5day.index = df_5day.index+1
    df_5day = df_5day.rename(columns={'index':'종목'})
    df_5day['5일 수익률'] = df_5day['5일 수익률'].astype(str) + "%"

    #20일
    df_20day = df.sort_values(by='20일 수익률' ,ascending=False)
    df_20day = df_20day.head(100)
    df_20day = df_20day.reset_index()
    df_20day.index = df_20day.index+1
    df_20day = df_20day.rename(columns={'index':'종목'})
    df_20day['20일 수익률'] = df_20day['20일 수익률'].astype(str) + "%"

    #60일
    df_60day = df.sort_values(by='60일 수익률' ,ascending=False)
    df_60day = df_60day.head(100)
    df_60day = df_60day.reset_index()
    df_60day.index = df_60day.index+1
    df_60day = df_60day.rename(columns={'index':'종목'})
    df_60day['60일 수익률'] = df_60day['60일 수익률'].astype(str) + "%"

    #120일
    df_120day = df.sort_values(by='120일 수익률' ,ascending=False)
    df_120day = df_120day.head(100)
    df_120day = df_120day.reset_index()
    df_120day.index = df_120day.index+1
    df_120day = df_120day.rename(columns={'index':'종목'})
    df_120day['120일 수익률'] = df_120day['120일 수익률'].astype(str) + "%"

    #전체
    df_all = df.sort_values(by='등락률' ,ascending=False)
    df_all = df_all.reset_index()
    df_all.index = df_all.index+1
    df_all = df_all.rename(columns={'index':'종목'})
    df_all['등락률'] = df_all['등락률'].astype(str) + "%"

    graph_type = ['등락률','5일 수익률','20일 수익률','60일 수익률','120일 수익률']

    contents = """
    <p data-ke-size="size16"> </p>
    <p data-ke-size="size16"> </p>
    <p style="text-align: center;" data-ke-size="size16"><span style="color: #000000;">투자에 대한 모든 책임은 본인에게 있습니다.</span></p>
    <p style="text-align: center;" data-ke-size="size16"><span style="color: #000000;">해당 자료는 국내주식 시세 실제 데이터를 기반으로 작성한 자료입니다.</span></p>
    <p data-ke-size="size16"> </p>
    """

    for type in graph_type:
        contents += f"""<p style="text-align: center;" data-ke-size="size16"><b>{type} 상위 기준 TOP100</b></p>
    <table style="border-collapse: collapse; width: 100%;" border="1">
    <tbody>
    <tr>
    <td><span><b><span style="color: #000000;">순위<span></span></span></b></span></td>
    <td><span><b><span>종목<span></span></span></b></span></td>
    <td><span><b><span>주가<span></span></span></b></span></td>
    """
        if type == '등락률':
            contents += f"""
    <td><span><b><span>전일 주가<span></span></span></b></span></td>
    <td><span><b><span>{type}<span></span></span></b></span></td>
    </tr>
    """
            for i in range(100):
                contents += f"""<tr>
    <td><span><b><span>{i+1}</span></b></span></td>
    <td><span><span style="color: #000000;">{df_high.loc[i+1]['종목']}<span></span></span></span></td>
    <td><span><span style="color: #000000;">{df_high.loc[i+1]['주가']}</span></span></td>
    <td><span><span style="color: #000000;">{df_high.loc[i+1]['전일 주가']}</span></span></td>
    <td><span><span style="color: #000000;">{df_high.loc[i+1][type]}</span></span></td>
    </tr>
    """
        elif type == '5일 수익률':
            contents += f"""
    <td><span><b><span>5일 전 주가<span></span></span></b></span></td>
    <td><span><b><span>5일 수익률<span></span></span></b></span></td>
    </tr>
    """
            for i in range(100):
                contents += f"""<tr>
    <td><span><b><span>{i+1}</span></b></span></td>
    <td><span><span style="color: #000000;">{df_5day.loc[i+1]['종목']}<span></span></span></span></td>
    <td><span><span style="color: #000000;">{df_5day.loc[i+1]['주가']}</span></span></td>
    <td><span><span style="color: #000000;">{df_5day.loc[i+1]['5일 전 주가']}</span></span></td>
    <td><span><span style="color: #000000;">{df_5day.loc[i+1][type]}</span></span></td>
    </tr>
    """
        elif type == '20일 수익률':
            contents += f"""
    <td><span><b><span>20일 전 주가<span></span></span></b></span></td>
    <td><span><b><span>20일 수익률<span></span></span></b></span></td>
    </tr>
    """
            for i in range(100):
                contents += f"""<tr>
    <td><span><b><span>{i+1}</span></b></span></td>
    <td><span><span style="color: #000000;">{df_20day.loc[i+1]['종목']}<span></span></span></span></td>
    <td><span><span style="color: #000000;">{df_20day.loc[i+1]['주가']}</span></span></td>
    <td><span><span style="color: #000000;">{df_20day.loc[i+1]['20일 전 주가']}</span></span></td>
    <td><span><span style="color: #000000;">{df_20day.loc[i+1][type]}</span></span></td>
    </tr>
    """
        elif type == '60일 수익률':
            contents += f"""
    <td><span><b><span>60일 전 주가<span></span></span></b></span></td>
    <td><span><b><span>60일 수익률<span></span></span></b></span></td>
    </tr>
    """
            for i in range(100):
                contents += f"""<tr>
    <td><span><b><span>{i+1}</span></b></span></td>
    <td><span><span style="color: #000000;">{df_60day.loc[i+1]['종목']}<span></span></span></span></td>
    <td><span><span style="color: #000000;">{df_60day.loc[i+1]['주가']}</span></span></td>
    <td><span><span style="color: #000000;">{df_60day.loc[i+1]['60일 전 주가']}</span></span></td>
    <td><span><span style="color: #000000;">{df_60day.loc[i+1][type]}</span></span></td>
    </tr>
    """
        elif type == '120일 수익률':
            contents += f"""
    <td><span><b><span>120일 전 주가<span></span></span></b></span></td>
    <td><span><b><span>120일 수익률<span></span></span></b></span></td>
    </tr>
    """
            for i in range(100):
                contents += f"""<tr>
    <td><span><b><span>{i+1}</span></b></span></td>
    <td><span><span style="color: #000000;">{df_120day.loc[i+1]['종목']}<span></span></span></span></td>
    <td><span><span style="color: #000000;">{df_120day.loc[i+1]['주가']}</span></span></td>
    <td><span><span style="color: #000000;">{df_120day.loc[i+1]['120일 전 주가']}</span></span></td>
    <td><span><span style="color: #000000;">{df_120day.loc[i+1][type]}</span></span></td>
    </tr>
    """
        contents += """
    </tbody>
    </table>
    <p data-ke-size="size16"> </p>
    <p data-ke-size="size16"> </p>
    <figure class="ad-wp" contenteditable="false" data-ke-type="revenue" data-ad-vendor="adsense" data-ad-id-pc="64576" data-ad-id-mobile="68671"></figure>
    <p data-ke-size="size16"> </p>
    <p data-ke-size="size16"> </p>
    <p data-ke-size="size16"> </p>
    <p data-ke-size="size16"> </p>
    """

    # 주식 전체 포스팅 내용
    contents_2 = """
    <p data-ke-size="size16"> </p>
    <p data-ke-size="size16"> </p>
    <p style="text-align: center;" data-ke-size="size16"><span style="color: #000000;">한국거래소에 상장한 모든 주식을 기준으로 작성하였습니다.</span></p>
    <p data-ke-size="size16"> </p>
    <table style="border-collapse: collapse; width: 100%;" border="1">
    <tbody>
    <tr>
    <td><span><b><span style="color: #000000;">순위<span></span></span></b></span></td>
    <td><span><b><span>종목<span></span></span></b></span></td>
    <td><span><b><span>주가<span></span></span></b></span></td>
    <td><span><b><span>전일 주가<span></span></span></b></span></td>
    <td><span><b><span>등락률<span></span></span></b></span></td>
    </tr>
    """
    for i in range(len(df_all)):
                contents_2 += f"""<tr>
    <td><span><b><span>{i+1}</span></b></span></td>
    <td><span><span style="color: #000000;">{df_all.loc[i+1]['종목']}<span></span></span></span></td>
    <td><span><span style="color: #000000;">{df_all.loc[i+1]['주가']}</span></span></td>
    <td><span><span style="color: #000000;">{df_all.loc[i+1]['전일 주가']}</span></span></td>
    <td><span><span style="color: #000000;">{df_all.loc[i+1]['등락률']}</span></span></td>
    </tr>
    """
                
    contents_2 += """
    </tbody>
    </table>
    <p data-ke-size="size16"> </p>
    <p data-ke-size="size16"> </p>
    <figure class="ad-wp" contenteditable="false" data-ke-type="revenue" data-ad-vendor="adsense" data-ad-id-pc="64576" data-ad-id-mobile="68671"></figure>
    <p data-ke-size="size16"> </p>
    <p data-ke-size="size16"> </p>
    <p data-ke-size="size16"> </p>
    <p data-ke-size="size16"> </p>
    """
    try:
        Autoposting(title,contents,title_2,contents_2)
        #평일일 경우 전부 실행 후 종료
        os.system("shutdown /s /f")
    except:
        os.system("shutdown /s /f")
else:
    #평일 공휴일 조건
    os.system("shutdown /s /f")
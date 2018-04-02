from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

browser = webdriver.Firefox()
browser.get("http://krc.gitam.edu/papers")
campus_selection = browser.find_element_by_id("ddlcampus").click()
vizag_selector = browser.find_element_by_xpath("/html/body/section/form/div/div/div[2]/div/div[2]/select/option[2]").click() #as I'm a vizag campus guy, I picked that option. look through source code of page and edit this line so it'll select whichever campus you belong to.
college_selector = browser.find_element_by_id("ddlcollege").click()
collegeselector = browser.find_element_by_xpath("/html/body/section/form/div/div/div[2]/div/div[4]/select/option[11]").click() #I'm a BTech guy, so GIT is my college. Again, search through HTML code to find your college. GIT or GIM or whatever.
degree_clicker = browser.find_element_by_id("ddldegree").click()
degree_selector = browser.find_element_by_xpath("/html/body/section/form/div/div/div[2]/div/div[6]/select/option[2]").click() #I'm btech, whatever you are, pick that by looking around the source code
branch_clicker = browser.find_element_by_id("ddlbranch").click()
branch_selector = browser.find_element_by_xpath("/html/body/section/form/div/div/div[2]/div[1]/div[8]/select/option[4]").click()
year_clicker = browser.find_element_by_id("ddlyear").click() #so this helps you chose which year's papers you want. A WORD OF CAUTION: 'Find out from which year onwards you have papers available.' Manually change the year by making changes to the below line of code after checking through source code of page. So if you have qps available from 2011, you change the below code for each year and sit through the whole process till you download till the present year. 
year_selector = browser.find_element_by_xpath("/html/body/section/form/div/div/div[2]/div[1]/div[10]/select/option[3]").click() #edit this from source code's options depending on which year you belong to.
acayear_clicker = browser.find_element_by_id("ddlacyear").click()
acayear_selector = browser.find_element_by_xpath("/html/body/section/form/div/div/div[2]/div[1]/div[12]/select/option[10]").click() #pick your academic year by looking through the source code of the page
semester_clicker = browser.find_element_by_id("ddlsem").click() #same here, look through source code, find your semester and click it.
semester_selector = browser.find_element_by_xpath("/html/body/section/form/div/div/div[2]/div[1]/div[14]/select/option[5]").click()
view_clicker = browser.find_element_by_xpath("//*[@id='submit']").click() #you are pushing the view button to display results

#so here, we have an issue. Using selenium, browser is automated, but you can't make the browser select save page or open from the pop up window when you hit download. So, you have to sit tight. Run this code and once its run, it'll click on all the download buttons. You then manually keep click Save file for all dialog boxes.
subject_1 = browser.find_element_by_xpath("/html/body/section/form/div/div/div[2]/div[2]/ul[1]/li/div[3]/a").click()
subject_2 = browser.find_element_by_xpath("/html/body/section/form/div/div/div[2]/div[2]/ul[2]/li/div[3]/a").click()
subject_3 = browser.find_element_by_xpath("/html/body/section/form/div/div/div[2]/div[2]/ul[3]/li/div[3]/a").click()
subject_4 = browser.find_element_by_xpath("/html/body/section/form/div/div/div[2]/div[2]/ul[4]/li/div[3]/a").click()
subject_5 = browser.find_element_by_xpath("/html/body/section/form/div/div/div[2]/div[2]/ul[5]/li/div[3]/a").click()
subject_6 = browser.find_element_by_xpath("/html/body/section/form/div/div/div[2]/div[2]/ul[6]/li/div[3]/a").click()

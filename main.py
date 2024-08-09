from bs4 import BeautifulSoup
import requests
import time


'''with open('home.html','r') as html_file:
    content = html_file.read()
    #print(content)

    soup = BeautifulSoup(content,'lxml')
    #print(soup.prettify())

    courses_html_tags=soup.find_all('h5')
    print(courses_html_tags)

    for course in courses_html_tags:
        print(course.text)

    course_cards=soup.find_all('div',class_='card')
    for course in course_cards:
        #print(course)
        #print(course.h5)
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        #print(course_name)
        #print(course_price)
        print(f'{course_name} costs {course_price}')'''
print('put some skill that you are not familiar with')
unfamiliar_skills = input('>')
print(f'filtering out {unfamiliar_skills}')
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    #print(html_text)

    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    #print(job1)
    for index,job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_='srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skills not in skills:
                #print(company_name)
                #print(skills)
                #print(published_date)
                with open(f'posts/{index}.txt','w') as f:
                    '''print(f"Company Name : {company_name.strip()}")
                    print(f"SKills : {skills.strip()}")
                    print(f"More Info : {more_info}")'''
                    f.write(f"Company Name : {company_name.strip()}\n")
                    f.write(f" Required Skills : {skills.strip()}\n")
                    f.write(f"More Info : {more_info}\n")
                print(f'file saved : {index}')
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print(f"waiting {time_wait} minutes...")
        time.sleep(time_wait*60)



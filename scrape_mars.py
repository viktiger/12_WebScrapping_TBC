# Import Dependencies / Modules / Libraries
import pandas as pd
import time
# import requests
# import re
# import pymongo
# import os

from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

def init_browser():
    # executable_path = {"executable_path": ChromeDriverManager().install()}
    executable_path = {"executable_path": "chromedriver.exe"}
    return browser = Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_data = {}

    #################################################
    ## NASA Mars News
    #################################################

    # Read HTML 
    news_url = "https://redplanetscience.com/"
    news_site = browser.visit(news_url)

    # Parse site with Beautiful Soup
    news_soup = BeautifulSoup(browser.html, "html.parser")

    # Print body of site
    # print(news_soup.prettify()) 

    # Visit the Mars news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Extract title text
    title = news_soup.title.text
    print(title)
    print("-------------------------")

    # Print all title headlines 
    titles = news_soup.find_all('div', class_='content_title')
    # titles
    for news_title in titles:
        titles = news_title.find('t')
        print(news_title.text)

    # Extract paragrapgh text
    paragraphs = news_soup.find_all('div', class_='article_teaser_body')
    # print(paragraphs)

    for news_paragraph in paragraphs:
        paragraphs = news_paragraph.find('t')
        print(news_paragraph.text)
    
    #################################################
    ## JPL Mars Space Images — Featured Image
    #################################################

    # Read HTML 
    image_url = "https://spaceimages-mars.com"
    browser.visit(image_url)
    # time.sleep(1)

    # Parse site with Beautiful Soup
    image_soup = BeautifulSoup(browser.html, "html.parser")

    # Print body of site
    # print(image_soup.prettify())

    #Find first Mars image url
    image_path1 = image_soup.find('img', class_='headerimage fade-in').get('src')
    # image_path2 = image_soup.find('img', class_='thumbimg').get('src')

    #Combine url to get image path
    featured_image_url1 = f"https://spaceimages-mars.com/{image_path1}"
    # featured_image_url2 = f"https://spaceimages-mars.com/{image_path2}"

    print(featured_image_url1)
    # print(featured_image_url2)

    #################################################
    # Mars Facts
    #################################################

    # Scrappe table using Pandas
    Facts_df = pd.read_html("https://galaxyfacts-mars.com")
    print(Facts_df[0])
    print("-------------------------")
    print(Facts_df[1])

    # Reset table 
    Facts_df[0].columns = ["Properties", "Mars", "Earth"]
    Table1 = Facts_df[0]
    NewTable1 = Table1.drop(labels=None, axis=0, index=0, columns=None, inplace=False)
    NewTable1

    # Reset table columns
    Facts_df[1].columns = ["Properties", "Measures"]
    Table2 = Facts_df[1]
    Table2

    NewTable1.to_html()
    # Table2.to_html()

    #################################################
    # Mars Hemispheres
    #################################################

    # Read HTML 
    hemispheres_url = "https://marshemispheres.com/"
    browser.visit(hemispheres_url)

    # Parse site with Beautiful Soup
    hemispheres_soup = BeautifulSoup(browser.html, "html.parser")

    # Print body of site
    # print(hemispheres_soup.prettify())

    # Get image titles
    hemisphere_titles = hemispheres_soup.find_all('div', class_='item')
    # print(hemisphere_titles)
    for hemisphere_imagetitles in hemisphere_titles:
        hemisphere_titles = hemisphere_imagetitles.find('h3')
        print(hemisphere_titles.text)
            
    print("-------------------------")

    # Get image urls
    hemisphere_images = hemispheres_soup.find_all('img', class_='thumb')
    # print(hemisphere_images)
    for hemisphere_imageurls in hemisphere_images:
        hemisphere_images = hemisphere_imageurls.get('src')
        print(hemisphere_images)

    print("-------------------------")

    # hemisphere_image0 = hemispheres_soup.find_all('img', class_='thumb')[0].get('src')
    # hemisphere_image1 = hemispheres_soup.find_all('img', class_='thumb')[1].get('src')
    # hemisphere_image2 = hemispheres_soup.find_all('img', class_='thumb')[2].get('src')
    # hemisphere_image3 = hemispheres_soup.find_all('img', class_='thumb')[3].get('src')

    # print(hemisphere_image0)
    # print(hemisphere_image1)
    # print(hemisphere_image2)
    # print(hemisphere_image3)

    # Append image title and URL into a dictionary and append the dictionaries into a list
    hemisphere_image_urls = [
        {"title": "Cerberus Hemisphere", "img_url": hemisphere_image0}, 
        {"title": "Schiaparelli Hemisphere", "img_url": hemisphere_image1}, 
        {"title": "Syrtis Major Hemisphere", "img_url": hemisphere_image2}, 
        {"title": "Valles Marineris Hemisphere", "img_url": hemisphere_image3}]

    hemisphere_image_urls 

    browser.quit()
    return mars_data

if __name__ == '__main__':
    app.run(debug=True)
    scrape_mars()
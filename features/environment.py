from features.browser import Browser
from selenium import webdriver

def befor_all(context):
    context.browser = Browser()

def after_all(context):
    context.browser.close()




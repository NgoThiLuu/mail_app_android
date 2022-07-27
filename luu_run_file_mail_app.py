import time, json, random
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from random import choice
from random import randint
import re
from sys import exit
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
import pathlib
from pathlib import Path
import os
from sys import platform
import appium_mail_app_python_luungo
from appium_mail_app_python_luungo import execution_log, fail_log, error_log, Logging

def Luu_mail_app_linux_Execution():
    error_menu = []
    #error_screenshot = []
    try:
        appium_mail_app_python_luungo.log_in_mail_app()
    except:
        Logging("Cannot continue execution")
        error_menu.append("appium_python_luungo.log_in_mail_app")
    
    try:
        appium_mail_app_python_luungo.send_mail_app()
    except:
        Logging("Cannot continue execution")
        error_menu.append("appium_python_luungo.send_mail_app")

    try:
        appium_mail_app_python_luungo.vacation_auto_replies_mail_app()
    except:
        Logging("Cannot continue execution")
        error_menu.append("appium_python_luungo.vacation_auto_replies_mail_app")

    try:
        appium_mail_app_python_luungo.auto_sort_mail_app()
    except:
        Logging("Cannot continue execution")
        error_menu.append("appium_python_luungo.auto_sort_mail_app")

    luu_log = {
        "execution_log": execution_log,
        "fail_log": fail_log,
        "error_log": error_log,
        "error_menu": error_menu
    }

    return luu_log

def Luu_mail_app_Execution():
    
    appium_mail_app_python_luungo.log_in_mail_app()
    appium_mail_app_python_luungo.send_mail_app()
    appium_mail_app_python_luungo.vacation_auto_replies_mail_app()
    appium_mail_app_python_luungo.auto_sort_mail_app()
    

    luu_log = {
        "execution_log": execution_log,
        "fail_log": fail_log,
        "error_log": error_log
    }

    return luu_log
    

Luu_mail_app_Execution()


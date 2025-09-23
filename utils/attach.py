import allure
from allure_commons.types import AttachmentType
import os


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')

def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')

def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')

def add_video(browser):
    # Внешний URL на Selenoid, доступный из браузера
    selenoid_url = "selenoid.autotests.cloud"
    session_id = browser.driver.session_id

    video_url = f"https://{selenoid_url}/video/{session_id}.mp4"

    html = f"""
    <html>
      <body>
        <video width="100%" height="100%" controls autoplay>
          <source src="{video_url}" type="video/mp4">
          Your browser does not support video playback.
        </video>
      </body>
    </html>
    """
    allure.attach(html, f"video_{session_id}", AttachmentType.HTML, ".html")
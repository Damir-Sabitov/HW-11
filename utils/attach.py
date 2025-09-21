from pathlib import Path
import allure
import os

SCREENSHOTS_DIR = Path("screenshots")
LOGS_DIR = Path("logs")
HTML_DIR = Path("html")
VIDEO_DIR = Path("video")

SCREENSHOTS_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)
HTML_DIR.mkdir(exist_ok=True)
VIDEO_DIR.mkdir(exist_ok=True)

def add_screenshot(browser, name="Screenshot"):
    screenshot_file = SCREENSHOTS_DIR / "screenshot.png"
    browser.screenshot(str(screenshot_file))  # сохраняем файл
    allure.attach.file(screenshot_file, name=name, attachment_type=allure.attachment_type.PNG)

def add_logs(browser, name="Browser Logs"):
    log_file = LOGS_DIR / "browser.log"
    logs = "\n".join(browser.driver.get_log("browser"))
    log_file.write_text(logs, encoding="utf-8")
    allure.attach.file(log_file, name=name, attachment_type=allure.attachment_type.TEXT)

def add_html(browser, name="Page HTML"):
    html_file = HTML_DIR / "page.html"
    html_content = browser.driver.page_source
    html_file.write_text(html_content, encoding="utf-8")
    allure.attach.file(html_file, name=name, attachment_type=allure.attachment_type.HTML)

def add_video(browser, name="Test Video"):
    video_file = VIDEO_DIR / "video.mp4"
    # Здесь предполагается, что видео уже сохраняется Selenoid. Если нет, нужно скопировать файл
    if video_file.exists():
        allure.attach.file(video_file, name=name, attachment_type=allure.attachment_type.MP4)
# hellp.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# 1. 导入 webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager

# 假设你在这里设置了 chrome_options
chrome_options = webdriver.ChromeOptions()
# 这里可以添加你需要的各种选项，例如无头模式
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')


# 2. 使用 ChromeDriverManager().install() 来自动处理驱动
# 它会返回正确版本的驱动路径
service = Service(ChromeDriverManager().install())

# 3. 像之前一样，使用 service 和 options 来初始化浏览器
# 这一行不需要改变
driver = webdriver.Chrome(service=service, options=chrome_options)

# --- 你的其他代码 ---
# ...
# driver.get("...")
# ...
# driver.quit()

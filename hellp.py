# hellp.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# --- 核心修改在这里 ---
# 为 GitHub Actions 环境正确配置 Chrome 选项
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # 必须：以无头模式（无界面）运行
chrome_options.add_argument("--no-sandbox") # 必须：在Linux环境下运行需要的参数
chrome_options.add_argument("--disable-dev-shm-usage") # 必须：防止因资源限制而崩溃
chrome_options.add_argument("--window-size=1920,1080") # 可选：设置一个固定的窗口大小

# --- 接下来的代码保持不变 ---

# 使用 webdriver-manager 自动安装和设置驱动
service = Service(ChromeDriverManager().install())

# 使用我们刚刚配置好的 service 和 options 来初始化浏览器
driver = webdriver.Chrome(service=service, options=chrome_options)


# --- 在这里继续你的其他代码 ---
# 例如：
# print("成功初始化浏览器，开始执行任务...")
# driver.get("https://www.bilibili.com")
# print(driver.title)
# driver.quit()

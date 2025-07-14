from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def close_google_password_popup(driver, timeout=3):
    """
    Tự động đóng popup 'Google change your password' nếu xuất hiện.
    """
    try:
        # Tìm nút đóng, nút đổi mật khẩu hoặc bất cứ nút nào trên popup
        button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((
                By.XPATH, "//button[contains(., 'Change your password') or contains(., 'Đổi mật khẩu') or contains(., 'Đóng') or contains(., 'Close')]"
            ))
        )
        button.click()
    except Exception:
        # Nếu không tìm thấy popup thì bỏ qua
        pass
@echo off
REM Xóa thư mục allure-results và allure-report nếu đã tồn tại
IF EXIST reports\allure-results (
    rmdir /s /q reports\allure-results
)
IF EXIST reports\allure-report (
    rmdir /s /q reports\allure-report
)

REM Tạo lại thư mục allure-results
mkdir reports\allure-results

REM Chạy pytest sinh kết quả allure
pytest --alluredir=reports/allure-results

REM Sinh HTML report mới từ kết quả allure
allure generate reports/allure-results -o reports/allure-report --clean
start reports\allure-report\index.html
REM Thông báo hoàn thành
echo ==== ĐÃ CHẠY XONG, BÁO CÁO NẰM Ở reports\allure-report\index.html ====
pause


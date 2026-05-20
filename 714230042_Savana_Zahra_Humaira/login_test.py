import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BubbleBoothLoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Inisialisasi WebDriver
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        cls.driver = webdriver.Chrome(options=options)
        
        # Membuka halaman login
        cls.driver.get("https://bubble-booth-ten.vercel.app/login.html")
        time.sleep(3) # Tunggu loading halaman awal
        
    @classmethod
    def tearDownClass(cls):
        # Menutup WebDriver setelah semua test selesai
        cls.driver.quit()

    def test_01_cek_judul_halaman(self):
        # Memastikan berada di halaman login
        self.assertIn("Login", self.driver.title)
        
    def test_02_cek_elemen_email(self):
        # Memastikan form input email tersedia di DOM
        email_input = self.driver.find_element(By.ID, "email")
        self.assertIsNotNone(email_input)
        
    def test_03_cek_elemen_password(self):
        # Memastikan form input password tersedia di DOM
        password_input = self.driver.find_element(By.ID, "password")
        self.assertIsNotNone(password_input)
        
    def test_04_cek_tombol_login(self):
        # Memastikan tombol masuk tersedia di DOM
        submit_btn = self.driver.find_element(By.CLASS_NAME, "auth-btn")
        self.assertIsNotNone(submit_btn)

    def test_05_login_gagal_kredensial_salah(self):
        # Melakukan testing pada fitur login dengan memasukkan data salah
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")
        
        # Memasukkan input baru
        email_input.send_keys("testuser@example.com")
        password_input.send_keys("password_salah123")
        password_input.send_keys(Keys.ENTER)
        
        time.sleep(3) # Tunggu proses loading dari server
        
        # Memastikan elemen pesan error ada setelah disubmit
        error_msg = self.driver.find_element(By.ID, "errorMsg")
        self.assertIsNotNone(error_msg)


if __name__ == "__main__":
    # Menggunakan unittest untuk mendapatkan report output test
    test_runner = unittest.TextTestRunner(verbosity=1)
    test_suite = unittest.TestLoader().loadTestsFromTestCase(BubbleBoothLoginTest)
    result = test_runner.run(test_suite)
    
    # Cetak format "RINGKASAN HASIL TESTING" persis seperti yang diminta di foto
    print("\n======================================================================")
    print("RINGKASAN HASIL TESTING")
    print("======================================================================")
    print(f"Total Test : {result.testsRun}")
    print(f"Berhasil   : {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Gagal      : {len(result.failures)}")
    print(f"Error      : {len(result.errors)}")
    print("======================================================================\n")

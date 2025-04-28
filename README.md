# 📅 ระบบจองห้องประชุม (Meeting Room Booking System)

โปรเจกต์นี้เป็นเว็บไซต์สำหรับการจองห้องประชุม พัฒนาด้วย **Django Framework**
รองรับการบันทึก, แก้ไข, ค้นหา, ยกเลิกการจองห้องได้เหมาะ

---

## ฟีเจอร์หลัก

- บันทึกการจองห้อง (ชื่อผู้จอง, วันที่จอง, เวลา, ห้องที่จอง)
- แก้ไข / ยกเลิกการจอง
- ค้นหาข้อมูลการจองตามชื่อผู้จอง, ห้อง, วันที่จอง
- แสดงรายการจองในตาราง
- เพิ่มพร้อมเบียบห้องประชุม (Admin)
- กำหนดจำนวนคนที่ห้องประชุมรอรับได้

---

## วิธีการติดตั้ง (Installation)

1. คลอนโปรเจ็ก
   ```bash
   git clone https://github.com/<ชื่อ GitHub>/room-booking-system.git
   cd room-booking-system
   ```

2. สร้าง Virtual Environment และติดตั้ง package
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. เริ่มถานฐ์ฐานถานถานเบิ้มต้นภานโครงสร้างเบาะ
   ```bash
   python manage.py migrate
   ```

4. สร้าง Superuser
   ```bash
   python manage.py createsuperuser
   ```

5. รัน server
   ```bash
   python manage.py runserver
   ```

6. เข้าใช้บราวเว็บไซต์
   - [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - บริหารสำหรับ admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## เทคโนโลยีที่ใช้
- Django 4+
- SQLite3
- HTML / CSS (Bootstrap)

## หมายเหตุ
- ต้องใช้ Python 3.8+ ขึ้นไป
- ตั้ง SECRET_KEY ใน settings.py ทุกครั้ง Production

---

✨ โปรเจ็กนี้มีไฟล์สมบูรณ์ไว้สำหรับพรีเซ็นต์ และแร้งค่ามเต็มตัวอย่างเหมาะ 😊


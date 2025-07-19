### ✅ **To-Do List API üçün Task List (Django, CRUD API)**

#### 🔹 1. **Layihəyə Başlanğıc**

* [+] Virtual mühit yarat (Poetry, venv və s.)
* [+] Yeni Django layihəsi yarat: `django-admin startproject todo_project`
* [+] Yeni app yarat: `python manage.py startapp todo`
* [+] `todo` app-i `settings.py`-ə əlavə et
* [+] Gerekli `INSTALLED_APPS` konfiqurasiyası (REST framework və s.)

---

#### 🔹 2. **Model Yaratmaq**

* [+] `Todo` modeli yarat:

  * `title` – CharField
  * `description` – TextField (optional)
  * `is_completed` – BooleanField (default=False)
  * `created_at`, `updated_at` – DateTimeField (auto\_now\_add / auto\_now)
* [+] Model üçün `__str__` metodu əlavə et
* [+] Migrasiyaları yarat və tətbiq et

---

#### 🔹 3. **Serializer Yazmaq**

* [+] `TodoSerializer` yaradaraq model sahələrini serialize et

---

#### 🔹 4. **API View-ları Yaratmaq (CRUD)**

##### 1. Variant: Function-Based Views (FBV)

##### 2. Variant: Class-Based Views (CBV)

* [+] `ListCreateAPIView` – bütün tapşırıqları görüntülə / yeni tapşırıq yarat
* [+] `RetrieveUpdateDestroyAPIView` – bir tapşırığı göstər / redaktə et / sil

---

#### 🔹 5. **URL Routing**

* [+] `urls.py` yaradaraq API endpoint-ləri təyin et

  * `/api/todos/` – GET, POST
  * `/api/todos/<int:id>/` – GET, PUT, DELETE

---

#### 🔹 6. **Testlər (Optional)**

* [+] API testləri üçün `pytest` və ya `unittest` istifadə et
* [+] `GET`, `POST`, `PUT`, `DELETE` metodları üçün testlər yaz

---

#### 🔹 7. **(Optional) Authentication**

* [+] İstifadəçi modeli əlavə et (`User` ilə əlaqələndir)
* [+] Yalnız auth olan istifadəçilərin öz tapşırıqlarını görməsinə icazə ver
* [+] Token-based Auth əlavə et (DRF TokenAuth, JWT və s.)

---

#### 🔹 8. **(Optional) Filter / Search / Order**

* [+] Tapşırıqları `is_completed` və ya `title` ilə süzmək
* [ ] Axtarış: `?search=keyword`
* [ ] Sıralama: `?ordering=created_at`

---

#### 🔹 9. **(Optional) Swagger və ya ReDoc**

* [ ] `drf-yasg` və ya `drf-spectacular` ilə auto-dokumentasiya əlavə et



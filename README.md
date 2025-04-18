
# CareConnect Project

**Version:** 1.0  
**Developed Using:** Python (Django Framework) and MySQL

---

## 📦 Pre-requisites

Before executing the project, ensure you have the following software installed and configured:

1. **Python**: Version 3.8 or above  
   - [Download Python](https://www.python.org/downloads/)  
   - ✅ Add Python to PATH during installation.

2. **PyCharm IDE**  
   - [Download PyCharm](https://www.jetbrains.com/pycharm/)

3. **MySQL (Included in XAMPP)**  
   - [Download XAMPP](https://www.apachefriends.org/index.html)  
   - Use **MySQL Server on Port 3307**

4. **Required Python Libraries**  
   - Install dependencies from `requirements.txt`:  
     ```bash
     pip install -r requirements.txt
     ```

5. **Web Browser**  
   - Modern browsers like Google Chrome or Mozilla Firefox are recommended.

---

## 🚀 Step-by-Step Execution Instructions

### 1. Download and Setup the Project

- Download the project ZIP file from the provided source.
- Extract it to a preferred directory.
- Copy the `hms` folder to your desktop for easy access.

### 2. Setup MySQL Database

- Launch MySQL from XAMPP Control Panel or any MySQL client.
- Create the database using:
  ```sql
  CREATE DATABASE hmspythondb;
  ```
- Import the SQL file from the SQL File Folder using:
  ```bash
  mysql -u root -P 3307 hmspythondb < path_to_sql_file.sql
  ```
  Alternatively, use MySQL Workbench or phpMyAdmin.

### 3. Run the Project Locally

- **Open PyCharm** and load the `hms` project folder.
- Open the terminal and navigate to:
  ```bash
  cd hospital
  ```
- Set the Generative AI API key:
  ```bash
  set GENERATIVE_AI_KEY=<Your_API_key>  # Windows
  export GENERATIVE_AI_KEY=<Your_API_key>  # macOS/Linux
  ```
  *(Get API key at: https://aistudio.google.com/app/apikey)*

- Run the development server:
  ```bash
  python manage.py runserver
  ```
- Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

### 4. Set SMTP Server

- Open `docapps/settings.py`
- On lines **152, 153, and 154**, update:
  - Host
  - Default email ID
  - Your email password

---

## 🔐 Login Credentials

### Admin Panel  
- **Username:** `admin@gmail.com`  
- **Password:** `Test@123`

### Doctor Account  
- **Username:** `aaryankuntal56@gmail.com`  
- **Password:** `aaryan`

### User/Patient Account  
- **Username:** `rndas2004@gmail.com`  
- **Password:** `ritesh`

---

## 📁 Project Structure

```
hms/
├── hospital/               # Main Django App
│   ├── migrations/         # DB Migrations
│   ├── static/             # Static files (CSS, JS, Images)
│   ├── templates/          # HTML templates
│   ├── views.py            # Django Views
│   ├── models.py           # DB Models
│   └── ...
├── SQL File Folder/        # SQL dump
├── requirements.txt        # Python dependencies
└── manage.py               # Django manager
```

---

## ✨ Features

- **Admin Panel**: Manage doctors, patients, appointments, and system configurations.
- **Doctor Dashboard**: View/manage appointments and patient records.
- **User/Patient Dashboard**: Book appointments, view prescriptions, and manage personal details.

---

## 📝 Notes

- Ensure **MySQL is running on Port 3307**.
- If errors occur, verify your **DB credentials** in `settings.py`.
- Server runs by default on: [http://localhost:8000](http://localhost:8000)

---

## 🛠 Troubleshooting

### 1. Database Connection Issues
- Confirm MySQL is running and accessible on Port 3307.
- Ensure `hmspythondb` is created and populated.

### 2. Dependency Issues
- Run:
  ```bash
  pip install -r requirements.txt
  ```

### 3. Port Conflicts
- If Port 8000 is in use, run the server on a different port:
  ```bash
  python manage.py runserver 8080
  ```

---

## 👨‍💻 Author Information

For any queries or issues, feel free to reach out:  
📧 **Email**: careconnectiiita@gmail.com

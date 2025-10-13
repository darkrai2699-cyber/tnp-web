# Alumni Management Portal 🎓

Welcome to the Alumni Management Portal! This project is designed to help manage alumni information efficiently and effectively.  
This repository contains the **Alumni Management Portal**, developed as part of our college and department requirements.  

---

## 📖 Table of Contents
- [📌 Project Overview](#-project-overview)
- [✨ Features](#-features)
- [🛠️ Technology Stack](#️-technology-stack)
- [🚀 Purpose](#-purpose)
- [📚 Documentation](#-documentation)

---

## 📌 Project Overview
The Alumni Management Portal helps the college and department:
- Maintain alumni records and profiles  
- Facilitate communication between alumni and the institution  
- Provide a centralized system to manage alumni information  
- Strengthen alumni engagement and networking  

---

## ✨ Features

✅ Alumni registration & authentication (login/signup)  
✅ Manage alumni profiles  
✅ Search and filter alumni data  
✅ Generate reports and analytics  
✅ User authentication and authorization  
✅ Responsive design  
✅ Batch Mentor management  
✅ Assign batches to Batch Mentors based on graduation year  
✅ Forgot Password functionality  

---

## 🛠️ Technology Stack

### **Frontend:**
- ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
- ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
- ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
- ![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=flat&logo=bootstrap&logoColor=white)
- ![Font Awesome](https://img.shields.io/badge/Font%20Awesome-339AF0?style=flat&logo=font-awesome&logoColor=white)

### **Backend:**
- ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
- ![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)

### **Database:**
- ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)

### **Tools:**
- ![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
- ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)
- ![npm](https://img.shields.io/badge/npm-CB3837?style=flat&logo=npm&logoColor=white)
- ![Webpack](https://img.shields.io/badge/Webpack-8DD6F9?style=flat&logo=webpack&logoColor=black)

---

## 🚀 Purpose
This project was developed as part of our **Final Year College Project**, under the guidance of our department, with the aim of providing a digital solution for managing alumni data and improving alumni–institution engagement.

---

## 📚 Documentation

### Project Structure
The project is organized as follows:
```
alumni-app/
├── frontend/          # Contains frontend code (HTML, CSS, JS)
├── backend/           # Contains backend code (Django project)
├── database/          # Database scripts and migrations
├── docs/              # Additional documentation
└── README.md          # Project overview and documentation
```

### Setup Instructions
Follow these steps to set up the project locally:

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-repo/alumni-app.git
   cd alumni-app
   ```

2. **Install Dependencies**  
   - **Frontend:** Ensure `npm` is installed, then run:
     ```bash
     cd frontend
     npm install
     ```
   - **Backend:** Ensure `Python` and `pip` are installed, then run:
     ```bash
     cd backend
     pip install -r requirements.txt
     ```

3. **Set Up the Database**  
   - Create a MySQL database and update the database configuration in `backend/settings.py`.
   - Run migrations:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

4. **Run the Application**  
   - Start the backend server:
     ```bash
     python manage.py runserver
     ```
   - Open the frontend in your browser or run a local server for the frontend.

### Usage Guidelines
- **Admin Panel:** Access the admin panel at `/admin` to manage users and data.
- **Alumni Registration:** Alumni can register and log in to update their profiles.
- **Batch Management:** Assign batches to mentors via the admin panel.

---

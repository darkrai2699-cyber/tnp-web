# 🎓 Alumni Management Portal

Welcome to the **Alumni Management Portal**! This project is designed to streamline the management of alumni information, foster alumni–institution engagement, and provide a centralized platform for alumni data management.  

---

## 📖 Table of Contents
- [📌 Project Overview](#-project-overview)
- [✨ Features](#-features)
- [🛠️ Technology Stack](#️-technology-stack)
- [🚀 Purpose](#-purpose)
- [📂 Project Structure](#-project-structure)
- [⚙️ Setup Instructions](#️-setup-instructions)
- [📋 Usage Guidelines](#-usage-guidelines)
- [📞 Support](#-support)

---

## 📌 Project Overview

The **Alumni Management Portal** is a web-based application that helps colleges and universities:
- Maintain and manage alumni records and profiles.
- Facilitate communication between alumni and the institution.
- Provide tools for generating reports and analytics.
- Strengthen alumni engagement and networking opportunities.
- Assign mentors to batches for better alumni–student interaction.

This project was developed as part of our **Final Year College Project** under the guidance of our department.

---

## ✨ Features

The portal comes with the following features:
- **Alumni Registration & Authentication:** Alumni can sign up, log in, and manage their profiles.
- **Profile Management:** Alumni can update their personal and professional details.
- **Search & Filter:** Admins can search and filter alumni data based on various criteria.
- **Reports & Analytics:** Generate insightful reports to analyze alumni data.
- **Batch Mentor Management:** Assign mentors to specific batches based on graduation year.
- **Forgot Password Functionality:** Secure password recovery for users.
- **Responsive Design:** Fully optimized for desktop and mobile devices.
- **Admin Panel:** Manage users, batches, and other data through a dedicated admin interface.

---

## 🛠️ Technology Stack

The project is built using the following technologies:

### **Frontend:**
- **HTML5**: For structuring the web pages.
- **CSS3**: For styling and layout.
- **JavaScript**: For interactivity and dynamic content.
- **Bootstrap**: For responsive design and pre-built UI components.
- **Font Awesome**: For icons and visual enhancements.

### **Backend:**
- **Python**: The core programming language.
- **Django**: A high-level Python web framework for rapid development.

### **Database:**
- **MySQL**: For storing and managing alumni data.

### **Tools:**
- **Git**: For version control.
- **GitHub**: For repository hosting and collaboration.
- **npm**: For managing frontend dependencies.
- **Webpack**: For bundling frontend assets.

---

## 🚀 Purpose

The primary goal of this project is to provide a **digital solution** for managing alumni data and improving alumni–institution engagement. It aims to:
- Replace traditional, manual methods of managing alumni information.
- Enhance communication between alumni and the institution.
- Provide a platform for alumni to stay connected with their alma mater.
- Enable the institution to track alumni achievements and contributions.

---

## 📂 Project Structure

The project is organized as follows:
```
alumni-app/
├── frontend/          # Contains frontend code (HTML, CSS, JS)
├── backend/           # Contains backend code (Django project)
├── database/          # Database scripts and migrations
├── templates/         # HTML templates for the application
├── static/            # Static files (CSS, JS, images)
└── README.md          # Project overview and documentation
```

---

## ⚙️ Setup Instructions

Follow these steps to set up the project locally:

### 1. **Clone the Repository**
   Open your terminal and run:
   ```bash
   git clone https://github.com/Aniketgudgal/Alumni-Management-Portal.git
   cd alumni-app
   ```

### 2. **Install Dependencies**
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

### 3. **Set Up the Database**
   - Create a MySQL database and update the database configuration in `backend/settings.py`.
   - Run the following commands to apply migrations:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

### 4. **Run the Application**
   - Start the backend server:
     ```bash
     python manage.py runserver
     ```
   - Open the frontend in your browser or run a local server for the frontend.

---

## 📋 Usage Guidelines

- **Admin Panel:**  
  Access the admin panel at `/admin` to manage users, alumni data, and batches.
  
- **Alumni Registration:**  
  Alumni can register and log in to update their profiles and stay connected.

- **Batch Management:**  
  Assign mentors to specific batches via the admin panel.

- **Reports & Analytics:**  
  Generate reports to analyze alumni data and trends.

---

## 📞 Support

If you encounter any issues or have questions about the project, feel free to reach out:
- **Email:** aniketgudgal5867@gmail.com
- **GitHub Issues:** [Submit an issue](https://github.com/Aniketgudgal/Alumni-Management-Portal/issues)

We welcome contributions and feedback to improve the project further!

---

**Proudly developed by the Alumni Management Portal Team with dedication and passion.**

# HealthHub

## Overview
HealthHub is a comprehensive full-stack healthcare application designed to empower users in managing their health by allowing them to input symptoms for accurate disease prediction. The system uses machine learning to match patients with specialist doctors related to the diagnosed condition and suggests hospitals specializing in the identified disease. The platform integrates appointment booking functionality for streamlined access to healthcare providers.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
- [Screenshots](#screenshots)
- [Contributors](#contributors)
- [License](#license)

## Features
- **Symptom Input and Disease Prediction:** Users can input symptoms and receive accurate disease predictions.
- **Doctor Matching:** Matches patients with specialist doctors based on the diagnosed condition.
- **Hospital Suggestions:** Recommends hospitals that specialize in the identified disease.
- **Appointment Booking:** Facilitates scheduling consultations with available specialists.
- **AI Chatbot:** Provides instant assistance to users.
- **Admin Module:** Manages doctor details, patient check-ins, and customer queries.
- **Doctor Module:** Allows doctors to manage their availability and consult history.
- **Patient Module:** Enables patients to manage their health records, book appointments, and interact with the AI chatbot.

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript, Bootstrap, JQuery, AJAX
- **Backend:** Django
- **Database:** Oracle DB
- **Machine Learning:** Various predictive algorithms

## Installation
1. **Clone the repository:**
    ```sh
    git clone https://github.com/saiaswath07/HealthHub.git
    ```
2. **Navigate to the project directory:**
    ```sh
    cd HealthHub
    ```
3. **Set up the virtual environment:**
    ```sh
    python -m venv env
    source env/bin/activate (Linux/Mac)
    .\env\Scripts\activate (Windows)
    ```
4. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
5. **Set up the database:**
    Configure your Oracle DB settings in the Django settings file and run:
    ```sh
    python manage.py migrate
    ```
6. **Run the server:**
    ```sh
    python manage.py runserver
    ```

## Usage
1. **Navigate to the login page:**
    Open your web browser and go to `http://localhost:8000/login/`
2. **Login as a patient, doctor, or admin.**
3. **Explore the functionalities:** 
    - Patients can input symptoms, book appointments, and chat with the AI bot.
    - Doctors can manage their schedule and view consultation history.
    - Admins can manage doctors and handle customer queries.

## Modules
- **Home Page:** Central hub for navigation.
- **Contact Us:** Form for user inquiries.
- **About Us:** Information about the application.
- **Admin Module:** Manage doctor details, patient check-ins, and customer queries.
- **Doctor Module:** Manage availability, consultation history, and medicine checks.
- **Patient Module:** Symptom input, disease prediction, appointment booking, and AI chatbot.

## Screenshots
### Home Page
![Home Page](/outputs/home.jpeg)

### Patient Page
![Patient Page](screenshots/patient.png)

### Doctor Page
![Doctor Page](screenshots/doctor.png)

### Admin Page
![Admin Page](screenshots/admin.png)

## Contributors
- **P Nandieswar Reddy** - BL.EN. U4AIE20046
- **Rithvika Alapati** - BL.EN. U4AIE20054
- **Sai Aswath S** - BL.EN. U4AIE20056
- **Guided by Dr. Radha D**

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# AWS Bus Booking Application

## Project Overview

The AWS Bus Booking Application is a web-based bus reservation system developed using Python and Flask.

The application allows users to view available buses, select seats, enter passenger details, confirm bookings, and view booking history.

The project demonstrates the development of a simple web application with a Flask backend, HTML templates, CSS styling, and basic booking management.

---

## Objective

The main objective of this project is to develop a simple and user-friendly bus booking application that demonstrates:

- Web application development using Flask
- Bus search and listing
- Seat selection
- Passenger registration
- User login
- Bus ticket booking
- Booking confirmation
- Booking history
- Duplicate seat prevention
- Application health monitoring

---

## Features

### 1. User Registration

Users can register by providing:

- Full Name
- Email
- Phone Number
- Password

### 2. User Login

Users can enter their:

- Email
- Password

### 3. Available Buses

The application displays available buses with:

- Bus Name
- Bus Number
- Source
- Destination
- Departure Time
- Ticket Price
- Total Seats
- Available Seats

### 4. Bus Search

Users can search buses using:

- Source
- Destination
- Bus Name
- Bus Number

### 5. Seat Selection

Users can select an available seat from the bus seat layout.

The application also prevents users from selecting an already booked seat.

### 6. Passenger Booking

Users enter:

- Passenger Name
- Email
- Phone Number

The selected bus and seat are displayed before confirming the booking.

### 7. Booking Confirmation

After successful booking, the application displays:

- Booking Status
- Passenger Name
- Email
- Phone Number
- Bus Number
- Seat Number

### 8. Booking History

Users can view previously created bookings.

### 9. Health Check

The application provides a health-check endpoint:

```text
/health
```

Example response:

```json
{
    "application": "Bus Booking Application",
    "status": "healthy"
}
```

---

## Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Jinja2 Templates
- Git
- GitHub

---

## Project Structure

```text
AWS-Bus-Booking-Application/
│
├── app.py
│
├── database/
│   └── schema.sql
│
├── static/
│   └── style.css
│
├── templates/
│   ├── booking.html
│   ├── booking_history.html
│   ├── buses.html
│   ├── confirmation.html
│   ├── login.html
│   ├── register.html
│   └── seats.html
│
├── .gitignore
└── README.md
```

---

## Application Workflow

```text
Home Page
    ↓
User Registration / Login
    ↓
Available Buses
    ↓
Search Bus
    ↓
Select Seat
    ↓
Enter Passenger Details
    ↓
Confirm Booking
    ↓
Booking Confirmation
    ↓
Booking History
```

---

## How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/saanchipadekar-eng/AWS-Bus-Booking-Application.git
```

### Step 2: Open the Project Folder

```bash
cd AWS-Bus-Booking-Application
```

### Step 3: Install Flask

```bash
pip install flask
```

### Step 4: Run the Application

```bash
python app.py
```

### Step 5: Open the Application

Open the following URL in a browser:

```text
http://127.0.0.1:5000
```

---

## Main Application URLs

| Page | URL |
|---|---|
| Home | `/` |
| Registration | `/register` |
| Login | `/login` |
| Available Buses | `/buses` |
| Seat Selection | `/seats` |
| Booking | `/booking` |
| Booking History | `/booking-history` |
| Health Check | `/health` |

---

## Booking Example

Example booking:

```text
Passenger Name: Saanchi
Email: saanchi@example.com
Phone: 9876543210
Bus Number: MH12AB1234
Seat Number: Seat 7
Booking Status: Confirmed
```

---

## Duplicate Seat Prevention

The application checks whether a selected seat has already been booked.

If a user tries to book the same seat again, the application displays an error message and asks the user to select another seat.

---

## Health Monitoring

The `/health` endpoint can be used to verify that the Flask application is running correctly.

Example:

```text
http://127.0.0.1:5000/health
```

Response:

```json
{
    "application": "Bus Booking Application",
    "status": "healthy"
}
```

---

## Current Storage

The current version uses temporary in-memory storage for booking information.

This is suitable for demonstrating the application workflow.

The project can be enhanced in the future by connecting the application to a permanent database.

---

## Future Enhancements

Future versions can include:

- MySQL or Amazon RDS database
- Secure password hashing
- User authentication and sessions
- Admin dashboard
- Payment gateway integration
- Email booking confirmation
- Booking cancellation
- Travel date selection
- Cloud deployment using AWS
- Amazon EC2 deployment
- Amazon RDS integration
- Amazon S3 integration
- Application monitoring using Amazon CloudWatch

---

## Learning Outcomes

Through this project, I learned:

- How to develop a Flask web application
- How Flask routes work
- How to use HTML templates with Jinja2
- How to create forms
- How to process form data
- How to implement seat selection
- How to prevent duplicate seat booking
- How to maintain booking history
- How to create a health-check endpoint
- How to organize a web application
- How to use Git and GitHub for version control

---

## Author

**Saanchi Narendra Padekar**

BCA Graduate | Aspiring Data Analyst & Business Analyst

GitHub:

https://github.com/saanchipadekar-eng
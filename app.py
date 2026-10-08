from flask import Flask, render_template, request

app = Flask(__name__)

# Temporary storage
booked_seats = {}
booking_history = []


# -------------------------------------------------
# Home
# -------------------------------------------------

@app.route("/")
def home():
    return """
    <h1>Bus Booking Application</h1>
    <p>Welcome to our AWS Bus Booking Application.</p>
    <p>Flask backend is working successfully!</p>

    <p><a href="/register">Register New User</a></p>
    <p><a href="/login">User Login</a></p>
    <p><a href="/buses">View Available Buses</a></p>
    <p><a href="/booking-history">View Booking History</a></p>
    <p><a href="/health">Health Check</a></p>
    """


# -------------------------------------------------
# Health Check
# -------------------------------------------------

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": "Bus Booking Application"
    }


# -------------------------------------------------
# Register
# -------------------------------------------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")

        return f"""
        <h1>Registration Received</h1>

        <p>Name: {name}</p>
        <p>Email: {email}</p>
        <p>Phone: {phone}</p>

        <p>Registration form is working successfully.</p>

        <p>
            <a href="/register">Back to Registration</a>
        </p>
        """

    return render_template("register.html")


# -------------------------------------------------
# Login
# -------------------------------------------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        return f"""
        <h1>Login Received</h1>

        <p>Email: {email}</p>

        <p>Login form is working successfully.</p>

        <p>
            <a href="/login">Back to Login</a>
        </p>
        """

    return render_template("login.html")


# -------------------------------------------------
# Available Buses
# -------------------------------------------------

@app.route("/buses")
def buses():

    search = request.args.get("search", "").strip().lower()

    bus_list = [
        {
            "name": "City Express",
            "number": "MH12AB1234",
            "source": "Pune",
            "destination": "Mumbai",
            "departure": "08:00 AM",
            "price": 500,
            "total_seats": 40,
            "available_seats": 32
        },
        {
            "name": "Shivneri Travels",
            "number": "MH14CD5678",
            "source": "Mumbai",
            "destination": "Pune",
            "departure": "10:30 AM",
            "price": 450,
            "total_seats": 40,
            "available_seats": 28
        },
        {
            "name": "Deccan Travels",
            "number": "MH15EF9012",
            "source": "Pune",
            "destination": "Nashik",
            "departure": "02:00 PM",
            "price": 600,
            "total_seats": 40,
            "available_seats": 35
        }
    ]

    if search:

        bus_list = [
            bus for bus in bus_list
            if search in bus["source"].lower()
            or search in bus["destination"].lower()
            or search in bus["name"].lower()
            or search in bus["number"].lower()
        ]

    return render_template(
        "buses.html",
        buses=bus_list,
        search=search
    )


# -------------------------------------------------
# Seat Selection
# -------------------------------------------------

@app.route("/seats")
def seats():

    bus_number = request.args.get("bus_number")

    bus_list = [
        {
            "name": "City Express",
            "number": "MH12AB1234",
            "source": "Pune",
            "destination": "Mumbai",
            "departure": "08:00 AM",
            "price": 500,
            "total_seats": 40,
            "available_seats": 32
        },
        {
            "name": "Shivneri Travels",
            "number": "MH14CD5678",
            "source": "Mumbai",
            "destination": "Pune",
            "departure": "10:30 AM",
            "price": 450,
            "total_seats": 40,
            "available_seats": 28
        },
        {
            "name": "Deccan Travels",
            "number": "MH15EF9012",
            "source": "Pune",
            "destination": "Nashik",
            "departure": "02:00 PM",
            "price": 600,
            "total_seats": 40,
            "available_seats": 35
        }
    ]

    bus = next(
        (bus for bus in bus_list if bus["number"] == bus_number),
        None
    )

    if bus is None:
        return "Bus not found", 404

    occupied_seats = booked_seats.get(
        bus_number,
        []
    )

    return render_template(
        "seats.html",
        bus=bus,
        occupied_seats=occupied_seats
    )


# -------------------------------------------------
# Booking
# -------------------------------------------------

@app.route("/booking", methods=["GET", "POST"])
def booking():

    if request.method == "POST":

        bus_number = request.form.get("bus_number")
        seat_number = request.form.get("seat_number")

        passenger_name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")

        # Check passenger details
        if not passenger_name or not email or not phone:
            return """
            <h1>Booking Error</h1>

            <p>Please fill in all passenger details.</p>

            <p>
                <a href="javascript:history.back()">
                    Go Back
                </a>
            </p>
            """

        # Check if seat is already booked
        current_booked_seats = booked_seats.get(
            bus_number,
            []
        )

        if seat_number in current_booked_seats:

            return f"""
            <h1>Booking Error</h1>

            <p>
                Seat {seat_number} is already booked.
            </p>

            <p>
                Please select another seat.
            </p>

            <p>
                <a href="/seats?bus_number={bus_number}">
                    Back to Seat Selection
                </a>
            </p>
            """

        # Create bus entry if needed
        if bus_number not in booked_seats:
            booked_seats[bus_number] = []

        # Save booked seat
        booked_seats[bus_number].append(
            seat_number
        )

        # Save booking history
        booking_history.append({
            "passenger_name": passenger_name,
            "email": email,
            "phone": phone,
            "bus_number": bus_number,
            "seat_number": seat_number,
            "status": "Confirmed"
        })

        # Show professional confirmation page
        return render_template(
            "confirmation.html",
            passenger_name=passenger_name,
            email=email,
            phone=phone,
            bus_number=bus_number,
            seat_number=seat_number,
            status="Confirmed"
        )

    # GET request

    bus_number = request.args.get("bus_number")
    seat_number = request.args.get("seat_number")

    bus_list = [
        {
            "name": "City Express",
            "number": "MH12AB1234",
            "source": "Pune",
            "destination": "Mumbai",
            "departure": "08:00 AM",
            "price": 500,
            "total_seats": 40,
            "available_seats": 32
        },
        {
            "name": "Shivneri Travels",
            "number": "MH14CD5678",
            "source": "Mumbai",
            "destination": "Pune",
            "departure": "10:30 AM",
            "price": 450,
            "total_seats": 40,
            "available_seats": 28
        },
        {
            "name": "Deccan Travels",
            "number": "MH15EF9012",
            "source": "Pune",
            "destination": "Nashik",
            "departure": "02:00 PM",
            "price": 600,
            "total_seats": 40,
            "available_seats": 35
        }
    ]

    bus = next(
        (bus for bus in bus_list if bus["number"] == bus_number),
        None
    )

    if bus is None:
        return "Bus not found", 404

    if seat_number is None:
        return "Seat number is missing", 400

    current_booked_seats = booked_seats.get(
        bus_number,
        []
    )

    if seat_number in current_booked_seats:

        return f"""
        <h1>Seat Already Booked</h1>

        <p>
            Seat {seat_number} is already booked.
        </p>

        <p>
            <a href="/seats?bus_number={bus_number}">
                Back to Seat Selection
            </a>
        </p>
        """

    return render_template(
        "booking.html",
        bus=bus,
        selected_seat=seat_number
    )


# -------------------------------------------------
# Booking History
# -------------------------------------------------

@app.route("/booking-history")
def booking_history_page():

    return render_template(
        "booking_history.html",
        bookings=booking_history
    )


# -------------------------------------------------
# Run Flask
# -------------------------------------------------

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

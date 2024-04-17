CREATE DATABASE LittleLemon;

USE LittleLemon;

CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerName VARCHAR(255),
    BookingDate DATE,
    NumberOfGuests INT
);

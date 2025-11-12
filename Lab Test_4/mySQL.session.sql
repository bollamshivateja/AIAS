-- Hospital Billing Database (MySQL)
-- File: mySQL.session.sql

-- Clean up if re-running
DROP TABLE IF EXISTS Bills;
DROP TABLE IF EXISTS Services;
DROP TABLE IF EXISTS Patients;

-- Patients table
CREATE TABLE Patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    date_of_birth DATE,
    gender CHAR(1),
    phone VARCHAR(25),
    email VARCHAR(100),
    address VARCHAR(255)
);

-- Services table
CREATE TABLE Services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    price DECIMAL(10,2) NOT NULL
);

-- Bills table (each row is a line-item; invoice_no groups items into one bill)
CREATE TABLE Bills (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    invoice_no VARCHAR(50) NOT NULL,
    patient_id INT NOT NULL,
    service_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    bill_date DATE NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE RESTRICT
);

-- Insert sample Patients
INSERT INTO Patients (full_name, date_of_birth, gender, phone, email, address) VALUES
('Alice Johnson', '1985-04-12', 'F', '555-0101', 'alice@example.com', '123 Maple St'),
('Bob Smith',     '1978-11-02', 'M', '555-0202', 'bob@example.com',   '456 Oak Ave'),
('Carlos Reyes',  '1990-07-23', 'M', '555-0303', 'carlos@example.com','789 Pine Rd'),
('Diana Lee',     '2000-01-15', 'F', '555-0404', 'diana@example.com', '321 Elm St');

-- Insert sample Services
INSERT INTO Services (service_name, description, price) VALUES
('Consultation', 'Doctor consultation (30 min)', 50.00),
('X-Ray',        'Chest x-ray',                120.00),
('Blood Test',   'CBC and metabolic panel',     75.00),
('MRI',          'Magnetic Resonance Imaging', 800.00),
('Medication',   'Prescription drugs (per item)', 30.00),
('Physiotherapy','Physical therapy session',    65.00);

-- Insert sample Bills (invoice_no groups items belonging to same invoice)
-- Invoice INV-1001 for Alice Johnson (patient_id = 1)
INSERT INTO Bills (invoice_no, patient_id, service_id, quantity, bill_date) VALUES
('INV-1001', 1, 1, 1, '2025-10-01'), -- Consultation
('INV-1001', 1, 3, 1, '2025-10-01'), -- Blood Test
('INV-1001', 1, 5, 2, '2025-10-01'); -- Medication x2

-- Invoice INV-1002 for Bob Smith (patient_id = 2)
INSERT INTO Bills (invoice_no, patient_id, service_id, quantity, bill_date) VALUES
('INV-1002', 2, 1, 1, '2025-10-02'),
('INV-1002', 2, 2, 1, '2025-10-02'),
('INV-1002', 2, 5, 1, '2025-10-02');

-- Invoice INV-1003 for Carlos Reyes (patient_id = 3)
INSERT INTO Bills (invoice_no, patient_id, service_id, quantity, bill_date) VALUES
('INV-1003', 3, 4, 1, '2025-10-03'), -- MRI
('INV-1003', 3, 5, 1, '2025-10-03');

-- Invoice INV-1004 for Diana Lee (patient_id = 4)
INSERT INTO Bills (invoice_no, patient_id, service_id, quantity, bill_date) VALUES
('INV-1004', 4, 1, 1, '2025-10-04'),
('INV-1004', 4, 6, 3, '2025-10-04'); -- 3 physio sessions

-- Query 1: Total bill amount for each patient (aggregated across all their invoices)
SELECT
    p.patient_id,
    p.full_name,
    p.phone,
    COALESCE(SUM(s.price * b.quantity), 0) AS total_amount
FROM Patients p
LEFT JOIN Bills b ON p.patient_id = b.patient_id
LEFT JOIN Services s ON b.service_id = s.service_id
GROUP BY p.patient_id, p.full_name, p.phone
ORDER BY total_amount DESC;

-- Query 2: Total amount per invoice (invoice breakdown)
SELECT
    b.invoice_no,
    b.patient_id,
    p.full_name,
    b.bill_date,
    SUM(s.price * b.quantity) AS invoice_total
FROM Bills b
JOIN Patients p ON b.patient_id = p.patient_id
JOIN Services s ON b.service_id = s.service_id
GROUP BY b.invoice_no, b.patient_id, p.full_name, b.bill_date
ORDER BY b.bill_date, b.invoice_no;

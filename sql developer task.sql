-- Create Database and Use It
CREATE DATABASE IF NOT EXISTS StudentManagement;
USE StudentManagement;

-- Create Students Table
CREATE TABLE IF NOT EXISTS Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50),
    Gender VARCHAR(1),
    Age INT,
    Grade VARCHAR(10),
    MathScore INT,
    ScienceScore INT,
    EnglishScore INT
);

-- Insert Sample Records
INSERT INTO Students (Name, Gender, Age, Grade, MathScore, ScienceScore, EnglishScore) VALUES
('Ayush Patil', 'M', 16, 'A', 88, 75, 80),
('Riya Shah', 'F', 17, 'B', 72, 65, 78),
('Shreya Vadanagekar', 'F', 16, 'A', 85, 90, 92),
('Avinash Nikam', 'M', 17, 'C', 60, 55, 58),
('Saurabh Nikam', 'M', 18, 'B', 75, 70, 74),
('Pooja Mishra', 'F', 17, 'A', 90, 92, 89),
('Kshitij Pawar', 'M', 16, 'B', 82, 78, 80),
('Meera Nair', 'F', 16, 'A', 95, 91, 93),
('Subodh Salvi', 'M', 17, 'C', 58, 60, 62),
('Sneha Roy', 'F', 18, 'B', 77, 84, 81);

-- Task Queries
-- 1. View all students
SELECT * FROM Students;

-- 2. Average subject scores
SELECT 
    AVG(MathScore) AS AvgMath,
    AVG(ScienceScore) AS AvgScience,
    AVG(EnglishScore) AS AvgEnglish
FROM Students;

-- 3. Top performer
SELECT 
    Name, 
    (MathScore + ScienceScore + EnglishScore) AS TotalScore
FROM Students
ORDER BY TotalScore DESC
LIMIT 1;

-- 4. Grade distribution
SELECT Grade, COUNT(*) AS StudentCount
FROM Students
GROUP BY Grade;

-- 5. Average scores by gender
SELECT Gender,
    AVG(MathScore) AS AvgMath,
    AVG(ScienceScore) AS AvgScience,
    AVG(EnglishScore) AS AvgEnglish
FROM Students
GROUP BY Gender;

-- 6. High Math scorers
SELECT * FROM Students
WHERE MathScore > 80;

-- 7. Update grade (example: ID = 4)
UPDATE Students
SET Grade = 'B'
WHERE StudentID = 4;

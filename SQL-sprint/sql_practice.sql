CREATE DATABASE Tutetubedb;
USE Tutetubedb;

CREATE TABLE Employees (
    Employee_ID INT PRIMARY KEY,
    Firstname VARCHAR(50),
    Lastname VARCHAR(50),
    Department VARCHAR(50),
    Salary Decimal(10,2),
    HireDate Date
    )

SELECT * FROM Employees;

INSERT INTO Employees(Employee_ID,Firstname,Lastname,Department,Salary,HireDate)
values(101,'Raksha','Ashtankar','Engineering',32000,'2025-06-23');

INSERT INTO Employees
(Employee_ID, Firstname, Lastname, Department, Salary, HireDate)
VALUES
(102, 'Ansh', 'Dwivedi', 'Engineering', 90000.00, '2024-03-15'),
(103, 'Priya', 'Patil', 'Finance', 38000.00, '2023-08-10'),
(104, 'Amit', 'Verma', 'HR', 35000.00, '2024-01-20'),
(105, 'Sneha', 'Joshi', 'Marketing', 42000.00, '2022-11-05'),
(106, 'Rohan', 'Mehta', 'Engineering', 55000.00, '2021-07-12');

Update Employees
set Salary = 90000
where Employee_ID = 101;

Delete from Employees
WHERE Employee_ID = 106;

ALTER TABLE Employees
Add Email VARCHAR(100);

ALTER TABLE Employees
MODIFY Salary Decimal(20,2);

UPDATE Employees
Set Email = 'raksha22ashtankar@gmail.com'
Where Employee_ID = 101;

ALTER TABLE Employees
rename column Email to Email_Address;

ALTER TABLE Employees
drop column Email_Address;

Rename TABLE Employees TO Employee;
Rename Table Employee TO Employees;

SHOW CREATE TABLE Employees;

ALTER TABLE Employees
modify FirstName VARCHAR(50) NOT NULL;

ALTER TABLE Employees
ADD CONSTRAINT un_Lastname UNIQUE(Lastname);

ALTER TABLE Employees
ADD constraint check_salary CHECK(Salary>500);

ALTER TABLE Employees
DROP CHECK check_salary;

Select distinct Department from Employees;

Select Employee_ID, concat(Firstname,' ',Lastname) as Full_Name, DATEDIFF(CURRENT_DATE(), HireDate) AS DaysWorked from Employees;

Select Employee_ID, concat(Firstname,' ',Lastname) as Full_Name, (CURRENT_DATE() - HireDate) AS 'Joining date' from Employees;

CREATE TABLE Department (
     DepartmentID int PRIMARY KEY,
     EmpID int,
     DepartmentName VARCHAR(100) NOT NULL,
     CONSTRAINT fk_empid foreign key(EmpID) references Employees(Employee_ID)
     )

Select * from Department;

Delete from Department
where DepartmentID = 3;

INSERT INTO Department
(DepartmentID, EmpID, DepartmentName)
VALUES
(1, 101, 'Engineering'),
(2, 102, 'Engineering'),
(3, 106, 'Engineering'),
(4, 103, 'Finance'),
(5, 104, 'HR'),
(6, 105, 'Marketing');

CREATE TABLE Projects (
     ProjectID int PRIMARY KEY,
     ProjectName VARCHAR(100) NOT NULL,
     Budget Decimal(12,2),
     StartDate date,
     EndDate date
     )

SELECT * FROM Projects;

INSERT INTO Projects
(ProjectID, ProjectName, Budget, StartDate, EndDate)
VALUES
(201, 'Data Migration', 150000.00, '2024-01-15', '2024-06-30'),
(202, 'Cloud Analytics', 250000.00, '2024-03-01', '2024-12-15'),
(203, 'HR Management System', 100000.00, '2024-05-10', '2024-10-31'),
(204, 'Customer Data Platform', 300000.00, '2024-07-01', '2025-03-31'),
(205, 'AI Forecasting', 450000.00, '2025-01-15', '2025-09-30'),
(206, 'ETL Pipeline Automation', 200000.00, '2025-02-01', '2025-08-31');


SELECT * FROM Employees;

Select count(*) from Employees;

Select Avg(Salary) from Employees;

Select Department, Avg(Salary) as Avg_salary from Employees
group by Department
having Department = 'HR';

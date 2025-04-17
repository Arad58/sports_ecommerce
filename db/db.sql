CREATE DATABASE appdb;

USE appdb;

CREATE TABLE Users (
                       UserID INT AUTO_INCREMENT PRIMARY KEY,
                       Username VARCHAR(50) NOT NULL,
                       Email VARCHAR(100) NOT NULL UNIQUE,
                       Password VARCHAR(255) NOT NULL,
                       Role VARCHAR(50) NOT NULL
);

CREATE TABLE Categories (
                            CategoryID INT AUTO_INCREMENT PRIMARY KEY,
                            CategoryName VARCHAR(100) NOT NULL
);

CREATE TABLE Products (
                          ProductID INT AUTO_INCREMENT PRIMARY KEY,
                          Name VARCHAR(100) NOT NULL,
                          Description TEXT,
                          Price DECIMAL(10, 2) NOT NULL,
                          StockQuantity INT NOT NULL,
                          CategoryID INT,
                          FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);

CREATE TABLE Orders (
                        OrderID INT AUTO_INCREMENT PRIMARY KEY,
                        UserID INT,
                        ProductID INT,
                        OrderDate DATETIME DEFAULT CURRENT_TIMESTAMP,
                        Quantity INT NOT NULL,
                        TotalAmount DECIMAL(10, 2) NOT NULL,
                        FOREIGN KEY (UserID) REFERENCES Users(UserID),
                        FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
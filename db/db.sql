-- Create the database
CREATE DATABASE bravoappdb;

-- Use the database
USE bravoappdb;

-- Create the Users table
CREATE TABLE Users (
                       UserID INT AUTO_INCREMENT PRIMARY KEY,
                       Username VARCHAR(50) NOT NULL,
                       Email VARCHAR(100) NOT NULL UNIQUE,
                       Password VARCHAR(255) NOT NULL,
                       Role VARCHAR(50) NOT NULL
);

-- Create the Categories table
CREATE TABLE Categories (
                            CategoryID INT AUTO_INCREMENT PRIMARY KEY,
                            CategoryName VARCHAR(100) NOT NULL
);

-- Create the Products table
CREATE TABLE Products (
                          ProductID INT AUTO_INCREMENT PRIMARY KEY,
                          Name VARCHAR(100) NOT NULL,
                          Description TEXT,
                          Price DECIMAL(10, 2) NOT NULL,
                          StockQuantity INT NOT NULL,
                          CategoryID INT,
                          ImageURL TEXT NOT NULL,
                          FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);

-- Create the Cart table
CREATE TABLE Cart (
                      CartID INT AUTO_INCREMENT PRIMARY KEY,
                      UserID INT,
                      ProductID INT,
                      Quantity INT NOT NULL,
                      FOREIGN KEY (UserID) REFERENCES Users(UserID),
                      FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Create the Orders table
CREATE TABLE Orders (
                        OrderID INT AUTO_INCREMENT PRIMARY KEY,
                        UserID INT,
                        ProductID INT,
                        OrderDate DATETIME DEFAULT CURRENT_TIMESTAMP,
                        Quantity INT NOT NULL,
                        Status VARCHAR(50) DEFAULT 'Pending',
                        FOREIGN KEY (UserID) REFERENCES Users(UserID),
                        FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
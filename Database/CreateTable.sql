create database py_ql

create table Access
(
	AccessID varchar(8) primary key,
	AccesssName nvarchar(25),
	AccesssDescription nvarchar(30)
)

create table Customer
(
	CustomerID varchar(8) primary key,
	CustomerName nvarchar(50),
	CustomerAddress nvarchar(12),
	Phone varchar(12),
	Gender nvarchar(5),
	Point int,
	deleteStatus int
)

create table Account
(
	AccountID varchar(8) primary key,
	Username varchar(12),
	Password varchar(15),
	AccessID varchar(8),
	CustomerID varchar(8),
	foreign key (AccessID) references Access(AccessID),
	foreign key (CustomerID) references Customer(CustomerID),
	deleteStatus int
)

create table CustomerOrder
(
	OrderID varchar(8) primary key,
	CustomerID varchar(8),
	OrderDate date,
	OrderAddress nvarchar(100),
	Phone varchar(10),
	TotalPrice float, 
	OrderStatus nvarchar(10),
	foreign key (CustomerID) references Customer(CustomerID)
)

create table OrderDetail
(
	OrderID varchar(8),
	ProductID varchar(8),
	Quantity int, 
    Price float, 
	SizeNumber int,
	primary key (OrderID,  ProductID),
	foreign key (OrderID) references CustomerOrder(OrderID),
	foreign key (ProductID) references Product(ProductID)
)

create table Supplier
(
	SupplierID varchar(8) primary key,
	SupplierName nvarchar(50),
	SupplierAddress nvarchar(20),
	Phone varchar(12),
	Email varchar(50)
)
create table Category
(
	CategoryID varchar(8) primary key,
	CategoryName nvarchar(50),
)

create table Product
(
	ProductID varchar(8) primary key,
	ProductName nvarchar(50),
	Price float, 
	Quantity int, 
	SupplierID varchar(8),
	CategoryID varchar(8),
	foreign key (CategoryID) references Category(CategoryID),
	foreign key (SupplierID) references Supplier(SupplierID),
	deleteStatus int
)

create table Size
(
	SizeNumber int primary key,
)

create table Product_Size
(
	ProductID varchar(8),
	SizeNumber int,
	Quantity int,
	primary key (ProductID,  SizeNumber),
	foreign key (ProductID) references Product(ProductID),
	foreign key (SizeNumber) references Size(SizeNumber)
)

Create table Cart
(
	AccountID varchar(8) NOT NULL foreign key (AccountID) references Account(AccountID),
	ProductID varchar(8) NOT NULL foreign key (ProductID) references Product(ProductID),
	SizeNumber int NOT NULL foreign key (SizeNumber) references Size(SizeNumber),
	Quantity int,
	Primary key(AccountID, ProductID)
)
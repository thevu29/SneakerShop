create database py_ql
use py_ql

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
	Point int
)

create table Account
(
	AccountID varchar(8) primary key,
	Username varchar(12),
	Password varchar(15),
	AccessID varchar(8),
	CustomerID varchar(8),
	foreign key (AccessID) references Access(AccessID),
	foreign key (CustomerID) references Customer(CustomerID)
)

create table CustomerOrder
(
	OrderID varchar(8) primary key,
	CustomerID varchar(8),
	OrderDate date, 
	TotalPrice float, 
	OrderStatus nvarchar(10),
	foreign key (CustomerID) references Customer(CustomerID)
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
	Price money, 
	Quantity int, 
	SupplierID varchar(8),
	CategoryID varchar(8),
	ImageLink varchar(50),
	foreign key (CategoryID) references Category(CategoryID),
	foreign key (SupplierID) references Supplier(SupplierID)
)

create table OrderDetail
(
	OrderID varchar(8),
	ProductID varchar(8),
	Quantity int, 
    Price float, 
	primary key (OrderID,  ProductID),
	foreign key (OrderID) references CustomerOrder(OrderID),
	foreign key (ProductID) references Product(ProductID)
)

INSERT INTO Access VALUES
('ACS001', 'Admin', N'Người quản trị'),
('ACS002', 'User', N'Người dùng')

INSERT INTO Customer VALUES
('CUS001', N'Nguyễn Thế Vũ', N'Hồ Chí Minh', '0123456789', 'Nam', 0),
('CUS002', N'Vương Huy Hoàng', N'Hà Nội', '0123456789', N'Nữ', 5),
('CUS003', N'Nguyễn Hoàng Hải Nam', N'Đồng Nai', '0123456789', N'Nữ', 15),
('CUS004', N'Trần Kim Phú', N'Quảng Bình ', '0123456789', N'Nam', 100),
('CUS005', N'Đào Đức Thắng', N'Hồ Chí Minh', '0123456789', N'Nam', 20)

INSERT INTO Account VALUES
('ACC001', 'admin', 'admin', 'ACS001', 'CUS000'),
('ACC002', 'thevu', '123', 'ACS002', 'CUS001'),
('ACC003', 'huyhoang', '123', 'ACS002', 'CUS002'),
('ACC004', 'kimphu', '123', 'ACS002', 'CUS004'),
('ACC005', 'hainam', '123', 'ACS002', 'CUS003'),
('ACC006', 'ducthang', '123', 'ACS002', 'CUS005')

INSERT INTO CustomerOrder VALUES
('HD001', 'CUS001', '2023-1-1', 2000000, N'Đã xử lí'),
('HD002', 'CUS002', '2023-1-2', 2000000, N'Chưa xử lí'),
('HD003', 'CUS003', '2023-1-3', 2000000, N'Đã xử lí'),
('HD004', 'CUS004', '2023-1-4', 2000000, N'Đã xử lí'),
('HD005', 'CUS005', '2023-1-5', 2000000, N'Chưa xử lí')

INSERT INTO Supplier VALUES
('SPL001', 'NIKE', N'Hồ Chí Minh', '0123456789', 'nike@gmail.com'),
('SPL002', 'ADDIDAS', N'Hà Nội', '0123456789', 'addidas@gmail.com'),
('SPL003', 'BALENCIAGA', N'Đà Nẵng', '0123456789', 'balenciaga@gmail.com'),
('SPL004', 'GUCCI', N'Nha Trang', '0123456789', 'gucci@gmail.com'),
('SPL005', 'Vans', N'Hồ Chí Minh', '0123456789', 'vans@gmail.com'),
('SPL006', 'Converse', N'Hà Nội', '0123456789', 'converse@gmail.com'),
('SPL007', 'Jordan', N'Đà Nẵng', '0123456789', 'jordan@gmail.com')

INSERT INTO Category VALUES
('CAT001', 'Nike'),
('CAT002', 'Addidas'),
('CAT003', 'Balenciaga'),
('CAT004', 'Gucci'),
('CAT005', 'Vans'),
('CAT006', 'Converse'),
('CAT007', 'Jordan')

INSERT INTO Product VALUES
('SP001', 'Vans Vault', 1100000, 50, 'SPL005', 'CAT005', 'link1'),
('SP002', 'Converse Chuck', 1200000, 50, 'SPL006', 'CAT006', 'link2'),
('SP003', 'Air Jordan 1 Retro', 1300000, 50, 'SPL007', 'CAT007', 'link3'),
('SP004', 'Nike Air Force 1', 1400000, 50, 'SPL001', 'CAT001', 'link4'),
('SP005', 'Ultra Addidas 4D', 1500000, 50, 'SPL002', 'CAT002', 'link5'),
('SP006', 'Nike Air Max', 1600000, 50, 'SPL001', 'CAT001', 'link6'),
('SP007', 'Balenciaga Stan Smith', 1700000, 50, 'SPL003', 'CAT003', 'link7'),
('SP008', 'Balenciaga Stan Smith', 1700000, 50, 'SPL003', 'CAT003', 'link7'),
('SP009', 'Balenciaga Stan Smith', 1700000, 50, 'SPL003', 'CAT003', 'link7'),
('SP010', 'Balenciaga Stan Smith', 1700000, 50, 'SPL003', 'CAT003', 'link7')

INSERT INTO OrderDetail VALUES
('HD001', 'SP001', 5, 1100000),
('HD002', 'SP002', 1, 1200000),
('HD003', 'SP003', 2, 1300000),
('HD004', 'SP004', 10, 1400000),
('HD005', 'SP005', 5, 1500000)
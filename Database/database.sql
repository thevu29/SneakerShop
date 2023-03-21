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
	foreign key (SupplierID) references Supplier(SupplierID)
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

INSERT INTO OrderDetail VALUES
('HD001', 'SP001', 5, 1100000),
('HD001', 'SP002', 1, 1200000),
('HD001', 'SP008', 3, 1700000),
('HD001', 'SP010', 2, 1700000),
('HD002', 'SP002', 1, 1200000),
('HD002', 'SP005', 1, 1500000),
('HD003', 'SP003', 2, 1300000),
('HD004', 'SP004', 10, 1400000),
('HD005', 'SP005', 5, 1500000)

INSERT INTO Supplier VALUES
('SPL001', 'NIKE', N'Hồ Chí Minh', '0123456789', 'nike@gmail.com'),
('SPL002', 'ADDIDAS', N'Hà Nội', '0123456789', 'addidas@gmail.com'),
('SPL003', 'BALENCIAGA', N'Đà Nẵng', '0123456789', 'balenciaga@gmail.com'),
('SPL004', 'GUCCI', N'Nha Trang', '0123456789', 'gucci@gmail.com'),
('SPL005', 'VANS', N'Hồ Chí Minh', '0123456789', 'vans@gmail.com'),
('SPL006', 'CONVERSE', N'Hà Nội', '0123456789', 'converse@gmail.com'),
('SPL007', 'JORDAN', N'Đà Nẵng', '0123456789', 'jordan@gmail.com'),
('SPL008', 'ASICS', N'Đà Nẵng', '0123456789', 'jordan@gmail.com')

INSERT INTO Category VALUES
('CAT001', 'Nike'),
('CAT002', 'Addidas'),
('CAT003', 'Balenciaga'),
('CAT004', 'Gucci'),
('CAT005', 'Vans'),
('CAT006', 'Converse'),
('CAT007', 'Jordan'),
('CAT008', 'Asics')

INSERT INTO Product VALUES
('SP001', 'Vans Vault', 1100000, 50, 'SPL005', 'CAT005'),
('SP002', 'Converse Chuck', 1200000, 50, 'SPL006', 'CAT006'),
('SP003', 'Air Jordan 1 Retro', 1300000, 50, 'SPL007', 'CAT007'),
('SP004', 'Nike Air Force 1', 1400000, 50, 'SPL001', 'CAT001'),
('SP005', 'Ultra Addidas 4D', 1500000, 50, 'SPL002', 'CAT002'),
('SP006', 'Nike Air Max', 1600000, 50, 'SPL001', 'CAT001'),
('SP007', 'Balenciaga Stan Smith', 1700000, 50, 'SPL003', 'CAT003'),
('SP008', 'Adidas X90000L4', 7900000, 65, 'SPL002', 'CAT002'),
('SP009', 'Asics III', 1700000, 45, 'SPL008', 'CAT008'),
('SP010', 'Nike Air Max 90 Paris', 5500000, 100, 'SPL001', 'CAT001'),
('SP011', 'Puma RS Z LTH Trainers', 3700000, 120, 'SPL004', 'CAT004'),
('SP012', 'Asics III Grey', 1650000, 55, 'SPL008', 'CAT008'),
('SP013', 'Vans Black Ball SF', 2900000, 130, 'SPL005', 'CAT005'),
('SP014', 'Jordan 1 High Tokyo Hack', 7200000, 60, 'SPL007', 'CAT007'),
('SP015', 'Fila White Ice', 2050000, 50, 'SPL003', 'CAT003'),
('SP016', 'Adidas Pod S3.1', 7900000, 40, 'SPL002', 'CAT002'),
('SP017', 'Nike Air Force 1', 2690000, 30, 'SPL001', 'CAT001'),
('SP018', 'Converse Dark Burgundy', 2600000, 20, 'SPL006', 'CAT006'),
('SP019', 'Jordan 1 Mid Carbon Fiber', 6500000, 95, 'SPL007', 'CAT007'),
('SP020', 'Adidas Edge Xt Black', 3850000, 25, 'SPL002', 'CAT002'),
('SP021', 'Puma Cell Venom Ader', 5500000, 35, 'SPL004', 'CAT004'),
('SP022', 'Jordan 33 Blackout', 1250000, 45, 'SPL007', 'CAT007'),
('SP023', 'Adidas Superstar', 3900000, 75, 'SPL002', 'CAT002'),
('SP024', 'Jordan Air CMFT', 6400000, 85, 'SPL007', 'CAT007'),
('SP025', 'Puma RS-X Toys While', 3800000, 90, 'SPL004', 'CAT004'),
('SP026', 'Nike Air Force 1', 3450000, 80, 'SPL001', 'CAT001'),
('SP027', 'Asics III Birch', 1500000, 75, 'SPL008', 'CAT008'),
('SP028', 'Fila All White', 2000000, 100, 'SPL003', 'CAT003'),
('SP029', 'Nike Why not zer 0.3', 5500000, 150, 'SPL001', 'CAT001'),
('SP030', 'Jordan 1 Zoom Air', 7000000, 50, 'SPL007', 'CAT007')

INSERT INTO Size VALUES (39), (40), (41), (42), (43)

INSERT INTO Product_Size VALUES
('SP001', 39, 20),
('SP001', 41, 30),

('SP002', 40, 10),
('SP002', 41, 20),
('SP002', 42, 10),
('SP002', 43, 10),

('SP003', 41, 20),
('SP003', 42, 20),
('SP003', 43, 10),

('SP004', 41, 25),
('SP004', 42, 25),

('SP005', 39, 10),
('SP005', 40, 10),
('SP005', 41, 10),
('SP005', 42, 10),
('SP005', 43, 10),

('SP006', 39, 25),
('SP006', 41, 10),
('SP006', 43, 15),

('SP007', 39, 13),
('SP007', 41, 17),
('SP007', 42, 10),
('SP007', 43, 10),

('SP008', 41, 19),
('SP008', 42, 39),
('SP008', 43, 7),

('SP009', 39, 13),
('SP009', 40, 12),
('SP009', 42, 12),
('SP009', 43, 8),

('SP010', 39, 35),
('SP010', 42, 35),
('SP010', 43, 30),

('SP011', 39, 42),
('SP011', 40, 18),
('SP011', 41, 34),
('SP011', 42, 26),

('SP012', 39, 11),
('SP012', 40, 34),
('SP012', 42, 10),

('SP013', 39, 27),
('SP013', 40, 25),
('SP013', 41, 39),
('SP013', 42, 28),
('SP013', 43, 11),

('SP014', 40, 27),
('SP014', 41, 33),

('SP015', 39, 12),
('SP015', 40, 12),
('SP015', 41, 12),
('SP015', 42, 14),

('SP016', 39, 18),
('SP016', 40, 11),
('SP016', 41, 11),

('SP017', 39, 11),
('SP017', 40, 12),
('SP017', 41, 5),
('SP017', 42, 2),

('SP018', 39, 4),
('SP018', 40, 5),
('SP018', 41, 3),
('SP018', 42, 6),
('SP018', 43, 2),

('SP019', 39, 7),
('SP019', 40, 23),
('SP019', 41, 39),
('SP019', 42, 26),

('SP020', 41, 25),

('SP021', 41, 13),
('SP021', 42, 22),

('SP022', 40, 17),
('SP022', 41, 15),
('SP022', 42, 12),
('SP022', 43, 1),

('SP023', 39, 43),
('SP023', 40, 22),
('SP023', 41, 10),

('SP024', 39, 10),
('SP024', 40, 19),
('SP024', 41, 21),
('SP024', 42, 12),
('SP024', 43, 23),

('SP025', 40, 43),
('SP025', 41, 47),

('SP026', 39, 11),
('SP026', 40, 44),
('SP026', 41, 12),
('SP026', 43, 13),

('SP027', 40, 47),
('SP027', 41, 28),

('SP028', 40, 19),
('SP028', 41, 28),
('SP028', 42, 47),
('SP028', 43, 6),

('SP029', 40, 75),
('SP029', 41, 75),

('SP030', 40, 12),
('SP030', 41, 13),
('SP030', 42, 14),
('SP030', 43, 11)
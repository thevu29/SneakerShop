create database py_ql
use py_ql

create table ACCESS
(
	AccsID varchar(8) primary key,
	AccsName nvarchar(10),
	AccsDescription nvarchar(30)
)
create table ACCOUNT
(
	AccID varchar(8) primary key,
	UserName varchar(12),
	Pass varchar(15),
	AccsID varchar(8),
	foreign key (AccsID) references ACCESS(AccsID)
)
create table CUSTOMER
(
	CustID varchar(8) primary key,
	CustName nvarchar(15),
	CustAddress nvarchar(12),
	Phone varchar(12),
	Sex nvarchar(5),
	Point int,
	AccID varchar(8),
	foreign key (AccID) references ACCOUNT(AccID)
)
create table PURCHASE_ORDER
(
	OrderID varchar(8) primary key,
	CustID varchar(8),
	OrderDate datetime,
	Total int,
	Order_Status nvarchar(10),
	foreign key (CustID) references CUSTOMER(CustID)
)
create table SUPPLIER
(
	SuppID varchar(8) primary key,
	SuppName nvarchar(20),
	SuppAddress nvarchar(20),
	Phone varchar(12),
	Email varchar(15)
)
create table CATEGORY
(
	CatgID varchar(8) primary key,
	CatgName nvarchar(20),
	CatgDescription nvarchar(30)
)
create table PRODUCT
(
	ProdID varchar(8) primary key,
	ProdName nvarchar(20),
	Price money,
	Stocks int,
	Category nvarchar(15),
	SuppID varchar(8),
	CatgID varchar(8),
	ImgLink varchar(50),
	foreign key (CatgID) references CATEGORY(CatgID),
	foreign key (SuppID) references SUPPLIER(SuppID)
)
create table ORDERDETAIL
(
	OrderID varchar(8),
	ProdID varchar(8),
	Quantity int,
	primary key (OrderID, ProdID),
	foreign key (OrderID) references PURCHASE_ORDER(OrderID),
	foreign key (ProdID) references PRODUCT(ProdID)
)
INSERT INTO ACCESS VALUES
('ACC111','nv1','description1'),
('ACC112','nv2','description2'),
('ACC113','nv3','description3'),
('ACC114','nv4','description4'),
('ACC115','nv5','description5'),
('ACC116','nv6','description6'),
('ACC117','nv7','description7')

INSERT INTO ACCOUNT VALUES
('AC111','nhanvien1','111','ACC111'),
('AC112','nhanvien2','112','ACC112'),
('AC113','nhanvien3','113','ACC113'),
('AC114','nhanvien4','114','ACC114'),
('AC115','nhanvien5','115','ACC115'),
('AC116','nhanvien6','116','ACC116'),
('AC117','nhanvien7','117','ACC117')

INSERT INTO CUSTOMER VALUES
('CUS111','a',N'Hồ Chí Minh','0112233441','nam',10,'AC111'),
('CUS112','b',N'Hà Nội','0112233442','nữ',10,'AC112'),
('CUS113','c',N'Đồng Nai','0112233443','nữ',10,'AC113'),
('CUS114','d',N'Quảng Bình ','0112233444','nam',10,'AC114'),
('CUS115','e',N'Hồ Chí Minh','0112233445','nam',10,'AC115'),
('CUS116','f',N'Đồng Nai','0112233446','nam',10,'AC116'),
('CUS117','g',N'Khánh Hòa','0112233447','nữ',10,'AC117')

INSERT INTO PURCHASE_ORDER VALUES
('ORDERID1','CUS111','2023-1-1',12,'status1'),
('ORDERID2','CUS112','2023-1-2',11,'status2'),
('ORDERID3','CUS113','2023-1-3',10,'status3'),
('ORDERID4','CUS114','2023-1-4',9,'status4'),
('ORDERID5','CUS115','2023-1-5',5,'status5'),
('ORDERID6','CUS116','2023-1-6',18,'status6'),
('ORDERID7','CUS117','2023-1-7',4,'status7')

INSERT INTO SUPPLIER VALUES
('IDS111','a',N'Hồ Chí Minh 1','0112233441','a@gmail.com'),
('IDS112','b',N'Hồ Chí Minh 2','0112233442','b@gmail.com'),
('IDS113','c',N'Hồ Chí Minh 3','0112233443','c@gmail.com'),
('IDS114','d',N'Hồ Chí Minh 4','0112233444','d@gmail.com'),
('IDS115','e',N'Hồ Chí Minh 5','0112233445','e@gmail.com'),
('IDS116','f',N'Hồ Chí Minh 6','0112233446','f@gmail.com'),
('IDS117','g',N'Hồ Chí Minh 7','0112233447','g@gmail.com')

INSERT INTO CATEGORY VALUES
('CA111','name1','description1'),
('CA112','name2','description2'),
('CA113','name3','description3'),
('CA114','name4','description4'),
('CA115','name5','description5'),
('CA116','name6','description6'),
('CA117','name7','description7')

INSERT INTO PRODUCT VALUES
('MSP111','VANS VAULT',1100000,36,'Vans','IDS111','CA111','link1'),
('MSP112','Converse Chuck',1200000,37,'Converse','IDS112','CA112','link2'),
('MSP113','Air Jordan 1 Retro',1300000,38,'Nike','IDS113','CA113','link3'),
('MSP114','ULTRA 4DFWD SHOES',1400000,39,'Adidas','IDS114','CA114','link4'),
('MSP115','BASAS WORKADAY',1500000,40,'Ananas','IDS115','CA115','link5'),
('MSP116','Nike Air Max',1600000,41,'Nike','IDS116','CA116','link6'),
('MSP117','Chunky Liner Yankees',1700000,42,'MLB','IDS117','CA117','link7')

INSERT INTO ORDERDETAIL VALUES
('ORDERID1','MSP111',11),
('ORDERID2','MSP112',12),
('ORDERID3','MSP113',13),
('ORDERID4','MSP114',14),
('ORDERID5','MSP115',15),
('ORDERID6','MSP116',16),
('ORDERID7','MSP117',17)










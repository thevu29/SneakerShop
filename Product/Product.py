import pyodbc

def Convert(item):
    array = []
    for i in range(0, len(item)):
        item[i] = str(item[i]).strip("'")
        array.append(item[i])
    return array

class ProductData():
    productList = []
    
    def __init__(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost;'
                      'Database=py_ql;'
                      'Trusted_Connection=yes;')
        self.data = conn.cursor()
    
    # ham lay so luong va size cua san pham dua vao ten san pham
    def getSizeAndQuantity(self, productName):
        arr = []
        self.data.execute("SELECT ps.SizeNumber, ps.Quantity FROM Product_Size ps JOIN Product p ON p.ProductID = ps.ProductID WHERE p.ProductName = " 
                          + "'" + productName + "'")
        for item in self.data:
            item = Convert(item)
            arr.append(item)
        return arr
    
    # ham lay toan bo san pham
    def getProductList(self, condition):
        listProduct = []
        
        if(condition.lower().capitalize() == "Tất cả"):
            self.data.execute("Select distinct p.ProductID, p.ProductName, p.Price from Product p JOIN Category c ON p.CategoryID = c.CategoryID")
        else:
            self.data.execute("Select distinct p.ProductID, p.ProductName, p.Price from Product p JOIN Category c ON p.CategoryID = c.CategoryID WHERE c.CategoryName = " 
                              + "'" + condition + "'")
            
        for item in self.data:
            item[2] = '{0:.2f}'.format(item[2]).rstrip('0').rstrip('.')
            item = Convert(item)
            listProduct.append(item)
        return listProduct
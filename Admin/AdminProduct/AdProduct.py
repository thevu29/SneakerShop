import pyodbc

def Convert(item):
    array = []
    for i in range(0, len(item)):
        item[i] = str(item[i]).strip("'")
        array.append(item[i])
    return array

class AdProductData():
    def __init__(self):
        self.productList = []
        
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-P91166MQ\\THEVU_SQL;'
                      'Database=py_ql;'
                      'Trusted_Connection=yes;')

        data = conn.cursor()
        data.execute('select * from dbo.Product')
        
        str = '1'
        cnt = int(str)
        for item in data:
            item[2] = '{0:.2f}'.format(item[2]).rstrip('0').rstrip('.')
            
            id = self.getID(cnt)
            cnt += 1
            imagePath = f'./img/product/SP{id}.png'
            item = Convert(item)
            item.append(imagePath)
            
            self.productList.append(item)
            
    def getProductList(self):
        return self.productList
    
    def getID(self, cnt):
        id = str(cnt)
        while len(id) != 3:
            id = '0' + id
        return id
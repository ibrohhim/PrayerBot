from requests import get,post

class Prayrequests:
    def __init__(self,sh:str)->None:
        self.__reg_id = {"Toshkent":1,
                         "Andijon":17,
                         "Samarqand":47,
                         "Buxoro":34,
                        "Fargona": 77,
                        "Jizzax":107,
                        "Xorazm":101}
        self.__city = sh
        self.__content = ""
        self.__utl = "https://praytime.uz/"

    def request(self):
        try:
            id = 1
            if self.__city in self.__reg_id:
                id = self.__reg_id[self.__city]
            print(id)
            body = {
                "region_id": id

            }
            res = get(self.__utl,params = body)
            if res.status_code == 200:
                self.__content = res.text
            else:
                raise Exception(f"surov yuborishda hatlik bor :{res.status_code}")
        except Exception as e:
            print(e)
    @property
    def Content(self):
        return self.__content
    
        

    
            
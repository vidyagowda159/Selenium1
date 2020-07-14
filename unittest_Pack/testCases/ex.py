class fest():
    date='12/07/2020'

    def displaydate(self):
        print('fest will be on : ',self.date)

    @classmethod
    def update_date(cls,newdate):
        cls.date=newdate

f1=fest()
f2=fest()
print('date in f1 :',f1.date)
f1.update_date('15/07/2020')
print(f1.displaydate())
print(f2.displaydate())







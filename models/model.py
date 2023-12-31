from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date, JSON
from models.database import Base

# класс для отработки навыков json
class Cont(Base):
    __tablename__ = 'cont'
    
    id = Column(Integer, primary_key=True)
    cont_data= Column(JSON)
   
# класс для отработки навыков по работе с бд (заливка данных из csv)
class Test(Base):
    __tablename__ = 'test'
    
    id = Column(Integer, primary_key=True)
    btt = Column(String(3))
    date_arr_jd =  Column(Date, nullable=True)
    hbl= Column(String(3))
    date_real_hbl =  Column(Date, nullable=True)
    customs_post= Column(String(100))
    date_check =  Column(Date, nullable=True)
    date_create_order =  Column(Date, nullable=True)
    date_get_order =  Column(Date, nullable=True)
    customer= Column(String(100))
    provider= Column(String(100))
    invoice_number= Column(String(25))
    broker= Column(String(25))
    recipient= Column(String(60))
    forwarder= Column(String(60))
    store= Column(String(100))
    cont_number= Column(String(100))
    cont_type= Column(String(15))
    del_cond= Column(String(3))
    place_dispatch= Column(String(25))
    country_dispatch= Column(String(25))
    place_delivery= Column(String(50))
    country_delivery= Column(String(25))
    line_w= Column(String(50))
    agent= Column(String(35))
    goods= Column(String(100))
    order_number= Column(String(100))
    number_places = Column(Integer, nullable=True)
    weight = Column(Float, nullable=True)
    volume = Column(Float, nullable=True)
    price = Column(Float, nullable=True)
    spec_load_cond= Column(String(300))
    date_ready =  Column(Date, nullable=True)
    date_load =  Column(Date, nullable=True)
    date_pack =  Column(Date, nullable=True)
    date_enter_sea =  Column(Date, nullable=True)
    consignment_number= Column(String(100))
    date_prepare_doc =  Column(Date, nullable=True)
    date_telex =  Column(Date, nullable=True)
    note= Column(String(200))
    date_send_docs =  Column(Date, nullable=True)
    date_arr =  Column(Date, nullable=True)
    port_name= Column(String(200))
    date_get_doc =  Column(Date, nullable=True)
    date_send_decl =  Column(Date, nullable=True)
    date_iss_decl =  Column(Date, nullable=True)
    decl_number= Column(String(100))
    date_send_jd =  Column(Date, nullable=True)
    date_unload =  Column(Date, nullable=True)
  
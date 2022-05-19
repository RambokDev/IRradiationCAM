# coding: utf-8

import sqlite3
conn = sqlite3.connect('TP.db')


cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
     id_users INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     GroupeName TEXT,
     mail_users1 TEXT,
     mail_users2 TEXT,
     mail_users3 TEXT
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS surfaceObservation(
     id_surfaceObservation INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     id_users INTEGER,
     SurfaceObservation1_text1 VARCHAR(255),
     SurfaceObservation2_text1 VARCHAR(255),
     SurfaceObservation3_text1 VARCHAR(255)
     
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ContactTemperatureCalculation(
     id_ContactTemperatureCalculation INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     id_users INTEGER,
     ContactTemperatureCalculation1_text1 VARCHAR(255),
     ContactTemperatureCalculation1_text2 VARCHAR(255),
     ContactTemperatureCalculation1_text3 VARCHAR(255),
     ContactTemperatureCalculation2_text1 VARCHAR(255),
     ContactTemperatureCalculation2_text2 VARCHAR(255)

)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS ThermalApproachOfElectricPhenomena(
     id_ThermalApproachOfElectricPhenomena INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     id_users INTEGER,
     ThermalApproachOfElectricPhenomena1_text1 VARCHAR(255),
     ThermalApproachOfElectricPhenomena2_text1 VARCHAR(255),
     ThermalApproachOfElectricPhenomena2_text2 VARCHAR(255),
     ThermalApproachOfElectricPhenomena2_text3 VARCHAR(255),
     ThermalApproachOfElectricPhenomena3_radioB VARCHAR(255),
     ThermalApproachOfElectricPhenomena4_list1 VARCHAR(255),
     ThermalApproachOfElectricPhenomena4_list2 VARCHAR(255),
     ThermalApproachOfElectricPhenomena4_list3 VARCHAR(255),
     ThermalApproachOfElectricPhenomena4_text1 VARCHAR(255)


)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS HeatTransferInFins(
     id_HeatTransferInFins INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     id_users INTEGER,
     HeatTransferInFins1_text1 VARCHAR(255),
     HeatTransferInFins2_text1 VARCHAR(255),
     HeatTransferInFins3_text1 VARCHAR(255),
     HeatTransferInFins4_text1 VARCHAR(255),
     HeatTransferInFins4_text2 VARCHAR(255),
     HeatTransferInFins4_text3 VARCHAR(255),
     HeatTransferInFins4_text4 VARCHAR(255),
     HeatTransferInFins4_text5 VARCHAR(255),
     HeatTransferInFins4_text6 VARCHAR(255),
     HeatTransferInFins4_text7 VARCHAR(255)



)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS IR_RadiationCAM(
     id_IR_RadiationCAM INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     id_users INTEGER,
     IR_RadiationCAM1_text1 VARCHAR(255)

)
""")




cursor.execute("""
CREATE TABLE IF NOT EXISTS tableData( 
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     id_users INTEGER,
     cosh1    float,
     cosh2    float,
     cosh3    float,
     Tx    float
)
""")


conn.commit()








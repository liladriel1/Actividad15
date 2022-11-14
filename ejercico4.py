import pandas as pd
import matplotlib.pyplot as plt

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def cargar_archvivo():
    datos = pd.read_csv("C:\\Users\\Tecnicos\\Desktop\\farmacias.csv")
    # datos = datos[["FID","NOMBRE","GEOCODIGO","DIRECCION","UTM_X","UTM_Y","GRAD_X","GRAD_Y","WEB","COFSCTFE","BARRIO","DISTRITO","COD_POSTAL","TELEFONO","LUNES","MARTES","MIERCOLES","JUEVES","VIERNES","SABADO","DOMINGO"]]
    df = datos[["DIRECCION", "NOMBRE"]]

    df = datos.rename(columns={
        "DIRECCION": "DRC",
        "NOMBRE": "NOM",
    })

    print(df.sample(5))
    valor_por_ciudad = df.groupby("DRC")["NOM"].mean()
    valor_por_ciudad.head(10).plot.barh()
    plt.show()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

cargar_archvivo()
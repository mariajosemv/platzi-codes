from borracho import BorrachoTradicional
from campo import Campo 
from coordenada import Coordenada 

from bokeh.models import LabelSet, ColumnDataSource
from bokeh.plotting import figure, show

def ejecutar_caminata(pasos_a_recorrer, tipo_de_borracho): 
    """Ejecuta la caminata para x pasos_a_recorrer """
    borracho = tipo_de_borracho(nombre='David')
    origen = Coordenada(0, 0)
    campo = Campo()
    campo.anadir_borracho(borracho, origen)
    coordenadas_x = [0]
    coordenadas_y = [0]

    for _ in range(pasos_a_recorrer):
        campo.mover_borracho(borracho)  #devuelve tupla(x,y)
        nueva_coordenada_x = campo.obtener_coordenada(borracho).x
        nueva_coordenada_y = campo.obtener_coordenada(borracho).y
        coordenadas_x.append(nueva_coordenada_x)
        coordenadas_y.append(nueva_coordenada_y)
    return coordenadas_x, coordenadas_y

def main_3(pasos_a_recorrer, tipo_de_borracho):
    x, y = ejecutar_caminata(pasos_a_recorrer,tipo_de_borracho)

    titulo_grafica = f"Random walk for {pasos_a_recorrer} steps"
    graficar(x, y, "x", "y", titulo_grafica, "Walk")

def graficar(x, y, nombre_x, nombre_y, titulo, leyenda):

    names = ['Start', 'End']
    
    x_plot = [x[0], x[-1]]
    y_plot = [y[0], y[-1]]    

    grafica = figure(title=titulo, x_axis_label=nombre_x, y_axis_label=nombre_y)
    grafica.line(x, y, legend=leyenda)
    
    grafica.circle(x_plot, y_plot, size=10, color="slateblue", alpha=0.5)
    source = ColumnDataSource(data=dict(x=x_plot, y=y_plot, names=names))
    labels = LabelSet(x='x', y='y', text='names', level='glyph', x_offset=5, y_offset=5, source=source, render_mode='canvas')
    grafica.add_layout(labels)

    show(grafica)

if __name__ == '__main__':
    
	
    pasos_a_recorrer = int(input("Choose how many steps the drunk will walk: "))
    main_3(pasos_a_recorrer, BorrachoTradicional)

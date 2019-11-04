import pandas as pd
path= 'C:/Users/Aspivina/PycharmProjects/excelconvertor/libro1.xls'
moviexls= 'C:/Users/Aspivina/PycharmProjects/e2c/movies.xls'
horasexls= 'C:/Users/Aspivina/PycharmProjects/e2c/reporte_horas.xls'



#movies = pd.read_excel(moviexls)
#movies.head()
#movies.info()
movie_sheet1 = pd.read_excel(horasexls,sheet_name=0, index_col=0) #index_col=0 se come la lista de 0,1,2,..,n de la numeración de cada fila
print(movie_sheet1.head(n=10))  #n=2 muestra el número de filas
#movie_sheet1.info()
print(movie_sheet1.shape) #da el tamaño de la matriz (32 filas, 6 columnas)
movie_sheet1.to_csv('reporte_horas.csv')




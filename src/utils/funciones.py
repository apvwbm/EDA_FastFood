import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Función para crear los gráficos
def plot_corr(df, x_var, y_var, ax, scatter_color, reg_color):
    x_var_name, x_var_label = x_var
    y_var_name, y_var_label = y_var

    # Calcular la correlación de Pearson
    corr, _ = stats.pearsonr(df[x_var_name], df[y_var_name])

    # Scatterplot con regresión
    sns.scatterplot(data=df, x=x_var_name, y=y_var_name, ax=ax[0], alpha=0.6, color=scatter_color, s=50)
    sns.regplot(data=df, x=x_var_name, y=y_var_name, scatter=False, ax=ax[0], color=reg_color, line_kws={'linestyle': '--'})
    ax[0].set_title(f'Scatterplot: {x_var_label} vs {y_var_label} (Correlación: {corr:.2f})', fontsize=14)
    ax[0].set_xlabel(f'{x_var_label}', fontsize=12)
    ax[0].set_ylabel(f'{y_var_label}', fontsize=12)

    # Boxplot en horizontal
    sns.boxplot(data=df, y=y_var_name, ax=ax[1], color=scatter_color, width=0.6)
    ax[1].set_title(f'Distribución de {y_var_label}', fontsize=14)
    ax[1].set_ylabel('')
    
def plot_pyramid(df, category_col, azucar_col, sodio_col, ax, colors):
    # Agrupamos por la categoría y calculamos la media de azúcares y sodio
    grouped = df.groupby(category_col).agg({azucar_col:'mean', sodio_col:'mean'}).reset_index()
    
    # Ordenamos las categorías según la columna category_col (o azucar_col, dependiendo)
    grouped = grouped.sort_values(by=category_col)
    
    # Seleccionamos solo las primeras 7 categorías
    grouped = grouped.head(7)

    # Extraemos los valores
    categories = grouped[category_col].astype(str)
    azucar_vals = grouped[azucar_col]
    sodio_vals = grouped[sodio_col]

    azucar_perc = azucar_vals
    sodio_perc = sodio_vals

    # Convertimos azúcar a valores negativos para plotearlos a la izquierda
    azucar_left = -azucar_perc

    # Calculamos el rango máximo para crear un eje simétrico
    max_val = max(abs(azucar_left.min()), sodio_perc.max())

    # Configuramos la posición en el eje Y
    y_positions = np.arange(len(categories))

    # Graficamos las barras horizontales
    ax.barh(y_positions, azucar_left, color=colors['azucar'], align='center')
    ax.barh(y_positions, sodio_perc, color=colors['sodio'], align='center')

    # Ajustamos el rango del eje X para ser simétrico
    ax.set_xlim(-max_val*1.1, max_val*1.1)  # Un 10% extra para estética

    # Etiquetas del eje Y
    ax.set_yticks(y_positions)
    ax.set_yticklabels(categories)

    # Línea vertical en el medio
    ax.axvline(0, color='black', linewidth=1)

    # Etiquetas y título
    ax.set_xlabel('Valor')
    ax.set_ylabel(category_col)
    ax.set_title('Comparación Azúcar vs Sodio', fontsize=14)

    # Grid vertical para facilitar la lectura
    ax.grid(axis='x', linestyle='--', color='gray', alpha=0.7)

    # Leyenda
    custom_lines = [
        plt.Line2D([0], [0], color=colors['azucar'], lw=6),
        plt.Line2D([0], [0], color=colors['sodio'], lw=6)
    ]
    ax.legend(custom_lines, ['Azúcar', 'Sodio'], loc='lower center', bbox_to_anchor=(0.5, -0.1), ncol=2)

    # Invertimos el orden en el eje Y, para que las categorías más grandes estén arriba (opcional)
    ax.invert_yaxis()

    return ax
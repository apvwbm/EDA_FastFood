<h1>🍔 EDA: Análisis Exploratorio de Comida Rápida</h1>

<h2>📝 Descripción del Proyecto</h2>
<p>Este proyecto realiza un análisis exploratorio de datos (EDA) en el dataset de pedidos de FastFood obtenido de <a href="https://www.kaggle.com/">Kaggle</a> analizando aspectos nutricionales como calorías, grasas, sodio, y su relación con otras variables. El propósito es obtener información útil que permita entender mejor las características nutricionales de los productos ofrecidos por diversas cadenas de comida rápida.</p>

<h2>🎯 Objetivos</h2>
<ul>
    <li>Comparar calorías por cadena para ver cuál ofrece productos menos calóricos.</li>
    <li>Comprobar correlaciones entre <code>Calorías</code> con <code>Grasas</code>, <code>Sodio</code> y <code>Azúcares</code>.</li>
    <li>Impacto de grasas saturadas en el colesterol.</li>
    <li>Identificar productos extremos (muy altos en calorías o sodio).</li>
    <li>Evaluar salud según puntos de <a href="https://www.weightwatchers.com/us/">Weight Watchers Points</a>.</li>
</ul>

<h2>📑 Estructura del Proyecto</h2>
<pre>
📂 EDA_FastFood/
├── 📂 src/
│   ├── 📂 data/            
│   │   └── fastfood.csv       # Dataset en formato CSV.
│   ├── 📂 img/                # Imágenes y gráficos generados.
│   └── 📂 utils/
│       └── funciones.py       # Funciones auxiliares para visualización.
│
├── main.ipynb                 # Notebook principal con el análisis.
├── memoria.pdf                # Informe final en formato PDF.
├── presentacion.pptx          # Presentación del proyecto.
├── .gitignore                 # Archivos y carpetas a ignorar por Git.
└── README.md                  # Descripción breve del proyecto.
</pre>


<h2>🛠️ Tecnologías</h2>
<ul>
    <li>Python</li>
    <li>Pandas</li>
    <li>Matplotlib / Seaborn</li>
</ul>

<h2>🚀 Cómo Ejecutar el Proyecto</h2>
<ol>
    <li>Clona el repositorio:</li>
    <pre>git clone https://github.com/usuario/EDA_FastFood.git</pre>
    <li>Instala las dependencias necesarias:</li>
    <pre>pip install -r requirements.txt</pre>
    <li>Abre el archivo <code>memoria.ipynb</code> y ejecuta todas las celdas en Jupyter Notebook.</li>
</ol>

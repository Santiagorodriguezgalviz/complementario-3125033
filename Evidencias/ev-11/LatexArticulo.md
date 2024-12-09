\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[spanish]{babel}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{setspace}
\usepackage{titlesec}

% Estilo para el título
\titleformat{\section}
  {\normalfont\Huge\bfseries\centering} % Formato del título
  {} % Etiqueta
  {0pt} % Espacio entre etiqueta y título
  {} % Formato del título

\begin{document}

% Portada
\begin{titlepage}
    \centering
    \vspace*{2cm}
    
    {\Huge \textbf{Desarrollo de un Sistema de Gestión Digital}} \\
    \vspace{0.5cm}
    {\LARGE \textbf{para Inspecciones Agrícolas:}} \\
    {\LARGE \textbf{Caso de Estudio del Proyecto FincaAudita}} \\
    
    \vspace{1.5cm}

     {\Large Autores:} \\
    {\Large Jhon Alexander Corredor Medina} \\
    {\Large Carlos Andrés Pantoja Jaramillo} \\
    {\Large Heyder Santiago Rodríguez Galviz} \\
    
    \vspace{1cm}
    
    {\Large Instructores:} \\
    {\Large Jesús Ariel González Bonilla} \\
    {\Large Jhon William Corredor Araujo} \\
    
    \vspace{1cm}
    
    {\large SENA: Centro de la Industria, La Empresa y Los Servicios} \\
    {\large Análisis y Desarrollo de Software} \\
    
    \vspace{1cm}
    
    {\large 2024} \\
    
    \vfill
    
    \includegraphics[width=0.3\textwidth]{imagen-auth.jpg} % Ajusta el tamaño de la imagen aquí
    
\end{titlepage}

% Abstract
\begin{center}
    \textbf{\LARGE Abstract}
\end{center}
\vspace{0.5cm}
\begin{quote}
Efficient management of data collected during agricultural inspections is critical to ensure product quality and compliance with international standards. However, traditional methods relying on paper forms have significant limitations in terms of time, accuracy, and information accessibility. The FincaAudita project offers a digital solution to optimize the process of data collection, storage, and real-time analysis, enabling better decision-making. The system provides an intuitive interface for mobile and desktop devices, with features that ensure the integrity and security of the collected data. This article explores the functional and non-functional requirements of the project, as well as its advantages in managing agricultural data.
\end{quote}

\begin{center}
    \textbf{Keywords:} management software, agricultural inspections, process optimization, digitization, data security.
\end{center}

\vspace{1cm}

% Resumen
\begin{center}
    \textbf{\LARGE Resumen}
\end{center}
\vspace{0.5cm}
\begin{quote}
El manejo eficiente de la información recolectada durante las inspecciones agrícolas es esencial para garantizar la calidad de los productos y el cumplimiento de los estándares internacionales. Sin embargo, el método tradicional basado en formularios en papel presenta limitaciones significativas en términos de tiempo, precisión y acceso a la información. El proyecto FincaAudita se propone como una solución digital para optimizar el proceso de recolección, almacenamiento y análisis de datos en tiempo real, permitiendo una mejor toma de decisiones. El sistema ofrece una interfaz intuitiva para dispositivos móviles y de escritorio, con funcionalidades que aseguran la integridad y seguridad de la información recolectada. Este artículo explora los requisitos funcionales y no funcionales del proyecto, así como sus ventajas en la gestión de datos agrícolas.
\end{quote}

\begin{center}
    \textbf{Palabras clave:} software de gestión, inspecciones agrícolas, optimización de procesos, digitalización.
\end{center}

% Resto del documento
\newpage
\section{1. Introducción}
La globalización ha impuesto exigencias cada vez mayores en la calidad y trazabilidad de los productos agrícolas. Las empresas agroindustriales, especialmente las exportadoras, deben llevar a cabo inspecciones constantes para verificar el cumplimiento de los estándares internacionales. Tradicionalmente, estas inspecciones se han realizado utilizando formularios en papel, lo que genera ineficiencias en términos de tiempo, costos y exactitud.

El proyecto FincaAudita surge como una solución integral para transformar el proceso de gestión de inspecciones agrícolas a través de la digitalización. Este software permite a los inspectores recolectar y gestionar datos en tiempo real, utilizando dispositivos móviles. Además, ofrece funcionalidades avanzadas para el análisis y la generación de informes, optimizando así la toma de decisiones estratégicas en la empresa. Este artículo describe los principales objetivos, características y beneficios del proyecto, además de sus requisitos técnicos, todo enmarcado en el desarrollo de software orientado a la mejora de procesos agroindustriales.

\section{2. Planteamiento del Problema}
El proceso manual de recolección y gestión de datos durante las inspecciones agrícolas se ha vuelto insostenible en el contexto actual de demanda global. Las empresas como Exportadora del Huila enfrentan desafíos significativos al intentar gestionar grandes volúmenes de información de manera eficiente. Los errores en la entrada de datos y la falta de centralización de la información dificultan el análisis oportuno de los resultados, lo que puede repercutir negativamente en la calidad de los productos y en la capacidad de cumplir con las normativas internacionales.

Por lo tanto, la necesidad de un sistema eficiente y digitalizado para gestionar la información recolectada durante las inspecciones es crucial no solo para mejorar la productividad, sino también para garantizar la calidad y competitividad en el mercado global.

\section{3. Objetivos}
El principal objetivo de FincaAudita es desarrollar un software que digitalice y optimice el proceso de recolección, almacenamiento y análisis de datos durante las inspecciones agrícolas. Los objetivos específicos incluyen:
\begin{itemize}
    \item Digitalizar el proceso de inspección, eliminando formularios en papel y reduciendo errores.
    \item Centralizar la información, asegurando su confidencialidad y accesibilidad.
    \item Mejorar el acceso y análisis de la información mediante una interfaz intuitiva.
    \item Garantizar la compatibilidad multiplataforma (Android y Windows).
    \item Asegurar la integridad de los datos mediante autenticación y cifrado robustos.
\end{itemize}

\section{4. Metodología}
El desarrollo de FincaAudita se llevó a cabo siguiendo los principios de desarrollo de software ágil. Se comenzó con una fase de análisis de los requisitos, durante la cual se identificaron las principales necesidades de las empresas agroindustriales.

\subsection{4.1. Tecnologías Utilizadas}
\begin{itemize}
    \item Backend: C, proporcionando una estructura robusta y segura.
    \item Frontend: Angular, asegurando una experiencia interactiva.
    \item Base de datos: PostgreSQL, con alta disponibilidad y seguridad.
    \item APIs externas: Integración mediante APIs RESTful.
\end{itemize}

\subsection{4.2. Desarrollo Iterativo}
El proyecto siguió un enfoque iterativo, incluyendo prototipos, pruebas de usabilidad y validación con usuarios clave.

\section{5. Resultados}
La implementación de FincaAudita ha mejorado significativamente la eficiencia de las inspecciones agrícolas. Se han reducido los errores en la entrada de datos y facilitado el acceso a la información en tiempo real, permitiendo una mejor toma de decisiones.

\section{6. Conclusiones}
FincaAudita representa un avance significativo en la gestión de inspecciones agrícolas, proporcionando una solución digital integral que mejora la recolección, almacenamiento y análisis de datos en tiempo real. Las empresas que adopten este tipo de soluciones estarán mejor posicionadas para competir en el mercado global.

\section{Referencias}
\begin{enumerate}
    \item Exportadora del Huila. (2024). Informe de especificación de requisitos.
    \item Rodríguez Santiago, H. S. (2024). FincaAudita: Gestión digital de inspecciones agrícolas.
    \item Corredor Medina, J. A. (2024). Especificación de requisitos de software para FincaAudita.
\end{enumerate}

\end{document}
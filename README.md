# coipo_gestion_flota_vehiculos — Maqueta del Sistema Nacional de Gestión de Flota

Maqueta de validación del sistema que reemplazará a GESAD para administrar el pool de
vehículos de CONAF: solicitud y autorización de salidas a terreno, asignación de patente
y conductor, control de caución y licencia (Decreto Ley N° 799), mantenciones,
vencimientos legales y combustible. Requerimiento de la Sección Servicios Generales
(GEFA), elaborado por la Unidad de Información y Análisis (UIA).

**Ver la maqueta:** https://alvarozvjac.github.io/coipo_gestion_flota_vehiculos/

> Demostración no operacional. Los vehículos y sus vencimientos son datos reales de
> Oficina Central (planilla de mantenciones al 28-09-2026), con los números de motor y
> chasis enmascarados. Personas, RUT, pólizas y cargas de combustible son ficticios
> (fecha simulada: 22-10-2026) y nada se envía a un servidor. La maqueta sirve para
> validar el flujo y el alcance con la contraparte y el Departamento de Informática.

## Cómo probarla

El selector **«Ver como»** de la cabecera cambia entre los cinco perfiles del ERS. Cada
perfil ve sus propios módulos:

| Perfil | Qué se puede probar |
|---|---|
| Funcionario solicitante | Nueva solicitud con revisión automática (días inhábiles DL 799, relevo sobre 400 km diarios, capacidad, conductor habilitado, imputación); seguimiento de sus solicitudes y orden de salida |
| Jefatura directa | Bandeja de aprobación: aprobar, observar o rechazar con comentario |
| Encargado de vehículos | Panel del día, asignación de patente y conductor con filtros de requisitos, visor Gantt, registro de salida y regreso, hoja de vida del vehículo, padrón de conductores, reportes por programa y centro de costo, y **reporte mensual o anual para Tesorería** (Excel, una fila por persona y salida finalizada) |
| Conductor | Agenda de cometidos y registro de odómetro, combustible y novedades mecánicas |
| Administrador nacional | Todo lo anterior, más calidad de datos de la carga inicial, tablas maestras, traspaso entre regiones y registro de auditoría |

Para ver el flujo completo: como **Funcionario solicitante**, envíe la solicitud de
ejemplo desde «Nueva solicitud»; como **Jefatura directa**, apruébela; como **Encargado de
vehículos**, asígnele vehículo y conductor en «Asignación» (se abre la orden de salida con
código QR) y revísela en el «Visor Gantt». La solicitud de ejemplo **OC-2026-000410**
muestra cómo el sistema descarta un camión con la revisión técnica vencida.

## Análisis de GESAD

Antes de diseñar el nuevo sistema, la UIA analizó GESAD, el sistema que hoy registra las salidas de vehículos y que dejará de operar a fines de 2026. El análisis se hizo con la base de datos, el código fuente y el menú que entregó el Departamento de Informática en respuesta al Memorándum N° 5772/2026.

- [Análisis de GESAD](docs/gesad/analisis-gesad.md): uso real del sistema, dependencias con otros sistemas, datos sensibles, calidad de datos, funciones que el ERS no menciona, antecedentes pendientes y el reporte para Tesorería que reemplaza la conexión con viáticos.
- [Diccionario de datos](docs/gesad/diccionario-datos.md): 77 tablas con columnas, tipos, claves y número de filas, sin registros.
- [Inventario de programas](docs/gesad/inventario-programas.md): menú del sistema y los 108 formularios y reportes, con las tablas que usa cada uno.
- [Lector del respaldo](herramientas/README.md): script que convierte el respaldo Oracle a CSV.

> El respaldo de la base de datos y los datos extraídos contienen datos personales y no se publican en este repositorio.

## Contenido del repositorio

- `index.html`: la maqueta completa en un solo archivo (código y estilos incluidos). Es
  la versión publicada en GitHub Pages (v0.2, con reporte para Tesorería).
- `banner-gefa.jpg` y `banner-gefa-corto.jpg`: banners de la Gerencia de Finanzas y
  Administración, tomados de `identidad/` de coipo_master_produccion.
- `.nojekyll`: indica a GitHub Pages que publique los archivos sin procesarlos.
- `docs/gesad/`: análisis de GESAD (ver sección anterior).
- `herramientas/`: script lector del respaldo de GESAD.
- `.gitignore`: impide versionar el respaldo y los CSV con datos personales.

Documento de referencia: Informe Técnico y Especificación de Requerimientos de Software
INF-LOG-TI-2026-V1 (Departamento de Servicios y Logística, 15-10-2026), con el Prototipo
Pool de Vehículos V7 y los comprobantes de salida de GESAD. Estándar de interfaz:
`identidad/ESTANDAR_UI.md` de coipo_master_produccion.

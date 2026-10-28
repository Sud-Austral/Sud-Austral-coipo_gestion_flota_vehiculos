# Inventario de programas de GESAD

GESAD es una aplicación Oracle Forms y Reports (cliente-servidor). El código fuente entregado tiene **66 formularios** (`.fmb`) y **42 reportes** (`.rdf`), más el menú (`menu.mmb` / `mvehiculos.mmx`, compilado el 23-03-2009 y modificado el 07-12-2011). Los comentarios del código registran cambios entre 2004 y 2010.

La revisión se hizo leyendo el texto contenido en los archivos binarios (títulos, mensajes y SQL), sin abrirlos en Oracle Forms Builder. Las descripciones son las que se pudieron leer; donde no hay un título legible se indica el contenido inferido de las tablas que usa.

## 1. Menú del sistema

Opciones tal como aparecen en el menú, agrupadas por menú principal:

- **Parámetros**: Parámetros generales; Tipos de vehículos; Tipos de origen de vehículos; Tipos de salidas de vehículos; Marcas y modelos de vehículos; Ubicación de vehículos; Tipos de conductores; Conceptos y descripciones; Conductores externos; Guardia que registra el movimiento diario.
- **Vehículos / Conductores**: Ficha de vehículos; Seguros de vehículos; Reporte ficha de vehículos; Reporte seguros de vehículos; Accidentes de tránsito; Guarde de vehículos; Ubicación de vehículos; Detalle de ubicación de vehículos; Operatividad mensual del vehículo; Ingreso de gastos; Gastos rechazados; Gastos de vehículos; Detalle por tipo de gasto; Gastos del período; Conductores; Ficha de conductores; Cursos de conductores; Reporte de conductores; Reporte de cursos de conductores.
- **Salidas de vehículos**: Ingreso de solicitudes; Consulta de salidas del día; Movimiento diario de vehículo; Consulta por conductor; Consulta por pasajeros para viático; Consulta de salidas por pasajeros.
- **Combustible**: Carga de archivo COPEC; Ingreso de combustible en efectivo; Ingreso de proyecto por consumo de combustible; Consulta de combustible por vehículo; Reportes de resumen de consumo; Compra a granel y distribución; Compañías de combustible; Estaciones de servicio por compañía; Departamentos definidos en COPEC; Tarjetas electrónicas; Modificación de proyectos por consumo de combustible.
- **Reportes**: Consumo de combustible anual por vehículo; Consumo de combustible por requerimiento; Gastos por vehículo; Rendimiento por vehículo; Listado de vehículos por estado; Revisión técnica; Revisión de gases; Informe de tarjetas por vehículo; Diferencia de proyecto entre salida y movimiento de combustible; Reportes PDF (resumen de gastos de combustible, operatividad mensual, operatividad mensual SIGI, revisión técnica).
- **Archivos**: Comunas por provincia y región; Compañías de combustible y estaciones de servicio.
- **Mantenciones**: Ficha de taller; Orden de trabajo; Emisión de orden de trabajo; Registro de factura; Análisis de pago de factura.
- **Cierre**: Cerrar período; Estado de cierre de centro financiero.
- **Accesos**: Selección de centro financiero; Mantenimiento de acceso.

El menú llama a un formulario, `vehi007` (tipos de origen de vehículos), cuyo fuente **no viene** en la carpeta entregada.

## 2. Archivos de programa

Columna «Tablas»: tablas de GESAD que el programa lee o escribe (no se listan las de otros sistemas institucionales).

| Archivo | Tipo | Descripción legible | Tablas de GESAD |
|---|---|---|---|
| `vehi001.fmb` | Formulario | Revisión Vehículo | CURSOS, DEPARTAMENTO, DET_ESTADO_DIA, TIPO_REVISION, UBICACION |
| `vehi002.fmb` | Formulario | — | DEPARTAMENTO, DET_DOCTOS, TIPO_DOCTOS, UBICACION |
| `vehi003.fmb` | Formulario | — | DEPARTAMENTO, DET_INVENTARIO, INV_VEHICULO, TIPO_INVENTARIO, UBICACION, VEHICULOS |
| `vehi004.fmb` | Formulario | Ubicación de Vehículos | DEPARTAMENTO, TIPO_SALIDA, UBICACION, VEHICULOS |
| `vehi005.fmb` | Formulario | Tipos de Salidas | DEPARTAMENTO, MEMORAMDUM, TIPO_SALIDA, UBICACION |
| `vehi006.fmb` | Formulario | — | DEPARTAMENTO, DETALLE_GASTO, DET_MANTENCION, SUBTIPO_GASTO, TIPO_GASTO, TIPO_SALIDA, UBICACION, VEHICULOS |
| `vehi008.fmb` | Formulario | — | CONDUCTORES, CURSOS, DEPARTAMENTO, TIPO_CONDUCTOR, TIPO_SALIDA, UBICACION |
| `vehi009.fmb` | Formulario | — | DEPARTAMENTO, TIPO_ORIGEN, UBICACION, VEHICULOS |
| `vehi010.fmb` | Formulario | Ficha de conductores (inferido) | AUSENCIAS, CONDUCTORES, CURSOS, CURSOS_CONDUCTORES, DEPARTAMENTO, INFRAC_CONDUCTORES, MOVIMIENTO_TARJETA_VEHICULO, SINIE_CONDUCTORES, TIPO_CONDUCTOR, TIPO_SALIDA, UBICACION, VEHI_CLASE_LICENCIA, VEHI_HIST_CONDUCTOR, VEHI_VALOR_DOMINIO |
| `vehi011.fmb` | Formulario | Detalle de gastos por tipo de salida (inferido) | DEPARTAMENTO, DETALLE_GASTO, DET_MANTENCION, SUBTIPO_GASTO, TIPO_SALIDA, UBICACION |
| `vehi012.fmb` | Formulario | Cursos de conductores (inferido) | AUSENCIAS, CONDUCTORES, CURSOS, CURSOS_CONDUCTORES, DEPARTAMENTO, INFRAC_CONDUCTORES, SINIE_CONDUCTORES, UBICACION, VEHI_CLASE_LICENCIA, VEHI_VALOR_DOMINIO |
| `vehi013.fmb` | Formulario | — | AUSENCIAS, CONDUCTORES, CURSOS, CURSOS_CONDUCTORES, DEPARTAMENTO, INFRAC_CONDUCTORES, MARCA_VEHI, MODELO_MARCA, SINIE_CONDUCTORES, UBICACION, VEHICULOS, VEHI_CLASE_LICENCIA, VEHI_SEGURO |
| `vehi014.fmb` | Formulario | Seguros Vehiculos | MESES, VEHICULOS, VEHI_PARAMETROS |
| `vehi015.fmb` | Formulario | Ficha de taller (inferido) | DEPARTAMENTO, LOCALIDAD, VEHICULOS, VEHI_DET_TALLER, VEHI_TALLER, VEHI_VALOR_DOMINIO |
| `vehi016.fmb` | Formulario | — | DEPARTAMENTO, MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, SOLICITUD_VEHICULO, TIPOS_VEHICULOS, VEHICULOS |
| `vehi017.fmb` | Formulario | Cierre de período | VEHI_CIERRE |
| `vehi019.fmb` | Formulario | — | VEHI_DOMINIO, VEHI_VALOR_DOMINIO |
| `vehi020.fmb` | Formulario | — | LOCALIDAD, VEHI_EMPRESA_CONV, VEHI_REPRESENTANTE_EMPRESA, VEHI_VALOR_DOMINIO |
| `vehi021.fmb` | Formulario | — | CONDUCTORES, DEPARTAMENTO, LOCALIDAD, UBICACION, VEHI_DET_CONEXT, VEHI_ENC_CONEXT |
| `vehi022.fmb` | Formulario | Orden de trabajo de mantención (inferido) | DEPARTAMENTO, LOCALIDAD, MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, TIPOS_VEHICULOS, VEHICULOS, VEHI_DET_MANTENCION, VEHI_ENC_MANTENCION, VEHI_TALLER, VEHI_VALOR_DOMINIO |
| `vehi022a.fmb` | Formulario | Emisión de orden de trabajo (inferido) | DEPARTAMENTO, LOCALIDAD, MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, TIPOS_VEHICULOS, VEHICULOS, VEHI_DET_MANTENCION, VEHI_DOMINIO, VEHI_ENC_MANTENCION, VEHI_TALLER, VEHI_VALOR_DOMINIO |
| `vehi023.fmb` | Formulario | Registro de factura de taller (inferido) | DEPARTAMENTO, MARCA_VEHI, MODELO_MARCA, TIPOS_VEHICULOS, VEHICULOS, VEHI_CIERRE, VEHI_DET_DCTO, VEHI_DOMINIO, VEHI_ENC_DCTO, VEHI_ENC_MANTENCION, VEHI_TALLER, VEHI_VALOR_DOMINIO |
| `vehi100.fmb` | Formulario | — | VEHICULOS |
| `vehi101.fmb` | Formulario | Ficha de vehículos (inferido) | CONDUCTORES, DEPARTAMENTO, DET_ORIGEN, INV_VEHICULO, MARCA_VEHI, MODELO_MARCA, TIPOS_VEHICULOS, TIPO_ORIGEN, TIPO_SALIDA, UBICACION, VEHICULOS, VEHI_DETALLE, VEHI_SEGURO, VEHI_VALOR_DOMINIO |
| `vehi102.fmb` | Formulario | Guarde de vehículos (inferido) | BITACORA, CONDUCTORES, DEPARTAMENTO, GUARDE_VEHICULO, LOCALIDAD, MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, SOLICITUD_VEHICULO, TARJETA_VEHICULO, UBICACION, VEHICULOS, VEHI_CIERRE, VEHI_VALOR_DOMINIO |
| `vehi103.fmb` | Formulario | — | DETALLE_GASTO, DETALLE_MANTENCION, MANTENCION_VEHICULO, MARCA_VEHI, MODELO_MARCA, SUBTIPO_GASTO, VEHICULOS |
| `vehi104.fmb` | Formulario | Selector de reportes | VEHICULOS |
| `vehi106.fmb` | Formulario | — | BITACORA, CONDUCTORES, DEPARTAMENTO, DET_MEMO, DET_MEMO_ACOMP, MEMORAMDUM, SALIDAS_VEHICULO, TIPOS_VEHICULOS, TIPO_SALIDA, UBICACION, VALES_COMBUST, VEHICULOS |
| `vehi106pdf.rdf` | Reporte | Ubicación de Vehículos | GUARDE_VEHICULO, MARCA_VEHI, MODELO_MARCA, UBICACION, VEHICULOS |
| `vehi107.fmb` | Formulario | — | BITACORA, MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, VEHICULOS |
| `vehi107.rdf` | Reporte | — | MARCA_VEHI, MODELO_MARCA, TIPOS_VEHICULOS, VEHICULOS, VEHI_DETALLE, VEHI_VALOR_DOMINIO |
| `vehi108.fmb` | Formulario | — | BITACORA, MOVIMIENTO_TARJETA_VEHICULO |
| `vehi108.rdf` | Reporte | Salidas a Terreno | DET_MEMO, LOCALIDAD, MEMORAMDUM, SALIDAS_VEHICULO, VEHICULOS |
| `vehi109.rdf` | Reporte | Ubicación de Vehículos al Término de la Jornada | GUARDE_VEHICULO, MARCA_VEHI, MODELO_MARCA, SOLICITUD_VEHICULO, UBICACION, VEHICULOS |
| `vehi110.rdf` | Reporte | — | DET_INVENTARIO, INV_VEHICULO, TIPOS_VEHICULOS, TIPO_INVENTARIO, VEHICULOS |
| `vehi111.rdf` | Reporte | DETALLE DE GASTOS | BITACORA, DET_MANTENCION, MANTENCION_VEHIC, SUBTIPO_GASTO, TIPO_GASTO, VEHICULOS |
| `vehi112.fmb` | Formulario | Accidentes de tránsito (inferido) | BITACORA, CONDUCTORES, DEPARTAMENTO, LOCALIDAD, MARCA_VEHI, MODELO_MARCA, TARJETA_VEHICULO, TIPOS_VEHICULOS, UBICACION, VEHICULOS, VEHI_ACCIDENTE, VEHI_DET_CONEXT, VEHI_ENC_CONEXT, VEHI_PASAJERO, VEHI_VALOR_DOMINIO |
| `vehi113.rdf` | Reporte | Gastos de mantención por mes (inferido) | DET_MANTENCION, MANTENCION_VEHIC, MESES, TIPO_GASTO, VEHICULOS |
| `vehi114.rdf` | Reporte | Resumen de gastos anual del pool de vehículos | DET_MANTENCION, MANTENCION_VEHIC, MESES, VEHICULOS |
| `vehi115.rdf` | Reporte | Informe de Conductores | CONDUCTORES, TIPO_CONDUCTOR, VEHICULOS, VEHI_CLASE_LICENCIA, VEHI_VALOR_DOMINIO |
| `vehi116.rdf` | Reporte | Informe de tarjetas por vehículo | MARCA_VEHI, MODELO_MARCA, TARJETA_VEHICULO, TIPOS_VEHICULOS, TIPO_ORIGEN, VEHICULOS |
| `vehi117.fmb` | Formulario | — | CONDUCTORES, DEPARTAMENTO, TIPO_CONDUCTOR |
| `vehi119.rdf` | Reporte | Resumen Gasto de Combustibles | MESES, VALES_COMBUST, VEHICULOS |
| `vehi120.rdf` | Reporte | Resumen Acumulado de Combustibles/Vales | BITACORA, MESES, VALES_COMBUST, VEHICULOS |
| `vehi121.rdf` | Reporte | Revisión Diaria de Vehículos | DET_ESTADO_DIA, TIPO_REVISION, VEHICULOS |
| `vehi122.RDF` | Reporte | Listado de vehículos por estado (inferido) | MARCA_VEHI, MODELO_MARCA, TIPOS_VEHICULOS, TIPO_ORIGEN, VEHICULOS |
| `vehi124.rdf` | Reporte | Resumen de Gastos de Combustible por Vehículo | MARCA_VEHI, MESES, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, TARJETA_VEHICULO, VEHICULOS |
| `vehi124pdf.rdf` | Reporte | Resumen de Gastos de Combustible por Vehículo | MARCA_VEHI, MESES, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, TARJETA_VEHICULO, VEHICULOS |
| `vehi125.rdf` | Reporte | Resumen de Consumo Combustible por Requerimiento/Vehículo | ESTACION_SERVICIO, MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, VEHICULOS |
| `vehi125_pp.rdf` | Reporte | Resumen de Gastos Presupuestario | DEPARTAMENTO, ESTACION_SERVICIO, MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, VEHICULOS |
| `vehi126.rdf` | Reporte | Resumen Gastos Presupuestario | MOVIMIENTO_TARJETA_VEHICULO, VEHICULOS |
| `vehi126_ppt.rdf` | Reporte | Resumen Gastos Presupuestario | MOVIMIENTO_TARJETA_VEHICULO, VEHICULOS |
| `vehi127.RDF` | Reporte | Operatividad mensual del vehículo | GUARDE_VEHICULO, MARCA_VEHI, MODELO_MARCA, TIPO_ORIGEN, UBICACION, VEHICULOS |
| `vehi127pdf.RDF` | Reporte | Operatividad mensual del vehículo (PDF) | GUARDE_VEHICULO, MARCA_VEHI, MODELO_MARCA, TIPO_ORIGEN, UBICACION, VEHICULOS |
| `vehi128.rdf` | Reporte | Rendimiento por vehículo según bitácora (inferido) | BITACORA, COMPANIA_BENCINA, ESTACION_SERVICIO, LOCALIDAD, MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, VEHICULOS, VEHI_ENC_CONEXT |
| `vehi129.rdf` | Reporte | Ficha del conductor | CONDUCTORES, CURSOS, CURSOS_CONDUCTORES, INFRAC_CONDUCTORES, VEHICULOS, VEHI_ACCIDENTE, VEHI_CLASE_LICENCIA, VEHI_VALOR_DOMINIO |
| `vehi130.rdf` | Reporte | — | CONDUCTORES, DET_ORIGEN, LOCALIDAD, MARCA_VEHI, MODELO_MARCA, SOLICITUD_VEHICULO, TARJETA_VEHICULO, TIPOS_VEHICULOS, TIPO_CONDUCTOR, TIPO_SALIDA, VEHICULOS, VEHI_ENC_CONEXT, VEHI_PASAJERO, VEHI_SEGURO |
| `vehi131.RDF` | Reporte | Resumen De Rendimiento por Vehículo | MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, VEHICULOS |
| `vehi131pdf.rdf` | Reporte | Resumen por Kilometraje - Consumo Combustible y Rendimiento | DEPARTAMENTO, MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, VEHICULOS |
| `vehi132.rdf` | Reporte | Revisión Técnica por Vehículo | MARCA_VEHI, MODELO_MARCA, TIPOS_VEHICULOS, VEHICULOS, VEHI_PARAMETROS |
| `vehi132pdf.rdf` | Reporte | Revisión Técnica por Vehículo | MARCA_VEHI, MODELO_MARCA, TIPOS_VEHICULOS, VEHICULOS, VEHI_PARAMETROS |
| `vehi133.rdf` | Reporte | Revisión Técnica por Vehículo | MARCA_VEHI, MODELO_MARCA, TIPOS_VEHICULOS, VEHICULOS |
| `vehi134.rdf` | Reporte | Detalle de ingreso de gastos por tipo de documento | INGRESO_GASTO, MARCA_VEHI, MODELO_MARCA, TIPOS_VEHICULOS, VEHICULOS |
| `vehi135.rdf` | Reporte | Resumen de Gastos por Presupuesto | MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, SOLICITUD_VEHICULO, VEHICULOS |
| `vehi136.rdf` | Reporte | Informe de centros financieros cerrados | VEHICULOS, VEHI_CIERRE |
| `vehi137.fmb` | Formulario | Ingreso de gastos del vehículo (inferido) | BITACORA, CONDUCTORES, DEPARTAMENTO, INGRESO_GASTO, LOCALIDAD, MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, TARJETA_VEHICULO, TIPOS_VEHICULOS, UBICACION, VEHICULOS, VEHI_CIERRE |
| `vehi138.rdf` | Reporte | Gastos rechazados (inferido) | INGRESO_GASTO, MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, VEHICULOS |
| `vehi139.rdf` | Reporte | Chequeo entre Solicitud de las Salidas y Movimiento de Combustible | MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, SOLICITUD_VEHICULO, TIPO_SALIDA, VEHICULOS, VEHI_PARAMETROS |
| `vehi140.rdf` | Reporte | Ficha Conductor | CONDUCTORES, DEPARTAMENTO, INFRAC_CONDUCTORES, VEHICULOS, VEHI_CLASE_LICENCIA, VEHI_VALOR_DOMINIO |
| `vehi141.rdf` | Reporte | Comunas por provincia y región (inferido) | LOCALIDAD, VEHICULOS |
| `vehi142.RDF` | Reporte | Listado de Cursos por Conductores | CONDUCTORES, CURSOS, CURSOS_CONDUCTORES, VEHICULOS, VEHI_VALOR_DOMINIO |
| `vehi143.RDF` | Reporte | Póliza por Vehículo | MARCA_VEHI, MODELO_MARCA, VEHICULOS, VEHI_SEGURO |
| `vehi144Pdf.rdf` | Reporte | Operatividad mensual SIGI (inferido) | GUARDE_VEHICULO, MARCA_VEHI, MODELO_MARCA, TIPO_ORIGEN, UBICACION, VEHICULOS |
| `vehi145.rdf` | Reporte | Compañia de Combustibles y Estaciones de Servicio Asociadas | COMPANIA_BENCINA, ESTACION_SERVICIO, LOCALIDAD |
| `vehi146.rdf` | Reporte | Orden de trabajo de mantención (inferido) | LOCALIDAD, MARCA_VEHI, MODELO_MARCA, VEHICULOS, VEHI_DET_MANTENCION, VEHI_DOMINIO, VEHI_ENC_MANTENCION, VEHI_TALLER, VEHI_VALOR_DOMINIO |
| `vehi146a.rdf` | Reporte | IDENTIFICACION DEL TALLER | LOCALIDAD, MARCA_VEHI, MODELO_MARCA, VEHICULOS, VEHI_DET_MANTENCION, VEHI_DOMINIO, VEHI_ENC_MANTENCION, VEHI_TALLER, VEHI_VALOR_DOMINIO |
| `vehi147.rdf` | Reporte | Análisis de pago de factura de taller (inferido) | MARCA_VEHI, MODELO_MARCA, TIPOS_VEHICULOS, VEHICULOS, VEHI_DET_DCTO, VEHI_DET_TALLER, VEHI_DOMINIO, VEHI_ENC_DCTO, VEHI_TALLER, VEHI_VALOR_DOMINIO |
| `vehi203.fmb` | Formulario | Selector de reportes de vales de combustible (inferido) | BITACORA, DEPARTAMENTO, UBICACION, VALES_COMBUST, VEHICULOS |
| `vehi204.fmb` | Formulario | Vales de combustible por conductor (inferido) | CONDUCTORES, DEPARTAMENTO, UBICACION, VALES_COMBUST, VEHICULOS |
| `vehi205.fmb` | Formulario | — | BITACORA, CONDUCTORES, DEPARTAMENTO, DET_MEMO, MEMORAMDUM, UBICACION, VALES_COMBUST, VEHICULOS |
| `vehi206.fmb` | Formulario | Modificación de Bitácora | BITACORA, DEPARTAMENTO, UBICACION, VALES_COMBUST, VEHICULOS |
| `vehi207.fmb` | Formulario | Proceso Bitacora | BITACORA, DEPARTAMENTO, UBICACION, VALES_COMBUST, VEHICULOS |
| `vehi300.fmb` | Formulario | Mantenimiento de Acceso a  Centros Financieros por Usuario | DEPARTAMENTO |
| `vehi301.fmb` | Formulario | — | BITACORA, COMPANIA_BENCINA, ESTACION_SERVICIO |
| `vehi302.fmb` | Formulario | — | BITACORA, COMPANIA_BENCINA, ESTACION_SERVICIO, LOCALIDAD, MOVIMIENTO_TARJETA_VEHICULO |
| `vehi303.fmb` | Formulario | — | BITACORA, DEPARTAMENTO, MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, TARJETA_VEHICULO, UBICACION, VEHICULOS |
| `vehi304.fmb` | Formulario | — | BITACORA, COMPANIA_BENCINA, CONDUCTORES, DEPARTAMENTO, ESTACION_SERVICIO, LOCALIDAD, MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, SOLICITUD_VEHICULO, TARJETA_VEHICULO, TIPO_SALIDA, UBICACION, VEHICULOS, VEHI_CIERRE, VEHI_DET_CONEXT, VEHI_ENC_CONEXT |
| `vehi305.fmb` | Formulario | Carga de archivo COPEC | BITACORA, CONDUCTORES, DEPARTAMENTO, ESTACION_SERVICIO, LOCALIDAD, MOVIMIENTO_TARJETA_VEHICULO, TARJETA_VEHICULO, VEHICULOS |
| `vehi306.fmb` | Formulario | — | BITACORA, DEPARTAMENTO, MOVIMIENTO_TARJETA_VEHICULO, TARJETA_VEHICULO |
| `vehi307.fmb` | Formulario | Consulta de combustible por vehículo (inferido) | BITACORA, COMPANIA_BENCINA, CONDUCTORES, DEPARTAMENTO, ESTACION_SERVICIO, LOCALIDAD, MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, SOLICITUD_VEHICULO, TARJETA_VEHICULO, TIPO_SALIDA, UBICACION, VEHICULOS, VEHI_ENC_CONEXT |
| `vehi308.fmb` | Formulario | Solicitud de la Salida | BITACORA, COMPANIA_BENCINA, CONDUCTORES, DEPARTAMENTO, ESTACION_SERVICIO, LOCALIDAD, MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, SOLICITUD_VEHICULO, TARJETA_VEHICULO, TIPO_SALIDA, UBICACION, VEHICULOS, VEHI_CIERRE, VEHI_DET_CONEXT, VEHI_ENC_CONEXT |
| `vehi309.fmb` | Formulario | — | DEPARTAMENTO, DETALLE_GASTO, MARCA_VEHI, MODELO_MARCA, UBICACION, VEHICULOS |
| `vehi310.fmb` | Formulario | Selección de centro financiero | VEHICULOS |
| `vehi311.fmb` | Formulario | Ingreso de solicitudes (inferido) | BITACORA, CONDUCTORES, DEPARTAMENTO, LOCALIDAD, MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, SOLICITUD_VEHICULO, TARJETA_VEHICULO, TIPOS_VEHICULOS, TIPO_SALIDA, UBICACION, VEHICULOS, VEHI_CIERRE, VEHI_DET_CONEXT, VEHI_ENC_CONEXT, VEHI_PASAJERO, VEHI_SEGURO |
| `vehi312.fmb` | Formulario | Consulta de salidas del día (inferido) | BITACORA, CONDUCTORES, DEPARTAMENTO, LOCALIDAD, MARCA_VEHI, MODELO_MARCA, SOLICITUD_VEHICULO, TARJETA_VEHICULO, TIPOS_VEHICULOS, TIPO_CONDUCTOR, TIPO_SALIDA, UBICACION, VEHICULOS, VEHI_DET_CONEXT, VEHI_ENC_CONEXT |
| `vehi313.fmb` | Formulario | Consulta por conductor (inferido) | BITACORA, CONDUCTORES, DEPARTAMENTO, LOCALIDAD, MARCA_VEHI, MODELO_MARCA, SOLICITUD_VEHICULO, TARJETA_VEHICULO, TIPOS_VEHICULOS, TIPO_CONDUCTOR, TIPO_SALIDA, UBICACION, VEHICULOS, VEHI_ENC_CONEXT |
| `vehi314.fmb` | Formulario | Centro Financiero del Vehículo | BITACORA, COMPANIA_BENCINA, CONDUCTORES, DEPARTAMENTO, ESTACION_SERVICIO, LOCALIDAD, MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, SOLICITUD_VEHICULO, TARJETA_VEHICULO, TIPOS_VEHICULOS, TIPO_SALIDA, UBICACION, VEHICULOS, VEHI_BITACORA |
| `vehi315.fmb` | Formulario | Consulta por pasajeros para viático (inferido) | BITACORA, CONDUCTORES, DEPARTAMENTO, LOCALIDAD, MARCA_VEHI, MODELO_MARCA, SOLICITUD_VEHICULO, TARJETA_VEHICULO, TIPOS_VEHICULOS, TIPO_SALIDA, UBICACION, VEHICULOS, VEHI_ENC_CONEXT, VEHI_PASAJERO |
| `vehi316.fmb` | Formulario | Consulta de salidas por pasajeros (inferido) | BITACORA, CONDUCTORES, DEPARTAMENTO, LOCALIDAD, MARCA_VEHI, MODELO_MARCA, SOLICITUD_VEHICULO, TARJETA_VEHICULO, TIPOS_VEHICULOS, TIPO_CONDUCTOR, TIPO_SALIDA, UBICACION, VEHICULOS, VEHI_ENC_CONEXT, VEHI_PASAJERO |
| `vehi317.fmb` | Formulario | — | BITACORA, COMPANIA_BENCINA, CONDUCTORES, DEPARTAMENTO, ESTACION_SERVICIO, LOCALIDAD, MOVIMIENTO_TARJETA_VEHICULO, SOLICITUD_VEHICULO, TARJETA_VEHICULO, TIPO_SALIDA, UBICACION, VEHICULOS, VEHI_CIERRE |
| `vehi318.fmb` | Formulario | — | BITACORA, COMPANIA_BENCINA, CONDUCTORES, DEPARTAMENTO, ESTACION_SERVICIO, LOCALIDAD, MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, SOLICITUD_VEHICULO, TARJETA_VEHICULO, TIPOS_VEHICULOS, TIPO_SALIDA, UBICACION, VEHICULOS, VEHI_CIERRE, VEHI_DIST_GRANEL |
| `vehi319.fmb` | Formulario | Movimiento diario de vehículo (kilometraje de salida y regreso) | BITACORA, CONDUCTORES, DEPARTAMENTO, LOCALIDAD, MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_DIARIO_VEHICULO, MOVIMIENTO_TARJETA_VEHICULO, SOLICITUD_VEHICULO, TARJETA_VEHICULO, TIPOS_VEHICULOS, TIPO_SALIDA, UBICACION, VEHICULOS, VEHI_CIERRE, VEHI_DET_CONEXT, VEHI_ENC_CONEXT, VEHI_GUARDIA, VEHI_PASAJERO |
| `vehi320.fmb` | Formulario | Personal que registra los Movimientos Diarios de los Vehículos | DEPARTAMENTO, UBICACION, VEHI_GUARDIA |
| `vehi401.fmb` | Formulario | Consumo de combustible anual por vehículo (inferido) | MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, TARJETA_VEHICULO, TIPOS_VEHICULOS, VEHICULOS |
| `vehi402.fmb` | Formulario | Consumo de combustible por requerimiento (inferido) | MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, TIPOS_VEHICULOS, VEHICULOS |
| `vehi403.fmb` | Formulario | Consumo de combustible por proyecto (inferido) | MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, TIPOS_VEHICULOS, VEHICULOS |
| `vehi404.fmb` | Formulario | — | INGRESO_GASTO, MARCA_VEHI, MODELO_MARCA, MOVIMIENTO_TARJETA_VEHICULO, TIPOS_VEHICULOS, VEHICULOS |
| `vehi405.fmb` | Formulario | Carga de archivo COPEC (versión alternativa) | BITACORA, CONDUCTORES, DEPARTAMENTO, ESTACION_SERVICIO, LOCALIDAD, MOVIMIENTO_TARJETA_VEHICULO, TARJETA_VEHICULO, VEHICULOS |

## 3. Tablas que ningún programa usa

`DET_OTROS_ACOMP`, `DOC_VEHICULO`, `ESTADO_VEHIC_DIA`, `LOCALIDAD_NEW`, `LOCALIDAD_OLD`, `MANT_POR_KM`, `VEHI_COMPRA_GRANEL`, `VEHI_MOV_GPS`. Son candidatas a no migrar, salvo `ESTADO_VEHIC_DIA` (historial 1980-2005) si se requiere conservarlo.
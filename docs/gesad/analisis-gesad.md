# Análisis de GESAD, el sistema actual de gestión de vehículos

Unidad de Información y Análisis (UIA) · 28-10-2026 · Versión pública

Este análisis se hizo sobre el respaldo de la base de datos, el código fuente y el menú de GESAD. Los entregó el Departamento de Informática en respuesta al Memorándum N° 5772/2026 (19-10-2026). Su objetivo es conocer la solución existente antes de diseñar el Sistema Nacional de Gestión de Flota.

Esta versión no contiene registros ni datos personales. El respaldo y los datos extraídos se conservan sólo en el entorno de trabajo de la UIA. La versión interna, con el detalle técnico completo, está en el proyecto UIA.

Documentos relacionados:
- [Diccionario de datos](diccionario-datos.md): las 77 tablas con sus columnas, tipos, claves y número de filas.
- [Inventario de programas](inventario-programas.md): el menú y los 108 formularios y reportes.
- [Lector del respaldo](../../herramientas/README.md): el script que convierte el respaldo a tablas CSV.

## 1. Material recibido

| Material | Estado de la revisión |
|---|---|
| Respaldo de la base de datos (export Oracle 9.2 del 22-10-2026, 163 MB) | Leído completo: 77 tablas, 1 vista y cerca de 1,3 millones de registros |
| Código fuente: 66 formularios Oracle Forms y 42 reportes Oracle Reports | Revisado leyendo el texto de los archivos (títulos, mensajes y consultas SQL) |
| Menú del sistema | Revisado: 9 menús principales y unas 90 opciones |
| Documentación (modelo de datos, manuales) | No se recibió |

## 2. Qué es GESAD

GESAD es una aplicación de escritorio construida en Oracle Forms y Reports, con base de datos Oracle 9.2. Su alcance es nacional: cada registro se asocia a un **centro financiero**, y el respaldo registra vehículos en 45 códigos distintos. Los vehículos de Oficina Central usan el código N1 (dato inferido, porque 20 de los 21 vehículos de la planilla de la Unidad de Vehículos tienen ese código).

El menú tiene nueve módulos:
- Parámetros
- Vehículos y conductores
- Salidas de vehículos
- Combustible
- Reportes
- Archivos
- Mantenciones
- Cierre de período
- Accesos

El menú se compiló en 2009 y su última modificación es de diciembre de 2011. Los comentarios del código registran cambios entre 2004 y 2010.

## 3. Uso real del sistema

| Registro | Cantidad | Periodo con datos | Lectura |
|---|---:|---|---|
| Solicitudes de vehículo | 137.020 | 2004 a 22-10-2026 | Es el único módulo vivo, en descenso: 11.522 en 2013 y 1.798 en 2026 (a octubre) |
| Acompañantes por solicitud | 78.596 | — | Se registran porque los usa el sistema de viáticos (ver punto 4) |
| Guarde diario de vehículos | 666.239 | 2007 a marzo de 2026 | Libro de guardia con kilometraje, combustible y ubicación. Sin registros desde abril de 2026 |
| Cargas de combustible con tarjeta | 334.225 | 2003 a marzo de 2019 | Sin registros desde 2019 |
| Órdenes de mantención | 335 | 2011 a mayo de 2023 | Sin registros desde 2023 |
| Vehículos registrados | 3.608 | — | Incluye motos, motobombas, motosierras, generadores y tractores |
| Conductores | 2.363 | — | Con licencia, caución, cursos, infracciones y accidentes |

Otras observaciones:
- En 2026 sólo ocho centros financieros registran solicitudes.
- Ninguna de las solicitudes de 2026 tiene registrado el kilometraje de salida ni el de regreso.
- La operación diaria ya se lleva en planillas, como mostraron los antecedentes de la Unidad de Vehículos.

## 4. Dependencias que deben resolverse antes de apagar GESAD

1. **Viáticos.** El menú tiene la opción «Consulta por pasajeros para viático», y el sistema de viáticos tiene permiso para leer las solicitudes, los acompañantes y los tipos de salida de GESAD. Si GESAD deja de operar sin un reemplazo de esa conexión, el cálculo de viáticos pierde su fuente de información sobre los cometidos. **Es el riesgo principal del cierre a fin de año.**
2. **Catálogo de localidades.** La tabla de comunas, provincias y regiones de GESAD la leen otros diez sistemas institucionales. Hay que mantenerla o trasladarla.
3. **Datos que GESAD toma de otros sistemas.** Los nombres de funcionarios, los programas presupuestarios, los centros financieros, los usuarios y las pólizas de seguro provienen de otros sistemas institucionales. Esos datos no vienen en el respaldo: conductores y solicitantes aparecen sólo con su número interno de funcionario.

## 5. Datos personales y sensibles (Ley N° 21.719)

El respaldo contiene:
- Datos de identificación de funcionarios: RUT y número interno.
- Antecedentes de conducción: licencias, infracciones y accidentes.
- Un dato de salud de los conductores.
- Credenciales de tarjetas de combustible.

Criterios adoptados por la UIA:
- El respaldo **no se versiona** en este ni en otro repositorio.
- Los datos extraídos se trabajan sólo en el entorno de la UIA.
- El dato de salud y las credenciales **no se migran** al nuevo sistema.

## 6. Calidad de los datos

- **Fechas imposibles** en varias tablas (años 201, 3013, 8201 o 2999), producto de digitación sin validación.
- **Vencimientos desactualizados.** Las fechas de revisión técnica no coinciden con la planilla vigente de la Unidad de Vehículos; por ejemplo, FXHB-90 figura con revisión técnica al 08-10-2025 en GESAD y al 21-10-2026 en la planilla.
- **Estados sin catálogo.** El campo de estado del vehículo usa los códigos A, B, C, I y T. Su significado no está documentado y debe confirmarse con Informática.
- **Vehículo faltante.** VGXF-75 (vehículo arrendado) no existe en GESAD.
- **Integridad no declarada.** La base declara pocas claves foráneas; la integridad la controlaban los formularios.

## 7. Funciones de GESAD que el requerimiento actual no menciona

El ERS de la Unidad de Vehículos (INF-LOG-TI-2026-V1) no contempla estas funciones, que GESAD sí tiene. Se propone revisarlas con la contraparte:

- Cursos de conductores (manejo defensivo, primeros auxilios, conducción en alta montaña).
- Infracciones de tránsito con catálogo de la Ley de Tránsito y gravedad.
- Registro de accidentes con tipo y causa.
- Historial de cambio de conductor asignado.
- Inventario de accesorios del vehículo (extintor, botiquín, triángulos).
- Libro de guardia diario.
- Compras de combustible a granel y su distribución.
- Carga del archivo de COPEC.
- Cierre mensual por centro financiero.
- Tipos de salida urbana, a terreno, internacional y urbana permanente.

## 8. Antecedentes pendientes

Se solicitarán al Departamento de Informática:

1. El catálogo de centros financieros y el significado de los códigos de estado.
2. Los nombres de los funcionarios que aparecen en GESAD, limitados a los números internos presentes en el respaldo.
3. La confirmación de qué información usa el sistema de viáticos y quién es su responsable.
4. El fuente del formulario `vehi007` (tipos de origen de vehículos), que el menú llama y no viene en la entrega.
5. La documentación técnica o el manual de usuario, si existen.

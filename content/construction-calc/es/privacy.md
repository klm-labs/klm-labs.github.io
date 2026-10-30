# Aviso de privacidad de Calculadora de Pies y Pulgadas

**Fecha de entrada en vigor:** 30 de octubre de 2026

**Contacto:** [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com)

Calculadora de Pies y Pulgadas (Fraction Feet Inch Calculator) es una app de KLM Labs. En tu pantalla de inicio aparece como **Construction Calculator**. Hace cuentas con pies, pulgadas y fracciones, y cálculos de construcción en tu iPhone o iPad. Este aviso explica qué se queda en tu dispositivo, qué sale de él, quién lo recibe y para qué.

## En resumen

- **Tus cálculos se guardan en tu dispositivo.** Los números que escribes, los resultados, tu historial, los datos de las herramientas y el último resultado del widget de la pantalla de inicio se guardan en tu dispositivo. Ningún evento de estadísticas los contiene, pero desde la versión 1.0.2 las grabaciones de pantalla de más abajo muestran los números de la calculadora, sus resultados y tu historial.
- **Iniciar sesión es opcional.** Desde la versión 1.2.0 puedes iniciar sesión con Apple o Google para que KLM Labs pueda escribirte sobre la app. La app funciona igual sin una cuenta. Si inicias sesión, recibimos tu correo y, si lo compartes, tu nombre, y se guardan en Google Firebase (consulta "Iniciar sesión con Apple o Google"). Tus registros de uso y de compra se mantienen juntos mediante identificadores aleatorios, así que están vinculados a ti (consulta más abajo).
- **Estadísticas de uso con un identificador aleatorio.** La versión del App Store envía a PostHog eventos de uso, como "se abrió una herramienta", junto con datos técnicos de la app y del dispositivo, y desde la versión 1.1.0 un reporte cuando la app falla. A partir de tu dirección de internet, que PostHog no guarda, se calcula una ubicación aproximada (país y ciudad). Ningún evento incluye un cálculo, un dato que escribiste ni un resultado.
- **Grabaciones de pantalla, desde la versión 1.0.2.** La versión del App Store también graba las pantallas de la app mientras la usas y dónde tocas. Las grabaciones muestran las palabras y los números propios de la app, también la calculadora; las casillas donde escribes en las herramientas se enmascaran en tu dispositivo (consulta más abajo).
- **Apple procesa los pagos.** Nunca vemos los datos de tu tarjeta ni de tu banco. RevenueCat recibe tus registros de compra del App Store para que la app pueda activar y restaurar tu plan.
- **Sin anuncios y sin rastreo.** No vendemos datos, no mostramos anuncios, no usamos el identificador de publicidad y no te rastreamos en otras apps ni sitios web.

## Lo que se guarda en tu dispositivo

Todo lo que escribes y calculas se guarda en tu dispositivo: los números y operaciones que escribes, los resultados, la memoria, el historial, la precisión y demás ajustes, los últimos datos de cada herramienta y el último resultado que muestra el widget. La app y su widget comparten ese último resultado a través del almacenamiento de tu dispositivo. Ningún evento de estadísticas ni registro de compra contiene nada de esto, y no podemos recuperarlo ni borrarlo. Pero desde la versión 1.0.2, las grabaciones de pantalla que se describen en "Una grabación de las pantallas de la app" muestran los números de la calculadora, sus resultados y tu historial tal como aparecen en pantalla. Fuera de eso, solo sale de tu dispositivo si lo compartes: puedes compartir tu historial o una línea, copiar un resultado en otra app o compartir el PDF del trazo de una escalera. Como otros datos de apps, se incluye en los respaldos de tu dispositivo (respaldo en iCloud o en una computadora) si los tienes activados; esos respaldos dependen de Apple y de tu configuración, no de nosotros.

La calculadora y las herramientas funcionan sin internet. Copiar y pegar usan el portapapeles de tu dispositivo solo cuando eliges Copiar o Pegar.

## Iniciar sesión con Apple o Google

Desde la versión 1.2.0 la app ofrece iniciar sesión con Apple o Google: en una página antes de la pantalla de planes, a lo mucho una vez más en la pantalla de la calculadora y cuando quieras en **Configuración → Cuenta**. Iniciar sesión es opcional. Toca **Ahora no** para omitirlo; todas las funciones, las compras y la prueba gratis funcionan igual sin una cuenta.

**Lo que recibimos.** Si inicias sesión, Apple o Google le da a la app tu correo y, si lo compartes, tu nombre. Nunca tienes que escribirlos. Si inicias sesión con Apple y eliges **Ocultar mi correo electrónico** (Hide My Email), recibimos la dirección de reenvío privada de Apple en lugar de la tuya.

**Dónde se guarda.** Tu correo y tu nombre se guardan en Google Firebase Authentication, en un proyecto que administra KLM Labs; Google los procesa por nosotros. Firebase también guarda si usaste Apple o Google, y cuándo iniciaste sesión por primera y por última vez. No hay un respaldo aparte. Apple o Google se encarga del inicio de sesión según su propio aviso de privacidad.

**Para qué.** Solo para que KLM Labs (Mayank, quien hace la app) pueda escribirte sobre la app: si algo falla o para saber qué opinas. Nunca vendemos tu correo ni tu nombre, y nunca los usamos para anuncios.

**Quién nunca lo recibe.** Tu correo y tu nombre nunca se envían a PostHog ni a RevenueCat. RevenueCat recibe solo un ID de cuenta aleatorio que relaciona tus compras con tu cuenta, y si la app viene del App Store o de TestFlight. RevenueCat pasa ese ID de cuenta a PostHog junto con los eventos de compra que se describen más abajo, así que podemos relacionar esos eventos con tu cuenta.

**Nuestra lista.** Para ver desde qué app iniciaste sesión y si tienes un plan, KLM Labs puede exportar la lista de Firebase, junto con los registros de compra de RevenueCat, a un solo archivo. Cada exportación reemplaza a la anterior. Es la única otra copia.

**Eliminar tu cuenta.** En la app, abre **Configuración → Cuenta → Eliminar mi cuenta** y confirma. La app te pide confirmar con Apple o Google una vez más y luego elimina tu cuenta de Firebase. Si iniciaste sesión con Apple, también revoca el acceso de la app a tu cuenta de Apple; si ese paso falla, la app te lo dice y puedes quitar la app en Iniciar sesión con Apple, en la configuración de tu cuenta de Apple. Si iniciaste sesión con Google, desconecta la app de tu cuenta de Google. También quita el ID de cuenta de tu registro de compra en RevenueCat y los datos de inicio de sesión guardados en tu dispositivo. Eliminar tu cuenta no cancela una suscripción, y tus cálculos y tu historial se quedan en tu dispositivo. Eliminar la app no elimina tu cuenta. También puedes escribir a [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com) y la eliminaremos.

## Estadísticas de uso (PostHog)

Usamos estadísticas de uso para saber qué funciones se usan y dónde se atoran las personas, y así mejorar la app. [PostHog, Inc.](https://posthog.com/privacy) procesa las estadísticas para KLM Labs en servidores de Estados Unidos. Las estadísticas, y desde la versión 1.0.2 las grabaciones de pantalla, solo las envía la versión del App Store (y las versiones de prueba de TestFlight); la app no tiene un ajuste para ellas.

### Qué recopilan las estadísticas

**Eventos que describen lo que hiciste, nunca lo que calculaste.** La app envía estos eventos: se abrió la app; se terminó un cálculo; se abrió una herramienta (cuál); se envió un resultado de una herramienta a la calculadora (de cuál); se compartió el PDF del trazo de una escalera; se abrió una guía (cuál); se abrió la app desde el widget (con qué atajo); se mostró la página del recordatorio de la prueba gratis y si permitiste las notificaciones; se mostró la pantalla de planes (desde dónde se abrió y qué conjunto de planes mostró); y el resultado de una compra o restauración (qué plan, Anual o De por vida, si empezó una prueba gratis y si se completó, se canceló, falló o está esperando aprobación). Desde la versión 1.1.0 también envía: cuánto tiempo estuvo abierta una página de bienvenida, la página del recordatorio de la prueba gratis o la pantalla de planes y cómo saliste de ella (siguiente, atrás o la app pasó a segundo plano); que un valor en una casilla de una herramienta no se pudo usar al salir de la casilla (qué herramienta, qué casilla y por qué, como vacía o fuera de rango; nunca lo que escribiste); qué plan elegiste en la pantalla de planes y que tocaste para comprarlo (qué plan y desde dónde); cuánto tiempo después de instalar la app hiciste tu primer cálculo; para la pantalla de planes, también su moneda, su versión y si puedes obtener la prueba gratis; para una compra cancelada, cuánto tiempo estuvo abierta la hoja de compra de Apple; para una fallida, el tipo de falla y el código de error del App Store; para cada compra o restauración, si ocurrió en el entorno de prueba de Apple; y, si la app no puede abrir el almacenamiento que guarda tu historial en tu dispositivo, qué paso falló y el código de error del sistema, nunca lo que contiene tu historial. Desde la versión 1.2.0 también envía eventos sobre el inicio de sesión, nunca tu correo ni tu nombre: que se mostró la página para iniciar sesión, la tarjeta para iniciar sesión en la pantalla de la calculadora o la sección Cuenta en Configuración; que iniciaste sesión, lo omitiste, lo cancelaste o que falló (con el tipo de falla, como sin conexión); si elegiste Apple o Google; si Apple dio una dirección de reenvío privada y si llegó un correo; y que eliminaste tu cuenta, o que no se pudo eliminar (y por qué). El software de estadísticas también envía un evento cuando tocas varias veces seguidas el mismo lugar (en qué pantalla y en qué punto). **Ningún evento contiene un número, una operación, un dato que escribiste ni un resultado de un cálculo.**

**Datos técnicos** que el software de estadísticas agrega a cada evento: el nombre, la versión y la compilación de la app; la marca, el modelo y el tipo de dispositivo; la versión de iOS o iPadOS; el tamaño de la pantalla; tu idioma, región y zona horaria; si el dispositivo usa Wi-Fi o datos móviles; si la app viene de TestFlight; el nombre y la versión del software de estadísticas; la hora del evento; e identificadores aleatorios del evento y de la sesión. También incluyen el identificador de paquete de la app, el nombre del sistema operativo, el nombre genérico del dispositivo que informa iOS (como "iPhone" o "iPad") y si la app se ejecuta en un simulador o se instaló desde fuera del App Store. Desde la versión 1.1.0, cada evento también lleva el país del App Store, el primer idioma de tu dispositivo, tu tamaño de texto y desde dónde se instaló la app (el App Store o TestFlight).

**Un identificador aleatorio** que PostHog crea en tu dispositivo. Le permite a PostHog contar los eventos de una misma instalación. No es tu nombre, tu correo, tu teléfono, tu cuenta de Apple ni el identificador de publicidad del dispositivo. La app también se lo da a RevenueCat, para relacionar tu uso con tus compras (consulta más abajo). Si inicias sesión, también se puede relacionar con tu cuenta mediante el ID de cuenta que se describe en "Iniciar sesión con Apple o Google".

**Una ubicación aproximada.** Como cualquier servicio de internet, PostHog ve la dirección IP desde la que se conecta tu dispositivo. PostHog usa esa dirección IP para estimar un país y una ciudad cuando llegan los eventos, y está configurado para descartarla en lugar de guardarla con los eventos. **La app no pide permiso de ubicación y nunca lee el GPS de tu dispositivo.**

**Eventos de compra.** Cuando empiezas una prueba, compras, renuevas, cancelas o cuando un plan vence, RevenueCat envía a PostHog un registro de ese evento (por ejemplo, el producto, su precio, el ID de usuario de RevenueCat y el ID de transacción de Apple) con el mismo identificador aleatorio, para que podamos ver cómo se usan los planes. Desde la versión 1.2.0, si inicias sesión, estos registros también llevan tu ID de cuenta aleatorio. Consulta "Compras y suscripciones" más abajo.

**Una grabación de las pantallas de la app, desde la versión 1.0.2.** Para ver dónde tocan las personas, qué se les dificulta y dónde se rinden, la app graba sus pantallas mientras la usas: capturas de las pantallas de la propia app, tomadas cuando cambian, y los lugares donde tocas. Una grabación puede incluir cualquier pantalla de la app. Comprobamos lo que muestra en una grabación real de la versión 1.0.2: las páginas de bienvenida, la pantalla de planes, una compra, la calculadora, las herramientas Escaleras y Concreto, y el Historial. En iPad comprobamos una grabación de la versión 1.1.0: la calculadora con el Historial al lado, una herramienta y Configuración.

| En una grabación | Qué muestra |
|---|---|
| Se lee | Las palabras y los números propios de la app: títulos, botones, etiquetas, nombres y precios de los planes, la pantalla de la calculadora (lo que escribiste y el resultado), los resultados de las herramientas, tu historial, la fracción que eliges en el menú de una herramienta y un consejo que aparece sobre una herramienta |
| Se enmascara | Cada casilla donde escribes en las herramientas: la cubre un bloque sólido, así que los números que escribes ahí no se ven (los resultados que se calculan con ellos, sí). Desde la versión 1.2.0, también el correo que muestra Configuración cuando tienes la sesión iniciada. |
| Tus toques | Dónde tocas. En el teclado de la calculadora, los toques muestran qué teclas presionaste |
| No aparece | El teclado, que no es parte de la pantalla de la app; las solicitudes propias de iOS, como la que pide permitir notificaciones, tampoco aparecieron en nuestras grabaciones |

La app no muestra fotos; su logotipo y sus símbolos son figuras dibujadas y siguen visibles.

Una grabación lleva el mismo identificador aleatorio y el mismo identificador de sesión que tus eventos de estadísticas, así que está vinculada a ti de la misma manera. No se graban los mensajes de la consola ni la actividad de red. Tratamos cualquier cambio en lo que una grabación muestra o enmascara como un cambio a este aviso.

**Reportes de fallas, desde la versión 1.1.0.** Si la app falla y se cierra, guarda un reporte en tu dispositivo y lo envía a PostHog la próxima vez que la abres. El reporte dice qué salió mal y en qué parte del código de la app ocurrió (en algunas fallas, el mensaje de error), con los mismos datos técnicos e identificadores que tus eventos de estadísticas, así que está vinculado a ti de la misma manera. La app no pone en él tus cálculos, los datos que escribes ni tus resultados. Usamos los reportes de fallas solo para encontrar y corregir fallas, no para las estadísticas de uso.

### Qué nunca recopilan las estadísticas

Las estadísticas nunca recopilan tu nombre, correo, teléfono, contactos, fotos, archivos ni ubicación precisa. Si inicias sesión, tu correo y tu nombre van a Google Firebase, nunca a PostHog (consulta "Iniciar sesión con Apple o Google"). Ningún evento de estadísticas contiene tus cálculos, datos que escribes, resultados, historial ni nada de lo que teclees; las grabaciones de pantalla muestran la calculadora y tu historial, y enmascaran lo que escribes en las casillas de las herramientas, como se describe arriba. La app tampoco pone tus cálculos, datos que escribes, resultados ni historial en los reportes de fallas.

## Compras y suscripciones (Apple y RevenueCat)

La app es de paga: ofrece una suscripción anual con prueba gratis para nuevos suscriptores que califiquen, y una compra única De por vida. Los pagos se hacen en el App Store con tu cuenta de Apple. **Apple procesa el pago; KLM Labs nunca recibe ni guarda los datos de tu tarjeta ni de tu banco.**

[RevenueCat, Inc.](https://www.revenuecat.com/privacy) procesa los registros de compra para KLM Labs, para que la app pueda revisar si tienes acceso, activarlo y restaurarlo en otro dispositivo. RevenueCat recibe tus registros de compra y suscripción del App Store (el producto, los ID de transacción de Apple, las fechas y el estado de la prueba y de la renovación), un ID de usuario aleatorio que crea RevenueCat (iniciar sesión no lo cambia), qué conjunto de planes te mostró la app, datos técnicos como la versión de la app, la versión de iOS o iPadOS y el país del App Store, y el identificador aleatorio de PostHog descrito arriba, para relacionar los eventos de compra con las estadísticas de uso. Desde la versión 1.2.0, si inicias sesión, también recibe tu ID de cuenta aleatorio y si la app viene del App Store o de TestFlight, nunca tu correo ni tu nombre. RevenueCat también recibe tu dirección IP cuando la app se conecta con él, y el ID de proveedor de tu dispositivo (IDFV) cuando iOS lo proporciona. iOS le da a cada desarrollador de apps un ID de proveedor por dispositivo, el mismo en todas las apps de ese desarrollador; no es el identificador de publicidad.

Usamos los registros de compra solo para darte y restaurar tu plan, para entender cómo se usan los planes y para atender tus solicitudes. No los usamos para publicidad.

## Recordatorios y notificaciones

Si empiezas una prueba gratis, la app puede recordártelo 2 días antes de que termine. El recordatorio es una notificación programada en tu dispositivo; no se envía desde un servidor y no se nos envía ningún token de notificaciones. Antes de la pantalla de planes, si el plan Anual está preseleccionado (desde la versión 1.1.0, solo cuando no se puede cargar el plan De por vida), puedes obtener su prueba gratis y aún no has respondido, la app muestra una página sobre la prueba y pide permiso para enviar notificaciones. Puedes decir que no o desactivarlas después en Configuración; la app funciona igual.

## Compartir el PDF del trazo de una escalera

La herramienta Escaleras puede crear un PDF de una página con el trazo de una escalera. El PDF se crea en tu dispositivo y abre la hoja para compartir del sistema. Solo sale de tu dispositivo si eliges un destino, que lo maneja según sus propias prácticas de privacidad.

## Cuando nos escribes

Si nos escribes para pedir ayuda o para una solicitud de privacidad, recibimos tu dirección de correo, tu nombre si tu correo lo incluye, tu mensaje y los archivos que decidas adjuntar, como capturas de pantalla. Google procesa este correo por nosotros mediante Gmail. Lo usamos solo para responder y atender tu solicitud.

## Proveedores de servicios

PostHog, RevenueCat y Google (Firebase Authentication, para el inicio de sesión, y Gmail, para el correo) procesan datos para KLM Labs. Exigimos que los proveedores de servicios que reciben datos personales de nosotros los protejan al mismo nivel, o a uno equivalente, que el descrito en este aviso y el que exigen las pautas de revisión de apps de Apple. No vendemos datos personales ni los compartimos para publicidad.

## Cuánto tiempo se guardan los datos

En tu dispositivo, el Historial conserva los 1,000 cálculos más recientes y borra los anteriores automáticamente. **Historial → Más (…) → Borrar todo** borra el historial y el último resultado del widget; no borra la memoria de la calculadora, los datos guardados de las herramientas ni los ajustes. Eliminar la app borra todo lo que guardó en el dispositivo; las copias en tus respaldos y lo que hayas compartido se manejan por separado.

Conservamos los eventos de estadísticas, los reportes de fallas, las grabaciones de pantalla, los registros de compra y los correos de ayuda solo mientras los necesitamos para operar, dar soporte y mejorar la app, o mientras la ley lo exija (por ejemplo, los registros de compra para fines fiscales y contables), y después los borramos. Eliminar la app no borra los registros que ya se enviaron a PostHog o a RevenueCat; para pedirnos que los borremos, consulta "Tus opciones y derechos" más abajo.

Si inicias sesión, tu cuenta (correo, nombre, si usaste Apple o Google y tus fechas de inicio de sesión) se guarda en Firebase hasta que la elimines o nos pidas eliminarla. Una cuenta eliminada sale de Firebase de inmediato, y de nuestro archivo exportado la próxima vez que lo exportemos; un archivo hecho antes de que eliminaras tu cuenta puede tener tu correo hasta entonces. Cuando nos lo pides por correo, eliminamos la cuenta y reemplazamos el archivo. Los registros que ya se enviaron a PostHog y a RevenueCat conservan el ID de cuenta aleatorio, pero cuando tu cuenta y ese archivo ya no existen, nada lo relaciona con tu correo.

## Menores de edad

Calculadora de Pies y Pulgadas es una herramienta para la construcción y los oficios, y no está dirigida a menores. No recopilamos a sabiendas datos personales de menores. Si crees que un menor usó la app, escríbenos y borraremos los registros que encontremos.

## Tus opciones y derechos

- **Borra tu historial** con Historial → Más (…) → Borrar todo, o elimina la app para borrar todo lo que guardó. Los respaldos del dispositivo, si los tienes activados, dependen de Apple y de tu configuración, no de nosotros.
- **Elimina tu cuenta**, si iniciaste sesión: **Configuración → Cuenta → Eliminar mi cuenta** en la app, o escribe a [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com) y la eliminaremos (consulta "Iniciar sesión con Apple o Google").
- **Desactiva los recordatorios** en Configuración → Notificaciones de tu dispositivo.
- **Cancela una suscripción** en la configuración de tu cuenta de Apple; consulta los [términos de uso](/construction-calc/es/terms/). Eliminar la app no la cancela.
- **Pídenos borrar registros de estadísticas (eventos, reportes de fallas y grabaciones) o de compras.** Escribe a [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com). Como estos registros usan identificadores aleatorios, dinos aproximadamente cuándo usaste la app y, si es una compra, cuándo compraste, para poder encontrarlos. Si iniciaste sesión, el correo que muestra Configuración también nos ayuda a encontrarlos. Te diremos qué encontramos y borramos. Apple conserva sus propios registros de compra.
- **Pregúntanos qué datos tenemos** escribiendo a la misma dirección.

Según dónde vivas, puedes tener otros derechos sobre tus datos personales, como el acceso, la rectificación, la cancelación y la oposición. Escríbenos y responderemos como lo exija la ley.

## Cambios a este aviso

Si cambian las prácticas de datos de la app, actualizaremos este aviso y los detalles de privacidad del App Store antes de publicar esa versión. La fecha de entrada en vigor, arriba, indica el último cambio. 21 de octubre de 2026: grabaciones de pantalla, desde la versión 1.0.2 (consulta "Estadísticas de uso"). 29 de octubre de 2026: la app funciona en iPhone y iPad, y envía reportes de fallas y más eventos de uso, desde la versión 1.1.0 (consulta "Estadísticas de uso"). 30 de octubre de 2026: inicio de sesión opcional con Apple o Google, desde la versión 1.2.0 (consulta "Iniciar sesión con Apple o Google"). Preguntas: [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com).

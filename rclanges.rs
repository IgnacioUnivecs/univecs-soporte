[1mdiff --git a/src/lang/es.rs b/src/lang/es.rs[m
[1mindex 8ad0c4cab..1e513e250 100644[m
[1m--- a/src/lang/es.rs[m
[1m+++ b/src/lang/es.rs[m
[36m@@ -1,4 +1,4 @@[m
[31m-lazy_static::lazy_static! {[m
[32m+[m[32m﻿lazy_static::lazy_static! {[m
 pub static ref T: std::collections::HashMap<&'static str, &'static str> =[m
     [[m
         ("Status", "Estado"),[m
[36m@@ -7,7 +7,7 @@[m [mpub static ref T: std::collections::HashMap<&'static str, &'static str> =[m
         ("Password", "Contraseña"),[m
         ("Ready", "Listo"),[m
         ("Established", "Establecido"),[m
[31m-        ("connecting_status", "Conexión a la red RustDesk en progreso..."),[m
[32m+[m[32m        ("connecting_status", "Conexión a la red Univecs Soporte en progreso..."),[m
         ("Enable service", "Habilitar Servicio"),[m
         ("Start service", "Iniciar Servicio"),[m
         ("Service is running", "El servicio se está ejecutando"),[m
[36m@@ -145,11 +145,11 @@[m [mpub static ref T: std::collections::HashMap<&'static str, &'static str> =[m
         ("Failed to make direct connection to remote desktop", "No se pudo establecer la conexión directa con el escritorio remoto"),[m
         ("Set Password", "Configurar la contraseña"),[m
         ("OS Password", "Contraseña del sistema operativo"),[m
[31m-        ("install_tip", "Debido al Control de cuentas de usuario, es posible que RustDesk no funcione correctamente como escritorio remoto. Para evitar este problema, haga clic en el botón de abajo para instalar RustDesk a nivel de sistema."),[m
[32m+[m[32m        ("install_tip", "Debido al Control de cuentas de usuario, es posible que Univecs Soporte no funcione correctamente como escritorio remoto. Para evitar este problema, haga clic en el botón de abajo para instalar Univecs Soporte a nivel de sistema."),[m
         ("Click to upgrade", "Clic para actualizar"),[m
         ("Configure", "Configurar"),[m
[31m-        ("config_acc", "Para controlar su escritorio desde el exterior, debe otorgar permiso a RustDesk de \"Accesibilidad\"."),[m
[31m-        ("config_screen", "Para controlar su escritorio desde el exterior, debe otorgar permiso a RustDesk de \"Grabación de pantalla\"."),[m
[32m+[m[32m        ("config_acc", "Para controlar su escritorio desde el exterior, debe otorgar permiso a Univecs Soporte de \"Accesibilidad\"."),[m
[32m+[m[32m        ("config_screen", "Para controlar su escritorio desde el exterior, debe otorgar permiso a Univecs Soporte de \"Grabación de pantalla\"."),[m
         ("Installing ...", "Instalando ..."),[m
         ("Install", "Instalar"),[m
         ("Installation", "Instalación"),[m
[36m@@ -170,7 +170,7 @@[m [mpub static ref T: std::collections::HashMap<&'static str, &'static str> =[m
         ("Local Port", "Puerto local"),[m
         ("Local Address", "Dirección Local"),[m
         ("Change Local Port", "Cambiar Puerto Local"),[m
[31m-        ("setup_server_tip", "Para una conexión más rápida, configure su propio servidor"),[m
[32m+[m[32m        ("setup_server_tip", "Para una conexión más rápida, servidor conectado"),[m
         ("Too short, at least 6 characters.", "Demasiado corto, al menos 6 caracteres."),[m
         ("The confirmation is not identical.", "La confirmación no coincide."),[m
         ("Permissions", "Permisos"),[m
[36m@@ -276,8 +276,8 @@[m [mpub static ref T: std::collections::HashMap<&'static str, &'static str> =[m
         ("Do you accept?", "¿Aceptas?"),[m
         ("Open System Setting", "Configuración del sistema abierto"),[m
         ("How to get Android input permission?", "¿Cómo obtener el permiso de entrada de Android?"),[m
[31m-        ("android_input_permission_tip1", "Para que un dispositivo remoto controle su dispositivo Android a través del ratón o toque, debe permitir que RustDesk use el servicio de \"Accesibilidad\"."),[m
[31m-        ("android_input_permission_tip2", "Vaya a la página de configuración del sistema que se abrirá a continuación, busque y acceda a [Servicios instalados], active el servicio [RustDesk Input]."),[m
[32m+[m[32m        ("android_input_permission_tip1", "Para que un dispositivo remoto controle su dispositivo Android a través del ratón o toque, debe permitir que Univecs Soporte use el servicio de \"Accesibilidad\"."),[m
[32m+[m[32m        ("android_input_permission_tip2", "Vaya a la página de configuración del sistema que se abrirá a continuación, busque y acceda a [Servicios instalados], active el servicio [Univecs Soporte Input]."),[m
         ("android_new_connection_tip", "Se recibió una nueva solicitud de control para el dispositivo actual."),[m
         ("android_service_will_start_tip", "Habilitar la captura de pantalla iniciará automáticamente el servicio, lo que permitirá que otros dispositivos soliciten una conexión desde este dispositivo."),[m
         ("android_stop_service_tip", "Cerrar el servicio cerrará automáticamente todas las conexiones establecidas."),[m
[36m@@ -299,7 +299,7 @@[m [mpub static ref T: std::collections::HashMap<&'static str, &'static str> =[m
         ("Failed to turn off", "Error al apagar"),[m
         ("Turned off", "Apagado"),[m
         ("Language", "Idioma"),[m
[31m-        ("Keep RustDesk background service", "Dejar RustDesk como Servicio en 2do plano"),[m
[32m+[m[32m        ("Keep RustDesk background service", "Dejar Univecs Soporte como Servicio en 2do plano"),[m
         ("Ignore Battery Optimizations", "Ignorar optimizacioens de bateria"),[m
         ("android_open_battery_optimizations_tip", "Si deseas deshabilitar esta característica, por favor, ve a la página siguiente de ajustes, busca y entra en  [Batería] y desmarca [Sin restricción]"),[m
         ("Start on boot", ""),[m
[36m@@ -381,7 +381,7 @@[m [mpub static ref T: std::collections::HashMap<&'static str, &'static str> =[m
         ("Wayland requires higher version of linux distro. Please try X11 desktop or change your OS.", "Wayland requiere una versión superior de la distribución de Linux. Pruebe el escritorio X11 o cambie su sistema operativo."),[m
         ("JumpLink", "Ver"),[m
         ("Please Select the screen to be shared(Operate on the peer side).", "Seleccione la pantalla que se compartirá (Operar en el lado del par)."),[m
[31m-        ("Show RustDesk", "Mostrar RustDesk"),[m
[32m+[m[32m        ("Show Univecs Soporte", "Mostrar Univecs Soporte"),[m
         ("This PC", "Este PC"),[m
         ("or", "o"),[m
         ("Elevate", "Elevar privilegios"),[m
[36m@@ -407,8 +407,8 @@[m [mpub static ref T: std::collections::HashMap<&'static str, &'static str> =[m
         ("Select local keyboard type", "Seleccionar tipo de teclado local"),[m
         ("software_render_tip", "Si tienes una gráfica Nvidia y la ventana remota se cierra inmediatamente, instalar el driver nouveau y elegir renderizado por software podría ayudar. Se requiere reiniciar la aplicación."),[m
         ("Always use software rendering", "Usar siempre renderizado por software"),[m
[31m-        ("config_input", "Para controlar el escritorio remoto con el teclado necesitas dar a RustDesk permisos de \"Monitorización de entrada\"."),[m
[31m-        ("config_microphone", "Para poder hablar de forma remota necesitas darle a RustDesk permisos de \"Grabar Audio\"."),[m
[32m+[m[32m        ("config_input", "Para controlar el escritorio remoto con el teclado necesitas dar a Univecs Soporte permisos de \"Monitorización de entrada\"."),[m
[32m+[m[32m        ("config_microphone", "Para poder hablar de forma remota necesitas darle a Univecs Soporte permisos de \"Grabar Audio\"."),[m
         ("request_elevation_tip", "También puedes solicitar elevación de privilegios si hay alguien en el lado remoto."),[m
         ("Wait", "Esperar"),[m
         ("Elevation Error", "Error de elevación de privilegios"),[m
[36m@@ -465,7 +465,7 @@[m [mpub static ref T: std::collections::HashMap<&'static str, &'static str> =[m
         ("show_monitors_tip", "Mostrar monitores en la barra de herramientas"),[m
         ("View Mode", "Modo Vista"),[m
         ("login_linux_tip", "Necesitas iniciar sesión con la cueneta del Linux remoto para activar una sesión de escritorio X"),[m
[31m-        ("verify_rustdesk_password_tip", "Verificar la contraseña de RustDesk"),[m
[32m+[m[32m        ("verify_rustdesk_password_tip", "Verificar la contraseña de Univecs Soporte"),[m
         ("remember_account_tip", "Recordar esta cuenta"),[m
         ("os_account_desk_tip", "Esta cueneta se usa para iniciar sesión en el sistema operativo remoto y habilitar la sesión de escritorio en headless."),[m
         ("OS Account", "Cuenta del SO"),[m
[36m@@ -530,7 +530,7 @@[m [mpub static ref T: std::collections::HashMap<&'static str, &'static str> =[m
         ("Reverse mouse wheel", "Invertir rueda del ratón"),[m
         ("{} sessions", "{} sesiones"),[m
         ("scam_title", "Podrías estar siendo ESTAFADO!"),[m
[31m-        ("scam_text1", "Si estás al teléfono con alguien a quien NO conoces y en quien NO confías y te ha pedido que uses RustDesk e inicies el servicio, no lo hagas y cuelga inmediatamente."),[m
[32m+[m[32m        ("scam_text1", "Si estás al teléfono con alguien a quien NO conoces y en quien NO confías y te ha pedido que uses Univecs Soporte e inicies el servicio, no lo hagas y cuelga inmediatamente."),[m
         ("scam_text2", "Probablemente son estafadores tratando de robar tu dinero o información privada."),[m
         ("Don't show again", "No mostrar de nuevo"),[m
         ("I Agree", "Estoy de acuerdo"),[m
[36m@@ -549,7 +549,7 @@[m [mpub static ref T: std::collections::HashMap<&'static str, &'static str> =[m
         ("Open in new window", "Abrir en una nueva ventana"),[m
         ("Show displays as individual windows", "Mostrar pantallas como ventanas individuales"),[m
         ("Use all my displays for the remote session", "Usar todas mis pantallas para la sesión remota"),[m
[31m-        ("selinux_tip", "SELinux está activado en tu dispositivo, lo que puede hacer que RustDesk no se ejecute correctamente como lado controlado."),[m
[32m+[m[32m        ("selinux_tip", "SELinux está activado en tu dispositivo, lo que puede hacer que Univecs Soporte no se ejecute correctamente como lado controlado."),[m
         ("Change view", "Cambiar vista"),[m
         ("Big tiles", "Mosaicos grandes"),[m
         ("Small tiles", "Mosaicos pequeños"),[m
[36m@@ -578,7 +578,7 @@[m [mpub static ref T: std::collections::HashMap<&'static str, &'static str> =[m
         ("2FA code must be 6 digits.", "El cóidigo 2FA debe tener 6 dígitos"),[m
         ("Multiple Windows sessions found", "Encontradas sesiones de múltiples ventanas"),[m
         ("Please select the session you want to connect to", "Por favor, seleccione la sesión a la que se desea conectar"),[m
[31m-        ("powered_by_me", "Con tecnología de RustDesk"),[m
[32m+[m[32m        ("powered_by_me", "Con tecnología de Univecs Soporte"),[m
         ("outgoing_only_desk_tip", "Esta es una edición personalizada.\nPuedes conectarte a otros dispositivos, pero ellos no pueden conectarse al tuyo."),[m
         ("preset_password_warning", "Esta edición personalizada viene con una contraseña preestablecida. Cualquiera que la conozca podrá tener control total de tu dispositivo.Si no es esto lo que esperabas, desinstala el software inmediatamente."),[m
         ("Security Alert", "Alerta de Seguridad"),[m
[36m@@ -608,7 +608,7 @@[m [mpub static ref T: std::collections::HashMap<&'static str, &'static str> =[m
         ("texture_render_tip", "Usar renderizado de texturas para hacer las imágenes más suaves."),[m
         ("Use texture rendering", "Usar renderizado de texturas"),[m
         ("Floating window", "Ventana flotante"),[m
[31m-        ("floating_window_tip", "Ayuda a mantener el servicio de RustDesk de fondo"),[m
[32m+[m[32m        ("floating_window_tip", "Ayuda a mantener el servicio de Univecs Soporte de fondo"),[m
         ("Keep screen on", "Mantener la pantalla encendida"),[m
         ("Never", "Nunca"),[m
         ("During controlled", "Mientras está siendo controlado"),[m
[36m@@ -624,7 +624,7 @@[m [mpub static ref T: std::collections::HashMap<&'static str, &'static str> =[m
         ("enable-bot-desc", "1, Abre un chat con @BotFather.\n2, Envía el comando \"/newbot\". Recibirás un token tras completar esta paso.\n3, Inicia un chat con tu bot recién creado. Envía un mensaje que comience con una barra (\"/\") como \"/hola\" para activarlo.\n"),[m
         ("cancel-2fa-confirm-tip", "¿Seguro que quieres cancelar 2FA?"),[m
         ("cancel-bot-confirm-tip", "¿Seguro que quieres cancelar el bot de Telegram?"),[m
[31m-        ("About RustDesk", "Acerca de RustDesk"),[m
[32m+[m[32m        ("About RustDesk", "Acerca de Univecs Soporte"),[m
         ("Send clipboard keystrokes", "Enviar pulsaciones de teclas"),[m
         ("network_error_tip", "Por fvor, comprueba tu conexión de red e inténtalo de nuevo."),[m
         ("Unlock with PIN", "Desbloquear con PIN"),[m
[36m@@ -651,7 +651,7 @@[m [mpub static ref T: std::collections::HashMap<&'static str, &'static str> =[m
         ("Untagged", "Sin itiquetar"),[m
         ("new-version-of-{}-tip", "Hay una nueva versión de {} disponible"),[m
         ("Accessible devices", ""),[m
[31m-        ("upgrade_remote_rustdesk_client_to_{}_tip", "Por favor, actualiza el cliente RustDesk a la versión {} o superior en el lado remoto"),[m
[32m+[m[32m        ("upgrade_remote_rustdesk_client_to_{}_tip", "Por favor, actualiza el cliente Univecs Soporte a la versión {} o superior en el lado remoto"),[m
         ("d3d_render_tip", "Al activar el renderizado D3D, la pantalla de control remoto puede verse negra en algunos equipos."),[m
         ("Use D3D rendering", "Usar renderizado D3D"),[m
         ("Printer", "Impresora"),[m

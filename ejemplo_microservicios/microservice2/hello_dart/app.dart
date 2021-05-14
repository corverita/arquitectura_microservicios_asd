// ----------------------------------------------------------------------------------------------------------------
// Archivo: app.dart
// Implementación de Arquitecturas Micro Servicios.
// Autor(es): Perla Velasco & Jorge Alfonso Solís.
// Version: 1.0.0 Marzo 2021
// Descripción:
//
//   Este archivo define un ejemplo sencillo de un micro servicio desarrollado en el lenguaje de programación Dart.
//
//                                             app.dart
//           +-----------------------+-------------------------+------------------------+
//           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
//           +-----------------------+-------------------------+------------------------+
//           |                       |  - Envía un mensaje     | - Utiliza el lenguaje  |
//           |         main          |    al recibir una       |   de programación      |
//           |                       |    solicitud HTTP.      |   Dart para su imple-  |
//           |                       |                         |   mentación.           |
//           +-----------------------+-------------------------+------------------------+
//
// ----------------------------------------------------------------------------------------------------------------

import "dart:io";
import 'dart:convert';

Future main() async {
  // Se crea la variable server, haciendo bind con el host y el puerto asignados
  var server = await HttpServer.bind(
    '172.15.0.5',
    49002,
  );

  // El servidor comienza a escuchar solicitudes HTTP
  await for (HttpRequest request in server) {
    // Mensaje a ser enviado cada que se reciba una solicitud
    Map jsonData = {'Message': 'Hello World from Dart!'};
    // Se envía el mensaje en formato json
    request.response.write(jsonEncode(jsonData));
    // Se cierra la respuesta de la solicitud
    await request.response.close();
  }
}

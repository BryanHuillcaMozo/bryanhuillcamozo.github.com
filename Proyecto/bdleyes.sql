-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-09-2021 a las 13:57:15
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 7.3.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bdleyes`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tinformacion`
--

CREATE TABLE `tinformacion` (
  `Expediente` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `Periodo` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `Legislatura` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `Fecha` date NOT NULL,
  `Propone` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `Parlamento` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `Titulo` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `Objeto` varchar(250) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `tinformacion`
--

INSERT INTO `tinformacion` (`Expediente`, `Periodo`, `Legislatura`, `Fecha`, `Propone`, `Parlamento`, `Titulo`, `Objeto`) VALUES
('00004/2021-CR', '2021-2026', 'Primera Legislatura Ordinaria ', '0000-00-00', 'Congreso', 'Partido Morado', 'LEY QUE DECLARA DE NECESIDAD PÚBLICA E INTERÉS NACIONAL LA RECUPERACIÓN, CONSTRUCCIÓN Y PROTECCIÓN D', 'Propone declarar de necesidad pública e interés nacional la recuperación, construcción y protección de la pesca ancestral en caballito de totora y la creación de los balsares en el distrito de Pimentel, provincia de Chiclayo, departamento de Lambayeq'),
('00036/2021-CR', '2016 - 2021', 'Primera Legislatura Ordinaria ', '0000-00-00', 'Congreso', 'Partido Morado', 'LEY QUE INTERPRETA EL ARTÍCULO 132 DE LA CONSTITUCIÓN POLÍTICA DEL PERÚ', 'Propone incorporar el artículo 15-A Prohibiciones, en la Ley Orgánica del Poder Ejecutivo.'),
('00037/2021-CR', '2021-2026', 'Primera Legislatura Ordinaria ', '0000-00-00', 'Congreso', 'Partido Morado', 'LEY QUE MODIFICA EL ARTÍCULO 15 DE LA LEY ORGÁNICA DEL PODER EJECUTIVO', 'Propone incorporar el artículo 15-A Prohibiciones, en la Ley Orgánica del Poder Ejecutivo.'),
('08023/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Partido Morado', 'LEY QUE MODIFICA EL DECRETO LEGISLATIVO 1141, DERCETO LEGISLATIVO DE FORTALECIMIENTO Y MODERNIZACIÓN', 'Propone modificar el artículo 34 del Decreto Legislativo 1141, Decreto Legislativo de Fortalecimiento y Modernización del Sistema de Inteligencia Nacional - SINA y de la Dirección Nacional de Inteligencia DINI.'),
('08024/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Unión por el Perú', 'LEY QUE MODIFICA EL ARTICULO 279°-G DEL CODIGO PENAL REFERIDA AL DELITO DE TENENCIA ILEGAL DE ARMAS', 'Propone modificar el artículo 279 - G del Código Penal, referido al delito de Tenencia Ilegal de Armas.'),
('08025/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Alianza Para el Progreso', 'LEY QUE DECLARA DE INTERÉS NACIONAL Y NECESIDAD PÚBLICA LA CREACIÓN Y EQUIPAMIENTO DE HOGARES DE REF', 'Propone declarar de interés nacional y necesidad pública la creación y equipamiento de hogares de refugio temporal para víctimas de violencia familiar y de grupos familiares en las provincias de la región Apurímac.'),
('08026/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Alianza Para el Progreso', 'LEY QUE DECLARA DE INTERÉS NACIONAL Y NECESIDAD PÚBLICA LA CREACIÓN DEL DISTRITO VÍCTOR RAÚL HAYA DE', 'Propone declarar de interés nacional y necesidad pública la creación del distrito Víctor Raúl Haya de la Torre con su capital Apumarca, en la provincia Cotabambas, departamento de Apurímac.'),
('08027/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Descentralización Democrática', 'LEY QUE SANCIONA CON CADENA PERPETUA E INHABILITACIÓN A LOS FUNCIONARIOS PÚBLICOS POR ENRIQUECIMIENT', 'Propone modificar el artículo 401 del Código Penal.'),
('08028/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Descentralización Democrática', 'LEY QUE DECLARA DE INTERÉS NACIONAL Y NECESIDAD PÚBLICA LA CREACIÓN DEL DISTRITO ALTO DORADO EN LA P', 'Propone declarar de interés nacional y necesidad pública la creación del distrito Alto Dorado de San Ignacio, departamento de Cajamarca.'),
('08029/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Descentralización Democrática', 'LEY DE LA PARTICIPACION DE LAS RONDAS CAMPESINAS EN LA SUPERVISIÓN Y FISCALIZACIÓN EN LA EJECUCIÓN D', 'Propone modificar el artículo 6 de la Ley 27908 Ley de rondas campesinas'),
('08030/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Unión por el Perú', 'LEY QUE MODIFICA LOS ARTÍCULOS 19° Y 20° DEL CÓDIGO CIVIL REFERIDO AL ORDEN DEL APELLIDO DE LOS HIJO', 'Propone modificar los artículos 19 y 20 del Código Civil a efectos de establecer un mecanismo de solución ante la disconformidad de los progenitores para asignar el orden de apellidos de los hijos.'),
('08031/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Unión por el Perú', 'LEY QUE MODIFICA EL ARTÍCULO 2 E INCORPORA UNA DISPOSICION COMPLEMENTARIA FINAL A LA LEY 28514, LEY ', 'Propone modificar el artículo 2 e incorporar una Disposición Complementaria Final a la Ley 28514 Ley que prohíbe la importación de ropa y calzado usados.'),
('08032/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Acción Popular', 'LEY QUE CREA EL COLEGIO DE FISIOTERAPEUTAS DEL PERÚ - CFP Y LEY DE TRABAJO DEL FISIOTERAPEUTA', 'Propone crear el Colegio de Fisioterapeutas del Perú - CFP y Ley de Trabajo del Fisioterapeuta, para la supervisión del desarrollo de la actividad profesional dentro de las normas éticas y profesionales, que contribuya con la mejor de la salud de la '),
('08033/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Nueva Constitución', 'LEY QUE DECLARA DE INTERES NACIONAL Y NECESIDAD PÚBLICA LA CREACIÓN DE TRES DISTRITOS DE LA CIUDAD D', 'Propone declarar de interés nacional y necesidad pública y dispóngase la creación de tres distritos en la ciudad de Juliaca en la Provincia de San Román, departamento de Puno, mediante la creación de dos distritos más el distrito de San Miguel.'),
('08034/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Nueva Constitución', 'LEY QUE DECLARA DE INTERES NACIONAL Y NECESIDAD PÚBLICA LA CREACIÓN DE LA PROVINCIA DE ACORA, DEL DE', 'Propone declarar de interés nacional y necesidad pública la creación de la provincia de Acora, del departamento de Puno.'),
('08035/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Nueva Constitución', 'LEY QUE DECLARA DE PREFERENTE INTERÉS NACIONAL Y DE NECESIDAD PÚBLICA LA INCORPORACIÓN A LA RED VIAL', 'Propone declarar de interés nacional y necesidad pública la incorporación de la red vial el tramo: Mazocruz - Pazacomo - Hito 27, en las provincias de Ilave e Ilo de los departamentos de Puno y Moquegua.'),
('08036/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Nueva Constitución', 'LEY QUE DECLARA DE NECESIDAD PÚBLICA Y PREFERENTE INTERÉS NACIONAL LA CONSTRUCCIÓN, REHABILITACIÓN Y', 'Propone declarar de necesidad pública y preferente interés nacional la construcción, rehabilitación y asfaltado a nivel de pavimento flexible de carretera Trayectoria EMP. PE-34 I (Asiruni)-Cotacucho-Sicta-Alto Challapa-Cartahuyo-Rosaspata-Ñapa Pampa'),
('08037/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Nueva Constitución', 'LEY QUE SUSPENDEN LA IMPORTACIÓN DE LA PAPA, QUINOA, ARROZ, TELAS CHINAS Y OTROS PRODUCTOS QUE EN NU', 'Propone promover acciones destinadas a salvaguardar a los productores agropecuarios que producen la papa, que se ven afectadas por la emergencia nacional producida por el COVID 19, promoviendo de esta manera que se dinamice su economía.'),
('08038/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Nueva Constitución', 'LEY QUE MOFIDICA EL ARTÍCULO 300 DE LA LEY 26859 - LEY ORGÁNICA DE ELECCIONES', 'Propone modificar el artículo 300 de la Ley 26859 - Ley Orgánica de Elecciones, a afectos de que se establezca la prohibición de la destrucción de las cédulas escrutadas y no impugnadas, después de concluido el escrutinio.'),
('08039/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Nueva Constitución', 'LEY QUE DECLARA DE PREFERENTE INTERES NACIONAL Y DE NECESIDAD PÚBLICA LA CONSTRUCCIÓN A NIVEL DE ASF', 'Propone declarar de interés nacional y necesidad pública la construcción a nivel de asfaltado económico e incorporación a la red vial el tramo: Mazocruz-Pizacoma - Hito 27, en las provincias de Ilave e Ilo de los departamentos de Puno y Moquegua'),
('08040/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Nueva Constitución', 'LEY QUE DECLARA INTERÉS NACIONAL, LA DECLARATORIA DE PATRIMONIO CULTURAL DE LA NACIÓN EL TORITO DE P', 'Propone declarar de interés nacional la Declaratoria de Patrimonio Cultural de la Nación El Torito de Pupuja y la tradicional forma de elaboración, del distrito de Santiago de Pupuja, provincia de Azángaro en el departamento de Puno, por tratarse de '),
('08041/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Alianza Para el Progreso', 'LEY QUE PROPONE SE DECLARE DE INTERÉS Y PREFERENTE NECESIDAD PÚBLICA EL FORTALECIMIENTO DE LA ENSEÑA', 'Propone declarar de interés nacional y preferente necesidad pública la enseñanza del curso de valores éticos y civismo en etapa escolar, como mecanismo de lucha contra la corrupción.'),
('08042/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Frente Popular Agrícola del Perú', 'LEY QUE EXTIENDE EL PERIODO DE FORMALIZACIÓN DE LOS PESCADORES ARTESANALES, CONSIDERA COMO PRIMERA O', 'Propone ampliar el plazo para la formalización de la actividad pesquera artesanal. Asimismo, dispone que el Estado considere como primera opción de compra, de requerirlo para sus programas de asistencia alimentaria, a los productos hidrobiológicos ge'),
('08043/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Frente Popular Agrícola del Perú', 'LEY QUE DECLARA DE INTERES NACIONAL Y NACESIDAD PÚBLICA LA CREACIÓN DEL DISTRITO DE MALDONADILLO, EN', 'Propone declarar de interés nacional y necesidad pública la creación del distrito de Maldonadillo, de la provincia de Atalaya, de la región de Ucayali.'),
('08044/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Alianza Para el Progreso', 'LEY QUE DECLARA DE INTERES NACIONAL Y NACESIDAD PÚBLICA LA CREACIÓN DE LA PROVINCIA CONSTITUCIONAL E', 'Propone declarar de necesidad pública e interés nacional la creación de la provincia Constitucional Energética de la Convención, a fin de promover su desarrollo y conectividad.'),
('08045/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Acción Popular', 'LEY QUE REESTRUCTURA EL PROYECTO ESPECIAL CHINECAS DE LA PROVINCIA DEL SANTA, DEPARTAMENTO DE ÁNCASH', 'Propone reestructurar el Proyecto Especial Chinecas de la provincia del Santa departamento de Áncash y crear un comité de gestión de pasivos.'),
('08046/2020-CR', '2016 - 2021', 'Cuarta Legislatura Ordinaria 2', '0000-00-00', 'Congreso', 'Acción Popular', 'LEY QUE MODIFICA EL DECRETO DE URGENCIA 034-2019, REFERIDO A LA INCORPORACIÓN DE LA DÉCIMA SEGUNDA D', 'Propone fortalecer el rol del Ministerio de Educación, como ente rector de la Política de Aseguramiento de la Calidad de la Educación Superior Universitaria, teniendo la finalidad de garantizar la calidad y continuidad del Servicio Educativo Universi');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tinformacion`
--
ALTER TABLE `tinformacion`
  ADD PRIMARY KEY (`Expediente`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

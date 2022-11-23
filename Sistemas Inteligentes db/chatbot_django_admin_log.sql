-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: chatbot
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_Usuario_usuario_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_Usuario_usuario_id` FOREIGN KEY (`user_id`) REFERENCES `usuario_usuario` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-11-23 17:57:13.033518','1','Respuestas object (1)',1,'[{\"added\": {}}]',6,1),(2,'2022-11-23 18:01:33.938949','2','AnonymousUser',1,'[{\"added\": {}}]',7,1),(3,'2022-11-23 18:07:17.057546','2','AnonymousUser',3,'',7,1),(4,'2022-11-23 18:19:56.601580','2','Respuestas object (2)',2,'[]',6,1),(5,'2022-11-23 18:20:15.990699','2','Respuestas object (2)',2,'[]',6,1),(6,'2022-11-23 18:20:23.136004','3','Respuestas object (3)',1,'[{\"added\": {}}]',6,1),(7,'2022-11-23 18:21:18.539101','7','Pregunta object (7)',3,'',8,1),(8,'2022-11-23 18:21:18.541631','6','Pregunta object (6)',3,'',8,1),(9,'2022-11-23 18:21:18.543626','5','Pregunta object (5)',3,'',8,1),(10,'2022-11-23 18:21:18.544624','4','Pregunta object (4)',3,'',8,1),(11,'2022-11-23 18:21:18.546618','3','Pregunta object (3)',3,'',8,1),(12,'2022-11-23 18:21:18.548613','2','Pregunta object (2)',3,'',8,1),(13,'2022-11-23 18:21:18.549611','1','Pregunta object (1)',3,'',8,1),(14,'2022-11-23 18:21:39.370080','1','Respuestas object (1)',2,'[{\"changed\": {\"fields\": [\"Respuesta\"]}}]',6,1),(15,'2022-11-23 18:21:58.799316','10','Pregunta object (10)',3,'',8,1),(16,'2022-11-23 18:21:58.801310','9','Pregunta object (9)',3,'',8,1),(17,'2022-11-23 18:21:58.803305','8','Pregunta object (8)',3,'',8,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-23 13:42:01

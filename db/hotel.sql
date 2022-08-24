-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: localhost    Database: hotel
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `hotel`
--

/*!40000 DROP DATABASE IF EXISTS `hotel`*/;

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `hotel` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `hotel`;

--
-- Table structure for table `Categories`
--

DROP TABLE IF EXISTS `Categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Categories` (
  `id_category` int NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id_category`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Categories`
--

LOCK TABLES `Categories` WRITE;
/*!40000 ALTER TABLE `Categories` DISABLE KEYS */;
INSERT INTO `Categories` VALUES (1,'Level 1','Premium',1),(2,'Level 2','Delux',1),(3,'Level 3','Royal',1),(4,'Level 4','Premium 2',0),(5,'Level 5','Premium 3',0),(6,'Level 6','Premium 4',1),(7,'Level 7','Premium 5',1),(8,'Level 8','Premium 6',1),(9,'Level 9','Premium 7',1);
/*!40000 ALTER TABLE `Categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Guests`
--

DROP TABLE IF EXISTS `Guests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Guests` (
  `id_guest` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  `age` int DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `active` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`id_guest`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Guests`
--

LOCK TABLES `Guests` WRITE;
/*!40000 ALTER TABLE `Guests` DISABLE KEYS */;
INSERT INTO `Guests` VALUES (1,'name1','lastname1',21,'email1@test1.com','password1',1),(2,'name2','lastname2',22,'email2@test2.com','password2',1),(3,'name3','lastname3',23,'email3@test3.com','password3',1),(4,'name4','lastname4',24,'email4@test4.com','password4',1),(5,'name5','lastname5',25,'email5@test5.com','password5',1);
/*!40000 ALTER TABLE `Guests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Reservations`
--

DROP TABLE IF EXISTS `Reservations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Reservations` (
  `id_reservation` int NOT NULL AUTO_INCREMENT,
  `start_date` datetime NOT NULL,
  `devolution_date` datetime NOT NULL,
  `score` int DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `active` tinyint(1) DEFAULT '1',
  `id_room` int DEFAULT NULL,
  `id_guest` int DEFAULT NULL,
  PRIMARY KEY (`id_reservation`),
  KEY `fk_reservations_rooms_idx` (`id_room`),
  KEY `fk_reservations_guests_idx` (`id_guest`),
  CONSTRAINT `fk_reservations_guests` FOREIGN KEY (`id_guest`) REFERENCES `Guests` (`id_guest`),
  CONSTRAINT `fk_reservations_rooms` FOREIGN KEY (`id_room`) REFERENCES `Rooms` (`id_room`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Reservations`
--

LOCK TABLES `Reservations` WRITE;
/*!40000 ALTER TABLE `Reservations` DISABLE KEYS */;
INSERT INTO `Reservations` VALUES (1,'2025-01-02 11:00:00','2025-01-12 12:00:00',NULL,'completed',1,1,1),(2,'2025-02-10 11:00:00','2025-02-20 12:00:00',NULL,'completed',1,6,1),(3,'2025-03-20 11:00:00','2025-03-23 12:00:00',NULL,'pending',1,5,2),(4,'2025-04-10 11:00:00','2025-04-20 12:00:00',NULL,'cancelled',1,2,3),(5,'2025-07-10 11:00:00','2025-07-20 12:00:00',NULL,'pending',1,2,4),(6,'2025-07-15 11:00:00','2025-07-20 12:00:00',NULL,'pending',1,3,1),(7,'2025-07-10 11:00:00','2025-07-20 12:00:00',NULL,'pending',1,4,5),(8,'2025-08-22 11:00:00','2025-08-25 12:00:00',NULL,'cancelled',1,6,1),(9,'2025-09-10 11:00:00','2025-09-20 12:00:00',NULL,'cancelled',1,4,3),(10,'2025-09-27 11:00:00','2025-09-28 12:00:00',NULL,'cancelled',1,5,2),(11,'2026-09-27 11:00:00','2025-09-28 12:00:00',NULL,'cancelled',1,5,2);
/*!40000 ALTER TABLE `Reservations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Rooms`
--

DROP TABLE IF EXISTS `Rooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Rooms` (
  `id_room` int NOT NULL AUTO_INCREMENT,
  `address` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `size` decimal(10,0) NOT NULL,
  `name` varchar(255) NOT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `id_category` int DEFAULT NULL,
  PRIMARY KEY (`id_room`),
  KEY `fk_rooms_categories_idx` (`id_category`),
  CONSTRAINT `fk_rooms_categories` FOREIGN KEY (`id_category`) REFERENCES `Categories` (`id_category`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Rooms`
--

LOCK TABLES `Rooms` WRITE;
/*!40000 ALTER TABLE `Rooms` DISABLE KEYS */;
INSERT INTO `Rooms` VALUES (1,'111 - Building 1 Floor 1 Room 1','Great value and good location',89,'Happy pocket',1,1),(2,'121 - Building 1 Floor 2 Room 1','Great value and better view',89,'Less Happy pocket',1,1),(3,'211 - Building 2 Floor 1 Room 1','Enjoy a lot',120,'Happy Family',1,2),(4,'221 - Building 2 Floor 2 Room 1','Enjoy a lot with better view',120,'Happy Family and view',1,2),(5,'311 - Building 3 Floor 1 Room 1','Luxury and relax',180,'Making Family',1,3),(6,'321 - Building 3 Floor 2 Room 1','Luxury, relax and view',180,'Making Starry Family',0,3);
/*!40000 ALTER TABLE `Rooms` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-24 10:46:40

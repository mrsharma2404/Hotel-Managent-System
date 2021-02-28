-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 20, 2021 at 05:42 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project1`
--

-- --------------------------------------------------------

--
-- Table structure for table `projecta`
--

CREATE TABLE `projecta` (
  `full_name` varchar(50) NOT NULL,
  `age` int(3) NOT NULL,
  `phone_no` varchar(12) NOT NULL,
  `time` varchar(20) NOT NULL,
  `date` varchar(20) NOT NULL,
  `days` int(2) NOT NULL,
  `id_type` varchar(50) NOT NULL,
  `id_no` varchar(30) NOT NULL,
  `room_type` varchar(30) NOT NULL,
  `room` int(2) NOT NULL,
  `out_time` varchar(10) NOT NULL,
  `out_date` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `projecta`
--

INSERT INTO `projecta` (`full_name`, `age`, `phone_no`, `time`, `date`, `days`, `id_type`, `id_no`, `room_type`, `room`, `out_time`, `out_date`) VALUES
('Rohit', 21, '2147483647', '16:30', '03-10-2020', 5, 'Adhaar Card', '123456789abc', '', 0, '', ''),
('Sudhanshu', 21, '2147483647', '16:32', '03-10-2020', 5, 'adhar card', 'abcd1234', '', 0, '', ''),
('Rohit Sharma', 21, '8269526372', '16:43', '03-10-2020', 5, 'Adhaar Card', '123456roh', '', 0, '', ''),
('Samar', 20, '123456789', '01:48', '04-10-2020', 2, 'ac', '123456sam', '', 0, '', ''),
('MS Dhoni', 37, '100', '13:37', '04-10-2020', 1, 'Not Required', '.....', '', 7, '15:45', '04-11'),
('Sachin_Tendulkar', 44, '1234567890', '16:21', '04-10-2020', 5, 'Not Required', '123sachin', '', 10, '', ''),
('Rohit Verma', 21, '123123', '15:45', '04-10', 5, 'ASD', '123', '', 88, '', ''),
('Virat Kohli', 32, '789456123', '12:49', '06-10', 5, 'Not Required', 'NIL', '', 25, '', ''),
('Sikhar Dhawan', 33, '4567891230', '12:52', '06-10', 5, 'Note Required', 'NIL', '', 44, '', ''),
('Pankaj', 21, '1234567891', '4:12', '04-10', 5, 'no', '10', '', 44, '', ''),
('Rishabh Pant', 28, '4567891230', '02:06', '04-10', 5, 'none', 'null', '', 9, '', ''),
('Rajkumar', 45, '4567891302', '15:14', '07-10', 5, 'nun', 'nun', 'Delux Room', 45, '', ''),
('Kartik', 10, '123', '12:10', '10-10', 5, 'none', '12', '45', 12, '12', '01');

-- --------------------------------------------------------

--
-- Table structure for table `projectb`
--

CREATE TABLE `projectb` (
  `full_name` varchar(50) NOT NULL,
  `age` int(2) NOT NULL,
  `phone_no` varchar(50) NOT NULL,
  `time` varchar(10) NOT NULL,
  `date` varchar(10) NOT NULL,
  `days` int(2) NOT NULL,
  `id_type` varchar(30) NOT NULL,
  `id_no` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `projectb`
--

INSERT INTO `projectb` (`full_name`, `age`, `phone_no`, `time`, `date`, `days`, `id_type`, `id_no`) VALUES
('xyz', 12, '8269526372', '16:41', '03-10-2020', 5, 'Adhaar Card', '123456xyz');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

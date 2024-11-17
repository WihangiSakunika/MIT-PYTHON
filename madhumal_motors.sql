-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 17, 2024 at 07:52 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `madhumal_motors`
--

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `id` int(11) NOT NULL,
  `make` varchar(50) NOT NULL,
  `model` varchar(50) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`id`, `make`, `model`, `quantity`, `price`) VALUES
(2, 'Honda', 'CBR600RR', 5, 8500.00),
(3, 'Suzuki', 'Gixxer SF', 12, 2000.00),
(4, 'Kawasaki', 'Z1000', 3, 12000.00),
(5, 'Harley-Davidson', 'Sportster Iron 883', 4, 9500.00),
(6, 'BMW', 'R1250 GS', 6, 23000.00),
(7, 'Ducati', 'Monster 821', 8, 11500.00),
(8, 'KTM', 'RC 200', 15, 2500.00),
(9, 'Royal Enfield', 'Meteor 350', 20, 4100.00),
(10, 'TVS', 'Apache RTR 160', 18, 1300.00),
(11, 'yamaha', 'y2016', 10, 100000.00),
(12, 'Harley-Davidson	', 'Sportster Iron 883', 10, 100000.00);

-- --------------------------------------------------------

--
-- Table structure for table `sales`
--

CREATE TABLE `sales` (
  `id` int(11) NOT NULL,
  `customer_name` varchar(100) NOT NULL,
  `bike_make` varchar(50) NOT NULL,
  `bike_model` varchar(50) NOT NULL,
  `quantity_sold` int(11) NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `sale_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sales`
--

INSERT INTO `sales` (`id`, `customer_name`, `bike_make`, `bike_model`, `quantity_sold`, `total_price`, `sale_date`) VALUES
(1, 'L.H.V', 'YAMAHA', 'FZ-S V3', 1, 1500.00, '2024-11-17 06:40:51'),
(2, 'antony perera', 'Harley-Davidson	', 'Sportster Iron 883', 1, 95000.00, '2024-11-17 06:45:33');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sales`
--
ALTER TABLE `sales`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `inventory`
--
ALTER TABLE `inventory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `sales`
--
ALTER TABLE `sales`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

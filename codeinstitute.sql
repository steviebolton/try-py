
/*******************************************************************************
   code_institute Database - Version 1.4
   Script: Chinook_MySql_AutoIncrementPKs.sql
   Description: Creates and populates the  Code_institute database.
   DB Server: MySql
   Author: Stevie Bolton
   License: http://www.codeinstitute.net/code_instite_Database/license
********************************************************************************/

/*******************************************************************************
   Drop database if it exists
********************************************************************************/
DROP DATABASE IF EXISTS `code_institute`;


/*******************************************************************************
   Create database
********************************************************************************/
CREATE DATABASE `code_institute`;


USE `code_institute`;


/*******************************************************************************
   Create Tables
********************************************************************************/

--
-- Table structure for table `Staff`
--

CREATE TABLE `Staff` (
  `id` int(11) NOT NULL,
  `firstName` varchar(20) NOT NULL,
  `secondName` varchar(20) NOT NULL,
  `teaching_subjects_id` varchar(20) NOT NULL,
  `staffId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Staff`
--

INSERT INTO `Staff` (`id`, `firstName`, `secondName`, `teaching_subjects_id`, `staffId`) VALUES
(1, 'Richard', 'Dalton', '2', 0),
(2, 'Katie', 'Maxwell', '4', 1),
(8, 'Brian', 'Farah', '22', 8),
(9, 'Matt', 'Kreux', '12', 33),
(14, 'Antonia', 'smith', '24', 44);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `id` int(4) NOT NULL,
  `firstName` varchar(20) DEFAULT NULL,
  `secondName` varchar(20) DEFAULT NULL,
  `studyId` varchar(20) DEFAULT NULL,
  `course` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `firstName`, `secondName`, `studyId`, `course`) VALUES
(1, 'Stevie', 'Bolton', 'python', ''),
(2, 'Daan', 'Franssen', 'python', ''),
(3, 'Dimitar', 'D', 'python', ''),
(4, 'Stein', 'de Vos', 'python', ''),
(5, 'Je', 'Maltana', 'python', ''),
(6, 'Gijs', 'Schilderer', 'python', '');

-- --------------------------------------------------------

--
-- Table structure for table `subjects`
--

CREATE TABLE `subjects` (
  `id` int(4) NOT NULL,
  `teacher` varchar(20) DEFAULT NULL,
  `studyId` varchar(20) DEFAULT NULL,
  `subject` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `subjects`
--

INSERT INTO `subjects` (`id`, `teacher`, `studyId`, `subject`) VALUES
(0, NULL, '1', 'Java Script'),
(1, NULL, '2', 'Python'),
(2, NULL, '3', 'java'),
(3, NULL, '4', 'css'),
(4, NULL, '5', 'php'),
(5, NULL, '6', 'sql');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Staff`
--
ALTER TABLE `Staff`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `teaching_subjects_id` (`teaching_subjects_id`),
  ADD UNIQUE KEY `staffId` (`staffId`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`),
  ADD KEY `study` (`studyId`);

--
-- Indexes for table `subjects`
--
ALTER TABLE `subjects`
  ADD PRIMARY KEY (`id`),
  ADD KEY `studyid` (`studyId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Staff`
--
ALTER TABLE `Staff`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

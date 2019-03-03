-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 03, 2019 at 04:19 AM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.3.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sih`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add action points', 7, 'add_actionpoints'),
(26, 'Can change action points', 7, 'change_actionpoints'),
(27, 'Can delete action points', 7, 'delete_actionpoints'),
(28, 'Can view action points', 7, 'view_actionpoints'),
(29, 'Can add dept_action_points', 8, 'add_dept_action_points'),
(30, 'Can change dept_action_points', 8, 'change_dept_action_points'),
(31, 'Can delete dept_action_points', 8, 'delete_dept_action_points'),
(32, 'Can view dept_action_points', 8, 'view_dept_action_points'),
(33, 'Can add dipp officer', 9, 'add_dippofficer'),
(34, 'Can change dipp officer', 9, 'change_dippofficer'),
(35, 'Can delete dipp officer', 9, 'delete_dippofficer'),
(36, 'Can view dipp officer', 9, 'view_dippofficer'),
(37, 'Can add meeting', 10, 'add_meeting'),
(38, 'Can change meeting', 10, 'change_meeting'),
(39, 'Can delete meeting', 10, 'delete_meeting'),
(40, 'Can view meeting', 10, 'view_meeting'),
(41, 'Can add monitoring_ meeting', 11, 'add_monitoring_meeting'),
(42, 'Can change monitoring_ meeting', 11, 'change_monitoring_meeting'),
(43, 'Can delete monitoring_ meeting', 11, 'delete_monitoring_meeting'),
(44, 'Can view monitoring_ meeting', 11, 'view_monitoring_meeting'),
(45, 'Can add notify', 12, 'add_notify'),
(46, 'Can change notify', 12, 'change_notify'),
(47, 'Can delete notify', 12, 'delete_notify'),
(48, 'Can view notify', 12, 'view_notify'),
(49, 'Can add status report', 13, 'add_statusreport'),
(50, 'Can change status report', 13, 'change_statusreport'),
(51, 'Can delete status report', 13, 'delete_statusreport'),
(52, 'Can view status report', 13, 'view_statusreport'),
(53, 'Can add target', 14, 'add_target'),
(54, 'Can change target', 14, 'change_target'),
(55, 'Can delete target', 14, 'delete_target'),
(56, 'Can view target', 14, 'view_target'),
(57, 'Can add dept officer', 15, 'add_deptofficer'),
(58, 'Can change dept officer', 15, 'change_deptofficer'),
(59, 'Can delete dept officer', 15, 'delete_deptofficer'),
(60, 'Can view dept officer', 15, 'view_deptofficer'),
(61, 'Can add feedback', 16, 'add_feedback'),
(62, 'Can change feedback', 16, 'change_feedback'),
(63, 'Can delete feedback', 16, 'delete_feedback'),
(64, 'Can view feedback', 16, 'view_feedback'),
(65, 'Can add ranking', 17, 'add_ranking'),
(66, 'Can change ranking', 17, 'change_ranking'),
(67, 'Can delete ranking', 17, 'delete_ranking'),
(68, 'Can view ranking', 17, 'view_ranking'),
(69, 'Can add stake holder', 18, 'add_stakeholder'),
(70, 'Can change stake holder', 18, 'change_stakeholder'),
(71, 'Can delete stake holder', 18, 'delete_stakeholder'),
(72, 'Can view stake holder', 18, 'view_stakeholder');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `dept_deptofficer`
--

CREATE TABLE `dept_deptofficer` (
  `dept_loginid` varchar(40) NOT NULL,
  `dept_password` varchar(40) NOT NULL,
  `dept_name` varchar(100) NOT NULL,
  `dept_email` varchar(40) NOT NULL,
  `dept_contact` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dept_deptofficer`
--

INSERT INTO `dept_deptofficer` (`dept_loginid`, `dept_password`, `dept_name`, `dept_email`, `dept_contact`) VALUES
('dept_DB', 'DB', 'Department of Biotechnology', 'db@db.com', '3456789012'),
('dept_DEIT', 'DEIT', 'Department of Electronics and IT', 'deit@deit.com', '5678901234'),
('dept_DHE', 'DHE', 'Department of Higher Education', 'dhe@dhe.com', '2345678901'),
('dept_DST', 'DST', 'Department of Science and Technology', 'dst@dst.com', '4567890123'),
('dept_MHRD', 'MHRD', 'Ministry of Human Resource and Development', 'mhrd@mhrd.com', '6789012345'),
('dept_MSDE', 'MSDE', 'Ministry of Skill Development and Entrepreneurship ', 'msde@msde.com', '7890123456');

-- --------------------------------------------------------

--
-- Table structure for table `dept_feedback`
--

CREATE TABLE `dept_feedback` (
  `id` int(11) NOT NULL,
  `stakeholder` varchar(40) NOT NULL,
  `rating` varchar(40) NOT NULL,
  `date` date NOT NULL,
  `dept` varchar(40) NOT NULL,
  `dept_loginid_id` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `dept_ranking`
--

CREATE TABLE `dept_ranking` (
  `id` int(11) NOT NULL,
  `score1` varchar(40) NOT NULL,
  `score2` varchar(40) NOT NULL,
  `dept_loginid_id` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dept_ranking`
--

INSERT INTO `dept_ranking` (`id`, `score1`, `score2`, `dept_loginid_id`) VALUES
(1, '0', '0', 'dept_DHE'),
(2, '20', '0', 'dept_DB'),
(3, '20', '0', 'dept_DST'),
(4, '0', '0', 'dept_DEIT'),
(5, '0', '0', 'dept_MHRD'),
(6, '0', '0', 'dept_MSDE');

-- --------------------------------------------------------

--
-- Table structure for table `dipp_actionpoints`
--

CREATE TABLE `dipp_actionpoints` (
  `action_no` varchar(2) NOT NULL,
  `action_name` varchar(100) NOT NULL,
  `action_objective` varchar(200) NOT NULL,
  `action_description` varchar(500) NOT NULL,
  `update_time` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dipp_actionpoints`
--

INSERT INTO `dipp_actionpoints` (`action_no`, `action_name`, `action_objective`, `action_description`, `update_time`) VALUES
('1', 'Compliance Regime based on Self-Certification', 'To reduce the regulatory burden on Startups thereby allowing them to focus on their core business and keep compliance cost low', 'Regulatory formalities requiring compliance with various labour and environment laws are time\r\nconsuming and difficult in nature. Often, new and small firms are unaware of nuances of the issues and\r\ncan be subjected to intrusive action by regulatory agencies. In order to make compliance for Startups\r\nfriendly and flexible, simplifications are required in the regulatory regime', '2019-02-26'),
('2', 'Startup India Hub', 'To create a single point of contact for the entire Startup ecosystem and enable knowledge exchange\r\nand access to funding', 'The “Startup India Hub” will be a key stakeholder in this vibrant ecosystem and will:\r\n• Work in a hub and spoke model and collaborate with Central & State governments, Indian and\r\nforeign VCs, angel networks, banks, incubators, legal partners, consultants, universities and R&D\r\ninstitutions\r\n• Assist Startups through their lifecycle with specific focus on important aspects like obtaining\r\nfinancing, feasibility testing, business structuring advisory, enhancement of marketing skills,\r\ntechnology', '2019-02-06'),
('3', 'Rolling-out of Mobile App and Portal', 'To serve as the single platform for Startups for interacting with Government and Regulatory\r\nInstitutions for all business needs and information exchange among various stakeholders', 'Towards these efforts, the Government shall introduce a Mobile App to provide on-the-go accessibility for:\r\n• Registering Startups with relevant agencies of the Government. A simple form shall be made\r\navailable for the same. The Mobile App shall have backend integration with Ministry of Corporate\r\nAffairs and Registrar of Firms for seamless information exchange and processing of the\r\nregistration application\r\n• Tracking the status of the registration application and anytime downloading of the r', '2019-03-01'),
('4', 'Legal Support and Fast-tracking Patent Examination at\r\nLower Costs', 'To promote awareness and adoption of IPRs by Startups and facilitate them in protecting and\r\ncommercializing the IPRs by providing access to high quality Intellectual Property services and\r\nresources,', 'Intellectual Property Rights (IPR) are emerging as a strategic business tool for any business\r\norganization to enhance industrial competitiveness. Startups with limited resources and manpower,\r\ncan sustain in this highly competitive world only through continuous growth and development oriented\r\ninnovations; for this, it is equally crucial that they protect their IPRs. The scheme for Startup Intellectual\r\nProperty Protection (SIPP) shall facilitate filing of Patents, Trademarks and Designs by inn', '2019-03-02'),
('5', 'Relaxed Norms of Public Procurement for Startups', 'To provide an equal platform to Startups (in the manufacturing sector) vis-à-vis the experienced\r\nentrepreneurs/ companies in public procurement', 'In order to promote Startups, Government shall exempt Startups (in the manufacturing sector) from\r\nthe criteria of “prior experience/ turnover” without any relaxation in quality standards or technical\r\nparameters. The Startups will also have to demonstrate requisite capability to execute the project as\r\nper the requirements and should have their own manufacturing facility in India.', '2019-02-01'),
('6', 'Faster Exit for Startups', 'To make it easier for Startups to wind up operations', 'In terms of the IBB, Startups with simple debt structures or those meeting such criteria as may be\r\nspecified may be wound up within a period of 90 days from making of an application for winding up on\r\na fast track basis. In such instances, an insolvency professional shall be appointed for the Startup, who\r\nshall be in charge of the company (the promoters and management shall no longer run the company)\r\nfor liquidating its assets and paying its creditors within six months of such appointment. On', '2019-03-01');

-- --------------------------------------------------------

--
-- Table structure for table `dipp_dept_action_points`
--

CREATE TABLE `dipp_dept_action_points` (
  `id` int(11) NOT NULL,
  `actionpoint_no_id` varchar(2) NOT NULL,
  `department_id` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dipp_dept_action_points`
--

INSERT INTO `dipp_dept_action_points` (`id`, `actionpoint_no_id`, `department_id`) VALUES
(1, '3', 'dept_DHE'),
(2, '4', 'dept_DB'),
(3, '6', 'dept_DB'),
(4, '2', 'dept_DST'),
(5, '3', 'dept_DST'),
(6, '1', 'dept_DEIT'),
(7, '5', 'dept_DEIT'),
(8, '4', 'dept_MHRD'),
(9, '5', 'dept_MHRD'),
(10, '1', 'dept_MSDE'),
(11, '2', 'dept_MSDE');

-- --------------------------------------------------------

--
-- Table structure for table `dipp_dippofficer`
--

CREATE TABLE `dipp_dippofficer` (
  `id` int(11) NOT NULL,
  `dipp_loginid` varchar(40) NOT NULL,
  `dipp_password` varchar(40) NOT NULL,
  `dipp_email` varchar(40) NOT NULL,
  `dipp_contact` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dipp_dippofficer`
--

INSERT INTO `dipp_dippofficer` (`id`, `dipp_loginid`, `dipp_password`, `dipp_email`, `dipp_contact`) VALUES
(1, 'DIPP', 'DIPP', 'dipp@dipp.com', '1234567890');

-- --------------------------------------------------------

--
-- Table structure for table `dipp_meeting`
--

CREATE TABLE `dipp_meeting` (
  `id` int(11) NOT NULL,
  `meeting_date` date NOT NULL,
  `subject` varchar(40) NOT NULL,
  `meeting_time` time(6) NOT NULL,
  `upload_minute` varchar(100) DEFAULT NULL,
  `description` longtext NOT NULL,
  `with_whom_id` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `dipp_monitoring_meeting`
--

CREATE TABLE `dipp_monitoring_meeting` (
  `id` int(11) NOT NULL,
  `meeting_date` date NOT NULL,
  `subject` varchar(40) NOT NULL,
  `meeting_time` time(6) NOT NULL,
  `upload_minute` varchar(100) DEFAULT NULL,
  `description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dipp_monitoring_meeting`
--

INSERT INTO `dipp_monitoring_meeting` (`id`, `meeting_date`, `subject`, `meeting_time`, `upload_minute`, `description`) VALUES
(1, '2019-03-03', 'Funding for startups', '12:30:00.000000', 'not uploaded', 'Discussion on Funding of Startups for year 2019-2020.');

-- --------------------------------------------------------

--
-- Table structure for table `dipp_notify`
--

CREATE TABLE `dipp_notify` (
  `id` int(11) NOT NULL,
  `when` date NOT NULL,
  `subject` varchar(40) NOT NULL,
  `type` varchar(40) NOT NULL,
  `desc` varchar(400) NOT NULL,
  `department` varchar(40) NOT NULL,
  `actionpoint_no_id` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `dipp_statusreport`
--

CREATE TABLE `dipp_statusreport` (
  `id` int(11) NOT NULL,
  `date_of_upload` date NOT NULL,
  `month` varchar(40) NOT NULL,
  `upload_statusreport` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dipp_statusreport`
--

INSERT INTO `dipp_statusreport` (`id`, `date_of_upload`, `month`, `upload_statusreport`) VALUES
(1, '2019-03-03', '2019-01', '/media/Np_Complete.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `dipp_target`
--

CREATE TABLE `dipp_target` (
  `id` int(11) NOT NULL,
  `date_of_assignment` date NOT NULL,
  `end_date` date NOT NULL,
  `status` varchar(10) NOT NULL,
  `desc_of_target` varchar(400) NOT NULL,
  `report` varchar(400) NOT NULL,
  `actionpoint_no_id` varchar(2) NOT NULL,
  `department_id` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dipp_target`
--

INSERT INTO `dipp_target` (`id`, `date_of_assignment`, `end_date`, `status`, `desc_of_target`, `report`, `actionpoint_no_id`, `department_id`) VALUES
(1, '2019-03-03', '2019-03-29', '1', '2 Incubation Centers', 'Setted up 2 incubation centers.', '4', 'dept_DB'),
(2, '2019-03-03', '2019-03-17', '0', '10 Startup Funding', 'Funded 2 startups.\r\nFurther , funded 1 startup.', '6', 'dept_DB'),
(3, '2019-03-03', '2019-03-14', '0', 'Publish 1 Mobile App', 'not updated yet', '1', 'dept_DEIT'),
(4, '2019-03-03', '2019-03-16', '0', '5 Startup Funding', 'Funded 1 startup.', '5', 'dept_DEIT'),
(5, '2019-03-03', '2019-03-14', '0', '2 Incubation Centers', '1 incubation centers established.', '3', 'dept_DHE'),
(6, '2019-03-03', '2019-03-28', '1', 'Roll out 2 mobile apps', 'Rolled out mobile apps together.', '2', 'dept_DST'),
(7, '2019-03-03', '2019-03-20', '0', 'Set up 3 websites.', 'Set up 2 websites.', '3', 'dept_DST'),
(8, '2019-03-03', '2019-03-21', '0', 'Set up 4 incubation centers', 'Established 1 Incubation center', '4', 'dept_MHRD'),
(9, '2019-03-03', '2019-03-18', '0', 'Set up 2 R&D Labs', 'Setted up 1 IC.', '4', 'dept_MHRD'),
(10, '2019-03-03', '2019-03-29', '0', 'Arrange 5 camps for skill enhancement', 'Arranged all 5 camps in single day at 5 locations.', '1', 'dept_MSDE'),
(11, '2019-03-03', '2019-03-27', '0', 'Arrange 10 bridge courses.', 'not updated yet', '2', 'dept_MSDE');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(15, 'dept', 'deptofficer'),
(16, 'dept', 'feedback'),
(17, 'dept', 'ranking'),
(7, 'dipp', 'actionpoints'),
(8, 'dipp', 'dept_action_points'),
(9, 'dipp', 'dippofficer'),
(10, 'dipp', 'meeting'),
(11, 'dipp', 'monitoring_meeting'),
(12, 'dipp', 'notify'),
(13, 'dipp', 'statusreport'),
(14, 'dipp', 'target'),
(6, 'sessions', 'session'),
(18, 'stk_hld', 'stakeholder');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-03-03 00:41:05.942209'),
(2, 'auth', '0001_initial', '2019-03-03 00:41:13.070703'),
(3, 'admin', '0001_initial', '2019-03-03 00:41:15.277837'),
(4, 'admin', '0002_logentry_remove_auto_add', '2019-03-03 00:41:15.307836'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2019-03-03 00:41:15.363934'),
(6, 'contenttypes', '0002_remove_content_type_name', '2019-03-03 00:41:16.433598'),
(7, 'auth', '0002_alter_permission_name_max_length', '2019-03-03 00:41:17.086125'),
(8, 'auth', '0003_alter_user_email_max_length', '2019-03-03 00:41:17.680401'),
(9, 'auth', '0004_alter_user_username_opts', '2019-03-03 00:41:17.730390'),
(10, 'auth', '0005_alter_user_last_login_null', '2019-03-03 00:41:18.201904'),
(11, 'auth', '0006_require_contenttypes_0002', '2019-03-03 00:41:18.248768'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2019-03-03 00:41:18.297303'),
(13, 'auth', '0008_alter_user_username_max_length', '2019-03-03 00:41:19.086545'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2019-03-03 00:41:19.806102'),
(15, 'dept', '0001_initial', '2019-03-03 00:41:22.617234'),
(16, 'dipp', '0001_initial', '2019-03-03 00:41:30.048862'),
(17, 'sessions', '0001_initial', '2019-03-03 00:41:30.537126'),
(18, 'stk_hld', '0001_initial', '2019-03-03 00:41:30.763815');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('vudpx2hvgbgyqcwu9kkk2gdu3esosf4f', 'YjllYzU0NTYyYzk2YTlhM2FlYjkwODA2ODA2ZmQ5ZjQ4NjNkOTUzMTp7InNoX3VzZXJuYW1lIjoiU1RBS0UifQ==', '2019-03-17 03:18:45.829872');

-- --------------------------------------------------------

--
-- Table structure for table `stk_hld_stakeholder`
--

CREATE TABLE `stk_hld_stakeholder` (
  `id` int(11) NOT NULL,
  `stk_loginid` varchar(40) NOT NULL,
  `stk_password` varchar(40) NOT NULL,
  `stk_name` varchar(100) NOT NULL,
  `stk_email` varchar(40) NOT NULL,
  `stk_contact` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `stk_hld_stakeholder`
--

INSERT INTO `stk_hld_stakeholder` (`id`, `stk_loginid`, `stk_password`, `stk_name`, `stk_email`, `stk_contact`) VALUES
(1, 'STAKE', 'STAKE', 'StakeHolder', 'stake@stake.com', '2345678901');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `dept_deptofficer`
--
ALTER TABLE `dept_deptofficer`
  ADD PRIMARY KEY (`dept_loginid`);

--
-- Indexes for table `dept_feedback`
--
ALTER TABLE `dept_feedback`
  ADD PRIMARY KEY (`id`),
  ADD KEY `dept_feedback_dept_loginid_id_f2fd06a9_fk_dept_dept` (`dept_loginid_id`);

--
-- Indexes for table `dept_ranking`
--
ALTER TABLE `dept_ranking`
  ADD PRIMARY KEY (`id`),
  ADD KEY `dept_ranking_dept_loginid_id_a45b58c5_fk_dept_dept` (`dept_loginid_id`);

--
-- Indexes for table `dipp_actionpoints`
--
ALTER TABLE `dipp_actionpoints`
  ADD PRIMARY KEY (`action_no`);

--
-- Indexes for table `dipp_dept_action_points`
--
ALTER TABLE `dipp_dept_action_points`
  ADD PRIMARY KEY (`id`),
  ADD KEY `dipp_dept_action_poi_actionpoint_no_id_0401ef67_fk_dipp_acti` (`actionpoint_no_id`),
  ADD KEY `dipp_dept_action_poi_department_id_04a8ac0e_fk_dept_dept` (`department_id`);

--
-- Indexes for table `dipp_dippofficer`
--
ALTER TABLE `dipp_dippofficer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dipp_meeting`
--
ALTER TABLE `dipp_meeting`
  ADD PRIMARY KEY (`id`),
  ADD KEY `dipp_meeting_with_whom_id_dc4fb8b9_fk_dept_dept` (`with_whom_id`);

--
-- Indexes for table `dipp_monitoring_meeting`
--
ALTER TABLE `dipp_monitoring_meeting`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dipp_notify`
--
ALTER TABLE `dipp_notify`
  ADD PRIMARY KEY (`id`),
  ADD KEY `dipp_notify_actionpoint_no_id_abadc699_fk_dipp_acti` (`actionpoint_no_id`);

--
-- Indexes for table `dipp_statusreport`
--
ALTER TABLE `dipp_statusreport`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dipp_target`
--
ALTER TABLE `dipp_target`
  ADD PRIMARY KEY (`id`),
  ADD KEY `dipp_target_actionpoint_no_id_bb9386e9_fk_dipp_acti` (`actionpoint_no_id`),
  ADD KEY `dipp_target_department_id_09e8d4e0_fk_dept_dept` (`department_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `stk_hld_stakeholder`
--
ALTER TABLE `stk_hld_stakeholder`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `dept_feedback`
--
ALTER TABLE `dept_feedback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `dept_ranking`
--
ALTER TABLE `dept_ranking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `dipp_dept_action_points`
--
ALTER TABLE `dipp_dept_action_points`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `dipp_dippofficer`
--
ALTER TABLE `dipp_dippofficer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `dipp_meeting`
--
ALTER TABLE `dipp_meeting`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `dipp_monitoring_meeting`
--
ALTER TABLE `dipp_monitoring_meeting`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `dipp_notify`
--
ALTER TABLE `dipp_notify`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `dipp_statusreport`
--
ALTER TABLE `dipp_statusreport`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `dipp_target`
--
ALTER TABLE `dipp_target`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `stk_hld_stakeholder`
--
ALTER TABLE `stk_hld_stakeholder`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `dept_feedback`
--
ALTER TABLE `dept_feedback`
  ADD CONSTRAINT `dept_feedback_dept_loginid_id_f2fd06a9_fk_dept_dept` FOREIGN KEY (`dept_loginid_id`) REFERENCES `dept_deptofficer` (`dept_loginid`);

--
-- Constraints for table `dept_ranking`
--
ALTER TABLE `dept_ranking`
  ADD CONSTRAINT `dept_ranking_dept_loginid_id_a45b58c5_fk_dept_dept` FOREIGN KEY (`dept_loginid_id`) REFERENCES `dept_deptofficer` (`dept_loginid`);

--
-- Constraints for table `dipp_dept_action_points`
--
ALTER TABLE `dipp_dept_action_points`
  ADD CONSTRAINT `dipp_dept_action_poi_actionpoint_no_id_0401ef67_fk_dipp_acti` FOREIGN KEY (`actionpoint_no_id`) REFERENCES `dipp_actionpoints` (`action_no`),
  ADD CONSTRAINT `dipp_dept_action_poi_department_id_04a8ac0e_fk_dept_dept` FOREIGN KEY (`department_id`) REFERENCES `dept_deptofficer` (`dept_loginid`);

--
-- Constraints for table `dipp_meeting`
--
ALTER TABLE `dipp_meeting`
  ADD CONSTRAINT `dipp_meeting_with_whom_id_dc4fb8b9_fk_dept_dept` FOREIGN KEY (`with_whom_id`) REFERENCES `dept_deptofficer` (`dept_loginid`);

--
-- Constraints for table `dipp_notify`
--
ALTER TABLE `dipp_notify`
  ADD CONSTRAINT `dipp_notify_actionpoint_no_id_abadc699_fk_dipp_acti` FOREIGN KEY (`actionpoint_no_id`) REFERENCES `dipp_actionpoints` (`action_no`);

--
-- Constraints for table `dipp_target`
--
ALTER TABLE `dipp_target`
  ADD CONSTRAINT `dipp_target_actionpoint_no_id_bb9386e9_fk_dipp_acti` FOREIGN KEY (`actionpoint_no_id`) REFERENCES `dipp_actionpoints` (`action_no`),
  ADD CONSTRAINT `dipp_target_department_id_09e8d4e0_fk_dept_dept` FOREIGN KEY (`department_id`) REFERENCES `dept_deptofficer` (`dept_loginid`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

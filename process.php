<?php

// Get the form data
$name = $_POST["name"];
$email = $_POST["email"];
$phone = $_POST["phone"];
$address = $_POST["address"];
$dob = $_POST["dob"];
$educational_background = $_POST["educational_background"];
$work_experience = $_POST["work_experience"];

// Connect to the database
$db = new PDO("mysql:host=localhost;dbname=mydb", "root", "");

// Insert the data into the database
$sql = "INSERT INTO users (name, email, phone, address, dob, educational_background, work_experience) VALUES (?, ?, ?, ?, ?, ?, ?)";
$stmt = $db->prepare($sql);
$stmt->execute(array($name, $email, $phone, $address, $dob, $educational_background, $work_experience));

// Send an email confirmation to the user
$message = "Dear $name,

Thank you for submitting your admission form. We will be in touch soon to let you know about the status of your application.

Sincerely,
The Admissions Team";

mail($email, "Admission Confirmation", $message);

?>

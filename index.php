<?php

$courses = json_decode(file_get_contents("database.json"));

function filterCourses($courses, $criteria) {
    $filteredCourses = array();
    foreach ($courses as $course) {
        if (isset($course[$criteria])) {
            $filteredCourses[] = $course;
        }
    }
    return $filteredCourses;
}

function displayCourses($courses) {
    foreach ($courses as $course) {
        echo $course . "<br>";
    }
}

$criteria = $_POST["criteria"];
$filteredCourses = filterCourses($courses, $criteria);
displayCourses($filteredCourses);

?>

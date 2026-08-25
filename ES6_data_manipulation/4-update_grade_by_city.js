// Function: updateStudentGradeByCity
// Purpose: Return students from a specific city with their updated grade
// Params:
//   students (Array) - list of student objects
//   city (String) - location to filter by
//   newGrades (Array) - list of objects: { studentId: Number, grade: Number }
// Returns: Array of student objects with an added 'grade' field

export default function updateStudentGradeByCity(students, city, newGrades) {
  if (!Array.isArray(students)) {
    return [];
  }

  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const gradeObj = newGrades.find((g) => g.studentId === student.id);
      return {
        ...student,
        grade: gradeObj ? gradeObj.grade : 'N/A',
      };
    });
}

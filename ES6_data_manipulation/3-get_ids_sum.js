// Function: getStudentIdsSum
// Purpose: Return the sum of all student IDs
// Params:
//   students (Array) - list of student objects
// Returns: Number - sum of IDs, or 0 if input is invalid

export default function getStudentIdsSum(students) {
  if (!Array.isArray(students)) {
    return 0;
  }

  return students.reduce((total, student) => total + student.id, 0);
}

// Function: getListStudentIds
// Purpose: Return an array of student IDs from an array of student objects
// Params: students (Array) - must match the format from getListStudents()
// Returns: Array of Numbers (IDs) or an empty array if input is not an array

export default function getListStudentIds(students) {
  if (!Array.isArray(students)) {
    return [];
  }

  return students.map((student) => student.id);
}

const fs = require('fs');

function countStudents(path) {
  try {
    // Read the database file synchronously using the path passed as argument
    const data = fs.readFileSync(path, 'utf8');

    // Split the file content into lines and remove empty lines
    const lines = data
      .split('\n')
      .filter((line) => line.trim() !== '');

    // Remove the first line because it is the CSV header
    const students = lines.slice(1);

    // Display the total number of valid students
    console.log(`Number of students: ${students.length}`);

    // Create an object to group student first names by field
    const fields = {};

    // Loop through every student row from the CSV file
    students.forEach((student) => {
      // Extract the firstname and field columns from the CSV row
      const [firstname, , , field] = student.split(',');

      // If this field does not exist yet, create an empty array for it
      if (!fields[field]) {
        fields[field] = [];
      }

      // Add the student's firstname to the correct field
      fields[field].push(firstname);
    });

    // Display the number of students and the list of first names for each field
    for (const [field, list] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
    }
  } catch (error) {
    // Throw the required error message if the database cannot be loaded
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;

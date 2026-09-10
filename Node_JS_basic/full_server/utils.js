import fs from 'fs';

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (error, data) => {
      if (error) {
        reject(error);
        return;
      }

      try {
        // Split into lines and filter out empty lines
        const lines = data.split('\n').filter((line) => line.trim() !== '');

        // Remove header line
        const students = lines.slice(1);

        // Group students by field
        const fields = {};

        students.forEach((student) => {
          const [firstname, , , field] = student.split(',');

          // Trim the field to avoid problems with spaces or Windows line endings
          const trimmedField = field.trim();

          if (!fields[trimmedField]) {
            fields[trimmedField] = [];
          }

          fields[trimmedField].push(firstname);
        });

        resolve(fields);
      } catch (parseError) {
        reject(parseError);
      }
    });
  });
}

export default readDatabase;

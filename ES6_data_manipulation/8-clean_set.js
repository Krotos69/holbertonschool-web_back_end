// Function: cleanSet
// Purpose: Return a string of set values that start with a given prefix,
//          removing the prefix and joining the rest with '-'
// Params:
//   set (Set) - collection of strings
//   startString (String) - prefix to match
// Returns: String - cleaned values joined by '-'

export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') {
    return '';
  }

  const result = [];

  for (const value of set) {
    if (typeof value === 'string' && value.startsWith(startString)) {
      result.push(value.slice(startString.length));
    }
  }

  return result.join('-');
}

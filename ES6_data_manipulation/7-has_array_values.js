// Function: hasValuesFromArray
// Purpose: Check if all elements in an array exist in a given Set
// Params:
//   set (Set) - the set to check against
//   array (Array) - list of values to verify
// Returns: Boolean - true if all array values are in the set

export default function hasValuesFromArray(set, array) {
  for (const value of array) {
    if (!set.has(value)) {
      return false;
    }
  }
  return true;
}

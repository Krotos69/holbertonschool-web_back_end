// Function: createInt8TypedArray
// Purpose: Create an ArrayBuffer and store an Int8 value at a specific position
// Params:
//   length (Number) - size of the buffer
//   position (Number) - index where the Int8 value should be stored
//   value (Number) - the Int8 value to write
// Returns: DataView with the value set, or throws an error if position is invalid

export default function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  const buffer = new ArrayBuffer(length);
  const view = new DataView(buffer);

  view.setInt8(position, value);

  return view;
}

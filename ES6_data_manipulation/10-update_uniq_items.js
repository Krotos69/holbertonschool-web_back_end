// Function: updateUniqueItems
// Purpose: Update all items in a Map that have quantity 1 to quantity 100
// Params:
//   map (Map) - a Map of grocery items and their quantities
// Returns: Map - the same Map instance with updated quantities
// Throws: Error('Cannot process') if the argument is not a Map

export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }

  map.forEach((quantity, item) => {
    if (quantity === 1) {
      map.set(item, 100);
    }
  });

  return map;
}

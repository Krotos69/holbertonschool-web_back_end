// Function: groceriesList
// Purpose: Return a Map containing grocery items and their quantities
// Params: None
// Returns: Map - keys are item names, values are quantities

export default function groceriesList() {
  const groceries = new Map();

  groceries.set('Apples', 10);
  groceries.set('Tomatoes', 10);
  groceries.set('Pasta', 1);
  groceries.set('Rice', 1);
  groceries.set('Banana', 5);

  return groceries;
}

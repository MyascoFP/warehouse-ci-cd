
# Application Features

## Adding materials

The `add_material()` method adds a material
to the warehouse.

## Getting material balance

The `get_balance()` method returns the
available quantity of a material.

## Writing off materials

The `write_off()` method decreases the
available material quantity.

The operation validates that the requested
quantity is positive and that sufficient
stock is available.

## Calculating total quantity

The `get_total_quantity()` method calculates
the total quantity of all warehouse materials.

## Continuous Integration

All application changes are automatically
tested with GitHub Actions.
from sqlalchemy import Integer, String, Boolean

# Structural Testing
# Table and Column Validation


# 1. Confirm the presence of all required tables within the database schema.
def test_model_structure_table_exists(db_inspector):
    assert db_inspector.has_table("category")


# 2.  Validate the existence of expected columns in each table, ensuring correct data types.
def test_model_structure_column_data_types(db_inspector):
    table = "category"
    columns = db_inspector.get_columns(table)
    columns = {column["name"]: column for column in columns}

    assert isinstance(columns["id"]["type"], Integer)
    assert isinstance(columns["name"]["type"], String)
    assert isinstance(columns["slug"]["type"], String)
    assert isinstance(columns["is_active"]["type"], Boolean)
    assert isinstance(columns["level"]["type"], Integer)
    assert isinstance(columns["parent_id"]["type"], Integer)


# 3. Verify nullable or not nullable fields
def test_model_structure_nullable_constraint(db_inspector):
    table = "category"
    columns = db_inspector.get_columns(table)
    expected_nullables = {
        "id": False,
        "name": False,
        "slug": False,
        "is_active": False,
        "level": False,
        "parent_id": True
    }
    for column in columns:
        column_name = column["name"]
        actual_nullable = column["nullable"]
        expected_nullable = expected_nullables.get(column_name)
        assert actual_nullable == expected_nullable, f"""
        Column {column_name} has a different nullable constraint than
        expected.
        """


# 4.  Test columns with specific constraints to ensure they are accurately defined.
def test_model_structure_constraints(db_inspector):
    table = "category"
    constraints = db_inspector.get_check_constraints(table)
    print(constraints)
    assert any(constraint["name"] == "name_length_check" for constraint in constraints)
    assert any(constraint["name"] == "slug_length_check" for constraint in constraints)


# 5. Verify the correctness of default values for relevant columns.
def test_model_structure_default_values(db_inspector):
    table = "category"
    columns = db_inspector.get_columns(table)
    columns = {column["name"]: column for column in columns}

    assert columns["is_active"]["default"] == "false"
    assert columns["level"]["default"] == "100"


# 6. Ensure that column lengths align with defined requirements.
def test_model_structure_column_lengths(db_inspector):
    table = "category"
    columns = db_inspector.get_columns(table)
    columns = {column["name"]: column for column in columns}

    assert columns["name"]["type"].length == 100
    assert columns["slug"]["type"].length == 120


# 7. Test columns with specific constraints to ensure they are accurately defined.
def test_model_structure_unique_constraints(db_inspector):
    table = "category"
    constraints = db_inspector.get_unique_constraints(table)

    assert any(constraint['name'] == "uq_category_name_level" for constraint in constraints)
    assert any(constraint['name'] == "uq_category_slug" for constraint in constraints)

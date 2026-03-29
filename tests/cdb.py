import dbc

with dbc.build_db("test.db","SQLite") as db:
    db.create_table("TEST", {"name":{"type":"TEXT"},"age":{"type":"INT"}})
    db.add_data("TEST",["'yuki'",999])

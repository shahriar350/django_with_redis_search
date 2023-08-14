from redis_om import JsonModel, Field, EmbeddedJsonModel, Migrator


class CategoryPydantic(EmbeddedJsonModel):
    uid: str = Field(index=False)
    name: str = Field(index=False)


class EmployeePydantic(JsonModel):
    uid: str = Field(index=False)
    name: str = Field(index=True, full_text_search=True)
    department: str = Field(index=False)
    category = CategoryPydantic


Migrator().run()

import glob
import pathlib

data_type_mappings = {
    "varchar": "DataTypes.STRING",
    "int": "DataTypes.NUMBER",
    "date": "DataTypes.DATEONLY",
    "bit": "DataTypes.BOOLEAN",
    "numeric": "DataTypes.NUMBER",
    "datetime": "'TIMESTAMP'",
}

modes_path = "./models/*"
schemas_path = "./schemas"
pathlib.Path(schemas_path).mkdir(parents=True, exist_ok=True)

def generate_schema(model_file_path):
    table_name = ""
    schema_name = ""
    model_name = ""
    table_column_mappings = ""

    model_file_contents = open(model_file_path, "r")
    for i, line in enumerate(model_file_contents):
        if i == 0:
            print("first line with table name")
            first_line = line
            table_name = (first_line.split("].["))[1].split("](")[0]
            print("table_name", table_name)
            schema_name = table_name.casefold()
            model_name = table_name.capitalize() + "Model"
            print("schema_name", schema_name)
        elif i == 1:
            print("second line with id column")
        else:
            if line.find(") ON", 0, 4) == -1: #Not Last list
                column_name = (line.split("]")[0]).split("[")[1]
                data_type = (line.split("] [")[1]).split("]")[0]
                data_type_mapping = "UNKNOWN_DATA_TYPE"
                if data_type in data_type_mappings:
                    data_type_mapping = data_type_mappings[data_type]
                table_column_mappings += " \t " + column_name + ": { \n"
                table_column_mappings += "  \t\t type: " + data_type_mapping
                if line.find("NOT NULL") != -1:
                    print(column_name, "-", "Not null")
                    table_column_mappings += ", \n  \t\t allowNull : false" + "\n"
                else:
                    table_column_mappings += "\n"
                    print(column_name, "-", "Null")
                table_column_mappings += "  \t }, \n"
            else:
                print("last column")

    model_file_contents.close()

    schema_content = "const " + model_name + " = sequelize.define('" + model_name + "', {" + "\n" + table_column_mappings + "\n" + "}, { " + "\n \t" + "tableName: '" + table_name + "', \n \t" + "timestamps: " + "false" + ", \n" + "});"

    schema_file_path = schemas_path + "/" + schema_name + ".js"
    f = open(schema_file_path, "w")
    f.write(schema_content)
    f.close()

model_files = glob.glob(modes_path)
for model_file_path in model_files:
    generate_schema(model_file_path)

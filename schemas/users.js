const UsersModel = sequelize.define('UsersModel', {
    created_at: {
        type: 'TIMESTAMP',
        allowNull: false
    },
    updated_at: {
        type: 'TIMESTAMP',
        allowNull: false
    },
    last_name: {
        type: DataTypes.STRING,
        allowNull: false
    },
    middle_name: {
        type: DataTypes.STRING
    },
    first_name: {
        type: DataTypes.STRING,
        allowNull: false
    },

}, {
    tableName: 'USERS',
    timestamps: false,
});
import java.sql.*;

public class ZipCodeDAO {
    private Connection c;

    public ZipCodeDAO(Connection c){
        this.c = c;
    }
    public void persist(ZipCode zipcode) throws SQLException {
        if(zipcode.getId()==null) {
            try(PreparedStatement ps=
                        c.prepareStatement("INSERT INTO zipcode (id, name) VALUES(DEFAULT, ?);",
                                Statement.RETURN_GENERATED_KEYS)) {
                ps.setString(1, zipcode.getName());
                ps.execute();
                try (ResultSet generatedKeys = ps.getGeneratedKeys()) {
                    if (generatedKeys.next()) {
                        zipcode.setId(generatedKeys.getLong(1));
                    } else {
                        throw new SQLException("Presisting zipcode failed, no ID obtained.");
                    }
                }
            }
        }
    }
}

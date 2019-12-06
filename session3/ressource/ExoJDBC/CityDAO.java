import java.sql.*;
import java.util.Iterator;
import java.util.List;

public class CityDAO {
    Connection c;
    public CityDAO(Connection c){
        this.c = c;
    }

    public void persist(List<City> cities) throws SQLException {
        try(PreparedStatement ps=
                    c.prepareStatement("INSERT INTO city (id, name, latitude, longitude)"
                                    +" VALUES(DEFAULT, ?, ?, ?);",
                            Statement.RETURN_GENERATED_KEYS);
        PreparedStatement assocs= c.prepareStatement("INSERT INTO city_zipcode(city_id, zipcode_id) VALUES(?, ?);")) {
            for(City c : cities){
                ps.setString(1, c.getName());
                ps.setDouble(2, c.getLatitude());
                ps.setDouble(3, c.getLongitude());
                ps.addBatch();
            }
            ps.executeBatch();
            try (ResultSet generatedKeys = ps.getGeneratedKeys()) {
                Iterator<City> it = cities.iterator();
                while(generatedKeys.next()) {
                    long cityId = generatedKeys.getLong(1);
                    City city = it.next();
                    city.setId(cityId);
                    for(ZipCode z : city.getZipCodes()) {
                        assocs.setLong(1,cityId);
                        assocs.setLong(2, z.getId());
                        assocs.addBatch();
                    }
                    assocs.executeBatch();
                }
            }
        }

    }
}

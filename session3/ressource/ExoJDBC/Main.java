import java.io.IOException;
import java.sql.*;
import java.util.*;

public class Main {
    private static final String createCityTable="CREATE TABLE IF NOT EXISTS city (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, latitude float NOT NULL, longitude float NOT NULL); ";
    private static final String createZipCodeTable="CREATE TABLE IF NOT EXISTS zipcode (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL);";
    private static final String createCityZipCodeTable="CREATE TABLE IF NOT EXISTS city_zipcode (city_id INTEGER REFERENCES city(id), zipcode_id INTEGER REFERENCES zipcode(id), CONSTRAINT city_zipcode_pk PRIMARY KEY (city_id, zipcode_id));";

    private static final Map<String, String> pgInfo= new HashMap<String, String>();
    private static final Map<String, String> h2Info= new HashMap<String, String>();
    static {
        pgInfo.put("DRIVER", "org.postgresql.Driver");
        pgInfo.put("URL", "jdbc:postgresql://localhost:5432/postgres");
        pgInfo.put("USER", "dbuser");
        pgInfo.put("PASSWD", "*****");
        h2Info.put("DRIVER", "org.h2.Driver");
        h2Info.put("URL", "jdbc:h2:mem:test");
        h2Info.put("USER", "sa");
        h2Info.put("PASSWD", "");
    }
        public static void main(String[] args) throws ClassNotFoundException, SQLException, IOException {
        long start= System.nanoTime();
        List<City> res = null;
        Map<String, String> dbInfo = pgInfo;
        Class.forName(dbInfo.get("DRIVER"));
        try (Connection conn = DriverManager.getConnection(dbInfo.get("URL")
                , dbInfo.get("USER"), dbInfo.get("PASSWD"))) {
            createTables(conn);
            CsvReader reader = new CsvReader(conn);
            res = reader.read("/home/bernard/Downloads/villes_france.csv");
        } catch (SQLException e) {
            e.printStackTrace();
        }
        System.out.println("elapsed time :"+((System.nanoTime()-start)/1e9));
        System.out.println("done");
        System.out.println(findLargestByZipCodes(res));
        System.out.println(findLargestByCities(allZipCodes(res)));
    }

    private static void createTables(Connection c) throws SQLException {
        try(Statement s= c.createStatement()) {
            s.execute(createCityTable);
            s.execute(createZipCodeTable);
            s.execute(createCityZipCodeTable);
        }
    }

    private static Set<ZipCode> allZipCodes(Collection<City> cities){
        Set<ZipCode> res = new HashSet<ZipCode>();
        for(City city : cities){
            res.addAll(city.getZipCodes());
        }
        return res;
    }
    private static City findLargestByZipCodes(Collection<City> cities) {
        City res = null;
        for (City city : cities) {
            if ((res == null)
                    || (res.getZipCodes().size() < city.getZipCodes().size())) {
                res = city;
            }
        }
        return res;
    }
    private static ZipCode findLargestByCities(Collection<ZipCode> zipCodes){
        ZipCode res = null;
        for(ZipCode zipCode : zipCodes){
            if((res == null)||(res.getCities().size() < zipCode.getCities().size())){
                res = zipCode;
            }
        }
        return res;
    }
}
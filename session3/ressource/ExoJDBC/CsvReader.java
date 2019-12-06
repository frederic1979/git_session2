import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVRecord;

import java.io.*;
import java.sql.Connection;
import java.sql.SQLException;
import java.util.*;

public class CsvReader {
    private Connection c;
    private ZipCodeDAO zDao;
    private CityDAO cDao;
    Map<String, ZipCode> insertedZipCodes = new HashMap<String, ZipCode>();

    private static final String[] HEADERS = {"id","county", "slug", "name",
    "simple-name", "real-name", "soundex-name", "metaphone-name", "zipcodes",
    "commune-nb", "INSEE-code","arrondissement", "canton", "pop-2010", "pop-1999", "pop-2012"
    ,"pop-density-2010", "area", "long-deg", "lat-deg", "long-grd", "lat-grd"
    ,"long-dms", "lat-dms", "z-min", "z-max"};

    public CsvReader(Connection c) {
        this.c = c;
        this.zDao = new ZipCodeDAO(c);
        this.cDao = new CityDAO(c);
    }
//TODO : transactions ?
    public List<City> read(String filename) throws IOException, SQLException {
        List<City> res = new ArrayList<City>();
        Reader in = new FileReader(filename);
        Iterable<CSVRecord> records = CSVFormat.DEFAULT
                .withHeader(HEADERS)
                .parse(in);
        for (CSVRecord record : records) {
            String[] zipCodesStrings = record.get("zipcodes").split("-");
            Set<ZipCode> zipCodes = new HashSet<ZipCode>();
            for (String z : zipCodesStrings) {
                zipCodes.add(interned(z));
            }
            City city = new City(record.get("real-name"), Double.parseDouble(record.get("lat-deg")),
                    Double.parseDouble(record.get("long-deg")), zipCodes);
            for(ZipCode zipCode : zipCodes){
                zipCode.addCity(city);
            }
            res.add(city);
        }
        cDao.persist(res);
        return res;
    }
    private ZipCode interned(String code) throws SQLException {
        ZipCode res = insertedZipCodes.get(code);
        if (res == null) {
            res = new ZipCode(code);
            zDao.persist(res);
            insertedZipCodes.put(code,res);
        }
        return res;
    }
}

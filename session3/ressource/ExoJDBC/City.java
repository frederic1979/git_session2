import java.util.*;

public class City {
    private Long id;
    private String name;
    private double latitude;
    private double longitude;
    private Set<ZipCode> zipCodes;

    public City(long id, String name, double latitude, double longitude,
                Collection<ZipCode> zipCodes){
        this.id = id;
        this.name = name;
        this.latitude = latitude;
        this.longitude = longitude;
        this.zipCodes = new HashSet<ZipCode>(zipCodes);
    }
    public City(String name, double latitude, double longitude, Collection<ZipCode> zipCodes){
        this.id = null;
        this.name = name;
        this.latitude = latitude;
        this.longitude = longitude;
        this.zipCodes = new HashSet<ZipCode>(zipCodes);
    }
    @Override
    public String toString(){
        String res= "city:{ id:"+id+" name:"+name+" latitude:"+latitude+
                " longitude:"+longitude+" zipCodes :[";
        for (ZipCode z: zipCodes) {
            res += z.getName()+" ";
        }
        return res+"]}";
    }
    @Override
    public int hashCode(){
        return Objects.hash(id == null ? 0 : id.longValue(),
                name, latitude, longitude);
    }
    @Override
    public boolean equals(Object o){
        if(!(o instanceof City)){ return false;}
        City other = (City) o;
        return Objects.equals(id, other.id);
    }
    public Long getId(){
        return id;
    }
    public void setId(long id){
        this.id = id;
    }
    public String getName(){
        return name;
    }
    public void setName(String name){
        this.name = name;
    }

    public double getLatitude() {
        return latitude;
    }
    public void setLatitude(double latitude){
        this.latitude = latitude;
    }
    public double getLongitude() {
        return longitude;
    }
    public void setLongitude(double longitude){
        this.longitude = longitude;
    }

    public Set<ZipCode> getZipCodes() {
        return zipCodes;
    }

    public void setZipCodes(Set<ZipCode> zipCodes) {
        this.zipCodes = zipCodes;
    }
}

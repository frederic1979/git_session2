import java.util.*;

public class ZipCode {
    private Long id;
    private String name;
    private Set<City> cities;

    public ZipCode(long id, String code, Collection<City> cities){
        this.id = id;
        this.name = code;
        this.cities = new HashSet<City>(cities);
    }
    public ZipCode(String code){
        this.id = null;
        this.name = code;
        this.cities = new HashSet<City>();
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
    public Set<City> getCities(){
        return new HashSet<>(cities);// TODO immutable
    }
    public void addCity(City city){
        cities.add(city);
    }
    public void removeCity(City city){
        cities.remove(city);
    }
    @Override
    public int hashCode(){
        return Objects.hash(id == null ? 0 : id.longValue(),
                name);
    }
    @Override
    public boolean equals(Object o){
        if(!(o instanceof ZipCode)){ return false;}
        ZipCode other = (ZipCode) o;
        return Objects.equals(id, other.id);
    }
    @Override
    public String toString(){
        String res="zipCode:{ id:"+id+" code:"+ name +" cities:[";
        for(City city : cities){
            res += city+" ";
        }
        return res+"]}";
    }
}

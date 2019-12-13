
import java.util.HashMap;
import java.util.Map;
import java.util.logging.Level;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

import model.City;
import model.Monument;
import model.User;


public class Main implements AutoCloseable {
    private static final String PERSISTENCE_UNIT_NAME = "jpa";
    private EntityManagerFactory factory;
    static {
        java.util.logging.Logger.getLogger("org.hibernate").setLevel(Level.OFF);
    }
    Main(){
        Map<String, String> env = System.getenv();
        Map<String, Object> configOverrides = new HashMap<String, Object>();
        for (String envName : env.keySet()) {
            if (envName.contains("JPA_DB_USER")) {
                configOverrides.put("javax.persistence.jdbc.user", env.get(envName));
            }
            if (envName.contains("JPA_DB_PASSWORD")) {
                configOverrides.put("javax.persistence.jdbc.password", env.get(envName));
            }
            if (envName.contains("JPA_DB_URL")) {
                configOverrides.put("javax.persistence.jdbc.url", env.get(envName));
            }		}
        factory = Persistence.createEntityManagerFactory(PERSISTENCE_UNIT_NAME, configOverrides);
    }

    public void close() {
        factory.close();
    }
    public City createCity() {
        EntityManager em= factory.createEntityManager();
        City city= new City("Atlantis", 0, 0.5);
        System.out.println(city);
        city= create(em, city);
        em.close();
        return city;
    }
    public City create(EntityManager em, City city) {
        em.getTransaction().begin();
        System.out.println("before: "+city);

        em.persist(city);
        System.out.println("after persist: "+city);

        em.getTransaction().commit();
        System.out.println("after commit: "+city);

        return city;
    }
    public City createCityAndUpdate() {
        EntityManager em= factory.createEntityManager();
        City city= new City("Paris", 0, 0.5);
        em.getTransaction().begin();
        em.persist(city);
        city.setLatitude(1000.);
        em.getTransaction().commit();// MAGIC HAPPENS HERE !
        em.close();
        return city;
    }
    public City readCity() {
        EntityManager em= factory.createEntityManager();
        City city= readCity(em, 5L);
        City city2= readCity(em, 1L);

        city.setLongitude(666.0);
        city.setName("Tutu");
        try {
            em.getTransaction().begin();
            em.getTransaction().commit();
            City city3= readCity(em, 5L);
            System.err.println(city3);
        }catch(Exception e){
            em.getTransaction().rollback();
        }
        em.close();
        return city;
    }
    public City readCity(EntityManager em, Long id)
    {
        return em.find(City.class, id);
    }
    public City updateCity() {
        EntityManager em= factory.createEntityManager();
        City res= update(em, new City(29L,"PaRiS", -1., -2.));
        em.close();
        return res;
    }
    public City update(EntityManager em, City city) {
        em.getTransaction().begin();
        city = em.merge(city);
        em.getTransaction().commit();
        return city;
    }
    public void deleteCity() {
        EntityManager em= factory.createEntityManager();
        em.getTransaction().begin();
        City c=readCity(em, 28L);
        System.err.println(c);
        em.remove(em.find(City.class,28L));
        em.getTransaction().commit();
    }
    public void delete(City city) {
        EntityManager em= factory.createEntityManager();
        em.getTransaction().begin();
        em.remove(em.merge(city));
        em.getTransaction().commit();
        em.close();
    }
    public Monument createMonument() {
        EntityManager em= factory.createEntityManager();
        em.getTransaction().begin();
        City city= readCity(em, 1L);
        Monument m= new Monument("Statue of Liberty", city);
        em.persist(m);
        em.getTransaction().commit();
        em.close();
        return m;
    }
    public Monument createMonument(EntityManager em, Monument m) {
        em.getTransaction().begin();
        em.persist(m);
        em.getTransaction().commit();
        return m;
    }

    public User createUser() {
        User user= new User("Superman");
        EntityManager em= factory.createEntityManager();
        user= create(em,user);
        user.addMonument(createMonument());
        user.addMonument(createMonument());
        em.getTransaction().begin();
        user= em.merge(user);
        em.getTransaction().commit();
        em.close();
        return user;
    }

    public User create(EntityManager em, User user) {
        em.getTransaction().begin();
        em.persist(user);
        em.getTransaction().commit();
        return user;
    }
    public static void main(String[] args) {
        try(Main app= new Main()){
            //app.deleteCity();
            app.createMonument();
            System.out.println(app.createCity());
//            System.out.println(app.createUser());
app.readCity();
        }catch(Exception e) {
            System.err.println(e);
        }



    }
}

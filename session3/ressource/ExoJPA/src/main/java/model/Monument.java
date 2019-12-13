package model;

import java.util.HashSet;
import java.util.Set;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToMany;
import javax.persistence.ManyToOne;
import javax.persistence.NamedQueries;
import javax.persistence.NamedQuery;
import javax.persistence.OneToOne;
import javax.persistence.Table;
import javax.persistence.Transient;

@Entity
@Table(name = "MONUMENTS")
public class Monument {

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    @Column(name = "ID")
    private Long id;

    @Column(name = "NAME", nullable = false, length = 100)
    private String name;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "fk_city")
    private City city;

    @ManyToMany(mappedBy="monuments")
    private Set<User> users = new HashSet<User>();

    public Monument(String name, City city) {
        super();
        this.name = name;
        this.city= city;
        System.err.println("monument in "+city);
    }

    public Monument() {
    }

    public Long getId() {
        return this.id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public City getCity() {
        return city;
    }

    public void setCity(City city) {
        this.city = city;
    }
    public Set<User> getUsers(){
        return users;
    }
    public void setUsers(Set<User> users){
        this.users= users;
    }
    @Override
    public String toString() {
        return "Monument [id=" + id + ", name=" + name
                + ", city=" + city + " visited by "+users.size()+"]";
    }
}

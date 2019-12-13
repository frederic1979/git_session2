package model;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.NamedQueries;
import javax.persistence.NamedQuery;
import javax.persistence.OneToMany;
import javax.persistence.Table;

import model.Monument;
import javax.persistence.OneToOne;

@Entity
@Table(name = "CITIES")
@NamedQueries({
        @NamedQuery(name = "City.findAll", query = " SELECT c FROM City c ORDER BY c.name "),
        @NamedQuery(name = "City.deleteById", query = " DELETE FROM City c WHERE c.id = :id") })
public class City {

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    @Column(name = "ID")
    private Long id;

    @Column(name = "NAME", nullable = false, length = 100)
    private String name;

    @Column(name = "LATITUDE")
    private Double latitude;

    @Column(name = "LONGITUDE")
    private Double longitude;

    @OneToMany(mappedBy = "city")//,  cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    private List<Monument> monuments = new ArrayList<Monument>();


	/*
	@OneToMany(mappedBy = "city", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
	private Set<Monument> monuments;
    */

    public City() {
    }
    public City(String name, double latitude, double longitude) {
        this.name=name;
        this.latitude=latitude;
        this.longitude=longitude;
    }
    public City(Long id, String name, double latitude, double longitude) {
        this.id= id;
        this.name= name;
        this.latitude= latitude;
        this.longitude= longitude;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String nom) {
        this.name = nom;
    }

    public Double getLongitude() {
        return this.longitude;
    }

    public void setLongitude(Double longitude) {
        this.longitude = longitude;
    }

    public Double getLatitude() {
        return this.latitude;
    }

    public void setLatitude(Double latitude) {
        this.latitude = latitude;
    }

    @Override
    public String toString() {
        return "City [id=" + id + ", name=" + name + ", latitude=" + latitude
                + ", longitude=" + longitude + "]";
    }

}

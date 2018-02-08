/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package project;

import java.util.ArrayList;
import java.util.Arrays;

/**
 *
 * @author Saumya
 */
public class Locdetails {
    
    Double[]t;
    String[] cities={"Ahmedabad","Aurangabad","Banglore","Bhopal","Delhi","Jaipur","Lucknow","Mumbai","Nagpur","Pune"};
     ArrayList<Double[]> latlo = new ArrayList<Double[]>();
    public Locdetails() {
         //ahmedabad
        t = new Double[]{23.0225, 72.5714};
        latlo.add(t);
         //aurangabad
        t = new Double[]{19.8762, 75.3433};
        latlo.add(t);
         //banglore
        t = new Double[]{12.9716,77.5946};
        latlo.add(t);
        //bhopal
        t = new Double[]{23.2599, 77.4126};
        latlo.add(t);
         //delhi
        t = new Double[]{28.6139, 77.2090};
        latlo.add(t);
        //jaipur
        t = new Double[]{26.9124, 75.7873};
        latlo.add(t);
         //lucknow
        t = new Double[]{26.8467, 80.9462};
        latlo.add(t);
        //mumbia
        t = new Double[]{19.0760, 72.8777};
        latlo.add(t);
         //nagpur
        t = new Double[]{21.1458, 79.0882};
        latlo.add(t);
        //pune
        t = new Double[]{18.5204, 73.8567};
        latlo.add(t);
    }
    
   public Double[] getloc(String c)
   {
       Double[] ret = new Double[2];
      int i= Arrays.asList(cities).indexOf(c);
       //System.out.println(i);
      ret = latlo.get(i);
      return ret;
   }
    
    
}

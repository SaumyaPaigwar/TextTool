/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package project;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import javax.naming.spi.DirStateFactory.Result;
import twitter4j.*;
import twitter4j.conf.ConfigurationBuilder;

/**
 *
 * @author Saumya
 */
public class temp {
    public static void main(String[] args) throws TwitterException, IOException {
         ConfigurationBuilder cb = new ConfigurationBuilder();
    cb.setDebugEnabled(true);
           int cnt =0;
          //String ct = args[0]; here catch the passed argument in ct, the type of ct should be string
           String ct = "Delhi"; // for example here is taken statically delhi
          cb.setOAuthConsumerKey("6H8JmrVZ0pxSugAepdDrnCUjq");
        cb.setOAuthConsumerSecret("dMR1JPIjdaugXh4n60D4DUQpElkPsC6S9FyJRWwedPuIdI2X7t");
        cb.setOAuthAccessToken("759368149-EFD5Tun7eLbJj4UCXYndJGRX5ooEhe2FRO8bgJKC");
        cb.setOAuthAccessTokenSecret("kcosMRYxpe5ciILXy54NOLoxEJqr9LS6SQNy9lH5KYMpA");
        
        
    
    TwitterFactory tf = new TwitterFactory(cb.build());
    Twitter twitter = tf.getInstance();
        //String[] cities = {"Nagpur","Mumbia","Pune"};
        //for(int i=0;i<cities.length;i++)
        //{    
            //System.out.println(ct);
            FileWriter fw = new FileWriter("D:/test.txt");
           BufferedWriter bw = new BufferedWriter(fw);
            Query q = new Query();
            q.setCount(1000);
            QueryResult result;
            //result = twitter.search(query);
            //double lat = 21.1458;
             //double lon = 79.0882;
           Locdetails g = new Locdetails();
           
           Double[]t = g.getloc(ct);
           //System.out.println(t[0]+" "+t[1]);
            double lat = t[0];
            double lon = t[1];
             double res = 10;
           String resUnit = "mi";
            result = twitter.search(q.geoCode(new GeoLocation(lat,lon),res, resUnit));  
            List<Status> tweets = result.getTweets();

            for (Status tweet : tweets) {
                String s = tweet.getText();
                //System.out.println(s.charAt(30)+" "+(int)s.charAt(30));
                //if((int) s.charAt(30)<2000)
                 System.out.println(s);
                bw.write(s);
                //ct++;
            }
            //System.out.println("Count is: "+ct);
            bw.close();
            removehttp();
        
    }
    public static void removehttp() throws IOException{
        FileWriter fw = new FileWriter("D:/text1.txt");
        BufferedWriter bw = new BufferedWriter(fw);
        
        Scanner sc=new Scanner(new FileReader("D:/test.txt"));
        String[] sp;
        while(sc.hasNext())
        {
            String a=sc.nextLine();
            if(a.contains("http"))
            {
                //System.out.println("yes");
                sp=a.split(" ");
                for(String s:sp)
                {
                    //System.out.println(s);
                    if((!s.contains("http")))
                        bw.append(s+" ");
                }
                bw.append('\n');
            }
            else
                bw.append(a+'\n');
            
        }
        bw.close();
        removehindiattherate();
    }
    
    public static void removehindiattherate() throws FileNotFoundException, IOException
    {
         String s =null;
        FileReader fr = new FileReader("D:/text1.txt");
        BufferedReader br = new BufferedReader(fr);
        FileWriter fw = new FileWriter("E:/op1.txt");
        BufferedWriter bw = new BufferedWriter(fw);
        
        while((s=br.readLine())!=null)
        {
            //System.out.println(s);
            String[] te = s.split(" ");
            for(int i=0;i<te.length;i++)
            {
                if(check(te[i]))
                {
                    //System.out.println(te[i]);
                    bw.write(te[i]+" ");
                }    
            }
        }
        bw.close();
    }
    public static boolean check(String t)
    {
        
        int i;
        boolean b = false;
        for(i=0;i<t.length();i++)
            if(t.charAt(i)>127)
                break;
        if(i==t.length())
            b=true;
        //if(t.charAt(0)==64)
            //b=false;
        return b;
    }
    }
    
    



// Java program to illustrate
// selecting from Database
import java.sql.*;

public class select {
  public static void main(String args[])
    {
        try
        {
            //Replace the driver if you have any other than oracle
            Class.forName("oracle.jdbc.driver.OracleDriver");

            // Replace login and password with your own database login and password
            Connection con = DriverManager.getConnection("
                    jdbc:oracle:thin:@localhost:1521:orcl", "login", "password");
            Statement stmt = con.createStatement();
             
            // SELECT query
            String q1 = "select companyname,address,city,region,postalcode,country FROM nothwind_customer";
            ResultSet rs = stmt.executeQuery(q1);
          // printing heading
            System.out.println("CompanyName,Address,City,Region,Postalcode,Country ");
            // loop through data
            while (rs.next())
            {
              if(rs.getString(1)==null){
                System.out.println("n/a")
              }
              else{
                System.out.println(rs.getString(1));
              }
              if(rs.getString(2)==null){
                System.out.println("n/a")
              }
              else{
                System.out.println(rs.getString(2));
              }
              if(rs.getString(3)==null){
                System.out.println("n/a")
              }
              else{
                System.out.println(rs.getString(3));
              }
              if(rs.getString(4)==null){
                System.out.println("n/a")
              }
              else{
                System.out.println(rs.getString(4));
              }
              if(rs.getString(5)==null){
                System.out.println("n/a")
              }
              else{
                System.out.println(rs.getString(5));
              }
              if(rs.getString(6)==null){
                System.out.println("n/a")
              }
              else{
                System.out.println(rs.getString(6));
              }
               

            }
          //  closing connection
            con.close();
        }
        catch(Exception e)
        {
            System.out.println(e);
        }
    }
}
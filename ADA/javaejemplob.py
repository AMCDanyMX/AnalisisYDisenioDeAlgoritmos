import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class feeding {
    public static void main(String[] args) throws IOException {
        int cubo, fuerza, fin;
        int n=0, res=0;
        String ser[];
        BufferedReader entrada=new BufferedReader(new InputStreamReader(System.in));
        String entra=entrada.readLine();
        ser=entra.split(" ");
        cubo=Integer.parseInt(ser[0]);
        fuerza=Integer.parseInt(ser[1]);
        String cubo2[]=new String[cubo];
        entra=entrada.readLine();
        cubo2=entra.split(" ");
            for (int i = 0; i < cubo; i++) {
                n=Integer.parseInt(cubo2[i]);
                res=res+n;
            }
        fin=res/fuerza;
        if(res%fuerza!=0){
            fin++;
        }
        System.out.println(fin);
    }
}
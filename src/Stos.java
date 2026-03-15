import java.util.Stack;

public class Stos {


    public static void main(String[] args) {
    Stack stos = new Stack();
        stos.add("nowy cos");
        stos.add(2);
        stos.add(21.37);
        System.out.println(stos);
        System.out.println(stos.pop());
        System.out.println(stos);
        //widac elegancko ze pop pozbywa sie ostatniego elementu
    }
}

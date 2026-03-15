import java.util.Collection;
import java.util.Collections;
import java.util.PriorityQueue;

public class Sterta {
    public static void main(String[] args) {
        PriorityQueue sterta = new PriorityQueue();
        // PriorityQueue - sterta eleangcka, sortuje od min -> max, jesli chcemy
        // na odwrot (od najwiekszego to piszemy:
        // PriorityQueue sterta = new PriorityQueue(Collections.reverseOrder());
        sterta.add(18);
        sterta.add(3);
        sterta.add(5);
        sterta.add(13);
        sterta.add(8);
        System.out.println("wynik = ");
        while (!sterta.isEmpty()) {
            System.out.println(sterta.poll());
        }
        // wynik = 3 5 8 13 18
        // to pokazuje ze w tej naszej cdunej queueueue najpierw tworzy sie porzadek przed tym poll'owaniem :D
    }
}

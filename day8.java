import java.io.IOException;
import java.util.*;
import java.io.File;

record Tuple(int x, int y, int z) {}

public class day8 {

    static double dist(Tuple a, Tuple b) {
        int dx = a.x() - b.x();
        int dy = a.y() - b.y();
        int dz = a.z() - b.z();
        return Math.sqrt(dx*dx + dy*dy + dz*dz);
    }

    public static void crearCircuitos(HashMap<Tuple, Integer> t) {
        int circuit = 0;

        while (t.containsValue(-1)) {
            Tuple bestA = null;
            Tuple bestB = null;
            double bestD = Double.MAX_VALUE;

            for (Tuple a : t.keySet()) {
                for (Tuple b : t.keySet()) {
                    if (a == b) continue;
                    int ca = t.get(a);
                    int cb = t.get(b);
                    if (ca != -1 && cb != -1 && ca == cb) continue;
                    double d = dist(a, b);
                    if (d < bestD) {
                        bestD = d;
                        bestA = a;
                        bestB = b;
                    }
                }
            }

            int ca = t.get(bestA);
            int cb = t.get(bestB);

            if (ca == -1 && cb == -1) {
                t.put(bestA, circuit);
                t.put(bestB, circuit);
                circuit++;
            } else if (ca != -1 && cb == -1) {
                t.put(bestB, ca);
            } else if (ca == -1 && cb != -1) {
                t.put(bestA, cb);
            } else if (ca != cb) {
                for (Tuple k : t.keySet()) {
                    if (t.get(k) == cb) t.put(k, ca);
                }
            }
            
        }
    }

    public static void main(String[] args) throws IOException {
        HashMap<Tuple, Integer> table = new HashMap<>();
        Scanner scanner = new Scanner(new File("input8.txt"));

        while (scanner.hasNextLine()) {
            String[] line = scanner.nextLine().split(",");
            Tuple tuple = new Tuple(Integer.parseInt(line[0]), Integer.parseInt(line[1]), Integer.parseInt(line[2]));
            table.put(tuple, -1);
        }
        scanner.close();

        crearCircuitos(table);
        //System.out.println(table);
    }
}

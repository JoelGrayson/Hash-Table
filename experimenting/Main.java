import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        HashMap<String, Integer> map=new HashMap<String, Integer>();
        map.put("hi", 32);
        map.put("foo", 200);
        System.out.println(map);
        System.out.println(map.get("hi"));
        map.remove("hi");
        System.out.println(map);
    }
}
